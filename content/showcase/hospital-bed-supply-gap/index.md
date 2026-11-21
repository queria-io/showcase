---
title: 人口あたりの病床数は、高知県が神奈川県の3.0倍
description: 国土数値情報の医療機関データを都道府県境界と空間結合し、人口10万人あたりの病床数と診療所数を比較しました。病床数は高知県の2,430床が最も多く、神奈川県の807床の約3.0倍です。診療所数は和歌山県の116.6施設が最も多く、病床数の多い県とは一致しません。
publishedAt: 2026-06-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療
  - 病床
  - 地域格差
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 医療機関データ（P04）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P04-v3_0.html
    publisher: 国土交通省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 診療所（medical_class_code=2）の人口10万人あたり施設数を都道府県別に集計して、病床数で西高東低だった順位と一致するか比べて。分母はa_pref_populationのA1101・2024年で、境界はnlftp.boundary.prefectureと空間結合して
socialAnnounce: |-
  国土数値情報の医療機関データを都道府県境界と空間結合し、人口あたりの病床数と診療所密度を比較しました。

  病床は西日本ほど多く、外来の診療所はまた別の分布です。

  病院・クリニック・介護の立地戦略に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

人口10万人あたりの病院の病床数は、高知県の2,430床が最も多く、最も少ない神奈川県の807床の約3.0倍です。上位には鹿児島県・長崎県・徳島県など西日本の県が並び、下位には埼玉県・愛知県・東京都など大都市圏が並びます。人口10万人あたりの診療所数は和歌山県の116.6施設が最も多く、病床数が最も多い高知県は中位です。病床数と診療所数の多い県は一致しません。

病院やクリニック、介護施設、調剤薬局といったヘルスケア事業の立地を検討するときは、対象地域にある医療資源の量が最初の判断材料になります。入院を受け入れる病床がどの地域に多いか、外来を受け付ける診療所がどれだけあるかの地域差から、新規開設の余地や既存施設との競合の程度を見積もれます。

病床については、医療法に基づく[基準病床数制度](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iryou/iryou_keikaku/index.html)や[地域医療構想](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000080850.html)によって、地域ごとに必要な病床数の目安が定められています。病床が過剰な地域では新規の開設が難しく、不足する地域では整備が課題になります。

## 医療機関の点データを、都道府県の境界と人口で集計する

使うのは[国土数値情報の医療機関データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P04-v3_0.html)（`nlftp.facility.medical_institution`）です。全国の医療機関が緯度経度付きの点データとして収録されており、施設ごとに病院・診療所・歯科診療所の種別（`medical_class`）、病床数（`bed_count`）、開設者種別（`establisher_type`）、診療科目（`departments`）などの列があります。

```sql
SELECT medical_class AS 種別, COUNT(*) AS 施設数, SUM(bed_count) AS 病床数 FROM nlftp.facility.medical_institution GROUP BY medical_class ORDER BY 施設数 DESC
```

施設数は診療所が最も多く、次いで歯科診療所、病院の順です。病床数は病院に集中しており、診療所の病床は一部の有床診療所に限られます。歯科診療所はほぼ無床です。入院医療の供給量は病院の病床数で、外来医療の窓口の多さは診療所の数で比較します。この記事では、病床数は病院（`medical_class_code = 1`）だけ、診療所数は診療所（`medical_class_code = 2`）だけを集計しています。

各施設には緯度経度が付いているので、[都道府県境界データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html)（`nlftp.boundary.prefecture`）と空間結合すると、施設がどの都道府県にあるかを判定できます。住所の文字列を使わずに、座標から都道府県を判定できます。以下では病床数・診療所数を都道府県ごとに集計し、[e-Stat「社会・人口統計体系」の人口データ](https://www.e-stat.go.jp/regional-statistics/ssdsview)（`e_stat.ssds.a_pref_population`）の総人口（`A1101`）の2024年値で割って、人口10万人あたりの値にします。

## 人口あたりの病床数は、西日本で多く、大都市圏で少ない

病院の病床数を人口10万人あたりの値にして地図にしました。色が濃いほど、人口に対して病床が多い県です。

```map
type: map
layers:
  - from: map_beds
    geojson: geojson
    color: beds
    label: pref_name
    name: "病床数 / 10万人"
lng: 137
lat: 36.5
zoom: 4
```

色の濃い県は四国・九州・中国地方に多く、首都圏や中部の太平洋側の県は色が薄くなっています。人口あたりの病床数は西日本で多く、東日本、とくに大都市圏で少なくなっています。

## 病床数が最も多い高知県は2,430床、最も少ない神奈川県は807床

同じ指標を47都道府県で並べ、上位10・中間27・下位10の3グループに色分けしました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "beds", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "beds",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "beds", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "beds",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間27",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "beds", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "beds",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も多いのは高知県で、人口10万人あたり2,430床です。鹿児島県が2,098床、長崎県が2,047床、徳島県が1,999床と続き、上位は西日本の県が占めます。下位は神奈川県の807床、埼玉県の856床、愛知県と東京都がともに889床で、大都市圏が並びます。高知県と神奈川県では約3.0倍の差があります。中央値は1,433床です。

人口に対して病床が多い地域は、入院の受け入れに余裕がある一方で、基準病床数制度のもとでは新規の病床整備が認められにくい地域でもあります。大都市圏は人口あたりの病床が少なく、高齢化で入院の需要が増えると病床が不足するおそれがあります。病床を伴う医療・介護事業に新しく参入できる余地を、地域ごとに見積もる材料になります。

## 診療所数は和歌山県の116.6施設が最も多く、病床数の多い県とは一致しない

横軸に人口10万人あたりの病床数、縦軸に人口10万人あたりの診療所数をとり、47都道府県を散布図にしました。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#7c3aed", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "beds_per", "type": "quantitative"},
          {"field": "clinic_per", "type": "quantitative"}
        ],
        "x": {
          "field": "beds_per",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {
          "field": "clinic_per",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "診療所数 / 人口10万人", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "beds_per",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {
          "field": "clinic_per",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "診療所数 / 人口10万人", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

病床数と診療所数の間に、明確な比例関係はありません。病床数が最も多い高知県は、診療所数では中位です。診療所数が最も多いのは和歌山県の116.6施設で、長崎県や島根県が続きます。東京都や大阪府は病床数は少ないものの、診療所数は98施設台と多い水準です。診療所数が最も少ないのは埼玉県の60.8施設で、千葉県や沖縄県が下位に並びます。中央値は86.8施設です。

大都市圏は病床が少なく診療所は多く、地方には病床が多く診療所数は中位の県があり、入院と外来で地域ごとの供給量の傾向が異なります。クリニックの新規開設では診療所数を、病床を伴う事業では病床数を見るというように、事業の種類によって確認する指標が変わります。

## まとめ

国土数値情報の医療機関データを都道府県境界と空間結合し、人口あたりの医療資源を比較しました。

- 人口あたりの病院の病床数は西日本で多く、最も多い高知県（2,430床/10万人）と最も少ない神奈川県（807床/10万人）で約3.0倍の差がある
- 病床が多い地域は基準病床数制度のもとで新規整備が難しく、大都市圏は病床が少ないまま高齢化で入院の需要が増えると考えられる
- 病床（入院）と診療所（外来）の多い県は一致せず、事業の種類によって確認する指標が変わる

## データの出典

本記事は[国土数値情報の医療機関データ（P04）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P04-v3_0.html)と、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別人口データを 2026-07-11 時点で取得して集計しています。人口は総人口（`A1101`）の2024年値です。医療機関データの整備時点は国土数値情報の公開年次によるので、直近の開設・閉院は含まれていない場合があります。

Queriaは、国土数値情報やe-Statのオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[医療機関データ](/datasets/queria/nlftp/facility/medical_institution)から対象地域の病床数や診療科目を確認したり、[都道府県別人口データ](/datasets/queria/e_stat/ssds/a_pref_population)と結合して人口あたりの値を出したりできます。

```sql id=map_beds
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(SUM(m.bed_count) * 100000.0 / pop.p, 0) AS beds FROM nlftp.facility.medical_institution m JOIN nlftp.boundary.prefecture p ON ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name WHERE m.medical_class_code = 1 GROUP BY p.prefecture_name, p.geometry, pop.p
```

```sql id=rank_top
WITH base AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) * 100000.0 / pop.p AS beds FROM nlftp.facility.medical_institution m JOIN nlftp.boundary.prefecture p ON ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name WHERE m.medical_class_code = 1 GROUP BY p.prefecture_name, pop.p), ranked AS (SELECT pref, ROUND(beds, 0) AS beds, ROW_NUMBER() OVER (ORDER BY beds DESC, pref) AS rn FROM base) SELECT pref, beds FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH base AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) * 100000.0 / pop.p AS beds FROM nlftp.facility.medical_institution m JOIN nlftp.boundary.prefecture p ON ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name WHERE m.medical_class_code = 1 GROUP BY p.prefecture_name, pop.p), ranked AS (SELECT pref, ROUND(beds, 0) AS beds, ROW_NUMBER() OVER (ORDER BY beds DESC, pref) AS rn FROM base) SELECT pref, beds FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH base AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) * 100000.0 / pop.p AS beds FROM nlftp.facility.medical_institution m JOIN nlftp.boundary.prefecture p ON ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name WHERE m.medical_class_code = 1 GROUP BY p.prefecture_name, pop.p), ranked AS (SELECT pref, ROUND(beds, 0) AS beds, ROW_NUMBER() OVER (ORDER BY beds DESC, pref) AS rn FROM base) SELECT pref, beds FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=scatter
WITH fac AS (SELECT p.prefecture_name AS pref, SUM(CASE WHEN m.medical_class_code = 1 THEN m.bed_count ELSE 0 END) AS beds, SUM(CASE WHEN m.medical_class_code = 2 THEN 1 ELSE 0 END) AS clinic FROM nlftp.facility.medical_institution m JOIN nlftp.boundary.prefecture p ON ST_Contains(p.geometry, m.geometry) GROUP BY p.prefecture_name), pop AS (SELECT area_name AS pref, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 GROUP BY area_name) SELECT f.pref, ROUND(f.beds * 100000.0 / pop.p, 0) AS beds_per, ROUND(f.clinic * 100000.0 / pop.p, 1) AS clinic_per, CASE WHEN f.pref IN ('高知県', '鹿児島県', '東京都', '埼玉県', '和歌山県', '神奈川県', '大阪府', '千葉県') THEN f.pref ELSE '' END AS label FROM fac f JOIN pop ON f.pref = pop.pref ORDER BY beds_per DESC
```
