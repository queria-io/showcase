---
title: 商業地の値段のうち、家賃で説明できる割合は、東京23区で9割近く、政令市以外の市町村で6割弱
description: 地価公示の鑑定評価書で、商業地の評価額のうち家賃から逆算した値段が占める割合を比較しました。2026年は東京23区87.2%、政令市以外の市町村58.7%です。
ogDescription: 地価公示の鑑定評価書を地点ごとに集計しました。商業地の評価額のうち家賃から逆算した値段が占める割合は、2026年に東京23区87.2%、政令市以外の市町村58.7%です。
publishedAt: 2026-09-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 地価
  - 不動産
  - 賃料
  - 融資
datasets:
  - queria/reinfolib
  - queria/soumu
sources:
  - title: 地価公示
    url: https://www.mlit.go.jp/totikensangyo/totikensangyo_fr4_000043.html
    publisher: 国土交通省
  - title: 不動産情報ライブラリ
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
agentHint: 住宅地の標準地で、2022年から2026年までの収益価格を鑑定評価額で割った割合を、東京23区・政令指定都市・それ以外の市町村に分けて年ごとに出して
socialAnnounce: |-
  地価公示の鑑定評価書を地点ごとに追いました。

  商業地の評価額のうち家賃から逆算できる割合は、東京23区87.2%、政令市以外の市町村58.7%。融資の担保評価に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

商業地の鑑定評価額のうち、家賃収入から逆算した値段で説明できる割合は、2026年に東京23区が87.2%、政令指定都市が73.6%、それ以外の市町村が58.7%でした。23区はこの4年で評価額が4割上がっても割合がほとんど変わりませんでした。値段がほとんど動いていない政令市以外の市町村では、割合が2022年から毎年下がっています。

テナントビルや店舗の取得資金を融資するときは、担保になる土地の値段と、その土地から入る家賃収入の両方を確認します。土地の値段がどこまで家賃収入で裏付けられているかは、地価の数字だけでは分かりません。

毎年1月1日時点の土地の値段を国が公表する[地価公示](https://www.mlit.go.jp/totikensangyo/totikensangyo_fr4_000043.html)では、地点ごとに不動産鑑定士が鑑定評価書を書いています。評価書には、近くの取引事例から求めた値段（比準価格）と、その土地に建物を建てて貸したときの家賃収入から逆算した値段（収益価格）の両方が載っています。この記事では、商業地の鑑定評価書を2022年から2026年まで地点ごとに結合し、地域ごとに比較します。

## 家賃で説明できる割合は、都心ほど高い

データは国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公開する鑑定評価書情報です。1地点に評価書が2通あるので、その平均を使います。この記事で使う項目は次のとおりです。

| 項目       | 内容                                                     |
| ---------- | -------------------------------------------------------- |
| 鑑定評価額 | 鑑定士が最終的に決めた1㎡あたりの価格                    |
| 比準価格   | 近くの取引事例の価格から出した1㎡あたりの価格            |
| 収益価格   | 家賃収入から逆算した1㎡あたりの価格                      |
| 総収益     | その土地に想定した建物を貸したときの、年間の賃料収入など |
| 還元利回り | 家賃収入から土地の値段を逆算するときに割り戻す利回り     |

収益価格は、基本的には、総収益から経費と建物の取り分を差し引いた「土地の取り分」を、還元利回りで割って求めます。ここでの家賃は実際の契約賃料ではなく、鑑定士がその土地に最も効率のよい建物を想定して見積もった値です。

2026年の商業地の標準地は6,509地点あります。そのうち5年とも総収益と還元利回りがそろう5,486地点を、東京23区（665地点）、政令指定都市（1,496地点）、それ以外の市町村（3,325地点）に分けました。途中の年で標準地の番号が変わった地点は、別の地点として扱われるため含まれません。それ以外の市町村では、2026年の4,258地点のうち837地点（19.7%）で収益価格そのものが求められておらず、この集計に入っていません。23区は674地点すべて、政令指定都市は1,577地点のうち25地点を除いて求められています。収益価格を鑑定評価額で割った値を、この記事では「家賃で説明できる割合」と呼びます。次の図は、その中央値を年ごとに描いたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"share_tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "share_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "share_tokyo",
          "type": "quantitative",
          "scale": {"domain": [50, 100], "zero": false, "nice": false},
          "axis": {"title": "収益価格 ÷ 鑑定評価額（%）", "grid": true}
        },
        "color": {
          "datum": "東京23区",
          "type": "nominal",
          "scale": {
            "domain": ["東京23区", "政令指定都市", "それ以外の市町村"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"share_major\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "share_major", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "share_major",
          "type": "quantitative",
          "scale": {"domain": [50, 100], "zero": false, "nice": false},
          "axis": {"title": "収益価格 ÷ 鑑定評価額（%）", "grid": true}
        },
        "color": {
          "datum": "政令指定都市",
          "type": "nominal",
          "scale": {
            "domain": ["東京23区", "政令指定都市", "それ以外の市町村"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"share_other\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "share_other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "share_other",
          "type": "quantitative",
          "scale": {"domain": [50, 100], "zero": false, "nice": false},
          "axis": {"title": "収益価格 ÷ 鑑定評価額（%）", "grid": true}
        },
        "color": {
          "datum": "それ以外の市町村",
          "type": "nominal",
          "scale": {
            "domain": ["東京23区", "政令指定都市", "それ以外の市町村"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

23区の割合は5年間、87.2%から88.9%の間にあります。政令指定都市は76.1%から73.6%へ、それ以外の市町村は62.2%から58.7%へ下がりました。収益価格が評価額の半分に届かない地点は、23区では2026年に0.2%しかありませんが、それ以外の市町村では2022年の25.0%から2026年の31.8%に増えています。

鑑定評価額は、取引事例から出した比準価格に沿って決まっています。2026年に比準価格を評価額で割った値の中央値は、23区が105.6%、政令指定都市が102.8%、それ以外の市町村が101.3%です。

## 23区の割合を保ったのは、利回りの低下と土地の取り分の伸び

23区の割合がほとんど動かなかったのは、値段が上がらなかったからではありません。次の図は、2022年を100として、地点ごとの鑑定評価額（実線）と総収益（破線）の伸びの中央値を描いたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"price_tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "price_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "price_tokyo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "23区 評価額",
          "type": "nominal",
          "scale": {
            "domain": ["23区 評価額", "23区 家賃", "政令市 評価額", "政令市 家賃", "それ以外 評価額", "それ以外 家賃"],
            "range": ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6", "#64748b", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rent_tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "rent_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "rent_tokyo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "23区 家賃",
          "type": "nominal",
          "scale": {
            "domain": ["23区 評価額", "23区 家賃", "政令市 評価額", "政令市 家賃", "それ以外 評価額", "それ以外 家賃"],
            "range": ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6", "#64748b", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"price_major\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "price_major", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "price_major",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "政令市 評価額",
          "type": "nominal",
          "scale": {
            "domain": ["23区 評価額", "23区 家賃", "政令市 評価額", "政令市 家賃", "それ以外 評価額", "それ以外 家賃"],
            "range": ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6", "#64748b", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rent_major\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "rent_major", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "rent_major",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "政令市 家賃",
          "type": "nominal",
          "scale": {
            "domain": ["23区 評価額", "23区 家賃", "政令市 評価額", "政令市 家賃", "それ以外 評価額", "それ以外 家賃"],
            "range": ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6", "#64748b", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"price_other\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "price_other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "price_other",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "それ以外 評価額",
          "type": "nominal",
          "scale": {
            "domain": ["23区 評価額", "23区 家賃", "政令市 評価額", "政令市 家賃", "それ以外 評価額", "それ以外 家賃"],
            "range": ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6", "#64748b", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rent_other\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "rent_other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価公示の年（1月1日時点）", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "rent_other",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "それ以外 家賃",
          "type": "nominal",
          "scale": {
            "domain": ["23区 評価額", "23区 家賃", "政令市 評価額", "政令市 家賃", "それ以外 評価額", "それ以外 家賃"],
            "range": ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6", "#64748b", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

23区の評価額は143.4まで上がりましたが、総収益は108.5です。家賃の伸びは値段の伸びの5分の1ほどでした。それでも収益価格が評価額との比を保ったのは、2つの動きが重なったためです。1つは還元利回りの低下で、中央値は3.9%から3.2%に下がりました。同じ土地の取り分でも、割り戻す利回りが下がれば値段は3.9 ÷ 3.2 で約1.22倍になります。もう1つは土地の取り分の伸びで、総収益から経費と建物の取り分を引いた残りは113.3と、総収益より大きく伸びています。2つを掛け合わせると約1.38倍で、評価額の1.434倍に近い値になります。

それ以外の市町村では、評価額が103.9、総収益が103.5で、2本の線はほとんど重なっていて、家賃は値段と同じだけ伸びました。一方で、土地の取り分は97.3に減っています。総収益から差し引く経費と建物の取り分が、総収益より大きく伸びたことになります。還元利回りは4.9%から4.7%への低下にとどまりました。家賃が伸びても土地に残る分が減ったため、評価額のうち家賃で説明できる割合が下がっています。

## 家賃で説明できる割合が50%を下回る15市は、すべて政令市以外の市

次の図は、5年分そろう地点が15以上ある市区について（23区のうち2区と、政令指定都市のうち2市はこの条件に届かず含まれません）、横軸に2022年から2026年の評価額の伸び、縦軸に2026年の「収益価格 ÷ 鑑定評価額」を取ったものです。

```chart
{
  "layer": [
    {
      "data": {"name": "city_tokyo"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "city", "type": "nominal"},
          {"field": "price_pct", "type": "quantitative"},
          {"field": "share_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "price_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "鑑定評価額の伸び 2022→2026年（%）", "grid": true}
        },
        "y": {
          "field": "share_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "収益価格 ÷ 鑑定評価額 2026年（%）", "grid": true}
        },
        "color": {
          "datum": "東京23区",
          "type": "nominal",
          "scale": {
            "domain": ["東京23区", "政令指定都市", "それ以外の市町村"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "city_major"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "city", "type": "nominal"},
          {"field": "price_pct", "type": "quantitative"},
          {"field": "share_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "price_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "鑑定評価額の伸び 2022→2026年（%）", "grid": true}
        },
        "y": {
          "field": "share_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "収益価格 ÷ 鑑定評価額 2026年（%）", "grid": true}
        },
        "color": {
          "datum": "政令指定都市",
          "type": "nominal",
          "scale": {
            "domain": ["東京23区", "政令指定都市", "それ以外の市町村"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "city_other"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "city", "type": "nominal"},
          {"field": "price_pct", "type": "quantitative"},
          {"field": "share_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "price_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "鑑定評価額の伸び 2022→2026年（%）", "grid": true}
        },
        "y": {
          "field": "share_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "収益価格 ÷ 鑑定評価額 2026年（%）", "grid": true}
        },
        "color": {
          "datum": "それ以外の市町村",
          "type": "nominal",
          "scale": {
            "domain": ["東京23区", "政令指定都市", "それ以外の市町村"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

23区の21区は、図の右上にまとまっています。割合は江戸川区の75.2%から中央区の92.9%までで、評価額の伸びは足立区の22.3%から中野区の58.4%までです。政令指定都市の18市は、岡山市の62.6%から大阪市の85.7%までに並びます。

それ以外の市町村の51市は、割合が徳島市の9.7%から大津市の85.5%まで大きく散らばります。50%を下回る市は15あり、すべてこのグループです。福島市23.6%、松山市25.8%、いわき市27.5%のように、家賃で説明できる割合が評価額の3割に届かない市もあります。

## 業務でどう使えるか

- 担保の土地に近い標準地の鑑定評価書を確認すると、その周辺で収益価格が評価額のどのくらいの水準に求められているかの目安が分かります。分かるのは標準地に想定した建物の収益で、担保物件そのものの収益ではありません。政令市以外の市町村では、5年とも総収益と還元利回りがそろう標準地のうち31.8%で、収益価格が評価額の半分に届きません
- 23区の割合が9割近くを保っている理由の1つは、還元利回りが3.9%から3.2%に下がったことです。還元利回りは鑑定士が取引で受け入れられている利回りを参照して決めるので、利回りが上がる局面では、23区の収益価格は家賃が変わらなくても下がります

## データの出典

本記事は国土交通省の[地価公示](https://www.mlit.go.jp/totikensangyo/totikensangyo_fr4_000043.html)の鑑定評価書を、[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公開する鑑定評価書情報から2026年9月23日時点で集計しています。対象は2022年から2026年の各年1月1日時点の商業地で、5年とも総収益と還元利回りがそろう地点に限っています。

土地の値段がどれだけ家賃収入で裏付けられているかは、地点ごとの鑑定評価書を1通ずつ開かないと分かりません。Queriaは鑑定評価書の項目を列に展開し、単位や用途区分の説明を付けて公開しています。本記事で使った[鑑定評価書テーブル](/datasets/queria/reinfolib/main/mart_appraisal_reports)から、担保の土地に近い標準地の評価額・収益価格・利回りを5年分並べて確認できます。

```sql id=share
WITH r AS (SELECT year, prefecture_code, standard_lot_number, MAX(city_code) AS city_code, AVG(appraised_price) AS ap, AVG(NULLIF(income_gross_revenue, 0)) AS gr, AVG(NULLIF(income_capitalization_rate, 0)) AS cap, AVG(NULLIF(income_method_price, 0)) AS inc, AVG(NULLIF(comparison_method_price, 0)) AS cmp, AVG(NULLIF(income_net_revenue_land, 0)) AS nl FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year BETWEEN 2022 AND 2026 GROUP BY year, prefecture_code, standard_lot_number), bal AS (SELECT prefecture_code, standard_lot_number FROM r WHERE gr IS NOT NULL AND cap IS NOT NULL GROUP BY prefecture_code, standard_lot_number HAVING COUNT(*) = 5), p AS (SELECT r.*, FIRST_VALUE(r.ap) OVER w AS ap0, FIRST_VALUE(r.gr) OVER w AS gr0, FIRST_VALUE(r.cap) OVER w AS cap0, FIRST_VALUE(r.inc) OVER w AS inc0, FIRST_VALUE(r.nl) OVER w AS nl0 FROM r JOIN bal USING (prefecture_code, standard_lot_number) WINDOW w AS (PARTITION BY r.prefecture_code, r.standard_lot_number ORDER BY r.year)), g AS (SELECT p.*, CASE WHEN p.city_code BETWEEN '13101' AND '13123' THEN '東京23区' WHEN m.area_kind = 'ward' THEN '政令指定都市' ELSE 'その他の市町村' END AS grp, m.pref_name || ' ' || COALESCE(m.designated_city_name, m.municipality_name) AS city FROM p LEFT JOIN soumu.code.municipality m ON p.city_code = m.area_code) SELECT year, ROUND(100 * MEDIAN(inc / ap) FILTER (WHERE grp = '東京23区'), 1) AS share_tokyo, ROUND(100 * MEDIAN(inc / ap) FILTER (WHERE grp = '政令指定都市'), 1) AS share_major, ROUND(100 * MEDIAN(inc / ap) FILTER (WHERE grp = 'その他の市町村'), 1) AS share_other, ROUND(100 * MEDIAN(cmp / ap) FILTER (WHERE grp = '東京23区'), 1) AS cmp_tokyo, ROUND(100 * MEDIAN(cmp / ap) FILTER (WHERE grp = '政令指定都市'), 1) AS cmp_major, ROUND(100 * MEDIAN(cmp / ap) FILTER (WHERE grp = 'その他の市町村'), 1) AS cmp_other, ROUND(100 * AVG(CASE WHEN inc / ap < 0.5 THEN 1 ELSE 0 END) FILTER (WHERE grp = '東京23区'), 1) AS half_tokyo, ROUND(100 * AVG(CASE WHEN inc / ap < 0.5 THEN 1 ELSE 0 END) FILTER (WHERE grp = '政令指定都市'), 1) AS half_major, ROUND(100 * AVG(CASE WHEN inc / ap < 0.5 THEN 1 ELSE 0 END) FILTER (WHERE grp = 'その他の市町村'), 1) AS half_other, COUNT(*) FILTER (WHERE grp = '東京23区') AS n_tokyo, COUNT(*) FILTER (WHERE grp = '政令指定都市') AS n_major, COUNT(*) FILTER (WHERE grp = 'その他の市町村') AS n_other FROM g GROUP BY year ORDER BY year
```

```sql id=trend
WITH r AS (SELECT year, prefecture_code, standard_lot_number, MAX(city_code) AS city_code, AVG(appraised_price) AS ap, AVG(NULLIF(income_gross_revenue, 0)) AS gr, AVG(NULLIF(income_capitalization_rate, 0)) AS cap, AVG(NULLIF(income_method_price, 0)) AS inc, AVG(NULLIF(comparison_method_price, 0)) AS cmp, AVG(NULLIF(income_net_revenue_land, 0)) AS nl FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year BETWEEN 2022 AND 2026 GROUP BY year, prefecture_code, standard_lot_number), bal AS (SELECT prefecture_code, standard_lot_number FROM r WHERE gr IS NOT NULL AND cap IS NOT NULL GROUP BY prefecture_code, standard_lot_number HAVING COUNT(*) = 5), p AS (SELECT r.*, FIRST_VALUE(r.ap) OVER w AS ap0, FIRST_VALUE(r.gr) OVER w AS gr0, FIRST_VALUE(r.cap) OVER w AS cap0, FIRST_VALUE(r.inc) OVER w AS inc0, FIRST_VALUE(r.nl) OVER w AS nl0 FROM r JOIN bal USING (prefecture_code, standard_lot_number) WINDOW w AS (PARTITION BY r.prefecture_code, r.standard_lot_number ORDER BY r.year)), g AS (SELECT p.*, CASE WHEN p.city_code BETWEEN '13101' AND '13123' THEN '東京23区' WHEN m.area_kind = 'ward' THEN '政令指定都市' ELSE 'その他の市町村' END AS grp, m.pref_name || ' ' || COALESCE(m.designated_city_name, m.municipality_name) AS city FROM p LEFT JOIN soumu.code.municipality m ON p.city_code = m.area_code) SELECT year, ROUND(100 * MEDIAN(ap / ap0) FILTER (WHERE grp = '東京23区'), 1) AS price_tokyo, ROUND(100 * MEDIAN(ap / ap0) FILTER (WHERE grp = '政令指定都市'), 1) AS price_major, ROUND(100 * MEDIAN(ap / ap0) FILTER (WHERE grp = 'その他の市町村'), 1) AS price_other, ROUND(100 * MEDIAN(gr / gr0) FILTER (WHERE grp = '東京23区'), 1) AS rent_tokyo, ROUND(100 * MEDIAN(gr / gr0) FILTER (WHERE grp = '政令指定都市'), 1) AS rent_major, ROUND(100 * MEDIAN(gr / gr0) FILTER (WHERE grp = 'その他の市町村'), 1) AS rent_other, ROUND(100 * MEDIAN(nl / nl0) FILTER (WHERE grp = '東京23区'), 1) AS landnoi_tokyo, ROUND(100 * MEDIAN(nl / nl0) FILTER (WHERE grp = '政令指定都市'), 1) AS landnoi_major, ROUND(100 * MEDIAN(nl / nl0) FILTER (WHERE grp = 'その他の市町村'), 1) AS landnoi_other, MEDIAN(cap) FILTER (WHERE grp = '東京23区') AS cap_tokyo, MEDIAN(cap) FILTER (WHERE grp = '政令指定都市') AS cap_major, MEDIAN(cap) FILTER (WHERE grp = 'その他の市町村') AS cap_other FROM g GROUP BY year ORDER BY year
```

```sql id=city_tokyo
WITH r AS (SELECT year, prefecture_code, standard_lot_number, MAX(city_code) AS city_code, AVG(appraised_price) AS ap, AVG(NULLIF(income_gross_revenue, 0)) AS gr, AVG(NULLIF(income_capitalization_rate, 0)) AS cap, AVG(NULLIF(income_method_price, 0)) AS inc, AVG(NULLIF(comparison_method_price, 0)) AS cmp, AVG(NULLIF(income_net_revenue_land, 0)) AS nl FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year BETWEEN 2022 AND 2026 GROUP BY year, prefecture_code, standard_lot_number), bal AS (SELECT prefecture_code, standard_lot_number FROM r WHERE gr IS NOT NULL AND cap IS NOT NULL GROUP BY prefecture_code, standard_lot_number HAVING COUNT(*) = 5), p AS (SELECT r.*, FIRST_VALUE(r.ap) OVER w AS ap0, FIRST_VALUE(r.gr) OVER w AS gr0, FIRST_VALUE(r.cap) OVER w AS cap0, FIRST_VALUE(r.inc) OVER w AS inc0, FIRST_VALUE(r.nl) OVER w AS nl0 FROM r JOIN bal USING (prefecture_code, standard_lot_number) WINDOW w AS (PARTITION BY r.prefecture_code, r.standard_lot_number ORDER BY r.year)), g AS (SELECT p.*, CASE WHEN p.city_code BETWEEN '13101' AND '13123' THEN '東京23区' WHEN m.area_kind = 'ward' THEN '政令指定都市' ELSE 'その他の市町村' END AS grp, m.pref_name || ' ' || COALESCE(m.designated_city_name, m.municipality_name) AS city FROM p LEFT JOIN soumu.code.municipality m ON p.city_code = m.area_code) SELECT city, COUNT(*) AS lots, ROUND(100 * (MEDIAN(ap / ap0) - 1), 1) AS price_pct, ROUND(100 * MEDIAN(inc / ap), 1) AS share_pct FROM g WHERE year = 2026 AND grp = '東京23区' GROUP BY city HAVING COUNT(*) >= 15 ORDER BY share_pct, city
```

```sql id=city_major
WITH r AS (SELECT year, prefecture_code, standard_lot_number, MAX(city_code) AS city_code, AVG(appraised_price) AS ap, AVG(NULLIF(income_gross_revenue, 0)) AS gr, AVG(NULLIF(income_capitalization_rate, 0)) AS cap, AVG(NULLIF(income_method_price, 0)) AS inc, AVG(NULLIF(comparison_method_price, 0)) AS cmp, AVG(NULLIF(income_net_revenue_land, 0)) AS nl FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year BETWEEN 2022 AND 2026 GROUP BY year, prefecture_code, standard_lot_number), bal AS (SELECT prefecture_code, standard_lot_number FROM r WHERE gr IS NOT NULL AND cap IS NOT NULL GROUP BY prefecture_code, standard_lot_number HAVING COUNT(*) = 5), p AS (SELECT r.*, FIRST_VALUE(r.ap) OVER w AS ap0, FIRST_VALUE(r.gr) OVER w AS gr0, FIRST_VALUE(r.cap) OVER w AS cap0, FIRST_VALUE(r.inc) OVER w AS inc0, FIRST_VALUE(r.nl) OVER w AS nl0 FROM r JOIN bal USING (prefecture_code, standard_lot_number) WINDOW w AS (PARTITION BY r.prefecture_code, r.standard_lot_number ORDER BY r.year)), g AS (SELECT p.*, CASE WHEN p.city_code BETWEEN '13101' AND '13123' THEN '東京23区' WHEN m.area_kind = 'ward' THEN '政令指定都市' ELSE 'その他の市町村' END AS grp, m.pref_name || ' ' || COALESCE(m.designated_city_name, m.municipality_name) AS city FROM p LEFT JOIN soumu.code.municipality m ON p.city_code = m.area_code) SELECT city, COUNT(*) AS lots, ROUND(100 * (MEDIAN(ap / ap0) - 1), 1) AS price_pct, ROUND(100 * MEDIAN(inc / ap), 1) AS share_pct FROM g WHERE year = 2026 AND grp = '政令指定都市' GROUP BY city HAVING COUNT(*) >= 15 ORDER BY share_pct, city
```

```sql id=city_other
WITH r AS (SELECT year, prefecture_code, standard_lot_number, MAX(city_code) AS city_code, AVG(appraised_price) AS ap, AVG(NULLIF(income_gross_revenue, 0)) AS gr, AVG(NULLIF(income_capitalization_rate, 0)) AS cap, AVG(NULLIF(income_method_price, 0)) AS inc, AVG(NULLIF(comparison_method_price, 0)) AS cmp, AVG(NULLIF(income_net_revenue_land, 0)) AS nl FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year BETWEEN 2022 AND 2026 GROUP BY year, prefecture_code, standard_lot_number), bal AS (SELECT prefecture_code, standard_lot_number FROM r WHERE gr IS NOT NULL AND cap IS NOT NULL GROUP BY prefecture_code, standard_lot_number HAVING COUNT(*) = 5), p AS (SELECT r.*, FIRST_VALUE(r.ap) OVER w AS ap0, FIRST_VALUE(r.gr) OVER w AS gr0, FIRST_VALUE(r.cap) OVER w AS cap0, FIRST_VALUE(r.inc) OVER w AS inc0, FIRST_VALUE(r.nl) OVER w AS nl0 FROM r JOIN bal USING (prefecture_code, standard_lot_number) WINDOW w AS (PARTITION BY r.prefecture_code, r.standard_lot_number ORDER BY r.year)), g AS (SELECT p.*, CASE WHEN p.city_code BETWEEN '13101' AND '13123' THEN '東京23区' WHEN m.area_kind = 'ward' THEN '政令指定都市' ELSE 'その他の市町村' END AS grp, m.pref_name || ' ' || COALESCE(m.designated_city_name, m.municipality_name) AS city FROM p LEFT JOIN soumu.code.municipality m ON p.city_code = m.area_code) SELECT city, COUNT(*) AS lots, ROUND(100 * (MEDIAN(ap / ap0) - 1), 1) AS price_pct, ROUND(100 * MEDIAN(inc / ap), 1) AS share_pct FROM g WHERE year = 2026 AND grp = 'その他の市町村' GROUP BY city HAVING COUNT(*) >= 15 ORDER BY share_pct, city
```

```sql id=excluded
WITH r AS (SELECT prefecture_code, standard_lot_number, MAX(CASE WHEN year = 2026 THEN city_code END) AS city_code, COUNT(DISTINCT CASE WHEN income_gross_revenue > 0 AND income_capitalization_rate > 0 THEN year END) AS nyears, MAX(CASE WHEN year = 2026 AND income_method_price > 0 THEN 1 ELSE 0 END) AS inc_2026 FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year BETWEEN 2022 AND 2026 GROUP BY prefecture_code, standard_lot_number), g AS (SELECT r.*, CASE WHEN r.city_code BETWEEN '13101' AND '13123' THEN '東京23区' WHEN m.area_kind = 'ward' THEN '政令指定都市' ELSE 'その他の市町村' END AS grp FROM r LEFT JOIN soumu.code.municipality m ON r.city_code = m.area_code WHERE r.city_code IS NOT NULL) SELECT grp, COUNT(*) AS lots_2026, COUNT(*) FILTER (WHERE nyears = 5) AS in_panel, COUNT(*) FILTER (WHERE inc_2026 = 0) AS no_income_2026, ROUND(100.0 * COUNT(*) FILTER (WHERE inc_2026 = 0) / COUNT(*), 1) AS no_income_pct FROM g GROUP BY grp ORDER BY grp
```

```sql id=coverage
WITH c AS (SELECT prefecture_code, standard_lot_number FROM reinfolib.main.mart_appraisal_reports WHERE use_category = '商業地' AND year = 2026 GROUP BY prefecture_code, standard_lot_number) SELECT COUNT(*) AS lots_2026 FROM c
```
