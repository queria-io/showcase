---
title: 中古マンションの㎡単価は10年で全国1.7倍、福岡県は2倍になり、秋田県と山形県は下がった
description: 国土交通省の不動産取引価格情報から、2007〜2024年の中古マンションの㎡単価中央値を集計しました。全国の中央値は2014年の31万円から2024年の53万円へ約1.7倍になり、福岡県は2倍になりました。秋田県と山形県は2014年より下がっています
publishedAt: 2026-03-16
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 不動産
  - 中古マンション
  - 地域格差
datasets:
  - queria/reinfolib
  - queria/nlftp
sources:
  - title: 不動産情報ライブラリ（不動産取引価格情報）
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
agentHint: 秋田県と山形県の中古マンション㎡単価を2007年以降の年次推移で出して。下落がいつ始まったかを、10年で2倍になった福岡県と重ねて
socialAnnounce: |-
  中古マンションの㎡単価が、この10年で全国平均1.7倍になりました。
  福岡県は2倍。東北の一部では下落した県も。

  都市と地方で広がる価格格差を、18年分のデータで追いました。
---

中古マンションの㎡単価の中央値は、全国で2014年の31万円から2024年の53万円へ、10年で約1.7倍になりました。都道府県別では福岡県が20万円から40万円へ2倍になり、沖縄県・大阪府・富山県も8割以上上がっています。秋田県と山形県は、2024年の㎡単価が2014年を下回りました。2024年の㎡単価は東京都が100万円で最も高く、20万円前後の県とは5倍以上の差があります。

この記事では、国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が提供する不動産取引価格情報から、2007〜2024年の中古マンションの取引を集計しました。

## 全国の㎡単価中央値は2013年から上がり続け、2024年は53万円

不動産情報ライブラリの不動産取引価格情報（`mart_trade_prices`）には、取引ごとの物件種別・所在地・面積・取引価格などが記録されています。成約した取引の記録ですが、すべての取引を収録しているわけではありません。主な物件種別は次のとおりです。

| 物件種別         | 内容                             |
| ---------------- | -------------------------------- |
| 宅地(土地と建物) | 一戸建て（土地付き）             |
| 宅地(土地)       | 更地・宅地                       |
| 中古マンション等 | 中古マンション・テラスハウスなど |
| 農地             | 田・畑                           |
| 林地             | 山林                             |

ここでは中古マンション等（`property_type = '中古マンション等'`）の取引に絞り、㎡単価（取引価格÷専有面積）の中央値を年ごとに集計しました。専有面積（`area`）または取引価格が0以下の取引は除いています。少数の高額な物件の影響を受けないように、平均ではなく中央値を使います。

```chart
{
  "layer": [
    {
      "data": {"name": "price_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"unit_man\"]) ? 0 : 1",
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
          {"field": "unit_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "unit_man",
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

全国の㎡単価中央値は、2007〜2013年は29〜30万円前後で推移し、2013年からは毎年上がって、2024年は53万円です。2014年（31万円）と比較すると、10年で約1.7倍になりました。中央値の変化には、その年に取引された物件の築年数・立地・面積の構成の変化も含まれます。築年数の浅い大規模な物件の取引が多い年は、相場が変わらなくても中央値が上がります。

## 2024年の㎡単価は東京都が100万円で、2位の神奈川県は55万円

2024年の取引を都道府県別に集計し、地図にしました。取引が10件未満の都道府県は除いています。

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

東京都の㎡単価は100万円で、2位の神奈川県（55万円）や大阪府・京都府（各50万円）を大きく上回ります。東北・北陸・四国・九州の一部には20万円前後の県が多く、東京都とは5倍以上の差があります。県庁所在地と郡部などの県内の差は、都道府県単位の集計には表れません。

## 2014年から2024年の上昇率は福岡県の+100%が最も高く、秋田県と山形県は下がった

2014年から2024年までの㎡単価中央値の変化率を、都道府県別に算出しました。2014年と2024年の両方で取引が20件以上ある県が対象で、47都道府県すべてがこの条件を満たしています。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "price_change"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "increase_pct", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "increase_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "㎡単価の変化率（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b"},
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

上昇率が最も高いのは福岡県（+100%）で、2014年の20万円/㎡から2024年は40万円/㎡と、10年で2倍になりました。沖縄県（+88%）、大阪府（+86%）、富山県（+85%）、石川県（+75%）が続きます。東京都（+67%）は、上昇率ではこれらの県より低くなっています。

秋田県（-6%）と山形県（-9%）は、2024年の㎡単価が2014年を下回りました。人口減少の影響が不動産の価格にも表れていると考えられます。

## まとめ

- 全国の中古マンションの㎡単価中央値は2013年から毎年上がり、2024年は53万円/㎡で、2014年の約1.7倍です
- 2024年の㎡単価は東京都が100万円/㎡で最も高く、神奈川県（55万円）、大阪府・京都府（各50万円）が続きます
- 2014年からの上昇率は福岡県の+100%が最も高く、沖縄県や北陸の県でも大きく上がっています
- 秋田県と山形県は、2024年の㎡単価が2014年より低くなっています

## データの出典

本記事は国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公開する不動産取引価格情報を、2026年7月11日時点で取得して集計しています。対象は2007〜2024年に成約した中古マンション等の取引です。

Queriaは、国土交通省の不動産取引価格情報を、列名・単位・文字コードを統一したテーブルにし、物件種別や項目の意味をメタデータに記載して公開しています。本記事で使った[不動産取引価格テーブル](/datasets/queria/reinfolib/main/mart_trade_prices)から、関心のある地域の㎡単価の推移を確認したり、物件種別ごとに比較したりできます。

```sql id=price_trend
SELECT year, ROUND(MEDIAN(trade_price / NULLIF(area, 0)) / 10000) AS unit_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND year BETWEEN 2007 AND 2024 GROUP BY year ORDER BY year
```

```sql id=price_map
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(MEDIAN(r.trade_price / NULLIF(r.area, 0)) / 10000) AS unit_price_man FROM nlftp.boundary.prefecture p JOIN reinfolib.main.mart_trade_prices r ON p.prefecture_name = r.prefecture WHERE r.property_type = '中古マンション等' AND r.area > 0 AND r.trade_price > 0 AND r.year = 2024 GROUP BY p.prefecture_name, p.geometry HAVING COUNT(*) >= 10
```

```sql id=price_change
WITH y2014 AS ( SELECT prefecture, MEDIAN(trade_price / NULLIF(area, 0)) AS unit_price FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND year = 2014 GROUP BY prefecture HAVING COUNT(*) >= 20 ), y2024 AS ( SELECT prefecture, MEDIAN(trade_price / NULLIF(area, 0)) AS unit_price FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND year = 2024 GROUP BY prefecture HAVING COUNT(*) >= 20 ) SELECT a.prefecture, ROUND((b.unit_price - a.unit_price) / a.unit_price * 100) AS increase_pct FROM y2014 a JOIN y2024 b ON a.prefecture = b.prefecture ORDER BY increase_pct DESC
```
