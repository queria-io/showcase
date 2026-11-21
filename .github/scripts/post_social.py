"""Announce a published article on X and Bluesky.

Usage: python post_social.py [--dry-run] <slug>

The text is the article's `socialAnnounce` front matter and its URL. The link
card uses the OGP image of the published report, read from its page.

Environment: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET,
BLUESKY_IDENTIFIER, BLUESKY_APP_PASSWORD. Prints `X: <url>` and
`Bluesky: <url>` for each post made; exits 1 if either one failed.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import html
import json
import os
import re
import secrets
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

SITE = "https://queria.io"
OWNER = "queria"
BLUESKY_API = "https://bsky.social/xrpc"
OG_WAIT_S = 10 * 60
URL_RE = re.compile(r"https?://\S+")
#: X counts a code point in these ranges as 1 and any other as 2 (twitter-text's
#: weighted length). Arrows, ellipses and circled digits fall outside them.
X_LIGHT_RANGES = ((0x0000, 0x10FF), (0x2000, 0x200D), (0x2010, 0x201F), (0x2032, 0x2037))
X_MAX = 280
#: Bluesky's limit is 300 graphemes; code points are never fewer, so this errs on the safe side.
BLUESKY_MAX = 300
#: What a failed request can raise: URLError and HTTPError are OSErrors, and so are the
#: TimeoutError and RemoteDisconnected that urlopen and read() let through unwrapped.
#: ValueError covers a reply that is not the JSON we expect.
REQUEST_ERRORS = (OSError, ValueError, KeyError)


def front_matter(slug: str) -> dict:
    text = Path("content/showcase", slug, "index.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(match.group(1)) if match else {}


def request(url: str, *, method: str = "GET", headers: dict | None = None, data: bytes | None = None):
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    return urllib.request.urlopen(req, timeout=60)


def og_image_url(article_url: str) -> str | None:
    """The page's og:image, once the published report has one."""
    deadline = time.time() + OG_WAIT_S
    while True:
        try:
            with request(article_url) as res:
                page = res.read().decode("utf-8", "replace")
            match = re.search(r'<meta property="og:image" content="([^"]+)"', page)
            if match:
                return html.unescape(match.group(1))
        except REQUEST_ERRORS as exc:
            print(f"page not ready ({exc})", file=sys.stderr)
        if time.time() > deadline:
            print("no OGP image after 10 minutes; posting without one", file=sys.stderr)
            return None
        time.sleep(15)


# --- X ---------------------------------------------------------------------


def x_length(text: str) -> int:
    """X's weighted length: a URL counts 23, a code point in X_LIGHT_RANGES 1, the rest 2."""

    def chars(s: str) -> int:
        return sum(1 if any(lo <= ord(c) <= hi for lo, hi in X_LIGHT_RANGES) else 2 for c in s)

    return chars(URL_RE.sub("", text)) + 23 * len(URL_RE.findall(text))


def _pct(s: str) -> str:
    return urllib.parse.quote(s, safe="~-._")


def post_x(text: str) -> str:
    url = "https://api.x.com/2/tweets"
    oauth = {
        "oauth_consumer_key": os.environ["X_API_KEY"],
        "oauth_nonce": secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_token": os.environ["X_ACCESS_TOKEN"],
        "oauth_version": "1.0",
    }
    params = "&".join(f"{_pct(k)}={_pct(v)}" for k, v in sorted(oauth.items()))
    base = "&".join(["POST", _pct(url), _pct(params)])
    key = f"{_pct(os.environ['X_API_SECRET'])}&{_pct(os.environ['X_ACCESS_TOKEN_SECRET'])}"
    oauth["oauth_signature"] = base64.b64encode(
        hmac.new(key.encode(), base.encode(), hashlib.sha1).digest()
    ).decode()
    header = "OAuth " + ", ".join(f'{_pct(k)}="{_pct(v)}"' for k, v in sorted(oauth.items()))
    body = json.dumps({"text": text}).encode()
    with request(url, method="POST", data=body, headers={"Authorization": header, "Content-Type": "application/json"}) as res:
        return f"https://x.com/i/status/{json.load(res)['data']['id']}"


# --- Bluesky ---------------------------------------------------------------


def _bsky(path: str, payload: dict | bytes, *, jwt: str | None = None, content_type: str = "application/json") -> dict:
    data = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
    headers = {"Content-Type": content_type, **({"Authorization": f"Bearer {jwt}"} if jwt else {})}
    with request(f"{BLUESKY_API}/{path}", method="POST", data=data, headers=headers) as res:
        return json.load(res)


def post_bluesky(text: str, article_url: str, title: str, description: str, og: str | None) -> str:
    identifier = os.environ["BLUESKY_IDENTIFIER"]
    session = _bsky(
        "com.atproto.server.createSession",
        {"identifier": identifier, "password": os.environ["BLUESKY_APP_PASSWORD"]},
    )
    jwt = session["accessJwt"]
    facets = []
    for match in URL_RE.finditer(text):
        start = len(text[: match.start()].encode())
        facets.append(
            {
                "index": {"byteStart": start, "byteEnd": start + len(match.group().encode())},
                "features": [{"$type": "app.bsky.richtext.facet#link", "uri": match.group()}],
            }
        )
    external = {"uri": article_url, "title": title, "description": description}
    if og:
        # The card is worth having but not worth the post: without the image, post without it
        try:
            with request(og) as res:
                image, content_type = res.read(), res.headers.get_content_type()
            blob = _bsky("com.atproto.repo.uploadBlob", image, jwt=jwt, content_type=content_type)
            external["thumb"] = blob["blob"]
        except REQUEST_ERRORS as exc:
            print(f"OGP image not attached ({exc})", file=sys.stderr)
    record = {
        "$type": "app.bsky.feed.post",
        "text": text,
        "facets": facets,
        "embed": {"$type": "app.bsky.embed.external", "external": external},
        "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    created = _bsky(
        "com.atproto.repo.createRecord",
        {"repo": session["did"], "collection": "app.bsky.feed.post", "record": record},
        jwt=jwt,
    )
    return f"https://bsky.app/profile/{identifier}/post/{created['uri'].rsplit('/', 1)[1]}"


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    slugs = [a for a in argv if not a.startswith("--")]
    if len(slugs) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    slug = slugs[0]
    meta = front_matter(slug)
    announce = (meta.get("socialAnnounce") or "").strip()
    if not announce:
        print(f"{slug}: no socialAnnounce, skipping")
        return 0
    article_url = f"{SITE}/reports/{OWNER}/{slug}"
    text = f"📊 {announce}\n{article_url}"
    # Each limit stops only its own post: a text too long for X still goes to Bluesky
    x_ok = x_length(text) <= X_MAX
    bluesky_ok = len(text) <= BLUESKY_MAX
    failed = False
    if not x_ok:
        print(f"::error::X への投稿に失敗: {slug} ({X_MAX} の重み付き文字数を超える: {x_length(text)})")
        failed = True
    if not bluesky_ok:
        print(f"::error::Bluesky への投稿に失敗: {slug} ({BLUESKY_MAX} 文字を超える: {len(text)})")
        failed = True
    if dry_run:
        print(text)
        return 1 if failed else 0
    if not (x_ok or bluesky_ok):
        return 1

    og = og_image_url(article_url)
    if x_ok:
        try:
            print(f"X: {post_x(text)}")
        except REQUEST_ERRORS as exc:
            print(f"::error::X への投稿に失敗: {slug} ({exc})")
            failed = True
    if bluesky_ok:
        try:
            title = meta.get("title") or ""
            description = meta.get("description") or ""
            print(f"Bluesky: {post_bluesky(text, article_url, title, description, og)}")
        except REQUEST_ERRORS as exc:
            print(f"::error::Bluesky への投稿に失敗: {slug} ({exc})")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
