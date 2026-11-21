---
title: 給油所は22年で47.9%減り、1か所あたりの道路は22.1kmから44.6kmに伸びた
description: 全国の給油所数・ガソリン販売量・道路実延長を2001年度から2023年度まで集計しました。給油所は47.9%減り、ガソリン販売量の減少は23.3%でした。給油所1か所あたりの道路実延長は22.1kmから44.6kmへ2倍になりました。
ogDescription: 全国の給油所数・ガソリン販売量・道路実延長を2001年度から2023年度まで集計し、給油所1か所あたりの道路実延長と販売量の変化を都道府県別に比較しました。
publishedAt: 2026-08-21
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - ガソリンスタンド
  - 給油所
  - 道路
  - エネルギー
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 令和6年度末揮発油販売業者数及び給油所数
    url: https://www.enecho.meti.go.jp/category/resources_and_fuel/distribution/hinnkakuhou/250730.html
    publisher: 経済産業省資源エネルギー庁
  - title: 道路統計年報
    url: https://www.mlit.go.jp/road/ir/ir-data/tokei-nen/index.html
    publisher: 国土交通省
agentHint: e_stat.ssds.h_pref_housing の給油所数(H6120)と道路実延長(H7110)を使って、都道府県別に給油所1か所あたりの道路実延長を2001年度から2023年度まで出して。自分の県が全国平均より上か下かの推移も見せて
socialAnnounce: |-
  全国の給油所数とガソリン販売量、道路の長さを2001年度から並べました。

  店は47.9%減りましたが、販売量が減ったのは23.3%です。1か所が受け持つ道路は2倍に伸びています。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

全国の給油所は2001年度の52,592か所から2023年度の27,414か所へ47.9%減りました。同じ期間にガソリン販売量の減少は23.3%で、道路実延長は4.9%増えています。その結果、給油所1か所あたりの道路実延長は22.1kmから44.6kmへ2倍になりました。2023年度の値は岩手県の70.8kmが最も長く、大阪府の22.8kmの3.1倍です。給油所数の減少率が最も高いのは東京都の59.3%で、最も低い沖縄県の26.6%の2.2倍でした。

使ったのは e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)にある都道府県別の給油所数・ガソリン販売量・道路実延長です。3つを2001年度から2023年度まで同じ年度・同じ都道府県で並べ、給油所1か所あたりの道路実延長を年度別・都道府県別に計算しました。

## 給油所は47.9%減り、ガソリン販売量の減少は23.3%だった

社会・人口統計体系は、各省庁が別々に公表している統計を、都道府県・市区町村ごとに並べ直したものです。使ったのは「居住」分野の3つの指標で、いずれも年度の値です。

| コード | 内容           | 単位 | 収録期間           |
| ------ | -------------- | ---- | ------------------ |
| H6120  | 給油所数       | 箇所 | 2001年度〜2024年度 |
| H5205  | ガソリン販売量 | kl   | 1985年度〜2023年度 |
| H7110  | 道路実延長     | km   | 1975年度〜2023年度 |

給油所数（`H6120`）は、揮発油等の品質の確保等に関する法律にもとづいて登録された給油所を、年度末の3月31日時点で集計したものです。資源エネルギー庁が[揮発油販売業者数及び給油所数](https://www.enecho.meti.go.jp/category/resources_and_fuel/distribution/hinnkakuhou/250730.html)として毎年公表しています。道路実延長（`H7110`）は国土交通省の[道路統計年報](https://www.mlit.go.jp/road/ir/ir-data/tokei-nen/index.html)によるもので、高速道路を含まない一般の道路の長さです。ガソリン販売量（`H5205`）は、[項目の定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/H)によれば石油製品製造業者が販売業者向け・消費者向けに販売した量の合計で、給油所の店頭での販売実績とは異なります。出典は2012年度までが経済産業省の資源・エネルギー統計、2013年度以降が石油連盟の集計です。3つの値がすべてあるのは2001年度から2023年度までなので、この期間を集計しました。

全国の推移を、2001年度を100とした指数で並べます。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"st_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "st_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "st_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2001年度＝100", "grid": true}
        },
        "color": {
          "datum": "給油所数",
          "type": "nominal",
          "scale": {
            "domain": ["給油所数", "ガソリン販売量", "道路実延長"],
            "range": ["#ef4444", "#f97316", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"gas_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gas_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "gas_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2001年度＝100", "grid": true}
        },
        "color": {
          "datum": "ガソリン販売量",
          "type": "nominal",
          "scale": {
            "domain": ["給油所数", "ガソリン販売量", "道路実延長"],
            "range": ["#ef4444", "#f97316", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"road_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "road_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "road_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2001年度＝100", "grid": true}
        },
        "color": {
          "datum": "道路実延長",
          "type": "nominal",
          "scale": {
            "domain": ["給油所数", "ガソリン販売量", "道路実延長"],
            "range": ["#ef4444", "#f97316", "#3b82f6"]
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

給油所数は2001年度の52,592か所から2023年度の27,414か所へ、一度も増えずに減り続けました。減少率は47.9%で、半分近くです。ガソリン販売量は58,656,752klから44,999,666klへ減り、減少率は23.3%、およそ4分の1でした。この比率は2013年度の出典の切り替えをまたいでいます。道路実延長は1,164,795.7kmから1,221,849.3kmへ4.9%増えています。給油所数の減少率は、販売量の減少率のおよそ2倍です。

販売量は2004年度に107.8まで上がってから減少に転じ、2020年度に74.3まで下がったあと、2023年度は76.7まで戻しています。給油所数は、この販売量の増減にほとんど関係なく減り続けました。販売量の減少だけでは、給油所数の減少を説明できません。

## 給油所1か所あたりの道路実延長は、22.1kmから44.6kmへ2倍になった

給油所が減って道路の長さが変わらなければ、1か所あたりの道路実延長は長くなります。販売量の減少率が給油所数の減少率より小さければ、全国の販売量を給油所数で割った量は増えます。この2つを全国で計算しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "load"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"km_per_st\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#3b82f6",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 25}
          },
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "km_per_st", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年度", "format": "d"}
            },
            "y": {
              "field": "km_per_st",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "1か所あたりの道路（km）", "grid": true}
            },
            "color": {
              "datum": "1か所あたりの道路（km）",
              "type": "nominal",
              "scale": {
                "domain": ["1か所あたりの道路（km）", "1か所あたりに割り戻した販売量（kl）"],
                "range": ["#3b82f6", "#f97316"]
              },
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "load"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kl_per_st\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#f97316",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 25}
          },
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "kl_per_st", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年度", "format": "d"}
            },
            "y": {
              "field": "kl_per_st",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "1か所あたりに割り戻した販売量（kl）", "orient": "right"}
            },
            "color": {
              "datum": "1か所あたりに割り戻した販売量（kl）",
              "type": "nominal",
              "scale": {
                "domain": ["1か所あたりの道路（km）", "1か所あたりに割り戻した販売量（kl）"],
                "range": ["#3b82f6", "#f97316"]
              },
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    }
  ],
  "resolve": {"scale": {"y": "independent"}},
  "config": {"legend": {"orient": "bottom"}}
}
```

給油所1か所あたりの道路実延長は、2001年度の22.1kmから2023年度の44.6kmへ2倍になりました。青い線は一度も下がらずに伸び続けています。

1か所あたりの販売量は1,115klから1,641klへ1.47倍になりました。これは全国のガソリン販売量を給油所数で割った値で、1店の店頭での販売実績ではありません。この値は2016年度の1,688klが最も多く、2020年度に1,503klまで下がってから戻しています。近年は横ばいです。

給油所の数は半分近くに減りましたが、販売量の減少は4分の1にとどまり、残った給油所1か所あたりの道路実延長と販売量はどちらも増えました。

## 1か所あたりの道路実延長は、岩手県が大阪府の3.1倍

2023年度の値を47都道府県で並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "km_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "km", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "km",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給油所1か所あたりの道路実延長（km）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "km_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "km", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "km",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給油所1か所あたりの道路実延長（km）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "km_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "km", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "km",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給油所1か所あたりの道路実延長（km）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
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

最も長いのは岩手県の70.8kmで、最も短い大阪府の22.8kmの3.1倍です。長野県（63.3km）・島根県（62.5km）・群馬県（61.9km）・岡山県（59.7km）が続きます。

面積の最も広い北海道は53.9kmで8位です。北海道の給油所は2023年度で1,668か所あり、東京都の898か所や大阪府の869か所を大きく上回ります。そのため道路の長さを給油所数で割ると、岩手県より短くなります。1か所あたりの道路実延長は、面積ではなく、道路の長さと給油所数の両方で決まります。

短い県は大阪府（22.8km）・沖縄県（25.9km）・東京都（27.2km）で、香川県（31.0km）・山梨県（33.4km）が続きます。

## 給油所数の減少率が最も高いのは東京都の59.3%

2001年度から2023年度までの給油所数の減少率を都道府県別に地図にしました。色が濃いほど減少率が高い県です。

```map
type: map
layers:
  - from: map
    geojson: geojson
    color: decline_pct
    label: pref_name
    name: "減少率（%）"
lng: 137
lat: 36.5
zoom: 4
```

減少率が最も高いのは東京都の59.3%で、2,209か所が898か所になりました。神奈川県が55.5%、千葉県が54.2%、大阪府が53.6%と続きます。5割を超える県は関東と東海に多く、群馬県（53.3%）・静岡県（52.7%）・栃木県（52.3%）が入りますが、九州の佐賀県（51.8%）・熊本県（51.3%）も同じ水準です。

最も低いのは沖縄県の26.6%で、432か所から317か所に減りました。東京都との差は2.2倍です。北海道が36.1%、富山県が39.8%、秋田県が41.0%と続きます。

減少率の上位には大都市のある都府県が並びます。給油所が多く集まっていた地域では、1か所が閉じても近くの給油所で給油できるためと考えられます。佐賀県・熊本県も5割を超えているので、都市かどうかだけでは決まっていません。もともと給油所が少なく、1か所が閉じると近くに代わりの給油所がない地域では、同じ割合では減らないと考えられます。資源エネルギー庁は[SS過疎地対策](https://www.enecho.meti.go.jp/category/resources_and_fuel/distribution/sskasochi/)として、市町村内の給油所が少ない地域への支援を続けています。減少率が低いことは、経営が楽であることを意味しません。

## 業務での使い方

- 営業エリアの県の、給油所1か所あたりの道路実延長が47都道府県のどこにあるかを確認する。岩手県の70.8kmと大阪府の22.8kmでは3.1倍の差があります。全国平均の44.6kmより長い県では、1か所が閉じたときに、残りの給油所1か所あたりの道路実延長の増え方も大きくなります
- 1か所あたりの道路実延長と、これまでの減少率を並べて自県の位置を確認する。北海道は道路実延長が53.9kmで8位、減少率は36.1%で低いほうから2番目です。東京都は道路実延長が27.2kmで短いほうから3番目、減少率は59.3%で最も高くなっています。2つの指標は連動していないので、両方を確認します
- 自県の1か所あたりの道路実延長を、年度をさかのぼって計算する。全国では2001年度の22.1kmから2023年度の44.6kmへ一度も下がらずに伸びました。同じ2指標（`H6120` と `H7110`）を自県に絞って年度別に集計すると、伸び方が全国より速いか遅いかが分かります

## データの出典

本記事は e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)から、都道府県別の給油所数・ガソリン販売量・道路実延長を2026年8月21日時点で集計しています。元データはそれぞれ資源エネルギー庁の揮発油販売業者数及び給油所数、石油連盟と経済産業省によるガソリン販売量の集計、国土交通省の道路統計年報で、数値はすべて年度の値です。

Queriaは、省庁ごとに別々に公表されるオープンデータを、列名・単位・文字コードを統一し、指標コードと収録期間の説明を付けて公開しています。本記事で使った[居住分野の都道府県データ](/datasets/queria/e_stat/ssds/h_pref_housing)から、営業エリアの県の値を年度をさかのぼって確認したり、道路種別や住宅着工などほかの指標と比較したりできます。

```sql id=coverage
SELECT cat01, MIN(year) AS first_year, MAX(year) AS last_year, COUNT(DISTINCT year) AS years FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H6120', 'H5205', 'H7110') AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY cat01 ORDER BY cat01
```

```sql id=trend
WITH n AS (SELECT year, SUM(CASE WHEN cat01 = 'H6120' THEN TRY_CAST(value AS DOUBLE) END) AS st, SUM(CASE WHEN cat01 = 'H5205' THEN TRY_CAST(value AS DOUBLE) END) AS gas, SUM(CASE WHEN cat01 = 'H7110' THEN TRY_CAST(value AS DOUBLE) END) AS road FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H6120', 'H5205', 'H7110') AND area_name <> '全国' AND year BETWEEN 2001 AND 2023 GROUP BY year), b AS (SELECT st AS st0, gas AS gas0, road AS road0 FROM n WHERE year = 2001) SELECT n.year AS year, ROUND(100.0 * n.st / b.st0, 1) AS st_idx, ROUND(100.0 * n.gas / b.gas0, 1) AS gas_idx, ROUND(100.0 * n.road / b.road0, 1) AS road_idx, n.st AS stations, n.gas AS gasoline, n.road AS road_km FROM n CROSS JOIN b ORDER BY n.year
```

```sql id=load
WITH n AS (SELECT year, SUM(CASE WHEN cat01 = 'H6120' THEN TRY_CAST(value AS DOUBLE) END) AS st, SUM(CASE WHEN cat01 = 'H5205' THEN TRY_CAST(value AS DOUBLE) END) AS gas, SUM(CASE WHEN cat01 = 'H7110' THEN TRY_CAST(value AS DOUBLE) END) AS road FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H6120', 'H5205', 'H7110') AND area_name <> '全国' AND year BETWEEN 2001 AND 2023 GROUP BY year) SELECT year, ROUND(road / st, 1) AS km_per_st, ROUND(gas / st, 0) AS kl_per_st FROM n ORDER BY year
```

```sql id=km_top
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H6120' THEN TRY_CAST(value AS DOUBLE) END) AS st, MAX(CASE WHEN cat01 = 'H7110' THEN TRY_CAST(value AS DOUBLE) END) AS road FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H6120', 'H7110') AND area_name <> '全国' AND year = 2023 GROUP BY 1), ranked AS (SELECT area_name AS pref, ROUND(road / st, 1) AS km, ROW_NUMBER() OVER (ORDER BY road / st DESC, area_name) AS rn FROM d) SELECT pref, km FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=km_mid
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H6120' THEN TRY_CAST(value AS DOUBLE) END) AS st, MAX(CASE WHEN cat01 = 'H7110' THEN TRY_CAST(value AS DOUBLE) END) AS road FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H6120', 'H7110') AND area_name <> '全国' AND year = 2023 GROUP BY 1), ranked AS (SELECT area_name AS pref, ROUND(road / st, 1) AS km, ROW_NUMBER() OVER (ORDER BY road / st DESC, area_name) AS rn FROM d) SELECT pref, km FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=km_bottom
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H6120' THEN TRY_CAST(value AS DOUBLE) END) AS st, MAX(CASE WHEN cat01 = 'H7110' THEN TRY_CAST(value AS DOUBLE) END) AS road FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H6120', 'H7110') AND area_name <> '全国' AND year = 2023 GROUP BY 1), ranked AS (SELECT area_name AS pref, ROUND(road / st, 1) AS km, ROW_NUMBER() OVER (ORDER BY road / st DESC, area_name) AS rn FROM d) SELECT pref, km FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=map
WITH d AS (SELECT area_name, MAX(CASE WHEN year = 2001 THEN TRY_CAST(value AS DOUBLE) END) AS st01, MAX(CASE WHEN year = 2023 THEN TRY_CAST(value AS DOUBLE) END) AS st23 FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H6120' AND area_name <> '全国' AND year IN (2001, 2023) GROUP BY 1) SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, ROUND(100.0 * (d.st01 - d.st23) / d.st01, 1) AS decline_pct, b.prefecture_name AS pref_name, d.st01 AS stations_2001, d.st23 AS stations_2023 FROM nlftp.boundary.prefecture b JOIN d ON d.area_name = b.prefecture_name
```
