---
title: 保育所に通う子どもが2023年度に27%減って見えるのは、幼保連携型認定こども園が統計の対象から外れたため
description: 2023年度から「保育所等」の統計は幼保連携型認定こども園を含みません。同じ定義で比較すると、在所児数の減少は27%ではなく3.0%です。対象から外れた割合は東京都の1.9%から福井県の60.5%まで県によって異なります。
publishedAt: 2026-03-14
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 保育所
  - 少子化
  - 子育て
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 社会福祉施設等調査
    url: https://www.mhlw.go.jp/toukei/list/23-22.html
    publisher: 厚生労働省
  - title: 保育所等関連状況取りまとめ
    url: https://www.cfa.go.jp/policies/hoiku/torimatome
    publisher: こども家庭庁
agentHint: 2022年度の保育所等在所児数のうち幼保連携型認定こども園が占める割合を都道府県別に出して。2017年度と比べて、どの県で移行が進んだかも見せて。
socialAnnounce: |-
  保育所に通う子どもが1年で27%減ったと読める統計があります。

  2023年度から幼保連携型認定こども園が調査対象外になったためです。定員計画では要確認です。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

全国の保育所等の在所児数は、2022年度の2,599,190人から2023年度の1,905,477人へ、統計上は27%減りました。2023年度から幼保連携型認定こども園が調査の対象から外れたためで、同じ定義に統一すると減少は3.0%です。対象から外れた子どもの割合は、東京都の1.9%から福井県の60.5%まで都道府県によって大きく異なります。待機児童数は2024年度に2,567人で、定員の3割近くが空いている三重県にも108人います。

この記事では、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別データを使って、保育所の定員・在所児数・待機児童数を最新年度まで集計しました。2023年度の数字を2022年度以前と同じ定義のつもりで定員計画に使うと、保育の需要が1年で4分の1以上減ったと誤って判断することになります。

## 在所児数は2021年度の2,643,196人が最も多く、2022年度は定員との差が広がった

全国の保育所等の定員数と在所児数の推移です。使っているカテゴリコードは、保育所等定員数が `J2505`、保育所等在所児数が `J2506` です。この系列は2022年度までを描いています。2023年度から調査の対象が変わり、同じ線でつなげられないためです。

```chart
{
  "layer": [
    {
      "data": {"name": "capacity"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "total",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人数（人）", "grid": true}
        },
        "color": {
          "datum": "定員数",
          "type": "nominal",
          "scale": {"domain": ["定員数", "在所児数"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "enrollment"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "total",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人数（人）", "grid": true}
        },
        "color": {
          "datum": "在所児数",
          "type": "nominal",
          "scale": {"domain": ["定員数", "在所児数"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

在所児数は1980年度の1,996,082人まで増えたあと少子化で減り続け、1994年度に1,675,877人になりました。定員も1981年度の2,168,811人から1998年度の1,914,712人まで減っています。在所児数は1995年度から増加に転じ、女性の就労の増加にともなって2000年代以降も増え続けました。国の整備による定員の拡大は、それより遅れて2000年代に入ってから始まりました。在所児数は2021年度の2,643,196人をピークに2022年度は2,599,190人へ減り、定員は2,936,183人まで伸びたため、両者の差が広がりました。

## 2023年度から「保育所等」は幼保連携型認定こども園を含まない

この統計の元データである社会福祉施設等調査は、2023年度（令和5年）から幼保連携型認定こども園を調査対象から外しました。2022年度まで「保育所等」は幼保連携型認定こども園・保育所型認定こども園・保育所の3種類を指していましたが、2023年度以降は保育所型認定こども園と保育所の2種類です。

そのため2023年度の在所児数1,905,477人をそのまま2022年度の2,599,190人と並べると、1年で27%減ったように見えます。減ったのは対象に含まれる施設の範囲で、保育を利用する子どもの数が27%減ったわけではありません。

幼保連携型認定こども園の在所児数は `J2545` という別のカテゴリコードで2022年度まで収録されています。これを `J2506` から差し引くと、2017年度以降を2023年度と同じ定義に統一できます。

```chart
{
  "layer": [
    {
      "data": {"name": "enrollment_basis"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"published\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "published", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "published",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "在所児数（人）", "grid": true}
        },
        "color": {
          "datum": "公表系列（幼保連携型を含む）",
          "type": "nominal",
          "scale": {
            "domain": ["公表系列（幼保連携型を含む）", "幼保連携型を除いてそろえた系列"],
            "range": ["#94a3b8", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "enrollment_basis"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"comparable\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "comparable", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "comparable",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "在所児数（人）", "grid": true}
        },
        "color": {
          "datum": "幼保連携型を除いてそろえた系列",
          "type": "nominal",
          "scale": {
            "domain": ["公表系列（幼保連携型を含む）", "幼保連携型を除いてそろえた系列"],
            "range": ["#94a3b8", "#f97316"]
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

同じ定義に統一した系列では、2022年度の1,964,131人から2023年度の1,905,477人へ3.0%の減少です。公表系列が2021年度まで増え続けていたのは、幼保連携型認定こども園に移った子どもを含んでいたためで、保育所と保育所型認定こども園だけでは2018年度の2,102,400人から毎年減っています。この減少には保育所が幼保連携型認定こども園に移行した分も含まれるので、子どもの数の減少とは一致しません。

## 対象から外れた子どもの割合は、福井県60.5%、東京都1.9%

2023年度の数字が2022年度以前とどれだけ異なるかは、その県で幼保連携型認定こども園がどれだけ広がっていたかで決まります。2022年度の在所児数のうち幼保連携型認定こども園が占めていた割合を都道府県別に並べました。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "yohoren_share"},
      "mark": {"type": "bar", "color": "#8b5cf6"},
      "encoding": {
        "tooltip": [
          {"field": "share_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "share_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "在所児数に占める幼保連携型の割合（2022年度、%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

福井県が60.5%、青森県が55.9%、富山県が52.7%、石川県が51.4%と、この4県では在所児数の半分以上が幼保連携型認定こども園でした。反対に東京都は1.9%、福岡県は5.9%、神奈川県は8.1%、埼玉県は9.0%にとどまります。2023年度の数字は、東京都ではほぼ従来どおりの範囲を、福井県では従来の4割弱の範囲を集計しています。

## 2023年度の定員充足率は島根県94.6%から山梨県66.4%まで

定員に対して実際に何人が利用しているかを示す「定員充足率（在所児数÷定員数×100）」で都道府県を比較しました。充足率が低い都道府県ほど、定員に余裕があります。幼保連携型認定こども園への移行が進んだ県では、移行せずに残った保育所だけの充足率になるので、この順位は保育需要の強さの順位ではなく、2022年度以前の充足率とも直接は比較できません。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "utilization"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "utilization_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "utilization_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "定員充足率（2023年度、%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

島根県が94.6%、神奈川県が93.3%、京都府が92.1%、熊本県が91.8%と高く、定員にほとんど余裕がありません。山梨県は66.4%、高知県は66.6%、三重県は71.2%、長野県は71.6%で、定員の3割前後が空いています。

## 待機児童数は2017年度の26,081人から2024年度の2,567人に減った

待機児童数（`J250502`）は、定員・在所児数とは元データが異なります。こども家庭庁の保育所等関連状況取りまとめが元データで、社会福祉施設等調査の対象変更の影響を受けないので、2024年度まで同じ定義で比較できます。

```chart
{
  "layer": [
    {
      "data": {"name": "waiting_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"waiting_children\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "waiting_children", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "waiting_children",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "待機児童数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2003, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 10,
        "color": "#94a3b8"
      },
      "encoding": {
        "x": {"datum": 2003, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "最多（2003年度）"}
      }
    }
  ]
}
```

2017年度に26,081人だった待機児童数は、保育所の整備が進んで急減しました。2022年度は2,944人、2023年度は2,680人、2024年度は2,567人で、減り方は年々小さくなっています。

## 2024年度の待機児童は東京都・沖縄県・滋賀県で多く、滋賀県は2年で3倍になった

2024年度の待機児童数を都道府県別に並べました。待機児童数が1人以上の都道府県だけを表示しています。

```chart
{
  "height": 430,
  "layer": [
    {
      "data": {"name": "waiting_pref"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "waiting_children", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "waiting_children",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "待機児童数（2024年度、人）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

東京都361人、沖縄県356人、滋賀県353人、兵庫県256人、埼玉県241人が上位です。全国が減るなかで滋賀県は2022年度の118人から2年で3倍に増えました。

充足率が高い県ほど待機児童が多い、という関係にはなっていません。三重県は充足率が下から3番目の71.2%ですが、待機児童は108人います。申し込みと定員の空きは市区町村ごと・年齢ごとに一致する必要があり、都道府県の合計では空きがあっても、特定の市区町村や年齢では定員が足りないためと考えられます。

## まとめ

- 2023年度から「保育所等」は幼保連携型認定こども園を含まない。在所児数1,905,477人を2022年度の2,599,190人と並べると27%減に見えるが、対象の範囲が変わったことによる
- 同じ定義に統一すると2022年度1,964,131人から2023年度1,905,477人で3.0%の減少。公表系列が2021年度まで増えていたのは幼保連携型認定こども園への移行分を含んでいたため
- 対象から外れた割合は東京都1.9%、福井県60.5%と県で大きく異なる。2023年度の県間比較は、県ごとに異なる範囲の施設を比較している
- 定員充足率は島根県94.6%から山梨県66.4%まで差がある。待機児童は別調査で2024年度2,567人が残り、充足率が下から3番目の三重県にも108人いる

少子化にともない、定員が余る地域が出てきています。2023年度以降の数字を前年度と比較するときは、その差が利用者の変化によるものか、統計の対象の変化によるものかを分けて確認する必要があります。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別福祉データ（`j_pref_welfare`）を 2026-08-04 時点で集計しています。定員数（`J2505`）・在所児数（`J2506`）・幼保連携型認定こども園在所児数（`J2545`）の元データは厚生労働省の[社会福祉施設等調査](https://www.mhlw.go.jp/toukei/list/23-22.html)、待機児童数（`J250502`）はこども家庭庁の[保育所等関連状況取りまとめ](https://www.cfa.go.jp/policies/hoiku/torimatome)で、数値はいずれも年度の値です。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の福祉・保育データ](/datasets/queria/e_stat/ssds/j_pref_welfare)から、自分の都道府県の定員充足率や、対象変更でどれだけの子どもが統計から外れたかを確認できます。

```sql id=capacity
SELECT year, value AS total FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J2505' AND area_name = '全国' AND value IS NOT NULL AND year <= 2022 ORDER BY year
```

```sql id=enrollment
SELECT year, value AS total FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J2506' AND area_name = '全国' AND value IS NOT NULL AND year <= 2022 ORDER BY year
```

```sql id=enrollment_basis
SELECT year, CASE WHEN year <= 2022 THEN MAX(CASE WHEN cat01 = 'J2506' THEN value END) END AS published, MAX(CASE WHEN cat01 = 'J2506' THEN value END) - COALESCE(MAX(CASE WHEN cat01 = 'J2545' THEN value END), 0) AS comparable FROM e_stat.ssds.j_pref_welfare WHERE area_name = '全国' AND cat01 IN ('J2506', 'J2545') AND year >= 2017 GROUP BY year ORDER BY year
```

```sql id=yohoren_share
SELECT area_name, ROUND(MAX(CASE WHEN cat01 = 'J2545' THEN value END) / MAX(CASE WHEN cat01 = 'J2506' THEN value END) * 100, 1) AS share_pct FROM e_stat.ssds.j_pref_welfare WHERE area_name != '全国' AND cat01 IN ('J2506', 'J2545') AND time_name = '2022年度' GROUP BY area_name ORDER BY share_pct DESC, area_name
```

```sql id=utilization
WITH capacity AS ( SELECT area_name, value AS cap FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J2505' AND area_name != '全国' AND value IS NOT NULL AND time_name = '2023年度' ), enrollment AS ( SELECT area_name, value AS enrolled FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J2506' AND area_name != '全国' AND value IS NOT NULL AND time_name = '2023年度' ) SELECT c.area_name, ROUND(e.enrolled / c.cap * 100, 1) AS utilization_rate FROM capacity c JOIN enrollment e ON c.area_name = e.area_name WHERE c.cap > 0 ORDER BY utilization_rate DESC, c.area_name
```

```sql id=waiting_trend
SELECT year, value AS waiting_children FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J250502' AND area_name = '全国' AND value IS NOT NULL ORDER BY year
```

```sql id=waiting_pref
WITH y AS ( SELECT area_name, MAX(CASE WHEN time_name = '2024年度' THEN value END) AS w2024, MAX(CASE WHEN time_name = '2022年度' THEN value END) AS w2022 FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J250502' AND area_name != '全国' AND time_name IN ('2022年度', '2024年度') GROUP BY area_name ) SELECT area_name, w2024 AS waiting_children, w2022 AS waiting_2022 FROM y WHERE w2024 > 0 ORDER BY waiting_children DESC, area_name
```
