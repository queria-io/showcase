---
title: 東京都と隣の3県を合わせた人口あたり医師数は、28回の調査で一度も全国に届いていない
description: 人口10万人あたりの医療施設の医師数は、東京都・埼玉県・千葉県・神奈川県を合わせると、1975〜2022年の28回の調査すべてで全国を下回りました。
publishedAt: 2026-02-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療
  - 医師偏在
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（I 健康・医療）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/I
    publisher: 総務省統計局
  - title: 令和4（2022）年 医師・歯科医師・薬剤師統計の概況
    url: https://www.mhlw.go.jp/toukei/saikin/hw/ishi/22/index.html
    publisher: 厚生労働省
  - title: 令和5年（2023）患者調査の概況
    url: https://www.mhlw.go.jp/toukei/saikin/hw/kanja/23/index.html
    publisher: 厚生労働省
agentHint: 医療施設に従事する医師数（I6101）を人口10万人あたりにして、関西の2府4県（大阪・京都・兵庫・奈良・滋賀・和歌山）を合わせた値が1975年から2022年まで全国を上回っているか確かめて
socialAnnounce: |-
  2022年の人口あたりの医師数で東京都は5位ですが、埼玉・千葉・神奈川と合わせると全国平均を下回ります。

  1975年から2022年までの28回の調査で、全国を上回った回は一度もありません。医療機関の開業地選びや、県の医師確保の検討に。
---

病院や診療所で働く医師は、1975年の12.6万人から2022年の32.7万人へ2.6倍に増えました。人口10万人あたりで見ると、2022年に最も多いのは徳島県の335.7人、最も少ないのは埼玉県の180.2人です。東京都は324.6人で5位に入ります。

東京都と、その隣の埼玉県・千葉県・神奈川県を合わせた1都3県を1つの地域として見ると、人口10万人あたりの医師数は250.8人で、全国の262.1人を下回ります。この1都3県の合計は、1975年から2022年までの28回の調査で一度も全国を上回っていません。

## 1都3県を合わせると、28回とも全国を下回る

使ったのは e-Stat「社会・人口統計体系」の都道府県別の健康・医療データ（`i_pref_health`）にある医療施設医師数（`I6101`）と、人口データ（`a_pref_population`）の総人口（`A1101`）です。医療施設医師数は、病院・診療所で働く医師の数で、大学病院で診療する医師は入りますが、大学の臨床以外の部門や行政機関、介護老人保健施設で働く医師は入りません。厚生労働省の医師・歯科医師・薬剤師統計が元で、都道府県は医師が働いている場所（従業地）で集計しています。調査は1982年まで毎年、その後は2年ごとで、各年12月31日の人数です。

下の図は、1都3県の医師数の合計を人口の合計で割った値と、全国・東京都・埼玉県の値を並べたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "area_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"nation\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "strokeWidth": 2,
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "nation", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "nation",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "1都3県の合計", "東京都", "埼玉県"],
            "range": ["#64748b", "#f97316", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "area_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo_area\"]) ? 0 : 1",
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
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tokyo_area", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokyo_area",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "color": {
          "datum": "1都3県の合計",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "1都3県の合計", "東京都", "埼玉県"],
            "range": ["#64748b", "#f97316", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "area_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokyo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "1都3県の合計", "東京都", "埼玉県"],
            "range": ["#64748b", "#f97316", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "area_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"saitama\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "saitama", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "saitama",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "color": {
          "datum": "埼玉県",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "1都3県の合計", "東京都", "埼玉県"],
            "range": ["#64748b", "#f97316", "#3b82f6", "#94a3b8"]
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

1都3県の合計は、全国の0.91〜0.99倍の間で動いてきました。最も近づいたのは1984年の0.99倍で、2022年は0.96倍です。東京都だけでは全国を大きく上回りますが、人口の多い3県が全国を下回る分のほうが大きいため、合計すると全国を下回ります。

```sql
SELECT first_year AS 最初の調査年, last_year AS 最後の調査年, surveys AS 調査の回数, tokyo_area_below_nation AS "1都3県が全国を下回った回数", min_ratio AS 全国に対する比_最小, max_ratio AS 全国に対する比_最大, max_ratio_year AS 最も近づいた年, doctors_1975 AS 全国の医師数_1975年, doctors_2022 AS 全国の医師数_2022年, doctors_growth AS 全国の医師数の倍率 FROM area_summary
```

```sql
SELECT year AS 年, tokyo_area AS "1都3県の合計", nation AS 全国, tokyo AS 東京都, kanagawa AS 神奈川県, chiba AS 千葉県, saitama AS 埼玉県, tokyo_area_to_nation AS "1都3県の全国に対する比" FROM area_trend ORDER BY year
```

2022年に1都3県を全国と同じ水準にするには、合計で4,200人の医師が足りない計算になります。県ごとに見ると、埼玉県だけで6,000人足りません。

```sql
SELECT area_name AS 地域, doctors AS 医療施設の医師数, per_100k AS 人口10万人あたり, nation_per_100k AS 全国の人口10万人あたり, shortfall AS 全国の水準までの不足_100人単位 FROM shortfall
```

## 埼玉県・千葉県・茨城県は、28回とも43位以下

都道府県の順位で見ても、下位の県はほとんど変わっていません。下の図は、人口10万人あたりの医師数の順位（多いほうから1位）を、首都圏の4県と沖縄県について並べたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "rank_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"saitama\"]) ? 0 : 1",
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
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "saitama", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "saitama",
          "type": "quantitative",
          "scale": {"domain": [48, 0], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたりの医師数の順位", "grid": true, "tickMinStep": 5}
        },
        "color": {
          "datum": "埼玉県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉県", "茨城県", "千葉県", "神奈川県", "沖縄県"],
            "range": ["#f97316", "#eab308", "#ef4444", "#8b5cf6", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rank_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ibaraki\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#eab308",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ibaraki", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "ibaraki",
          "type": "quantitative",
          "scale": {"domain": [48, 0], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたりの医師数の順位", "grid": true, "tickMinStep": 5}
        },
        "color": {
          "datum": "茨城県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉県", "茨城県", "千葉県", "神奈川県", "沖縄県"],
            "range": ["#f97316", "#eab308", "#ef4444", "#8b5cf6", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rank_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"chiba\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "chiba", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "chiba",
          "type": "quantitative",
          "scale": {"domain": [48, 0], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたりの医師数の順位", "grid": true, "tickMinStep": 5}
        },
        "color": {
          "datum": "千葉県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉県", "茨城県", "千葉県", "神奈川県", "沖縄県"],
            "range": ["#f97316", "#eab308", "#ef4444", "#8b5cf6", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rank_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kanagawa\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#8b5cf6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "kanagawa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "kanagawa",
          "type": "quantitative",
          "scale": {"domain": [48, 0], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたりの医師数の順位", "grid": true, "tickMinStep": 5}
        },
        "color": {
          "datum": "神奈川県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉県", "茨城県", "千葉県", "神奈川県", "沖縄県"],
            "range": ["#f97316", "#eab308", "#ef4444", "#8b5cf6", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rank_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"okinawa\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "okinawa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "okinawa",
          "type": "quantitative",
          "scale": {"domain": [48, 0], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたりの医師数の順位", "grid": true, "tickMinStep": 5}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉県", "茨城県", "千葉県", "神奈川県", "沖縄県"],
            "range": ["#f97316", "#eab308", "#ef4444", "#8b5cf6", "#22c55e"]
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

埼玉県は28回すべてで46位か47位、茨城県は44〜46位、千葉県は43〜46位でした。1975年に47位だった沖縄県は、2010年代に21位まで上がっています。沖縄県が順位を大きく上げたのに対し、3県は下位から動いていません。神奈川県は25〜43位の間で、2022年は40位です。

```sql
SELECT area_name AS 都道府県, surveys AS 調査の回数, best_rank AS 最も高い順位, worst_rank AS 最も低い順位, rank_1975 AS 順位_1975年, rank_2022 AS 順位_2022年 FROM rank_range
```

2022年の47都道府県を並べると、次のとおりです。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "doc_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "y": {
          "field": "area_name",
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
      "data": {"name": "doc_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "y": {
          "field": "area_name",
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
      "data": {"name": "doc_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたりの医療施設の医師数（人）", "grid": true}
        },
        "y": {
          "field": "area_name",
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

## 埼玉県・千葉県・茨城県は、県外に通う患者の分を加えても全国との差が残る

医師数は働いている場所で集計するので、埼玉県や千葉県の住民が東京都の病院を受診すると、その患者を診る医師は東京都に計上されます。県内の医療機関で受診した患者数と、県に住む患者数を比較すると、県境をまたぐ受診の大きさが分かります。厚生労働省の患者調査（2023年10月の調査日1日分を、抽出した医療機関から推計した値。外来には歯科診療所の患者も含みます）では、東京都の医療機関が受けた外来患者は、東京都に住む外来患者より14.1%多くなっています。

```sql
SELECT area_name AS 都県, outpatients_facility AS 外来_県内の施設が受けた患者_千人, outpatients_residence AS 外来_県に住む患者_千人, outpatients_net_pct AS 外来_差_パーセント, inpatients_facility AS 入院_県内の施設が受けた患者_千人, inpatients_residence AS 入院_県に住む患者_千人, inpatients_net_pct AS 入院_差_パーセント FROM patient_flow
```

差し引きで県の外の医療機関に出ている分は、埼玉県で外来3.5%・入院2.9%、千葉県で外来2.4%、茨城県で外来3.0%でした。一方、埼玉県の人口10万人あたりの医師数は全国の7割弱です。差し引きで県外に出ている分は数%なので、その分を加えても全国との差は残ります。歯科をほとんど含まない入院で見ても、埼玉県の差し引きの流出は2.9%です。この値は県外へ出た患者と県外から来た患者を相殺した後のもので、患者がどの都県へ行ったかはこのデータには入っていません。神奈川県は差し引きで外来の13.6%が県外に出ていて、5都県の中で最も大きい流出です。

## 上位10県と下位10県の比は、1975年の1.80倍から2022年の1.51倍に縮んだ

医師の多い県と少ない県の差は、比で見ると縮小してきました。人口10万人あたりの医師数で上位10の平均を下位10の平均で割った値は、1975年の1.80倍から2022年の1.51倍になっています。最多と最少の比も3.09倍から1.86倍に下がりました。1979年まで最少だった沖縄県が順位を上げ、1980年からは最少がずっと埼玉県です。人数の差（最多−最少）は112.5人から155.4人に広がりました。医師の総数が増えたので、比が同じでも人数の差は大きくなります。

```sql
SELECT year AS 年, max_area AS 最多, max_v AS 最多の値, min_area AS 最少, min_v AS 最少の値, max_minus_min AS 最多と最少の差, max_to_min AS 最多と最少の比, top10_to_bottom10 AS 上位10と下位10の平均の比 FROM spread WHERE year IN (1975, 1980, 1990, 2000, 2010, 2020, 2022) ORDER BY year
```

全国の差が縮むなかで、1都3県の合計が全国を下回る状態と、埼玉県・千葉県・茨城県が下位にいる状態は、28回の調査を通じて変わっていません。

## 業務での使い方

診療所の開業地を探す医師にとって、人口あたりの医師数が全国を下回る県は、住民1人あたりの競合の医師が少ない県です。この医師数には病院の勤務医も入り、住民の一部は県外の医療機関に通うので、診療所どうしの競合を見るには同じテーブルの一般診療所数（`I5102`）と並べます。東京都の医師数は全国上位ですが、埼玉県・千葉県・神奈川県を合わせた1都3県は28回の調査すべてで全国を下回り、埼玉県と千葉県は毎回43位以下でした。埼玉県・千葉県・茨城県は、県外の医療機関に通う患者の分を差し引きで加えても、全国との差が残ります。本記事の SQL の都道府県名を書き換えれば、自分の県の順位の履歴や、隣の県と合わせた値を同じ形で出せます。都道府県単位の集計なので、県の中の二次医療圏ごとの差はこのデータでは分かりません。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年10月28日時点で集計しています。医療施設医師数の元データは厚生労働省の[医師・歯科医師・薬剤師統計](https://www.mhlw.go.jp/toukei/saikin/hw/ishi/22/index.html)、推計患者数の元データは[患者調査](https://www.mhlw.go.jp/toukei/saikin/hw/kanja/23/index.html)で、定義と時点は[項目定義（I 健康・医療）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/I)にあります。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の健康・医療テーブル](/datasets/queria/e_stat/ssds/i_pref_health)から、自分の県の医師数を1975年から並べたり、看護師数や病院数と比較したりできます。

```sql id=area_trend
-- 人口10万人あたりの医療施設の医師数。1都3県は医師数の合計を人口の合計で割る
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), g AS ( SELECT year, SUM(doctors) FILTER (WHERE tokyo_area) / SUM(pop) FILTER (WHERE tokyo_area) * 100000 AS tokyo_area, SUM(doctors) FILTER (WHERE area_name = '全国') / SUM(pop) FILTER (WHERE area_name = '全国') * 100000 AS nation, SUM(doctors) FILTER (WHERE area_name = '東京都') / SUM(pop) FILTER (WHERE area_name = '東京都') * 100000 AS tokyo, SUM(doctors) FILTER (WHERE area_name = '神奈川県') / SUM(pop) FILTER (WHERE area_name = '神奈川県') * 100000 AS kanagawa, SUM(doctors) FILTER (WHERE area_name = '千葉県') / SUM(pop) FILTER (WHERE area_name = '千葉県') * 100000 AS chiba, SUM(doctors) FILTER (WHERE area_name = '埼玉県') / SUM(pop) FILTER (WHERE area_name = '埼玉県') * 100000 AS saitama FROM j GROUP BY year ) SELECT year, ROUND(tokyo_area, 1) AS tokyo_area, ROUND(nation, 1) AS nation, ROUND(tokyo, 1) AS tokyo, ROUND(kanagawa, 1) AS kanagawa, ROUND(chiba, 1) AS chiba, ROUND(saitama, 1) AS saitama, ROUND(tokyo_area / nation, 3) AS tokyo_area_to_nation FROM g ORDER BY year
```

```sql id=area_summary
-- 1都3県の合計が全国を下回った回数と、全国の医師数の伸び（プロットはしない）
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), g AS ( SELECT year, SUM(doctors) FILTER (WHERE tokyo_area) / SUM(pop) FILTER (WHERE tokyo_area) AS tokyo_area, SUM(doctors) FILTER (WHERE area_name = '全国') / SUM(pop) FILTER (WHERE area_name = '全国') AS nation, SUM(doctors) FILTER (WHERE area_name = '全国') AS doctors_nation FROM j GROUP BY year ) SELECT MIN(year) AS first_year, MAX(year) AS last_year, COUNT(*) AS surveys, COUNT(*) FILTER (WHERE tokyo_area < nation) AS tokyo_area_below_nation, ROUND(MIN(tokyo_area / nation), 2) AS min_ratio, ROUND(MAX(tokyo_area / nation), 2) AS max_ratio, ARG_MAX(year, tokyo_area / nation) AS max_ratio_year, MAX(doctors_nation) FILTER (WHERE year = 1975) AS doctors_1975, MAX(doctors_nation) FILTER (WHERE year = 2022) AS doctors_2022, ROUND(MAX(doctors_nation) FILTER (WHERE year = 2022) / MAX(doctors_nation) FILTER (WHERE year = 1975), 2) AS doctors_growth FROM g
```

```sql id=rank_trend
-- 人口10万人あたりの医療施設の医師数の都道府県順位（多いほうから。同値は同順位）
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), r AS ( SELECT year, area_name, RANK() OVER (PARTITION BY year ORDER BY doctors / pop DESC) AS rk FROM j WHERE area_name <> '全国' ) SELECT year, MAX(rk) FILTER (WHERE area_name = '埼玉県') AS saitama, MAX(rk) FILTER (WHERE area_name = '千葉県') AS chiba, MAX(rk) FILTER (WHERE area_name = '茨城県') AS ibaraki, MAX(rk) FILTER (WHERE area_name = '神奈川県') AS kanagawa, MAX(rk) FILTER (WHERE area_name = '沖縄県') AS okinawa, COUNT(*) AS prefectures FROM r GROUP BY year ORDER BY year
```

```sql id=rank_range
-- 28回の調査での順位の幅（プロットはしない）
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), r AS ( SELECT year, area_name, RANK() OVER (PARTITION BY year ORDER BY doctors / pop DESC) AS rk FROM j WHERE area_name <> '全国' ) SELECT area_name, COUNT(*) AS surveys, MIN(rk) AS best_rank, MAX(rk) AS worst_rank, MAX(rk) FILTER (WHERE year = 1975) AS rank_1975, MAX(rk) FILTER (WHERE year = 2022) AS rank_2022 FROM r WHERE area_name IN ('埼玉県', '千葉県', '茨城県', '神奈川県', '沖縄県', '東京都') GROUP BY area_name ORDER BY worst_rank DESC, area_name
```

```sql id=doc_top
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), r AS ( SELECT area_name, ROUND(doctors / pop * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY doctors / pop DESC, area_name) AS rn FROM j WHERE year = 2022 AND area_name <> '全国' ) SELECT area_name, per_100k FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=doc_mid
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), r AS ( SELECT area_name, ROUND(doctors / pop * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY doctors / pop DESC, area_name) AS rn FROM j WHERE year = 2022 AND area_name <> '全国' ) SELECT area_name, per_100k FROM r WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=doc_bottom
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), r AS ( SELECT area_name, ROUND(doctors / pop * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY doctors / pop DESC, area_name) AS rn FROM j WHERE year = 2022 AND area_name <> '全国' ) SELECT area_name, per_100k FROM r WHERE rn > 37 ORDER BY rn
```

```sql id=spread
-- 47都道府県のばらつき（プロットはしない）
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), x AS ( SELECT year, area_name, doctors / pop * 100000 AS v, ROW_NUMBER() OVER (PARTITION BY year ORDER BY doctors / pop DESC, area_name) AS rank_desc, ROW_NUMBER() OVER (PARTITION BY year ORDER BY doctors / pop, area_name) AS rank_asc FROM j WHERE area_name <> '全国' ) SELECT year, ROUND(MAX(v), 1) AS max_v, ARG_MAX(area_name, v) AS max_area, ROUND(MIN(v), 1) AS min_v, ARG_MIN(area_name, v) AS min_area, ROUND(MAX(v) - MIN(v), 1) AS max_minus_min, ROUND(MAX(v) / MIN(v), 2) AS max_to_min, ROUND(AVG(v) FILTER (WHERE rank_desc <= 10) / AVG(v) FILTER (WHERE rank_asc <= 10), 2) AS top10_to_bottom10 FROM x GROUP BY year ORDER BY year
```

```sql id=patient_flow
-- 2023年10月の調査日の推計患者数（千人）。施設所在地は県内の医療施設が受けた患者、患者住所地はその県に住む患者
SELECT area_name, MAX(value) FILTER (WHERE cat01 = 'I820102') AS outpatients_facility, MAX(value) FILTER (WHERE cat01 = 'I820202') AS outpatients_residence, ROUND((MAX(value) FILTER (WHERE cat01 = 'I820102') / MAX(value) FILTER (WHERE cat01 = 'I820202') - 1) * 100, 1) AS outpatients_net_pct, MAX(value) FILTER (WHERE cat01 = 'I820101') AS inpatients_facility, MAX(value) FILTER (WHERE cat01 = 'I820201') AS inpatients_residence, ROUND((MAX(value) FILTER (WHERE cat01 = 'I820101') / MAX(value) FILTER (WHERE cat01 = 'I820201') - 1) * 100, 1) AS inpatients_net_pct FROM e_stat.ssds.i_pref_health WHERE cat01 IN ('I820101', 'I820102', 'I820201', 'I820202') AND year = 2023 AND area_name IN ('東京都', '神奈川県', '千葉県', '埼玉県', '茨城県') GROUP BY area_name ORDER BY outpatients_net_pct DESC
```

```sql id=shortfall
-- 2022年に全国と同じ人口10万人あたりの医師数にするには何人足りないか（プロットはしない）
WITH d AS ( SELECT year, area_name, value AS doctors FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6101' AND value IS NOT NULL ), p AS ( SELECT year, area_name, value AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value > 0 ), j AS ( SELECT year, area_name, doctors, pop, area_name IN ('東京都', '埼玉県', '千葉県', '神奈川県') AS tokyo_area FROM d JOIN p USING (year, area_name) ), k AS ( SELECT area_name, doctors, pop FROM j WHERE year = 2022 AND area_name IN ('埼玉県', '千葉県', '茨城県', '神奈川県', '東京都') UNION ALL SELECT '1都3県の合計', SUM(doctors), SUM(pop) FROM j WHERE year = 2022 AND tokyo_area ), n AS ( SELECT doctors / pop AS rate FROM j WHERE year = 2022 AND area_name = '全国' ) SELECT k.area_name, k.doctors, ROUND(k.doctors / k.pop * 100000, 1) AS per_100k, ROUND(n.rate * 100000, 1) AS nation_per_100k, ROUND(n.rate * k.pop - k.doctors, -2) AS shortfall FROM k, n ORDER BY shortfall DESC
```
