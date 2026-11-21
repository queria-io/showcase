---
title: 東京都の認可保育所は営利法人の運営が38.8%で最も多く、中央区では71.4%
description: 東京都の認可保育所3,581施設を運営主体別に集計しました。施設数では営利法人が38.8%で最も多いものの、1園あたりの定員が小さく、認可定員では社会福祉法人が39.7%で最も多くなっています。営利法人が運営する施設の割合は、中央区の71.4%から多摩地域の0%まで差があります
publishedAt: 2026-07-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 保育
  - 子育て
  - 東京都
  - オープンデータ
datasets:
  - queria/metro_tokyo
  - queria/nlftp
sources:
  - title: 東京都オープンデータカタログサイト
    url: https://portal.data.metro.tokyo.lg.jp/
    publisher: 東京都
agentHint: 公立(establisher_typeが区市町村)の認可保育所の比率を市区町村別に出して、営利法人が多い都心と対照的に公立が担い手になっている地域を確かめて
socialAnnounce: |-
  東京都の認可保育所3,581件を運営主体別に数えました。

  施設数は営利法人が最多ですが1園あたりは小さく、定員では社会福祉法人が最大。営利法人比率は中央区71%〜多摩0%と開きます。
  Queriaは行政のオープンデータを整えて公開しています。
---

東京都の認可保育所3,581施設のうち、営利法人が運営する施設は1,388施設（38.8%）で、運営主体の中で最も多くなっています。営利法人の園の平均定員は69.4人で、社会福祉法人の99.2人、公立の105.0人より小さく、認可定員の合計では社会福祉法人が39.7%で最も多くなります。営利法人が運営する施設の割合は市区町村によって異なり、中央区の71.4%から、日野市・国立市などの0%まで差があります。

認可保育所は、かつては社会福祉法人と自治体が主に運営していました。2000年に株式会社などの営利法人の参入が認められ、待機児童の解消を急ぐ都市部を中心に、企業が運営する保育所が増えました。東京では、駅の近くのビルの一室を借りた小規模な園が数多く開設されています。

この記事では、[東京都オープンデータカタログ](https://portal.data.metro.tokyo.lg.jp/)が公開する東京都福祉局「社会福祉施設等一覧」（令和7年5月1日時点）から、都内の認可保育所3,581施設を運営主体別に集計します。施設ごとに設置主体・所在地・認可定員が記録されているので、運営主体の構成と地域による違いを施設単位で集計できます。対象は認可保育所で、認可外保育施設や認定こども園、幼稚園は含みません。

## 施設数は営利法人が38.8%で最も多く、認可定員は社会福祉法人が39.7%で最も多い

都内3,581施設を設置主体で4つに分けました。設置主体は「営利法人」「社福法人（社会福祉法人）」「区市町村（公立）」のほか、公益法人・学校法人・医療法人などが少数あり、数の少ない主体は「その他」にまとめています。

| 運営主体       | 施設数 | 施設数の割合 | 認可定員の割合 | 平均定員 |
| -------------- | -----: | -----------: | -------------: | -------: |
| 営利法人       |  1,388 |        38.8% |          30.6% |   69.4人 |
| 社会福祉法人   |  1,261 |        35.2% |          39.7% |   99.2人 |
| 公立(区市町村) |    756 |        21.1% |          25.2% |  105.0人 |
| その他         |    176 |         4.9% |           4.5% |   79.8人 |

施設数では営利法人が最も多く、全体の38.8%です。1園あたりの認可定員は営利法人が69.4人で最も小さく、社会福祉法人（99.2人）や公立（105.0人）とは30人以上の差があります。この規模の違いにより、施設数と定員では運営主体の順位が入れ替わります。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "mix"},
      "transform": [
        {"fold": ["pct_n", "pct_cap"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"pct_n\": \"施設数の割合\", \"pct_cap\": \"認可定員の割合\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"pct_n\",\"pct_cap\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "grp",
          "type": "nominal",
          "axis": {"title": "運営主体", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["施設数の割合", "認可定員の割合"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["施設数の割合", "認可定員の割合"]},
        "tooltip": [
          {"field": "grp", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

営利法人は施設数の割合（38.8%）が定員の割合（30.6%）を上回り、社会福祉法人は施設数の割合（35.2%）より定員の割合（39.7%）が大きくなっています。営利法人は施設の数が多く1園あたりの規模が小さく、社会福祉法人は施設の数は営利法人に次ぐものの、定員の大きい園を運営しています。定員の合計では、社会福祉法人が最も多くの子どもを受け入れています。

## 営利法人が運営する施設の割合は、都心の区で高く、多摩地域の市で低い

各施設の所在地から区市町村を取り出し、認可保育所が10施設以上ある49市区町村について、営利法人が運営する施設の割合（営利法人比率）を計算しました。所在地は「千代田区外神田…」のように都道府県名を含まない形式なので、[国土数値情報の市区町村境界](/datasets/queria/nlftp/boundary/municipality)の市区町村名が所在地の文字列に含まれるかどうかで照合しています。認可保育所が10施設未満の島しょ部などは対象外です。色が濃いほど営利法人比率が高い市区町村です。

```map
type: map
layers:
  - from: ward_map
    geojson: geojson
    color: value
    label: muni
    name: "営利法人比率（%）"
lng: 139.5
lat: 35.72
zoom: 9.2
```

営利法人比率が高いのは、中央区・文京区・新宿区・港区といった都心部の区です。地図の西側の多摩地域の市では色が薄く、営利法人が運営する認可保育所がほとんど、またはまったくない市もあります。49市区町村の営利法人比率の中央値は29.5%で、都心から郊外へ向かうにつれて下がる傾向があります。

## 営利法人比率は中央区の71.4%が最も高く、23区では世田谷区の20.9%が最も低い

認可保育所が10施設以上ある49市区町村を、営利法人比率の高い順に並べました。

```chart
{
  "height": 1030,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "muni", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"domain": [0, 80], "zero": false, "nice": false},
          "axis": {"title": "営利法人比率（%）", "grid": true}
        },
        "y": {"field": "muni", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "muni", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"domain": [0, 80], "zero": false, "nice": false},
          "axis": {"title": "営利法人比率（%）", "grid": true}
        },
        "y": {"field": "muni", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "muni", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"domain": [0, 80], "zero": false, "nice": false},
          "axis": {"title": "営利法人比率（%）", "grid": true}
        },
        "y": {"field": "muni", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは中央区の71.4%で、認可保育所の7割超を営利法人が運営しています。小金井市（63.6%）、文京区（62.5%）、新宿区（61.8%）、港区（59.8%）と続き、上位は都心部の区が占めます。多摩地域の市はいずれも低く、八王子市（5.7%）、町田市（5.3%）、立川市（2.8%）のほか、日野市・国立市・武蔵村山市・羽村市など営利法人比率が0%の市もあります。これらの市では、認可保育所を営利法人以外の主体が運営しています。

23区の中では世田谷区が20.9%で最も低く、認可保育所の8割近くを営利法人以外が運営しています。同じ23区でも、待機児童対策として企業が運営する園をどれだけ受け入れてきたかによって、運営主体の構成に差があると考えられます。

## まとめ

東京都の認可保育所を運営主体別に集計した結果は次のとおりです。

- 施設数では営利法人が38.8%で最も多いものの、1園あたりの定員が小さく、定員の合計では社会福祉法人（39.7%）が最も多い
- 営利法人比率は市区町村によって0%から71.4%まで差があり、都心部の区で高く、多摩地域の市で低い
- 世田谷区のように、23区でも営利法人比率が2割程度の区がある

## データの出典

本記事は[東京都オープンデータカタログサイト](https://portal.data.metro.tokyo.lg.jp/)が公開する東京都福祉局「社会福祉施設等一覧」（令和7年5月1日時点）の認可保育所3,581施設を、2026年7月17日時点で取得して集計しています。

Queriaは、東京都などの行政のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[認可保育所テーブル](/datasets/queria/metro_tokyo/childcare/nursery_school)には、設置主体・認可定員に加えて施設ごとの緯度経度も含まれており、特定の自治体の園の一覧や、定員規模別の分布を集計したり、園の立地を地図で確認したりできます。

```sql id=mix
WITH g AS (SELECT CASE WHEN establisher_type = '営利法人' THEN '営利法人' WHEN establisher_type = '社福法人' THEN '社会福祉法人' WHEN establisher_type = '区市町村' THEN '公立(区市町村)' ELSE 'その他' END AS grp, capacity FROM metro_tokyo.childcare.nursery_school) SELECT grp, COUNT(*) AS n, ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_n, ROUND(100.0 * SUM(capacity) / SUM(SUM(capacity)) OVER (), 1) AS pct_cap, ROUND(AVG(capacity), 1) AS avg_cap FROM g GROUP BY grp ORDER BY n DESC
```

```sql id=ward_map
WITH j AS (SELECT b.city_name AS muni, n.establisher_type AS et FROM metro_tokyo.childcare.nursery_school n JOIN nlftp.boundary.municipality b ON b.prefecture_name = '東京都' AND CONTAINS(n.address, b.city_name)), agg AS (SELECT muni, COUNT(*) AS total, ROUND(100.0 * SUM((et = '営利法人')::INT) / COUNT(*), 1) AS pct FROM j GROUP BY muni HAVING COUNT(*) >= 10) SELECT agg.muni, ST_AsGeoJSON(ST_Simplify(b.geometry, 0.001)) AS geojson, agg.pct AS value, ROW_NUMBER() OVER (ORDER BY agg.muni) - 1 AS row_id FROM agg JOIN nlftp.boundary.municipality b ON b.prefecture_name = '東京都' AND b.city_name = agg.muni
```

```sql id=rank_top
WITH j AS (SELECT b.city_name AS muni, n.establisher_type AS et FROM metro_tokyo.childcare.nursery_school n JOIN nlftp.boundary.municipality b ON b.prefecture_name = '東京都' AND CONTAINS(n.address, b.city_name)), agg AS (SELECT muni, COUNT(*) AS total, ROUND(100.0 * SUM((et = '営利法人')::INT) / COUNT(*), 1) AS pct FROM j GROUP BY muni HAVING COUNT(*) >= 10), ranked AS (SELECT muni, pct, ROW_NUMBER() OVER (ORDER BY pct DESC, muni) AS rn FROM agg) SELECT muni, pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH j AS (SELECT b.city_name AS muni, n.establisher_type AS et FROM metro_tokyo.childcare.nursery_school n JOIN nlftp.boundary.municipality b ON b.prefecture_name = '東京都' AND CONTAINS(n.address, b.city_name)), agg AS (SELECT muni, COUNT(*) AS total, ROUND(100.0 * SUM((et = '営利法人')::INT) / COUNT(*), 1) AS pct FROM j GROUP BY muni HAVING COUNT(*) >= 10), ranked AS (SELECT muni, pct, ROW_NUMBER() OVER (ORDER BY pct DESC, muni) AS rn FROM agg) SELECT muni, pct FROM ranked WHERE rn > 10 AND rn <= 39 ORDER BY rn
```

```sql id=rank_bottom
WITH j AS (SELECT b.city_name AS muni, n.establisher_type AS et FROM metro_tokyo.childcare.nursery_school n JOIN nlftp.boundary.municipality b ON b.prefecture_name = '東京都' AND CONTAINS(n.address, b.city_name)), agg AS (SELECT muni, COUNT(*) AS total, ROUND(100.0 * SUM((et = '営利法人')::INT) / COUNT(*), 1) AS pct FROM j GROUP BY muni HAVING COUNT(*) >= 10), ranked AS (SELECT muni, pct, ROW_NUMBER() OVER (ORDER BY pct DESC, muni) AS rn FROM agg) SELECT muni, pct FROM ranked WHERE rn > 39 ORDER BY rn
```
