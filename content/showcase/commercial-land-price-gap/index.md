---
title: 商業地の㎡単価は、東京都の87万円と秋田県の1.8万円で約48倍違う
description: 国土交通省の不動産取引価格情報から、商業地として取引された宅地の㎡単価中央値を都道府県別に集計しました。2024年は東京都が87.0万円、秋田県が1.8万円で約48倍の差があります。全国の中央値は2013年の6.6万円を底に、2022年以降は上がっています
publishedAt: 2026-05-27
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 不動産
  - 商業地
  - 出店戦略
  - 地域格差
datasets:
  - queria/reinfolib
  - queria/nlftp
sources:
  - title: 不動産情報ライブラリ
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 商業地の㎡単価中央値を2013年と2024年で都道府県別に比べて、上昇率が大きい県を出して
socialAnnounce: |-
  全国の商業地取引データを都道府県別に集計しました。2024年の㎡単価中央値は東京87万円、秋田1.8万円。

  出店候補地の比較や、初期投資の見積もりに。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2024年に商業地として取引された宅地の㎡単価の中央値は、東京都が87.0万円、秋田県が1.8万円で、約48倍の差がありました。2位の神奈川県は38.0万円で、東京都はその2倍以上です。全国の中央値は8.0万円で、2013年の6.6万円を底に、2022年以降は上がっています。

出店候補地を比較するときは、商圏人口や駅前の歩行者数とともに、土地の取得や賃借にかかる費用の水準を把握しておく必要があります。この記事では、国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公表する不動産取引価格情報から、商業地の宅地の㎡単価を都道府県別に集計しました。

## 集計の対象は、商業地として取引された更地の宅地

不動産情報ライブラリの不動産取引価格情報（`reinfolib.main.mart_trade_prices`）は、宅地建物取引業者へのアンケート調査をもとに整備された、取引1件ごとの価格のデータです。アンケートに基づくので、すべての取引を収録しているわけではありません。物件種別と土地用途区分は次のとおりです。

| 物件種別         | region 区分                           |
| ---------------- | ------------------------------------- |
| 宅地(土地と建物) | 住宅地 / 商業地 / 工業地など          |
| 宅地(土地)       | 住宅地 / 商業地 / 工業地 / 宅地見込地 |
| 中古マンション等 | (区分なし)                            |
| 農地             | (区分なし)                            |
| 林地             | (区分なし)                            |

ここでは `property_type = '宅地(土地)'` のうち `region = '商業地'` の取引に絞りました。「宅地(土地と建物)」を含めると、建物の価値が単価に混ざるためです。㎡単価は取引価格を面積で割った `unit_price` 列の値を万円に換算して使い、`unit_price` が0以下の取引は除いています。少数の高額取引の影響を受けないように、平均ではなく中央値を使います。2024年の商業地の取引は、47都道府県すべてで10件以上あります。

## 全国の中央値は2013年の6.6万円が底で、2024年は8.0万円

全国の商業地の㎡単価中央値の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_price_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "unit_price_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

2007年の11.0万円/㎡から2013年の6.6万円/㎡まで下がり続け、2014〜2021年は6.5〜7.0万円/㎡で横ばいでした。2022年からは緩やかに上がり、2024年は8.0万円/㎡です。年ごとの中央値の変化には、その年にどの地区の取引が多かったかという違いも含まれます。

都道府県ごとの動きは、この全国の推移とは異なります。次に、2024年の都道府県別の水準を示します。

## 東京都は87.0万円で、2位の神奈川県の2倍以上

2024年の商業地の取引から、都道府県別の㎡単価中央値を算出しました。取引が10件以上ある都道府県が対象です。47都道府県を上位10・中間27・下位10の3グループに色分けしています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unit_price_man", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
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
        "tooltip": [
          {"field": "unit_price_man", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
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
        "tooltip": [
          {"field": "unit_price_man", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
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

東京都は87.0万円/㎡で、2位の神奈川県（38.0万円）の2倍以上です。大阪府（34.0万円）、京都府（33.0万円）、兵庫県（17.0万円）が続き、上位5都府県はすべて首都圏と近畿圏です。最も低いのは秋田県（1.8万円）で、鳥取県（2.7万円）、山形県（3.0万円）、青森県・岩手県（各3.1万円）と、東北と山陰の県が並びます。秋田県と東京都の差は約48倍です。

中間の27県は3.5〜8.5万円/㎡の範囲にあり、そのうち21県が4〜6万円台です。地方の主要都市がある県とそのほかの県の差は小さく、広島県（12.0万円）や福岡県（9.9万円）も、東京都とは7倍以上の差があります。

## 単価の高い県は、首都圏・近畿圏・福岡県の周辺に集まっている

同じ2024年のデータを地図にしました。色が濃いほど商業地の㎡単価が高い県です。

```map
type: map
layers:
  - from: price_map
    geojson: geojson
    color: unit_price_man
    label: pref_name
    name: "㎡単価（万円）"
lng: 137
lat: 36.5
zoom: 4
```

色の濃い県は首都圏・近畿圏・福岡県の周辺にあり、東北から日本海側にかけての県は色が薄くなっています。この中央値は区画の位置・面積・接道条件・容積率を調整していないので、同じ県の中の駅前の繁華街と郊外の沿道の商業地が混ざった値です。出店を検討する最初の段階で、候補の県が何万円/㎡の水準かを把握する目安として使えます。

## 東京都・神奈川県・大阪府は2022年から上昇が速く、愛知県と福岡県は変動が小さい

商業地の取引件数が多い東京都・神奈川県・大阪府・愛知県・福岡県の推移を比較します。取引が20件以上ある年だけを対象にしています。

```chart
{
  "layer": [
    {
      "data": {"name": "trend_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_price_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "unit_price_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "神奈川県", "大阪府", "愛知県", "福岡県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_kanagawa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_price_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "unit_price_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "神奈川県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "神奈川県", "大阪府", "愛知県", "福岡県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_osaka"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_price_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "unit_price_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "大阪府",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "神奈川県", "大阪府", "愛知県", "福岡県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_aichi"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_price_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "unit_price_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "愛知県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "神奈川県", "大阪府", "愛知県", "福岡県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_fukuoka"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_price_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "unit_price_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_price_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "福岡県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "神奈川県", "大阪府", "愛知県", "福岡県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

東京都は2007年の71.0万円/㎡から2012年の48.0万円/㎡まで下がり、2013年からはおおむね上がり続けて、2024年は87.0万円/㎡と2007年の水準を上回りました。大阪府は2010年代に19〜24万円/㎡で推移し、2022年から上昇が速くなって2024年は34.0万円/㎡です。神奈川県は2010年代に25〜32万円/㎡で推移し、2022年から上昇が速くなって2024年は38.0万円/㎡です。愛知県は2008年から11〜14万円/㎡、福岡県は6〜10万円/㎡で推移しており、5都府県の中では変動が小さくなっています。

東京都・神奈川県・大阪府は単価が高く、近年の上昇も速いので、出店では用地の費用と確保の時期の両方を他の県とは別に検討する必要があると考えられます。愛知県や福岡県は相場が比較的安定しているので、長期の計画で物件を比較しやすいと考えられます。

## 業務での使い方

- 出店候補地の絞り込み: 売上計画から出店できる㎡単価の範囲を出し、各都道府県の中央値と比較して候補の県を絞り込めます
- 初期投資の概算: 必要な面積と各県の㎡単価中央値から土地の取得費用の目安を試算し、地域別の収益モデルを比較できます
- 物件評価の基準: 同業の競合店がある県の㎡単価と自社の出店予定地域の㎡単価を比較し、物件評価の基準にできます。このデータは土地の取得価格なので、賃料の水準は別に確認する必要があります
- 地域ごとの出店計画: 主要都府県の推移から上昇が速い県と安定している県を区別し、出店の優先順位を決める材料にできます

## まとめ

- 2024年の商業地の㎡単価中央値は、東京都の87.0万円から秋田県の1.8万円まで、約48倍の差があります
- 全国の中央値は2013年に6.6万円まで下がり、2021年まで横ばいで、2022年から緩やかに上がっています
- 上位は東京都・神奈川県・大阪府・京都府・兵庫県で、首都圏と近畿圏に集まっています
- 主要5都府県では、東京都・神奈川県・大阪府の上昇が2022年から速く、愛知県と福岡県は比較的安定しています

## データの出典

本記事は国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公表する不動産取引価格情報を、2026年7月11日時点で取得して集計しています。対象は2007年から2024年までに商業地として取引された宅地です。地図の境界には国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、不動産取引価格情報を列名・単位・文字コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[不動産取引価格テーブル](/datasets/queria/reinfolib/main/mart_trade_prices)から、候補の県の相場を取得したり、自社の出店計画と比較したりできます。

```sql id=national_trend
SELECT year, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND year BETWEEN 2007 AND 2024 GROUP BY year ORDER BY year
```

```sql id=rank_top
WITH ranked AS (SELECT prefecture, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man, ROW_NUMBER() OVER (ORDER BY MEDIAN(unit_price) DESC, prefecture) AS rn FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND year = 2024 GROUP BY prefecture HAVING COUNT(*) >= 10) SELECT prefecture, unit_price_man FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT prefecture, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man, ROW_NUMBER() OVER (ORDER BY MEDIAN(unit_price) DESC, prefecture) AS rn FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND year = 2024 GROUP BY prefecture HAVING COUNT(*) >= 10) SELECT prefecture, unit_price_man FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH ranked AS (SELECT prefecture, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man, ROW_NUMBER() OVER (ORDER BY MEDIAN(unit_price) DESC, prefecture) AS rn FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND year = 2024 GROUP BY prefecture HAVING COUNT(*) >= 10) SELECT prefecture, unit_price_man FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=price_map
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(MEDIAN(r.unit_price) / 10000, 1) AS unit_price_man FROM nlftp.boundary.prefecture p JOIN reinfolib.main.mart_trade_prices r ON p.prefecture_name = r.prefecture WHERE r.property_type = '宅地(土地)' AND r.region = '商業地' AND r.unit_price > 0 AND r.year = 2024 GROUP BY p.prefecture_name, p.geometry HAVING COUNT(*) >= 10
```

```sql id=trend_tokyo
SELECT year, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND prefecture = '東京都' AND year BETWEEN 2007 AND 2024 GROUP BY year HAVING COUNT(*) >= 20 ORDER BY year
```

```sql id=trend_kanagawa
SELECT year, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND prefecture = '神奈川県' AND year BETWEEN 2007 AND 2024 GROUP BY year HAVING COUNT(*) >= 20 ORDER BY year
```

```sql id=trend_osaka
SELECT year, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND prefecture = '大阪府' AND year BETWEEN 2007 AND 2024 GROUP BY year HAVING COUNT(*) >= 20 ORDER BY year
```

```sql id=trend_aichi
SELECT year, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND prefecture = '愛知県' AND year BETWEEN 2007 AND 2024 GROUP BY year HAVING COUNT(*) >= 20 ORDER BY year
```

```sql id=trend_fukuoka
SELECT year, ROUND(MEDIAN(unit_price) / 10000, 1) AS unit_price_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '商業地' AND unit_price > 0 AND prefecture = '福岡県' AND year BETWEEN 2007 AND 2024 GROUP BY year HAVING COUNT(*) >= 20 ORDER BY year
```
