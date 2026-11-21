---
title: 国の公共調達は3月の契約が8月の4倍、半数は500万円未満
description: gBizINFOの調達実績で、2025年の国の公共調達34,494件を集計しました。3月の契約件数は8月のおよそ4倍で、契約の約半数は500万円未満、国土交通省が全体の24.3%を発注しています。
publishedAt: 2026-06-07
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 公共調達
  - 官公需
  - 入札
  - 中小企業
datasets:
  - queria/gbizinfo
sources:
  - title: gBizINFO（Gビズインフォ）
    url: https://info.gbiz.go.jp/
    publisher: 経済産業省
  - title: 官公需情報ポータルサイト
    url: https://kkj.go.jp/s/
    publisher: 中小企業庁
agentHint: 2025年の契約金額（award_price）の合計を発注機関（org_name）別に集計して、件数ではなく金額規模で見たときに上位に来る機関を出して。1件あたりの平均額も添えて
socialAnnounce: |-
  国の公共調達（調達実績）データを分析しました。

  発注が集中する時期や、中小企業でも狙える契約規模がわかり、官公庁ビジネスへの参入検討に使えます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

国の公共調達の契約は、2025年に34,494件ありました。件数が最も多いのは3月の6,564件で、8月（1,632件）のおよそ4倍です。契約金額は500万円未満が約半数（49.7%）、1,000万円未満が約3分の2（67.1%）で、5億円以上の大型契約は約1%です。発注機関では国土交通省が全体の24.3%を占めます。

使ったのは、[gBizINFO](https://info.gbiz.go.jp/)が公開する「調達（受注）実績」データです。中央省庁等が発注した物品・役務・工事の契約実績で、1行が1契約にあたります。主な項目は発注日（`order_date`）、契約金額（`award_price`）、発注機関（`org_name`）、受注者（`name`）です。gBizINFOに登録された実績を集めたものなので、国の調達のすべてを含むとは限りません。地方自治体の調達や、独立行政法人・国立大学法人などの発注も含まれていません。国の入札・調達情報は[官公需情報ポータルサイト](https://kkj.go.jp/s/)などで公開されていて、官公庁ビジネスへの参入を検討する企業は、この記事の集計で発注の時期・契約規模・発注機関を確認できます。

## 契約件数は3月が最も多く、8月のおよそ4倍

月ごとの契約件数を、2023年から2025年の3年分で重ねました。集計は発注日が1月1日から12月31日までに入る暦年で、会計年度ではありません。

```chart
{
  "layer": [
    {
      "data": {"name": "season_2023"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"mo\"]) && isValid(datum[\"n\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#93c5fd",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "mo", "type": "quantitative"},
          {"field": "n", "type": "quantitative"}
        ],
        "x": {
          "field": "mo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "契約件数（件）", "grid": true}
        },
        "color": {
          "datum": "2023年",
          "type": "nominal",
          "scale": {
            "domain": ["2023年", "2024年", "2025年"],
            "range": ["#93c5fd", "#3b82f6", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "season_2024"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"mo\"]) && isValid(datum[\"n\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "mo", "type": "quantitative"},
          {"field": "n", "type": "quantitative"}
        ],
        "x": {
          "field": "mo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "契約件数（件）", "grid": true}
        },
        "color": {
          "datum": "2024年",
          "type": "nominal",
          "scale": {
            "domain": ["2023年", "2024年", "2025年"],
            "range": ["#93c5fd", "#3b82f6", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "season_2025"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"mo\"]) && isValid(datum[\"n\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "mo", "type": "quantitative"},
          {"field": "n", "type": "quantitative"}
        ],
        "x": {
          "field": "mo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "契約件数（件）", "grid": true}
        },
        "color": {
          "datum": "2025年",
          "type": "nominal",
          "scale": {
            "domain": ["2023年", "2024年", "2025年"],
            "range": ["#93c5fd", "#3b82f6", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

3年とも同じ形です。件数は3月に最も多くなり、2025年は3月が6,564件、4月が5,606件でした。夏は少なく、8月は1,632件です。

この形は、4月に始まり3月に終わる国の会計年度に対応しています。年度末の1〜3月は予算を執行するための発注が増え、特に3月に集中します。4月も新年度予算の執行で件数が多くなります。官公庁向けの営業では、件数で見ると、年度末から年度初め（おおむね1〜4月）に商談と入札参加の人員を多く割り当てるのが合理的です。案件が少ない夏は、資格審査の準備や発注機関との関係づくりに充てる、という年間計画を立てられます。

## 契約の約半数は500万円未満

2025年の契約金額を、規模帯ごとに件数で分けました。金額が0以下の行は除いています。金額が入っていない契約や単価契約が混ざっていて、そのまま最小の規模帯に入れると分布が実際と違ってしまうためです。

```chart
{
  "layer": [
    {
      "data": {"name": "size_band"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "band", "type": "nominal"}, {"field": "n", "type": "quantitative"}],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "契約金額の規模帯", "labelAngle": 0},
          "sort": [
            "100万円未満",
            "100万〜500万円",
            "500万〜1000万円",
            "1000万〜5000万円",
            "5000万〜1億円",
            "1億〜5億円",
            "5億円以上"
          ]
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "契約件数（件）", "grid": true}
        }
      }
    }
  ]
}
```

最も多い規模帯は100万〜500万円で12,478件でした。500万円未満の契約は17,158件で全体の約半数（49.7%）、1,000万円未満まで広げると23,153件で全体の約3分の2（67.1%）です。5億円以上の大型契約は333件で、全体の約1%です。

件数で見ると、国の公共調達の多くは中小企業でも受注できると考えられる規模の契約です。このテーブルには受注者の企業規模が入っていないので、これは契約金額の分布からの推測で、実際の受注者の内訳ではありません。新しく参入する企業は、自社の供給能力に見合った数百万円規模の案件に継続して応札するのが現実的です。

## 国土交通省が全体の24.3%を発注している

2025年の契約件数が多い順に、上位15機関を並べました。発注機関名（`org_name`）には表記のゆれが残っている可能性があり、同じ機関が別の名前で複数行に分かれる場合があります。

```chart
{
  "height": 480,
  "layer": [
    {
      "data": {"name": "agency"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "n", "type": "quantitative"},
          {"field": "org_name", "type": "nominal"}
        ],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "契約件数（件）", "grid": true}
        },
        "y": {
          "field": "org_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "発注機関"},
          "sort": null
        }
      }
    }
  ]
}
```

最も件数が多いのは国土交通省で8,374件、全体の24.3%です。厚生労働省（9.3%）、林野庁（8.8%）、法務省（8.2%）、国税庁（5.6%）が続きます。公共工事や施設管理の多い国土交通省が特に多くなっています。上位15機関の合計は30,917件で全体の89.6%、残りの約1割はほかの機関の発注です。林野庁や海上保安庁のような外局も本省と並んで上位に入っています。

自社の商材が施設・土木系なら国土交通省や林野庁、IT・事務系の役務なら各省庁の本省や、国税庁・法務省のように庁舎や拠点を多く持つ機関、というように、商材に合う発注機関を選べます。発注機関ごとに入札参加資格や調達ポータルでの手続きが必要なので、件数の多い機関から資格を取得すると、応札できる案件の数を早く増やせます。

## まとめ

- 発注は年度末から年度初め（1〜4月、特に3月）に集中し、夏は少ない。2025年は3月が8月のおよそ4倍
- 契約金額は500万円未満が約半数、1,000万円未満が約3分の2を占める
- 発注機関は国土交通省が最多で全体の24.3%。上位15機関で全体の約9割

## データの出典

本記事は [gBizINFO](https://info.gbiz.go.jp/)（経済産業省）が公開する「調達（受注）実績」データを、2026年7月11日時点で取得して集計しています。

Queriaは、gBizINFOをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[国の調達実績テーブル](/datasets/queria/gbizinfo/main/mart_gbizinfo_procurement)から、自社の事業領域を所管する機関の発注件数や時期を確認したり、規模帯を変えて集計したりできます。

```sql id=season_2023
SELECT EXTRACT(month FROM order_date) AS mo, COUNT(*) AS n FROM gbizinfo.main.mart_gbizinfo_procurement WHERE order_date BETWEEN DATE '2023-01-01' AND DATE '2023-12-31' GROUP BY mo ORDER BY mo
```

```sql id=season_2024
SELECT EXTRACT(month FROM order_date) AS mo, COUNT(*) AS n FROM gbizinfo.main.mart_gbizinfo_procurement WHERE order_date BETWEEN DATE '2024-01-01' AND DATE '2024-12-31' GROUP BY mo ORDER BY mo
```

```sql id=season_2025
SELECT EXTRACT(month FROM order_date) AS mo, COUNT(*) AS n FROM gbizinfo.main.mart_gbizinfo_procurement WHERE order_date BETWEEN DATE '2025-01-01' AND DATE '2025-12-31' GROUP BY mo ORDER BY mo
```

```sql id=size_band
WITH b AS (SELECT CASE WHEN award_price < 1000000 THEN '100万円未満' WHEN award_price < 5000000 THEN '100万〜500万円' WHEN award_price < 10000000 THEN '500万〜1000万円' WHEN award_price < 50000000 THEN '1000万〜5000万円' WHEN award_price < 100000000 THEN '5000万〜1億円' WHEN award_price < 500000000 THEN '1億〜5億円' ELSE '5億円以上' END AS band, CASE WHEN award_price < 1000000 THEN 1 WHEN award_price < 5000000 THEN 2 WHEN award_price < 10000000 THEN 3 WHEN award_price < 50000000 THEN 4 WHEN award_price < 100000000 THEN 5 WHEN award_price < 500000000 THEN 6 ELSE 7 END AS ord FROM gbizinfo.main.mart_gbizinfo_procurement WHERE order_date BETWEEN DATE '2025-01-01' AND DATE '2025-12-31' AND award_price > 0) SELECT band, COUNT(*) AS n FROM b GROUP BY band, ord ORDER BY ord
```

```sql id=agency
SELECT org_name, n FROM (SELECT org_name, COUNT(*) AS n FROM gbizinfo.main.mart_gbizinfo_procurement WHERE order_date BETWEEN DATE '2025-01-01' AND DATE '2025-12-31' GROUP BY org_name ORDER BY n DESC LIMIT 15) ORDER BY n ASC
```
