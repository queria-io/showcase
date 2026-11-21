---
title: 子育て世代の女性が転入してくる町でも、生まれる子どもの数は中央値で2割近く減っています
description: 25〜39歳の女性の転入超過が大きい上位5分の1の市区町村でも、出生数は2015〜17年から2022〜24年に中央値で18.7%減りました。比較した1,028市区町村のうち、出生数が減らなかったのは6市町です。
publishedAt: 2026-11-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口動態統計
  - 出生
  - 人口移動
  - 子育て
  - 保育
datasets:
  - queria/e_stat
sources:
  - title: 人口動態統計
    url: https://www.mhlw.go.jp/toukei/list/81-1.html
    publisher: 厚生労働省
  - title: 住民基本台帳人口移動報告
    url: https://www.stat.go.jp/data/idou/index.html
    publisher: 総務省統計局
  - title: 令和7年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2025/index.html
    publisher: 総務省統計局
agentHint: 自分の県の市区町村ごとに、2015〜17年と2022〜24年の出生数の3年平均と、2015〜2024年の25〜39歳の日本人女性の転入超過数を並べて。転入超過数は2025年国勢調査の25〜39歳の日本人女性の人口に対する割合でも出して
socialAnnounce: |-
  25〜39歳の女性の転入超過が上位5分の1の市区町村でも、出生数は2015〜17年から2022〜24年に中央値で18.7%減りました。

  保育所や学校の整備計画の見通しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

25〜39歳の女性の転入超過が最も大きい5分の1の市区町村でも、1年に生まれる子どもの数は、2015〜17年の平均から2022〜24年の平均にかけて中央値で18.7%減りました。転出超過が最も大きい5分の1の市区町村では39.0%減で、転入超過が大きい町ほど減り方は小さくなりますが、比較した1,028市区町村のうち出生数が減らなかったのは6市町だけです。

人口ビジョンや総合戦略で子育て世帯の転入を増やす目標を掲げる市区町村は多く、子育て世帯の転入が続けば出生数や保育所・小学校の需要も保てると見込む計画があります。この記事では、子育て世代にあたる25〜39歳の女性の転入超過と出生数を市区町村ごとに並べ、その見込みが実績と合うかを確認します。

## 転入超過が大きい町でも、出生数は中央値で18.7%減った

出生数は、厚生労働省の[人口動態統計](https://www.mhlw.go.jp/toukei/list/81-1.html)を市区町村ごとに2015年から2024年まで収録した[人口動態のテーブル](/datasets/queria/e_stat/vital_statistics/vital_events)から取りました。集計しているのは日本人の子どもの出生で、母の住所がある市区町村に計上されます。1年ごとの値は町によって上下するので、2015〜17年と2022〜24年の3年平均どうしを比較します。対象は、2015〜17年の平均で1年に100人以上生まれていた1,028市区町村です。政令指定都市は市全体で1つ、東京23区は区ごとに集計しています。

女性の転入は、総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)を年齢5歳階級別に収録した[人口移動のテーブル](/datasets/queria/e_stat/migration/municipality_migration_age)から取りました。25〜29歳・30〜34歳・35〜39歳の日本人女性の転入者数から転出者数を引いた転入超過数を、2015年から2024年までの10年分合計しています。これを[2025年国勢調査の年齢別人口](/datasets/queria/e_stat/census/census_municipality_age_2025)にある同じ年齢の日本人女性の人数で割り、町の人口規模の違いを除いた「転入超過の割合」とします。たとえば流山市は10年間の転入超過が9,708人で、2025年の25〜39歳の日本人女性19,731人の49.2%にあたります。

この割合の小さい順に1,028市区町村を5つのグループに分け、グループごとに出生数の増減率の中央値を出しました。

```chart caption="25〜39歳の日本人女性の転入超過の割合で5つに分けた市区町村の、出生数の増減率の中央値（2015〜17年平均→2022〜24年平均）"
{
  "data": { "name": "groups" },
  "height": 260,
  "encoding": {
    "y": { "field": "label", "type": "nominal", "sort": { "field": "grp", "op": "min" }, "title": null }
  },
  "layer": [
    {
      "mark": { "type": "bar", "color": "#b2182b" },
      "encoding": {
        "x": { "field": "median_chg", "type": "quantitative", "title": "出生数の増減率の中央値（%）", "scale": { "domain": [-48, 0] } },
        "tooltip": [
          { "field": "label", "title": "グループ" },
          { "field": "inflow_range", "title": "転入超過の割合" },
          { "field": "towns", "title": "市区町村数" },
          { "field": "median_chg", "title": "出生数の増減率の中央値（%）", "format": ".1f" },
          { "field": "held", "title": "出生数が減らなかった市区町村" }
        ]
      }
    },
    {
      "mark": { "type": "text", "align": "right", "dx": -4, "fontSize": 12, "color": "#334155" },
      "encoding": {
        "x": { "field": "median_chg", "type": "quantitative" },
        "text": { "field": "median_chg", "type": "quantitative", "format": ".1f" }
      }
    }
  ]
}
```

25〜39歳の女性の転出超過が最も大きい町（グループ1、転出超過の割合が16.5%以上）では、出生数の中央値は39.0%減りました。グループが上がるにつれて減り方は小さくなり、転入超過が最も大きいグループ5（転入超過の割合が6.4〜50.8%、205市区町村）では18.7%減です。グループ5の中にも、福岡県新宮町のように転入超過の割合が23.7%ありながら出生数が38.2%減った町があります。

## どのグループも、出生数は2015年から2024年まで毎年減った

グループごとに、各市区町村の出生数を2015〜17年の平均を100とした値にして、その中央値を年ごとに並べました。

```chart caption="出生数の推移（2015〜17年平均＝100、グループごとの市区町村の中央値）"
{
  "data": { "name": "trend" },
  "height": 300,
  "mark": { "type": "line", "point": true },
  "encoding": {
    "x": { "field": "year", "type": "ordinal", "title": "年" },
    "y": { "field": "idx", "type": "quantitative", "title": "2015〜17年平均＝100", "scale": { "zero": false } },
    "color": { "field": "label", "type": "nominal", "title": "転入超過の割合", "sort": { "field": "grp" } },
    "tooltip": [
      { "field": "label", "title": "グループ" },
      { "field": "year", "title": "年" },
      { "field": "idx", "title": "指数", "format": ".1f" }
    ]
  }
}
```

5つのグループはどれも2015年から2024年まで毎年下がりました。グループ5とグループ1の差は2017年から2023年まで年々開き、2023年と2024年はともに20.0ポイントです。2024年の値は、グループ5が76.6、グループ1が56.6です。転入超過が大きい町の出生数も、ほかの町と同じく毎年減っており、減る幅が小さいことが違いです。

## 出生数が減らなかった6市町は、どれも転入超過の割合が10%以上

1,028市区町村を1つずつ点にしました。横軸が25〜39歳の日本人女性の転入超過の割合、縦軸が出生数の増減率です。原発事故の避難指示が出ていた福島県浪江町と富岡町は、転出超過の割合が100%を超えて横軸の範囲が大きく広がるため、図から外しています。

```chart caption="市区町村ごとの、25〜39歳の日本人女性の転入超過の割合と出生数の増減率（点の大きさは2015〜17年の平均出生数）"
{
  "data": { "name": "scatter" },
  "height": 380,
  "layer": [
    {
      "data": { "values": [{ "y": 0 }] },
      "mark": { "type": "rule", "color": "#94a3b8", "strokeDash": [4, 4] },
      "encoding": { "y": { "field": "y", "type": "quantitative" } }
    },
    {
      "mark": { "type": "circle", "opacity": 0.6, "stroke": "#fff", "strokeWidth": 0.5 },
      "encoding": {
        "x": { "field": "inflow_pct", "type": "quantitative", "title": "25〜39歳の日本人女性の転入超過の割合（%、2015〜2024年の累計÷2025年の人口）" },
        "y": { "field": "birth_chg", "type": "quantitative", "title": "出生数の増減率（%）" },
        "size": { "field": "b0", "type": "quantitative", "title": "2015〜17年の平均出生数", "scale": { "range": [10, 400] } },
        "color": { "field": "kind", "type": "nominal", "title": null, "scale": { "domain": ["出生数が減らなかった", "減った"], "range": ["#2166ac", "#94a3b8"] } },
        "tooltip": [
          { "field": "label", "title": "市区町村" },
          { "field": "inflow_pct", "title": "転入超過の割合（%）", "format": ".1f" },
          { "field": "birth_chg", "title": "出生数の増減率（%）", "format": ".1f" },
          { "field": "b0", "title": "2015〜17年の平均出生数", "format": ",.0f" },
          { "field": "b1", "title": "2022〜24年の平均出生数", "format": ",.0f" }
        ]
      }
    }
  ]
}
```

出生数が減らなかったのは、京都府大山崎町（16.9%増）、千葉県印西市（11.4%増）、石川県かほく市（9.8%増）、千葉県流山市（5.7%増）、神奈川県大井町（1.0%増）と、増減のなかった熊本県御船町の6市町です。6市町とも転入超過の割合が10%以上で、すべてグループ5に入ります。このうち大井町と御船町は、3年平均の出生数の差が1年あたり1人以内で、増えたとも減ったとも言いにくい幅です。転入超過の割合が10%以上の市区町村は全部で148あり、そのうち142は出生数が減っています。

## 都道府県別では、秋田県の市区町村の減り方が中央値41.7%で最も大きい

比較した1,028市区町村の出生数の増減率を地図にしました。政令指定都市は市全体の値を各区に塗っています。2015〜17年の平均出生数が100人に満たない市区町村は塗っていません。

```map
type: map
caption: 出生数の増減率（2015〜17年平均→2022〜24年平均）
lng: 137.5
lat: 37.5
zoom: 4.3
layers:
  - from: muni_map
    area: city
    code: code
    color: birth_chg
    label: label
    name: 出生数の増減率（%）
    ends: [減少, 増加]
```

ほぼ全域が減少の色です。都道府県ごとに市区町村の増減率の中央値を出すと、減り方が大きいのは秋田県（41.7%減）・岩手県（39.0%減）・宮城県（37.0%減）、小さいのは大阪府（19.2%減）・東京都（22.0%減）・沖縄県（22.8%減）です。減少が1割未満か、増えた市区町村は31あり、千葉県の袖ケ浦市、茨城県のつくば市・阿見町、東京都の中央区・台東区、福岡県の福津市・筑前町、岡山県の総社市・浅口市などです。

## 保育・学校の整備計画で使う

- 子育て世帯の転入を見込んで保育所の定員や小学校の教室数を計画している市区町村の担当者は、自分の町の転入超過の割合と出生数の増減率を、同じグループの中央値と並べられます。転入超過が大きい町でも、2015〜17年から2022〜24年に出生数は中央値で2割近く減っているので、「転入が続けば子どもの数は大きく減らない」という前提で需要を見込んでいる計画は、見直す根拠になります
- 出生数がはっきり増えた大山崎町・印西市・かほく市・流山市の4市町や、転入超過の割合が近いのに出生数の減り方が大きく違う町を、比較の対象に選べます。住宅開発の時期や子育て支援の内容を確認する先を、数字で絞り込めます
- 総合戦略を評価する担当者は、転入超過の目標と出生数の目標を、それぞれの実績で別々に確認できます。転入超過が目標どおりでも出生数は減ることがあるので、転入超過の実績を出生数の目標を達成する根拠にしない判断に使えます

## データの出典

本記事は、厚生労働省の[人口動態統計](https://www.mhlw.go.jp/toukei/list/81-1.html)と、総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)と[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)を、2026-11-17 時点で集計しています。

Queriaは、人口動態統計・住民基本台帳人口移動報告・国勢調査を、地域コードと列名を統一し、項目の意味をメタデータとして付けて公開しています。本記事で使った[人口動態のテーブル](/datasets/queria/e_stat/vital_statistics/vital_events)と[人口移動のテーブル](/datasets/queria/e_stat/migration/municipality_migration_age)から、自分の町と近隣の町の出生数と転入超過の推移を確認できます。

```sql id=muni
-- 市区町村（政令指定都市は市全体、東京23区は区ごと）の出生数と、25〜39歳の日本人女性の転入超過
WITH b AS (
  SELECT
    area_code,
    any_value(area_name) AS name,
    any_value(prefecture_code) AS pref_code,
    avg(births) FILTER (WHERE year BETWEEN 2015 AND 2017) AS b0,
    avg(births) FILTER (WHERE year BETWEEN 2022 AND 2024) AS b1,
    count(births) FILTER (WHERE year BETWEEN 2015 AND 2017) AS n0,
    count(births) FILTER (WHERE year BETWEEN 2022 AND 2024) AS n1
  FROM e_stat.vital_statistics.vital_events
  WHERE area_kind IN ('municipality', 'designated_city') AND year <= 2024
  GROUP BY area_code
),
m AS (
  SELECT area, sum(net_inflow) AS net_f
  FROM e_stat.migration.municipality_migration_age
  WHERE (area_level = 'municipality' OR (area_level = 'ward' AND area LIKE '131%'))
    AND sex_code = '2' AND nationality_code = '61000'
    AND age_code IN ('206', '207', '208') AND year BETWEEN 2015 AND 2024
  GROUP BY area
),
w AS (
  SELECT area, sum(population_japanese_female) AS f2025
  FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'town_village', 'ward') AND age_code IN ('06', '07', '08')
  GROUP BY area
),
p AS (
  SELECT left(area, 2) AS pref_code, area_name AS pref_name
  FROM e_stat.census.census_municipality_age_2025
  WHERE area_level = 'prefecture' AND age_code = '06'
),
j AS (
  SELECT
    b.area_code, p.pref_name, b.name, b.b0, b.b1, m.net_f, w.f2025,
    round(100.0 * m.net_f / w.f2025, 1) AS inflow_pct,
    round(100.0 * (b.b1 / b.b0 - 1), 1) AS birth_chg
  FROM b
  JOIN m ON m.area = b.area_code
  JOIN w ON w.area = b.area_code
  JOIN p ON p.pref_code = b.pref_code
  -- 2015〜17年の平均出生数が100人以上で、両方の3年がそろう市区町村（途中でコードが変わった団体は落ちる）
  WHERE b.b0 >= 100 AND b.n0 = 3 AND b.n1 = 3
)
SELECT *, ntile(5) OVER (ORDER BY net_f / f2025, area_code) AS grp
FROM j
```

```sql id=groups
SELECT
  grp,
  CASE grp
    WHEN 1 THEN '1 転出超過が大きい'
    WHEN 2 THEN '2 転出超過'
    WHEN 3 THEN '3 やや転出超過'
    WHEN 4 THEN '4 ほぼ均衡'
    ELSE '5 転入超過が大きい'
  END AS label,
  printf('%.1f〜%.1f%%', min(inflow_pct), max(inflow_pct)) AS inflow_range,
  count(*) AS towns,
  round(median(birth_chg), 1) AS median_chg,
  count(*) FILTER (WHERE b1 >= b0) AS held
FROM muni
GROUP BY grp
ORDER BY grp
```

```sql id=trend
-- 各市区町村の出生数を2015〜17年平均＝100にして、グループごとの中央値を年ごとに
SELECT g.grp, g.label, v.year, round(median(100.0 * v.births / m.b0), 1) AS idx
FROM e_stat.vital_statistics.vital_events v
JOIN muni m ON m.area_code = v.area_code
JOIN groups g ON g.grp = m.grp
WHERE v.area_kind IN ('municipality', 'designated_city') AND v.year BETWEEN 2015 AND 2024
GROUP BY g.grp, g.label, v.year
ORDER BY g.grp, v.year
```

```sql id=scatter
-- 浪江町・富岡町（転出超過の割合が-100%を下回る）は図から外す
SELECT
  pref_name || name AS label, inflow_pct, birth_chg, b0, b1,
  CASE WHEN b1 >= b0 THEN '出生数が減らなかった' ELSE '減った' END AS kind
FROM muni
WHERE inflow_pct >= -100
ORDER BY b0 DESC
```

```sql id=held
-- 出生数が減らなかった市区町村と、転入超過の割合が10%以上の市区町村の数（プロットはしない）
SELECT
  count(*) FILTER (WHERE b1 >= b0) AS held,
  count(*) FILTER (WHERE b1 > b0) AS increased,
  count(*) FILTER (WHERE inflow_pct >= 10) AS inflow10,
  count(*) FILTER (WHERE inflow_pct >= 10 AND b1 < b0) AS inflow10_fell,
  min(inflow_pct) FILTER (WHERE b1 >= b0) AS held_min_inflow,
  count(*) FILTER (WHERE birth_chg > -10) AS under10_or_up,
  count(*) AS towns
FROM muni
```

```sql id=muni_map
-- 政令指定都市は市全体の値を各区のコードに配る
WITH wards AS (
  SELECT DISTINCT area, parent_area
  FROM e_stat.census.census_municipality_age_2025
  WHERE area_level = 'ward'
)
SELECT
  coalesce(wards.area, muni.area_code) AS code,
  muni.birth_chg,
  muni.pref_name || muni.name || '：' || muni.birth_chg || '%' AS label
FROM muni
LEFT JOIN wards ON wards.parent_area = muni.area_code
```

```sql id=pref_median
-- 都道府県ごとの、市区町村の出生数の増減率の中央値（プロットはしない）
SELECT pref_name, count(*) AS towns, round(median(birth_chg), 1) AS median_chg
FROM muni
GROUP BY pref_name
ORDER BY median_chg
```
