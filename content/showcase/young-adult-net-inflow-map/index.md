---
title: 20代が転入超過になったのは1,876市区町村のうち338で、東京23区と大阪・名古屋・福岡の都心の区に集まる
description: 2025年の住民基本台帳人口移動報告で、20代の日本人の転入超過数を市区町村ごとに20代の人口1,000人あたりで比較しました。転入超過は1,876市区町村のうち338です。転入超過になった町村は、20〜24歳では85、25〜29歳では258でした。
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
  - queria/ipss
sources:
  - title: 住民基本台帳人口移動報告
    url: https://www.stat.go.jp/data/idou/index.html
    publisher: 総務省統計局
  - title: 日本の地域別将来推計人口（令和5年推計）
    url: https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp
    publisher: 国立社会保障・人口問題研究所
agentHint: 自分の県の市町村ごとに、20〜24歳と25〜29歳の日本人の転入超過数を2025年について出して、2020年の20代の人口1,000人あたりの値で並べて
socialAnnounce: |-
  20代が増えた町・減った町を地図に塗りました（2025年、日本人）。

  転入超過になったのは1,876市区町村のうち338だけです。上位は名古屋市中区・東京都中央区・墨田区・台東区・大阪市東成区。20〜24歳は都市の中心へ、25〜29歳は周りの町へ移ります。
  Queriaは行政のオープンデータを整えて公開しています
---

2025年に20代の日本人が転入超過になったのは、1,876市区町村のうち338でした。上位には東京都の中央区・墨田区・台東区と、名古屋市・大阪市の都心の区が並び、東京23区は23区すべてが転入超過です。年齢別では、20〜24歳で転入超過になった町村は85でしたが、25〜29歳では258に増えます。

若者の定住や UIJ ターンの施策を検討するときは、自分の町から20代がどのくらい出ていっているかを、全国の市区町村と比較して把握する必要があります。[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)の2025年の年齢別の移動者数から、市区町村ごとに20〜29歳の日本人の転入超過数（転入者数 − 転出者数）を求め、2020年の20代の人口1,000人あたりの値で地図にしました。青い市区町村は20代が転入超過、赤い市区町村は転出超過です。

```map
type: map
caption: 20代の日本人の転入超過数（2025年、2020年の20代の人口1,000人あたり）
layers:
  - from: rate_map
    area: city
    code: area
    color: rate
    label: label
    name: 20代1,000人あたりの転入超過数
    ends: [転出超過, 転入超過]
lng: 137.5
lat: 37.5
zoom: 4.3
```

青いのは、東京23区と、大阪市・名古屋市・福岡市・神戸市などの都心の区が中心です。それ以外の大半の市町村は赤く、20代が出ていく側です。北海道や離島などに濃い青の町村もありますが、20代の人口が数百人の町村では、数十人の移動で1,000人あたりの値が大きく変わります。

## 20代が転入超過になったのは、1,876市区町村のうち338

使ったのは、住民基本台帳人口移動報告の市区町村別・年齢5歳階級別の転入者数・転出者数（`municipality_migration_age`）です。2025年1〜12月の移動で、年齢は移動した時点の20〜24歳と25〜29歳、日本人移動者の数です。外国人を含めると、技能実習などで国外から来た人（転入者数に入らない）が国内の別の市町村へ移ったときだけ転出者数に入り、農業や工場の多い町の転出超過が大きく出るため、日本人に絞っています。

市区町村の単位は、政令指定都市と東京23区を区ごとに分けた1,876です。分母は社人研の将来推計人口が持つ2020年の国勢調査の20〜29歳の人口で、福島県の浜通り13市町村は分母が無いため除いています。

20代が転入超過になったのは338、転出超過は1,523です。中央値は20代1,000人あたり33.0人の転出超過で、1,000人あたり50人以上の転出超過は598あります。

```sql
SELECT label AS "市区町村", net AS "20代の転入超過数（人）", round(rate, 1) AS "20代1,000人あたり"
FROM rate
WHERE p20s >= 3000
QUALIFY row_number() OVER (ORDER BY rate DESC) <= 10
ORDER BY rate DESC
```

上位10は、東京都の中央区・墨田区・台東区・品川区のほかに、名古屋市の中区・中村区・東区、大阪市の東成区・淀川区・西区が並びます。20代の人口が3,000人以上の市区町村で比較しています。東京23区は23区すべてが転入超過で、転入超過数では大田区・世田谷区・品川区が多くなります。

## 20〜24歳は都市の中心へ、25〜29歳は周りの市町村へ

20代を20〜24歳と25〜29歳に分けて、転入超過になった市区町村の数を、区・市・町村の別に集計しました。

```chart
{
  "height": 280,
  "data": { "name": "by_kind" },
  "mark": "bar",
  "encoding": {
    "y": {
      "field": "kind",
      "type": "nominal",
      "sort": { "field": "kind_order", "order": "ascending" },
      "title": null
    },
    "yOffset": { "field": "age", "type": "nominal", "sort": ["20〜24歳", "25〜29歳"] },
    "x": { "field": "plus", "type": "quantitative", "title": "転入超過になった市区町村の数" },
    "color": {
      "field": "age",
      "type": "nominal",
      "title": null,
      "scale": { "domain": ["20〜24歳", "25〜29歳"], "range": ["#ef4444", "#3b82f6"] }
    },
    "tooltip": [
      { "field": "kind", "title": "区分" },
      { "field": "age", "title": "年齢" },
      { "field": "plus", "title": "転入超過の数", "format": "," },
      { "field": "n", "title": "区分の数", "format": "," }
    ]
  }
}
```

20〜24歳で転入超過になった町村は916のうち85ですが、25〜29歳では258に増えます。市でも79から173に増えます。20代前半は就職などで都市の中心へ集まり、20代後半になると都市の周りの市町村へ移る人が増えると考えられます。20代後半は結婚や住宅の取得の時期と重なります。

```sql
SELECT
  kind AS "区分",
  max(n) AS "数",
  max(plus) FILTER (WHERE age = '20〜24歳') AS "20〜24歳で転入超過",
  max(plus) FILTER (WHERE age = '25〜29歳') AS "25〜29歳で転入超過"
FROM by_kind
GROUP BY kind, kind_order
ORDER BY kind_order
```

## 若者の定住施策での使い方

- 自分の町の値を、同じ県の市町村や人口規模の近い市町村と並べ、20代の出ていき方が周りより大きいのか小さいのかを確認する
- 20〜24歳と25〜29歳を分けて見る。20代前半が出ていっても、20代後半で戻る・入ってくる町では、住宅や子育ての施策で20代後半の転入を増やせる可能性がある
- 大学のある町は、卒業の年齢で20〜24歳が大きく転出超過になる。卒業生がその後どこへ移るかは、転出先別のテーブルで確認する

## データの出典

本記事は、総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)の2025年の市区町村別・年齢5歳階級別の移動者数と、国立社会保障・人口問題研究所の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)の2020年の人口（国勢調査の値）を、2026-11-12 時点で集計しています。

Queria は住民基本台帳人口移動報告を、市区町村・年齢・国籍の区分ごとに検索できるテーブルにし、列の説明を付けて公開しています。本記事で使った[年齢別の移動者数のテーブル](/datasets/queria/e_stat/migration/municipality_migration_age)から、自分の町の年齢ごとの転入超過数や、過去の年の動きを確認できます。

```sql id=moves
-- 市区町村（政令指定都市と東京23区は区）ごとの20代の日本人の転入超過数
WITH m AS (
  SELECT
    area,
    area_level,
    parent_area,
    sum(net_inflow) AS net,
    sum(net_inflow) FILTER (WHERE age_code = '205') AS net_20_24,
    sum(net_inflow) FILTER (WHERE age_code = '206') AS net_25_29
  FROM e_stat.migration.municipality_migration_age
  WHERE year = 2025
    AND sex_code = '0'
    AND nationality_code = '61000'
    AND age_code IN ('205', '206')
    AND area_level IN ('municipality', 'ward')
  GROUP BY ALL
)
SELECT
  *,
  CASE
    WHEN area_level = 'ward' AND parent_area = '13100' THEN '東京23区'
    WHEN area_level = 'ward' THEN '政令指定都市の区'
    WHEN substr(area, 3, 1) = '2' THEN '市'
    ELSE '町村'
  END AS kind
FROM m
WHERE area_level = 'ward'
  OR area NOT IN (SELECT parent_area FROM m WHERE area_level = 'ward')
```

```sql id=rate
-- 2020年の20代の人口（国勢調査）1,000人あたり。浜通り13市町村は分母が無いので外れる
WITH pop AS (
  SELECT
    city_code,
    any_value(prefecture) || any_value(city_and_county) AS label,
    sum(population) AS p20s
  FROM ipss.regional_projection.population
  WHERE year = 2020
    AND age_from IN (20, 25)
    AND area_level IN ('city', 'town_village', 'ward')
  GROUP BY city_code
)
SELECT m.*, p.label, p.p20s, 1000.0 * m.net / p.p20s AS rate
FROM moves m
JOIN pop p ON p.city_code = m.area
```

```sql id=rate_map
SELECT area, round(rate, 1) AS rate, label || '：' || net || '人（1,000人あたり ' || round(rate, 1) || '）' AS label
FROM rate
```

```sql id=by_kind
SELECT
  kind,
  CASE kind WHEN '東京23区' THEN 1 WHEN '政令指定都市の区' THEN 2 WHEN '市' THEN 3 ELSE 4 END AS kind_order,
  age,
  count(*) AS n,
  count(*) FILTER (WHERE v > 0) AS plus
FROM (
  SELECT kind, '20〜24歳' AS age, net_20_24 AS v FROM rate
  UNION ALL
  SELECT kind, '25〜29歳' AS age, net_25_29 AS v FROM rate
)
GROUP BY ALL
```
