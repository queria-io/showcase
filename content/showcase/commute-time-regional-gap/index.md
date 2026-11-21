---
title: 片道1時間以上かけて通勤する世帯の割合が高い5都県は、1978年から2023年までの10回の調査で一度も入れ替わっていない
description: 住宅・土地統計調査の10回分で、片道1時間以上かけて通勤する世帯の割合の上位5は毎回同じ5都県です。2023年は5都県とも2018年を下回りました。
publishedAt: 2026-06-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 通勤時間
  - 職住近接
  - 住宅・土地統計
  - 採用
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（H 居住）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/H
    publisher: 総務省統計局
  - title: 令和5年住宅・土地統計調査 用語の解説
    url: https://www.stat.go.jp/data/jyutaku/2023/pdf/yougo.pdf
    publisher: 総務省統計局
  - title: 平成15年調査調査票と平成20年調査調査票の対照表（案）
    url: https://www.soumu.go.jp/main_sosiki/singi/toukei/meetings/iinkai_1/siryou_8-11.pdf
    publisher: 総務省
agentHint: 2023年の通勤時間の構成を市区町村別（h_municipal_housing の H7405 系）に出して、千葉県・埼玉県・神奈川県のどの市で片道1時間以上の世帯が多いかを比べて
socialAnnounce: |-
  片道1時間以上かけて通勤する世帯の割合は、1978〜2023年の10回の調査すべてで千葉・埼玉・神奈川・奈良・東京が上位5です。

  採用圏や拠点の検討に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

片道1時間以上かけて通勤する世帯の割合が高い上位5は、1978年から2023年までの10回の調査で、毎回千葉県・埼玉県・神奈川県・奈良県・東京都でした。2023年は神奈川県が32.9%で最も高く、最も低い鳥取県（3.1%）の10倍以上です。5都県の割合は2018年と比較して0.3〜1.4ポイント下がり、上がった都県はありません。

使ったのは総務省統計局の住宅・土地統計調査です。この調査は5年ごとに、家計を主に支える人の自宅から勤め先までの片道の通勤時間を尋ねています。採用する人の住まいから勤め先までの時間は、拠点の場所や勤務制度を決めるときの前提になります。

## 通勤時間は、雇われて働く世帯を4つの区分で集計している

データは e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別の居住テーブル（`h_pref_housing`）から取っています。家計を主に支える人が雇われて働いている世帯を、片道の通勤時間で4つに分けた世帯数です。

```sql
SELECT * FROM coverage
```

2018年までは普通世帯（`H7401` 系）、2023年は主世帯（`H7405` 系）を数えた系列で、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/H)では別の項目です。主世帯は1つの住宅に住む世帯のうち家の持ち主や借り主の世帯で、間借りの世帯などを含みません。2023年の4区分も、2018年までと同じ30分・1時間・1時間30分の区切りです。

通勤時間は、[用語の解説](https://www.stat.go.jp/data/jyutaku/2023/pdf/yougo.pdf)で「ふだん利用している交通機関による自宅から勤め先までの通常の通勤所要時間（片道）」と定められています。週に何日通うかは尋ねていないので、この値は住まいと勤め先がどれだけ離れているかを表します。

割合の分母は4区分の合計（通勤時間が分かる世帯）で、片道1時間以上は「1時間〜1時間30分」と「1時間30分以上」の合計です。

## 2023年は神奈川県が32.9%で最も高く、鳥取県の10倍以上

```chart caption="片道1時間以上かけて通勤する世帯の割合（2023年）"
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_2023_top10"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_2023_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_2023_bottom10"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

2023年に割合が最も高いのは神奈川県（32.9%）で、埼玉県（32.5%）、千葉県（32.1%）、奈良県（27.3%）、東京都（23.3%）が続きます。6位は兵庫県（18.9%）で、全国は15.2%です。最も低い鳥取県は3.1%で、神奈川県は鳥取県の10倍以上です。

```map
type: map
caption: "片道1時間以上かけて通勤する世帯の割合（2023年）"
layers:
  - from: map_2023
    geojson: geojson
    color: value
    label: pref_name
    name: "1時間以上（%）"
lng: 137
lat: 36.5
zoom: 4
```

色が濃いのは東京都・神奈川県・埼玉県・千葉県と、大阪府の東隣の奈良県です。愛知県は12.3%で、名古屋の周りの県にはここまで高い県はありません。

## 上位5都県は、1978年から10回とも同じ

同じ割合を10回分並べます。1998年と2003年の値は、47都道府県すべてで1993年と2008年の両方より高く出ています。2008年の低下は、通勤時間の答え方が数字の書き込み（2003年）から区分を選ぶ方式（2008年）に変わった時期と重なります（[総務省の対照表](https://www.soumu.go.jp/main_sosiki/singi/toukei/meetings/iinkai_1/siryou_8-11.pdf)）。対照表は2003年と2008年の調査票だけを比較していて、1998年に上がった理由は書かれていません。そのため、1998年と2003年の前後の上がり下がりは、通勤そのものの変化とはみなせません。

```sql
SELECT * FROM step_check
```

```chart caption="片道1時間以上かけて通勤する世帯の割合の推移"
{
  "layer": [
    {
      "data": {"name": "trend_kanagawa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pct\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {
            "title": "調査年",
            "values": [1978, 1983, 1988, 1993, 1998, 2003, 2008, 2013, 2018, 2023]
          }
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
        },
        "color": {
          "datum": "神奈川県",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県", "埼玉県", "千葉県", "奈良県", "東京都", "全国"],
            "range": ["#ef4444", "#f97316", "#eab308", "#a855f7", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_saitama"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pct\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {
            "title": "調査年",
            "values": [1978, 1983, 1988, 1993, 1998, 2003, 2008, 2013, 2018, 2023]
          }
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
        },
        "color": {
          "datum": "埼玉県",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県", "埼玉県", "千葉県", "奈良県", "東京都", "全国"],
            "range": ["#ef4444", "#f97316", "#eab308", "#a855f7", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_chiba"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pct\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#eab308",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {
            "title": "調査年",
            "values": [1978, 1983, 1988, 1993, 1998, 2003, 2008, 2013, 2018, 2023]
          }
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
        },
        "color": {
          "datum": "千葉県",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県", "埼玉県", "千葉県", "奈良県", "東京都", "全国"],
            "range": ["#ef4444", "#f97316", "#eab308", "#a855f7", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_nara"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pct\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#a855f7",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {
            "title": "調査年",
            "values": [1978, 1983, 1988, 1993, 1998, 2003, 2008, 2013, 2018, 2023]
          }
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
        },
        "color": {
          "datum": "奈良県",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県", "埼玉県", "千葉県", "奈良県", "東京都", "全国"],
            "range": ["#ef4444", "#f97316", "#eab308", "#a855f7", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pct\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {
            "title": "調査年",
            "values": [1978, 1983, 1988, 1993, 1998, 2003, 2008, 2013, 2018, 2023]
          }
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県", "埼玉県", "千葉県", "奈良県", "東京都", "全国"],
            "range": ["#ef4444", "#f97316", "#eab308", "#a855f7", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pct\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {
            "title": "調査年",
            "values": [1978, 1983, 1988, 1993, 1998, 2003, 2008, 2013, 2018, 2023]
          }
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "片道1時間以上の世帯の割合（%）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県", "埼玉県", "千葉県", "奈良県", "東京都", "全国"],
            "range": ["#ef4444", "#f97316", "#eab308", "#a855f7", "#3b82f6", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rect", "color": "#94a3b8", "opacity": 0.15},
      "encoding": {
        "x": {"datum": 1995.5, "type": "quantitative"},
        "x2": {"datum": 2005.5, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

各回の上位6を並べると、上位5は10回とも千葉県・埼玉県・神奈川県・奈良県・東京都で、入れ替わるのは5都県の中の順番だけです。6位は2003年まで大阪府、2008年からは兵庫県です。

```sql
SELECT * FROM top6_by_year
```

東京都は10回とも5位で、千葉県・埼玉県・神奈川県のどれよりも割合が低くなっています。通勤時間は住んでいる都道府県で集計するので、3県から東京都の勤め先に通う世帯は3県の値に入ります。

## 2018年から2023年に、5都県はいずれも下がった

隣り合う2018年と2023年を比較すると、5都県はいずれも0.3〜1.4ポイント下がりました。2023年は主世帯の系列なので、普通世帯を集計した2018年までとは対象の世帯の範囲が少し違います。

```sql
SELECT * FROM five_changes
```

47都道府県では、2018年から2023年の変化が上下1.0ポイント以内に収まったのは44で、超えたのは和歌山県・神奈川県・千葉県の3県でした。

```chart caption="片道1時間以上かけて通勤する世帯の割合の変化（2018年→2023年、ポイント）"
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "change_2018_2023"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2023年の割合 − 2018年の割合（ポイント）", "grid": true}
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

```sql
SELECT * FROM change_summary
```

住宅・土地統計調査は抽出した世帯を調べる標本調査なので、都道府県の値は推計値で、小さな上下には推計の誤差が含まれます。下がった側で最も大きいのは和歌山県（−1.7ポイント）、上がった側で最も大きいのは青森県と愛知県（ともに+0.6ポイント）でした。

2018年と2023年の調査のあいだには、新型コロナウイルス感染症の流行がありました。通勤時間は週に何日通うかを問わない値なので、勤め先から遠くへ移り住んだ世帯が増えれば、1時間以上の割合は上がる方向に動きます。5都県の割合はどれも下がっているので、勤め先から遠くへ移り住んだ世帯が増えたとは、この割合からは言えません。ふだん出勤しない人の通勤時間をどう答えるかは、用語の解説には書かれていません。

## 神奈川県・埼玉県・千葉県では、1時間30分以上の世帯が8%を超える

```chart caption="通勤時間の構成（2023年）"
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "composition_2023"},
      "transform": [
        {"fold": ["p_u30", "p_3060", "p_6090", "p_90"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"p_u30\": \"30分未満\", \"p_3060\": \"30分〜1時間\", \"p_6090\": \"1時間〜1時間30分\", \"p_90\": \"1時間30分以上\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"p_u30\",\"p_3060\",\"p_6090\",\"p_90\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "構成比（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["30分未満", "30分〜1時間", "1時間〜1時間30分", "1時間30分以上"],
            "range": ["#86efac", "#fcd34d", "#f97316", "#ef4444"]
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
  ]
}
```

神奈川県・埼玉県・千葉県では、1時間30分以上かかる世帯が8%を超えます。宮崎県は30分未満が80.1%で、1時間30分以上は1.2%です。東京都は30分〜1時間が45.2%で最も多く、1時間30分以上は4.5%です。

## 採用と拠点の検討での使い方

千葉県・埼玉県・神奈川県では、雇われて働く人が家計を支える世帯のうち、2023年も3世帯に1世帯ほどが片道1時間以上かけて通勤しています。3県の割合は、1998年と2003年を除く8回の調査で、どれも32.1〜38.7%の間にあります。

```sql
SELECT * FROM three_pref_range
```

この割合の分母は3県に住む勤め人の世帯全体で、県内に勤める世帯も含みます。東京都の勤め先に通う世帯だけに限った1時間以上の割合は、この表からは計算できませんが、これより高くなると考えられます。東京都に拠点を置く会社の採用担当者は、3県の勤め人の世帯の3分の1ほどが片道1時間以上かけて通っていることを、出社日の数や始業時刻を決めるときの手がかりにできます。この割合は2008年から少しずつ下がっているものの、2023年も32%を下回った県はありません。サテライトオフィスを置く市を選ぶときは、2023年の値を市区町村別（`h_municipal_housing` の `H7405` 系）に引くと、片道1時間以上かかる世帯の割合が高い市を絞り込めます。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別データ（`h_pref_housing`）を2026年11月8日時点で集計しています。元データは総務省統計局の住宅・土地統計調査（1978〜2023年、5年ごとの10回）です。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名と単位を統一して公開しています。本記事で使った[都道府県別の住宅・土地統計データのテーブル](/datasets/queria/e_stat/ssds/h_pref_housing)では、住宅・土地統計調査の10回分が同じテーブルに入っているので、自社の採用圏の県を選んで推移を比較できます。

```sql id=coverage
-- 使う指標の収録年。2018年までは普通世帯、2023年は主世帯の系列
SELECT cat01, item_name, min_year, max_year, year_count
FROM e_stat.ssds.series_coverage
WHERE table_name = 'h_pref_housing'
  AND cat01 IN ('H740101','H740102','H740103','H740104','H740501','H740502','H740503','H740504')
ORDER BY cat01
```

```sql id=shares
-- 都道府県・調査年ごとの通勤時間の構成比（%）。分母は4区分の合計。rk は全国を除く47都道府県の順位
WITH d AS (
  SELECT year, area_name,
    SUM(CASE WHEN cat01 IN ('H740101','H740501') THEN TRY_CAST(value AS DOUBLE) END) AS u30,
    SUM(CASE WHEN cat01 IN ('H740102','H740502') THEN TRY_CAST(value AS DOUBLE) END) AS m3060,
    SUM(CASE WHEN cat01 IN ('H740103','H740503') THEN TRY_CAST(value AS DOUBLE) END) AS m6090,
    SUM(CASE WHEN cat01 IN ('H740104','H740504') THEN TRY_CAST(value AS DOUBLE) END) AS o90
  FROM e_stat.ssds.h_pref_housing
  WHERE cat01 IN ('H740101','H740102','H740103','H740104','H740501','H740502','H740503','H740504')
  GROUP BY year, area_name
)
SELECT year, area_name,
  (m6090 + o90) / (u30 + m3060 + m6090 + o90) * 100 AS p60_raw,
  ROUND((m6090 + o90) / (u30 + m3060 + m6090 + o90) * 100, 1) AS pct,
  ROUND(u30 / (u30 + m3060 + m6090 + o90) * 100, 1) AS p_u30,
  ROUND(m3060 / (u30 + m3060 + m6090 + o90) * 100, 1) AS p_3060,
  ROUND(m6090 / (u30 + m3060 + m6090 + o90) * 100, 1) AS p_6090,
  ROUND(o90 / (u30 + m3060 + m6090 + o90) * 100, 1) AS p_90,
  CASE WHEN area_name <> '全国' THEN ROW_NUMBER() OVER (PARTITION BY year, area_name = '全国' ORDER BY (m6090 + o90) / (u30 + m3060 + m6090 + o90) DESC, area_name) END AS rk
FROM d
```

```sql id=rank_2023_top10
SELECT area_name, pct FROM shares WHERE year = 2023 AND rk <= 10 ORDER BY rk
```

```sql id=rank_2023_mid
SELECT area_name, pct FROM shares WHERE year = 2023 AND rk > 10 AND rk <= 37 ORDER BY rk
```

```sql id=rank_2023_bottom10
SELECT area_name, pct FROM shares WHERE year = 2023 AND rk > 37 ORDER BY rk
```

```sql id=map_2023
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, s.pct AS value
FROM nlftp.boundary.prefecture p
JOIN shares s ON p.prefecture_name = s.area_name
WHERE s.year = 2023
```

```sql id=step_check
-- 1998年・2003年の割合が1993年・2008年より高い都道府県の数（47のうち）
SELECT
  COUNT(*) FILTER (WHERE y98 > y93) AS "1998年が1993年より高い",
  COUNT(*) FILTER (WHERE y98 > y08) AS "1998年が2008年より高い",
  COUNT(*) FILTER (WHERE y03 > y93) AS "2003年が1993年より高い",
  COUNT(*) FILTER (WHERE y03 > y08) AS "2003年が2008年より高い"
FROM (
  SELECT area_name,
    MAX(CASE WHEN year = 1993 THEN p60_raw END) AS y93,
    MAX(CASE WHEN year = 1998 THEN p60_raw END) AS y98,
    MAX(CASE WHEN year = 2003 THEN p60_raw END) AS y03,
    MAX(CASE WHEN year = 2008 THEN p60_raw END) AS y08
  FROM shares
  WHERE area_name <> '全国'
  GROUP BY area_name
)
```

```sql id=trend_kanagawa
SELECT year, pct FROM shares WHERE area_name = '神奈川県' ORDER BY year
```

```sql id=trend_saitama
SELECT year, pct FROM shares WHERE area_name = '埼玉県' ORDER BY year
```

```sql id=trend_chiba
SELECT year, pct FROM shares WHERE area_name = '千葉県' ORDER BY year
```

```sql id=trend_nara
SELECT year, pct FROM shares WHERE area_name = '奈良県' ORDER BY year
```

```sql id=trend_tokyo
SELECT year, pct FROM shares WHERE area_name = '東京都' ORDER BY year
```

```sql id=trend_national
SELECT year, pct FROM shares WHERE area_name = '全国' ORDER BY year
```

```sql id=top6_by_year
-- 調査年ごとの上位6（片道1時間以上の世帯の割合、%）
SELECT year AS 調査年,
  MAX(CASE WHEN rk = 1 THEN area_name || ' ' || pct END) AS "1位",
  MAX(CASE WHEN rk = 2 THEN area_name || ' ' || pct END) AS "2位",
  MAX(CASE WHEN rk = 3 THEN area_name || ' ' || pct END) AS "3位",
  MAX(CASE WHEN rk = 4 THEN area_name || ' ' || pct END) AS "4位",
  MAX(CASE WHEN rk = 5 THEN area_name || ' ' || pct END) AS "5位",
  MAX(CASE WHEN rk = 6 THEN area_name || ' ' || pct END) AS "6位"
FROM shares
WHERE rk <= 6
GROUP BY year
ORDER BY year
```

```sql id=five_changes
-- 5都県と全国の割合（%）と、2018→2023年の変化（ポイント）
SELECT area_name,
  MAX(CASE WHEN year = 2018 THEN pct END) AS "2018年",
  MAX(CASE WHEN year = 2023 THEN pct END) AS "2023年",
  ROUND(MAX(CASE WHEN year = 2023 THEN p60_raw END) - MAX(CASE WHEN year = 2018 THEN p60_raw END), 1) AS "2018→2023"
FROM shares
WHERE area_name IN ('千葉県','埼玉県','神奈川県','奈良県','東京都','全国')
GROUP BY area_name
ORDER BY "2023年" DESC
```

```sql id=change_2018_2023
SELECT a.area_name, ROUND(b.p60_raw - a.p60_raw, 1) AS diff
FROM shares a JOIN shares b ON a.area_name = b.area_name
WHERE a.year = 2018 AND b.year = 2023 AND a.area_name <> '全国'
ORDER BY b.p60_raw - a.p60_raw, a.area_name
```

```sql id=change_summary
-- 2018→2023年の変化（小数第1位に丸めた値）の大きさ別の都道府県数と、変化が最も大きい都道府県
SELECT
  COUNT(*) FILTER (WHERE ABS(ROUND(b.p60_raw - a.p60_raw, 1)) <= 1) AS "変化が1.0ポイント以内",
  COUNT(*) FILTER (WHERE ABS(ROUND(b.p60_raw - a.p60_raw, 1)) > 1) AS "変化が1.0ポイント超",
  ARG_MIN(a.area_name, b.p60_raw - a.p60_raw) AS 最も下がった,
  ROUND(MIN(b.p60_raw - a.p60_raw), 1) AS 下げ幅,
  ARG_MAX(a.area_name, b.p60_raw - a.p60_raw) AS 最も上がった,
  ROUND(MAX(b.p60_raw - a.p60_raw), 1) AS 上げ幅
FROM shares a JOIN shares b ON a.area_name = b.area_name
WHERE a.year = 2018 AND b.year = 2023 AND a.area_name <> '全国'
```

```sql id=three_pref_range
-- 千葉県・埼玉県・神奈川県の割合（%）の最小と最大。1998年と2003年を除く8回
SELECT MIN(pct) AS 最小, ARG_MIN(area_name || ' ' || year || '年', p60_raw) AS 最小の県と年,
  MAX(pct) AS 最大, ARG_MAX(area_name || ' ' || year || '年', p60_raw) AS 最大の県と年
FROM shares
WHERE area_name IN ('千葉県','埼玉県','神奈川県') AND year NOT IN (1998, 2003)
```

```sql id=composition_2023
SELECT area_name, p_u30, p_3060, p_6090, p_90
FROM shares
WHERE year = 2023 AND area_name IN ('神奈川県','埼玉県','千葉県','奈良県','東京都','大阪府','愛知県','宮崎県','全国')
ORDER BY p60_raw DESC
```
