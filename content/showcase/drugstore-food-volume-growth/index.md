---
title: ドラッグストアで売れる食品の量が増えたのは、店が増えたからだった
description: ドラッグストアの食品販売額を物価と店舗数で割ると、値上がり分を除いた1店あたりの量は2022年から2025年まで横ばいで、量の伸びの大半は店の数でした。
ogDescription: ドラッグストアの食品販売額を物価と店舗数で割ると、値上がり分を除いた1店あたりの量は2022年から2025年まで横ばいでした。
publishedAt: 2026-09-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 小売業
  - ドラッグストア
  - 物価
datasets:
  - queria/meti
  - queria/e_stat
sources:
  - title: 商業動態統計
    url: https://www.meti.go.jp/statistics/tyo/syoudou/
    publisher: 経済産業省
  - title: 消費者物価指数（CPI）
    url: https://www.stat.go.jp/data/cpi/index.html
    publisher: 総務省統計局
agentHint: ドラッグストアの商品区分ごとに、2019年から2025年の1店あたりの販売額の伸びを出して、食品と比べて
socialAnnounce: |-
  ドラッグストアの食品販売額を物価と店舗数で割ると、値上がり分を除いた1店あたりの量は2022年から2025年まで横ばいでした。

  食品メーカーの販路配分の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

ドラッグストアの食品の販売額は、2025年に2019年の1.65倍になりました。食料の物価の上昇分を除いた量では約3割の増加で、店舗数も同じ期間に16,056店から20,130店へ増え、2019年を100とした指数は125.4です。値上がり分を除いた1店あたりの量は、2022年と2025年がどちらも103.4で、量の伸びのほとんどは店の数の伸びで説明できます。

使ったのは、経済産業省の[商業動態統計](https://www.meti.go.jp/statistics/tyo/syoudou/)が公表しているドラッグストアの食品の販売額と店舗数と、総務省の[消費者物価指数](https://www.stat.go.jp/data/cpi/index.html)の食料の指数です。販売額を物価で割って値上がり分を除き、さらに店舗数で割って、伸びを値上がり・店の数・1店あたりの量に分けました。食品メーカーで販路の配分を考える担当者は、取引先の店で売れる量が増えているのか、店の数が増えているのかによって、商談の優先順位を変えることになります。

## 1店あたりの量は、2022年から横ばい

商業動態統計は、ドラッグストアの商品別の販売額と店舗数を毎月公表しています。調査の対象は、ドラッグストアを50店舗以上持つか、ドラッグストアの年間販売額が100億円以上の企業です。店舗数はその企業が持つ店の数で、業界全体の店舗数ではありません。ここでは商品区分のうち「食品」を使い、店舗数は各月末の値を年ごとに平均しました。物価は消費者物価指数（2020年＝100）の「食料」（`0002`）です。

次の図は、2019年を100として、食品の販売額、それを食料の物価で割った値（値上がり分を除いた量の目安）、店舗数、値上がり分を除いた1店あたりの量を描いたものです。ドラッグストアの統計は2019年1月の調査範囲の見直しより後には段差が無いので、2019年から描いています。

```chart
{
  "layer": [
    {
      "data": {"name": "drug_store"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"food\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#fca5a5",
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "food", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "food",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "食品の販売額",
          "type": "nominal",
          "scale": {
            "domain": ["食品の販売額", "値上がり分を除いた量", "店舗数", "1店あたりの量"],
            "range": ["#fca5a5", "#ec4899", "#22c55e", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "drug_store"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"real_food\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "real_food", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "real_food",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "値上がり分を除いた量",
          "type": "nominal",
          "scale": {
            "domain": ["食品の販売額", "値上がり分を除いた量", "店舗数", "1店あたりの量"],
            "range": ["#fca5a5", "#ec4899", "#22c55e", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "drug_store"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"stores\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "stores", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "stores",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "店舗数",
          "type": "nominal",
          "scale": {
            "domain": ["食品の販売額", "値上がり分を除いた量", "店舗数", "1店あたりの量"],
            "range": ["#fca5a5", "#ec4899", "#22c55e", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "drug_store"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"real_per_store\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "real_per_store", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "real_per_store",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "1店あたりの量",
          "type": "nominal",
          "scale": {
            "domain": ["食品の販売額", "値上がり分を除いた量", "店舗数", "1店あたりの量"],
            "range": ["#fca5a5", "#ec4899", "#22c55e", "#7c3aed"]
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

2025年の食品の販売額は2019年の1.65倍（指数165.2）ですが、同じ期間に食料の物価も127.5まで上がっているので、値上がり分を除いた量は129.6で、約3割の増加です。店舗数は16,056店から20,130店へ増え、指数は125.4でした。量の伸びのほとんどは、この店の数の伸びで説明できます。

値上がり分を除いた1店あたりの量は、新型コロナの流行が始まった2020年に106.9まで上がったあと下がり、2022年と2025年はどちらも103.4で、その間も103〜106の範囲にあります。物価には外食や酒類も含む「食料」の指数を使っているので、ドラッグストアが売る食品の値上がり幅とは一致せず、この横ばいは量の目安です。2022年から2025年に食料の物価が2割上がるあいだ、1店あたりの食品の販売額も同じだけ伸びた（指数109.5→131.8）ことになり、1つの店で売れる量は増えていません。

店舗数と販売額は調査対象の企業が持つ店の合計なので、新しく開いた店だけでなく、対象企業が他社の店を買い取った分も増加として出ます。ここで言う「店が増えた」は、新規出店と買収の両方を含みます。

## 4つの業態で、値上がり分を超えて伸びたのはドラッグストアだけ

1店あたりが横ばいでも、店の数が増えた分だけ、ドラッグストア全体で売れる食品の量は増えています。ほかの業態と比較するため、商業動態統計が食品の販売額を公表している4つの業態で、食品にあたる項目を並べます。

| 業態           | 使う項目                        | 調査の対象                                                                           |
| -------------- | ------------------------------- | ------------------------------------------------------------------------------------ |
| ドラッグストア | 食品                            | ドラッグストアを50店舗以上持つか、年間販売額が100億円以上の企業                      |
| スーパー       | 飲食料品                        | 従業者50人以上で、売場面積1,500㎡以上・売場の半分以上がセルフサービスの事業所        |
| コンビニ       | FF・日配食品 と 加工食品 の合計 | コンビニを500店舗以上持つ企業                                                        |
| 百貨店         | 飲食料品                        | 従業者50人以上で、売場面積1,500㎡以上（東京23区と政令指定都市は3,000㎡以上）の事業所 |

ここでの「スーパー」は売場面積1,500㎡以上の大型店だけで、それより小さい食品スーパーは入っていません。ネット通販や個人商店もこの4つには含まれないので、以下はこの4つの業態どうしの比較です。

次の図は、2022年1〜12月の販売額を100として、各月までの12か月間の販売額の合計を描いたものです。破線は食料の物価指数を同じく12か月で平均したものです。4つの業態の統計に調査範囲の見直しによる段差が無い期間に統一するため、2022年を起点にしています。

```chart
{
  "layer": [
    {
      "data": {"name": "rolling"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"ym\"]) && isValid(datum[\"drug\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [{"field": "ym", "type": "temporal"}, {"field": "drug", "type": "quantitative"}],
        "x": {
          "field": "ym",
          "type": "temporal",
          "axis": {"title": "12か月間の最後の月", "format": "%Y年%-m月"}
        },
        "y": {
          "field": "drug",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "ドラッグストア",
          "type": "nominal",
          "scale": {
            "domain": ["ドラッグストア", "スーパー", "コンビニ", "百貨店", "食料の物価"],
            "range": ["#ec4899", "#3b82f6", "#22c55e", "#f97316", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rolling"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"ym\"]) && isValid(datum[\"sup\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#3b82f6", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "ym", "type": "temporal"}, {"field": "sup", "type": "quantitative"}],
        "x": {
          "field": "ym",
          "type": "temporal",
          "axis": {"title": "12か月間の最後の月", "format": "%Y年%-m月"}
        },
        "y": {
          "field": "sup",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "スーパー",
          "type": "nominal",
          "scale": {
            "domain": ["ドラッグストア", "スーパー", "コンビニ", "百貨店", "食料の物価"],
            "range": ["#ec4899", "#3b82f6", "#22c55e", "#f97316", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rolling"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"ym\"]) && isValid(datum[\"cvs\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#22c55e", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "ym", "type": "temporal"}, {"field": "cvs", "type": "quantitative"}],
        "x": {
          "field": "ym",
          "type": "temporal",
          "axis": {"title": "12か月間の最後の月", "format": "%Y年%-m月"}
        },
        "y": {
          "field": "cvs",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "コンビニ",
          "type": "nominal",
          "scale": {
            "domain": ["ドラッグストア", "スーパー", "コンビニ", "百貨店", "食料の物価"],
            "range": ["#ec4899", "#3b82f6", "#22c55e", "#f97316", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rolling"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"ym\"]) && isValid(datum[\"dept\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "ym", "type": "temporal"}, {"field": "dept", "type": "quantitative"}],
        "x": {
          "field": "ym",
          "type": "temporal",
          "axis": {"title": "12か月間の最後の月", "format": "%Y年%-m月"}
        },
        "y": {
          "field": "dept",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "百貨店",
          "type": "nominal",
          "scale": {
            "domain": ["ドラッグストア", "スーパー", "コンビニ", "百貨店", "食料の物価"],
            "range": ["#ec4899", "#3b82f6", "#22c55e", "#f97316", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rolling"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"ym\"]) && isValid(datum[\"cpi\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "strokeWidth": 2,
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [{"field": "ym", "type": "temporal"}, {"field": "cpi", "type": "quantitative"}],
        "x": {
          "field": "ym",
          "type": "temporal",
          "axis": {"title": "12か月間の最後の月", "format": "%Y年%-m月"}
        },
        "y": {
          "field": "cpi",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2022年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "食料の物価",
          "type": "nominal",
          "scale": {
            "domain": ["ドラッグストア", "スーパー", "コンビニ", "百貨店", "食料の物価"],
            "range": ["#ec4899", "#3b82f6", "#22c55e", "#f97316", "#64748b"]
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

直近の12か月（2025年8月〜2026年7月）の販売額は、ドラッグストアが138.2、スーパーが114.3、コンビニが114.1、百貨店が99.9で、食料の物価は122.9でした。2023年3月以降、物価の線より上を通っているのはドラッグストアだけで、スーパーとコンビニの線は2023年1月から一度も物価の線を上回っていません。

暦年で区切り、2022年から2025年の販売額の伸びと、それを食料の物価の伸びで割った値を並べると次のとおりです。食料には外食も含まれるので、各業態が売っている品目の値上がり幅とは一致しません。割った値は量の目安として読んでください。

```chart
{
  "layer": [
    {
      "data": {"name": "growth"},
      "transform": [
        {"fold": ["nominal_pct", "real_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"nominal_pct\": \"販売額の伸び\", \"real_pct\": \"値上がり分を除いた伸び\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"nominal_pct\",\"real_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "fmt",
          "type": "nominal",
          "axis": {"title": "業態", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2022年から2025年の伸び（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["販売額の伸び", "値上がり分を除いた伸び"], "range": ["#93c5fd", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["販売額の伸び", "値上がり分を除いた伸び"]},
        "tooltip": [
          {"field": "fmt", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

この3年で食料の物価は20.4%上がりました。スーパーとコンビニの食品の販売額はどちらも13.1%伸びましたが、物価の伸びで割るとスーパーは6.1%減、コンビニは6.0%減です。百貨店は販売額が0.2%減で、値上がり分を除くと17.1%減でした。販売額が物価を上回って伸びたのはドラッグストア（34.1%増）だけで、値上がり分を除いても11.4%増えています。

2025年の食品の販売額は、スーパーが13兆6,428億円、コンビニが8兆5,811億円、ドラッグストアが3兆2,081億円、百貨店が1兆6,124億円です。ドラッグストアの食品は、百貨店の食品の約2倍の規模になっています。

## ドラッグストアの売上の3分の1は食品

次の図は、2025年のドラッグストアの商品販売額を、統計の9つの商品区分に分けたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "drug_mix"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "sales_cho", "type": "quantitative"},
          {"field": "share_pct", "type": "quantitative"},
          {"field": "item_name", "type": "nominal"}
        ],
        "x": {
          "field": "share_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2025年の商品販売額に占める割合（%）", "grid": true}
        },
        "y": {
          "field": "item_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"name": "drug_mix"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "share_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2025年の商品販売額に占める割合（%）", "grid": true}
        },
        "y": {
          "field": "item_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "text": {"field": "sales_cho"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

食品は3.21兆円で、ドラッグストアの商品販売額の34.1%を占めます。2番目の家庭用品・日用消耗品・ペット用品（13.4%）の約2.5倍、OTC医薬品（1.04兆円）の約3倍で、調剤医薬品とOTC医薬品を合わせた医薬品全体（21.4%）よりも多く売れています。健康食品は食品とは別の区分（3.1%）です。

## 販路の見直しにどう使えるか

- ドラッグストア向けの販売計画では、既存の取引先の店で売れる量が年々増えることを前提にしないほうが安全です。量が増えたのは店の数が増えたためなので、自社の商品を取り扱う店の数を増やせるかどうかで、販売量の伸びが決まります
- 取引先のチェーンが出店や買収で店を増やしている間は、その分だけ量が伸びます。月次で公表される店舗数を確認し、店の増え方が鈍った時点で、ドラッグストア向けの計画を見直せます
- 自社の業態別の出荷額を2022年から並べ、この記事の業態別の販売額の伸びと比較すると、どの業態で市場の伸びについていけていないかが分かります。値上げをした商品なら、出荷額の伸びを自社の値上げ幅で割り、値上がり分を除いた伸びと比較します

## データの出典

本記事は、経済産業省[商業動態統計](https://www.meti.go.jp/statistics/tyo/syoudou/)の業態別・商品別の月次販売額と店舗数、総務省統計局[消費者物価指数](https://www.stat.go.jp/data/cpi/index.html)（2020年基準・全国）の食料の指数を、2026年9月25日時点で集計しています。販売額は2026年7月分までを使っています。

Queriaは、業態ごとに別々の表で公表されている販売額と店舗数を1つのテーブルにまとめ、消費者物価指数も品目・地域・時点を列にして、テーブルと列の説明を付けて公開しています。本記事で使った[業態別・商品別販売額テーブル](/datasets/queria/meti/commerce/retail_sales_by_business_type_and_item)と[消費者物価指数テーブル](/datasets/queria/e_stat/cpi/price_index)から、自社の商品に近い品目の物価で割り直したり、最新の月までグラフを延ばしたりできます。

```sql id=drug_store
WITH a AS (SELECT year, SUM(CASE WHEN item_name = '食品' THEN sales_value_million_yen END) AS food, AVG(CASE WHEN item_name = '店舗数' THEN establishments END) AS stores FROM meti.commerce.retail_sales_by_business_type_and_item WHERE business_type = 'ドラッグストア' AND year BETWEEN 2019 AND 2025 GROUP BY year), p AS (SELECT year, value AS cpi FROM e_stat.cpi.price_index WHERE tab = '1' AND area = '00000' AND cat01 = '0002' AND time_name = CAST(year AS VARCHAR) || '年' AND year BETWEEN 2019 AND 2025), j AS (SELECT a.year, a.food, a.stores, p.cpi FROM a JOIN p USING (year)), b AS (SELECT * FROM j WHERE year = 2019) SELECT j.year, ROUND(j.food / b.food * 100, 1) AS food, ROUND((j.food / j.cpi) / (b.food / b.cpi) * 100, 1) AS real_food, ROUND(j.stores / b.stores * 100, 1) AS stores, ROUND((j.food / j.stores) / (b.food / b.stores) * 100, 1) AS food_per_store, ROUND((j.food / j.stores / j.cpi) / (b.food / b.stores / b.cpi) * 100, 1) AS real_per_store, ROUND(j.cpi / b.cpi * 100, 1) AS cpi, ROUND(j.stores, 0) AS stores_n FROM j, b ORDER BY j.year
```

```sql id=rolling
WITH m AS (SELECT year, month, SUM(CASE WHEN business_type = 'ドラッグストア' AND item_name = '食品' THEN sales_value_million_yen END) AS drug, SUM(CASE WHEN business_type = 'スーパー' AND item_name = '飲食料品' THEN sales_value_million_yen END) AS sup, SUM(CASE WHEN business_type = 'コンビニエンスストア' AND item_name IN ('FF・日配食品', '加工食品') THEN sales_value_million_yen END) AS cvs, SUM(CASE WHEN business_type = '百貨店' AND item_name = '飲食料品' THEN sales_value_million_yen END) AS dept FROM meti.commerce.retail_sales_by_business_type_and_item WHERE year BETWEEN 2022 AND 2026 GROUP BY year, month), p AS (SELECT year, CAST(regexp_extract(time_name, '年([0-9]+)月', 1) AS INTEGER) AS month, value AS cpi FROM e_stat.cpi.price_index WHERE tab = '1' AND area = '00000' AND cat01 = '0002' AND time_name LIKE '%月' AND year BETWEEN 2022 AND 2026), r AS (SELECT m.year, m.month, SUM(drug) OVER w AS drug, SUM(sup) OVER w AS sup, SUM(cvs) OVER w AS cvs, SUM(dept) OVER w AS dept, AVG(cpi) OVER w AS cpi, COUNT(*) OVER w AS n FROM m JOIN p ON m.year = p.year AND m.month = p.month WINDOW w AS (ORDER BY m.year, m.month ROWS BETWEEN 11 PRECEDING AND CURRENT ROW)), b AS (SELECT * FROM r WHERE year = 2022 AND month = 12) SELECT printf('%04d-%02d-01', r.year, r.month) AS ym, ROUND(r.drug / b.drug * 100, 1) AS drug, ROUND(r.sup / b.sup * 100, 1) AS sup, ROUND(r.cvs / b.cvs * 100, 1) AS cvs, ROUND(r.dept / b.dept * 100, 1) AS dept, ROUND(r.cpi / b.cpi * 100, 1) AS cpi FROM r, b WHERE r.n = 12 AND r.year * 100 + r.month <= 202607 ORDER BY r.year, r.month
```

```sql id=growth
WITH s AS (SELECT CASE WHEN business_type = 'コンビニエンスストア' THEN 'コンビニ' ELSE business_type END AS fmt, SUM(CASE WHEN year = 2022 THEN sales_value_million_yen END) AS v22, SUM(CASE WHEN year = 2025 THEN sales_value_million_yen END) AS v25 FROM meti.commerce.retail_sales_by_business_type_and_item WHERE year IN (2022, 2025) AND ((business_type = 'ドラッグストア' AND item_name = '食品') OR (business_type IN ('スーパー', '百貨店') AND item_name = '飲食料品') OR (business_type = 'コンビニエンスストア' AND item_name IN ('FF・日配食品', '加工食品'))) GROUP BY 1), p AS (SELECT MAX(CASE WHEN year = 2025 THEN value END) / MAX(CASE WHEN year = 2022 THEN value END) AS ratio FROM e_stat.cpi.price_index WHERE tab = '1' AND area = '00000' AND cat01 = '0002' AND time_name IN ('2022年', '2025年')) SELECT fmt, ROUND(v22 / 100, 0) AS sales_2022_oku, ROUND(v25 / 100, 0) AS sales_2025_oku, ROUND((v25 / v22 - 1) * 100, 1) AS nominal_pct, ROUND((v25 / v22 / p.ratio - 1) * 100, 1) AS real_pct, ROUND((p.ratio - 1) * 100, 1) AS cpi_pct FROM s, p ORDER BY real_pct DESC
```

```sql id=drug_mix
WITH d AS (SELECT item_name, SUM(sales_value_million_yen) AS v FROM meti.commerce.retail_sales_by_business_type_and_item WHERE business_type = 'ドラッグストア' AND year = 2025 AND item_name NOT IN ('商品販売額', '店舗数') GROUP BY item_name) SELECT item_name, ROUND(v / 1000000, 2) AS sales_cho, ROUND(v / SUM(v) OVER () * 100, 1) AS share_pct, CASE WHEN item_name = '食品' THEN '#ec4899' ELSE '#94a3b8' END AS color FROM d ORDER BY v DESC
```
