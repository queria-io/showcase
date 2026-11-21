---
title: 要介護3以上の高齢者は860の市町村ですでに減っている。その8割で、10年後の85歳以上は今より多い
description: 介護保険の要介護認定者数を市町村別に2010〜2024年度で集計しました。要介護3以上は1,521市町村のうち860で最多の年度より5%以上減っており、そのうち推計のある851市町村の82.6%で、2035年の85歳以上は2025年より多くなります。
publishedAt: 2026-10-29
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 介護
  - 要介護認定
  - 将来推計人口
  - 介護施設
datasets:
  - queria/e_stat
  - queria/ipss
  - queria/nlftp
  - queria/soumu
sources:
  - title: 介護保険事業状況報告
    url: https://www.mhlw.go.jp/toukei/list/84-1.html
    publisher: 厚生労働省
  - title: 日本の地域別将来推計人口（令和5年推計）
    url: https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp
    publisher: 国立社会保障・人口問題研究所
agentHint: 要介護3〜5の認定者数が2010年度以降の最多より5%以上減った市町村を都道府県別に数えて、県内の市町村のうち何割がそうなっているかを比べて
socialAnnounce: |-
  要介護認定を市町村別に数えました。

  要介護3以上は1,521市町村の860で最多の年度より5%以上減り、うち703では2035年の85歳以上が2025年より多い推計です。
  特養の整備計画に。Queriaは行政のオープンデータを整えています
---

2010〜2024年度の数字がそろう1,521市町村のうち860市町村（56.5%）で、65歳以上の要介護3〜5の人数は、2024年度に2010年度以降の最多より5%以上少なくなっていました。全国の合計も2024年度に初めて前年度を下回りました。一方で、この860市町村のうち将来推計のある851市町村の82.6%にあたる703市町村では、2035年の85歳以上の人口が2025年より多くなる推計です。

特別養護老人ホームは原則として要介護3以上の人が入る施設なので、地域の要介護3以上（要介護3〜5）の人数は、増床や建て替えを検討するときの需要の目安になります。この記事では、厚生労働省の[介護保険事業状況報告](https://www.mhlw.go.jp/toukei/list/84-1.html)で要介護3以上の人数が減り始めた市町村を集計し、[国立社会保障・人口問題研究所（社人研）の将来推計人口](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)で、その市町村の85歳以上の人口が今後どう変わるかを確認します。

## 全国の要介護3以上は、2024年度に初めて前年度を下回った

介護保険事業状況報告は、保険者（市町村や、複数の市町村でつくる広域連合）ごとに、要介護認定を受けた人の数を年度末（翌年の3月末）時点で集計しています。Queria の[要介護認定者数のテーブル](/datasets/queria/e_stat/kaigo_insurance/certified_persons)では、認定者を次の区分で集計できます。

| 列                 | 値                                                               |
| ------------------ | ---------------------------------------------------------------- |
| `insured_category` | 総数、第1号被保険者（65歳以上）、第2号被保険者（40〜64歳）       |
| `care_level`       | 要支援1・要支援2・要介護1〜5、それに合計                         |
| `age_group`        | 第1号被保険者の年齢の内訳（5歳刻み、90歳以上）。空の行が年齢の計 |

ここでは65歳以上（第1号被保険者）を使い、要介護度を「要支援1・2」「要介護1・2」「要介護3〜5」の3つにまとめて、全国の人数を2010年度から並べます。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"heavy\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "heavy", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "heavy",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "認定者数（人）", "grid": true}
        },
        "color": {
          "datum": "要介護3〜5",
          "type": "nominal",
          "scale": {
            "domain": ["要介護3〜5", "要介護1・2", "要支援1・2"],
            "range": ["#ef4444", "#f97316", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"middle\"]) ? 0 : 1",
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
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "middle", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "middle",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "認定者数（人）", "grid": true}
        },
        "color": {
          "datum": "要介護1・2",
          "type": "nominal",
          "scale": {
            "domain": ["要介護3〜5", "要介護1・2", "要支援1・2"],
            "range": ["#ef4444", "#f97316", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"support\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "support", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "support",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "認定者数（人）", "grid": true}
        },
        "color": {
          "datum": "要支援1・2",
          "type": "nominal",
          "scale": {
            "domain": ["要介護3〜5", "要介護1・2", "要支援1・2"],
            "range": ["#ef4444", "#f97316", "#94a3b8"]
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

要介護3〜5の人は2010年度の186.4万人から増え続け、2023年度に236.1万人になりました。2024年度は235.99万人で、前年度より1,277人少なくなっています。このテーブルが持つ2002年度以降で、前年度を下回ったのは初めてです。要介護1・2と要支援1・2は2024年度も増えています。

2024年度の要介護3〜5のうち、85歳以上の人は62.1%を占めます。

## 減り始めた市町村は年々増え、2024年度には860になった

全国の合計がほぼ横ばいになる前から、市町村ごとには減少が始まっていました。単独で保険者を務め、2010〜2024年度の数字がすべてそろう1,521市町村について、要介護3〜5の人数が「その年度までの最多より5%以上少ない」市町村を年度ごとに集計しました。広域連合などで共同運営している市町村は、市町村ごとの数字が無いので含みません。

```chart
{
  "layer": [
    {
      "data": {"name": "past_count"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "below5", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "below5",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市町村数（1,521のうち）", "grid": true}
        },
        "color": {
          "datum": "最多より5%以上少ない",
          "type": "nominal",
          "scale": {"domain": ["最多より5%以上少ない", "最多より10%以上少ない"], "range": ["#fca5a5", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "past_count"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "below10", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "below10",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市町村数（1,521のうち）", "grid": true}
        },
        "color": {
          "datum": "最多より10%以上少ない",
          "type": "nominal",
          "scale": {"domain": ["最多より5%以上少ない", "最多より10%以上少ない"], "range": ["#fca5a5", "#ef4444"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2024年度には、1,521市町村のうち860（56.5%）で、要介護3〜5の人数が2010年度以降の最多より5%以上少なくなっています。10%以上少ない市町村も576あります。数は2011年度から毎年度増えていて、とくに2022年度は1年で126増えました。

減り始めた市町村は、要介護3〜5の人数が少ない町村に多くなっています。最多の年度の人数で市町村を4つに分けて集計しました。

```sql caption="要介護3〜5が最多の年度より5%以上少ない市町村（2024年度、規模別）"
SELECT * FROM by_size
```

最多の年度に500人未満だった市町村では674のうち507（75.2%）が減っていますが、2,000人以上の市では254のうち53（20.9%）です。最多の年度が100人に満たない町村では、5%は数人です。15年間の最多と比較しているので、人数の少ない町村ほど、年ごとの増減だけで「減った」に入りやすくなっています。人数で見ると、減った860市町村に住む要介護3〜5の人は54.1万人で、1,521市町村の合計224.1万人の24.1%にあたります。

人数の多い市にも、減り始めた市があります。減った市町村を、最多の年度の人数が多い順に並べました。

```sql caption="要介護3〜5が最多の年度より5%以上少ない市町村（最多の年度の人数が多い順に12）"
SELECT * FROM large_past
```

東京都大田区や静岡県浜松市のような大都市でも、要介護3〜5の人は最多の年度より5%以上少なくなっています。

市町村ごとの減少率を地図にしました。色が濃いほど、2024年度の人数が最多の年度より大きく減っています（30%以上は同じ色）。色の無い市町村は、広域連合などで共同運営しているか、2010〜2024年度の数字がそろわないところです。

```map
type: map
layers:
  - from: muni_map
    geojson: geojson
    color: decline_pct
    label: name
    name: "減少率（%）"
lng: 137.5
lat: 37.5
zoom: 4.3
```

## 860市町村では85歳以上が2022年度から減り、75〜84歳は2018年度から10.8%増えた

減り始めた860市町村を合計して、要介護3〜5の人数と、介護保険に加入している65歳以上の人（第1号被保険者）の年齢別の人数を並べました。[被保険者数のテーブル](/datasets/queria/e_stat/kaigo_insurance/insured_persons)は2018年度から85歳以上を分けて集計しているので、2018年度を100とした指数で比較します。

```chart
{
  "layer": [
    {
      "data": {"name": "past_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"heavy_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "heavy_index", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "heavy_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2018年度＝100", "grid": true}
        },
        "color": {
          "datum": "要介護3〜5の認定者",
          "type": "nominal",
          "scale": {
            "domain": ["要介護3〜5の認定者", "85歳以上の被保険者", "75〜84歳の被保険者"],
            "range": ["#ef4444", "#7c3aed", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "past_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"p85_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "p85_index", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "p85_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2018年度＝100", "grid": true}
        },
        "color": {
          "datum": "85歳以上の被保険者",
          "type": "nominal",
          "scale": {
            "domain": ["要介護3〜5の認定者", "85歳以上の被保険者", "75〜84歳の被保険者"],
            "range": ["#ef4444", "#7c3aed", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "past_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"p75_index\"]) ? 0 : 1",
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
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "p75_index", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "p75_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2018年度＝100", "grid": true}
        },
        "color": {
          "datum": "75〜84歳の被保険者",
          "type": "nominal",
          "scale": {
            "domain": ["要介護3〜5の認定者", "85歳以上の被保険者", "75〜84歳の被保険者"],
            "range": ["#ef4444", "#7c3aed", "#3b82f6"]
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

この860市町村の85歳以上は、2022年度の170.1万人を最多に、2024年度には166.3万人へ減りました。要介護3〜5の人も、2021年度の57.2万人から2024年度の54.1万人へ減っています。

要介護3以上の人数は、85歳以上の人数と同じ割合では増減しません。1,521市町村全体でも、2018年度から2024年度に85歳以上の被保険者は17.3%増えましたが、要介護3〜5の人は6.6%の増加です。

一方、860市町村の75〜84歳の人は、2018年度の283.0万人から2024年度の313.5万人へ10.8%増えています。この世代が今後85歳以上になります。

## 851市町村の85歳以上は、2035年に2025年より25.6%増える推計

社人研の[市区町村別の将来推計人口](/datasets/queria/ipss/regional_projection/population)で、同じ860市町村の85歳以上の人口の推計を集計しました。推計は2020年の国勢調査を起点に、5年ごとの10月1日時点の人口を男女・5歳階級別に出したもので、2025年以降は推計値です。市町村ごとの推計が無い福島県浜通りの9市町村を除いた851市町村を合計します。

```chart
{
  "layer": [
    {
      "data": {"name": "future_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"p85\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "p85", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "p85",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（人）", "grid": true}
        },
        "color": {
          "datum": "85歳以上",
          "type": "nominal",
          "scale": {"domain": ["85歳以上", "75〜84歳"], "range": ["#7c3aed", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "future_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"p75\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "p75", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "p75",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（人）", "grid": true}
        },
        "color": {
          "datum": "75〜84歳",
          "type": "nominal",
          "scale": {"domain": ["85歳以上", "75〜84歳"], "range": ["#7c3aed", "#3b82f6"]},
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

851市町村の85歳以上は、2025年の170.5万人から2035年に214.2万人へ、25.6%増える推計です。2040年の224.4万人まで増え、その後に減ります。いま75〜84歳の世代が、2030年代に85歳を迎えるためです。

市町村ごとに、2025年から2035年への85歳以上の増減率の分布を示します。2025年の85歳以上が0人の1村は除き、100%を超えて増える1村は右端の棒に含めています。

```chart
{
  "layer": [
    {
      "data": {"name": "future_ratio"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "x": {
          "field": "change_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "85歳以上の人口の増減（2025年→2035年、%）"},
          "bin": {"step": 5, "extent": [-40, 105]}
        },
        "y": {
          "aggregate": "count",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市町村数", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

851市町村のうち703（82.6%）で、2035年の85歳以上は2025年より多くなります。10%以上増えるのは544です。2035年に2025年より少なくなるのは145です。また、851のうち395では2030年の85歳以上が2025年より少なく、そのうち251は2035年に2025年を上回る推計です。

施設の周辺の年齢構成は、下の地図で確認できます。例として、上の表で要介護3〜5が12.2%減り、85歳以上が2035年に2025年より27.3%多くなる山口県下関市の、市役所から半径2kmの範囲の年齢構成を出しています。地図をクリックすると、その地点を中心に集計し直します。

```map
type: around
lng: 130.941459
lat: 33.957828
radius: 2000
caption: 下関市役所から半径2km
```

## 施設計画での使い方

- 定員を減らす・施設を転換する判断の前に、その市町村の要介護3以上の人数が、減り始めただけなのか、今後も減り続けるのかを確認する。減り始めた860市町村の多くでは、2035年の85歳以上が2025年より多い推計です
- 85歳以上が増えても、要介護3以上の認定を受ける人が同じ割合で増えるとは限りません。1,521市町村全体でも、2018〜2024年度に85歳以上は17.3%増え、要介護3〜5は6.6%増でした。需要の見通しは、85歳以上の人数と、そのうち要介護3以上になる人の割合の両方で立てます
- 2035年の85歳以上が2025年より少ない145市町村では、85歳以上の人数を増床の根拠にできません。定員の見直しや在宅サービスへの転換も含めて検討する地域です
- 広域で利用者を受け入れる施設では、自施設のある市町村と、利用者が住む周辺の市町村の数字を並べて確認します

## データの出典

本記事は、厚生労働省の[介護保険事業状況報告](https://www.mhlw.go.jp/toukei/list/84-1.html)（年報）の保険者別の要介護認定者数と第1号被保険者数（2010〜2024年度、各年度末現在）、および国立社会保障・人口問題研究所の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)を、2026年10月29日時点で集計しています。将来推計人口の2025年以降は推計値です。

Queria は、介護保険事業状況報告と将来推計人口を、列名・単位・地域コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[要介護認定者数](/datasets/queria/e_stat/kaigo_insurance/certified_persons)・[第1号被保険者数](/datasets/queria/e_stat/kaigo_insurance/insured_persons)・[将来推計人口](/datasets/queria/ipss/regional_projection/population)のテーブルから、自施設のある市町村や周辺の市町村の推移を確認できます。

```sql id=national
-- 全国の65歳以上（第1号被保険者）の要介護認定者数を、要介護度の3つのまとまりで数える
SELECT
  fiscal_year,
  SUM(value) FILTER (WHERE care_level IN ('要介護3', '要介護4', '要介護5')) AS heavy,
  SUM(value) FILTER (WHERE care_level IN ('要介護1', '要介護2')) AS middle,
  SUM(value) FILTER (WHERE care_level IN ('要支援1', '要支援2')) AS support
FROM e_stat.kaigo_insurance.certified_persons
WHERE insurer_kind = 'nationwide' AND insured_category = '第1号被保険者' AND age_group IS NULL
  AND fiscal_year BETWEEN 2010 AND 2024
GROUP BY fiscal_year
ORDER BY fiscal_year
```

```sql id=national_check
-- プロットはしない。2002年度以降で要介護3〜5が前年度を下回った年度と、2024年度の85歳以上の割合
WITH h AS (
  SELECT fiscal_year, SUM(value) AS heavy
  FROM e_stat.kaigo_insurance.certified_persons
  WHERE insurer_kind = 'nationwide' AND insured_category = '第1号被保険者' AND age_group IS NULL
    AND care_level IN ('要介護3', '要介護4', '要介護5') AND fiscal_year <= 2024
  GROUP BY fiscal_year
), a AS (
  SELECT
    SUM(value) FILTER (WHERE age_group IN ('85歳以上90歳未満', '90歳以上')) AS age85,
    SUM(value) FILTER (WHERE age_group IS NULL) AS total
  FROM e_stat.kaigo_insurance.certified_persons
  WHERE insurer_kind = 'nationwide' AND insured_category = '第1号被保険者' AND fiscal_year = 2024
    AND care_level IN ('要介護3', '要介護4', '要介護5')
)
SELECT
  (SELECT MIN(fiscal_year) FROM h) AS first_year,
  (SELECT string_agg(fiscal_year::VARCHAR, ',') FROM (SELECT fiscal_year, heavy - LAG(heavy) OVER (ORDER BY fiscal_year) AS diff FROM h) WHERE diff < 0) AS decline_years,
  (SELECT heavy FROM h WHERE fiscal_year = 2024) - (SELECT heavy FROM h WHERE fiscal_year = 2023) AS diff_2024,
  ROUND(100.0 * age85 / total, 1) AS age85_pct
FROM a
```

```sql id=heavy_by_muni
-- 単独で保険者を務め、2010〜2024年度の数字がすべてそろう市町村の、65歳以上の要介護3〜5の認定者数
WITH c AS (
  SELECT area_code, fiscal_year, SUM(value) AS v
  FROM e_stat.kaigo_insurance.certified_persons
  WHERE insurer_kind = 'municipality' AND area_code IS NOT NULL
    AND insured_category = '第1号被保険者' AND age_group IS NULL
    AND care_level IN ('要介護3', '要介護4', '要介護5')
    AND fiscal_year BETWEEN 2010 AND 2024
  GROUP BY area_code, fiscal_year
)
SELECT area_code, fiscal_year, v
FROM c
WHERE area_code IN (SELECT area_code FROM c GROUP BY area_code HAVING COUNT(*) = 15)
```

```sql id=peak
-- 市町村ごとの2010年度以降の最多と、その年度（同数なら早い年度）、2024年度の人数
WITH m AS (SELECT area_code, MAX(v) AS peak FROM heavy_by_muni GROUP BY area_code)
SELECT
  m.area_code,
  m.peak,
  MIN(h.fiscal_year) FILTER (WHERE h.v = m.peak) AS peak_year,
  MAX(h.v) FILTER (WHERE h.fiscal_year = 2024) AS v2024
FROM m JOIN heavy_by_muni h USING (area_code)
GROUP BY m.area_code, m.peak
```

```sql id=past_count
-- 各年度に、その年度までの最多（2010年度以降）より5%以上・10%以上少ない市町村の数
WITH r AS (
  SELECT area_code, fiscal_year, v,
    MAX(v) OVER (PARTITION BY area_code ORDER BY fiscal_year ROWS UNBOUNDED PRECEDING) AS runmax
  FROM heavy_by_muni
)
SELECT
  fiscal_year,
  COUNT(*) AS municipalities,
  COUNT(*) FILTER (WHERE v < runmax * 0.95) AS below5,
  COUNT(*) FILTER (WHERE v < runmax * 0.9) AS below10
FROM r
WHERE fiscal_year >= 2011
GROUP BY fiscal_year
ORDER BY fiscal_year
```

```sql id=by_size
-- 最多の年度の人数で4つに分け、2024年度に最多より5%以上少ない市町村を数える
SELECT
  CASE WHEN peak < 100 THEN '100人未満' WHEN peak < 500 THEN '100〜499人' WHEN peak < 2000 THEN '500〜1,999人' ELSE '2,000人以上' END AS "最多の年度の人数",
  COUNT(*) AS "市町村",
  COUNT(*) FILTER (WHERE v2024 < peak * 0.95) AS "減った市町村",
  ROUND(100.0 * COUNT(*) FILTER (WHERE v2024 < peak * 0.95) / COUNT(*), 1) AS "割合（%）"
FROM peak
GROUP BY ALL
ORDER BY MIN(peak)
```

```sql id=share
-- プロットはしない。減った市町村の数と、そこに住む要介護3〜5の人の数・割合（2024年度）
SELECT
  COUNT(*) AS municipalities,
  COUNT(*) FILTER (WHERE v2024 < peak * 0.95) AS past,
  COUNT(*) FILTER (WHERE v2024 < peak * 0.9) AS past10,
  COUNT(*) FILTER (WHERE v2024 < peak * 0.95 AND peak < 500) AS past_small,
  COUNT(*) FILTER (WHERE peak < 500) AS small,
  SUM(v2024) FILTER (WHERE v2024 < peak * 0.95) AS past_people,
  SUM(v2024) AS total_people,
  ROUND(100.0 * SUM(v2024) FILTER (WHERE v2024 < peak * 0.95) / SUM(v2024), 1) AS past_people_pct
FROM peak
```

```sql id=ipss_muni
-- 社人研の推計を、介護保険の保険者と同じ単位（市町村・政令指定都市・東京23区）でまとめる
SELECT city_code, year,
  SUM(population) FILTER (WHERE age_from >= 85) AS p85,
  SUM(population) FILTER (WHERE age_from BETWEEN 75 AND 84) AS p75
FROM ipss.regional_projection.population
WHERE area_level IN ('city', 'designated_city', 'town_village')
  OR (area_level = 'ward' AND designated_city_code IS NULL)
GROUP BY city_code, year
```

```sql id=large_past
-- 減った市町村のうち、最多の年度の人数が多い12
SELECT
  m.pref_name AS "都道府県",
  COALESCE(m.municipality_name, m.designated_city_name) AS "市町村",
  p.peak_year AS "最多の年度",
  p.peak AS "最多の年度の人数",
  p.v2024 AS "2024年度",
  ROUND(100.0 * p.v2024 / p.peak - 100, 1) AS "増減（%）",
  ROUND(100.0 * f.a35 / f.a25 - 100, 1) AS "85歳以上の増減（2025→2035年、%）"
FROM peak p
JOIN soumu.code.municipality m ON m.area_code = p.area_code
LEFT JOIN (
  SELECT city_code,
    MAX(p85) FILTER (WHERE year = 2025) AS a25,
    MAX(p85) FILTER (WHERE year = 2035) AS a35
  FROM ipss_muni GROUP BY city_code
) f ON f.city_code = p.area_code
WHERE p.v2024 < p.peak * 0.95
ORDER BY p.peak DESC, p.area_code
LIMIT 12
```

```sql id=muni_map
-- 市町村ごとの最多からの減少率。政令指定都市は市の値を各区に塗る
SELECT
  ST_AsGeoJSON(ST_SimplifyPreserveTopology(b.geometry, 0.005)) AS geojson,
  m.pref_name || COALESCE(m.designated_city_name, m.municipality_name) AS name,
  ROUND(100 - 100.0 * p.v2024 / p.peak, 1) AS decline_pct
FROM peak p
JOIN soumu.code.municipality m
  ON (m.area_code = p.area_code AND m.area_kind <> 'designated_city')
  OR (m.municipality_code = p.area_code AND m.area_kind = 'ward')
JOIN nlftp.boundary.municipality b ON b.lg_code = m.area_code
```

```sql id=all_trend
-- プロットはしない。1,521市町村全体の要介護3〜5と85歳以上の被保険者の、2018→2024年度の増加率
WITH h AS (
  SELECT SUM(v) FILTER (WHERE fiscal_year = 2018) AS h18, SUM(v) FILTER (WHERE fiscal_year = 2024) AS h24
  FROM heavy_by_muni
), i AS (
  SELECT SUM(value) FILTER (WHERE fiscal_year = 2018) AS p18, SUM(value) FILTER (WHERE fiscal_year = 2024) AS p24
  FROM e_stat.kaigo_insurance.insured_persons
  WHERE insurer_kind = 'municipality' AND category = '85歳以上'
    AND area_code IN (SELECT DISTINCT area_code FROM heavy_by_muni)
)
SELECT h18, h24, ROUND(100.0 * h24 / h18 - 100, 1) AS heavy_pct, p18, p24, ROUND(100.0 * p24 / p18 - 100, 1) AS p85_pct
FROM h, i
```

```sql id=past_trend
-- 減った市町村をまとめ、要介護3〜5の認定者と、85歳以上・75〜84歳の被保険者を2018年度＝100で比べる
WITH g AS (SELECT area_code FROM peak WHERE v2024 < peak * 0.95),
h AS (
  SELECT fiscal_year, SUM(v) AS heavy
  FROM heavy_by_muni WHERE area_code IN (SELECT area_code FROM g) AND fiscal_year >= 2018
  GROUP BY fiscal_year
),
i AS (
  SELECT fiscal_year,
    SUM(value) FILTER (WHERE category = '85歳以上') AS p85,
    SUM(value) FILTER (WHERE category = '75歳以上85歳未満') AS p75
  FROM e_stat.kaigo_insurance.insured_persons
  WHERE insurer_kind = 'municipality' AND area_code IN (SELECT area_code FROM g)
    AND fiscal_year BETWEEN 2018 AND 2024
  GROUP BY fiscal_year
)
SELECT
  h.fiscal_year, h.heavy, i.p85, i.p75,
  ROUND(100.0 * h.heavy / FIRST_VALUE(h.heavy) OVER (ORDER BY h.fiscal_year), 1) AS heavy_index,
  ROUND(100.0 * i.p85 / FIRST_VALUE(i.p85) OVER (ORDER BY h.fiscal_year), 1) AS p85_index,
  ROUND(100.0 * i.p75 / FIRST_VALUE(i.p75) OVER (ORDER BY h.fiscal_year), 1) AS p75_index
FROM h JOIN i USING (fiscal_year)
ORDER BY h.fiscal_year
```

```sql id=future_trend
-- 減った市町村のうち推計人口のある市町村の、85歳以上と75〜84歳の人口の合計
SELECT year, COUNT(*) AS municipalities, SUM(p85) AS p85, SUM(p75) AS p75
FROM ipss_muni
WHERE city_code IN (SELECT area_code FROM peak WHERE v2024 < peak * 0.95)
GROUP BY year
ORDER BY year
```

```sql id=future_ratio
-- 減った市町村ごとの、85歳以上の人口の2025年→2035年の増減率。2025年が0人の村は除き、100%を超える村は100にまとめる
SELECT city_code,
  LEAST(ROUND(100.0 * MAX(p85) FILTER (WHERE year = 2035) / MAX(p85) FILTER (WHERE year = 2025) - 100, 1), 100) AS change_pct
FROM ipss_muni
WHERE city_code IN (SELECT area_code FROM peak WHERE v2024 < peak * 0.95)
GROUP BY city_code
HAVING MAX(p85) FILTER (WHERE year = 2025) > 0
ORDER BY city_code
```

```sql id=future_counts
-- プロットはしない。85歳以上が2035年に2025年より増える・10%以上増える・減る市町村と、2030年に2025年より少ない市町村
WITH w AS (
  SELECT city_code,
    MAX(p85) FILTER (WHERE year = 2025) AS a25,
    MAX(p85) FILTER (WHERE year = 2030) AS a30,
    MAX(p85) FILTER (WHERE year = 2035) AS a35
  FROM ipss_muni
  WHERE city_code IN (SELECT area_code FROM peak WHERE v2024 < peak * 0.95)
  GROUP BY city_code
)
SELECT
  COUNT(*) AS municipalities,
  COUNT(*) FILTER (WHERE a35 > a25) AS up,
  COUNT(*) FILTER (WHERE a35 > a25 * 1.1) AS up10,
  COUNT(*) FILTER (WHERE a35 < a25) AS down,
  COUNT(*) FILTER (WHERE a30 < a25) AS dip2030,
  COUNT(*) FILTER (WHERE a30 < a25 AND a35 > a25) AS dip_then_above,
  ROUND(100.0 * COUNT(*) FILTER (WHERE a35 > a25) / COUNT(*), 1) AS up_pct
FROM w
```
