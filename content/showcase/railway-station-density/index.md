---
title: 人が住める土地の面積あたりの鉄道駅の数は、東京都が沖縄県の約27倍
description: 全国約9,000駅の位置データを都道府県別に集計しました。可住地面積100km²あたりの駅数は東京都の45.8駅が最も多く、沖縄県の1.7駅の約27倍です。人口10万人あたりでは高知県の25.3駅が最も多くなります。
publishedAt: 2026-06-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 鉄道
  - 公共交通
  - 出店戦略
  - 地域格差
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 鉄道データ（N02）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N02-v3_1.html
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ（N03）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html
    publisher: 国土交通省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 人口10万人あたりの駅数（A1101）を都道府県ランキングにして、面積あたり密度が低い高知県や秋田県が人口あたりでは上位か確かめて
socialAnnounce: |-
  全国約9,000駅の位置データを都道府県別に集計しました。可住地面積あたりの駅密度は東京45.8、沖縄1.7と27倍の差。

  出店市場が駅前型か車前提かの見極めに。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

可住地面積100km²あたりの鉄道駅の数は、東京都の45.8駅が最も多く、最も少ない沖縄県の1.7駅の約27倍です。大阪府（36.5駅）、神奈川県（23.7駅）が続き、北海道は1.9駅で沖縄県に次いで少なくなっています。人口10万人あたりの駅数では高知県の25.3駅が最も多く、面積あたりと人口あたりで駅の多い県は一致しません。

出店候補地を評価するときは、その市場で人が鉄道で移動するか車で移動するかによって、業態や立地の選び方が変わります。鉄道網が密な地域では駅前や駅ナカへの出店が中心になり、鉄道が少ない地域ではロードサイドへの出店や駐車場の確保が前提になります。この記事では、全国の鉄道駅の位置データを都道府県別に集計し、可住地面積や人口に対する駅の数を比較します。駅の数は人口や面積の大きい都道府県ほど多くなるので、可住地面積や人口で割った値で比較します。

## 乗換駅を1駅にまとめると、全国の駅は約9,000駅

駅の位置は[国土数値情報の鉄道データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N02-v3_1.html)（`nlftp.railway.station`）を使います。全国の駅が緯度経度付きの点データとして収録されており、主な列は次のとおりです。

| 列名               | 内容                                                                     |
| ------------------ | ------------------------------------------------------------------------ |
| station_name       | 駅名                                                                     |
| line_name          | 路線名                                                                   |
| operator           | 運営事業者名                                                             |
| operator_type      | 運営主体タイプ（JR在来線・民営鉄道・第三セクター・公営鉄道・JRの新幹線） |
| station_group_code | 同一地点の駅をまとめるコード                                             |
| geometry           | 駅の位置（点）                                                           |

複数の路線が乗り入れる乗換駅は路線ごとに別の行に入っているので、同一地点をまとめる `station_group_code` で重複を除き、1つの駅として集計します。この方法で全国の駅数は約9,000駅になります。各駅の位置を[都道府県境界データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html)（`nlftp.boundary.prefecture`）と空間結合し、どの都道府県にあるかを判定しています。境界のポリゴンの内側にある点だけを集計するので、境界線の上にある駅は集計に含まれない場合があります。

分母には、e-Stat「社会・人口統計体系」の都道府県別自然環境データ（`e_stat.ssds.b_pref_land`）の可住地面積（`B1103`）と、人口・世帯データ（`e_stat.ssds.a_pref_population`）の総人口（`A1101`）の2024年値を使います。可住地面積は総面積から林野や湖沼などを除いた、人が住める土地の面積です。総面積で割ると山林の多い県で駅の密度が低く出るので、可住地面積で割っています。

## 駅の密度が高いのは、首都圏・近畿圏・福岡周辺の都市圏

可住地面積100km²あたりの駅数を地図にしました。色が濃いほど、人が住める土地に対して駅が多い県です。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: density
    label: pref_name
    name: "駅数 / 100km²"
lng: 137
lat: 36.5
zoom: 4
```

色の濃い県は首都圏・近畿圏・福岡周辺の都市圏に集まり、東北から北海道、九州南部にかけては色が薄くなっています。可住地面積あたりの駅数は、市街地のうち駅まで歩いて行ける範囲がどれだけあるかの目安です。色が濃い県ほど、駅を起点にした徒歩の商圏が成り立ちやすいと考えられます。

## 可住地面積100km²あたりの駅数は、東京都の45.8駅が最多、沖縄県の1.7駅が最少

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
          {"field": "density", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "density",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "駅数 / 可住地面積100km²", "grid": true}
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
          {"field": "density", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "density",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "駅数 / 可住地面積100km²", "grid": true}
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
          {"field": "density", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "density",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "駅数 / 可住地面積100km²", "grid": true}
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

最も多いのは東京都で、可住地面積100km²あたり45.8駅です。大阪府が36.5駅、神奈川県が23.7駅、京都府が20.3駅と続きます。最も少ないのは沖縄県の1.7駅、次が北海道の1.9駅で、東京都とは約27倍の差があります。沖縄県の鉄道は沖縄都市モノレール（ゆいレール）だけで在来線がないので、可住地の広さに対して駅がごく少なくなっています。北海道も広い可住地に対して路線が少ないので、沖縄県に次いで低い値です。

中央値は7.9駅です。この値が低い県では、徒歩で来店する客を前提とした駅前型の店舗は来店者を集めにくく、車での来店を前提とした立地を選ぶことになります。

## 面積あたりの駅数と人口あたりの駅数は連動しない

横軸に可住地面積あたりの駅数、縦軸に人口10万人あたりの駅数をとり、47都道府県を散布図にしました。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "per_area", "type": "quantitative"},
          {"field": "per_pop", "type": "quantitative"}
        ],
        "x": {
          "field": "per_area",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "駅数 / 可住地面積100km²", "grid": true}
        },
        "y": {
          "field": "per_pop",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "駅数 / 人口10万人", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "per_area",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "駅数 / 可住地面積100km²", "grid": true}
        },
        "y": {
          "field": "per_pop",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "駅数 / 人口10万人", "grid": true}
        },
        "text": {"field": "label"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 7.9, "type": "quantitative"},
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
        "y": {"datum": 9.2, "type": "quantitative"}
      }
    }
  ]
}
```

破線は各指標の47都道府県の中央値（面積あたり7.9駅、人口あたり9.2駅）です。2つの指標はほとんど連動しておらず、面積あたりの駅数が多い県が人口あたりでも多いとは限りません。

右下にある東京都・大阪府・神奈川県は、面積あたりの駅数は多い一方で、人口あたりの駅数は少なくなっています。人口が密集しているので、1つの駅の周辺に住む人口が多い県です。徒歩の商圏が成り立ちやすい一方、1つの駅前に多くの店舗が集まり、競合も多くなりやすいと考えられます。埼玉県は人口あたりの駅数が全国でも少ない県で、1駅あたりの人口が多くなっています。

上にある高知県は、人口あたり25.3駅で全国で最も多く、人口の少ない地域にも在来線の駅があります。秋田県のように、面積あたりの駅数は少ないものの人口あたりでは多い東北の県もあり、地方の県では人口に対して駅は多く、土地の広さに対しては少ない傾向があります。左下の沖縄県は面積あたり・人口あたりのどちらでも最も少なく、鉄道での移動を前提にできない県です。

駅まで歩いて行ける範囲の広さを見るなら面積あたり、人口に対する駅の多さを見るなら人口あたりと、目的に応じて指標を使い分ける必要があります。

## 業務での活用

- 出店候補地の業態選択: 面積あたりの駅数が多い県では駅前型・駅ナカ型、少ない県ではロードサイド型と、県ごとに立地と業態を選ぶ
- 商圏の設計: 鉄道が少ない地域では徒歩圏でなく車での到達圏で商圏を設計し、駐車場の規模を見積もる
- 複数の候補地の比較: 進出を検討する複数の都道府県を同じ指標で並べ、鉄道での来店を前提にするか車での来店を前提にするかを早い段階で分ける

## データの出典

本記事は国土交通省の[国土数値情報 鉄道データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N02-v3_1.html)と[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_2.html)、総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)を、2026年7月11日時点で取得して集計しています。分母には2024年の可住地面積（`B1103`）と総人口（`A1101`）を使っています。

Queriaは、国土数値情報の鉄道データや行政区域データ、e-Statの統計を、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[鉄道駅テーブル](/datasets/queria/nlftp/railway/station)や[都道府県別自然環境テーブル](/datasets/queria/e_stat/ssds/b_pref_land)から、検討している地域の駅の数や位置を確認できます。

```sql id=map_data
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(COUNT(DISTINCT s.station_group_code) * 10000.0 / l.ha, 1) AS density FROM nlftp.boundary.prefecture p JOIN nlftp.railway.station s ON ST_Contains(p.geometry, s.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ha FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2024 GROUP BY area_name) l ON p.prefecture_name = l.area_name GROUP BY p.prefecture_name, p.geometry, l.ha
```

```sql id=rank_top
WITH base AS (SELECT p.prefecture_name AS pref, COUNT(DISTINCT s.station_group_code) * 10000.0 / l.ha AS density FROM nlftp.boundary.prefecture p JOIN nlftp.railway.station s ON ST_Contains(p.geometry, s.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ha FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2024 GROUP BY area_name) l ON p.prefecture_name = l.area_name GROUP BY p.prefecture_name, l.ha), ranked AS (SELECT pref, ROUND(density, 1) AS density, ROW_NUMBER() OVER (ORDER BY density DESC, pref) AS rn FROM base) SELECT pref, density FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH base AS (SELECT p.prefecture_name AS pref, COUNT(DISTINCT s.station_group_code) * 10000.0 / l.ha AS density FROM nlftp.boundary.prefecture p JOIN nlftp.railway.station s ON ST_Contains(p.geometry, s.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ha FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2024 GROUP BY area_name) l ON p.prefecture_name = l.area_name GROUP BY p.prefecture_name, l.ha), ranked AS (SELECT pref, ROUND(density, 1) AS density, ROW_NUMBER() OVER (ORDER BY density DESC, pref) AS rn FROM base) SELECT pref, density FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH base AS (SELECT p.prefecture_name AS pref, COUNT(DISTINCT s.station_group_code) * 10000.0 / l.ha AS density FROM nlftp.boundary.prefecture p JOIN nlftp.railway.station s ON ST_Contains(p.geometry, s.geometry) JOIN (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ha FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2024 GROUP BY area_name) l ON p.prefecture_name = l.area_name GROUP BY p.prefecture_name, l.ha), ranked AS (SELECT pref, ROUND(density, 1) AS density, ROW_NUMBER() OVER (ORDER BY density DESC, pref) AS rn FROM base) SELECT pref, density FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=scatter
WITH st AS (SELECT p.prefecture_name AS pref, COUNT(DISTINCT s.station_group_code) AS stations FROM nlftp.railway.station s JOIN nlftp.boundary.prefecture p ON ST_Contains(p.geometry, s.geometry) GROUP BY p.prefecture_name), land AS (SELECT area_name AS pref, MAX(TRY_CAST(value AS DOUBLE)) AS ha FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2024 GROUP BY area_name), pop AS (SELECT area_name AS pref, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 GROUP BY area_name) SELECT st.pref, ROUND(st.stations * 10000.0 / land.ha, 1) AS per_area, ROUND(st.stations * 100000.0 / pop.p, 1) AS per_pop, CASE WHEN st.pref IN ('東京都', '大阪府', '神奈川県', '埼玉県', '京都府', '高知県', '秋田県', '北海道', '沖縄県') THEN st.pref ELSE '' END AS label FROM st JOIN land ON st.pref = land.pref JOIN pop ON st.pref = pop.pref ORDER BY per_area DESC
```
