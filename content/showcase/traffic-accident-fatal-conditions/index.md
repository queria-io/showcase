---
title: 車の単独事故は、車どうしの事故より16倍死亡事故になりやすい
description: 警察庁の交通事故オープンデータ2024年の約28万件を、事故類型・時間帯・道路形状・都道府県で比較しました。死亡事故になる割合は、車両単独の事故で車どうしの約16倍、午前3時台で朝8時台の約17倍です。
ogDescription: 警察庁の交通事故オープンデータ2024年の約28万件を、事故類型・時間帯・道路形状・都道府県で比較しました。
publishedAt: 2026-07-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 交通事故
  - 警察庁
  - 死亡事故
datasets:
  - queria/npa
  - queria/nlftp
sources:
  - title: 交通事故統計情報のオープンデータ
    url: https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html
    publisher: 警察庁
agentHint: 事故類型(accident_pattern)が車両単独のものに絞って、道路形状(road_shape)別の事故件数と死亡率(accident_typeが死亡の割合)を出して、単独事故が死亡に至りやすい場所を確かめて
socialAnnounce: |-
  警察庁が公開する交通事故のオープンデータ2024年・約28万件を数えました。

  件数の8割超は車両どうしの衝突ですが、死亡事故の割合は車両単独事故で6.2%と約16倍。深夜3時台は昼のおよそ十数倍でした。
  Queriaは行政のオープンデータを整えて公開しています。
---

2024年に全国で警察が記録した交通事故は282,376件で、そのうち死亡事故は2,591件でした。割合は0.92%で、およそ100件に1件です。この割合は、どんな事故か、いつどこで起きたかによって大きく変わります。車が単独で電柱やガードレールにぶつかる事故では6.16%で、車どうしの事故の約16倍です。午前3時台に起きた事故では6.70%で、朝8時台の約17倍でした。

使ったのは警察庁の[交通事故統計情報のオープンデータ](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)です。事故1件ごとに、発生日時・緯度経度・事故類型・道路形状・天候と、死亡事故か負傷事故かの区分が記録されています。この記事では、事故の件数のうち死亡事故が占める割合を「死亡事故の割合」と呼びます。死者や負傷者の人数をもとにした致死率とは別の値です。

## 件数が最も多い車どうしの事故は、死亡事故の割合が最も低い

事故類型（`accident_pattern`）ごとの件数と死亡事故の割合です。

```sql
SELECT accident_pattern AS '事故類型', COUNT(*) AS '件数', SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) AS '死亡事故', ROUND(100.0 * SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) / COUNT(*), 2) AS '死亡事故の割合(%)' FROM npa.main.traffic_accident GROUP BY accident_pattern ORDER BY COUNT(*) DESC
```

件数の82.6%（233,191件）は車どうしの衝突「車両相互」です。歩行者と車の「人対車両」が37,328件、車が単独で電柱やガードレールなどにぶつかる「車両単独」が11,803件で続きます。踏切などで列車とぶつかる「列車」は54件しかなく、1件の死亡事故で割合が大きく動くので、図では残りの3類型を比較します。

```chart
{
  "height": 200,
  "layer": [
    {
      "data": {"name": "pattern"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "fatal_pct", "type": "quantitative"},
          {"field": "pattern", "type": "nominal"}
        ],
        "x": {
          "field": "fatal_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡事故の割合（%）", "grid": true}
        },
        "y": {
          "field": "pattern",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "事故類型"},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "pattern"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "fatal_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡事故の割合（%）", "grid": true}
        },
        "y": {
          "field": "pattern",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "事故類型"},
          "sort": null
        },
        "text": {"field": "fatal_pct"}
      }
    }
  ]
}
```

死亡事故の割合は件数の順と逆になり、車両相互が0.39%、人対車両が2.46%、車両単独が6.16%です。車どうしの事故では互いに減速や回避ができることが多く、固定物にぶつかる事故や歩行者が巻き込まれる事故では衝撃を和らげるものが少ないためと考えられます。

## 午前3時台の事故は、朝8時台の17倍の割合で死亡事故になる

事故が起きた時刻ごとに、死亡事故の割合を並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "hourly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hr\"]) && isValid(datum[\"fatal_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "hr", "type": "quantitative"},
          {"field": "fatal_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "hr",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "発生時刻（時）", "tickMinStep": 2}
        },
        "y": {
          "field": "fatal_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡事故の割合（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

割合が最も低いのは通勤・通学の時間帯で、8時台が0.40%、7時台が0.50%です。そこから夜に向かって上がり、深夜から明け方にかけて大きく上がります。最も高いのは午前3時台の6.70%です。事故の件数は日中のほうがはるかに多い一方で、1件の事故が死亡事故になる割合は、人も車も少ない深夜に高くなります。速度が出やすいことや、事故の発見が遅れることが関係していると考えられます。

## 交差点より単路、とくにカーブで高い

事故が起きた場所の道路形状（`road_shape`）ごとに比較します。事故が1,000件に満たない形状は、割合が安定しないので除いています。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "shape"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "fatal_pct", "type": "quantitative"},
          {"field": "road_shape", "type": "nominal"}
        ],
        "x": {
          "field": "fatal_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡事故の割合（%）", "grid": true}
        },
        "y": {
          "field": "road_shape",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "道路形状"},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "shape"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "fatal_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡事故の割合（%）", "grid": true}
        },
        "y": {
          "field": "road_shape",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "道路形状"},
          "sort": null
        },
        "text": {"field": "fatal_pct"}
      }
    }
  ]
}
```

最も高いのは「単路－カーブ・屈折」の5.28%で、「単路－トンネル」の3.93%が続きます。単路は交差点以外の道路区間です。件数が最も多い「交差点－その他」は0.71%で、交差点付近もほぼ同じ水準です。カーブの割合は交差点の約7倍です。交差点では信号や標識で速度が落ち、ぶつかっても低速のことが多い一方、直線やカーブでは速度が出たまま単独事故になりやすいと考えられます。事故類型で車両単独の割合が高かったことと同じ傾向です。

カーブで起きた死亡事故387件の地点を地図にしました。色は事故類型です。

```map
type: map
layers:
  - from: curve
    lng: lng
    lat: lat
    color: 事故類型
    label: 都道府県
    name: カーブでの死亡事故
lng: 137
lat: 36.5
zoom: 4
```

387件のうち213件（55%）が車両単独の事故で、275件（71%）は市街地の外で起きています。

## 都市部の都府県は低く、地方の県は高い

都道府県ごとの死亡事故の割合を地図にしました。色が濃いほど割合が高い県です。北海道は元データで方面本部ごとに分かれているので、合算しています。

```map
type: map
layers:
  - from: map
    geojson: geojson
    color: fatal_pct
    label: pref_name
    name: "死亡事故の割合（%）"
lng: 137
lat: 36.5
zoom: 4
```

最も低いのは東京都と静岡県で、どちらも約0.50%です。神奈川県・大阪府・福岡県・愛知県など大都市のある都府県も低い側に並びます。高いのは秋田県（3.13%）・和歌山県（2.78%）・福井県（2.52%）などで、最も低い県とは約6倍の差があります。都市部は事故の件数は多いものの、渋滞や信号で速度が抑えられ、病院への搬送も速いと考えられます。地方では走行速度が高く、単独事故や夜間の事故の比重も大きくなりやすいので、ここまで見た事故類型・時間帯・道路形状の傾向が、県の差として表れていると考えられます。

## まとめ

- 事故の82.6%は車どうしの衝突で、死亡事故の割合は0.39%と最も低い。車両単独の事故は6.16%で、車どうしの約16倍
- 午前3時台の事故は6.70%で、朝8時台（0.40%）の約17倍
- 道路形状ではカーブ・屈折が5.28%で最も高く、交差点の約7倍。都道府県では秋田県・和歌山県・福井県が高く、東京都・静岡県が低い

事故の件数が多い条件と、事故が死亡事故になりやすい条件は一致しません。

## データの出典

本記事は警察庁の[交通事故統計情報のオープンデータ](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)のうち、2024年（令和6年）の本票を2026年7月23日時点で集計しています。

Queriaは、このオープンデータの事故1件ごとの記録を、発生時刻や道路形状を列にして、緯度経度や都道府県の境界と組み合わせられる形で公開しています。本記事で使った[交通事故テーブル](/datasets/queria/npa/main/traffic_accident)から、自分の地域や道路条件に絞って同じ割合を出したり、事故の発生場所を地図で確認したりできます。

```sql id=pattern
SELECT accident_pattern AS pattern, ROUND(100.0 * SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) / COUNT(*), 2) AS fatal_pct FROM npa.main.traffic_accident WHERE accident_pattern IN ('車両相互', '人対車両', '車両単独') GROUP BY accident_pattern ORDER BY fatal_pct DESC
```

```sql id=hourly
SELECT occurred_hour AS hr, ROUND(100.0 * SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) / COUNT(*), 2) AS fatal_pct FROM npa.main.traffic_accident WHERE occurred_hour IS NOT NULL GROUP BY occurred_hour ORDER BY occurred_hour
```

```sql id=shape
SELECT road_shape, ROUND(100.0 * SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) / COUNT(*), 2) AS fatal_pct FROM npa.main.traffic_accident GROUP BY road_shape HAVING COUNT(*) >= 1000 ORDER BY fatal_pct DESC
```

```sql id=map
WITH pref AS (SELECT CASE WHEN prefecture LIKE '北海道%' THEN '北海道' ELSE prefecture END AS pk, COUNT(*) AS n, SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) AS fatal FROM npa.main.traffic_accident GROUP BY 1) SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, ROUND(100.0 * p.fatal / p.n, 2) AS fatal_pct, b.prefecture_name AS pref_name FROM nlftp.boundary.prefecture b JOIN pref p ON regexp_replace(b.prefecture_name, '(都|府|県)$', '') = p.pk
```

```sql id=curve
SELECT longitude AS lng, latitude AS lat, accident_pattern AS 事故類型, prefecture AS 都道府県 FROM npa.main.traffic_accident WHERE accident_type = '死亡' AND road_shape = '単路－カーブ・屈折' ORDER BY accident_pattern DESC
```
