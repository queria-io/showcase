---
title: 企業所得は1人あたり県民所得の2割台だが、都道府県のばらつきの4〜5割を占める
description: 1人あたり県民所得を雇用者報酬・財産所得・企業所得に分けると、企業所得は構成比が22.2〜28.8%で、47都道府県のばらつきへの寄与は40.7〜50.0%でした。東京都を除いても、2011〜2021年度の11年とも寄与が構成比を上回るのは企業所得だけです。和歌山県は11年間、雇用者報酬が39〜47位、企業所得が2〜8位です。
publishedAt: 2026-03-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 経済
  - 地域格差
  - 県民所得
datasets:
  - queria/e_stat
sources:
  - title: 県民経済計算
    url: https://www.esri.cao.go.jp/jp/sna/sonota/kenmin/kenmin_top.html
    publisher: 内閣府経済社会総合研究所
  - title: 県民経済計算 利用上の注意
    url: https://www.esri.cao.go.jp/jp/sna/data/data_list/kenmin/files/contents/pdf/riyouchui.pdf
    publisher: 内閣府経済社会総合研究所
  - title: 県民経済計算推計方法ガイドライン 第二部 分配系列
    url: https://www.esri.cao.go.jp/jp/sna/data/data_list/kenmin/files/contents/pdf/guideline/guide3_220204.pdf
    publisher: 内閣府経済社会総合研究所
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 1人あたり県民所得（C122101）を雇用者報酬（C1222）・財産所得（C1223）・企業所得（C1224）の構成比で分け、自分の県の内訳と順位が2011年度から2021年度にどう変わったか出して
socialAnnounce: |-
  1人あたり県民所得の都道府県の差を内訳に分けると、企業所得は県民所得に占める割合を超えて差に寄与していました。

  東京都を除いても2011〜2021年度の11年続けてそうなるのは、企業所得だけです。
---

1人あたり県民所得のうち企業所得が占める割合は22.2〜28.8%ですが、47都道府県のばらつきの40.7〜50.0%は企業所得によるものでした。東京都を除いた46道府県でも、2011〜2021年度の11年続けて、ばらつきへの寄与が県民所得に占める割合を上回ったのは、3つの内訳のうち企業所得だけです。

1人あたり県民所得は、都道府県の豊かさを比較する数字としてよく使われます。2021年度は東京都が5,761千円で最も高く、沖縄県が2,258千円で最も低く、その差は2.55倍です。県民所得は雇用者報酬・財産所得・企業所得の3つを合計したもので、内閣府の[利用上の注意](https://www.esri.cao.go.jp/jp/sna/data/data_list/kenmin/files/contents/pdf/riyouchui.pdf)にあるとおり、個人の所得水準とは違い、企業の利潤も含みます。

## 全国の県民所得の6〜7割は雇用者報酬

使ったのは e-Stat「社会・人口統計体系」の都道府県別経済データ（`c_pref_economy`）にある、内閣府[県民経済計算](https://www.esri.cao.go.jp/jp/sna/sonota/kenmin/kenmin_top.html)の平成27年基準の系列です。県民所得（`C1221`）とその内訳の雇用者報酬（`C1222`）・財産所得（`C1223`）・企業所得（`C1224`）、1人当たり県民所得（`C122101`）がそろう2011〜2021年度の11年分です。同じテーブルにある平成17年基準・平成23年基準の系列は体系基準年が異なるので、つなげて使えません。

```sql
SELECT * FROM coverage
```

1人当たり県民所得は県民所得を総人口で割った値です。内訳も同じく総人口で割った住民1人あたりの額で、単位は千円、物価の動きを除かない名目値です。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"fold": ["emp", "prop", "ent"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"emp\": \"雇用者報酬\", \"prop\": \"財産所得\", \"ent\": \"企業所得\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"emp\",\"prop\",\"ent\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "全国の1人あたり県民所得（千円）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["雇用者報酬", "財産所得", "企業所得"],
            "range": ["#3b82f6", "#94a3b8", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "year", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

全国の1人あたり県民所得は2011年度の2,989千円から2021年度の3,330千円になり、雇用者報酬が63.3〜71.0%、企業所得が21.8〜29.8%を占めました。年ごとに大きく動くのは企業所得で、2020年度の1人あたり県民所得は前年度から201千円減りましたが、そのうち185千円が企業所得の減少です。

```sql
SELECT year AS 年度, total AS 県民所得, emp AS 雇用者報酬, prop AS 財産所得, ent AS 企業所得, emp_share AS 雇用者報酬の割合, ent_share AS 企業所得の割合 FROM national
```

## 東京都を除いても11年続けて構成比を超えるのは企業所得

47都道府県の1人あたり県民所得のばらつき（分散）は、内訳ごとの寄与に分けられます。都道府県は人口で重み付けせず、1都道府県を1つとして集計します。寄与は、その内訳と県民所得の共分散を県民所得の分散で割ったもので、雇用者報酬・財産所得・企業所得の3つを足すと100%になります。この寄与を、対象の都道府県の1人あたりの額を合計して計算した構成比（東京都を除くときは46道府県の合計）で割ると、その内訳が県民所得に占める割合と比較して、どれだけばらつきに寄与しているかが分かります。1倍なら構成比どおり、1倍より大きければ構成比を超えています。

```chart
{
  "layer": [
    {
      "data": {"name": "contrib"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ent_ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ent_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ent_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ばらつきへの寄与 ÷ 構成比", "grid": true}
        },
        "color": {
          "datum": "企業所得（47都道府県）",
          "type": "nominal",
          "scale": {
            "domain": [
              "企業所得（47都道府県）",
              "企業所得（東京都を除く46道府県）",
              "財産所得（47都道府県）",
              "財産所得（東京都を除く46道府県）",
              "雇用者報酬（47都道府県）",
              "雇用者報酬（東京都を除く46道府県）"
            ],
            "range": ["#f97316", "#f97316", "#94a3b8", "#94a3b8", "#3b82f6", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "contrib"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ent_ratio_ex_tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 3,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ent_ratio_ex_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ent_ratio_ex_tokyo",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ばらつきへの寄与 ÷ 構成比", "grid": true}
        },
        "color": {
          "datum": "企業所得（東京都を除く46道府県）",
          "type": "nominal",
          "scale": {
            "domain": [
              "企業所得（47都道府県）",
              "企業所得（東京都を除く46道府県）",
              "財産所得（47都道府県）",
              "財産所得（東京都を除く46道府県）",
              "雇用者報酬（47都道府県）",
              "雇用者報酬（東京都を除く46道府県）"
            ],
            "range": ["#f97316", "#f97316", "#94a3b8", "#94a3b8", "#3b82f6", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "contrib"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"prop_ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "prop_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "prop_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ばらつきへの寄与 ÷ 構成比", "grid": true}
        },
        "color": {
          "datum": "財産所得（47都道府県）",
          "type": "nominal",
          "scale": {
            "domain": [
              "企業所得（47都道府県）",
              "企業所得（東京都を除く46道府県）",
              "財産所得（47都道府県）",
              "財産所得（東京都を除く46道府県）",
              "雇用者報酬（47都道府県）",
              "雇用者報酬（東京都を除く46道府県）"
            ],
            "range": ["#f97316", "#f97316", "#94a3b8", "#94a3b8", "#3b82f6", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "contrib"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"prop_ratio_ex_tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 3,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "prop_ratio_ex_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "prop_ratio_ex_tokyo",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ばらつきへの寄与 ÷ 構成比", "grid": true}
        },
        "color": {
          "datum": "財産所得（東京都を除く46道府県）",
          "type": "nominal",
          "scale": {
            "domain": [
              "企業所得（47都道府県）",
              "企業所得（東京都を除く46道府県）",
              "財産所得（47都道府県）",
              "財産所得（東京都を除く46道府県）",
              "雇用者報酬（47都道府県）",
              "雇用者報酬（東京都を除く46道府県）"
            ],
            "range": ["#f97316", "#f97316", "#94a3b8", "#94a3b8", "#3b82f6", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "contrib"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"emp_ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "emp_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "emp_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ばらつきへの寄与 ÷ 構成比", "grid": true}
        },
        "color": {
          "datum": "雇用者報酬（47都道府県）",
          "type": "nominal",
          "scale": {
            "domain": [
              "企業所得（47都道府県）",
              "企業所得（東京都を除く46道府県）",
              "財産所得（47都道府県）",
              "財産所得（東京都を除く46道府県）",
              "雇用者報酬（47都道府県）",
              "雇用者報酬（東京都を除く46道府県）"
            ],
            "range": ["#f97316", "#f97316", "#94a3b8", "#94a3b8", "#3b82f6", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "contrib"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"emp_ratio_ex_tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "emp_ratio_ex_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "emp_ratio_ex_tokyo",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ばらつきへの寄与 ÷ 構成比", "grid": true}
        },
        "color": {
          "datum": "雇用者報酬（東京都を除く46道府県）",
          "type": "nominal",
          "scale": {
            "domain": [
              "企業所得（47都道府県）",
              "企業所得（東京都を除く46道府県）",
              "財産所得（47都道府県）",
              "財産所得（東京都を除く46道府県）",
              "雇用者報酬（47都道府県）",
              "雇用者報酬（東京都を除く46道府県）"
            ],
            "range": ["#f97316", "#f97316", "#94a3b8", "#94a3b8", "#3b82f6", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 1, "type": "quantitative"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

47都道府県では、企業所得の構成比は22.2〜28.8%ですが、ばらつきへの寄与は40.7〜50.0%で、構成比の1.70〜1.93倍でした。財産所得も1.65〜2.31倍で、2012年度以降は企業所得を上回ります。雇用者報酬は0.55〜0.66倍です。

分散は平均からの差を2乗して合計するので、平均から大きく離れた東京都の影響が大きく、東京都1都で47都道府県の分散の62.8〜67.3%を占めます。東京都を除いた46道府県では、ばらつきへの寄与の大きさは雇用者報酬が53.0〜67.7%で、企業所得の26.5〜41.2%より11年とも大きくなります。構成比と比較すると、企業所得は1.10〜1.48倍で、11年すべてで1倍を上回りました。2019年度は1.10倍で、1倍に近い年もあります。財産所得は0.85〜1.04倍で1倍を上回ったのは2012年度だけでした。雇用者報酬は0.80〜0.96倍で、どの年も構成比を下回ります。財産所得が構成比を大きく超えるのは、東京都を含めたときだけです。

```sql
SELECT year AS 年度, ent_share AS 企業所得の構成比, ent_contrib AS 企業所得の寄与, ent_ratio AS 企業所得の倍率, emp_contrib AS 雇用者報酬の寄与, emp_ratio AS 雇用者報酬の倍率, prop_contrib AS 財産所得の寄与, prop_ratio AS 財産所得の倍率, tokyo_var_share AS 東京都が分散に占める割合, ent_share_ex_tokyo AS 東京都を除く企業所得の構成比, ent_contrib_ex_tokyo AS 東京都を除く企業所得の寄与, ent_ratio_ex_tokyo AS 東京都を除く企業所得の倍率, emp_contrib_ex_tokyo AS 東京都を除く雇用者報酬の寄与, emp_ratio_ex_tokyo AS 東京都を除く雇用者報酬の倍率, prop_ratio_ex_tokyo AS 東京都を除く財産所得の倍率 FROM contrib
```

## 和歌山県と徳島県は企業所得、千葉県・大阪府・埼玉県は雇用者報酬で順位が高い

下の図は2021年度の47都道府県を1人あたり県民所得の高い順に並べ、内訳を積み上げたものです。

```chart
{
  "height": 880,
  "layer": [
    {
      "data": {"name": "pref"},
      "transform": [
        {"fold": ["emp", "prop", "ent"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"emp\": \"雇用者報酬\", \"prop\": \"財産所得\", \"ent\": \"企業所得\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"emp\",\"prop\",\"ent\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": null}, "sort": null},
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2021年度の1人あたり県民所得（千円）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["雇用者報酬", "財産所得", "企業所得"],
            "range": ["#3b82f6", "#94a3b8", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

11年間の順位の幅を並べると、和歌山県は雇用者報酬が39〜47位、企業所得が2〜8位で、県民所得の順位は11〜32位の間を動きました。徳島県も雇用者報酬が29〜37位、企業所得が3〜10位です。逆に千葉県は雇用者報酬が11年とも4位、企業所得は36〜46位で、大阪府（雇用者報酬5〜6位、企業所得37〜46位）と埼玉県（6〜8位、33〜41位）も同じ形です。

雇用者報酬と企業所得は、計上される都道府県の決め方が違います。推計方法の[ガイドライン](https://www.esri.cao.go.jp/jp/sna/data/data_list/kenmin/files/contents/pdf/guideline/guide3_220204.pdf)は雇用者を常時住んでいる県の居住者とみなすので、千葉県や埼玉県に住んで東京都で働く人の雇用者報酬は千葉県・埼玉県に入ります。企業所得は、県内の事業の営業余剰と混合所得に企業の財産所得の受け払いを加えたもので、法人企業と公的企業の利益のほか、農家や自営業者の所得、持ち家の取り分（帰属家賃から費用を引いた営業余剰）も含みます。ここでの住民1人あたりの雇用者報酬は総人口で割っているので、子どもや高齢者、自営業者のような雇用者でない住民も分母に入ります。内閣府が公表する「1人当たり県民雇用者報酬」は雇用者数で割った値で、別の数字です。[利用上の注意](https://www.esri.cao.go.jp/jp/sna/data/data_list/kenmin/files/contents/pdf/riyouchui.pdf)には、推計方法が都道府県ごとに同一ではないと書かれています。

```sql
SELECT area_name AS 都道府県, best_total AS 県民所得の最高順位, worst_total AS 県民所得の最低順位, best_emp AS 雇用者報酬の最高順位, worst_emp AS 雇用者報酬の最低順位, best_ent AS 企業所得の最高順位, worst_ent AS 企業所得の最低順位 FROM ranks WHERE area_name IN ('和歌山県', '徳島県', '千葉県', '大阪府', '埼玉県', '沖縄県') ORDER BY best_ent
```

## 東京都と沖縄県の差の54.1%は企業所得

最も高い東京都と最も低い沖縄県の差を、内訳に分けました。

```sql
SELECT ratio_total AS 県民所得の倍率, ratio_emp AS 雇用者報酬の倍率, ratio_ent AS 企業所得の倍率, gap_total AS 県民所得の差_千円, gap_emp AS 雇用者報酬の差_千円, gap_prop AS 財産所得の差_千円, gap_ent AS 企業所得の差_千円, gap_ent_share AS 差に占める企業所得の割合, okinawa_rank_emp AS 沖縄県の雇用者報酬の順位 FROM summary
```

2021年度の1人あたり県民所得の差は3,503千円で、内訳は雇用者報酬が1,066千円、財産所得が543千円、企業所得が1,895千円です。差の54.1%を企業所得が占め、47都道府県で見た企業所得の構成比（24.6%）の2倍を超えます。この差は、東京都がほかの道府県から大きく離れていることを反映しています。倍率で見ると、県民所得は2.55倍、雇用者報酬は1.60倍、企業所得は7.1倍でした。

沖縄県は11年とも1人あたり県民所得が47位です。2021年度の住民1人あたりの雇用者報酬は41位で、宮崎県・青森県・鳥取県・和歌山県・鹿児島県・高知県の6県を上回りますが、企業所得は47都道府県で最も低い310千円でした。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別経済データを2026年10月8日時点で集計しています。元データは内閣府経済社会総合研究所の[県民経済計算](https://www.esri.cao.go.jp/jp/sna/sonota/kenmin/kenmin_top.html)で、内訳の定義は[県民経済計算推計方法ガイドライン 第二部 分配系列](https://www.esri.cao.go.jp/jp/sna/data/data_list/kenmin/files/contents/pdf/guideline/guide3_220204.pdf)にあります。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別経済データのテーブル](/datasets/queria/e_stat/ssds/c_pref_economy)から、自分の県の1人あたり県民所得の内訳を11年分並べたり、隣の県と比較したりできます。

```sql id=national
-- 全国の1人あたり県民所得の内訳（住民1人あたり・千円）と構成比（%）
WITH d AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'C1221' THEN TRY_CAST(value AS DOUBLE) END) AS total, MAX(CASE WHEN cat01 = 'C122101' THEN TRY_CAST(value AS DOUBLE) END) AS per_capita, MAX(CASE WHEN cat01 = 'C1222' THEN TRY_CAST(value AS DOUBLE) END) AS emp, MAX(CASE WHEN cat01 = 'C1223' THEN TRY_CAST(value AS DOUBLE) END) AS prop, MAX(CASE WHEN cat01 = 'C1224' THEN TRY_CAST(value AS DOUBLE) END) AS ent FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C1221', 'C122101', 'C1222', 'C1223', 'C1224') GROUP BY year, area_name ), c AS ( SELECT year, area_name, per_capita, per_capita * emp / total AS emp_pc, per_capita * prop / total AS prop_pc, per_capita * ent / total AS ent_pc FROM d WHERE total > 0 ) SELECT year, per_capita AS total, ROUND(emp_pc) AS emp, ROUND(prop_pc) AS prop, ROUND(ent_pc) AS ent, ROUND(emp_pc / per_capita * 100, 1) AS emp_share, ROUND(ent_pc / per_capita * 100, 1) AS ent_share FROM c WHERE area_name = '全国' ORDER BY year
```

```sql id=contrib
-- 1人あたり県民所得の都道府県間の分散に対する内訳ごとの寄与（%）と、構成比に対する倍率。寄与 = 内訳と県民所得の共分散 ÷ 県民所得の分散、構成比 = 対象の都道府県の内訳の合計 ÷ 県民所得の合計
WITH d AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'C1221' THEN TRY_CAST(value AS DOUBLE) END) AS total, MAX(CASE WHEN cat01 = 'C122101' THEN TRY_CAST(value AS DOUBLE) END) AS per_capita, MAX(CASE WHEN cat01 = 'C1222' THEN TRY_CAST(value AS DOUBLE) END) AS emp, MAX(CASE WHEN cat01 = 'C1223' THEN TRY_CAST(value AS DOUBLE) END) AS prop, MAX(CASE WHEN cat01 = 'C1224' THEN TRY_CAST(value AS DOUBLE) END) AS ent FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C1221', 'C122101', 'C1222', 'C1223', 'C1224') GROUP BY year, area_name ), c AS ( SELECT year, area_name, per_capita, per_capita * emp / total AS emp_pc, per_capita * prop / total AS prop_pc, per_capita * ent / total AS ent_pc FROM d WHERE total > 0 ) , p AS ( SELECT * FROM c WHERE area_name <> '全国' ), x AS ( SELECT * FROM p WHERE area_name <> '東京都' ), a AS ( SELECT year, COVAR_POP(emp_pc, per_capita) / VAR_POP(per_capita) AS emp_c, COVAR_POP(prop_pc, per_capita) / VAR_POP(per_capita) AS prop_c, COVAR_POP(ent_pc, per_capita) / VAR_POP(per_capita) AS ent_c, SUM(ent_pc) / SUM(per_capita) AS ent_s, SUM(emp_pc) / SUM(per_capita) AS emp_s, SUM(prop_pc) / SUM(per_capita) AS prop_s FROM p GROUP BY year ), b AS ( SELECT year, COVAR_POP(emp_pc, per_capita) / VAR_POP(per_capita) AS emp_c, COVAR_POP(prop_pc, per_capita) / VAR_POP(per_capita) AS prop_c, COVAR_POP(ent_pc, per_capita) / VAR_POP(per_capita) AS ent_c, SUM(ent_pc) / SUM(per_capita) AS ent_s, SUM(emp_pc) / SUM(per_capita) AS emp_s, SUM(prop_pc) / SUM(per_capita) AS prop_s FROM x GROUP BY year ), t AS ( SELECT p.year, SUM(CASE WHEN p.area_name = '東京都' THEN POWER(p.per_capita - m.mean, 2) END) / SUM(POWER(p.per_capita - m.mean, 2)) AS tokyo_var_share FROM p JOIN ( SELECT year, AVG(per_capita) AS mean FROM p GROUP BY year ) m ON m.year = p.year GROUP BY p.year ) SELECT a.year, ROUND(a.emp_c * 100, 1) AS emp_contrib, ROUND(a.prop_c * 100, 1) AS prop_contrib, ROUND(a.ent_c * 100, 1) AS ent_contrib, ROUND(a.ent_s * 100, 1) AS ent_share, ROUND(a.ent_c / a.ent_s, 2) AS ent_ratio, ROUND(a.emp_c / a.emp_s, 2) AS emp_ratio, ROUND(a.prop_c / a.prop_s, 2) AS prop_ratio, ROUND(b.emp_c * 100, 1) AS emp_contrib_ex_tokyo, ROUND(b.ent_c * 100, 1) AS ent_contrib_ex_tokyo, ROUND(b.ent_s * 100, 1) AS ent_share_ex_tokyo, ROUND(b.ent_c / b.ent_s, 2) AS ent_ratio_ex_tokyo, ROUND(b.emp_c / b.emp_s, 2) AS emp_ratio_ex_tokyo, ROUND(b.prop_c / b.prop_s, 2) AS prop_ratio_ex_tokyo, ROUND(t.tokyo_var_share * 100, 1) AS tokyo_var_share FROM a JOIN b ON b.year = a.year JOIN t ON t.year = a.year ORDER BY a.year
```

```sql id=pref
-- 2021年度の都道府県別の内訳と順位（住民1人あたり・千円）
WITH d AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'C1221' THEN TRY_CAST(value AS DOUBLE) END) AS total, MAX(CASE WHEN cat01 = 'C122101' THEN TRY_CAST(value AS DOUBLE) END) AS per_capita, MAX(CASE WHEN cat01 = 'C1222' THEN TRY_CAST(value AS DOUBLE) END) AS emp, MAX(CASE WHEN cat01 = 'C1223' THEN TRY_CAST(value AS DOUBLE) END) AS prop, MAX(CASE WHEN cat01 = 'C1224' THEN TRY_CAST(value AS DOUBLE) END) AS ent FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C1221', 'C122101', 'C1222', 'C1223', 'C1224') GROUP BY year, area_name ), c AS ( SELECT year, area_name, per_capita, per_capita * emp / total AS emp_pc, per_capita * prop / total AS prop_pc, per_capita * ent / total AS ent_pc FROM d WHERE total > 0 ) , r AS ( SELECT area_name, per_capita, emp_pc, prop_pc, ent_pc, RANK() OVER (ORDER BY per_capita DESC) AS rank_total, RANK() OVER (ORDER BY emp_pc DESC) AS rank_emp, RANK() OVER (ORDER BY ent_pc DESC) AS rank_ent FROM c WHERE year = 2021 AND area_name <> '全国' ) SELECT area_name, per_capita AS total, ROUND(emp_pc) AS emp, ROUND(prop_pc) AS prop, ROUND(ent_pc) AS ent, ROUND(ent_pc / per_capita * 100, 1) AS ent_share, rank_total, rank_emp, rank_ent, rank_total - rank_emp AS rank_shift FROM r ORDER BY rank_total, area_name
```

```sql id=ranks
-- 2011〜2021年度の都道府県別の順位の幅
WITH d AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'C1221' THEN TRY_CAST(value AS DOUBLE) END) AS total, MAX(CASE WHEN cat01 = 'C122101' THEN TRY_CAST(value AS DOUBLE) END) AS per_capita, MAX(CASE WHEN cat01 = 'C1222' THEN TRY_CAST(value AS DOUBLE) END) AS emp, MAX(CASE WHEN cat01 = 'C1223' THEN TRY_CAST(value AS DOUBLE) END) AS prop, MAX(CASE WHEN cat01 = 'C1224' THEN TRY_CAST(value AS DOUBLE) END) AS ent FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C1221', 'C122101', 'C1222', 'C1223', 'C1224') GROUP BY year, area_name ), c AS ( SELECT year, area_name, per_capita, per_capita * emp / total AS emp_pc, per_capita * prop / total AS prop_pc, per_capita * ent / total AS ent_pc FROM d WHERE total > 0 ) , r AS ( SELECT year, area_name, RANK() OVER (PARTITION BY year ORDER BY per_capita DESC) AS rank_total, RANK() OVER (PARTITION BY year ORDER BY emp_pc DESC) AS rank_emp, RANK() OVER (PARTITION BY year ORDER BY ent_pc DESC) AS rank_ent FROM c WHERE area_name <> '全国' ) SELECT area_name, COUNT(*) AS years, MIN(rank_total) AS best_total, MAX(rank_total) AS worst_total, MIN(rank_emp) AS best_emp, MAX(rank_emp) AS worst_emp, MIN(rank_ent) AS best_ent, MAX(rank_ent) AS worst_ent FROM r GROUP BY area_name ORDER BY area_name
```

```sql id=summary
-- 2021年度の東京都と沖縄県の比較
WITH d AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'C1221' THEN TRY_CAST(value AS DOUBLE) END) AS total, MAX(CASE WHEN cat01 = 'C122101' THEN TRY_CAST(value AS DOUBLE) END) AS per_capita, MAX(CASE WHEN cat01 = 'C1222' THEN TRY_CAST(value AS DOUBLE) END) AS emp, MAX(CASE WHEN cat01 = 'C1223' THEN TRY_CAST(value AS DOUBLE) END) AS prop, MAX(CASE WHEN cat01 = 'C1224' THEN TRY_CAST(value AS DOUBLE) END) AS ent FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C1221', 'C122101', 'C1222', 'C1223', 'C1224') GROUP BY year, area_name ), c AS ( SELECT year, area_name, per_capita, per_capita * emp / total AS emp_pc, per_capita * prop / total AS prop_pc, per_capita * ent / total AS ent_pc FROM d WHERE total > 0 ) , r AS ( SELECT area_name, per_capita, emp_pc, prop_pc, ent_pc, RANK() OVER (ORDER BY per_capita DESC) AS rank_total, RANK() OVER (ORDER BY emp_pc DESC) AS rank_emp FROM c WHERE year = 2021 AND area_name <> '全国' ), t AS ( SELECT * FROM r WHERE area_name = '東京都' ), o AS ( SELECT * FROM r WHERE area_name = '沖縄県' ) SELECT (SELECT COUNT(*) FROM r WHERE rank_total <= 10 AND rank_emp <= 10) AS top10_both, (SELECT COUNT(*) FROM r WHERE ABS(rank_total - rank_emp) >= 10) AS shift10, ROUND(t.per_capita / o.per_capita, 2) AS ratio_total, ROUND(t.emp_pc / o.emp_pc, 2) AS ratio_emp, ROUND(t.ent_pc / o.ent_pc, 1) AS ratio_ent, t.per_capita - o.per_capita AS gap_total, ROUND(t.emp_pc - o.emp_pc) AS gap_emp, ROUND(t.prop_pc - o.prop_pc) AS gap_prop, ROUND(t.ent_pc - o.ent_pc) AS gap_ent, ROUND((t.ent_pc - o.ent_pc) / (t.per_capita - o.per_capita) * 100, 1) AS gap_ent_share, o.rank_emp AS okinawa_rank_emp FROM t, o
```

```sql id=coverage
-- 使った系列の収録年
SELECT cat01 AS 分類コード, item_name AS 指標, min_year AS 収録開始, max_year AS 収録最終, year_count AS 収録年数 FROM e_stat.ssds.series_coverage WHERE table_name = 'c_pref_economy' AND cat01 IN ('C1221', 'C122101', 'C1222', 'C1223', 'C1224') ORDER BY cat01
```
