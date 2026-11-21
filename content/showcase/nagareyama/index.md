---
title: 流山市の転入超過は2018年度の3分の1に縮み、小学校児童数は2024年度に最多の14,205人になった
description: 千葉県流山市の人口は2005年度から2024年度に約36%増えました。転入超過は2018年度の4,121人から2024年度は1,423人へ縮み、小学校児童数は2024年度に14,205人と、収録が始まった1980年度以降で最も多くなりました
publishedAt: 2026-02-22
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口
  - 子育て
  - 流山市
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数調査
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
agentHint: 流山市の出生数と15歳未満人口の推移を並べて、TX開業後にどちらが先に伸びたか、両者のタイミングのずれを確かめて。
---

千葉県流山市の人口は、2005年度の153,026人から2024年度の208,455人へ約36%増えました。転入超過は2018年度の4,121人が最も多く、2024年度は1,423人とその約3分の1です。出生数も2018年度の2,082人が最も多く、その後は増えていません。小学校の児童数は2024年度に14,205人になり、収録が始まった1980年度以降で最も多くなりました。

流山市は、2005年度のつくばエクスプレス（TX）開業をきっかけに、「母になるなら、流山市。」のキャッチコピーで子育て世代に向けた都市のPRを続け、駅前送迎保育ステーションなどの施策を行ってきました。この記事では、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別データで、流山市の人口・転入・出生・保育・学校・住宅・財政の推移を最新年度まで集計しました。グラフ中の赤い点線はTX開業の2005年度です。

## 人口はTX開業から19年で約36%増えた

住民基本台帳に基づく人口の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "population"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"population\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#2563eb"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "population", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "population",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
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
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ]
}
```

データが始まる2000年度から2004年度までは15万人前後で横ばいでしたが、TX開業から増え始め、2021年度に20万人を超えました。2005年度の153,026人から2024年度の208,455人へ、19年間で約36%（55,429人）増えています。この人口は住民基本台帳人口のうち日本人だけを集計したもので、外国人住民を含みません。以降の転入・転出・出生数も同じ範囲です。

### 2005年度を100とすると、2024年度は流山市が136.2、柏市が112.2

TX沿線の柏市、近隣の松戸市・船橋市・野田市と比較しました。2005年度の住民基本台帳人口を100とした指数で示しています。

```chart
{
  "layer": [
    {
      "data": {"name": "idx_nagareyama"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "pop_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2005年度=100）", "grid": true}
        },
        "color": {
          "datum": "流山市",
          "type": "nominal",
          "scale": {
            "domain": ["流山市", "柏市", "松戸市", "船橋市", "野田市"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "idx_kashiwa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "pop_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2005年度=100）", "grid": true}
        },
        "color": {
          "datum": "柏市",
          "type": "nominal",
          "scale": {
            "domain": ["流山市", "柏市", "松戸市", "船橋市", "野田市"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "idx_matsudo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "pop_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2005年度=100）", "grid": true}
        },
        "color": {
          "datum": "松戸市",
          "type": "nominal",
          "scale": {
            "domain": ["流山市", "柏市", "松戸市", "船橋市", "野田市"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "idx_funabashi"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "pop_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2005年度=100）", "grid": true}
        },
        "color": {
          "datum": "船橋市",
          "type": "nominal",
          "scale": {
            "domain": ["流山市", "柏市", "松戸市", "船橋市", "野田市"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "idx_noda"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "pop_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口指数（2005年度=100）", "grid": true}
        },
        "color": {
          "datum": "野田市",
          "type": "nominal",
          "scale": {
            "domain": ["流山市", "柏市", "松戸市", "船橋市", "野田市"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
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

2024年度の指数は流山市が136.2で、同じTX沿線の柏市の112.2、船橋市の109.8、松戸市の101.6を上回ります。野田市は97.2で、2005年度より人口が少なくなっています。

## 転入超過は2018年度の4,121人が最も多く、2024年度は1,423人

転入者数と転出者数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "migration"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"transfers_out\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "transparent",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "transparent"}
      },
      "encoding": {
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "transfers_out",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "migration"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"transfers_in\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "area",
        "color": "rgba(37,99,235,0.15)",
        "invalid": "break-paths-show-domains",
        "opacity": 1
      },
      "encoding": {
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "transfers_in",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人数（人）", "grid": true}
        },
        "y2": {"field": "transfers_out"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "migration"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"transfers_in\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#2563eb", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "transfers_in", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "transfers_in",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "migration"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"transfers_out\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "transfers_out", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "transfers_out",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
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
        "fontSize": 11,
        "color": "#2563eb"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 1"}},
        "y": {"value": {"expr": "height * (1 - 0.8)"}},
        "text": {"value": "転入"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 11,
        "color": "#f97316"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 1"}},
        "y": {"value": {"expr": "height * (1 - 0.5)"}},
        "text": {"value": "転出"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 10,
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

TX開業前の2004年度は、転出者が転入者を1,328人上回る転出超過でした。2005年度に転入と転出がほぼ同じになり、2006年度から転入超過になっています。2つの線の間にある青い面が、その年度の転入超過の人数です。

転入超過は2018年度の4,121人が最も多く、その後は減っています。2022年度は3,331人、2023年度は1,985人、2024年度は1,423人で、2024年度は2018年度のおよそ3分の1です。転入の減少と転出の増加の両方が起きており、転入者は2022年度の11,550人から2023年度に9,974人へ減り、2024年度は10,026人とほぼ同じでした。転出者は同じ期間に8,219人から8,603人へ増えています。

## 出生数も2018年度の2,082人が最も多い

出生数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "births"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#ec4899"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
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
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ]
}
```

流山市の出生数は、2005年度の1,271人から2018年度の2,082人へ64%増えました。2019年度から2022年度は2,019人から2,079人の間で推移し、2023年度は1,991人と2,000人を下回っています。転入超過が最も多かったのも2018年度です。出生数のデータは2023年度までで、転入超過より1年短くなっています。今後の保育や学校の需要を見積もるときは、総人口ではなく出生数の推移を使う必要があります。

### 15歳未満人口は2005年度から2020年度に55%増えた

年齢3区分の人口の推移です。この3つの値は国勢調査をもとにした5年ごとの値なので、最新は2020年度で、2021年度以降の変化は含まれていません。

```chart
{
  "layer": [
    {
      "data": {"name": "age_under15"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "population", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "population",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（人）", "grid": true}
        },
        "color": {
          "datum": "15歳未満",
          "type": "nominal",
          "scale": {
            "domain": ["15歳未満", "15〜64歳", "65歳以上"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "age_working"},
      "transform": [
        {"lookup": "year", "from": {"data": {"name": "age_under15"}, "key": "year", "fields": ["population"]}, "as": ["__b0"]},
        {"calculate": "datum.__b0", "as": "__below"},
        {"calculate": "datum.__below + datum.population", "as": "__top"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "population", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__top",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（人）", "grid": true}
        },
        "y2": {"field": "__below"},
        "color": {
          "datum": "15〜64歳",
          "type": "nominal",
          "scale": {
            "domain": ["15歳未満", "15〜64歳", "65歳以上"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "age_over65"},
      "transform": [
        {"lookup": "year", "from": {"data": {"name": "age_under15"}, "key": "year", "fields": ["population"]}, "as": ["__b0"]},
        {"lookup": "year", "from": {"data": {"name": "age_working"}, "key": "year", "fields": ["population"]}, "as": ["__b1"]},
        {"calculate": "datum.__b0 + datum.__b1", "as": "__below"},
        {"calculate": "datum.__below + datum.population", "as": "__top"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "population", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__top",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（人）", "grid": true}
        },
        "y2": {"field": "__below"},
        "color": {
          "datum": "65歳以上",
          "type": "nominal",
          "scale": {
            "domain": ["15歳未満", "15〜64歳", "65歳以上"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        }
      }
    }
  ]
}
```

15歳未満人口（緑色）は2005年度の20,081人から2020年度の31,172人へ55%増えています。生産年齢人口（15〜64歳）も106,157人から118,860人へ増えており、子育て世代の転入が年齢構成に表れています。

## 保育所等は2000年度の13箇所から2017年度の38箇所に増えた

保育所等の数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "nurseries"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"nurseries\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#8b5cf6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#8b5cf6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "nurseries", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "nurseries",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "保育所等数", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
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
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ]
}
```

保育所等は1981年度から2000年度まで13箇所で変わらず、2000年代に入って増え始め、2017年度には38箇所になりました。このデータは2017年度までで、2018年度以降は同じ定義の値がありません。

在所児数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "enrolled"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"enrolled\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#8b5cf6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#8b5cf6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "enrolled", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "enrolled",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "保育所等在所児数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
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
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ]
}
```

在所児数は1990年度の897人から2017年度の4,193人へ、約4.7倍になりました。保育所の整備と同じ時期に、在所児数も増えています。

## 小学校児童数は2024年度に14,205人で、1980年度以降で最も多い

小学校の児童数の推移です。灰色の点線は1982年度の水準です。

```chart
{
  "layer": [
    {
      "data": {"name": "students"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"students\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#16a34a",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#16a34a"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "students", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "students",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "小学校児童数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 14042, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 10,
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 10,
        "color": "#94a3b8"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "y": {"datum": 14042, "type": "quantitative"},
        "text": {"value": "1982年度 14,042人"}
      }
    }
  ]
}
```

児童数は、団塊ジュニア世代が通っていた1982年度の14,042人から減り続け、2004年度には7,924人と4割以上減りました。そこから増え、2024年度は14,205人です。1982年度を163人上回り、データが始まる1980年度以降で最も多くなりました。2004年度からは79%増えています。

転入超過が減っても児童数が増えているのは、すでに転入した世帯の子どもが順に小学校に入学しているためです。今後の学級数や校舎の必要量は、転入超過ではなく、2018年度から増えていない出生数をもとに見積もる必要があります。

## 着工新設住宅は2015年度の3,322戸が最も多く、2024年度はその6割程度

着工新設住宅の戸数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "housing"},
      "mark": {"type": "bar", "color": "#f59e0b"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "houses", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "houses",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工新設住宅（戸）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "ordinal"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

TX開業の2005年度に2,789戸が着工され、その後も着工が続いています。最も多いのは2015年度の3,322戸で、2019年度も3,250戸でした。2022年度は1,705戸、2023年度は1,902戸、2024年度は2,127戸で、2015年度の5割から6割の水準です。転入超過が減った時期と重なっています。

## 通勤・通学先は他県が最も多く、2020年度は40,374人

通勤・通学先別の人数です。この3つの値は国勢調査をもとにしており、市内の値が2010年度から収録されているので、2010年度と2020年度を比較しました。

```chart
{
  "layer": [
    {
      "data": {"name": "commute_local"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "commuters", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "commuters",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "通勤・通学者数（人）", "grid": true}
        },
        "color": {
          "datum": "市内",
          "type": "nominal",
          "scale": {
            "domain": ["市内", "県内他市", "他県（主に東京）"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "commute_pref"},
      "transform": [
        {"lookup": "year", "from": {"data": {"name": "commute_local"}, "key": "year", "fields": ["commuters"]}, "as": ["__b0"]},
        {"calculate": "datum.__b0", "as": "__below"},
        {"calculate": "datum.__below + datum.commuters", "as": "__top"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "commuters", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__top",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "通勤・通学者数（人）", "grid": true}
        },
        "y2": {"field": "__below"},
        "color": {
          "datum": "県内他市",
          "type": "nominal",
          "scale": {
            "domain": ["市内", "県内他市", "他県（主に東京）"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "commute_other"},
      "transform": [
        {"lookup": "year", "from": {"data": {"name": "commute_local"}, "key": "year", "fields": ["commuters"]}, "as": ["__b0"]},
        {"lookup": "year", "from": {"data": {"name": "commute_pref"}, "key": "year", "fields": ["commuters"]}, "as": ["__b1"]},
        {"calculate": "datum.__b0 + datum.__b1", "as": "__below"},
        {"calculate": "datum.__below + datum.commuters", "as": "__top"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "commuters", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__top",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "通勤・通学者数（人）", "grid": true}
        },
        "y2": {"field": "__below"},
        "color": {
          "datum": "他県（主に東京）",
          "type": "nominal",
          "scale": {
            "domain": ["市内", "県内他市", "他県（主に東京）"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        }
      }
    }
  ]
}
```

他県（主に東京）への通勤・通学者が最も多く、2020年度は40,374人です。県内の他市は25,066人、市内は19,847人でした。2010年度からの10年で増えたのは他県（35,135人から40,374人）と市内（16,980人から19,847人）で、県内の他市はほぼ横ばいです。流山市に住む人の通勤・通学先は、東京を中心とする他県が最も多くなっています。

## 地方税収は63%、児童福祉費は6.8倍に増えた

児童福祉費と地方税収の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "fiscal"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tax_revenue\"]) ? 0 : 1",
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
          {"field": "tax_revenue", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "tax_revenue",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "金額（億円）", "grid": true}
        },
        "color": {
          "datum": "地方税収",
          "type": "nominal",
          "scale": {"domain": ["地方税収", "児童福祉費"], "range": ["#2563eb", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "fiscal"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"child_welfare\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "child_welfare", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "child_welfare",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "金額（億円）", "grid": true}
        },
        "color": {
          "datum": "児童福祉費",
          "type": "nominal",
          "scale": {"domain": ["地方税収", "児童福祉費"], "range": ["#2563eb", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
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
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ]
}
```

地方税収（青）は、2005年度の190.3億円から2021年度の310.1億円へ63%増えました。人口が増えたことで、住民税と固定資産税が増えたと考えられます。

児童福祉費（ピンク）は、同じ期間に34.3億円から232.8億円へ6.8倍になりました。2009年度の46.3億円から2010年度の70.4億円へ、1年で52%増えています。2010年度は子ども手当が創設された年度なので、6.8倍には市の施策以外の要因も含まれます。この2つの値は2021年度までで、転入超過が減った2023年度以降は含まれていません。

## まとめ

- 人口は2005年度の153,026人から2024年度の208,455人へ約36%増えました。2005年度を100とした2024年度の指数は、流山市が136.2、柏市が112.2、船橋市が109.8、松戸市が101.6、野田市が97.2です
- 転入超過は2018年度の4,121人が最も多く、2024年度は1,423人です。2022年度と比較すると、転入が11,550人から10,026人へ減り、転出が8,219人から8,603人へ増えました
- 出生数も2018年度の2,082人が最も多く、2019年度以降は増えていません。2023年度は1,991人で、2,000人を下回りました
- 小学校児童数は2024年度に14,205人になり、1982年度の14,042人を上回って、1980年度以降で最も多くなりました
- 児童福祉費は2005年度の34.3億円から2021年度の232.8億円へ6.8倍になりました。子ども手当が始まった2010年度に52%増えており、市の施策だけによる増加ではありません。同じ期間の地方税収は63%増えました

流山市では、転入超過と出生数は2018年度が最も多く、小学校児童数は2024年度に最も多くなりました。人口が増えている自治体で施設や学級の必要量を見積もるときは、総人口ではなく、転入超過・出生数・児童数のそれぞれが増えているか減っているかを確認する必要があります。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別データを 2026-08-16 時点で集計しています。流山市は標準地域コード `12220` で抽出しました。人口（`A2101`）・転入者数（`A5101`）・転出者数（`A5102`）・出生数（`A4101`）の元データは総務省の[住民基本台帳に基づく人口、人口動態及び世帯数調査](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)、年齢3区分（`A1301`〜`A1303`）と通勤・通学先（`H7302`〜`H7304`）は国勢調査です。ほかに保育所等数（`J2503`）・在所児数（`J2506`）・小学校児童数（`E2501`）・着工新設住宅（`H1800`）・児童福祉費（`D3203033`）・地方税（`D320101`）を使っています。数値はいずれも年度の値で、近隣市との比較は2005年度の住民基本台帳人口を100とする指数に統一しています。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[市区町村別の人口統計データ](/datasets/queria/e_stat/ssds/a_municipal_population)から、自分の自治体や比較したい都市の推移を同じ指標で確認できます。

```sql id=population
SELECT year, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_municipal_population WHERE area = '12220' AND cat01 = 'A2101' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024 ORDER BY year
```

```sql id=idx_nagareyama
WITH base AS ( SELECT TRY_CAST(value AS DOUBLE) AS base_pop FROM e_stat.ssds.a_municipal_population WHERE area = '12220' AND cat01 = 'A2101' AND time_name = '2005年度' ) SELECT TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) AS year, ROUND(TRY_CAST(p.value AS DOUBLE) / b.base_pop * 100, 1) AS pop_index FROM e_stat.ssds.a_municipal_population p, base b WHERE p.area = '12220' AND p.cat01 = 'A2101' AND TRY_CAST(p.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) <= 2024 ORDER BY year
```

```sql id=idx_kashiwa
WITH base AS ( SELECT TRY_CAST(value AS DOUBLE) AS base_pop FROM e_stat.ssds.a_municipal_population WHERE area = '12217' AND cat01 = 'A2101' AND time_name = '2005年度' ) SELECT TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) AS year, ROUND(TRY_CAST(p.value AS DOUBLE) / b.base_pop * 100, 1) AS pop_index FROM e_stat.ssds.a_municipal_population p, base b WHERE p.area = '12217' AND p.cat01 = 'A2101' AND TRY_CAST(p.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) <= 2024 ORDER BY year
```

```sql id=idx_matsudo
WITH base AS ( SELECT TRY_CAST(value AS DOUBLE) AS base_pop FROM e_stat.ssds.a_municipal_population WHERE area = '12207' AND cat01 = 'A2101' AND time_name = '2005年度' ) SELECT TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) AS year, ROUND(TRY_CAST(p.value AS DOUBLE) / b.base_pop * 100, 1) AS pop_index FROM e_stat.ssds.a_municipal_population p, base b WHERE p.area = '12207' AND p.cat01 = 'A2101' AND TRY_CAST(p.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) <= 2024 ORDER BY year
```

```sql id=idx_funabashi
WITH base AS ( SELECT TRY_CAST(value AS DOUBLE) AS base_pop FROM e_stat.ssds.a_municipal_population WHERE area = '12204' AND cat01 = 'A2101' AND time_name = '2005年度' ) SELECT TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) AS year, ROUND(TRY_CAST(p.value AS DOUBLE) / b.base_pop * 100, 1) AS pop_index FROM e_stat.ssds.a_municipal_population p, base b WHERE p.area = '12204' AND p.cat01 = 'A2101' AND TRY_CAST(p.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) <= 2024 ORDER BY year
```

```sql id=idx_noda
WITH base AS ( SELECT TRY_CAST(value AS DOUBLE) AS base_pop FROM e_stat.ssds.a_municipal_population WHERE area = '12208' AND cat01 = 'A2101' AND time_name = '2005年度' ) SELECT TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) AS year, ROUND(TRY_CAST(p.value AS DOUBLE) / b.base_pop * 100, 1) AS pop_index FROM e_stat.ssds.a_municipal_population p, base b WHERE p.area = '12208' AND p.cat01 = 'A2101' AND TRY_CAST(p.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(p.time_name, '(\d{4})', 1) AS INTEGER) <= 2024 ORDER BY year
```

```sql id=migration
SELECT TRY_CAST(regexp_extract(t1.time_name, '(\d{4})', 1) AS INTEGER) AS year, TRY_CAST(t1.value AS DOUBLE) AS transfers_in, TRY_CAST(t2.value AS DOUBLE) AS transfers_out, TRY_CAST(t1.value AS DOUBLE) - TRY_CAST(t2.value AS DOUBLE) AS net_migration FROM e_stat.ssds.a_municipal_population t1 JOIN e_stat.ssds.a_municipal_population t2 ON t1.time_name = t2.time_name AND t1.area = t2.area WHERE t1.area = '12220' AND t1.cat01 = 'A5101' AND t2.cat01 = 'A5102' AND TRY_CAST(t1.value AS DOUBLE) IS NOT NULL AND TRY_CAST(t2.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(t1.time_name, '(\d{4})', 1) AS INTEGER) <= 2024 ORDER BY year
```

```sql id=births
SELECT year, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_municipal_population WHERE area = '12220' AND cat01 = 'A4101' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=age_under15
SELECT year, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_municipal_population WHERE area = '12220' AND cat01 = 'A1301' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2020 ORDER BY year
```

```sql id=age_working
SELECT year, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_municipal_population WHERE area = '12220' AND cat01 = 'A1302' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2020 ORDER BY year
```

```sql id=age_over65
SELECT year, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_municipal_population WHERE area = '12220' AND cat01 = 'A1303' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2020 ORDER BY year
```

```sql id=nurseries
SELECT year, TRY_CAST(value AS DOUBLE) AS nurseries FROM e_stat.ssds.j_municipal_welfare WHERE area = '12220' AND cat01 = 'J2503' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2017 ORDER BY year
```

```sql id=enrolled
SELECT year, TRY_CAST(value AS DOUBLE) AS enrolled FROM e_stat.ssds.j_municipal_welfare WHERE area = '12220' AND cat01 = 'J2506' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2017 ORDER BY year
```

```sql id=students
SELECT year, TRY_CAST(value AS DOUBLE) AS students FROM e_stat.ssds.e_municipal_education WHERE area = '12220' AND cat01 = 'E2501' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024 ORDER BY year
```

```sql id=housing
SELECT year, TRY_CAST(value AS DOUBLE) AS houses FROM e_stat.ssds.h_municipal_housing WHERE area = '12220' AND cat01 = 'H1800' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024 ORDER BY year
```

```sql id=commute_local
SELECT year, TRY_CAST(value AS DOUBLE) AS commuters FROM e_stat.ssds.h_municipal_housing WHERE area = '12220' AND cat01 = 'H7302' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2020 ORDER BY year
```

```sql id=commute_pref
SELECT year, TRY_CAST(value AS DOUBLE) AS commuters FROM e_stat.ssds.h_municipal_housing WHERE area = '12220' AND cat01 = 'H7303' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2010 AND 2020 ORDER BY year
```

```sql id=commute_other
SELECT year, TRY_CAST(value AS DOUBLE) AS commuters FROM e_stat.ssds.h_municipal_housing WHERE area = '12220' AND cat01 = 'H7304' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2010 AND 2020 ORDER BY year
```

```sql id=fiscal
SELECT TRY_CAST(regexp_extract(t1.time_name, '(\d{4})', 1) AS INTEGER) AS year, ROUND(TRY_CAST(t1.value AS DOUBLE) / 100000, 1) AS child_welfare, ROUND(TRY_CAST(t2.value AS DOUBLE) / 100000, 1) AS tax_revenue FROM e_stat.ssds.d_municipal_administration t1 JOIN e_stat.ssds.d_municipal_administration t2 ON t1.time_name = t2.time_name AND t1.area = t2.area WHERE t1.area = '12220' AND t1.cat01 = 'D3203033' AND t2.cat01 = 'D320101' AND TRY_CAST(t1.value AS DOUBLE) IS NOT NULL AND TRY_CAST(t2.value AS DOUBLE) IS NOT NULL AND TRY_CAST(regexp_extract(t1.time_name, '(\d{4})', 1) AS INTEGER) <= 2021 ORDER BY year
```
