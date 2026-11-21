---
title: 外国人住民の割合がこの10年で最も上がったのは、ニセコ・白馬・湯沢のようなスキー場と温泉の町でした
description: 住民基本台帳の2016年と2026年の人口から、市区町村ごとの外国人住民の割合を地図にしました。割合が5%以上の市区町村は34から193に増え、上がり幅の上位にはスキー場と温泉の町が並びます。北海道倶知安町は6.5%から24.6%に上がりました。
publishedAt: 2026-11-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 外国人住民
  - 多文化共生
  - 地図
  - 観光
datasets:
  - queria/e_stat
  - queria/ipss
sources:
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数調査
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
agentHint: 自分の県の市町村ごとに、住民基本台帳の外国人住民の人数と割合を2016年と2026年について出して、割合の上がり幅の順に並べて
socialAnnounce: |-
  外国人住民の割合を市区町村ごとに地図に塗りました（住民基本台帳、2016→2026年）。

  10年で割合が最も上がったのは、北海道倶知安町（6.5%→24.6%）・長野県白馬村・ニセコ町・箱根町・草津町・湯沢町。スキー場と温泉の町が上位に並びます。
  Queriaは行政のオープンデータを整えて公開しています
---

2016年から2026年の10年間で、人口に占める外国人住民の割合が最も上がったのは、北海道倶知安町（6.5%→24.6%）、ニセコ町、長野県白馬村、新潟県湯沢町などのスキー場の町と、神奈川県箱根町や群馬県草津町などの温泉の町でした。全国の割合は1.7%から3.3%に上がり、割合が5%以上の市区町村は34から193に増えています。

総務省の[住民基本台帳に基づく人口、人口動態及び世帯数調査](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)から、市区町村ごとに2026年1月1日の人口に占める外国人住民の割合を算出し、地図にしました。色が濃いほど割合が高い市区町村です。

```map
type: map
caption: 人口に占める外国人住民の割合（2026年1月1日、%）
layers:
  - from: share_map
    area: city
    code: area_code
    color: share_2026
    label: label
    name: 外国人住民の割合（%）
lng: 137.5
lat: 37.5
zoom: 4.3
```

割合の高い市区町村は、東京23区と大阪市・名古屋市・神戸市の都心の区、愛知県・岐阜県・群馬県・茨城県・静岡県の工場や農業の多い市町、北海道の後志地方と長野県北部のスキー場の町です。

## 人口5,000人以上の町で割合が最も上がったのは、倶知安町の6.5%から24.6%

使ったのは、住民基本台帳の人口を総計・日本人住民・外国人住民の区分で記録したテーブル（`e_stat.resident_registry.population`）です。各年1月1日の人口で、2016年と2026年を比較しました。市区町村は、政令指定都市を区ごとに分けた1,874です。福島県の浜通りの町村など、2016年か2026年の値がない市区町村は除いています。

人口5,000人以上の市区町村を、外国人住民の割合の上がり幅が大きい順に並べました。

```chart
{
  "height": 420,
  "data": { "name": "top_gain" },
  "mark": { "type": "bar" },
  "encoding": {
    "y": {
      "field": "label",
      "type": "nominal",
      "sort": { "field": "gain", "order": "descending" },
      "title": null
    },
    "yOffset": { "field": "year", "type": "nominal" },
    "x": { "field": "share", "type": "quantitative", "title": "外国人住民の割合（%）" },
    "color": {
      "field": "year",
      "type": "nominal",
      "title": null,
      "scale": { "domain": ["2016年", "2026年"], "range": ["#93c5fd", "#1d4ed8"] }
    },
    "tooltip": [
      { "field": "label", "title": "市区町村" },
      { "field": "year", "title": "年" },
      { "field": "share", "title": "割合（%）", "format": ".1f" }
    ]
  }
}
```

上位には、北海道の倶知安町（6.5%→24.6%）とニセコ町、長野県の白馬村、新潟県の湯沢町のスキー場の町と、神奈川県の箱根町、群馬県の草津町、沖縄県の恩納村などの温泉やリゾートの町が入っています。大阪市の西成区・浪速区や埼玉県の蕨市などの都市部の区や市、三重県の木曽岬町や茨城県の利根町などの工場や住宅地の町も入ります。群馬県の大泉町は、2016年にすでに割合が16.3%だったので、この10年の上がり幅では上位に入りません。

人口5,000人未満の町村も含めると、2026年の割合が最も高いのは北海道の赤井川村（36.7%）で、占冠村（35.5%）が続きます。どちらもスキー場のある村です。

## 割合が5%以上の市区町村は34から193に、10%以上は5から34に増えた

全国の外国人住民の割合は、2016年の1.7%から2026年の3.3%に上がりました。1,874市区町村のうち1,855で割合が上がり、割合が5%以上の市区町村は34から193に、10%以上は5から34に増えています。

```sql
SELECT
  count(*) AS "市区町村の数",
  count(*) FILTER (WHERE share_2026 > share_2016) AS "割合が上がった",
  count(*) FILTER (WHERE share_2016 >= 5) AS "5%以上（2016年）",
  count(*) FILTER (WHERE share_2026 >= 5) AS "5%以上（2026年）",
  count(*) FILTER (WHERE share_2016 >= 10) AS "10%以上（2016年）",
  count(*) FILTER (WHERE share_2026 >= 10) AS "10%以上（2026年）",
  round(100.0 * sum(f2016) / sum(t2016), 1) AS "全国の割合（2016年）",
  round(100.0 * sum(f2026) / sum(t2026), 1) AS "全国の割合（2026年）"
FROM share
```

## 多文化共生と観光の施策での使い方

- 自分の町の割合と上がり幅を、同じ県の市町村や、観光・製造業・農業など同じ産業の町と比較し、窓口の多言語対応や日本語教室の規模を決める根拠にできます
- スキー場の町では、冬の間だけ住む人も、住民登録をしていれば住民基本台帳に含まれます。1月1日の値は冬の人数なので、ほかの季節の人数は、月ごとの人口を公表している自治体の資料で確認する必要があります
- 割合が上がった町どうしで、住まいの確保や医療・学校の対応の事例を共有する相手を探せます

## データの出典

本記事は、総務省の[住民基本台帳に基づく人口、人口動態及び世帯数調査](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)の2016年と2026年（各年1月1日現在）の市区町村別の人口を、2026-11-12 時点で集計しています。市区町村の単位を統一するため、国立社会保障・人口問題研究所の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)の市区町村コードの一覧を使っています。

Queria は、住民基本台帳の人口を、総計・日本人住民・外国人住民の区分ごとに1968年から取得できるテーブルにし、列の意味をメタデータに記載して公開しています。本記事で使った[住民基本台帳の人口のテーブル](/datasets/queria/e_stat/resident_registry/population)から、自分の町の外国人住民の推移を確認できます。

```sql id=share
-- 市区町村（政令指定都市は区）ごとの外国人住民の割合。単位は将来推計人口の市区町村コードにそろえる
WITH units AS (
  SELECT DISTINCT city_code
  FROM ipss.regional_projection.population
  WHERE year = 2020 AND area_level IN ('city', 'town_village', 'ward')
), p AS (
  SELECT
    area_code,
    any_value(pref_name || municipality_name) AS label,
    sum(population_total) FILTER (WHERE year = 2016 AND resident_kind = 'total') AS t2016,
    sum(population_total) FILTER (WHERE year = 2016 AND resident_kind = 'foreign') AS f2016,
    sum(population_total) FILTER (WHERE year = 2026 AND resident_kind = 'total') AS t2026,
    sum(population_total) FILTER (WHERE year = 2026 AND resident_kind = 'foreign') AS f2026
  FROM e_stat.resident_registry.population
  WHERE area_level = 'municipality'
    AND year IN (2016, 2026)
    AND area_code IN (SELECT city_code FROM units)
  GROUP BY area_code
)
SELECT
  *,
  100.0 * f2016 / t2016 AS share_2016,
  100.0 * f2026 / t2026 AS share_2026
FROM p
WHERE t2016 IS NOT NULL AND t2026 IS NOT NULL
```

```sql id=share_map
SELECT
  area_code,
  round(share_2026, 1) AS share_2026,
  label || '：' || round(share_2016, 1) || '% → ' || round(share_2026, 1) || '%' AS label
FROM share
```

```sql id=top_gain
WITH top AS (
  SELECT label, share_2016, share_2026, share_2026 - share_2016 AS gain
  FROM share
  WHERE t2026 >= 5000
  ORDER BY gain DESC
  LIMIT 12
)
SELECT label, gain, '2016年' AS year, round(share_2016, 1) AS share FROM top
UNION ALL
SELECT label, gain, '2026年' AS year, round(share_2026, 1) AS share FROM top
```
