---
title: 上場企業のROEの中央値は、情報・通信業の12.8%からパルプ・紙の5.1%まで約2.5倍の差がある
description: EDINETの有価証券報告書データから、上場企業3,541社のROEと自己資本比率を業種別・規模別に比較しました。ROEの中央値は情報・通信業が12.8%で最も高く、パルプ・紙が5.1%で最も低い値です。不動産業は自己資本比率33.4%で12.6%のROEを出しています。
publishedAt: 2026-06-26
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - EDINET
  - 財務
  - ROE
  - 上場企業
datasets:
  - queria/edinet
sources:
  - title: EDINET 書類一覧API
    url: https://disclosure2.edinet-fsa.go.jp/
    publisher: 金融庁
agentHint: 自己資本比率(equity_to_asset_ratio)の業種別中央値を高い順に並べて、直近決算年度の上場企業で。ROEの業種順位と逆になる業種があるか見たい
socialAnnounce: |-
  EDINETの有価証券報告書データから、上場企業のROEと自己資本比率を業種別・規模別に比較しました。

  情報・通信業は稼ぐ力と財務の安全性を両立し、金融や不動産は薄い自己資本で高いROEを出す構造です。

  経営企画のベンチマークや投資先のスクリーニングに。Queriaは行政や公的機関のオープンデータを業務で使える形に整えて公開しています。
---

上場企業3,541社の直近の本決算を業種別に集計すると、ROE（自己資本利益率）の中央値は情報・通信業の12.8%が最も高く、パルプ・紙の5.1%が最も低い値でした。情報・通信業は自己資本比率も63.4%と高く、不動産業はROEが12.6%と高い一方で自己資本比率は33.4%です。売上高の規模別では、1兆円以上の企業のROEが9.4%、100億円未満が8.2%で、規模が大きいほどROEが高く、自己資本比率は低くなります。

東京証券取引所は2023年に「[資本コストや株価を意識した経営](https://www.jpx.co.jp/equities/follow-up/index.html)」を上場企業に要請し、ROEが経営指標として改めて注目されています。ROEの一般的な水準は業種によって大きく違うので、自社のROEを評価するには、業種ごとの中央値と比較する必要があります。この記事では、金融庁の[EDINET](https://disclosure2.edinet-fsa.go.jp/)（電子開示システム）で公開されている有価証券報告書のデータで、上場企業の収益性と財務の安全性を業種別・規模別に比較します。

## 使ったデータ

EDINETから取り込んだ財務サマリーのテーブル（`mart_business_results`）と、提出会社の属性テーブル（`mart_companies`）を使います。財務サマリーには売上高・純利益・ROE・自己資本比率などの主要指標が、属性テーブルには業種区分や上場区分が入っています。2つを提出会社コード（`edinet_code`）で結合して、財務指標を業種別に集計します。

決算期は会社によって違うので、各社の直近の本決算（有価証券報告書の当期）を1社1件取り出し、上場区分が「上場」の企業に絞りました。対象は3,541社で、ROEの中央値は8.7%、自己資本比率の中央値は55.8%です。以下では、極端な値の影響を小さくするため、各指標とも中央値で比較します。

## ROEの中央値は情報・通信業が12.8%で最も高く、パルプ・紙が5.1%で最も低い

所属企業が10社以上ある30業種について、ROEの中央値を並べました。

```chart
{
  "height": 600,
  "layer": [
    {
      "data": {"name": "roe_ind"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "roe", "type": "quantitative"},
          {"field": "industry", "type": "nominal"}
        ],
        "x": {
          "field": "roe",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ROE中央値（%）", "grid": true}
        },
        "y": {
          "field": "industry",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "業種"},
          "sort": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 8.7, "type": "quantitative"},
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
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 8.7, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "全体中央値 8.7%"}
      }
    }
  ]
}
```

最も高いのは情報・通信業の12.8%で、不動産業（12.6%）、サービス業（12.2%）、建設業（10.7%）、その他金融業（9.9%）が続きます。低いのはパルプ・紙（5.1%）、鉄鋼（5.3%）、繊維製品（5.4%）、金属製品（5.5%）です。上位と下位では約2.5倍の差があります。

設備投資の負担が大きい製造業よりも、負担が比較的小さい情報・サービス系の業種でROEが高くなっています。自社のROEを評価するときは、全体の中央値8.7%だけでなく、同じ業種の中央値と比較する必要があります。

## 不動産業は自己資本比率33.4%で、12.6%のROEを出している

ROEは自己資本に対する利益の比率なので、借入を増やして自己資本の割合を下げれば、利益が同じでもROEは高くなります。横軸にROE、縦軸に自己資本比率（総資産に占める自己資本の割合）を取り、業種ごとに並べました。自己資本比率が高いほど財務の安全性が高く、低いほど借入などの負債への依存が大きいことを示します。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "scatter_ind"},
      "mark": {"type": "point", "color": "#7c3aed", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "roe", "type": "quantitative"},
          {"field": "eqr", "type": "quantitative"}
        ],
        "x": {
          "field": "roe",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "ROE中央値（%）", "grid": true}
        },
        "y": {
          "field": "eqr",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "自己資本比率中央値（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scatter_ind"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "roe",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "ROE中央値（%）", "grid": true}
        },
        "y": {
          "field": "eqr",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "自己資本比率中央値（%）", "grid": true}
        },
        "text": {"field": "label"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#cbd5e1", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"datum": 8.7, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#cbd5e1", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 59, "type": "quantitative"}
      }
    }
  ]
}
```

右上にあるのは情報・通信業（ROE12.8%、自己資本比率63.4%）や精密機器（9.3%、66.7%）で、ROEも自己資本比率も高い業種です。不動産業（12.6%、33.4%）は自己資本比率が低く、借入を使って高いROEを出していると考えられます。

左下の銀行業（5.8%、4.9%）は自己資本比率が特に低くなっています。銀行は預金という負債を原資に運用するので、製造業と同じ基準で自己資本比率を評価することはできません。

医薬品（5.9%、65.4%）や繊維製品（5.4%、63.8%）は、自己資本比率が高い一方でROEは低めです。自己資本を利益に結びつける効率には改善の余地があると考えられます。

## 売上高が大きい企業ほどROEが高く、自己資本比率は低い

売上高の規模で企業を4つに分け、ROEと自己資本比率の中央値を比較しました。

```chart
{
  "height": 320,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "size_band"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "band", "type": "nominal"},
              {"field": "roe", "type": "quantitative"}
            ],
            "x": {
              "field": "band",
              "type": "nominal",
              "axis": {"title": "売上高の規模", "labelAngle": 0},
              "sort": ["100億円未満", "100億〜1千億円", "1千億〜1兆円", "1兆円以上"]
            },
            "y": {
              "field": "roe",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "ROE中央値（%）", "grid": true}
            },
            "color": {
              "datum": "ROE中央値",
              "type": "nominal",
              "scale": {"domain": ["ROE中央値", "自己資本比率中央値"], "range": ["#22c55e", "#f97316"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "size_band"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"band\"]) && isValid(datum[\"eqr\"]) ? 0 : 1",
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
              {"field": "band", "type": "nominal"},
              {"field": "eqr", "type": "quantitative"}
            ],
            "x": {
              "field": "band",
              "type": "nominal",
              "axis": {"title": "売上高の規模", "labelAngle": 0},
              "sort": ["100億円未満", "100億〜1千億円", "1千億〜1兆円", "1兆円以上"]
            },
            "y": {
              "field": "eqr",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "自己資本比率中央値（%）", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "自己資本比率中央値",
              "type": "nominal",
              "scale": {"domain": ["ROE中央値", "自己資本比率中央値"], "range": ["#22c55e", "#f97316"]},
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

ROEの中央値は、売上高100億円未満で8.2%、100億〜1千億円で8.7%、1千億〜1兆円で9.0%、1兆円以上で9.4%です。自己資本比率は100億円未満の62.6%から1兆円以上の43.1%まで下がります。規模の大きい企業ほど、借入なども使って利益を伸ばしていると考えられます。

規模の小さい企業は、自己資本比率が高い一方でROEが低い傾向があります。自社のROEが同業の大企業より低い場合も、同じ規模の企業の中央値と比較すると、規模の違いを除いて評価できます。

## 業務での使い方

- 自社のROEや自己資本比率を、同じ業種・同じ規模の企業の中央値と並べて比較する
- 投資先や取引先の候補を評価するときに、業種ごとの中央値を基準にして収益性を比較する
- 中期計画の目標を決めるときに、金融や不動産のように財務構造が違う業種を同じ基準で比較しない

## データの出典

本記事は金融庁の[EDINET](https://disclosure2.edinet-fsa.go.jp/)で公開されている有価証券報告書のデータを、各社の直近の本決算の値で集計しています。決算期は会社ごとに異なります。

Queriaは、EDINETの有価証券報告書の数値を、列名・単位・指標の意味を統一したテーブルにし、テーブルと列の説明を付けて公開しています。本記事で使った[財務サマリーのテーブル](/datasets/queria/edinet/main/mart_business_results)と[提出会社のテーブル](/datasets/queria/edinet/main/mart_companies)から、有価証券報告書を1社ずつ開かずに、自社や関心のある企業の数字を業種・規模別に並べて確認できます。

```sql id=overview
WITH latest AS ( SELECT b.edinet_code, b.net_sales, CAST(b.roe AS DOUBLE) AS roe, CAST(b.equity_to_asset_ratio AS DOUBLE) AS eqr, ROW_NUMBER() OVER (PARTITION BY b.edinet_code ORDER BY b.period_end DESC, b.doc_id DESC) AS rn FROM edinet.main.mart_business_results b WHERE b.year_offset = 0 ), f AS ( SELECT c.industry, l.net_sales, l.roe, l.eqr FROM latest l JOIN edinet.main.mart_companies c USING(edinet_code) WHERE l.rn = 1 AND c.listing_status = '上場' ) SELECT COUNT(*) AS n_companies, ROUND(MEDIAN(roe) * 100, 1) AS roe, ROUND(MEDIAN(eqr) * 100, 1) AS eqr FROM f WHERE roe IS NOT NULL
```

```sql id=roe_ind
WITH latest AS ( SELECT b.edinet_code, b.net_sales, CAST(b.roe AS DOUBLE) AS roe, CAST(b.equity_to_asset_ratio AS DOUBLE) AS eqr, ROW_NUMBER() OVER (PARTITION BY b.edinet_code ORDER BY b.period_end DESC, b.doc_id DESC) AS rn FROM edinet.main.mart_business_results b WHERE b.year_offset = 0 ), f AS ( SELECT c.industry, l.net_sales, l.roe, l.eqr FROM latest l JOIN edinet.main.mart_companies c USING(edinet_code) WHERE l.rn = 1 AND c.listing_status = '上場' ) SELECT industry, ROUND(MEDIAN(roe) * 100, 1) AS roe, COUNT(*) AS n FROM f WHERE roe IS NOT NULL GROUP BY industry HAVING COUNT(*) >= 10 ORDER BY roe ASC, industry
```

```sql id=scatter_ind
WITH latest AS ( SELECT b.edinet_code, b.net_sales, CAST(b.roe AS DOUBLE) AS roe, CAST(b.equity_to_asset_ratio AS DOUBLE) AS eqr, ROW_NUMBER() OVER (PARTITION BY b.edinet_code ORDER BY b.period_end DESC, b.doc_id DESC) AS rn FROM edinet.main.mart_business_results b WHERE b.year_offset = 0 ), f AS ( SELECT c.industry, l.net_sales, l.roe, l.eqr FROM latest l JOIN edinet.main.mart_companies c USING(edinet_code) WHERE l.rn = 1 AND c.listing_status = '上場' ) SELECT industry, ROUND(MEDIAN(roe) * 100, 1) AS roe, ROUND(MEDIAN(eqr) * 100, 1) AS eqr, COUNT(*) AS n, CASE WHEN industry IN ('情報・通信業', '不動産業', '銀行業', '医薬品', '精密機器', '建設業', '小売業', '繊維製品') THEN industry ELSE '' END AS label FROM f WHERE roe IS NOT NULL GROUP BY industry HAVING COUNT(*) >= 10 AND MEDIAN(eqr) IS NOT NULL ORDER BY industry
```

```sql id=size_band
WITH latest AS ( SELECT b.edinet_code, b.net_sales, CAST(b.roe AS DOUBLE) AS roe, CAST(b.equity_to_asset_ratio AS DOUBLE) AS eqr, ROW_NUMBER() OVER (PARTITION BY b.edinet_code ORDER BY b.period_end DESC, b.doc_id DESC) AS rn FROM edinet.main.mart_business_results b WHERE b.year_offset = 0 ), f AS ( SELECT c.industry, l.net_sales, l.roe, l.eqr FROM latest l JOIN edinet.main.mart_companies c USING(edinet_code) WHERE l.rn = 1 AND c.listing_status = '上場' ) SELECT CASE WHEN net_sales >= 1e12 THEN '1兆円以上' WHEN net_sales >= 1e11 THEN '1千億〜1兆円' WHEN net_sales >= 1e10 THEN '100億〜1千億円' ELSE '100億円未満' END AS band, CASE WHEN net_sales >= 1e12 THEN 4 WHEN net_sales >= 1e11 THEN 3 WHEN net_sales >= 1e10 THEN 2 ELSE 1 END AS ord, ROUND(MEDIAN(roe) * 100, 1) AS roe, ROUND(MEDIAN(eqr) * 100, 1) AS eqr, COUNT(*) AS n FROM f WHERE net_sales > 0 AND roe IS NOT NULL GROUP BY band, ord ORDER BY ord
```
