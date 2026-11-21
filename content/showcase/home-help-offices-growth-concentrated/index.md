---
title: 訪問介護の事業所の増加の72%は大阪など5府県で、東京とほかの41道県では要介護の人の伸びに届かない
description: 2013〜24年に増えた訪問介護の事業所4,503の72.0%は大阪など5府県です。東京都と残る41道県の合計では、事業所の伸びが要介護の人の伸びを下回ります。
publishedAt: 2026-11-07
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 訪問介護
  - 訪問看護
  - 要介護認定
  - 介護保険事業計画
  - 介護サービス施設・事業所調査
datasets:
  - queria/e_stat
sources:
  - title: 介護サービス施設・事業所調査
    url: https://www.mhlw.go.jp/toukei/list/24-22-2.html
    publisher: 厚生労働省
  - title: 令和6（2024）年介護サービス施設・事業所調査の概況
    url: https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/service24/index.html
    publisher: 厚生労働省
  - title: 介護保険事業状況報告
    url: https://www.mhlw.go.jp/toukei/list/84-1.html
    publisher: 厚生労働省
agentHint: 自分の県の訪問介護と訪問看護ステーションの事業所数を2013年から2024年まで並べて、要介護1〜5の認定者数を事業所数で割った値の推移を出して。全国と大阪府も並べて
socialAnnounce: |-
  11年で増えた訪問介護の事業所4,503の72%は大阪など5府県。東京都と残る41道県の合計では事業所の伸びが要介護者の伸びを下回ります。

  介護保険事業計画に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

訪問介護の事業所は、2013年の32,761から2024年の37,264へ全国で4,503増えました。増えた4,503のうち3,240、72.0%は大阪府・愛知県・神奈川県・京都府・千葉県の5府県の分です。[介護保険事業状況報告](https://www.mhlw.go.jp/toukei/list/84-1.html)の要介護の人（要介護1〜5の認定を受けた人）と並べると、要介護の人は東京都で27.8%、残る41道県の合計で15.8%増えたのに対し、訪問介護の事業所の増加はそれぞれ4.6%、5.5%です。

事業所数は厚生労働省の[介護サービス施設・事業所調査](https://www.mhlw.go.jp/toukei/list/24-22-2.html)の値です。都道府県や市町村で介護保険事業（支援）計画を作る担当者は、これから必要になる訪問介護の量を見込み、それを提供する事業所が地域にあるかを確認します。この記事の数字は、その確認に使えます。

## 5府県の事業所は34.7%増え、東京都は4.6%、ほかの41道県は5.5%

介護サービス施設・事業所調査は、毎年10月1日現在で活動中の介護サービスの事業所を集計する統計です。Queria の[介護サービス事業所数のテーブル](/datasets/queria/e_stat/kaigo_service/service_establishment)は、居宅サービスや地域密着型サービスの事業所数を、都道府県ごと・サービスの種類ごとに2013年から2024年まで収録しています。この記事では次の2つを使います。

| サービスの種類（`service_type`） | 内容                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| 訪問介護                         | ホームヘルパーが自宅を訪ね、入浴・排せつ・食事・家事を手伝う |
| 訪問看護ステーション             | 看護師などが自宅を訪ね、医師の指示で療養上の世話や処置をする |

都道府県の行（`area_kind = 'prefecture'`）を合計すると全国の値になり、2024年の訪問介護 37,264 は厚生労働省の[令和6年の概況](https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/service24/index.html)の数と一致します。

2013年から2024年に訪問介護の事業所が増えた数の多い順に、上位5府県（大阪府・愛知県・神奈川県・京都府・千葉県）、東京都、ほかの41道県の3つに分け、2013年を100として事業所数の推移を並べました。

```chart caption="訪問介護の事業所数（2013年=100、各年10月1日現在）"
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"help_index_top5\"]) ? 0 : 1",
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
          {"field": "help_top5", "type": "quantitative"},
          {"field": "year", "type": "quantitative"},
          {"field": "help_index_top5", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "help_index_top5",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2013年=100", "grid": true}
        },
        "color": {
          "datum": "大阪など5府県",
          "type": "nominal",
          "scale": {
            "domain": ["大阪など5府県", "東京都", "ほかの41道県"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"help_index_tokyo\"]) ? 0 : 1",
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
          {"field": "help_tokyo", "type": "quantitative"},
          {"field": "year", "type": "quantitative"},
          {"field": "help_index_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "help_index_tokyo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2013年=100", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["大阪など5府県", "東京都", "ほかの41道県"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"help_index_other\"]) ? 0 : 1",
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
          {"field": "help_other", "type": "quantitative"},
          {"field": "year", "type": "quantitative"},
          {"field": "help_index_other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "help_index_other",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2013年=100", "grid": true}
        },
        "color": {
          "datum": "ほかの41道県",
          "type": "nominal",
          "scale": {
            "domain": ["大阪など5府県", "東京都", "ほかの41道県"],
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

大阪など5府県の事業所は、2013年の9,345から2024年の12,585へ34.7%増えました。東京都は3,121から3,265へ4.6%、ほかの41道県は合わせて20,295から21,414へ5.5%の増加です。5府県は2013年の時点で全国の事業所の28.5%を持っていましたが、増えた分では72.0%を占めています。大阪府1府だけで1,499増え、全国の増加の33.3%にあたります。全国の合計で見ても、2013年から2024年に事業所は13.7%増え、要介護の人の21.3%増に届いていません。

増えた4,503を、都道府県ごとに分けたのが下の図です。

```chart caption="訪問介護の事業所数の増減の内訳（2013年→2024年）"
{
  "data": {"name": "decomp"},
  "transform": [
    {"window": [{"op": "sum", "field": "delta", "as": "cum"}]},
    {"calculate": "datum.measure === 'relative' ? datum.cum - datum.delta : 0", "as": "start"},
    {"calculate": "datum.cum", "as": "end"},
    {
      "calculate": "datum.measure !== 'relative' ? '合計' : datum.delta >= 0 ? '増加' : '減少'",
      "as": "kind"
    },
    {"calculate": "max(datum.start, datum.end)", "as": "top"}
  ],
  "encoding": {
    "x": {
      "field": "item",
      "type": "nominal",
      "sort": null,
      "title": null,
      "axis": {"labelAngle": -30}
    }
  },
  "layer": [
    {
      "mark": {"type": "bar", "clip": true},
      "encoding": {
        "y": {
          "field": "start",
          "type": "quantitative",
          "title": "事業所数",
          "scale": {"domain": [30000, 38500]}
        },
        "y2": {"field": "end"},
        "color": {
          "field": "kind",
          "type": "nominal",
          "legend": null,
          "scale": {"domain": ["増加", "減少", "合計"], "range": ["#ef4444", "#3b82f6", "#64748b"]}
        },
        "tooltip": [{"field": "item", "title": "項目"}, {"field": "label", "title": "事業所数"}]
      }
    },
    {
      "mark": {"type": "text", "dy": -4, "baseline": "bottom", "fontSize": 11},
      "encoding": {"y": {"field": "top", "type": "quantitative"}, "text": {"field": "label"}}
    }
  ]
}
```

5府県以外で事業所が増えたのは東京都を含む28都道県で、合わせて1,551の増加でした。秋田県は2013年と2024年が同じ251で、福島県・福井県・山形県・宮崎県・徳島県・佐賀県・大分県・鹿児島県・長崎県・新潟県・岡山県・山口県・高知県の13県は2013年より減り、減った数は合わせて288です。

## 東京都とほかの41道県では、1事業所あたりの要介護の人が増えた

事業所が増えても、利用する人がそれ以上に増えていれば、1つの事業所が受け持つ人は増えます。[要介護認定者数のテーブル](/datasets/queria/e_stat/kaigo_insurance/certified_persons)から、保険者ごとの要介護1〜5の認定者数を都道府県ごとに合計し、訪問介護の事業所数で割りました。訪問介護は介護保険の要介護の人が使うサービスで、要支援の人の訪問サービスは市町村の総合事業に移っているため、要支援1・2は含めていません。認定者数は年度末（翌年3月末）現在の値で、事業所数（10月1日現在）とは半年ずれています。

```chart caption="訪問介護の1事業所あたりの要介護1〜5の認定者数"
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"per_office_top5\"]) ? 0 : 1",
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
          {"field": "per_office_top5", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "per_office_top5",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1事業所あたりの認定者数（人）", "grid": true}
        },
        "color": {
          "datum": "大阪など5府県",
          "type": "nominal",
          "scale": {
            "domain": ["大阪など5府県", "東京都", "ほかの41道県"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"per_office_tokyo\"]) ? 0 : 1",
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
          {"field": "per_office_tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "per_office_tokyo",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1事業所あたりの認定者数（人）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["大阪など5府県", "東京都", "ほかの41道県"],
            "range": ["#ef4444", "#3b82f6", "#64748b"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"per_office_other\"]) ? 0 : 1",
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
          {"field": "per_office_other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "per_office_other",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1事業所あたりの認定者数（人）", "grid": true}
        },
        "color": {
          "datum": "ほかの41道県",
          "type": "nominal",
          "scale": {
            "domain": ["大阪など5府県", "東京都", "ほかの41道県"],
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

大阪など5府県では、要介護の人が2013年度の993,017人から2024年度の1,337,553人へ34.7%増え、事業所も同じ34.7%増えたので、1事業所あたりの認定者数は2013年も2024年も106.3人で、その間の年も104〜111人です。東京都では要介護の人が27.8%増えて1事業所あたり120.9人から147.6人に、ほかの41道県では15.8%増えて140.2人から153.8人になりました。5府県が全国の要介護の人の増加に占める割合は38.4%で、事業所の増加に占める72.0%の半分ほどです。

事業所の数は、ヘルパーの人数や訪問できる時間の量を表しません。1事業所あたりの認定者数は、大きな事業所が多い地域でも高くなるので、この値が高いことが事業所の不足を意味するとは限りません。ここで比較しているのは、同じ地域の中で、要介護の人の増え方と事業所の増え方が同じくらいかどうかです。

都道府県ごとに、2013年から2024年の要介護の人の増え方を横軸、訪問介護の事業所の増え方を縦軸に置きました。点線より下にある都道府県は、事業所の増え方が要介護の人の増え方に届いていません。

```chart caption="都道府県別、要介護1〜5の認定者数と訪問介護の事業所数の増減率（2013年→2024年）"
{
  "layer": [
    {
      "data": {"name": "pref_change"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "prefecture_name", "type": "nominal"},
          {"field": "care_change", "type": "quantitative"},
          {"field": "help_change", "type": "quantitative"}
        ],
        "x": {
          "field": "care_change",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "要介護1〜5の認定者数の増減率（%）", "grid": true}
        },
        "y": {
          "field": "help_change",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "訪問介護の事業所数の増減率（%）", "grid": true}
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"datum": -5, "type": "quantitative"},
        "x2": {"datum": 55, "type": "quantitative"},
        "y": {"datum": -5, "type": "quantitative"},
        "y2": {"datum": 55, "type": "quantitative"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

赤が大阪など5府県、青が東京都、灰色がほかの41道県です。47都道府県のうち36で、1事業所あたりの認定者数が2013年より増えました。事業所が2013年より減った13県では、どこも要介護の人が増えています。要介護の人が最も増えたのは埼玉県の49.3%で、事業所は16.6%の増加にとどまります。事業所が最も増えたのは京都府の74.5%です。ほかの41道県のうち、岐阜県・長野県など8県は事業所の伸びが要介護の人の伸びを上回り、残る33道県は下回っています。5府県のうち千葉県と神奈川県は単独で見ると点線より下にあり、5府県の合計で事業所の伸びと要介護の人の伸びが同じになるのは、大阪府・愛知県・京都府の事業所が大きく増えたためです。

## 訪問看護ステーションは、全47都道府県で増えた

同じ調査の訪問看護ステーションは、2013年から2024年に47都道府県のすべてで増えました。3つの地域ごとに、要介護の人、訪問介護、訪問看護ステーションの増え方を並べます。

```chart caption="2013年→2024年の増加率（要介護の人は年度末現在、事業所は10月1日現在）"
{
  "layer": [
    {
      "data": {"name": "growth"},
      "transform": [
        {"fold": ["care_change", "help_change", "nursing_change"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"care_change\": \"要介護1〜5の認定者数\", \"help_change\": \"訪問介護の事業所\", \"nursing_change\": \"訪問看護ステーション\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"care_change\",\"help_change\",\"nursing_change\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "grp",
          "type": "nominal",
          "axis": {"title": null, "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "増加率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["要介護1〜5の認定者数", "訪問介護の事業所", "訪問看護ステーション"],
            "range": ["#94a3b8", "#ef4444", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["要介護1〜5の認定者数", "訪問介護の事業所", "訪問看護ステーション"]},
        "tooltip": [
          {"field": "grp", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

訪問看護ステーションは、大阪など5府県で1,874から5,548へ196.1%、東京都で688から1,717へ149.6%、ほかの41道県で4,591から10,777へ134.7%増えました。どの地域でも要介護の人の増え方を大きく上回っています。東京都とほかの41道県で、要介護の人の伸びに届いていないのは訪問介護の事業所のほうです。

## 計画を作るときに確認すること

- 全国の事業所数は増えていても、増えた分の7割は5府県です。自分の県の訪問介護の事業所数を2013年から並べ、要介護の人の増え方と比較すると、全国の伸びが自分の県に当てはまるかを確認できます
- 2024年の1事業所あたりの認定者数は、2013年と比較して東京都で1.22倍、ほかの41道県の合計で1.10倍です。自分の県で倍率が上がっていれば、事業所1つあたりの受け持ちが増えているので、計画の担当者がヘルパーの人数や訪問回数を事業所に聞き取って確認する理由になります
- 同じテーブルには政令指定都市と中核市の行もあるので、市の単位でも同じ比較ができます

## データの出典

本記事は、厚生労働省の[介護サービス施設・事業所調査](https://www.mhlw.go.jp/toukei/list/24-22-2.html)の都道府県別の事業所数（2013〜2024年、各年10月1日現在）と、[介護保険事業状況報告](https://www.mhlw.go.jp/toukei/list/84-1.html)（年報）の保険者別の要介護認定者数（2013〜2024年度、各年度末現在）を、2026年11月7日時点で集計しています。

Queria は、介護サービス施設・事業所調査と介護保険事業状況報告を、列名と地域の区分を統一し、テーブルと列の説明を付けて公開しています。本記事で使った[介護サービス事業所数のテーブル](/datasets/queria/e_stat/kaigo_service/service_establishment)と[要介護認定者数のテーブル](/datasets/queria/e_stat/kaigo_insurance/certified_persons)から、自分の県や市の訪問介護の事業所と要介護の人の増え方を確認できます。

```sql id=base
-- 都道府県 × 年の、訪問介護・訪問看護ステーションの事業所数と要介護1〜5の認定者数（プロットはしない）
-- 事業所数は各年10月1日現在、認定者数は年度末（翌年3月末）現在で、同じ年の数字を並べる
WITH s AS (
  SELECT prefecture_name, survey_year AS year,
    sum(value) FILTER (WHERE service_type = '訪問介護') AS home_help,
    sum(value) FILTER (WHERE service_type = '訪問看護ステーション') AS home_nursing
  FROM e_stat.kaigo_service.service_establishment
  WHERE area_kind = 'prefecture' AND survey_year BETWEEN 2013 AND 2024
  GROUP BY ALL
), c AS (
  -- 市町村と広域連合の保険者を足すと全国になる
  SELECT prefecture_name, fiscal_year AS year, sum(value) AS care_needed
  FROM e_stat.kaigo_insurance.certified_persons
  WHERE insurer_kind IN ('municipality', 'union') AND insured_category = '総数'
    AND age_group IS NULL
    AND care_level IN ('要介護1', '要介護2', '要介護3', '要介護4', '要介護5')
    AND fiscal_year BETWEEN 2013 AND 2024
  GROUP BY ALL
)
SELECT s.prefecture_name, s.year,
  CAST(s.home_help AS DOUBLE) AS home_help,
  CAST(s.home_nursing AS DOUBLE) AS home_nursing,
  CAST(c.care_needed AS DOUBLE) AS care_needed,
  CASE WHEN s.prefecture_name IN ('大阪府', '愛知県', '神奈川県', '京都府', '千葉県') THEN '大阪など5府県'
       WHEN s.prefecture_name = '東京都' THEN '東京都'
       ELSE 'ほかの41道県' END AS grp
FROM s JOIN c USING (prefecture_name, year)
```

```sql id=top_contributors
-- 2013→2024年に訪問介護の事業所が増えた数の上位（5府県の選び方の根拠。プロットはしない）
SELECT prefecture_name,
  max(home_help) FILTER (WHERE year = 2024) - max(home_help) FILTER (WHERE year = 2013) AS increase
FROM base
GROUP BY 1
ORDER BY increase DESC, prefecture_name
LIMIT 8
```

```sql id=trend
-- 3つの地域ごとの訪問介護の事業所数（2013年=100）と、1事業所あたりの要介護1〜5の認定者数
WITH g AS (
  SELECT year, grp, sum(home_help) AS help, sum(care_needed) AS care
  FROM base GROUP BY ALL
), i AS (
  SELECT year, grp, help, care,
    round(help * 100 / max(help) FILTER (WHERE year = 2013) OVER (PARTITION BY grp), 1) AS help_index,
    round(care / help, 1) AS per_office
  FROM g
)
SELECT year,
  max(help) FILTER (WHERE grp = '大阪など5府県') AS help_top5,
  max(help) FILTER (WHERE grp = '東京都') AS help_tokyo,
  max(help) FILTER (WHERE grp = 'ほかの41道県') AS help_other,
  max(help_index) FILTER (WHERE grp = '大阪など5府県') AS help_index_top5,
  max(help_index) FILTER (WHERE grp = '東京都') AS help_index_tokyo,
  max(help_index) FILTER (WHERE grp = 'ほかの41道県') AS help_index_other,
  max(care) FILTER (WHERE grp = '大阪など5府県') AS care_top5,
  max(care) FILTER (WHERE grp = '東京都') AS care_tokyo,
  max(care) FILTER (WHERE grp = 'ほかの41道県') AS care_other,
  max(per_office) FILTER (WHERE grp = '大阪など5府県') AS per_office_top5,
  max(per_office) FILTER (WHERE grp = '東京都') AS per_office_tokyo,
  max(per_office) FILTER (WHERE grp = 'ほかの41道県') AS per_office_other
FROM i
GROUP BY year
ORDER BY year
```

```sql id=national
-- 全国の訪問介護の事業所数・要介護1〜5の認定者数と、5府県の占める割合（プロットはしない）
WITH w AS (
  SELECT
    sum(home_help) FILTER (WHERE year = 2013) AS help_2013,
    sum(home_help) FILTER (WHERE year = 2024) AS help_2024,
    sum(home_help) FILTER (WHERE year = 2013 AND grp = '大阪など5府県') AS top5_help_2013,
    sum(home_help) FILTER (WHERE year = 2024 AND grp = '大阪など5府県') AS top5_help_2024,
    sum(home_help) FILTER (WHERE year = 2013 AND prefecture_name = '大阪府') AS osaka_help_2013,
    sum(home_help) FILTER (WHERE year = 2024 AND prefecture_name = '大阪府') AS osaka_help_2024,
    sum(care_needed) FILTER (WHERE year = 2013) AS care_2013,
    sum(care_needed) FILTER (WHERE year = 2024) AS care_2024,
    sum(care_needed) FILTER (WHERE year = 2013 AND grp = '大阪など5府県') AS top5_care_2013,
    sum(care_needed) FILTER (WHERE year = 2024 AND grp = '大阪など5府県') AS top5_care_2024
  FROM base
)
SELECT *,
  help_2024 - help_2013 AS help_increase,
  round((help_2024 / help_2013 - 1) * 100, 1) AS help_change,
  round((care_2024 / care_2013 - 1) * 100, 1) AS care_change,
  top5_help_2024 - top5_help_2013 AS top5_help_increase,
  round((top5_help_2024 - top5_help_2013) * 100 / (help_2024 - help_2013), 1) AS top5_share_of_help_increase,
  round(top5_help_2013 * 100 / help_2013, 1) AS top5_share_of_help_2013,
  round((osaka_help_2024 - osaka_help_2013) * 100 / (help_2024 - help_2013), 1) AS osaka_share_of_help_increase,
  round((top5_care_2024 - top5_care_2013) * 100 / (care_2024 - care_2013), 1) AS top5_share_of_care_increase
FROM w
```

```sql id=pref_status
-- 都道府県ごとの2013→2024年の変化と、増えた・変わらない・減ったの数（プロットはしない）
WITH w AS (
  SELECT prefecture_name, grp,
    max(home_help) FILTER (WHERE year = 2013) AS help_2013,
    max(home_help) FILTER (WHERE year = 2024) AS help_2024,
    max(home_nursing) FILTER (WHERE year = 2013) AS nursing_2013,
    max(home_nursing) FILTER (WHERE year = 2024) AS nursing_2024,
    max(care_needed) FILTER (WHERE year = 2013) AS care_2013,
    max(care_needed) FILTER (WHERE year = 2024) AS care_2024
  FROM base GROUP BY ALL
)
SELECT
  count(*) FILTER (WHERE help_2024 > help_2013 AND grp <> '大阪など5府県') AS other_increased,
  sum(help_2024 - help_2013) FILTER (WHERE help_2024 > help_2013 AND grp <> '大阪など5府県') AS other_increase,
  count(*) FILTER (WHERE help_2024 = help_2013) AS unchanged,
  string_agg(prefecture_name, '・') FILTER (WHERE help_2024 = help_2013) AS unchanged_names,
  count(*) FILTER (WHERE help_2024 < help_2013) AS decreased,
  sum(help_2024 - help_2013) FILTER (WHERE help_2024 < help_2013) AS decrease,
  count(*) FILTER (WHERE help_2024 < help_2013 AND care_2024 > care_2013) AS decreased_while_care_increased,
  count(*) FILTER (WHERE care_2024 / help_2024 > care_2013 / help_2013) AS per_office_increased,
  count(*) FILTER (WHERE grp = 'ほかの41道県' AND care_2024 / help_2024 > care_2013 / help_2013) AS other_per_office_increased,
  count(*) FILTER (WHERE grp = 'ほかの41道県' AND care_2024 / help_2024 <= care_2013 / help_2013) AS other_per_office_not_increased,
  string_agg(prefecture_name, '・' ORDER BY prefecture_name) FILTER (WHERE grp = 'ほかの41道県' AND care_2024 / help_2024 <= care_2013 / help_2013) AS other_not_increased_names,
  count(*) FILTER (WHERE nursing_2024 > nursing_2013) AS nursing_increased
FROM w
```

```sql id=decomp
-- 2013→2024年の訪問介護の事業所数の増減を、5府県・ほかに増えた都道県・減った県に分ける
WITH w AS (
  SELECT prefecture_name, grp,
    max(home_help) FILTER (WHERE year = 2013) AS help_2013,
    max(home_help) FILTER (WHERE year = 2024) AS help_2024
  FROM base GROUP BY ALL
), parts AS (
  SELECT 0 AS ord, '2013年' AS item, sum(help_2013) AS delta, 'absolute' AS measure FROM w
  UNION ALL
  SELECT CASE prefecture_name WHEN '大阪府' THEN 1 WHEN '愛知県' THEN 2 WHEN '神奈川県' THEN 3 WHEN '京都府' THEN 4 ELSE 5 END,
    prefecture_name, help_2024 - help_2013, 'relative'
  FROM w WHERE grp = '大阪など5府県'
  UNION ALL
  SELECT 6, 'ほかに増えた' || CAST(count(*) AS VARCHAR) || '都道県', sum(help_2024 - help_2013), 'relative'
  FROM w WHERE grp <> '大阪など5府県' AND help_2024 > help_2013
  UNION ALL
  SELECT 7, '減った' || CAST(count(*) AS VARCHAR) || '県', sum(help_2024 - help_2013), 'relative'
  FROM w WHERE help_2024 < help_2013
  UNION ALL
  SELECT 8, '2024年', 0, 'total'
)
SELECT item, delta, measure,
  CASE WHEN measure = 'absolute' THEN format('{:,}', CAST(delta AS BIGINT))
       WHEN measure = 'total' THEN format('{:,}', CAST((SELECT sum(help_2024) FROM w) AS BIGINT))
       WHEN delta >= 0 THEN '+' || format('{:,}', CAST(delta AS BIGINT))
       ELSE '−' || format('{:,}', CAST(-delta AS BIGINT)) END AS label
FROM parts
ORDER BY ord
```

```sql id=pref_change
-- 都道府県別の2013→2024年の増減率（要介護1〜5の認定者数と訪問介護の事業所数）
WITH w AS (
  SELECT prefecture_name, grp,
    max(home_help) FILTER (WHERE year = 2013) AS help_2013,
    max(home_help) FILTER (WHERE year = 2024) AS help_2024,
    max(care_needed) FILTER (WHERE year = 2013) AS care_2013,
    max(care_needed) FILTER (WHERE year = 2024) AS care_2024
  FROM base GROUP BY ALL
)
SELECT prefecture_name, grp,
  round((care_2024 / care_2013 - 1) * 100, 1) AS care_change,
  round((help_2024 / help_2013 - 1) * 100, 1) AS help_change,
  CASE grp WHEN '大阪など5府県' THEN '#ef4444' WHEN '東京都' THEN '#3b82f6' ELSE '#94a3b8' END AS color
FROM w
ORDER BY care_change DESC, prefecture_name
```

```sql id=growth
-- 3つの地域ごとの2013→2024年の増加率
WITH g AS (
  SELECT grp,
    sum(care_needed) FILTER (WHERE year = 2013) AS care_2013,
    sum(care_needed) FILTER (WHERE year = 2024) AS care_2024,
    sum(home_help) FILTER (WHERE year = 2013) AS help_2013,
    sum(home_help) FILTER (WHERE year = 2024) AS help_2024,
    sum(home_nursing) FILTER (WHERE year = 2013) AS nursing_2013,
    sum(home_nursing) FILTER (WHERE year = 2024) AS nursing_2024
  FROM base GROUP BY grp
)
SELECT grp, care_2013, care_2024, help_2013, help_2024, nursing_2013, nursing_2024,
  round((care_2024 / care_2013 - 1) * 100, 1) AS care_change,
  round((help_2024 / help_2013 - 1) * 100, 1) AS help_change,
  round((nursing_2024 / nursing_2013 - 1) * 100, 1) AS nursing_change
FROM g
ORDER BY CASE grp WHEN '大阪など5府県' THEN 1 WHEN '東京都' THEN 2 ELSE 3 END
```
