---
title: 小学校の児童数は1982年度から半減し、学校数は4分の3に、教員数は1割減った
description: 1980〜2024年度の市区町村別データで小学校を集計しました。1982年度から2024年度に児童数は49.9%、学校数は75.2%、教員数は89.5%になり、1校あたり児童数は2002年度の304.1人から下がっていません。
ogDescription: 1982年度から2024年度に、小学校の児童数は半減し、学校数は4分の3、教員数は1割減になりました。市区町村別データで集計しています。
publishedAt: 2026-07-31
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 教育
  - 学校基本調査
  - 市区町村
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系 市区町村データ
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality
    publisher: 総務省統計局
  - title: 学校基本調査
    url: https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/1267995.htm
    publisher: 文部科学省
agentHint: 小学校数(E2101)と義務教育学校数(E3901)を足した学校数を、2019年度と2024年度で市区町村別に出して、減少数の大きい順に並べて。児童数(E2501+E3905)の減少率も添えて
socialAnnounce: |-
  1980〜2024年度の市区町村別データで小学校を数え直しました。

  児童数は半減しましたが、学校数は4分の3、教員数は1割減にとどまります。学校単位で顧客を数える事業の計画に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

小学校の児童数は、1982年度の11,898,851人から2024年度の5,941,695人へ、49.9%に減りました。同じ期間に学校数は25,035校から18,819校へ75.2%に、教員数は474,893人から425,150人へ89.5%になっています。1校あたりの児童数は2002年度の304.1人から下がっておらず、2024年度は315.7人です。

学校に製品やサービスを届ける事業では、市場の大きさを何の数で見積もるかで結果が変わります。デジタル教材やドリルは児童ひとりあたりの単価で売られ、校務システムや複合機の保守は1校あたり、研修や指導者向けサービスは教員ひとりあたりで売上が決まります。少子化の話題で目にする数字はほぼ児童数なので、それを自社の市場の縮小率として使うと、事業によっては見積もりが大きく外れます。

この記事では、[社会・人口統計体系の市区町村データ](https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality)から、1980年度から2024年度までの小学校を3つの単位で集計しました。この統計は[文部科学省の学校基本調査](https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/1267995.htm)などの結果を市区町村別に組み替えたもので、全国1,741市区町村について同じ指標が1980年度から並びます。使うカテゴリは次の5つです。

| コード | 内容                       |
| ------ | -------------------------- |
| E2101  | 小学校数                   |
| E2401  | 小学校教員数               |
| E2501  | 小学校児童数               |
| E3901  | 義務教育学校数             |
| E3905  | 義務教育学校前期課程児童数 |

小学校の3つの指標（`E2101`・`E2401`・`E2501`）を、児童数が最も多かった1982年度を100として重ねました。2008年度は121市区町村の値が欠けているので、時系列のグラフからはこの年度を外しています。

## 児童数は半減、学校数は4分の3、教員数は1割減

```chart
{
  "layer": [
    {
      "data": {"name": "nation"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"idx_pupils\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#3b82f6", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "idx_pupils", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "idx_pupils",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1982年度=100", "grid": true}
        },
        "color": {
          "datum": "児童数",
          "type": "nominal",
          "scale": {"domain": ["児童数", "学校数", "教員数"], "range": ["#3b82f6", "#f97316", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "nation"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"idx_schools\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "idx_schools", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "idx_schools",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1982年度=100", "grid": true}
        },
        "color": {
          "datum": "学校数",
          "type": "nominal",
          "scale": {"domain": ["児童数", "学校数", "教員数"], "range": ["#3b82f6", "#f97316", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "nation"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"idx_teachers\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#22c55e", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "idx_teachers", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "idx_teachers",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1982年度=100", "grid": true}
        },
        "color": {
          "datum": "教員数",
          "type": "nominal",
          "scale": {"domain": ["児童数", "学校数", "教員数"], "range": ["#3b82f6", "#f97316", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

児童数は1982年度の11,898,851人から2024年度の5,941,695人へ、49.9%になりました。学校数は1982年度の25,035校から2024年度の18,819校へ、75.2%です。学校数が最も多かったのは1984年度の25,065校で、児童数が最も多かった年度の2年後です。教員数は1982年度の474,893人から2000年度の407,556人まで減ったあと増加に転じ、2024年度は425,150人です。1982年度と比較すると89.5%で、減ったのは1割です。

同じ期間でも、児童・学校・教員のどれで集計するかによって、市場の縮小は半分にも4分の3にも1割減にもなります。

## 1校あたりの児童数は、2002年度の304.1人から下がっていない

前のグラフと同じ集計から、児童数を学校数で割った「1校あたり児童数」と、児童数を教員数で割った「教員1人あたり児童数」を出しました。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "ratio"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"per_school\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "per_school", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年度", "format": "d"}
            },
            "y": {
              "field": "per_school",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "1校あたり児童数（人）", "grid": true}
            },
            "color": {
              "datum": "1校あたり児童数",
              "type": "nominal",
              "scale": {"domain": ["1校あたり児童数", "教員1人あたり児童数"], "range": ["#f97316", "#22c55e"]},
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
          "data": {"name": "ratio"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"per_teacher\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {"type": "line", "color": "#22c55e", "invalid": "break-paths-show-domains"},
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "per_teacher", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年度", "format": "d"}
            },
            "y": {
              "field": "per_teacher",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "教員1人あたり児童数（人）", "orient": "right"}
            },
            "color": {
              "datum": "教員1人あたり児童数",
              "type": "nominal",
              "scale": {"domain": ["1校あたり児童数", "教員1人あたり児童数"], "range": ["#f97316", "#22c55e"]},
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

1校あたり児童数は、1982年度の475.3人から2002年度の304.1人まで下がったあと、それ以上は下がっていません。2024年度は315.7人で、2002年度より増えています。児童数はこの間も2割近く減っており、学校数がそれと同じかそれ以上の割合で減ったためです。2000年代以降は、統廃合によって1校あたりの規模が300人前後に保たれてきました。

教員1人あたり児童数は、1982年度の25.06人から2024年度の13.98人まで下がり続けています。この教員数（`E2401`）には義務教育学校の教員は含まれないので、後で述べる義務教育学校に移行した分を加えると、教員数はもう少し多くなります。学校数は減っても、1校あたりの教員数は減っていません。教員ひとりを単位に売る事業では、児童数が半分になったこの期間の市場の縮小は1割で、2000年度以降に限れば市場は広がっています。

この300人前後という水準は全国の平均で、都道府県ごとには異なります。

## 1校あたりの児童数は、熊本県で26.4%増え、山梨県で17.8%減った

都道府県別に、2000年度と2024年度の1校あたり児童数を比較します。プラスは学校の統廃合が児童数の減少を上回った県、マイナスは統廃合が児童数の減少に追いつかず学校が小規模になった県です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "chg", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1校あたり児童数の変化率（2000年度比・%）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "chg", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1校あたり児童数の変化率（2000年度比・%）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "chg", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1校あたり児童数の変化率（2000年度比・%）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も大きく増えたのは熊本県で、1校あたり225人から284人へ26.4%増えました。児童数が21.7%減るあいだに学校数を38.1%減らしたためです。最も大きく減ったのは山梨県で、254人から209人へ17.8%減りました。児童数が33.9%減ったのに対し、学校数の減少は19.6%です。全国では横ばいの1校あたりの規模が、県ごとには26.4%増から17.8%減まで分かれています。

2番目に増えた東京都は、児童数が11.3%増えているのに、学校数は8.4%減っており、1校あたりが387人から470人へ21.5%増えました。児童が増えている地域でも学校の数は増えていないので、児童数の伸びを顧客の学校数の伸びとして扱うことはできません。

学校を減らすと1校あたりの児童は増えますが、1校が受け持つ地域の範囲も広がります。

## 1校あたりの可住地面積は、北海道が東京都の22.5倍

同じ統計の自然環境データ（`B1103` 可住地面積）を市区町村単位で結合し、2024年度の可住地面積を小学校数で割りました。人が住める土地の面積を学校の数で割った値で、1校が受け持つ範囲の広さの目安になります。可住地の中で人がどう分布しているかは考慮していないので、通学距離とは異なります。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "area_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_school_km2", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "per_school_km2",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1校あたり可住地面積（km²）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "area_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_school_km2", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "per_school_km2",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1校あたり可住地面積（km²）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "area_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_school_km2", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "per_school_km2",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1校あたり可住地面積（km²）", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
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

最も広いのは北海道の24.30km²、最も狭いのは東京都の1.08km²で、22.5倍の差があります。北海道に次ぐのは秋田県18.69km²、岩手県14.00km²と東北の県で、狭い側には大阪府1.36km²、神奈川県1.68km²と大都市圏が入ります。訪問や配送、現地での据え付けを伴うサービスでは、同じ1校でも移動にかかる負担がこれだけ違います。統廃合が進んだ県ほど1校あたりの児童は増えますが、そのぶん1校を訪問する距離は長くなります。

小学校数（`E2101`）だけで市区町村を確認すると、学校が1校もないように見える自治体があります。

## 小学校が0校の42市区町村は、すべて義務教育学校を持っている

小学校から中学校までを1つの学校として運営する義務教育学校は、学校基本調査でも小学校とは別のカテゴリ（`E3901`・`E3905`）で集計されます。このデータで義務教育学校の値が入っている最初の年度は2019年度です。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "gikyo"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "schools", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "schools",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "義務教育学校数（校）", "grid": true}
            },
            "color": {
              "datum": "義務教育学校数",
              "type": "nominal",
              "scale": {"domain": ["義務教育学校数", "前期課程児童数"], "range": ["#7c3aed", "#ec4899"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "gikyo"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pupils\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#ec4899",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 36}
          },
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "pupils", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "pupils",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "前期課程児童数（人）", "orient": "right"}
            },
            "color": {
              "datum": "前期課程児童数",
              "type": "nominal",
              "scale": {"domain": ["義務教育学校数", "前期課程児童数"], "range": ["#7c3aed", "#ec4899"]},
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

義務教育学校は2019年度の94校・27,292人から、2024年度には238校・52,760人へ増えました。5年で学校数は2.5倍です。2024年度に義務教育学校を置いている市区町村は164あります。

2024年度に小学校数が0校と記録されている市区町村は42あり、42すべてが義務教育学校を持っています。小学校数だけで一覧を作ると、この42市区町村は学校が1校もない自治体として営業対象から外れますが、実際には小学生にあたる児童が通う学校があります。学校数を集計するときは、`E2101` と `E3901` を合計する必要があります。

## 業務でどう使うか

- 事業計画で見込む市場の縮小率を、売上の単位に合わせて設定する。児童ひとりあたりで売る事業と、1校あたり・教員ひとりあたりで売る事業とでは、長期の縮小幅が違う
- 担当地域で統廃合がどこまで進んでいるかを確認する。1校あたり児童数が増えている県では顧客の学校数が減り、1校あたりの規模が大きくなる。減っている県では顧客の学校数は保たれ、1校あたりの規模が小さくなる。営業の人員の配分はこの違いで変わる
- 訪問を伴うサービスでは、1校あたりの可住地面積を移動の負担の目安にして担当エリアを決める
- 顧客の一覧を作るときは小学校と義務教育学校を合算する。市区町村を小学校数だけで絞り込むと、義務教育学校に移行した自治体が漏れる

## データの出典

本記事は e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality)から、市区町村別の教育データ（E 教育）と自然環境データ（B 自然環境）を2026年7月31日時点で集計しています。元データは[文部科学省の学校基本調査](https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/1267995.htm)などで、数値はすべて年度の値です。

Queriaは、省庁ごとに配布形式が違う統計を、列名・単位・文字コードを統一し、カテゴリコードの意味をメタデータとして付けて公開しています。本記事で使った[市区町村別の教育テーブル](/datasets/queria/e_stat/ssds/e_municipal_education)から、担当エリアの学校数と児童数の推移を取得したり、[自然環境テーブル](/datasets/queria/e_stat/ssds/b_municipal_land)と結合して1校あたりの面積を出したりできます。

```sql id=scope
SELECT COUNT(DISTINCT area) FILTER (WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%') AS municipalities, COUNT(DISTINCT area) FILTER (WHERE year = 2008 AND cat01 = 'E2101' AND TRY_CAST(value AS DOUBLE) IS NULL AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%') AS missing_2008, MIN(year) FILTER (WHERE cat01 = 'E3901') AS gikyo_from FROM e_stat.ssds.e_municipal_education
```

```sql id=nation
WITH m AS (SELECT year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.e_municipal_education WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND year <> 2008 AND year <= 2024), a AS (SELECT year, SUM(v) FILTER (WHERE cat01 = 'E2101') AS schools, SUM(v) FILTER (WHERE cat01 = 'E2501') AS pupils, SUM(v) FILTER (WHERE cat01 = 'E2401') AS teachers FROM m GROUP BY year) SELECT year, schools, pupils, teachers, ROUND(pupils / (SELECT pupils FROM a WHERE year = 1982) * 100, 1) AS idx_pupils, ROUND(schools / (SELECT schools FROM a WHERE year = 1982) * 100, 1) AS idx_schools, ROUND(teachers / (SELECT teachers FROM a WHERE year = 1982) * 100, 1) AS idx_teachers FROM a ORDER BY year
```

```sql id=ratio
WITH m AS (SELECT year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.e_municipal_education WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND year <> 2008 AND year <= 2024), a AS (SELECT year, SUM(v) FILTER (WHERE cat01 = 'E2101') AS schools, SUM(v) FILTER (WHERE cat01 = 'E2501') AS pupils, SUM(v) FILTER (WHERE cat01 = 'E2401') AS teachers FROM m GROUP BY year) SELECT year, ROUND(pupils / schools, 1) AS per_school, ROUND(pupils / teachers, 2) AS per_teacher FROM a ORDER BY year
```

```sql id=pref_top
WITH m AS (SELECT year, cat01, split_part(area_name, ' ', 1) AS pref, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.e_municipal_education WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND year IN (2000, 2024)), p AS (SELECT pref, SUM(v) FILTER (WHERE cat01 = 'E2101' AND year = 2000) AS s0, SUM(v) FILTER (WHERE cat01 = 'E2101' AND year = 2024) AS s1, SUM(v) FILTER (WHERE cat01 = 'E2501' AND year = 2000) AS p0, SUM(v) FILTER (WHERE cat01 = 'E2501' AND year = 2024) AS p1 FROM m GROUP BY pref), r AS (SELECT pref, ROUND(p0 / s0, 0) AS per00, ROUND(p1 / s1, 0) AS per24, ROUND(((p1 / s1) / (p0 / s0) - 1) * 100, 1) AS chg, ROUND((p1 / p0 - 1) * 100, 1) AS d_pupils, ROUND((s1 / s0 - 1) * 100, 1) AS d_schools, ROW_NUMBER() OVER (ORDER BY (p1 / s1) / (p0 / s0) DESC, pref) AS rn FROM p) SELECT pref, per00, per24, chg, d_pupils, d_schools FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH m AS (SELECT year, cat01, split_part(area_name, ' ', 1) AS pref, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.e_municipal_education WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND year IN (2000, 2024)), p AS (SELECT pref, SUM(v) FILTER (WHERE cat01 = 'E2101' AND year = 2000) AS s0, SUM(v) FILTER (WHERE cat01 = 'E2101' AND year = 2024) AS s1, SUM(v) FILTER (WHERE cat01 = 'E2501' AND year = 2000) AS p0, SUM(v) FILTER (WHERE cat01 = 'E2501' AND year = 2024) AS p1 FROM m GROUP BY pref), r AS (SELECT pref, ROUND(p0 / s0, 0) AS per00, ROUND(p1 / s1, 0) AS per24, ROUND(((p1 / s1) / (p0 / s0) - 1) * 100, 1) AS chg, ROUND((p1 / p0 - 1) * 100, 1) AS d_pupils, ROUND((s1 / s0 - 1) * 100, 1) AS d_schools, ROW_NUMBER() OVER (ORDER BY (p1 / s1) / (p0 / s0) DESC, pref) AS rn FROM p) SELECT pref, per00, per24, chg, d_pupils, d_schools FROM r WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH m AS (SELECT year, cat01, split_part(area_name, ' ', 1) AS pref, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.e_municipal_education WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND year IN (2000, 2024)), p AS (SELECT pref, SUM(v) FILTER (WHERE cat01 = 'E2101' AND year = 2000) AS s0, SUM(v) FILTER (WHERE cat01 = 'E2101' AND year = 2024) AS s1, SUM(v) FILTER (WHERE cat01 = 'E2501' AND year = 2000) AS p0, SUM(v) FILTER (WHERE cat01 = 'E2501' AND year = 2024) AS p1 FROM m GROUP BY pref), r AS (SELECT pref, ROUND(p0 / s0, 0) AS per00, ROUND(p1 / s1, 0) AS per24, ROUND(((p1 / s1) / (p0 / s0) - 1) * 100, 1) AS chg, ROUND((p1 / p0 - 1) * 100, 1) AS d_pupils, ROUND((s1 / s0 - 1) * 100, 1) AS d_schools, ROW_NUMBER() OVER (ORDER BY (p1 / s1) / (p0 / s0) DESC, pref) AS rn FROM p) SELECT pref, per00, per24, chg, d_pupils, d_schools FROM r WHERE rn > 37 ORDER BY rn
```

```sql id=area_top
WITH s AS (SELECT split_part(area_name, ' ', 1) AS pref, SUM(TRY_CAST(value AS DOUBLE)) AS sch FROM e_stat.ssds.e_municipal_education WHERE cat01 = 'E2101' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY 1), l AS (SELECT split_part(area_name, ' ', 1) AS pref, SUM(TRY_CAST(value AS DOUBLE)) / 100 AS km2 FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B1103' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY 1), r AS (SELECT s.pref, ROUND(l.km2 / s.sch, 2) AS per_school_km2, ROW_NUMBER() OVER (ORDER BY l.km2 / s.sch DESC, s.pref) AS rn FROM s JOIN l USING (pref)) SELECT pref, per_school_km2 FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=area_mid
WITH s AS (SELECT split_part(area_name, ' ', 1) AS pref, SUM(TRY_CAST(value AS DOUBLE)) AS sch FROM e_stat.ssds.e_municipal_education WHERE cat01 = 'E2101' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY 1), l AS (SELECT split_part(area_name, ' ', 1) AS pref, SUM(TRY_CAST(value AS DOUBLE)) / 100 AS km2 FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B1103' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY 1), r AS (SELECT s.pref, ROUND(l.km2 / s.sch, 2) AS per_school_km2, ROW_NUMBER() OVER (ORDER BY l.km2 / s.sch DESC, s.pref) AS rn FROM s JOIN l USING (pref)) SELECT pref, per_school_km2 FROM r WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=area_bottom
WITH s AS (SELECT split_part(area_name, ' ', 1) AS pref, SUM(TRY_CAST(value AS DOUBLE)) AS sch FROM e_stat.ssds.e_municipal_education WHERE cat01 = 'E2101' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY 1), l AS (SELECT split_part(area_name, ' ', 1) AS pref, SUM(TRY_CAST(value AS DOUBLE)) / 100 AS km2 FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B1103' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY 1), r AS (SELECT s.pref, ROUND(l.km2 / s.sch, 2) AS per_school_km2, ROW_NUMBER() OVER (ORDER BY l.km2 / s.sch DESC, s.pref) AS rn FROM s JOIN l USING (pref)) SELECT pref, per_school_km2 FROM r WHERE rn > 37 ORDER BY rn
```

```sql id=gikyo
WITH m AS (SELECT area, year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.e_municipal_education WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND year BETWEEN 2019 AND 2024), w AS (SELECT area, year, SUM(v) FILTER (WHERE cat01 = 'E3901') AS g, SUM(v) FILTER (WHERE cat01 = 'E3905') AS gp, SUM(v) FILTER (WHERE cat01 = 'E2101') AS s FROM m GROUP BY area, year) SELECT year, SUM(g) AS schools, SUM(gp) AS pupils, COUNT(*) FILTER (WHERE g > 0) AS munis_with, COUNT(*) FILTER (WHERE s = 0) AS munis_zero, COUNT(*) FILTER (WHERE s = 0 AND g > 0) AS munis_zero_gikyo FROM w GROUP BY year ORDER BY year
```
