---
title: 民営借家率は大阪市浪速区が70.7%で最も高く、東京23区でも1.7倍の差
description: 2023年の住宅・土地統計調査で民営借家率を市区町村・区ごとに計算しました。大阪市浪速区が70.7%、福岡市博多区が62.7%で、東京23区の中でも豊島区の54.9%から江東区の32.7%まで約1.7倍の差があります
publishedAt: 2026-05-31
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 住宅
  - 賃貸
  - 不動産
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 住宅・土地統計調査
    url: https://www.stat.go.jp/data/jyutaku/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
agentHint: 福岡市の各区の民営借家率（民営借家数÷居住世帯あり住宅数）を2023年で出して、博多区・中央区と他の区でどれくらい差があるか並べて。
socialAnnounce: |-
  民営借家率を市区町村・区レベルまで下ろしました。2023年は大阪市浪速区71%、福岡市博多区63%。東京23区内でも33〜55%と差があります。

  賃貸の投資エリア選定に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2023年の住宅・土地統計調査で、人が住んでいる住宅のうち民営借家が占める割合（民営借家率）を市区町村・区ごとに計算すると、最も高いのは大阪市浪速区の70.7%で、福岡市博多区の62.7%が続きました。東京23区の中でも、豊島区の54.9%から江東区の32.7%まで約1.7倍の差があります。

賃貸住宅の投資エリアを検討するとき、都道府県単位の指標では地域が広すぎて判断に使えません。同じ大阪府でも、持ち家が中心の郊外と、単身者向けの賃貸が集中する都心の区では、賃貸需要の大きさが異なります。この記事では、賃貸需要の代理指標として民営借家率（民営借家数を居住世帯あり住宅数で割った割合）を、市区町村と、政令市・特別区の区の単位で集計します。使うのは、[住宅・土地統計調査](https://www.stat.go.jp/data/jyutaku/index.html)をもとにした e-Stat「社会・人口統計体系」の市区町村別住宅データ（`municipal_housing`）です。

## データの概要

市区町村別の民営借家率は、次の2つの項目から計算します。

| コード | 内容                       |
| ------ | -------------------------- |
| H1101  | 居住世帯あり住宅数（分母） |
| H1322  | 民営借家数                 |

分母には空き家や別荘などの居住世帯のない住宅を入れていません。実際に人が住んでいる住宅のうち民営借家がどれだけあるかを見るほうが、賃貸需要の実態に近いためです。公営・公社・都市再生機構の借家と給与住宅は民営借家に含まれないので、公的な賃貸住宅の多い地域では民営借家率が低くなります。

民営借家数（`H1322`）は2003年から2023年まで5年ごとに収録されており、政令市・特別区の区を含む市区町村単位で並んでいます。住宅・土地統計調査は標本調査なので、人口の少ない一部の町村は民営借家の集計対象に含まれません。

## 民営借家率は大阪市浪速区の70.7%が最も高く、上位は地方中枢都市の都心の区

全国の市区町村・区を2023年の民営借家率で並べた上位20です。居住世帯あり住宅数が2万戸未満の市区町村は除いています。住宅数が少ない町村では標本調査の誤差で比率が大きく変わり、上位が小規模な自治体で埋まってしまうためです。

```chart
{
  "height": 640,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "民営借家率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
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

上位は大阪市浪速区（70.7%）、福岡市博多区（62.7%）、福岡市中央区（58.5%）、大阪市西区（58.3%）、名古屋市中区（58.0%）で、地方中枢都市の都心の区です。住宅の7割が民営借家の浪速区のような地域では、賃貸に住む人が多く、賃貸経営では退去後の次の入居者が見つかりやすい市場と考えられます。

同じ都道府県の中でも、区によって民営借家率は大きく異なります。[都道府県別の分析](/showcase/housing-tenure-regional-gap)では都道府県ごとの平均を集計しましたが、大阪府を区の単位で見ると、浪速区は70.7%です。都道府県の平均値では、区ごとの賃貸需要の差は分かりません。

## 東京23区では、豊島区の54.9%と江東区の32.7%で約1.7倍の差がある

東京23区について、2023年の区ごとの民営借家率を集計しました。この節と次の地図では、住宅数2万戸以上の条件は使っていません。

```chart
{
  "height": 600,
  "layer": [
    {
      "data": {"name": "tokyo_ku"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "rate", "type": "quantitative"}, {"field": "ku", "type": "nominal"}],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "民営借家率（%）", "grid": true}
        },
        "y": {
          "field": "ku",
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

豊島区（54.9%）や中野区（54.4%）は単身者向けの賃貸が多く、民営借家率が高くなっています。江東区（32.7%）・葛飾区（33.5%）・足立区（34.8%）はファミリー層の持ち家の比率が比較的高く、民営借家率は低めです。同じ東京の賃貸市場でも、区によって主な入居者層が異なります。

## 東京都内では、民営借家率は都心の区で高く、多摩地域の市部に向かって下がる

東京都の市区町村別の2023年の民営借家率を地図にしました。

```map
type: map
layers:
  - from: tokyo_map
    geojson: geojson
    color: value
    label: pref_name
    name: "民営借家率（%）"
lng: 139.45
lat: 35.71
zoom: 8.5
```

豊島区・中野区・新宿区など山手線沿線の区の色が濃く、多摩地域の市部に向かうほど民営借家率は下がり、持ち家が多くなります。都市の中のこうした違いは、単身者向けとファミリー向けのどちらの物件にするかを判断する材料になります。

## 業務での使い方

市区町村・区単位の民営借家率は、賃貸投資・開発エリアの最初の絞り込みに使えます。

- エリアの絞り込み: 市区町村・区の単位で民営借家率を比較し、賃貸需要が大きいエリアを抽出する
- 物件タイプの判断: 民営借家率の高い都心の区は単身者向け、低めの郊外はファミリー向けと、エリアの入居者層に合わせて物件を企画する
- 都市内の比較: 同じ都市の中でも区によって需要が異なるので、都市全体の平均ではなく区単位で評価する

民営借家率が高いことは賃貸住宅が多いことを示しますが、需要が供給を上回っているかどうかは、家賃や空室率など別のデータで確認する必要があります。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別住宅データ（`h_municipal_housing`）を、2026年7月11日時点で取得して集計しています。元データは総務省統計局の[住宅・土地統計調査](https://www.stat.go.jp/data/jyutaku/index.html)の2023年（令和5年）調査で、調査は5年ごとに行われます。地図の境界は国土数値情報の行政区域データを使いました。

Queriaは、e-Statの社会・人口統計体系を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[市区町村別の住宅統計テーブル](/datasets/queria/e_stat/ssds/h_municipal_housing)から、関心のある市区町村・区の民営借家率を計算し、ほかの地域と比較できます。

```sql id=rank_top
WITH d AS (SELECT DISTINCT cat01, area_name, value FROM e_stat.ssds.h_municipal_housing WHERE year = 2023 AND cat01 IN ('H1101','H1322') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT area_name, MAX(value) FILTER (WHERE cat01='H1101') AS stock, MAX(value) FILTER (WHERE cat01='H1322') / MAX(value) FILTER (WHERE cat01='H1101') * 100 AS rate FROM d GROUP BY area_name) SELECT area_name, rate FROM (SELECT area_name, ROUND(rate, 1) AS rate FROM r WHERE stock >= 20000 ORDER BY rate DESC LIMIT 20) ORDER BY rate ASC
```

```sql id=tokyo_ku
WITH d AS (SELECT DISTINCT cat01, area, area_name, value FROM e_stat.ssds.h_municipal_housing WHERE year = 2023 AND cat01 IN ('H1101','H1322') AND area BETWEEN '13101' AND '13123' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT REPLACE(area_name, '東京都 ', '') AS ku, ROUND(MAX(value) FILTER (WHERE cat01='H1322') / MAX(value) FILTER (WHERE cat01='H1101') * 100, 1) AS rate FROM d GROUP BY area_name ORDER BY rate ASC
```

```sql id=tokyo_map
WITH d AS (SELECT DISTINCT cat01, area, area_name, value FROM e_stat.ssds.h_municipal_housing WHERE year = 2023 AND cat01 IN ('H1101','H1322') AND area LIKE '13%' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT area, REPLACE(area_name, '東京都 ', '') AS muni_name, ROUND(MAX(value) FILTER (WHERE cat01='H1322') / MAX(value) FILTER (WHERE cat01='H1101') * 100, 1) AS rate FROM d GROUP BY area, area_name) SELECT r.muni_name AS pref_name, ST_AsGeoJSON(ST_Simplify(m.geometry, 0.0005)) AS geojson, r.rate AS value, ROW_NUMBER() OVER (ORDER BY r.area) - 1 AS row_id FROM r JOIN nlftp.boundary.municipality m ON r.area = m.lg_code
```
