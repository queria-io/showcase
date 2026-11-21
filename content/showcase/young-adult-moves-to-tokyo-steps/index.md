---
title: 20代がいちばん多く引っ越す先を町から順にたどると、全国の市町村の9割超が5回以内に東京23区へ行き着きます
description: 2025年の住民基本台帳人口移動報告で、市区町村ごとに20代の転出者が最も多い転出先を集計しました。東京23区が最も多い転出先になっている市区町村は279で、最も多い転出先を順にたどると、1,508市区町村の95.8%が5回以内に東京23区に着きます。
publishedAt: 2026-11-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口移動
  - 若者
  - 地図
  - 移住・定住
datasets:
  - queria/e_stat
  - queria/nlftp
  - queria/address_br
sources:
  - title: 住民基本台帳人口移動報告
    url: https://www.stat.go.jp/data/idou/index.html
    publisher: 総務省統計局
  - title: 国土数値情報（行政区域データ）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2025.html
    publisher: 国土交通省
  - title: アドレス・ベース・レジストリ
    url: https://www.digital.go.jp/policies/base_registry_address
    publisher: デジタル庁
agentHint: 自分の県の市町村ごとに、20代の転出先の上位3位までと人数を2025年について出して、1位が県庁所在地の町と、県外の都市の町に分けて
socialAnnounce: |-
  市区町村ごとに「20代がいちばん多く引っ越した先」を線で結びました（2025年）。

  町から県庁所在地へ、県庁所在地から札幌・仙台・名古屋・大阪・福岡へ、そこから東京23区へ。1位の行き先をたどると、全国の9割超の市町村が5回以内に東京23区へ行き着きます。
  Queriaは行政のオープンデータを整えて公開しています
---

2025年に20代の転出者が最も多かった転出先が東京23区である市区町村は、1,509のうち279でした。多くの市町村では、最も多い転出先は県庁所在地や近くの市です。最も多い転出先を順にたどると、町から県庁所在地、札幌市・仙台市・名古屋市・大阪市・福岡市などの地方の中心都市を経て、1,508市区町村（東京23区を除く）の95.8%が5回以内に東京23区に着きます。

[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)は、住民票を移した人を、前の住所地と新しい住所地の組み合わせで集計しています。市区町村ごとに、20〜29歳の転出者が最も多かった転出先（以下「1位の転出先」）を選び、矢印で結びました。地方の市町村で若者の定住や UIJ ターンの施策を検討するときに、自分の町の20代がどこへ転出しているかを確認する材料になります。下の地図は、そのうちほかの市区町村の1位の転出先にもなっている232の都市だけを描いたものです。矢印の色は、その1位の転出先へ移った20代の人数です。

```map
type: map
caption: ほかの市区町村の1位の転出先になっている都市から、その都市の1位の転出先への矢印（2025年、20代）
layers:
  - from: hub_flows
    flow: city
    origin: origin_code
    destination: destination_code
    color: movers
    label: route
    name: 移った20代（人）
lng: 137.5
lat: 38.3
zoom: 4.0
```

矢印は、市から県庁所在地へ、県庁所在地から札幌市・仙台市・名古屋市・大阪市・福岡市などの地方の中心都市へ向かい、その先は東京23区へ向かっています。北海道の矢印は札幌市に集まり、九州では熊本市・大分市・宮崎市・鹿児島市の矢印が福岡市へ向かいます。

## 東京23区は279の市区町村の1位の転出先で、そのうち245は東京都の外

使ったのは、総務省統計局の住民基本台帳人口移動報告のうち、転出元の市区町村ごとに転出先の市区町村別の人数を年齢10歳階級で集計した表（`municipality_migration_destination`）です。2025年1〜12月の移動で、年齢は移動した時点の20〜29歳（`age_code` = `503`）、外国人を含む移動者の数です。市区町村の単位は、政令指定都市を1つの市、東京都の特別区部を「東京23区」として1つにまとめています。1位の転出先が5人未満の町村と、1位が同数で2つ以上ある町村は除き、残る1,509の市区町村を集計しています。

1位の転出先になった回数を都市ごとに集計すると、東京23区が279の市区町村で1位でした。続く札幌市・大阪市・名古屋市・福岡市・仙台市は、それぞれ数十の市区町村の1位の転出先です。

```chart
{
  "height": 420,
  "data": { "name": "dest_rank" },
  "mark": "bar",
  "encoding": {
    "y": {
      "field": "destination_name",
      "type": "nominal",
      "sort": { "field": "total", "op": "max", "order": "descending" },
      "title": null
    },
    "x": {
      "field": "n",
      "type": "quantitative",
      "stack": "zero",
      "title": "1位の転出先にしている市区町村の数"
    },
    "color": {
      "field": "kind",
      "type": "nominal",
      "title": null,
      "scale": {
        "domain": ["同じ都道府県の市区町村", "ほかの都道府県の市区町村"],
        "range": ["#93c5fd", "#ef4444"]
      }
    },
    "order": { "field": "kind_order", "type": "quantitative" },
    "tooltip": [
      { "field": "destination_name", "title": "転出先" },
      { "field": "kind", "title": "転出元" },
      { "field": "n", "title": "市区町村の数", "format": "," }
    ]
  }
}
```

色は、転出元がその都市と同じ都道府県か、ほかの都道府県かを表しています。東京23区を1位にしている279の市区町村のうち、東京都の外にあるものが245です。大阪市・名古屋市・福岡市・仙台市も、府県の外の市町村から1位に選ばれています。札幌市の108と鹿児島市の27は、すべて同じ道県の中の市町村です。

## 九州の町村の1位の転出先は県庁所在地や近くの市で、その先は福岡市

福岡・佐賀・長崎・熊本・大分・宮崎・鹿児島の7県の市区町村について、すべての1位の転出先を矢印で描きました。町村の矢印は、福岡市・熊本市・鹿児島市・宮崎市・大分市・長崎市などの県庁所在地や近くの市に向かい、それらの都市からの矢印は福岡市へ向かっています。

```map
type: map
caption: 九州7県の市区町村から1位の転出先への矢印（2025年、20代）
layers:
  - from: kyushu_flows
    flow: city
    origin: origin_code
    destination: destination_code
    color: movers
    label: route
    name: 移った20代（人）
lng: 130.8
lat: 32.6
zoom: 6.3
```

## 1位の転出先をたどると、95.8%の市区町村が5回以内に東京23区に着く

1位の転出先の都市にも、それぞれ1位の転出先があります。たとえば鹿児島県の奄美市の1位は鹿児島市、鹿児島市の1位は福岡市、福岡市の1位は東京23区です。このように1位の転出先を順にたどり、何回目で東京23区に着くかで市区町村を色分けしました。

```map
type: map
caption: 1位の転出先をたどって東京23区に着くまでの回数（2025年、20代）
layers:
  - from: steps_map
    area: city
    code: lg_code
    color: steps
    label: path
    name: 東京23区までの回数
```

```sql
SELECT steps AS "東京23区までの回数", count(*) AS "市区町村の数", arg_max(path, movers) AS "たどった例（20代の転出が1位の転出先へ最も多い市区町村）"
FROM steps
GROUP BY steps
ORDER BY min(steps_order)
```

1,508の市区町村（東京23区を除く）のうち、1回目で東京23区に着くのが279、2回目が761、3回目が346です。5回以内に着く市区町村は1,444で、全体の95.8%にあたります。北海道は札幌市を経て2回目、九州南部の町は県庁所在地と福岡市を経て3〜4回目で着きます。

東京23区に着かない64の市区町村では、たどった先の2つの都市が互いを1位の転出先にしています。島根県の松江市と出雲市、岡山県の岡山市と倉敷市、山口県の周南市と下松市、沖縄県の沖縄市とうるま市などです。これらの地域では、20代の転出が県内の2つの都市の間で最も多くなっています。

## 東京23区を1位の転出先にする市町村が半数を超えるのは、埼玉県・千葉県・茨城県・山梨県

都道府県ごとに、市区町村の1位の転出先が同じ都道府県の中か、東京23区か、ほかの都道府県の都市かを集計しました。1位の転出先が県内に多い県と、県外に多い県に分かれます。

```chart
{
  "height": 900,
  "data": { "name": "pref_mix" },
  "mark": "bar",
  "encoding": {
    "y": {
      "field": "pref_name",
      "type": "nominal",
      "sort": { "field": "pref_code", "order": "ascending" },
      "title": null
    },
    "x": {
      "field": "n",
      "type": "quantitative",
      "stack": "normalize",
      "title": "市区町村の割合",
      "axis": { "format": "%" }
    },
    "color": {
      "field": "kind",
      "type": "nominal",
      "title": null,
      "scale": {
        "domain": ["同じ都道府県の市区町村", "東京23区", "ほかの都道府県の市区町村"],
        "range": ["#93c5fd", "#ef4444", "#f97316"]
      }
    },
    "order": { "field": "kind_order", "type": "quantitative" },
    "tooltip": [
      { "field": "pref_name", "title": "都道府県" },
      { "field": "kind", "title": "1位の転出先" },
      { "field": "n", "title": "市区町村の数", "format": "," }
    ]
  }
}
```

東京都を除くと、東京23区を1位にする市町村が半数を超えるのは埼玉県（60のうち47）・千葉県（53のうち39）・茨城県（43のうち22）・山梨県（24のうち14）です。奈良県は27のうち22の市町村が県外の都市を1位にしていて、岐阜県・三重県・兵庫県・和歌山県・佐賀県・長崎県でも県外の都市を1位にする市町村が3割を超えます。北海道（147のうち143）・宮城県・愛知県・広島県・熊本県・高知県などは、ほとんどの市町村が県の中の都市を1位にしています。

## 若者の定住施策での使い方

- 自分の町の1位の転出先が県庁所在地か、県外の中心都市か、東京23区かを確認し、若者向けの情報発信や UIJ ターンの相談会を開く場所を決める材料にできます
- 1位の転出先が同じ近隣の市町村を並べ、同じ都市へ転出している町どうしで、広域の定住施策や合同の採用説明会を検討できます
- 県庁所在地や中心都市の担当者は、自分の市を1位の転出先にしている市町村の数と、自分の市の1位の転出先を並べて、周りの市町村から20代が転入しているか、ほかの都市へ転出しているかを確認できます

## データの出典

本記事は総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)の2025年の市区町村別の移動者数を、2026-11-12 時点で集計しています。地図の矢印の端は、デジタル庁の[アドレス・ベース・レジストリ](https://www.digital.go.jp/policies/base_registry_address)の市区町村の代表点（役所の位置）で、東京23区は23区の代表点の平均です。東京23区に着くまでの回数の地図は、国土交通省の[国土数値情報（行政区域データ）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2025.html)の市区町村の境界で色分けしています。

Queria は、住民基本台帳人口移動報告を、転出元と転出先の組み合わせごとに年齢・性別で取得できるテーブルにし、列の意味をメタデータに記載して公開しています。本記事で使った[市区町村別の転出先のテーブル](/datasets/queria/e_stat/migration/municipality_migration_destination)から、自分の町の20代が2位・3位にどこへ出ているか、年によって変わっているかを確認できます。

```sql id=first_dest
-- 市区町村ごとの20代の1位の転出先。1位が5人未満と、1位が同数で2つ以上あるものは除く
SELECT
  origin_code,
  replace(origin_name, '東京都特別区部', '東京23区') AS origin_name,
  origin_parent,
  destination_code,
  replace(destination_name, '東京都特別区部', '東京23区') AS destination_name,
  destination_parent,
  movers
FROM e_stat.migration.municipality_migration_destination
WHERE year = 2025
  AND sex_code = '0'
  AND age_code = '503'
  AND origin_level = 'municipality'
  AND destination_level = 'municipality'
  AND destination_code <> origin_code
QUALIFY rank() OVER (PARTITION BY origin_code ORDER BY movers DESC) = 1
  AND count(*) OVER (PARTITION BY origin_code, movers) = 1
  AND movers >= 5
```

```sql id=prefs
SELECT DISTINCT destination_code AS pref_code, destination_name AS pref_name
FROM e_stat.migration.municipality_migration_destination
WHERE year = 2025 AND sex_code = '0' AND age_code = '503' AND destination_level = 'prefecture'
```

```sql id=dest_rank
WITH counted AS (
  SELECT
    destination_name,
    CASE WHEN origin_parent = destination_parent THEN '同じ都道府県の市区町村' ELSE 'ほかの都道府県の市区町村' END AS kind,
    CASE WHEN origin_parent = destination_parent THEN 1 ELSE 2 END AS kind_order,
    count(*) AS n
  FROM first_dest
  GROUP BY ALL
), totals AS (
  SELECT destination_name, sum(n) AS total FROM counted GROUP BY ALL
)
SELECT c.*, t.total
FROM counted c
JOIN totals t USING (destination_name)
WHERE t.destination_name IN (
  SELECT destination_name FROM totals ORDER BY total DESC, destination_name LIMIT 15
)
ORDER BY t.total DESC, c.kind_order
```

```sql id=hub_flows
-- ほかの市区町村の1位の転出先になっている都市から、その都市の1位の転出先へ
SELECT origin_code, destination_code, origin_name || ' → ' || destination_name || '（' || movers || '人）' AS route, movers
FROM first_dest
WHERE origin_code IN (SELECT destination_code FROM first_dest)
```

```sql id=kyushu_flows
SELECT origin_code, destination_code, origin_name || ' → ' || destination_name || '（' || movers || '人）' AS route, movers
FROM first_dest
WHERE left(origin_code, 2) BETWEEN '40' AND '46'
```

```sql id=steps
-- 東京23区に着くか、通った市区町村に戻るまで1位の転出先をたどる
WITH RECURSIVE walk(origin_code, cur, n, path, seen) AS (
  SELECT origin_code, destination_code, 1, origin_name || ' → ' || destination_name, [origin_code]
  FROM first_dest
  WHERE origin_code <> '13100'
  UNION ALL
  SELECT w.origin_code, f.destination_code, w.n + 1, w.path || ' → ' || f.destination_name, list_append(w.seen, w.cur)
  FROM walk w
  JOIN first_dest f ON f.origin_code = w.cur
  WHERE w.cur <> '13100' AND NOT list_contains(w.seen, w.cur)
), ends AS (
  SELECT origin_code, arg_max(path, n) AS path, arg_max(cur, n) = '13100' AS reached, max(n) AS n
  FROM walk
  GROUP BY origin_code
)
SELECT
  f.origin_code,
  CASE
    WHEN NOT e.reached THEN '着かない'
    WHEN e.n >= 4 THEN '4回以上'
    ELSE e.n || '回目'
  END AS steps,
  CASE WHEN e.reached THEN e.n ELSE 99 END AS steps_order,
  f.movers,
  CASE WHEN e.reached THEN e.path ELSE e.path || '（以後くり返し）' END AS path
FROM first_dest f
JOIN ends e USING (origin_code)
WHERE f.origin_code <> '13100'
```

```sql id=steps_map
-- 政令指定都市は区ごとの境界で塗る
WITH wards AS (
  SELECT DISTINCT origin_code AS code, origin_parent AS city
  FROM e_stat.migration.municipality_migration_destination
  WHERE year = 2025 AND origin_level = 'ward' AND origin_parent <> '13100'
)
SELECT coalesce(w.code, s.origin_code) AS lg_code, s.steps, s.path
FROM steps s
LEFT JOIN wards w ON w.city = s.origin_code
UNION ALL
SELECT code AS lg_code, '東京23区' AS steps, '東京23区' AS path
FROM (
  SELECT DISTINCT origin_code AS code
  FROM e_stat.migration.municipality_migration_destination
  WHERE year = 2025 AND origin_level = 'ward' AND origin_parent = '13100'
)
```

```sql id=pref_mix
SELECT
  p.pref_code,
  p.pref_name,
  CASE
    WHEN f.destination_code = '13100' THEN '東京23区'
    WHEN f.origin_parent = f.destination_parent THEN '同じ都道府県の市区町村'
    ELSE 'ほかの都道府県の市区町村'
  END AS kind,
  CASE
    WHEN f.destination_code = '13100' THEN 2
    WHEN f.origin_parent = f.destination_parent THEN 1
    ELSE 3
  END AS kind_order,
  count(*) AS n
FROM first_dest f
JOIN prefs p ON p.pref_code = f.origin_parent
GROUP BY ALL
ORDER BY p.pref_code, kind_order
```
