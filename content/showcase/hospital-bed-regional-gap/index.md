---
title: 人口10万人あたりの病床数は高知県が2,305床で、神奈川県の約2.9倍
description: 全国約8,300の病院の位置と病床数を都道府県別に集計しました。人口10万人あたりの病床数は高知県の2,305床から神奈川県の806床まで約2.9倍の差があり、病床の多い県ほど1病院あたりの病床数が小さい傾向があります。
publishedAt: 2026-07-07
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療
  - 病床
  - 在宅医療
  - 地域格差
  - エリア戦略
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 医療機関データ（P04）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P04-v3_0.html
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ（N03）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html
    publisher: 国土交通省
  - title: 統計でみる都道府県・市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
agentHint: 開設者（establisher_type）別の病床数（bed_count）を都道府県別に集計して、医療法人と公的医療機関のどちらが主な担い手かが地域で変わるか比べて。medical_class='病院'に絞って
socialAnnounce: |-
  全国約8,300の病院の位置と病床数を都道府県別に集計しました。人口10万人あたり病床数は高知2,305床、神奈川806床と約2.9倍の差があります。

  在宅医療の後方支援体制や連携先の選定に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2020年の人口10万人あたりの病院の病床数は、最も多い高知県が2,305床、最も少ない神奈川県が806床で、約2.9倍の差がありました。上位には西日本の県が、下位には大都市圏の都府県が並びます。人口あたりの病床が多い県ほど1病院あたりの病床数は小さく、高知県は132床、滋賀県は247床です。

この記事では、全国の病院の位置と病床数を都道府県別に集計し、人口あたりの病床数と、病床が少数の大きな病院に集まっているか多数の中小病院に分かれているかを比較しました。在宅医療や訪問看護のサービスエリアを設計するときは、急変時の入院先になる後方支援病院がどれだけあるかを確認する必要があります。国は新たな地域医療構想のもとで入院から在宅医療への移行を進めていますが、受け入れ先になる病床の数は地域によって大きく異なります。

## 病床の大半は病院にあるので、病院だけを集計する

医療機関の位置は[国土数値情報の医療機関データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P04-v3_0.html)（`nlftp.facility.medical_institution`）を使います。全国の医療機関が緯度経度付きの点データとして収録されており、病床数や開設者などの属性が付いています。施設は医療機関の種別（`medical_class`）で病院・診療所・歯科診療所に分かれます。

```sql
SELECT medical_class AS 施設種別, COUNT(*) AS 施設数, SUM(bed_count) AS 病床数 FROM nlftp.facility.medical_institution GROUP BY medical_class ORDER BY 病床数 DESC
```

診療所や歯科診療所は施設数は多いものの、大半は入院設備を持たないので、病床数はわずかです。後方支援の受け入れ先になるのは入院機能を持つ病院なので、種別が病院のものだけを対象に病床数（`bed_count`）を集計しました。このデータは令和2年（2020年）時点の収録です。医療機関データの住所欄には都道府県名が入っていないので、各病院の位置を[都道府県境界データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html)（`nlftp.boundary.prefecture`）と空間結合して都道府県を判定しました。そのうえで、e-Stat「社会・人口統計体系」の総人口（`e_stat.ssds.a_pref_population` の `A1101`）の2020年値で割り、人口10万人あたりの病床数を出しています。

## 人口あたりの病床は西日本と北海道で多く、大都市圏で少ない

人口10万人あたりの病院の病床数を地図にしました。色が濃いほど、人口に対して病床が多い地域です。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: beds
    label: pref_name
    name: "病床 / 10万人"
lng: 137
lat: 36.5
zoom: 4
```

色の濃い県は西日本、とくに九州・四国・中国地方と北海道に多く、首都圏や中京圏など大都市圏は色が薄くなっています。47都道府県の中央値は1,362床です。この中央値は47都道府県それぞれの比率の中央値で、全国の総病床数を全国人口で割った値とは一致しません。

## 最も多い高知県は2,305床で、最も少ない神奈川県の約2.9倍

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
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
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
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
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
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も多いのは高知県で、人口10万人あたり2,305床です。鹿児島県が2,024床、長崎県が1,953床、徳島県が1,903床と、西日本の県が上位に並びます。下位は神奈川県の806床、埼玉県の855床、愛知県の879床、東京都の897床、千葉県の926床と、大都市圏の都県です。高知県と神奈川県の差は約2.9倍で、中央値は岩手県の1,362床です。

大都市圏で人口あたりの病床が少ないのは、人口の増加に病床の整備が追いついていないためと考えられます。こうした地域では後方支援病床の余裕が小さく、連携先を確保しにくいと考えられます。このデータには病床の機能区分（急性期・回復期・慢性期など）や稼働状況は含まれないので、病床が多いことは、すぐに受け入れられる余力があることを意味しません。

## 人口あたりの病床が多い県ほど、1病院あたりの病床数は小さい

病床が多数の中小病院に分かれているか、少数の大きな病院に集まっているかで、連携の組み方は変わります。横軸に人口10万人あたりの病床数、縦軸に1病院あたりの平均病床数を取り、47都道府県を散布図にしました。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "per_pop", "type": "quantitative"},
          {"field": "avg_beds", "type": "quantitative"}
        ],
        "x": {
          "field": "per_pop",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {
          "field": "avg_beds",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1病院あたり平均病床数", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "per_pop",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "病床数 / 人口10万人", "grid": true}
        },
        "y": {
          "field": "avg_beds",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1病院あたり平均病床数", "grid": true}
        },
        "text": {"field": "label"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1362, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 183, "type": "quantitative"}
      }
    }
  ]
}
```

破線は47都道府県それぞれの中央値（人口あたり1,362床、1病院あたり183床）です。人口あたりの病床が多い県ほど、1病院あたりの病床数は小さくなっています。

右下にある高知県や鹿児島県は、人口あたりの病床は全国で最も多く、1病院あたりの病床数は高知県132床、大分県129床、徳島県128床と小さくなっています。中小規模の病院が数多くある県です。左上にある滋賀県は、人口あたりの病床は997床と少なく、1病院あたりは247床で全国で最も大きくなっています。少数の大規模病院に病床が集まっている県です。神奈川県・愛知県・埼玉県などの大都市圏も、人口あたりの病床が少なく、1病院あたりの病床数が大きい側にあります。

中小病院が多い県では多数の中小病院とそれぞれ連携する必要があり、大規模病院に集まっている県では少数の基幹病院との連携が中心になります。

## 病床の半数以上は医療法人の病院にある

病院の病床を開設者別に集計しました。

```sql
SELECT establisher_type AS 開設者, COUNT(*) AS 病院数, SUM(bed_count) AS 病床数 FROM nlftp.facility.medical_institution WHERE medical_class = '病院' GROUP BY establisher_type ORDER BY 病床数 DESC
```

医療法人の病院の病床は839,187床で、全体の半数以上です。次いで自治体立の病院などの公的医療機関が301,045床、独立行政法人や国立病院機構などの国が125,458床です。1病院あたりの平均病床数は医療法人立が147床、国立が393床、公的医療機関が258床です。医療法人立は地域の中小規模の病院、公的医療機関や国立は救命救急や高度医療を行う大規模病院が中心と考えられます。開設者の構成を確認しておくと、地域でどのような病院と連携できるかを事前に判断できます。

## 業務での使い方

- 進出エリアの絞り込み: 人口あたりの病床が少ない大都市圏では後方支援先の余裕が小さいことを前提に、連携先を確保できるエリアから優先して検討する
- 連携方法の設計: 中小病院が多い県では多数の中小病院と、大規模病院に集まっている県では少数の基幹病院と連携するように、地域の病床の構成に合わせて連携方法を変える
- 候補地の比較: 進出を検討する複数の都道府県を同じ指標で並べ、後方支援病床の数と病院規模を早い段階で比較する

## データの出典

本記事は国土交通省[国土数値情報の医療機関データ（P04）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P04-v3_0.html)と[行政区域データ（N03）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html)、および総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)を、2026-07-11 時点で取得して集計しています。医療機関データは令和2年（2020年）時点の収録で、人口も2020年の値を使っています。

Queriaは、国土数値情報の医療機関データ・行政区域データとe-Statの統計を、列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[医療機関テーブル](/datasets/queria/nlftp/facility/medical_institution)と[都道府県別人口テーブル](/datasets/queria/e_stat/ssds/a_pref_population)から、検討している地域の病床数と病院の規模を確認できます。

```sql id=map_data
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(SUM(m.bed_count) * 100000.0 / pop.p, 0) AS beds FROM nlftp.boundary.prefecture p JOIN nlftp.facility.medical_institution m ON m.medical_class = '病院' AND ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name GROUP BY p.prefecture_name, p.geometry, pop.p
```

```sql id=rank_top
WITH base AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) * 100000.0 / pop.p AS beds FROM nlftp.boundary.prefecture p JOIN nlftp.facility.medical_institution m ON m.medical_class = '病院' AND ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name GROUP BY p.prefecture_name, pop.p), ranked AS (SELECT pref, ROUND(beds, 0) AS beds, ROW_NUMBER() OVER (ORDER BY beds DESC, pref) AS rn FROM base) SELECT pref, beds FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH base AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) * 100000.0 / pop.p AS beds FROM nlftp.boundary.prefecture p JOIN nlftp.facility.medical_institution m ON m.medical_class = '病院' AND ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name GROUP BY p.prefecture_name, pop.p), ranked AS (SELECT pref, ROUND(beds, 0) AS beds, ROW_NUMBER() OVER (ORDER BY beds DESC, pref) AS rn FROM base) SELECT pref, beds FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH base AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) * 100000.0 / pop.p AS beds FROM nlftp.boundary.prefecture p JOIN nlftp.facility.medical_institution m ON m.medical_class = '病院' AND ST_Contains(p.geometry, m.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 GROUP BY area_name) pop ON p.prefecture_name = pop.area_name GROUP BY p.prefecture_name, pop.p), ranked AS (SELECT pref, ROUND(beds, 0) AS beds, ROW_NUMBER() OVER (ORDER BY beds DESC, pref) AS rn FROM base) SELECT pref, beds FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=scatter
WITH h AS (SELECT p.prefecture_name AS pref, SUM(m.bed_count) AS beds, COUNT(*) AS hosp FROM nlftp.boundary.prefecture p JOIN nlftp.facility.medical_institution m ON m.medical_class = '病院' AND ST_Contains(p.geometry, m.geometry) GROUP BY p.prefecture_name), pop AS (SELECT area_name AS pref, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 GROUP BY area_name) SELECT h.pref, ROUND(h.beds * 100000.0 / pop.p, 0) AS per_pop, ROUND(h.beds * 1.0 / h.hosp, 0) AS avg_beds, CASE WHEN h.pref IN ('高知県', '鹿児島県', '徳島県', '神奈川県', '埼玉県', '東京都', '愛知県', '滋賀県', '大分県') THEN h.pref ELSE '' END AS label FROM h JOIN pop ON h.pref = pop.pref ORDER BY per_pop DESC
```
