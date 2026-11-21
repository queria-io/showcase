---
title: 政府調達の落札は件数の75%が最低価格、金額の59%が総合評価
description: 中央省庁の落札総額は2017年度から2025年度に2倍を超え、約1兆3,300億円になりました。2025年度は件数の74.8%が一般競争・最低価格、金額の59.2%が一般競争・総合評価で、落札総額の30.2%を上位10社が占めます。
ogDescription: 中央省庁の2025年度の落札は、件数の74.8%が最低価格、金額の59.2%が総合評価の案件でした。
publishedAt: 2026-07-24
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 政府調達
  - 入札
  - 官公庁ビジネス
datasets:
  - queria/p_portal
sources:
  - title: 調達ポータル（政府電子調達システム GEPS）
    url: https://www.p-portal.go.jp/
    publisher: デジタル庁
agentHint: 特定の府省庁(ministry_name)の落札実績を入札方式別に、2020年度以降の推移で出して。一般競争の最低価格と総合評価で金額の比率がどう変わるかを比べて
socialAnnounce: |-
  中央省庁の落札実績オープンデータを入札方式と落札企業で数えました。

  件数の約75%は価格勝負の一般競争入札ですが、金額の約6割は技術力を競う総合評価に集まります。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

中央省庁の落札総額は、2017年度の約6,200億円から2025年度の約1兆3,300億円へ、8年で2倍を超えました。2025年度の落札の74.8%は価格だけで決まる一般競争・最低価格の案件ですが、金額では価格と技術提案で決まる一般競争・総合評価の案件が59.2%を占めます。落札した企業は9,529社で、落札総額の30.2%は上位10社に集まっています。

使ったのは、政府電子調達システム（GEPS）に登録された落札実績を公開する[調達ポータル](https://www.p-portal.go.jp/)のオープンデータです。1行が1件の落札案件にあたり、落札決定日・落札価格・発注した府省庁・入札方式・落札した事業者（法人番号付き）が記録されています。gBizINFOなどほかの調達データにはない入札方式と、法人番号で名寄せできる落札企業が入っていることが、このデータの特徴です。対象は中央省庁の落札案件で、地方自治体や独立行政法人の調達は含まれません。発注の時期と規模は[別の記事](/showcase/gov-procurement-market)で集計しました。この記事では、受注のしやすさに関係する入札方式と、落札がどの企業に集まっているかを集計します。

## 落札総額は8年で2倍を超えた

落札額の合計の年度ごとの推移です。年度は会計年度（4月〜翌年3月）で、集計途中の2026年度は除き、2017〜2025年度を対象にしています。

```chart
{
  "layer": [
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_oku\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_oku", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "total_oku",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "落札総額（億円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

落札総額は2017年度の約6,200億円から2025年度の約1兆3,300億円へ、2倍を超えました。件数も同じ期間に約2万2千件から約3万4千件に増えています。新規参入を検討する事業者は、市場の規模が伸びていることを前提にできます。落札価格は契約時点の金額で、その後の変更契約は反映されていません。

## 件数の74.8%は最低価格、金額の59.2%は総合評価

2025年度の案件の入札方式を、4つに分けました。「随意契約」は方式名が「随意契約」で始まる案件をまとめたものです。

| 分類               | 内容                                                     |
| ------------------ | -------------------------------------------------------- |
| 一般競争・最低価格 | 公告して広く募り、最も安い価格を提示した者が落札         |
| 一般競争・総合評価 | 価格と技術提案を点数化し、総合点で落札者を決める         |
| 随意契約           | 特定の事業者と直接契約（少額随契・プロポーザル等を含む） |
| その他             | 指名競争入札、最高価格による売却案件など                 |

一般競争入札は公告して広く参加者を募る方式で、新規の事業者も参加できます。総合評価は価格のほかに技術力で点数に差がつく方式で、随意契約は取引実績のある事業者が有利になりやすい方式です。件数の割合と金額の割合を並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "method_share"},
      "transform": [
        {"fold": ["cnt_share", "amt_share"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"cnt_share\": \"件数シェア\", \"amt_share\": \"金額シェア\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"cnt_share\",\"amt_share\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {"field": "method", "type": "nominal", "axis": {"title": "入札方式"}, "sort": null},
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "シェア（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["件数シェア", "金額シェア"], "range": ["#93c5fd", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["金額シェア", "件数シェア"]},
        "tooltip": [
          {"field": "method", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

件数では、2025年度の落札の74.8%が一般競争・最低価格です。金額ではこの方式の割合は37.8%で、件数では16.3%の一般競争・総合評価が金額の59.2%を占めます。件数の多い小〜中規模の調達は価格で決まり、金額の大きい案件は技術提案で決まる総合評価が中心です。随意契約は件数8.3%・金額2.3%で、少額の案件が中心です。

最低価格の案件で受注実績を増やすには価格競争力が必要で、金額の大きい総合評価の案件を受注するには技術提案の質が必要です。自社の強みが価格と技術のどちらにあるかで、応札する案件の種類が変わります。このデータには何社が応札したかが記録されていないので、方式ごとの参入のしやすさは、方式の仕組みからの推測です。

## 上位10社が落札総額の30.2%を占める

落札企業は法人番号で名寄せできるので、同じ企業の複数の落札をまとめて集計できます。2025年度の落札総額を企業別に合計し、上位15社を並べました。法人番号が入っていない案件は、同じ名前の別の事業者を1社として合計しないように除いています。集計は商号（`trade_name`）の単位なので、同じ法人番号でも商号の表記が違えば別の行になります。

```chart
{
  "height": 480,
  "layer": [
    {
      "data": {"name": "top_companies"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "oku", "type": "quantitative"},
          {"field": "trade_name", "type": "nominal"}
        ],
        "x": {
          "field": "oku",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "落札総額（億円）", "grid": true}
        },
        "y": {"field": "trade_name", "type": "nominal", "axis": {"title": "落札企業"}, "sort": null}
      }
    }
  ]
}
```

金額の上位は富士通、日本電気（NEC）、NTTデータなどのIT・システム大手です。2025年度に落札した企業は9,529社で、落札総額の18.4%を上位3社が、30.2%を上位10社が占めます。9,529社は商号の単位で集計した数なので、法人番号で集計すると社数は一致しません。金額の大きい案件は大手に集中していて、件数では9千社を超える企業に分かれているので、多くの案件は中小の事業者が受注していると考えられます。

大型のシステム開発は上位数社が多く受注していて、金額の小さい案件には多くの企業が参入しています。新しく参入する事業者は、自社の規模や強みに合う金額帯と入札方式の案件を選ぶのが現実的です。

## 業務での使い方

- 入札方式の選択: 自社の強み（価格か技術か）に合わせて、最低価格の案件を多く受注するか、総合評価の大型案件に応札するかを判断する
- 発注元の選定: どの府省庁がどの方式でどれくらい発注しているかを集計し、営業の対象を絞り込む
- 競合の把握: 対象の分野で落札実績のある企業を法人番号で検索し、競合の受注規模や多く受注している案件を把握する

案件の中身を示す区分はデータに入っていないので、業種や商材ごとの市場規模を計算するには、案件名から分類する作業が別に必要です。

## データの出典

本記事はデジタル庁が運営する[調達ポータル](https://www.p-portal.go.jp/)の落札実績情報オープンデータを、2026年7月24日時点で取得して集計しています。

Queriaは、調達ポータルのオープンデータを、落札価格・入札方式・府省庁名・落札企業の法人番号を列にして、テーブルと列の説明を付けて公開しています。本記事で使った[落札実績テーブル](/datasets/queria/p_portal/main/procurement_award)から、自社が対象とする分野の発注府省庁や落札企業を集計できます。

```sql id=yearly
SELECT fiscal_year AS year, ROUND(SUM(award_price) / 1e8) AS total_oku, COUNT(*) AS n FROM p_portal.main.procurement_award WHERE fiscal_year <= 2025 GROUP BY fiscal_year ORDER BY fiscal_year
```

```sql id=method_share
WITH g AS (SELECT CASE WHEN bidding_method_name = '一般競争入札・最低価格' THEN '一般競争・最低価格' WHEN bidding_method_name = '一般競争入札・総合評価' THEN '一般競争・総合評価' WHEN bidding_method_name LIKE '随意契約%' THEN '随意契約' ELSE 'その他' END AS method, award_price AS p FROM p_portal.main.procurement_award WHERE fiscal_year = 2025) SELECT method, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS cnt_share, ROUND(SUM(p) * 100.0 / SUM(SUM(p)) OVER (), 1) AS amt_share FROM g GROUP BY method ORDER BY cnt_share DESC
```

```sql id=top_companies
SELECT trade_name, ROUND(SUM(award_price) / 1e8, 1) AS oku FROM p_portal.main.procurement_award WHERE fiscal_year = 2025 AND corporate_number IS NOT NULL AND corporate_number <> '' GROUP BY trade_name ORDER BY oku DESC LIMIT 15
```

```sql id=concentration
WITH f AS (SELECT trade_name, SUM(award_price) AS s FROM p_portal.main.procurement_award WHERE fiscal_year = 2025 AND corporate_number IS NOT NULL AND corporate_number <> '' GROUP BY trade_name), r AS (SELECT s, SUM(s) OVER () AS tot, ROW_NUMBER() OVER (ORDER BY s DESC) AS rn FROM f) SELECT COUNT(*) AS winners, ROUND(SUM(CASE WHEN rn <= 3 THEN s ELSE 0 END) * 100.0 / MAX(tot), 1) AS top3_share, ROUND(SUM(CASE WHEN rn <= 10 THEN s ELSE 0 END) * 100.0 / MAX(tot), 1) AS top10_share FROM r
```
