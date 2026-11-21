# showcase

Queria のショーケース記事の原稿です。記事は `queria` アカウントのレポートとして https://queria.io/reports/queria/{slug} で公開しています。

- `content/showcase/{slug}/index.md`: 記事の本文。形式は Queria のレポートの Markdown（[レポートのドキュメント](https://docs.queria.io/reports)）です。本文の図は同じディレクトリに置き、`![説明](source.png)` と名前だけで参照します
- `public/og/{slug}.webp`: OGP 画像。一覧のカードは、公開時に Queria がこの画像を縮小して作ります

図表の結果は、Queria がページの保存のあとに SQL を実行して作ります。

## 公開

main へのマージで `.github/workflows/publish.yml` が、変わった記事だけを公開の CLI（PyPI の `queria`）の `queria report create` / `edit` でページに保存します。本文の図と `public/og/{slug}.webp` は、CLI が本文より先に送ります。新しい記事は、保存のあとに `.github/workflows/social.yml` が `.github/scripts/post_social.py` で X と Bluesky に投稿します。手で保存し直すときは Publish を手動実行します（記事の欄を空にすると全件。手動実行では投稿しません）。

Queria への書き込みには、CLI が GitHub Actions の OIDC で取得する 1 時間有効のトークンを使います。`queria` アカウントの設定の「GitHub Actions」に、リポジトリ `queria-io/showcase`・ワークフロー `publish.yml`・ブランチ `main` を登録してあります。

SNS への投稿には、secret の `X_API_KEY`・`X_API_SECRET`・`X_ACCESS_TOKEN`・`X_ACCESS_TOKEN_SECRET`・`BLUESKY_IDENTIFIER`・`BLUESKY_APP_PASSWORD`・`DISCORD_WEBHOOK_POST` を使います。
