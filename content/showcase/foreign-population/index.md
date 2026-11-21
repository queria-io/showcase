---
title: 外国人以外の人口が減った1,475市区町村のうち、外国人の増加で総人口が増えたのは55
description: 2015年から2020年に外国人以外の人口が減った市区町村は1,475。外国人の増加で総人口が増えたのは55にとどまり、外国人が増えた1,301市区町村でも埋まったのは減少分の中央値5.2%でした
publishedAt: 2026-02-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口
  - 外国人
  - 市区町村
datasets:
  - queria/e_stat
  - queria/soumu
sources:
  - title: 統計でみる都道府県・市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 令和2年国勢調査 人口等基本集計
    url: https://www.stat.go.jp/data/kokusei/2020/kekka.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義 Ａ 人口・世帯
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/A
    publisher: 総務省統計局
agentHint: a_municipal_population の A1101 と A1700 から、2015年と2020年の外国人以外の人口（総人口−外国人人口）を出して。対象は soumu.code.municipality の is_municipality で市区町村1,741件に絞って。外国人以外が減ったのに総人口が増えた自治体を、外国人の増加数が減少をどれだけ上回ったか順に並べて
socialAnnounce: |-
  「外国人の増加が人口減少を補っている」を市区町村単位で数えました。

  2015年から2020年に外国人以外が減ったのは1,475市区町村。外国人の増加で総人口が増えたのは55だけでした。
  Queriaは行政のオープンデータを整えて公開しています。
---

2015年から2020年に外国人以外の人口が減った市区町村は1,475ありました。そのうち、外国人の増加が減少を上回り、総人口が増えたのは55です。外国人が増えた1,301市区町村でも、外国人の増加が外国人以外の減少を埋めた割合は中央値で5.2%でした。外国人以外が100人減った町で、外国人が5人増えた規模です。

人口が減る町を外国人の増加が支えている、という説明をよく見かけます。そうした町の数は、市区町村ごとの数字を並べると集計できます。e-Stat の「[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)」には、市区町村ごとの総人口と外国人人口が同じテーブルに入っているので、それぞれの増減を計算できます。

## 全国の外国人人口は、40年で3.6倍になった

全国の外国人人口です。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"foreign_pop\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#7c3aed"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "foreign_pop", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "foreign_pop",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人人口（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1980年の66万8,675人から2020年の240万2,460人まで、40年で3.6倍になりました。国勢調査をもとにした系列なので5年ごとの値で、2020年までが入っています。

## 外国人の増加が埋めたのは、外国人以外の減少の28.3%

総人口には外国人が含まれるので、総人口と外国人人口を並べても、外国人がどれだけ人口を支えているかは分かりません。そこで外国人と、外国人を除いた人口を分けて、2010年をそれぞれ100とした指数で並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "national_index"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"other_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "other_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "other_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2010年=100）", "grid": true}
        },
        "color": {
          "datum": "外国人以外",
          "type": "nominal",
          "scale": {"domain": ["外国人以外", "外国人"], "range": ["#2563eb", "#7c3aed"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national_index"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"foreign_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "foreign_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "foreign_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2010年=100）", "grid": true}
        },
        "color": {
          "datum": "外国人",
          "type": "nominal",
          "scale": {"domain": ["外国人以外", "外国人"], "range": ["#2563eb", "#7c3aed"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 100, "type": "quantitative"}
      }
    }
  ]
}
```

外国人以外の人口は2010年の1億2,640万9,315人が最も多く、2020年は1億2,374万3,639人で、指数は97.9に下がりました。同じ10年で、外国人は164万8,037人から240万2,460人に増え、指数は145.8です。減った266万5,676人に対して増えたのは75万4,423人で、全国では外国人の増加が埋めたのは減少分の28.3%です。

ここでの「外国人以外」は、日本人と、国籍が判明していない人の合計です。国勢調査は国籍を回答しなかった人を国籍不詳として別に集計しており、その人数は年々増えています。

```sql
SELECT * FROM nationality_composition
```

2020年の国籍不詳は220万2,484人で、総人口の1.75%です。2015年の0.83%から倍増しました。国籍不詳が増えると「外国人以外」の人数がその分だけ多くなるので、以下で集計する外国人以外の減少幅は実際より小さくなります。そのため、この記事の55という数は下限です。

## 外国人比率が最も高いのは群馬県大泉町の17.6%

2020年の外国人比率（外国人人口 / 総人口）が高い市区町村です。総人口が少ないと数十人の増減で比率が大きく動くので、総人口1万人以上の市区町村に絞っています。政令指定都市は市全体で1件とし、行政区は除いています。東京23区は各区を1件としています。区と市を同じ表に入れると、同じ人口が市と区で二重に数えられるためです。市区町村かどうかは `soumu.code.municipality` の `is_municipality` で判定し、1,741件に絞りました。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "ratio_ranking"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "foreign_ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "foreign_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "外国人比率（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": ""}, "sort": null}
      }
    }
  ]
}
```

群馬県大泉町の17.6%が特に高く、2位の東京都豊島区と3位の埼玉県蕨市はどちらも8.5%で、大泉町の半分以下です。岐阜県美濃加茂市8.2%、茨城県常総市7.8%、東京都新宿区7.8%が続きます。東京の都心部と、北関東・東海の製造業が集まる市町が交互に並んでいます。

## 大泉町・常総市・美濃加茂市は1990年代に急に上がり、豊島区と蕨市は上がり続けている

上位の5つの市区町について、外国人比率を1980年から並べました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "city_ratio_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ohizumi\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ohizumi", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "ohizumi",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人比率（%）", "grid": true}
        },
        "color": {
          "datum": "群馬県大泉町",
          "type": "nominal",
          "scale": {
            "domain": ["群馬県大泉町", "東京都豊島区", "埼玉県蕨市", "岐阜県美濃加茂市", "茨城県常総市"],
            "range": ["#7c3aed", "#2563eb", "#22c55e", "#ef4444", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "city_ratio_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"toshima\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "toshima", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "toshima",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人比率（%）", "grid": true}
        },
        "color": {
          "datum": "東京都豊島区",
          "type": "nominal",
          "scale": {
            "domain": ["群馬県大泉町", "東京都豊島区", "埼玉県蕨市", "岐阜県美濃加茂市", "茨城県常総市"],
            "range": ["#7c3aed", "#2563eb", "#22c55e", "#ef4444", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "city_ratio_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"warabi\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "warabi", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "warabi",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人比率（%）", "grid": true}
        },
        "color": {
          "datum": "埼玉県蕨市",
          "type": "nominal",
          "scale": {
            "domain": ["群馬県大泉町", "東京都豊島区", "埼玉県蕨市", "岐阜県美濃加茂市", "茨城県常総市"],
            "range": ["#7c3aed", "#2563eb", "#22c55e", "#ef4444", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "city_ratio_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"minokamo\"]) ? 0 : 1",
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
          {"field": "minokamo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "minokamo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人比率（%）", "grid": true}
        },
        "color": {
          "datum": "岐阜県美濃加茂市",
          "type": "nominal",
          "scale": {
            "domain": ["群馬県大泉町", "東京都豊島区", "埼玉県蕨市", "岐阜県美濃加茂市", "茨城県常総市"],
            "range": ["#7c3aed", "#2563eb", "#22c55e", "#ef4444", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "city_ratio_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"joso\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f59e0b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "joso", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "joso",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人比率（%）", "grid": true}
        },
        "color": {
          "datum": "茨城県常総市",
          "type": "nominal",
          "scale": {
            "domain": ["群馬県大泉町", "東京都豊島区", "埼玉県蕨市", "岐阜県美濃加茂市", "茨城県常総市"],
            "range": ["#7c3aed", "#2563eb", "#22c55e", "#ef4444", "#f59e0b"]
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

上位の市区町でも、比率の上がり方は2種類あります。大泉町と常総市は1990年から1995年にかけて大きく上がり、大泉町は2.65%から7.81%へ、常総市は0.42%から1.82%へ上がりました。美濃加茂市はその次の5年で、1995年の1.86%から2000年の5.70%に上がっています。その後は3市町とも一度比率が下がり、大泉町は2005年の14.65%から2010年に12.97%、美濃加茂市は2010年の7.65%から2015年に6.40%、常総市は2005年の4.62%から2015年に3.72%になりました。製造業の雇用に合わせて増減していると考えられます。

豊島区と蕨市は、1980年の0.98%・0.38%から2020年の8.48%・8.47%まで上がり続けています。蕨市は9時点のあいだ一度も前回を下回っていません。豊島区も、2000年に3.60%から3.48%へ下がった1回を除けば上がり続けています。

## 外国人の増加数の上位20市区のうち18は、外国人以外の人口も増えている

2015年から2020年の外国人人口の増加数を市区町村ごとに並べます。2015年時点で外国人が100人以上いた市区町村に絞っています。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "increase_ranking"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "foreign_inc", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "foreign_inc",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "外国人人口の増加数（人）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": ""}, "sort": null}
      }
    }
  ]
}
```

最も多いのは大阪市の4万2,018人で、横浜市・川崎市・名古屋市と大都市が続きます。この20市区のうち18では、外国人以外の人口も同じ5年間で増えています。これらの都市では、人が集まる中で外国人も増えたと考えられます。

外国人以外の人口が減ったのは2市です。千葉市は外国人が6,636人増え、外国人以外が3,567人減ったので、総人口は増えました。浜松市は外国人が5,929人増えましたが、外国人以外が1万3,191人減ったので、総人口は減りました。

## 外国人以外が減った1,475市区町村のうち、総人口が増えたのは55

外国人以外の人口が減った市区町村を、外国人の増加が減少を上回ったかどうかで分けました。

```sql
SELECT * FROM offset_summary
```

市区町村1,741のうち、外国人以外が減ったのは1,475（84.7%）です。そのうち1,301では外国人が増えていますが、増加が減少を上回って総人口が増えたのは55です。外国人が増えた1,301市区町村で、外国人の増加が外国人以外の減少を埋めた割合は、中央値で5.2%です。

55市区町村のうち、総人口の増加数が大きい15件です。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "offset_towns"},
      "transform": [
        {"fold": ["other_inc", "foreign_inc"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"other_inc\": \"外国人以外\", \"foreign_inc\": \"外国人\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"other_inc\",\"foreign_inc\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": ""}, "sort": null},
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2015年から2020年の増減（人）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["外国人以外", "外国人"], "range": ["#94a3b8", "#7c3aed"]},
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

最も大きいのは群馬県太田市で、外国人以外が440人減り、外国人が3,647人増えて、総人口は3,207人増えました。群馬県伊勢崎市は外国人以外の減少が30人で、3,066人の外国人の増加がほぼそのまま総人口の増加になっています。埼玉県蕨市は532人減に対して2,555人増、静岡県菊川市は260人減に対して1,286人増です。

千葉市と八王子市は外国人以外の減少がそれぞれ3,567人・1,579人と大きく、外国人の増加（6,636人・3,421人）がそれを上回りました。この15件には、外国人比率が高い市町が多く入っています。大泉町・蕨市・可児市・碧南市・菊川市は、外国人比率の上位20にも入っています。すでに外国人が多い町ほど、人口の維持を外国人の増加に頼っていると考えられます。

## まとめ

- 全国の外国人人口は、1980年の66万8,675人から2020年の240万2,460人へ3.6倍になった
- 外国人以外の人口は2010年が最も多く、2020年までに266万5,676人減った。同じ10年の外国人の増加（75万4,423人）は、その28.3%にあたる
- 市区町村1,741のうち、外国人以外が減ったのは1,475。外国人の増加で総人口が増えたのは55
- 外国人が増えた1,301市区町村で、外国人以外の減少を埋めた割合は中央値で5.2%
- 外国人の増加数の上位20市区のうち18は、外国人以外の人口も増えている

外国人の増加で人口の減少を補えている町は、外国人比率がすでに高い一部の市町に限られています。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)の都道府県データ（`a_pref_population`）と市区町村データ（`a_municipal_population`）を2026年8月26日時点で集計しています。使ったのは `A1101_総人口`・`A1102_日本人人口`・`A1700_外国人人口` の3指標で、いずれも元は総務省統計局の[国勢調査](https://www.stat.go.jp/data/kokusei/2020/kekka.html)です。定義は e-Stat の[項目定義 Ａ 人口・世帯](https://www.e-stat.go.jp/koumoku/koumoku_teigi/A)によります。市区町村の外国人人口は1980年から2020年まで5年ごとの値です。市区町村の区域は集計時点のもので、過去の値も合併後の区域に組み替えられています。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[市区町村別の人口統計テーブル](/datasets/queria/e_stat/ssds/a_municipal_population)から、任意の市区町村の総人口と外国人人口を同じテーブルで取り出せます。

```sql id=trend
SELECT year, CAST(MAX(TRY_CAST(value AS DOUBLE)) AS INTEGER) AS foreign_pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1700' AND area_name = '全国' GROUP BY year ORDER BY year
```

```sql id=national_index
WITH n AS ( SELECT year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1101') AS total, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1700') AS foreign_pop FROM e_stat.ssds.a_pref_population WHERE area_name = '全国' AND cat01 IN ('A1101', 'A1700') GROUP BY year HAVING MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1700') IS NOT NULL ), b AS (SELECT total AS base_total, foreign_pop AS base_foreign FROM n WHERE year = 2010) SELECT n.year, ROUND(n.foreign_pop / b.base_foreign * 100, 1) AS foreign_idx, ROUND((n.total - n.foreign_pop) / (b.base_total - b.base_foreign) * 100, 1) AS other_idx, CAST(n.foreign_pop AS INTEGER) AS foreign_pop, CAST(n.total - n.foreign_pop AS INTEGER) AS other_pop FROM n CROSS JOIN b ORDER BY n.year
```

```sql id=nationality_composition
WITH n AS ( SELECT year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1101') AS total, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1102') AS japanese, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1700') AS foreign_pop FROM e_stat.ssds.a_pref_population WHERE area_name = '全国' AND cat01 IN ('A1101', 'A1102', 'A1700') AND year IN (2000, 2005, 2010, 2015, 2020) GROUP BY year ) SELECT year AS 年, CAST(total AS INTEGER) AS 総人口, CAST(japanese AS INTEGER) AS 日本人人口, CAST(foreign_pop AS INTEGER) AS 外国人人口, CAST(total - japanese - foreign_pop AS INTEGER) AS 国籍不詳, ROUND((total - japanese - foreign_pop) / total * 100, 2) AS '国籍不詳の割合（%）' FROM n ORDER BY 年
```

```sql id=ratio_ranking
WITH m AS ( SELECT p.area_name, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1700') AS foreign_pop, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1101') AS total_pop, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1700') / MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1101') * 100 AS ratio FROM e_stat.ssds.a_municipal_population p JOIN soumu.code.municipality c ON p.area = c.area_code WHERE p.year = 2020 AND p.cat01 IN ('A1101', 'A1700') AND c.is_municipality GROUP BY p.area_name ) SELECT area_name, ROUND(ratio, 1) AS foreign_ratio, CAST(foreign_pop AS INTEGER) AS foreign_pop, CAST(total_pop AS INTEGER) AS total_pop FROM m WHERE total_pop >= 10000 ORDER BY ratio DESC, area_name LIMIT 20
```

```sql id=city_ratio_trend
WITH m AS ( SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1700') / MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1101') * 100 AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 IN ('A1101', 'A1700') AND area_name IN ('群馬県 大泉町', '東京都 豊島区', '埼玉県 蕨市', '岐阜県 美濃加茂市', '茨城県 常総市') GROUP BY area_name, year ) SELECT year, ROUND(MAX(ratio) FILTER (WHERE area_name = '群馬県 大泉町'), 2) AS ohizumi, ROUND(MAX(ratio) FILTER (WHERE area_name = '東京都 豊島区'), 2) AS toshima, ROUND(MAX(ratio) FILTER (WHERE area_name = '埼玉県 蕨市'), 2) AS warabi, ROUND(MAX(ratio) FILTER (WHERE area_name = '岐阜県 美濃加茂市'), 2) AS minokamo, ROUND(MAX(ratio) FILTER (WHERE area_name = '茨城県 常総市'), 2) AS joso FROM m GROUP BY year ORDER BY year
```

```sql id=increase_ranking
WITH m AS ( SELECT p.area_name, p.year, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1700') AS f, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1101') AS t FROM e_stat.ssds.a_municipal_population p JOIN soumu.code.municipality c ON p.area = c.area_code WHERE p.year IN (2015, 2020) AND p.cat01 IN ('A1101', 'A1700') AND c.is_municipality GROUP BY p.area_name, p.year ), p AS ( SELECT area_name, MAX(f) FILTER (WHERE year = 2020) AS f20, MAX(f) FILTER (WHERE year = 2015) AS f15, MAX(t) FILTER (WHERE year = 2020) AS t20, MAX(t) FILTER (WHERE year = 2015) AS t15 FROM m GROUP BY area_name ) SELECT area_name, CAST(f20 - f15 AS INTEGER) AS foreign_inc, CAST((t20 - f20) - (t15 - f15) AS INTEGER) AS other_inc FROM p WHERE f15 IS NOT NULL AND f20 IS NOT NULL AND t15 IS NOT NULL AND t20 IS NOT NULL AND f15 >= 100 ORDER BY foreign_inc DESC, area_name LIMIT 20
```

```sql id=offset_summary
WITH m AS ( SELECT p.area_name, p.year, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1700') AS f, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1101') AS t FROM e_stat.ssds.a_municipal_population p JOIN soumu.code.municipality c ON p.area = c.area_code WHERE p.year IN (2015, 2020) AND p.cat01 IN ('A1101', 'A1700') AND c.is_municipality GROUP BY p.area_name, p.year ), p AS ( SELECT area_name, MAX(f) FILTER (WHERE year = 2020) AS f20, MAX(f) FILTER (WHERE year = 2015) AS f15, MAX(t) FILTER (WHERE year = 2020) AS t20, MAX(t) FILTER (WHERE year = 2015) AS t15 FROM m GROUP BY area_name ), c AS ( SELECT f20 - f15 AS foreign_inc, (t20 - f20) - (t15 - f15) AS other_inc, t20 - t15 AS total_inc FROM p WHERE f15 IS NOT NULL AND f20 IS NOT NULL AND t15 IS NOT NULL AND t20 IS NOT NULL ) SELECT count(*) AS 市区町村数, count(*) FILTER (WHERE other_inc < 0) AS 外国人以外が減った, count(*) FILTER (WHERE other_inc < 0 AND foreign_inc > 0) AS うち外国人が増えた, count(*) FILTER (WHERE other_inc < 0 AND total_inc > 0) AS うち総人口が増えた, ROUND(MEDIAN(CASE WHEN other_inc < 0 AND foreign_inc > 0 THEN foreign_inc / (-other_inc) END) * 100, 1) AS '減少分を埋めた割合の中央値（%）' FROM c
```

```sql id=offset_towns
WITH m AS ( SELECT p.area_name, p.year, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1700') AS f, MAX(TRY_CAST(p.value AS DOUBLE)) FILTER (WHERE p.cat01 = 'A1101') AS t FROM e_stat.ssds.a_municipal_population p JOIN soumu.code.municipality c ON p.area = c.area_code WHERE p.year IN (2015, 2020) AND p.cat01 IN ('A1101', 'A1700') AND c.is_municipality GROUP BY p.area_name, p.year ), p AS ( SELECT area_name, MAX(f) FILTER (WHERE year = 2020) AS f20, MAX(f) FILTER (WHERE year = 2015) AS f15, MAX(t) FILTER (WHERE year = 2020) AS t20, MAX(t) FILTER (WHERE year = 2015) AS t15 FROM m GROUP BY area_name ), c AS ( SELECT area_name, f20 - f15 AS foreign_inc, (t20 - f20) - (t15 - f15) AS other_inc, t20 - t15 AS total_inc FROM p WHERE f15 IS NOT NULL AND f20 IS NOT NULL AND t15 IS NOT NULL AND t20 IS NOT NULL ) SELECT area_name, CAST(foreign_inc AS INTEGER) AS foreign_inc, CAST(other_inc AS INTEGER) AS other_inc, CAST(total_inc AS INTEGER) AS total_inc FROM c WHERE other_inc < 0 AND total_inc > 0 ORDER BY total_inc DESC, area_name LIMIT 15
```
