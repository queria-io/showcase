---
title: 全域が過疎地域の83市町村にも市街地があり、函館市では21.6万人が住む
description: 過疎地域に指定された816市町村の区域と、国勢調査の人口集中地区を重ねました。全域が指定された83市町村には市街地があり1,532,897人が住み、京都市は市域の26.3%が過疎地域です。
ogDescription: 過疎地域に指定された816市町村の区域と、国勢調査の人口集中地区を重ねました。全域が指定された83市町村には市街地があり、1,532,897人が住んでいます。
publishedAt: 2026-09-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 過疎地域
  - 人口集中地区
  - 立地
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 過疎地域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A17-v4_0.html
    publisher: 国土交通省
  - title: 国土数値情報 人口集中地区データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A16-v2_3.html
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
  - title: 社会・人口統計体系 市区町村データ
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality
    publisher: 総務省統計局
  - title: 過疎地域を対象とした税制措置等
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/c-gyousei/2001/kaso/kasomain9.htm
    publisher: 総務省
agentHint: 全域が過疎地域に指定された市町村の人口集中地区を、面積あたりの人口密度が高い順に出して。2015年と2020年で密度がどう変わったかも比べて
socialAnnounce: |-
  過疎地域データと人口集中地区データを重ねました。

  全域が過疎地域の83市町村にも市街地があり、約153万人が住んでいます。京都市は市域の26.3%が過疎地域でした。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

市町村の全域が過疎地域に指定された671市町村のうち、83市町村には人口集中地区（市街地）があり、1,532,897人が住んでいます。最も大きいのは北海道函館市の216,044人です。市域の一部だけが指定された市では、京都市が市域の26.3%、浜松市と豊田市が48.8%を過疎地域が占めています（いずれも2017年時点の指定）。

工場や物流拠点、事業所の新設先を探すときは、候補地が過疎地域に指定されているかどうかで条件が変わります。[総務省が示す過疎地域の税制措置](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/c-gyousei/2001/kaso/kasomain9.htm)では、過疎地域の中で製造業・旅館業・情報サービス業などの設備を取得した場合に、市町村が固定資産税を課税免除したときの減収を国が補てんします。そのため、指定区域かどうかで自治体が出せる条件が変わります。この記事では、[国土数値情報の過疎地域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A17-v4_0.html)と[人口集中地区データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A16-v2_3.html)を使います。どちらも区域をポリゴンで持っているので、2つを重ねると、過疎地域と市街地が重なる範囲を集計できます。

## 過疎地域は、神奈川県を除く46都道府県にある

過疎地域データ（`nlftp.region.depopulated_area`）は1行が1つの指定区域で、全国に816区域あります。指定は3つの区分に分かれていて、`category_code` で区別します。

| コード | 区分                       | 区域数 | 意味                                       |
| ------ | -------------------------- | ------ | ------------------------------------------ |
| 1      | 過疎市町村                 | 646    | 市町村の全域が過疎地域                     |
| 2      | 過疎地域とみなされる市町村 | 25     | 合併後の市町村の全域を過疎地域とみなす     |
| 3      | 過疎地域とみなされる区域   | 145    | 合併前の旧市町村にあたる区域だけが過疎地域 |

区分1と2は市町村の全域が指定されるので、合わせて671市町村の全域が過疎地域です。区分3は「一部過疎」と呼ばれ、市域の一部だけが指定されます。過疎地域コードと行政区域コードは1対1で対応するので、816区域は816市町村にあたります。

このデータは、当時の過疎地域自立促進特別措置法に基づく2017年（平成29年）時点の指定です。指定は法の改正に合わせて変わるので、以下の集計は2017年時点のもので、現在の指定は総務省の公示で確認する必要があります。

都道府県ごとの区域数です。

```map
type: map
layers:
  - from: pref_map
    geojson: geojson
    color: z_val
    label: pref_name
    name: "区域数"
lng: 137.5
lat: 38.2
zoom: 4.1
```

最も多いのは北海道の149区域で、鹿児島県41、長野県37、福島県31が続きます。指定が1つもないのは神奈川県だけで、残りの46都道府県には過疎地域があります。東京都には6区域あり、大島町・三宅村・新島村・青ヶ島村の島しょ部と、奥多摩町・檜原村が入ります。大阪府は千早赤阪村の1区域です。

## 全域が過疎地域の83市町村に市街地があり、153万人が住む

指定区域の中に市街地があるかどうかは、人口集中地区（DID）のデータで確認できます。人口集中地区は、人口密度が4,000人/km²以上の基本単位区が市区町村の中で隣り合い、合わせて人口5,000人以上になる区域で、国勢調査が市街地の範囲を面で定めたものです。ここでは令和2年（2020年）国勢調査に基づく1,463地区を使います。

全域が指定されている671市町村（区分1と2）について、その中にある人口集中地区を集計します。全域が指定されているので、これらの市町村の人口集中地区はすべて過疎地域の中にあります。

結果は83市町村・89地区で、1,532,897人が住んでいます。市街地の面積は合わせて435.4km²です。市街地の人口が多い順に並べると、上位は次のとおりです。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "did_cities"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [{"field": "pop", "type": "quantitative"}, {"field": "city", "type": "nominal"}],
        "x": {
          "field": "pop",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口集中地区の人口（人）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

最も大きいのは北海道函館市の216,044人で、釧路市148,153人、小樽市92,939人、福岡県大牟田市91,868人が続きます。いずれも市の全域が過疎地域に指定されていて、その中に十万人規模の市街地があります。山形県鶴岡市57,238人、愛媛県宇和島市29,893人、和歌山県田辺市28,986人も同じです。

過疎地域の指定は人口の減り方と財政力で決まるので、市街地がある市も指定されます。これらの市では、市街地そのものが指定区域の中にあります。

## 全域が過疎地域の市町村の市街地では、人口が5年で8.4%減った

人口集中地区データは、同じ地区の前回の国勢調査（2015年）時点の人口と面積も持っています。2015年の値が欠測の1地区を除いて比較すると、市街地の人口は1,666,170人から1,525,539人へ8.4%減りました。同じ期間に、市街地の面積は445.0km²から433.3km²へ2.6%の減少です。人口密度は3,744人/km²から3,520人/km²に下がり、市街地の範囲はほぼ変わらないまま、住む人が減っています。人口集中地区の区域は国勢調査ごとに設定し直されるので、この増減には区域が広がったり狭まったりした分も含まれます。

83市町村のうち7市町村では、市街地の人口が増えています。増えた7市町村と、減り方の大きい8市町村を並べます。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "did_change"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "chg", "type": "quantitative"}, {"field": "city", "type": "nominal"}],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市街地人口の変化率（2015年→2020年、%）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

最も増えたのは福岡県八女市の20.0%で、沖縄県宮古島市13.9%、京都府南丹市10.0%が続きます。最も減ったのは秋田県大仙市の44.4%減です。83市町村の中央値は7.6%減で、増えた7市町村は少数ですが、過疎地域に指定された市町村でも市街地の人口が増えている所があります。

## 京都市は市域の26.3%、浜松市は48.8%が過疎地域

「一部過疎」の市町村では、合併前の旧市町村にあたる区域だけが指定されるので、市の一部だけが過疎地域になります。145市町村がこれにあたります。

指定区域が市域に占める割合は、過疎地域データのポリゴンの面積を[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)の市域の面積で割って求めました。分子は2017年時点の指定区域、分母は令和7年版の市域なので、この間に市域が変わった市では、その分だけ割合がずれます。145市町村の中央値は40.4%で、最も低い広島県福山市が2.5%、最も高い大分県中津市が88.5%です。市域の半分以上が指定区域の市町村は44あります。

2020年国勢調査の人口が多い順に15市を並べます。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "partial_big"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "city", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市域に占める指定区域の割合（%）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

人口146万人の京都市は、市域の26.3%が過疎地域です。旧京北町にあたる区域が指定されています。人口79万人の浜松市は48.8%、自動車産業の集まる愛知県豊田市も48.8%で、どちらも市域のおよそ半分が指定区域です。長野市49.1%、高知市38.7%、秋田市33.3%と、県庁所在地にも3割を超える市があります。

市の名前だけで候補地を絞り、京都市や浜松市を「都市なので対象外」として除くと、同じ市の中にある指定区域を見落とします。

## 業務での使い方

ここで使った指定は2017年時点のものです。候補地を決めるときは、最新の指定を総務省の公示で確認してください。

- 候補地の分類: 候補地リストの市町村コードを過疎地域データと照合し、全域指定・一部過疎・指定なしの3区分に分ける。一部過疎の市では、区域のポリゴンと候補地の座標を重ねて、候補地が指定区域の中にあるかどうかまで判定する
- 市街地との位置関係の評価: 人口集中地区データと重ねて、候補地が市街地の中にあるかどうかで並べ替える
- 労働力の見通し: 人口集中地区の2015年と2020年の値を比較し、候補地の市街地の人口が維持されているか減っているかを確認する

## データの出典

本記事は[国土数値情報の過疎地域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A17-v4_0.html)（A17、2017年版）、[人口集中地区データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A16-v2_3.html)（A16、令和2年国勢調査）、[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)（N03、令和7年版）と、e-Stat [社会・人口統計体系の市区町村データ](https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality)の総人口（`A1101`、2020年）を2026年9月17日時点で集計しています。

Queria は、国土数値情報や e-Stat のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[過疎地域データ](/datasets/nlftp/region/depopulated_area)と[人口集中地区データ](/datasets/nlftp/boundary/did)から、候補地のある市の指定状況を確認したり、市街地との重なりを集計したりできます。

```sql id=overview
SELECT category AS label, COUNT(*) AS areas, COUNT(DISTINCT lg_code) AS lgs FROM nlftp.region.depopulated_area GROUP BY category_code, category ORDER BY category_code
```

```sql id=pref_map
SELECT ST_AsGeoJSON(ST_SimplifyPreserveTopology(b.geometry, 0.01)) AS geojson, COALESCE(k.n, 0) AS z_val, b.prefecture_name AS pref_name FROM nlftp.boundary.prefecture b LEFT JOIN (SELECT prefecture_name, COUNT(*) AS n FROM nlftp.region.depopulated_area GROUP BY prefecture_name) k ON k.prefecture_name = b.prefecture_name
```

```sql id=metro_areas
SELECT prefecture_name AS pref, municipality_name AS city, category FROM nlftp.region.depopulated_area WHERE prefecture_name IN ('東京都', '大阪府') ORDER BY prefecture_name DESC, municipality_name
```

```sql id=did_summary
WITH whole AS (SELECT DISTINCT lg_code FROM nlftp.region.depopulated_area WHERE category_code IN (1, 2)), d AS (SELECT i.* FROM nlftp.boundary.did i JOIN whole w ON w.lg_code = i.lg_code) SELECT (SELECT COUNT(*) FROM nlftp.boundary.did) AS dids_national, SUM(CASE WHEN previous_population IS NULL THEN 1 ELSE 0 END) AS no_prev, COUNT(*) AS dids, COUNT(DISTINCT lg_code) AS cities, SUM(population) AS pop_2020, ROUND(SUM(area_km2), 1) AS km2_2020, SUM(CASE WHEN previous_population IS NOT NULL THEN population END) AS pop_2020_cmp, SUM(previous_population) AS pop_2015_cmp, ROUND(SUM(CASE WHEN previous_area_km2 IS NOT NULL THEN area_km2 END), 1) AS km2_2020_cmp, ROUND(SUM(previous_area_km2), 1) AS km2_2015_cmp FROM d
```

```sql id=did_cities
WITH whole AS (SELECT DISTINCT lg_code FROM nlftp.region.depopulated_area WHERE category_code IN (1, 2)) SELECT i.prefecture_name || ' ' || i.municipality_name AS city, SUM(i.population) AS pop FROM nlftp.boundary.did i JOIN whole w ON w.lg_code = i.lg_code GROUP BY 1 ORDER BY pop DESC, city LIMIT 15
```

```sql id=did_change
WITH whole AS (SELECT DISTINCT lg_code FROM nlftp.region.depopulated_area WHERE category_code IN (1, 2)), c AS (SELECT i.prefecture_name || ' ' || i.municipality_name AS city, SUM(i.population) AS p20, SUM(i.previous_population) AS p15 FROM nlftp.boundary.did i JOIN whole w ON w.lg_code = i.lg_code WHERE i.previous_population IS NOT NULL GROUP BY 1), r AS (SELECT city, ROUND(100.0 * (p20 - p15) / CAST(p15 AS DOUBLE), 1) AS chg FROM c) SELECT city, chg FROM (SELECT city, chg, ROW_NUMBER() OVER (ORDER BY chg DESC, city) AS rn_hi, ROW_NUMBER() OVER (ORDER BY chg ASC, city) AS rn_lo FROM r) WHERE rn_hi <= 7 OR rn_lo <= 8 ORDER BY chg DESC, city
```

```sql id=did_change_summary
WITH whole AS (SELECT DISTINCT lg_code FROM nlftp.region.depopulated_area WHERE category_code IN (1, 2)), c AS (SELECT i.prefecture_name || ' ' || i.municipality_name AS city, SUM(i.population) AS p20, SUM(i.previous_population) AS p15 FROM nlftp.boundary.did i JOIN whole w ON w.lg_code = i.lg_code WHERE i.previous_population IS NOT NULL GROUP BY 1) SELECT COUNT(*) AS cities, SUM(CASE WHEN p20 > p15 THEN 1 ELSE 0 END) AS grew, ROUND(MEDIAN(100.0 * (p20 - p15) / CAST(p15 AS DOUBLE)), 1) AS median_chg FROM c
```

```sql id=partial_summary
WITH target AS (SELECT DISTINCT prefecture_name, REPLACE(municipality_name, '¥', '') AS mname FROM nlftp.region.depopulated_area WHERE category_code = 3), city AS (SELECT m.prefecture_name, m.city_name, SUM(ST_Area(m.geometry)) AS a FROM nlftp.boundary.municipality m JOIN target t ON t.prefecture_name = m.prefecture_name AND t.mname = m.city_name GROUP BY 1, 2), kaso AS (SELECT prefecture_name, REPLACE(municipality_name, '¥', '') AS mname, SUM(ST_Area(geometry)) AS a FROM nlftp.region.depopulated_area WHERE category_code = 3 GROUP BY 1, 2), shares AS (SELECT k.prefecture_name || k.mname AS full_name, 100.0 * k.a / c.a AS pct FROM kaso k JOIN city c ON c.prefecture_name = k.prefecture_name AND c.city_name = k.mname) SELECT COUNT(*) AS cities, ROUND(MEDIAN(pct), 1) AS median_pct, ROUND(MIN(pct), 1) AS min_pct, ROUND(MAX(pct), 1) AS max_pct, SUM(CASE WHEN pct >= 50 THEN 1 ELSE 0 END) AS half_or_more, ARG_MAX(full_name, pct) AS max_city, ARG_MIN(full_name, pct) AS min_city FROM shares
```

```sql id=partial_big
WITH target AS (SELECT DISTINCT prefecture_name, REPLACE(municipality_name, '¥', '') AS mname FROM nlftp.region.depopulated_area WHERE category_code = 3), city AS (SELECT m.prefecture_name, m.city_name, SUM(ST_Area(m.geometry)) AS a FROM nlftp.boundary.municipality m JOIN target t ON t.prefecture_name = m.prefecture_name AND t.mname = m.city_name GROUP BY 1, 2), kaso AS (SELECT prefecture_name, REPLACE(municipality_name, '¥', '') AS mname, SUM(ST_Area(geometry)) AS a FROM nlftp.region.depopulated_area WHERE category_code = 3 GROUP BY 1, 2), pop AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS p FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A1101' AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT k.mname AS city, ROUND(100.0 * k.a / c.a, 1) AS pct, CAST(p.p AS BIGINT) AS pop FROM kaso k JOIN city c ON c.prefecture_name = k.prefecture_name AND c.city_name = k.mname JOIN pop p ON p.area_name = k.prefecture_name || ' ' || k.mname ORDER BY p.p DESC, city LIMIT 15
```
