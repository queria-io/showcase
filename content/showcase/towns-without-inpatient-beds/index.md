---
title: 町の中に病院も、入院用のベッドがある診療所も無い市町村が、2008年の250から2024年の324に増えた
description: 町の中に病院も、入院用のベッドがある診療所も無い市町村は、2008年の250から2024年の324に増えました。町村926のうち321がこれにあたり、324市町村には2025年の国勢調査で177万人が住んでいます。
publishedAt: 2026-11-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療施設調査
  - 有床診療所
  - 在宅医療
  - 介護連携
  - 国勢調査
datasets:
  - queria/e_stat
  - queria/geocoder
sources:
  - title: 医療施設調査
    url: https://www.mhlw.go.jp/toukei/list/79-1.html
    publisher: 厚生労働省
  - title: 令和7年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2025/index.html
    publisher: 総務省統計局
agentHint: 自分の県の市町村ごとに、病院数と入院用のベッドを持つ一般診療所の数を2008年から2024年まで並べて、両方が0になった年を出して。2025年国勢調査の人口と65歳以上の割合も添えて
socialAnnounce: |-
  町の中に病院も、入院用のベッドがある診療所も無い市町村は、2008年の250から2024年の324に増え、177万人が住んでいます。

  町村の在宅医療・介護連携の計画に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

病院（病床20床以上）が無く、入院用のベッドを持つ診療所（有床診療所、19床以下）も無い市町村は、2008年の250から2024年の324に増えました。324のうち321は町村で、町村926の3分の1強にあたります。2025年の[国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)では、324市町村に177万人が住んでいます。2010年から2024年に町の中で入院できる場所がなくなった89市町村のうち72は、病院が無く、有床診療所だけで入院を受けていた市町村でした。

町村で在宅医療・介護連携推進事業を担当する職員は、退院してくる高齢者をどの病院から受け入れ、急に具合が悪くなったときにどこへ入院してもらうかを、地域の医療機関と決めておく必要があります。その前提として、町の中に入院を受けられる医療機関があるかを、厚生労働省の[医療施設調査](https://www.mhlw.go.jp/toukei/list/79-1.html)で市区町村ごとに集計しました。

## 入院できる場所が無い市町村は、2014年以降は毎年増えている

医療施設調査は、毎年10月1日現在の病院・診療所の数と病床数を集計する統計で、Queria の[医療施設数のテーブル](/datasets/queria/e_stat/medical_facility/municipality_facility)は2008年から2024年まで（2013年を除く16年分）の市区町村ごとの値を収録しています。この記事では次の列を使います。

| 列                          | 内容                               |
| --------------------------- | ---------------------------------- |
| `hospitals`                 | 病院数（病床20床以上）             |
| `general_clinics_with_beds` | 有床の一般診療所数（病床19床以下） |
| `general_clinics`           | 一般診療所数（有床と無床の合計）   |
| `general_clinic_beds`       | 一般診療所の病床数                 |

病院が0の市町村を、有床診療所があるかどうかで2つに分けて集計しました。施設は所在地の市町村で集計しているので、「入院できる場所が無い」は、入院先が町の外にしか無いという意味です。

```chart caption="病院が無い市区町村の数（各年10月1日現在）"
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"fold": ["no_bed", "clinic_beds_only"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"no_bed\": \"病院も有床診療所も無い\", \"clinic_beds_only\": \"病院は無いが有床診療所はある\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"no_bed\",\"clinic_beds_only\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["病院も有床診療所も無い", "病院は無いが有床診療所はある"], "range": ["#ef4444", "#fca5a5"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "year", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

病院が無い市区町村の数は、2008年の451から2024年の450までほとんど変わっていません。そのうち有床診療所で入院を受けられる市町村が201から126に減り、病院も有床診療所も無い市町村が250から324に増えました。2014年以降は前の年より減った年がありません。

2008年から2011年にかけては合併で市区町村の数が1,956から1,896に減っています。町村が隣の市町村と合併すると施設を集計する範囲が広がるので、合併はこの数を減らす方向に働くと考えられます。合併があっても、この数は増えています。

2010年と2024年の両方に同じコードで残る1,877市区町村で比較すると、2010年には入院できる場所があり2024年には無くなったのが89、2010年には無く2024年にはあるのが8でした。無くなった89のうち72は、2010年の時点ですでに病院が無く、有床診療所だけで入院を受けていた市町村です。

## 全国の有床診療所は、16年で11,500から5,415に減った

病院と有床診療所の全国の数を、2008年を100として並べました。

```chart caption="病院と有床診療所の全国の数（2008年=100）"
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"hospitals_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "hospitals", "type": "quantitative"},
          {"field": "year", "type": "quantitative"},
          {"field": "hospitals_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 2}
        },
        "y": {
          "field": "hospitals_index",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2008年=100", "grid": true}
        },
        "color": {
          "datum": "病院",
          "type": "nominal",
          "scale": {"domain": ["病院", "有床診療所"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"bed_clinics_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "bed_clinics", "type": "quantitative"},
          {"field": "year", "type": "quantitative"},
          {"field": "bed_clinics_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 2}
        },
        "y": {
          "field": "bed_clinics_index",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2008年=100", "grid": true}
        },
        "color": {
          "datum": "有床診療所",
          "type": "nominal",
          "scale": {"domain": ["病院", "有床診療所"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

病院は2008年の8,794から2024年の8,060へ8.3%減り、有床診療所は11,500から5,415へ52.9%減りました。病床数では、一般診療所の病床は2008年の146,568床から2024年の72,451床に減っています。医療施設調査の病床数は許可を受けた病床の数で、休んでいる病床も含むので、実際に入院を受けている診療所はこれより少ない可能性があります。

## 人口5,000人未満の市町村の61%、1万〜2万人の市町村の16%に、入院できる場所が無い

2024年の医療施設調査と2025年の国勢調査を市区町村コードで結合し、人口の規模ごとに、入院できる場所が無い市区町村の割合を算出しました。施設は2024年、人口は2025年の値です。

```chart caption="人口規模別、病院も有床診療所も無い市区町村の割合（施設は2024年、人口は2025年国勢調査）"
{
  "layer": [
    {
      "data": {"name": "size"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "size_class", "type": "nominal"},
          {"field": "share", "type": "quantitative"}
        ],
        "x": {
          "field": "size_class",
          "type": "nominal",
          "axis": {"title": "2025年の人口", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "share",
          "type": "quantitative",
          "scale": {"domain": [0, 75], "zero": false, "nice": false},
          "axis": {"title": "病院も有床診療所も無い割合（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "size"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "size_class",
          "type": "nominal",
          "axis": {"title": "2025年の人口", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "share",
          "type": "quantitative",
          "scale": {"domain": [0, 75], "zero": false, "nice": false},
          "axis": {"title": "病院も有床診療所も無い割合（%）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

人口5,000人未満の320市町村では、195（61%）に入院できる場所がありません。5,000〜1万人では32%、1万〜2万人でも16%です。2万人以上になると1,051のうち7まで減ります。

入院できる場所が無い324市町村に住む人は、2025年の国勢調査で合わせて177万2,177人です。このうち町村321に住む人では、年齢の分かる人に占める65歳以上の割合は39.0%で、入院できる場所がある町村（35.3%）より高くなっています。入院できる場所がある市・区では29.0%です。

人口が1万5,000人以上で入院できる場所が無い市町村は19あります。米原市・潮来市・鳥羽市の3市のほか、奈良県広陵町・平群町、大阪府豊能町、京都府大山崎町、愛知県豊山町のような大都市圏の町も含まれます。

```sql
SELECT 市町村, 人口_2025年, 一般診療所数_2024年
FROM big_towns
```

表のどの市町村にも無床の一般診療所が5つ以上あり、外来の受診は町の中でできます。入院が必要になったときは、町の外の病院へ移ることになります。

下の地図は、奈良県広陵町の代表点（アドレス・ベース・レジストリで町に付けられている位置）から半径3kmの範囲です。範囲に住む人の数と年齢構成が表示されます。地図をクリックすると中心が移動するので、自分の町の役場の位置に変更できます。町の中心から3kmの範囲に住む65歳以上の人の数から、入院が必要になったときに町の外の病院へ移ることになる人の規模を見積もれます。円が隣の市町村にかかる場合は、その住民も集計に含まれます。

```map
type: around
lng: 135.750842
lat: 34.54274
radius: 3000
caption: 奈良県広陵町の代表点から半径3km
```

## 町村の在宅医療・介護連携の計画での使い方

- 自分の町と隣の町について、病院数と有床診療所数を年ごとに並べ、0になった年を確認できます。入退院支援のルールを作った年が0になった年より前なら、そのルールは町の中での入院を前提にしている可能性があるので、受け入れ先に町の外の病院が含まれているかを確認する必要があります
- 人口1万〜2万人の市町村でも、6つに1つは町の中で入院できません。人口規模の近い町の取り組みを参考にするときは、その町に入院できる場所があるかを先に確認すると、前提の異なる事例を除けます
- 病院が無く、有床診療所だけで入院を受けている町では、その診療所が病床を廃止すると入院できる場所が無くなります。入院できる場所がなくなった市町村の多くはこの状況でした。町に残る有床診療所が病床を続けられる見通しを、その診療所や地域の医師会に早めに確認しておくと、町の外の入院先との調整を前もって始められます

## データの出典

本記事は厚生労働省の[医療施設調査](https://www.mhlw.go.jp/toukei/list/79-1.html)の市区町村別の病院数・一般診療所数（各年10月1日現在）と、総務省統計局の[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)の市区町村別人口・年齢別人口を、2026-11-05 時点で集計しています。施設は2024年、人口は2025年の値で、時点が1年異なります。

Queriaは、医療施設調査や国勢調査を、列名・単位・地域コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[医療施設数のテーブル](/datasets/queria/e_stat/medical_facility/municipality_facility)と[2025年国勢調査の年齢別人口のテーブル](/datasets/queria/e_stat/census/census_municipality_age_2025)から、自分の町と近隣の町の病院・有床診療所の数の推移を確認できます。

```sql id=trend
-- 病院が0の市区町村を、有床の一般診療所の有無で分けて年ごとに数える
SELECT
  survey_year AS year,
  count(*) FILTER (WHERE hospitals = 0 AND general_clinics_with_beds = 0) AS no_bed,
  count(*) FILTER (WHERE hospitals = 0 AND general_clinics_with_beds > 0) AS clinic_beds_only,
  count(*) FILTER (WHERE hospitals = 0) AS no_hospital,
  count(*) AS municipalities
FROM e_stat.medical_facility.municipality_facility
WHERE area_level = 'municipality'
GROUP BY survey_year
ORDER BY survey_year
```

```sql id=national
-- 病院と有床の一般診療所の全国の数（都道府県の行の合計）と、2008年を100とした指数
WITH t AS (
  SELECT
    survey_year AS year,
    CAST(sum(hospitals) AS BIGINT) AS hospitals,
    CAST(sum(general_clinics_with_beds) AS BIGINT) AS bed_clinics,
    CAST(sum(general_clinic_beds) AS BIGINT) AS clinic_beds
  FROM e_stat.medical_facility.municipality_facility
  WHERE area_level = 'prefecture'
  GROUP BY survey_year
)
SELECT
  year, hospitals, bed_clinics, clinic_beds,
  round(CAST(hospitals AS DOUBLE) * 100 / first_value(hospitals) OVER (ORDER BY year), 1) AS hospitals_index,
  round(CAST(bed_clinics AS DOUBLE) * 100 / first_value(bed_clinics) OVER (ORDER BY year), 1) AS bed_clinics_index
FROM t
ORDER BY year
```

```sql id=transition
-- 2010年と2024年の両方に同じコードで残る市区町村で、入院できる場所の有無の変化を数える（プロットはしない）
WITH a AS (
  SELECT area_code, hospitals AS h, general_clinics_with_beds AS b
  FROM e_stat.medical_facility.municipality_facility
  WHERE area_level = 'municipality' AND survey_year = 2010
),
z AS (
  SELECT area_code, hospitals AS h, general_clinics_with_beds AS b
  FROM e_stat.medical_facility.municipality_facility
  WHERE area_level = 'municipality' AND survey_year = 2024
)
SELECT
  count(*) AS municipalities,
  count(*) FILTER (WHERE a.h + a.b > 0 AND z.h + z.b = 0) AS lost,
  count(*) FILTER (WHERE a.h + a.b > 0 AND z.h + z.b = 0 AND a.h = 0) AS lost_clinic_only,
  count(*) FILTER (WHERE a.h + a.b > 0 AND z.h + z.b = 0 AND a.h > 0) AS lost_had_hospital,
  count(*) FILTER (WHERE a.h + a.b = 0 AND z.h + z.b > 0) AS gained
FROM a JOIN z USING (area_code)
```

```sql id=joined
-- 2024年の施設数と2025年国勢調査の人口・65歳以上人口を市区町村コードで結ぶ
WITH f AS (
  SELECT area_code, hospitals, general_clinics_with_beds, general_clinics
  FROM e_stat.medical_facility.municipality_facility
  WHERE area_level = 'municipality' AND survey_year = 2024
),
c AS (
  SELECT area, area_name, area_level, population
  FROM e_stat.census.census_municipality_2025
  WHERE area_level IN ('city', 'ward', 'town_village')
),
pref AS (
  SELECT area, area_name AS pref_name
  FROM e_stat.census.census_municipality_2025
  WHERE area_level = 'prefecture'
),
age AS (
  SELECT
    area,
    sum(CASE WHEN age_from >= 65 THEN population ELSE 0 END) AS pop65,
    sum(CASE WHEN age_from IS NOT NULL THEN population ELSE 0 END) AS pop_known
  FROM e_stat.census.census_municipality_age_2025
  GROUP BY area
)
SELECT
  f.area_code, pref.pref_name, c.area_name, c.area_level, c.population,
  f.hospitals, f.general_clinics_with_beds, f.general_clinics,
  (f.hospitals + f.general_clinics_with_beds = 0) AS no_bed,
  age.pop65, age.pop_known
FROM f
JOIN c ON c.area = f.area_code
JOIN age ON age.area = f.area_code
JOIN pref ON pref.area = left(f.area_code, 2) || '000'
```

```sql id=summary
-- 入院できる場所の有無 × 市・町村の別に、団体数・人口・65歳以上の割合を出す（プロットはしない）
SELECT
  no_bed,
  CASE WHEN area_level = 'town_village' THEN '町村' ELSE '市・区' END AS kind,
  count(*) AS municipalities,
  CAST(sum(population) AS BIGINT) AS population,
  round(CAST(sum(pop65) AS DOUBLE) * 100 / sum(pop_known), 1) AS share_65_over
FROM joined
GROUP BY ALL
ORDER BY no_bed, kind
```

```sql id=size
-- 2025年の人口規模別に、病院も有床診療所も無い市区町村の割合を出す
SELECT
  CASE
    WHEN population < 5000 THEN '5,000人未満'
    WHEN population < 10000 THEN '5,000〜1万人'
    WHEN population < 20000 THEN '1万〜2万人'
    ELSE '2万人以上'
  END AS size_class,
  min(population) AS sort_key,
  count(*) AS municipalities,
  count(*) FILTER (WHERE no_bed) AS no_bed,
  round(CAST(count(*) FILTER (WHERE no_bed) AS DOUBLE) * 100 / count(*), 1) AS share,
  CAST(count(*) FILTER (WHERE no_bed) AS VARCHAR) || ' / ' || CAST(count(*) AS VARCHAR) AS label
FROM joined
GROUP BY 1
ORDER BY sort_key
```

```sql id=big_towns
-- 病院も有床診療所も無い市区町村のうち、2025年の人口が1万5,000人以上のもの
SELECT
  pref_name || ' ' || area_name AS 市町村,
  population AS 人口_2025年,
  general_clinics AS 一般診療所数_2024年
FROM joined
WHERE no_bed AND population >= 15000
ORDER BY population DESC
```

```sql id=map_point
-- 地図の中心にした広陵町の代表点（プロットはしない）
SELECT pref_name, city_name, lng, lat
FROM geocoder.main.city
WHERE lg_code = '294268'
```
