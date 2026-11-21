---
title: サービス産業の活動量は2019年を上回ったが、金融業・保険業は37.0%増え、卸売業は21.3%減った
description: 第3次産業活動指数の直近12か月（2025年8月〜2026年7月）は2019年平均を1.9%上回りました。業種別では金融業・保険業が37.0%増、卸売業は21.3%減で、13業種のうち2019年を上回るのは5業種です。
publishedAt: 2026-07-21
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 経済産業省
  - サービス産業
  - 景気指標
datasets:
  - queria/meti
sources:
  - title: 第3次産業活動指数
    url: https://www.meti.go.jp/statistics/tyo/sanzi/index.html
    publisher: 経済産業省
  - title: 第3次産業活動指数の概要
    url: https://www.meti.go.jp/statistics/tyo/sanzi/gaiyo.html
    publisher: 経済産業省
  - title: 第3次産業活動指数 2020年基準改定の概要
    url: https://www.meti.go.jp/statistics/tyo/sanzi/result/pdf/b2020_ITA_ovvj.pdf
    publisher: 経済産業省
agentHint: 宿泊業・飲食サービス業の季節調整済指数を2018年以降の月次で出して。底がいつで直近どこまで戻ったかを、下がり続ける卸売業と並べて
socialAnnounce: |-
  経済産業省の第3次産業活動指数を103か月分数えました。

  直近12か月の全体は2019年平均を超えましたが、金融業・保険業が37.0%増の一方、卸売業は21.3%減でした。
  Queriaは行政のオープンデータを整えて公開しています。
---

経済産業省の[第3次産業活動指数](https://www.meti.go.jp/statistics/tyo/sanzi/index.html)で、サービス産業全体の直近12か月（2025年8月〜2026年7月）の活動量は、2019年平均を1.9ポイント上回りました。13業種のうち2019年を上回っているのは5業種で、金融業・保険業は37.0%増、情報通信業は17.2%増です。卸売業・小売業は14.5%減で、2021年から4年続けて下がっています。その中でも卸売業は21.3%減、小売業は6.1%減でした。

第3次産業活動指数は、サービス産業の活動量を月次で集計した統計です。全体値は2020年に大きく下がったあと回復しましたが、業種別に分けると、コロナで大きく下がった業種と、いま水準が低い業種は一致しません。以下の数値は、2018年1月から2026年7月までの103か月分の業種別の系列から求めたものです。

## 13業種のウエイトは、卸売業・小売業だけで全体の4分の1近くを占める

第3次産業活動指数は、サービス産業の生産活動量を指数化した統計です。商業動態統計や特定サービス産業動態統計など複数の統計を組み合わせて作られる加工統計で、金額の系列は物価指数で割って実質化されています。そのため、この指数は売上金額ではなく、取引されたモノやサービスの量を表します。値上げで売上が伸びても取扱量が減っていれば、指数は下がります。

Queriaのデータセットには大分類から細かい品目までが収録されています。このうち日本標準産業分類に対応した13業種と、その合計である「第3次産業総合」を使います。経済産業省が主系列としているのは日本標準産業分類を組み替えた10業種で、13業種は参考系列として公表されているものです。各業種には産業規模に応じたウエイトが与えられ、合計が10000になります。ウエイトは全体値を計算するときの重みであると同時に、その業種がサービス産業に占める大きさの目安にもなります。

```sql
WITH j AS (SELECT item_name, weight, year_month, index_value FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND item_code LIKE 'J%' AND item_code <> 'J000000I') SELECT item_name AS 業種, CAST(weight AS INTEGER) AS ウエイト, ROUND(AVG(CASE WHEN year_month BETWEEN '202508' AND '202607' THEN index_value END) / AVG(CASE WHEN year_month BETWEEN '201901' AND '201912' THEN index_value END) * 100 - 100, 1) AS '2019年平均比（%）' FROM j GROUP BY 1, weight ORDER BY weight DESC
```

ウエイトは業種によって大きく異なります。卸売業・小売業だけで全体の4分の1近くを占め、最小の複合サービス事業とは3桁の開きがあります。

## 指数が100になるのは、2020年ではなく2019年と2020年の平均

この統計は「2020年基準」と呼ばれますが、指数が100になるのは2020年ではありません。2020年は感染症の影響で活動が大きく落ち込んだ年のため、[2020年基準改定の概要](https://www.meti.go.jp/statistics/tyo/sanzi/result/pdf/b2020_ITA_ovvj.pdf)で基準時が2019年と2020年の2年平均とされています。

```sql
SELECT item_name AS 業種, ROUND(AVG(CASE WHEN year = 2019 THEN index_value END), 1) AS '2019年平均', ROUND(AVG(CASE WHEN year = 2020 THEN index_value END), 1) AS '2020年平均', ROUND((AVG(CASE WHEN year = 2019 THEN index_value END) + AVG(CASE WHEN year = 2020 THEN index_value END)) / 2, 2) AS '2年平均' FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND (item_code LIKE 'J%' AND item_code <> 'J000000I' OR item_code = 'K1D000000I') GROUP BY 1 ORDER BY 2 DESC
```

どの業種も、2019年と2020年を平均すると100に戻ります。13業種と第3次産業総合のいずれも99.99から100.01の範囲に収まっており、丸めの誤差の範囲で100です。

一方で2019年単独の値は業種によって大きく違い、宿泊業・飲食サービス業は117.3、生活関連サービス業・娯楽業は117.9です。コロナで深く落ちた業種ほど、2020年が基準に含まれる分だけ2019年の値が高く出ます。指数の値をそのまま業種間で比較して「宿泊業は水準が高い」と判断すると誤りになります。

以降の数値は、すべての系列を2019年（暦年）の平均を100として基準化し直した水準です。

## 季節調整済指数の底は2020年5月の83.9で、2026年7月は103.2

このデータには、系列種別（`series_type`）として原指数（`original`）と季節調整済指数（`seasonally_adjusted`）の2つが収録されています。原指数は観測されたままの値で、季節調整済指数はそこから毎年繰り返す季節変動を取り除いた値です。全体値で両者を並べました。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "total_monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"t\"]) && isValid(datum[\"original\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#bfdbfe",
        "strokeWidth": 1,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "t", "type": "quantitative"},
          {"field": "original", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "original",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "原指数",
          "type": "nominal",
          "scale": {"domain": ["原指数", "季節調整済指数"], "range": ["#bfdbfe", "#2563eb"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "total_monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"t\"]) && isValid(datum[\"adjusted\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "t", "type": "quantitative"},
          {"field": "adjusted", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "adjusted",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "季節調整済指数",
          "type": "nominal",
          "scale": {"domain": ["原指数", "季節調整済指数"], "range": ["#bfdbfe", "#2563eb"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

薄い線の原指数は毎月上下に振れており、前月と比較しても、水準が変わったのか季節による変動なのかを判断できません。濃い線の季節調整済指数はこの振れを取り除いてあり、水準の変化だけが残ります。

季節調整済指数で見ると、底は2020年5月の83.9でした。2019年平均より16.1%低い水準です。その後は緩やかに回復し、直近の2026年7月は103.2と、2019年平均を上回っています。

ここで使っている全体値は、業種別の季節調整済指数を加重平均した「第3次産業総合」（`K1D000000I`）で、経済産業省が公表値としている系列です。[統計の概要](https://www.meti.go.jp/statistics/tyo/sanzi/gaiyo.html)のとおり、当月分の公表時に過去3か月分が遡って計算し直され、毎年2月分の公表時には前年の1年分がまとめて補正されます。2026年の各月の値は、まだ確定していません。

季節変動の大きさは業種によってまったく違います。2023年から2025年の月別平均をとり、13業種それぞれの最大と最小の幅を並べます。

```sql
WITH b AS (SELECT item_code, AVG(index_value) AS base FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND year = 2019 GROUP BY 1), m AS (SELECT t.item_name, t.month, AVG(t.index_value / b.base * 100) AS v FROM meti.main.tertiary_industry_activity_index t JOIN b USING (item_code) WHERE t.series_type = 'original' AND t.year BETWEEN 2023 AND 2025 AND t.item_code LIKE 'J%' AND t.item_code <> 'J000000I' GROUP BY 1, 2) SELECT item_name AS 業種, ROUND(MAX(v), 1) AS '月別平均の最大', ROUND(MIN(v), 1) AS '月別平均の最小', ROUND(MAX(v) - MIN(v), 1) AS '幅' FROM m GROUP BY 1 ORDER BY 4 DESC, 1
```

幅が最も大きいのは情報通信業の50.2ポイント、最も小さいのは医療・福祉の8.8ポイントです。この2業種の月別平均を並べます。

```chart
{
  "height": 240,
  "layer": [
    {
      "data": {"name": "seasonal"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"infocomm\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "month", "type": "quantitative"},
          {"field": "infocomm", "type": "quantitative"}
        ],
        "x": {
          "field": "month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "tickMinStep": 1}
        },
        "y": {
          "field": "infocomm",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "情報通信業",
          "type": "nominal",
          "scale": {"domain": ["情報通信業", "医療、福祉"], "range": ["#22c55e", "#7c3aed"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "seasonal"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"health\"]) ? 0 : 1",
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
          {"field": "month", "type": "quantitative"},
          {"field": "health", "type": "quantitative"}
        ],
        "x": {
          "field": "month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "tickMinStep": 1}
        },
        "y": {
          "field": "health",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "医療、福祉",
          "type": "nominal",
          "scale": {"domain": ["情報通信業", "医療、福祉"], "range": ["#22c55e", "#7c3aed"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

情報通信業は3月が148.1と突出し、5月の97.9とは50ポイント以上開きます。6月・9月・12月にも山があり、四半期末の月が高くなる形です。一方の医療・福祉は103.0から111.8の範囲に収まり、季節による振れはほとんどありません。

同じ「前月比プラス」でも、情報通信業の3月と医療・福祉の3月では意味がまったく違います。月次で水準を比較するなら季節調整済指数、1年を通した活動量なら原指数の12か月平均が季節の影響を受けません。以降の業種比較の数値は、原指数の12か月平均です。

## 13業種のうち、2019年の水準を上回るのは5業種

直近12か月（2025年8月〜2026年7月）の平均を、2019年の平均と比較します。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "change_rate"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "item_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2019年平均比（%）", "grid": true}
        },
        "y": {
          "field": "item_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

13業種のうち、2019年の水準を上回っているのは5業種です。金融業・保険業が37.0%増と突出し、情報通信業が17.2%増、その他サービス業が12.7%増、医療・福祉が11.6%増、不動産業・物品賃貸業が2.2%増です。

下側では、学習支援業が19.7%減、複合サービス事業が17.1%減、卸売業・小売業が14.5%減となっています。宿泊業・飲食サービス業は9.6%減、運輸業・郵便業は9.0%減で、いずれもまだ2019年の水準に届いていません。

下位に並ぶ業種の性格は一様ではありません。宿泊業・飲食サービス業は2020年に3割近く落ちた業種ですが、卸売業・小売業の2020年の落ち込みは全体とほぼ同じ程度で、2021年に横ばいとなったあと下がり続けた業種です。

## 卸売業・小売業は2021年から4年続けて下がり、その大半は卸売業

代表的な業種について、2018年からの年平均の推移をたどります。2026年はまだ7か月分なので、年平均は2025年までです。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "yearly"},
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
        "color": "#64748b",
        "strokeWidth": 3,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
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
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "total",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "第3次産業総合",
          "type": "nominal",
          "scale": {
            "domain": ["第3次産業総合", "金融業、保険業", "情報通信業", "卸売業、小売業", "運輸業、郵便業", "宿泊業、飲食サービス業"],
            "range": ["#64748b", "#3b82f6", "#22c55e", "#ef4444", "#7c3aed", "#ec4899"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"finance\"]) ? 0 : 1",
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
          {"field": "finance", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "finance",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "金融業、保険業",
          "type": "nominal",
          "scale": {
            "domain": ["第3次産業総合", "金融業、保険業", "情報通信業", "卸売業、小売業", "運輸業、郵便業", "宿泊業、飲食サービス業"],
            "range": ["#64748b", "#3b82f6", "#22c55e", "#ef4444", "#7c3aed", "#ec4899"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"infocomm\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "infocomm", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "infocomm",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "情報通信業",
          "type": "nominal",
          "scale": {
            "domain": ["第3次産業総合", "金融業、保険業", "情報通信業", "卸売業、小売業", "運輸業、郵便業", "宿泊業、飲食サービス業"],
            "range": ["#64748b", "#3b82f6", "#22c55e", "#ef4444", "#7c3aed", "#ec4899"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"retail\"]) ? 0 : 1",
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
          {"field": "retail", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "retail",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "卸売業、小売業",
          "type": "nominal",
          "scale": {
            "domain": ["第3次産業総合", "金融業、保険業", "情報通信業", "卸売業、小売業", "運輸業、郵便業", "宿泊業、飲食サービス業"],
            "range": ["#64748b", "#3b82f6", "#22c55e", "#ef4444", "#7c3aed", "#ec4899"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"transport\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "transport", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "transport",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "運輸業、郵便業",
          "type": "nominal",
          "scale": {
            "domain": ["第3次産業総合", "金融業、保険業", "情報通信業", "卸売業、小売業", "運輸業、郵便業", "宿泊業、飲食サービス業"],
            "range": ["#64748b", "#3b82f6", "#22c55e", "#ef4444", "#7c3aed", "#ec4899"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"hotel\"]) ? 0 : 1",
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
          {"field": "hotel", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "hotel",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年平均=100", "grid": true}
        },
        "color": {
          "datum": "宿泊業、飲食サービス業",
          "type": "nominal",
          "scale": {
            "domain": ["第3次産業総合", "金融業、保険業", "情報通信業", "卸売業、小売業", "運輸業、郵便業", "宿泊業、飲食サービス業"],
            "range": ["#64748b", "#3b82f6", "#22c55e", "#ef4444", "#7c3aed", "#ec4899"]
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

業種によって、推移は3つに分かれます。

宿泊業・飲食サービス業（ピンク）は2021年に65.0まで落ち、2019年の3分の2以下になりました。その後は毎年上がり、2025年は90.3です。下がり幅は最も大きかったものの、回復が続いています。運輸業・郵便業（紫）も2021年の84.3が底ですが、2023年以降は89.8、90.7、90.9とほぼ横ばいで、回復が止まっています。

卸売業・小売業（赤）は、ほかの2業種と違う推移です。2020年に92.4まで下がったあと、2021年は92.8とほぼ動かず、そこから2022年88.9、2023年87.9、2024年87.1、2025年86.0と、4年続けて下がっています。2018年の100.6から2019年にかけても下がっており、2020年に下がったあとも低下が続いています。

「卸売業、小売業」の大分類の下には、卸売業と小売業が別々の系列として収録されています。2つを分けて、大分類の値と並べました。

```sql
WITH b AS (SELECT item_code, AVG(index_value) AS base FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND year = 2019 GROUP BY 1) SELECT t.item_name AS 業種, ROUND(AVG(CASE WHEN t.year = 2020 THEN t.index_value / b.base * 100 END), 1) AS '2020年', ROUND(AVG(CASE WHEN t.year_month BETWEEN '202508' AND '202607' THEN t.index_value / b.base * 100 END), 1) AS '直近12か月' FROM meti.main.tertiary_industry_activity_index t JOIN b USING (item_code) WHERE t.series_type = 'original' AND t.item_code IN ('K1D000000I', 'JI00000I', 'DD00000I', 'DG00000I') GROUP BY 1 ORDER BY 3
```

低下の大半は卸売業で起きています。卸売業は2019年平均を100として直近12か月が78.7で、21.3%低い水準です。小売業は93.9で6.1%減にとどまります。「卸売業、小売業」の85.5は、動きの違う2つの業種を平均した値です。

小売業は最終消費者への販売、卸売業は企業間の取引です。指数の上では、消費者への販売よりも企業間で取引される量のほうが大きく減っています。卸売業の指数は、商業動態統計の販売額を日本銀行の企業物価指数（輸入物価を含む）で割って作られています（[2020年基準改定の概要](https://www.meti.go.jp/statistics/tyo/sanzi/result/pdf/b2020_ITA_ovvj.pdf)の附表1）。販売額が伸びても、物価指数の上昇がそれを上回れば、指数には物量の減少として出ます。

2019年を上回っている2業種では、金融業・保険業（青）は2020年も100.7とほとんど下がらず、以降は毎年上昇して2025年に126.8まで達しました。情報通信業（緑）は2020年に97.0まで下がったものの2022年には2019年を超え、2025年は115.6です。

このグラフは暦年の平均なので、先ほどの直近12か月（2025年8月〜2026年7月）の数値とは範囲が違います。金融業・保険業は暦年2025年が26.8%増、直近12か月では37.0%増と、暦年2025年より高い水準にあります。

## 全体値を最も押し下げたのは卸売業・小売業の3.49ポイント

業種ごとの変化が全体値をどれだけ動かしたかを分解します。各業種の指数の変化幅にウエイトを掛けて10000で割ると、全体値の変化に対する寄与が求められます。すべての業種の寄与を足し合わせると、全体値の変化幅になります。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "contribution"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "contrib", "type": "quantitative"},
          {"field": "item_name", "type": "nominal"}
        ],
        "x": {
          "field": "contrib",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "全体値への寄与（ポイント）", "grid": true}
        },
        "y": {
          "field": "item_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

全体値は2019年平均を100として直近12か月が101.9で、変化幅は1.9ポイントでした。この内訳を見ると、押し上げ側は金融業・保険業が2.83ポイント、情報通信業が1.95ポイント、医療・福祉が1.33ポイント、その他サービス業が0.97ポイントです。

押し下げ側で最も大きいのは卸売業・小売業の3.49ポイントで、他のすべての押し下げ要因を合計した1.92ポイントより大きくなっています。変化率では学習支援業の19.7%減が最大でしたが、ウエイトが103しかないため寄与は0.21ポイントにとどまります。卸売業・小売業は14.5%減と率では3番目ですが、ウエイト2409を通じて全体値を最も強く押し下げています。

全体値の1.9ポイントの上昇は、押し上げ側の合計7.33ポイントと押し下げ側の合計5.41ポイントの差し引きです。金融業・保険業と情報通信業の2業種だけで4.78ポイントあり、卸売業・小売業の3.49ポイントの押し下げを上回っています。

## まとめ

- 直近12か月の全体値は2019年平均を1.9ポイント上回るが、13業種のうち2019年を上回るのは5業種で、上昇の大半は金融業・保険業と情報通信業によるもの
- 卸売業・小売業は2021年から4年続けて下がり、全体値を3.49ポイント押し下げている。その中身は卸売業の21.3%減で、小売業は6.1%減にとどまる
- 変化率と全体への寄与は順位が一致しない。率で最大の下げの学習支援業は、寄与では0.21ポイントにとどまる

全体値が2019年を1.9ポイント上回る同じ12か月に、卸売業の指数は2019年より21.3%低い水準にあります。企業間の取引に関わる事業者には、全体値の回復はそのまま当てはまりません。

## データの出典

本記事は経済産業省の[第3次産業活動指数](https://www.meti.go.jp/statistics/tyo/sanzi/index.html)（2020年基準）の月次系列を、2026年10月14日時点で集計しています。対象期間は2018年1月から2026年7月までの103か月で、全国値のみです。基準時とウエイト、卸売業のデフレータは[2020年基準改定の概要](https://www.meti.go.jp/statistics/tyo/sanzi/result/pdf/b2020_ITA_ovvj.pdf)、遡及改定と年間補正は[統計の概要](https://www.meti.go.jp/statistics/tyo/sanzi/gaiyo.html)によります。

Queriaは、経済産業省の第3次産業活動指数を、原指数と季節調整済指数を同じテーブルにまとめ、業種コード・業種名・ウエイトを列に持たせた形で公開しています。本記事で使った[第3次産業活動指数のテーブル](/datasets/queria/meti/main/tertiary_industry_activity_index)から、大分類の下にある細かい品目まで降りて、自分の業界に近い系列の動きを確認できます。

```sql id=total_monthly
WITH b AS (SELECT AVG(index_value) AS base FROM meti.main.tertiary_industry_activity_index WHERE item_code = 'K1D000000I' AND series_type = 'original' AND year = 2019) SELECT CAST(t.year AS DOUBLE) + (t.month - 1) / 12.0 AS t, ROUND(MAX(CASE WHEN t.series_type = 'original' THEN t.index_value END) / b.base * 100, 1) AS original, ROUND(MAX(CASE WHEN t.series_type = 'seasonally_adjusted' THEN t.index_value END) / b.base * 100, 1) AS adjusted FROM meti.main.tertiary_industry_activity_index t CROSS JOIN b WHERE t.item_code = 'K1D000000I' GROUP BY 1, b.base ORDER BY 1
```

```sql id=seasonal
WITH b AS (SELECT item_code, AVG(index_value) AS base FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND year = 2019 GROUP BY 1) SELECT t.month, ROUND(AVG(CASE WHEN t.item_code = 'JG00000I' THEN t.index_value / b.base * 100 END), 1) AS infocomm, ROUND(AVG(CASE WHEN t.item_code = 'JP00000I' THEN t.index_value / b.base * 100 END), 1) AS health FROM meti.main.tertiary_industry_activity_index t JOIN b USING (item_code) WHERE t.series_type = 'original' AND t.year BETWEEN 2023 AND 2025 AND t.item_code IN ('JG00000I', 'JP00000I') GROUP BY 1 ORDER BY 1
```

```sql id=change_rate
WITH j AS (SELECT item_name, year_month, index_value FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND item_code LIKE 'J%' AND item_code <> 'J000000I') SELECT item_name, ROUND(AVG(CASE WHEN year_month BETWEEN '202508' AND '202607' THEN index_value END) / AVG(CASE WHEN year_month BETWEEN '201901' AND '201912' THEN index_value END) * 100 - 100, 1) AS pct FROM j GROUP BY 1 ORDER BY pct DESC
```

```sql id=yearly
WITH b AS (SELECT item_code, AVG(index_value) AS base FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND year = 2019 GROUP BY 1) SELECT t.year, ROUND(AVG(CASE WHEN t.item_code = 'K1D000000I' THEN t.index_value / b.base * 100 END), 1) AS total, ROUND(AVG(CASE WHEN t.item_code = 'JI00000I' THEN t.index_value / b.base * 100 END), 1) AS retail, ROUND(AVG(CASE WHEN t.item_code = 'JJ00000I' THEN t.index_value / b.base * 100 END), 1) AS finance, ROUND(AVG(CASE WHEN t.item_code = 'JG00000I' THEN t.index_value / b.base * 100 END), 1) AS infocomm, ROUND(AVG(CASE WHEN t.item_code = 'JH00000I' THEN t.index_value / b.base * 100 END), 1) AS transport, ROUND(AVG(CASE WHEN t.item_code = 'JM00000I' THEN t.index_value / b.base * 100 END), 1) AS hotel FROM meti.main.tertiary_industry_activity_index t JOIN b USING (item_code) WHERE t.series_type = 'original' AND t.year BETWEEN 2018 AND 2025 GROUP BY t.year ORDER BY t.year
```

```sql id=contribution
WITH tb AS (SELECT AVG(index_value) AS base FROM meti.main.tertiary_industry_activity_index WHERE item_code = 'K1D000000I' AND series_type = 'original' AND year = 2019), j AS (SELECT item_name, weight, year_month, index_value FROM meti.main.tertiary_industry_activity_index WHERE series_type = 'original' AND item_code LIKE 'J%' AND item_code <> 'J000000I') SELECT j.item_name, ROUND((AVG(CASE WHEN year_month BETWEEN '202508' AND '202607' THEN index_value END) - AVG(CASE WHEN year_month BETWEEN '201901' AND '201912' THEN index_value END)) * weight / 10000 / tb.base * 100, 2) AS contrib FROM j CROSS JOIN tb GROUP BY j.item_name, weight, tb.base ORDER BY contrib DESC
```
