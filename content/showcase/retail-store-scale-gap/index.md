---
title: 小売業の1店舗あたり販売額は、東京都が高知県の約2.7倍
description: 小売業の事業所数・従業者数・年間商品販売額を都道府県別に集計しました。1事業所あたりの従業者数は1976年の約3.5人から2021年の約8.6人に増えています。2021年の1店舗あたり販売額は東京都が高知県の約2.7倍で、従業者1人あたり販売額の差は約1.6倍でした。
ogDescription: 小売業の1事業所あたりの従業者数は1976年の約3.5人から2021年の約8.6人に増えました。2021年の1店舗あたり販売額は東京都が高知県の約2.7倍です。
publishedAt: 2026-06-03
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 小売業
  - 店舗開発
  - 経済
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 経済センサス
    url: https://www.stat.go.jp/data/e-census/index.html
    publisher: 総務省統計局
agentHint: 1事業所あたり従業者数（C350302÷C350202）を2021年の都道府県別に出して、1店舗あたり販売額（C350102）の順位と揃うか比べて
socialAnnounce: |-
  全国の小売業データで、店舗の大型化と都道府県ごとの店舗規模・労働生産性の差を分析しました。

  出店フォーマットの選定やエリア戦略の検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2021年の小売業の1店舗あたりの年間商品販売額は、東京都の約300百万円が最も大きく、最も小さい高知県の約110百万円の約2.7倍でした。従業者1人あたりの販売額の差は、東京都と奈良県で約1.6倍です。全国の小売業の事業所数は1982年の約172万店から2021年の約76万店へ半分以下に減り、1事業所あたりの従業者数は1976年の約3.5人から2021年の約8.6人に増えています。

小売チェーンやフランチャイズ本部が出店先を決めるときは、その地域に合う店の規模を判断する必要があります。同じ商圏人口でも、大型店が成り立つ地域と、小型店を多く配置したほうがよい地域があります。e-Stat「[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)」の都道府県別データを使い、小売業の店舗の規模の変化と、都道府県ごとの差を集計しました。使ったのは経済基盤の3指標です。

| コード  | 内容                           |
| ------- | ------------------------------ |
| C350202 | 小売業事業所数（店舗数）       |
| C350302 | 小売業従業者数                 |
| C350102 | 小売業年間商品販売額（百万円） |

これらは商業統計調査（古い年次）と[経済センサス](https://www.stat.go.jp/data/e-census/index.html)（近年）をもとに作られた指標です。調査の枠組みが切り替わった年（おおむね2007年から2011年）の前後では値が連続しないため、単年の増減ではなく長期的な傾向を見ます。

## 店舗数はピークの半分以下に減り、従業者数はピークの約8割を保っている

全国の小売業事業所数と従業者数の推移です。横軸の点は調査年だけで、1976年から2021年までの16時点です。

```chart
{
  "layer": [
    {
      "data": {"name": "store_emp_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"est_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "est_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "est_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "万（事業所数・従業者数）", "grid": true}
        },
        "color": {
          "datum": "事業所数（万店）",
          "type": "nominal",
          "scale": {"domain": ["事業所数（万店）", "従業者数（万人）"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "store_emp_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"emp_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "emp_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "emp_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "万（事業所数・従業者数）", "grid": true}
        },
        "color": {
          "datum": "従業者数（万人）",
          "type": "nominal",
          "scale": {"domain": ["事業所数（万店）", "従業者数（万人）"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

小売業の事業所数は1982年の約172万店がピークで、その後は減少が続き、2021年には約76万店とピークの半分以下になりました。2016年から2021年の99.0万店から75.5万店への減少には、実際の閉店と調査方法の変更の両方が含まれます。従業者数は1999年の約803万人がピークで、2021年も約646万人です。店舗数が大きく減ったのに対して従業者数はそれほど減っていないので、1店舗あたりの規模が大きくなっていると考えられます。

## 1事業所あたりの従業者数は、約3.5人から約8.6人に増えた

従業者数を事業所数で割り、1事業所あたりの従業者数を計算しました。

```chart
{
  "layer": [
    {
      "data": {"name": "emp_per_store"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"emp_per_est\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#7c3aed"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "emp_per_est", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "emp_per_est",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1事業所あたり従業者数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1事業所あたりの従業者数は、1976年の約3.5人から2021年の約8.6人へ増え続けています。家族経営の小規模店が減り、チェーンの大型店やスーパー、ホームセンターなどが小売の中心になってきたためと考えられます。出店計画では、全国的に店舗が大型化していることを前提にします。

## 従業者1人あたりの販売額は、最も高い東京都と最も低い奈良県で約1.6倍

2021年の都道府県別データで地域差を比較します。小売業の労働生産性として、年間商品販売額（C350102）を従業者数（C350302）で割り、従業者1人あたりの年間商品販売額を計算しました。全国の行を除いた47都道府県を、上位10・中位・下位10の3色で示します。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "prod_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "prod", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "prod",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者1人あたり年間商品販売額（百万円）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中位", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "prod_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "prod", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "prod",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者1人あたり年間商品販売額（百万円）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中位",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中位", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "prod_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "prod", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "prod",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者1人あたり年間商品販売額（百万円）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中位", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは東京都の約28.0百万円で、北海道、宮城県、栃木県、愛知県が続きます。最も低い奈良県は約17.1百万円で、差は約1.6倍です。小売業は消費地で商品を販売するので、従業者1人あたりの販売額は地域による差が小さいと考えられます。

## 1店舗あたりの販売額は、東京都が高知県の約2.7倍

年間商品販売額を事業所数で割った1店舗あたりの販売額では、地域差が大きくなります。このデータには売場面積が入っていないので、店舗の規模は1店舗あたりの販売額で表しています。都心の高単価の店と郊外の大型店は、この指標では区別できません。都道府県別の値を地図にしました。

```map
type: map
layers:
  - from: store_scale_map
    geojson: geojson
    color: z_val
    label: pref_name
    name: "百万円/店"
lng: 137
lat: 36.5
zoom: 4
```

1店舗あたりの販売額は、東京都の約300百万円が最も大きく、神奈川県、千葉県、埼玉県、愛知県、北海道、大阪府が続きます。最も小さい高知県は約110百万円で、差は約2.7倍です。従業者1人あたりの販売額の差（約1.6倍）より大きくなっています。

東京都と近隣の神奈川県・埼玉県・千葉県が上位に並ぶのは、人口が集中していて、郊外型の大型店が成り立ちやすいためと考えられます。人口が分散する地方では、1店舗あたりの規模は小さくなります。同じチェーンでも、地域によって標準店の規模を変える必要があります。

## 1店舗あたりの販売額が大きい都道府県ほど、従業者1人あたりの販売額も高い

横軸を1店舗あたり販売額、縦軸を従業者1人あたり販売額にした散布図です。

```chart
{
  "layer": [
    {
      "data": {"name": "scale_prod_scatter"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "scale", "type": "quantitative"},
          {"field": "prod", "type": "quantitative"}
        ],
        "x": {
          "field": "scale",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1店舗あたり販売額（百万円）", "grid": true}
        },
        "y": {
          "field": "prod",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "従業者1人あたり販売額（百万円）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scale_prod_scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "scale",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1店舗あたり販売額（百万円）", "grid": true}
        },
        "y": {
          "field": "prod",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "従業者1人あたり販売額（百万円）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

1店舗あたり販売額が大きい都道府県ほど、従業者1人あたり販売額も高くなっています。右上に東京都が離れて位置し、神奈川県・埼玉県・千葉県・愛知県・大阪府といった大都市圏が続きます。左下には高知県や和歌山県など、1店舗あたり販売額が小さく、従業者1人あたり販売額も低い県が並びます。大型店では省人化した売場運営やセルフレジ、効率的な物流を導入しやすく、従業者1人あたりの販売額が高くなると考えられます。地域の1店舗あたり販売額の水準は、その地域で見込める労働生産性の目安になります。

## 出店計画での使い方

- 標準店の規模の地域別の調整: 1店舗あたり販売額の地図から、大型店が成り立ちやすい地域と小型店が中心の地域を分け、出店する店の規模を地域に合わせる
- 投資判断の目安: 1店舗あたり販売額の水準を、その地域で見込める売上規模の基準にする
- 人員計画: 1事業所あたり従業者数の推移をもとに、店舗の大型化に合わせた人員配置・採用計画を立てる
- 競合環境の把握: 事業所数の推移から、店舗の減少が大きい地域を確認し、新規出店の余地を評価する

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)に収録された都道府県別経済データを、2026年7月11日時点で集計しています。元データは古い年次が商業統計調査、近年が[経済センサス](https://www.stat.go.jp/data/e-census/index.html)で、2021年までの値を使っています。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の経済基盤データ](/datasets/queria/e_stat/ssds/c_pref_economy)から、出店を検討している地域の1店舗あたり販売額や従業者1人あたり販売額を確認できます。

```sql id=store_emp_trend
WITH est AS (SELECT year, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350202' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year), emp AS (SELECT year, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350302' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year) SELECT e.year, ROUND(e.v / 10000, 1) AS est_man, ROUND(m.v / 10000, 0) AS emp_man FROM est e JOIN emp m ON e.year = m.year WHERE e.year <= 2021 ORDER BY e.year
```

```sql id=emp_per_store
WITH est AS (SELECT year, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350202' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year), emp AS (SELECT year, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350302' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year) SELECT e.year, ROUND(m.v / e.v, 2) AS emp_per_est FROM est e JOIN emp m ON e.year = m.year WHERE e.year <= 2021 ORDER BY e.year
```

```sql id=prod_top
WITH sales AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350102' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), emp AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350302' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT s.area_name, ROUND(s.v / e.v, 1) AS prod, ROW_NUMBER() OVER (ORDER BY s.v / e.v DESC, s.area_name) AS rn FROM sales s JOIN emp e ON s.area_name = e.area_name) SELECT area_name, prod FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=prod_mid
WITH sales AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350102' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), emp AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350302' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT s.area_name, ROUND(s.v / e.v, 1) AS prod, ROW_NUMBER() OVER (ORDER BY s.v / e.v DESC, s.area_name) AS rn FROM sales s JOIN emp e ON s.area_name = e.area_name) SELECT area_name, prod FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=prod_bottom
WITH sales AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350102' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), emp AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350302' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT s.area_name, ROUND(s.v / e.v, 1) AS prod, ROW_NUMBER() OVER (ORDER BY s.v / e.v DESC, s.area_name) AS rn FROM sales s JOIN emp e ON s.area_name = e.area_name) SELECT area_name, prod FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=store_scale_map
WITH sales AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350102' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), est AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350202' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT ST_AsGeoJSON(p.geometry) AS geojson, ROUND(s.v / e.v, 0) AS z_val, p.prefecture_name AS pref_name FROM nlftp.boundary.prefecture p JOIN sales s ON p.prefecture_name = s.area_name JOIN est e ON p.prefecture_name = e.area_name
```

```sql id=scale_prod_scatter
WITH sales AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350102' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), emp AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350302' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), est AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C350202' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT s.area_name, ROUND(s.v / es.v, 0) AS scale, ROUND(s.v / e.v, 1) AS prod FROM sales s JOIN emp e ON s.area_name = e.area_name JOIN est es ON s.area_name = es.area_name
```
