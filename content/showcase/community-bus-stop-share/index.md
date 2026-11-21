---
title: バス停留所の33.1%はコミュニティバスで、県別では6.0%から63.0%まで差がある
description: 国土数値情報のバス停留所27.8万件を運行区分で集計しました。コミュニティバスが停まる停留所は33.1%で、県別では6.0%から63.0%まで差があります。可住地面積あたりの密度では、民間路線の停留所が少ない県ほどコミュニティバスの停留所が多いという関係はありませんでした（相関係数0.06）。
ogTitle: バス停留所の33.1%はコミュニティバスで、県別では6.0%から63.0%まで差がある
ogDescription: 国土数値情報のバス停留所27.8万件を運行区分で集計し、コミュニティバスの割合と密度を都道府県別に比較しました。
publishedAt: 2026-08-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 地域公共交通
  - 国土数値情報
  - バス
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 バス停留所データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P11.html
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
  - title: 社会・人口統計体系 都道府県データ
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures
    publisher: 総務省統計局
agentHint: コミュニティバスの停留所を運行主体(operator)別に数えて、停留所数の多い自治体を上位30件出して。あわせて各主体の系統数(route_count)の平均も添えて
socialAnnounce: |-
  全国のバス停留所27.8万件を運行区分で数えました。

  コミュニティバスは33.1%を占め、県別では6.0%から63.0%まで開きます。地域公共交通計画で比べる相手を選ぶときに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

全国のバス停留所278,515件のうち、コミュニティバスが停まる停留所は92,195件で33.1%でした。都道府県別では岐阜県の63.0%から長崎県の6.0%まで差があります。可住地面積100km²あたりの停留所数で比較すると、民間・公営の路線バスの停留所が少ない県ほどコミュニティバスの停留所が多いという関係はなく、2つの密度の相関係数は0.06でした。コミュニティバスの運行主体は774あり、停留所数の中央値は89件です。

地域公共交通計画を作るときは、自分の自治体と比較する相手を選びます。人口規模や高齢化率が近い自治体を選ぶことが多いものの、民間の路線バスが撤退した地域を自治体のバスが補っているかどうかは、地域によって異なります。

使ったのは[国土数値情報のバス停留所データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P11.html)です。全国の停留所が1件1レコードで記録され、そこに停まる系統の運行区分が付いています。区分は民間の路線バス、公営の路線バス、コミュニティバス、そのいずれでもない「その他」の4つで、高速バス・デマンドバス・貸切バス・スクールバスは含みません。全国の停留所を、この区分の組み合わせ（`bus_class_codes`）で集計しました。

## 停留所の3件に1件はコミュニティバスが停まる

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "classes"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "class_name", "type": "nominal"},
          {"field": "stops", "type": "quantitative"}
        ],
        "x": {
          "field": "class_name",
          "type": "nominal",
          "axis": {"title": "運行区分", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "stops",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "停留所数（件）", "grid": true}
        }
      }
    }
  ]
}
```

全国の停留所は278,515件です。最も多いのは民間の路線バスだけが停まる停留所で171,127件、全体の61.4%を占めます。コミュニティバスだけが停まる停留所は91,867件で33.0%、公営の路線バスだけは14,856件で5.3%です。1つの停留所に複数の区分の系統が停まることもあり、公営路線とコミュニティバスの両方が停まる停留所が328件あります。どの区分にも当てはまらない「その他」は337件です。両方が停まる停留所を含めると、コミュニティバスが停まる停留所は92,195件、全体の33.1%になります。全国では、停留所の3件に1件に自治体が運行するバスが停まります。

## 県別では、コミュニティバスの割合が6.0%から63.0%まで差がある

停留所に占めるコミュニティバスの割合を都道府県別に集計しました。停留所の所属県は配布ファイルの単位で決まるため、県境をまたぐ路線の停留所はファイルが属する県に入ります。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "comm_pct", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "comm_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "コミュニティバスが停まる停留所の割合（%）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "comm_pct", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "comm_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "コミュニティバスが停まる停留所の割合（%）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "comm_pct", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "comm_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "コミュニティバスが停まる停留所の割合（%）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは岐阜県の63.0%で、長野県60.0%、群馬県58.2%、三重県56.9%、愛知県53.8%と、中部を中心とした県が上位に並びます。これらの県では、停留所の半分以上に自治体が運行するバスが停まります。最も低いのは長崎県の6.0%で、神奈川県6.9%、北海道10.3%、大阪府10.8%と続きます。最も高い県と低い県では10倍以上の差があります。

神奈川県や大阪府が低いのは、民間の路線バスの路線網が広いためと考えられます。北海道が低いことは、この理由では説明できません。民間の路線が少ない地域ほど自治体のバスが補っているのであれば、北海道の割合は高くなるはずです。

## 民間路線の停留所が少ない県ほどコミュニティバスの停留所が多い、という関係はない

県ごとに、コミュニティバス以外の停留所数（大半は民間・公営の路線バス）と、コミュニティバスの停留所数を、それぞれ可住地面積100km²あたりの密度にしました。可住地面積は[社会・人口統計体系の都道府県データ](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)（`B1103` 可住地面積）を使っています。集計しているのは停留所の数で、便数ではないので、この密度は路線網の広さを表し、運行本数は表しません。自治体のバスが民間路線の少ない地域を補っているのであれば、横軸が小さい県ほど縦軸が大きくなるはずです。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "density"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "route_per100", "type": "quantitative"},
          {"field": "comm_per100", "type": "quantitative"}
        ],
        "x": {
          "field": "route_per100",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "コミュニティバス以外の停留所（可住地100km²あたり）", "grid": true}
        },
        "y": {
          "field": "comm_per100",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "コミュニティバスの停留所（可住地100km²あたり）", "grid": true}
        }
      }
    }
  ]
}
```

散布図に右下がりの関係はありません。2つの密度の相関係数は0.06です。コミュニティバスの割合と民間の密度の間には負の相関（相関係数-0.53）がありますが、これは割合の分母に民間の停留所が含まれるためで、密度どうしで比較すると相関はなくなります。

北海道と山形県を比較すると違いが分かります。コミュニティバス以外の停留所密度は北海道57.2、山形県50.5でほぼ同じですが、コミュニティバスの密度は北海道6.6、山形県48.8で、7倍以上の差があります。民間の路線の量が同じくらいでも、自治体が運行するバスの量は県によって大きく異なります。図の右上には東京都（コミュニティバス以外671.5、コミュニティバス199.3）が離れて位置します。左下の、どちらの停留所も少ない位置にあるのは北海道だけです。このデータには予約制のデマンドバスが含まれないため、北海道でデマンド交通を含めた移動手段が少ないとまでは言えません。

## コミュニティバスの停留所密度が高いのは東京都と中部の県、島根県・大分県

コミュニティバスの停留所密度を地図にしました。色が濃いほど、可住地面積あたりのコミュニティバスの停留所が多い県です。

```map
type: map
layers:
  - from: map
    geojson: geojson
    color: comm_per100
    label: pref_name
    name: "停留所数"
lng: 137
lat: 36.5
zoom: 4
```

最も濃いのは東京都の199.3で、岐阜県180.1、島根県178.7、大分県172.8、愛知県163.9が続きます。割合で上位だった岐阜県・愛知県・長野県（156.8）・三重県（153.6）は密度でも上位に入っています。中部の県では、コミュニティバスの停留所が県内の広い範囲にあることが、割合と密度の両方から分かります。島根県は割合でも10位です。大分県は割合では中位（44.5%）ですが、密度では中部の県と同じ水準です。

すべての区分を含めた停留所の密度は、最も高い東京都が870.7件、最も低い北海道が63.8件で、13.6倍の差があります。

## コミュニティバスの運行主体774のうち、半分以上は停留所が100件未満

比較の相手を選ぶ単位は自治体なので、運行主体ごとにも集計しました。コミュニティバスの運行主体は `operator` 列に自治体名で入っているので、主体ごとに停留所を集計すると、自治体ごとの規模が分かります。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "operators"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "operator", "type": "nominal"},
          {"field": "stops", "type": "quantitative"}
        ],
        "x": {
          "field": "operator",
          "type": "nominal",
          "axis": {"title": "運行主体", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "stops",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "コミュニティバス停留所数（件）", "grid": true}
        }
      }
    }
  ]
}
```

コミュニティバスが停まる停留所を持つ運行主体は774あり、1主体あたりの停留所数の中央値は89件です。430主体は100件未満で、半分以上が100件に届きません。最も多いのは長野市の868件で、鹿児島市838件、岐阜市745件、豊田市713件、高崎市701件と続きます。

比較の相手を選ぶときは、まず自分の自治体がこの分布のどこにあるかを確認します。中央値の89件前後か、上位の数百件規模かによって、参考にする運行形態も費用の規模も変わります。同じ県の中でも運行主体ごとの規模は大きく異なるので、県の割合だけでは自治体の位置は判断できません。

## 業務でどう使うか

- 比較対象を選ぶときに、人口規模や高齢化率に加えて、コミュニティバス以外の停留所密度が近い県を先に絞り込む。民間路線の量が同じくらいの県の間で、コミュニティバスの密度を比較すると、自分の自治体の位置が分かる
- 民間路線が撤退した地域を自治体のバスが補っているという前提を、自県の数字で確認する。密度の間にその関係がなければ、どちらのバスも少ない範囲がどこかを先に洗い出す
- 運行主体別の停留所数で、自分の自治体が774主体のどのあたりにいるかを確認する。中央値の89件前後か、数百件規模かによって、参考にする先行事例が変わる

## データの出典

本記事は[国土数値情報のバス停留所データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P11.html)（第3.0版・令和4年度）を2026年8月1日時点で集計しています。可住地面積は[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県データ（2022年度）、地図の境界は[国土数値情報の行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)です。

Queriaは、国土数値情報のシェープファイルを、列名・単位・文字コードを統一したテーブルに変換し、運行区分コードを名称に変えて公開しています。本記事で使った[バス停留所テーブル](/datasets/queria/nlftp/transit/bus_stop)から自分の自治体の停留所を運行主体で抽出したり、[可住地面積を含む都道府県データ](/datasets/queria/e_stat/ssds/b_pref_land)と結合して近隣県と密度を比較したりできます。

```sql id=classes
SELECT CASE bus_class_codes WHEN '1' THEN '民間路線' WHEN '3' THEN 'コミュニティ' WHEN '2' THEN '公営路線' WHEN '2,3' THEN '公営／コミュニティ' ELSE 'その他' END AS class_name, COUNT(*) AS stops, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct FROM nlftp.transit.bus_stop GROUP BY 1 ORDER BY stops DESC
```

```sql id=total
SELECT COUNT(*) AS stops, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm_stops, ROUND(COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') * 100.0 / COUNT(*), 1) AS comm_pct, COUNT(DISTINCT operator) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm_operators, COUNT(*) FILTER (WHERE bus_class_codes = '2,3') AS both_stops FROM nlftp.transit.bus_stop
```

```sql id=pref_top
WITH b AS (SELECT prefecture_code AS pc, COUNT(*) AS stops, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm FROM nlftp.transit.bus_stop GROUP BY 1), l AS (SELECT left(area, 2) AS pc, area_name AS pref FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area <> '00000' GROUP BY 1, 2), r AS (SELECT l.pref, b.stops, ROUND(b.comm * 100.0 / b.stops, 1) AS comm_pct, ROW_NUMBER() OVER (ORDER BY b.comm * 1.0 / b.stops DESC, l.pref) AS rn FROM b JOIN l ON l.pc = b.pc) SELECT pref, stops, comm_pct FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH b AS (SELECT prefecture_code AS pc, COUNT(*) AS stops, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm FROM nlftp.transit.bus_stop GROUP BY 1), l AS (SELECT left(area, 2) AS pc, area_name AS pref FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area <> '00000' GROUP BY 1, 2), r AS (SELECT l.pref, b.stops, ROUND(b.comm * 100.0 / b.stops, 1) AS comm_pct, ROW_NUMBER() OVER (ORDER BY b.comm * 1.0 / b.stops DESC, l.pref) AS rn FROM b JOIN l ON l.pc = b.pc) SELECT pref, stops, comm_pct FROM r WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH b AS (SELECT prefecture_code AS pc, COUNT(*) AS stops, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm FROM nlftp.transit.bus_stop GROUP BY 1), l AS (SELECT left(area, 2) AS pc, area_name AS pref FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area <> '00000' GROUP BY 1, 2), r AS (SELECT l.pref, b.stops, ROUND(b.comm * 100.0 / b.stops, 1) AS comm_pct, ROW_NUMBER() OVER (ORDER BY b.comm * 1.0 / b.stops DESC, l.pref) AS rn FROM b JOIN l ON l.pc = b.pc) SELECT pref, stops, comm_pct FROM r WHERE rn > 37 ORDER BY rn
```

```sql id=density
WITH b AS (SELECT prefecture_code AS pc, COUNT(*) AS stops, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm, COUNT(*) FILTER (WHERE bus_class_codes NOT LIKE '%3%') AS route FROM nlftp.transit.bus_stop GROUP BY 1), l AS (SELECT left(area, 2) AS pc, area_name AS pref, SUM(TRY_CAST(value AS DOUBLE)) / 100 AS km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area <> '00000' GROUP BY 1, 2) SELECT l.pref, ROUND(b.route / l.km2 * 100, 1) AS route_per100, ROUND(b.comm / l.km2 * 100, 1) AS comm_per100, ROUND(b.stops / l.km2 * 100, 1) AS all_per100, ROUND(b.comm * 100.0 / b.stops, 1) AS comm_pct FROM b JOIN l ON l.pc = b.pc ORDER BY all_per100 DESC
```

```sql id=relation
WITH b AS (SELECT prefecture_code AS pc, COUNT(*) AS stops, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm, COUNT(*) FILTER (WHERE bus_class_codes NOT LIKE '%3%') AS route FROM nlftp.transit.bus_stop GROUP BY 1), l AS (SELECT left(area, 2) AS pc, SUM(TRY_CAST(value AS DOUBLE)) / 100 AS km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area <> '00000' GROUP BY 1) SELECT ROUND(corr(b.comm / l.km2, b.route / l.km2), 2) AS corr_density, ROUND(corr(b.comm * 1.0 / b.stops, b.route / l.km2), 2) AS corr_share_route FROM b JOIN l ON l.pc = b.pc
```

```sql id=operators
WITH c AS (SELECT operator, COUNT(*) AS stops FROM nlftp.transit.bus_stop WHERE bus_class_codes LIKE '%3%' GROUP BY 1) SELECT operator, stops, COUNT(*) OVER () AS operators, ROUND(MEDIAN(stops) OVER (), 0) AS median_stops, COUNT(*) FILTER (WHERE stops < 100) OVER () AS under100 FROM c QUALIFY ROW_NUMBER() OVER (ORDER BY stops DESC, operator) <= 12 ORDER BY stops DESC, operator
```

```sql id=map
WITH b AS (SELECT prefecture_code AS pc, COUNT(*) FILTER (WHERE bus_class_codes LIKE '%3%') AS comm FROM nlftp.transit.bus_stop GROUP BY 1), l AS (SELECT left(area, 2) AS pc, SUM(TRY_CAST(value AS DOUBLE)) / 100 AS km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area <> '00000' GROUP BY 1) SELECT ST_AsGeoJSON(ST_Simplify(g.geometry, 0.01)) AS geojson, ROUND(b.comm / l.km2 * 100, 1) AS comm_per100, g.prefecture_name AS pref_name FROM nlftp.boundary.prefecture g JOIN b ON b.pc = g.prefecture_code JOIN l ON l.pc = g.prefecture_code
```
