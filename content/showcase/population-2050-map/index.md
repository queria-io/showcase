---
title: 2050年には1,883市区町村のうち1,779で人口が減り、342は2020年の半分を下回る推計です
description: 国立社会保障・人口問題研究所の将来推計人口で、市区町村ごとの2020年から2050年の人口の増減率を地図に塗りました。人口が増えるのは104だけで、20〜39歳の女性が半分を下回る市区町村は741あります。
publishedAt: 2026-11-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 将来推計人口
  - 人口減少
  - 地図
  - 総合計画
datasets:
  - queria/ipss
sources:
  - title: 日本の地域別将来推計人口（令和5年推計）
    url: https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp
    publisher: 国立社会保障・人口問題研究所
agentHint: 自分の県の市町村ごとに、2020年と2050年の人口、20〜39歳の女性、65歳以上の割合を将来推計人口から並べて、増減率の順に出して
socialAnnounce: |-
  2050年、あなたの町の人口は何%減る？ 市区町村ごとの将来推計人口を地図に塗りました。

  1,883市区町村のうち1,779で人口が減り、342は2020年の半分を下回ります。増えるのは東京都中央区や千葉県流山市など104だけです。
  Queriaは行政のオープンデータを整えて公開しています
---

国立社会保障・人口問題研究所（社人研）の将来推計人口で、2020年から2050年の人口の増減率を市区町村ごとに計算すると、1,883市区町村のうち1,779（94.5%）で人口が減り、342は2020年の半分を下回る推計でした。人口が増えるのは104市区町村で、市区町村の増減率の中央値は33.5%減です。市区町村の総合計画や人口ビジョンをつくるときは、自分の町の数字を周りの市町村や全国と並べると、減り方が大きい側か小さい側かを確認できます。

社人研の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)は、2020年の国勢調査をもとに、市区町村ごとの人口を2050年まで5年ごとに推計しています。2020年から2050年の人口の増減率で市区町村を塗ったのが下の地図です。赤いほど大きく減り、青い市区町村は増えます。

```map
type: map
caption: 2020年から2050年の人口の増減率（%）
layers:
  - from: muni_map
    area: city
    code: city_code
    color: change_pct
    label: label
    name: 人口の増減率（%）
lng: 137.5
lat: 37.5
zoom: 4.3
```

人口が増える市区町村は、東京23区と多摩東部、川崎市と横浜市北部、さいたま市と埼玉県南部、つくばエクスプレスの沿線（八潮市・流山市・守谷市・つくばみらい市・つくば市）に集まっています。東京圏の外では、札幌・名古屋・大阪・神戸・福岡の都心の区、福岡市の周りの町、熊本県の菊陽町・大津町・合志市、沖縄本島の中南部が増えます。それ以外の大半の地域は減り、山間部や離島には半分以下になる町村が並びます。

## 1,883市区町村のうち1,779で人口が減り、中央値は33.5%減

社人研の将来推計人口を男女・5歳階級別に持つテーブル（`ipss.regional_projection.population`）です。市区町村の単位は、政令指定都市を区ごとに分けた1,883です。福島県の浜通り13市町村は、推計が1つにまとめられていて市町村ごとの推計が無いため除いています。2020年は国勢調査の人口、2050年は推計値です。

2050年の人口が2020年より少ない市区町村は1,779で、全体の94.5%です。増減率の幅ごとに集計すると、半分を下回る（50%以上減る）市区町村が342、30〜50%減るのが715あります。

```chart
{
  "height": 260,
  "data": { "name": "change_bins" },
  "mark": "bar",
  "encoding": {
    "x": {
      "field": "bin",
      "type": "nominal",
      "sort": { "field": "bin_order", "order": "ascending" },
      "title": "2020年から2050年の人口の増減",
      "axis": { "labelAngle": 0 }
    },
    "y": { "field": "n", "type": "quantitative", "title": "市区町村の数" },
    "color": {
      "field": "bin",
      "type": "nominal",
      "legend": null,
      "sort": { "field": "bin_order", "order": "ascending" },
      "scale": { "range": ["#3b82f6", "#fecaca", "#fca5a5", "#ef4444", "#b91c1c"] }
    },
    "tooltip": [
      { "field": "bin", "title": "増減" },
      { "field": "n", "title": "市区町村の数", "format": "," }
    ]
  }
}
```

全国の合計では、2050年の人口は2020年の83.0%です。市区町村の増減率の中央値は33.5%減で、全国の合計の17%減より大きく減ります。人口の多い都市の減り方が小さいので、全国の合計の減少率は小さくなります。

## 人口1万人未満の町村は中央値で47.7%減り、20万人以上の市区は10.1%減

増減率の上位と下位の市区町村です。増える市区町村には、東京都の中央区・港区・千代田区と、千葉県流山市のような鉄道沿線の住宅地が入っています。減少率が大きいのは、群馬県南牧村・熊本県球磨村・奈良県野迫川村のような山間の町村です。

```sql
SELECT label AS "市区町村", p2020 AS "2020年の人口", p2050 AS "2050年の人口（推計）", change_pct AS "増減率（%）"
FROM muni
QUALIFY row_number() OVER (ORDER BY change_pct DESC) <= 10
  OR row_number() OVER (ORDER BY change_pct) <= 10
ORDER BY change_pct DESC
```

2020年の人口の規模で分けると、1万人未満の町村は中央値で47.7%減り、半分を下回る町村が多くあります。20万人以上の市区は中央値で10.1%減で、半分を下回る市区はありません。20万人以上でも、長崎市（31.5%減）・横須賀市（29.7%減）・旭川市（28.3%減）・秋田市（28.2%減）のように、人口30万人以上でも3割近く減る市があります。

```sql
SELECT
  size_class AS "2020年の人口",
  count(*) AS "市区町村の数",
  round(median(change_pct), 1) AS "増減率の中央値（%）",
  count(*) FILTER (WHERE p2050 < p2020 * 0.5) AS "半分を下回る",
  count(*) FILTER (WHERE p2050 >= p2020) AS "増える"
FROM muni
GROUP BY size_class, size_order
ORDER BY size_order
```

## 20〜39歳の女性が2050年に2020年の半分を下回る市区町村は741

生まれる子どもの数は、20〜39歳の女性の人数に大きく影響されます。2050年の20〜39歳の女性が2020年の半分を下回る市区町村は741です。そのうち329は総人口も半分を下回ります。また、2050年に65歳以上が人口の過半数になる市区町村は559あります。

```sql
SELECT
  count(*) FILTER (WHERE w2050 < w2020 * 0.5) AS "20〜39歳の女性が半分を下回る",
  count(*) FILTER (WHERE w2050 < w2020 * 0.5 AND p2050 < p2020 * 0.5) AS "うち総人口も半分を下回る",
  count(*) FILTER (WHERE o2050 > p2050 * 0.5) AS "65歳以上が過半数"
FROM muni
```

## 総合計画・人口ビジョンでの使い方

- 自分の市町村の増減率を、同じ県の市町村や人口規模の近い市町村と並べ、減り方が周りより大きいのか小さいのかを確認してから目標人口を置く
- 総人口と20〜39歳の女性の減少率を分けて確認する。総人口の減少が小さくても、20〜39歳の女性が大きく減る町では、その後の出生数が先に減る
- 隣の市町村が増える側か減る側かを地図で確認し、通勤・通学や買い物で結びつく範囲で、公共施設の再編や広域連携の相手を考える

## データの出典

本記事は、国立社会保障・人口問題研究所の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)を、2026年11月12日時点で集計しています。2020年は国勢調査の人口、2025年以降は推計値です。福島県の浜通り13市町村は推計が1つにまとめられているため、地図と集計から除いています。

Queria は社人研の将来推計人口を、市区町村・男女・5歳階級ごとに1行のテーブルにして、列の説明を付けて公開しています。本記事で使った[将来推計人口のテーブル](/datasets/queria/ipss/regional_projection/population)から、自分の町と周りの市町村の年齢別の推移を確認できます。

```sql id=muni
-- 市区町村（政令指定都市は区）ごとの2020年と2050年の人口
SELECT
  city_code,
  any_value(prefecture) || any_value(city_and_county) AS label,
  sum(population) FILTER (WHERE year = 2020) AS p2020,
  sum(population) FILTER (WHERE year = 2050) AS p2050,
  round(100.0 * sum(population) FILTER (WHERE year = 2050) / sum(population) FILTER (WHERE year = 2020) - 100, 1) AS change_pct,
  sum(population) FILTER (WHERE year = 2020 AND sex_code = '2' AND age_from BETWEEN 20 AND 39) AS w2020,
  sum(population) FILTER (WHERE year = 2050 AND sex_code = '2' AND age_from BETWEEN 20 AND 39) AS w2050,
  sum(population) FILTER (WHERE year = 2050 AND age_from >= 65) AS o2050,
  CASE
    WHEN sum(population) FILTER (WHERE year = 2020) < 10000 THEN '1万人未満'
    WHEN sum(population) FILTER (WHERE year = 2020) < 50000 THEN '1万〜5万人'
    WHEN sum(population) FILTER (WHERE year = 2020) < 200000 THEN '5万〜20万人'
    ELSE '20万人以上'
  END AS size_class,
  CASE
    WHEN sum(population) FILTER (WHERE year = 2020) < 10000 THEN 1
    WHEN sum(population) FILTER (WHERE year = 2020) < 50000 THEN 2
    WHEN sum(population) FILTER (WHERE year = 2020) < 200000 THEN 3
    ELSE 4
  END AS size_order
FROM ipss.regional_projection.population
WHERE area_level IN ('city', 'town_village', 'ward')
GROUP BY city_code
```

```sql id=muni_map
SELECT city_code, change_pct, label || '：' || change_pct || '%' AS label
FROM muni
```

```sql id=change_bins
SELECT
  CASE
    WHEN p2050 >= p2020 THEN '増える'
    WHEN p2050 >= p2020 * 0.8 THEN '0〜20%減'
    WHEN p2050 >= p2020 * 0.7 THEN '20〜30%減'
    WHEN p2050 >= p2020 * 0.5 THEN '30〜50%減'
    ELSE '50%以上減'
  END AS bin,
  CASE
    WHEN p2050 >= p2020 THEN 1
    WHEN p2050 >= p2020 * 0.8 THEN 2
    WHEN p2050 >= p2020 * 0.7 THEN 3
    WHEN p2050 >= p2020 * 0.5 THEN 4
    ELSE 5
  END AS bin_order,
  count(*) AS n
FROM muni
GROUP BY ALL
ORDER BY bin_order
```
