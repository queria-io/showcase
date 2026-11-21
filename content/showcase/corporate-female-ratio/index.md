---
title: 女性従業員比率の平均は、建設業25.1%と医療・福祉70.1%で約2.8倍違う
description: gBizINFOで女性従業員比率を公表している約2万1000社を集計しました。業種別の平均は建設業の25.1%から医療・福祉の70.1%まで約2.8倍の差があり、企業規模別の差は約6ポイントです
publishedAt: 2026-06-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 女性活躍
  - gBizINFO
  - 採用
datasets:
  - queria/gbizinfo
sources:
  - title: gBizINFO（Gビズインフォ）
    url: https://info.gbiz.go.jp/
    publisher: 経済産業省
agentHint: 医療・福祉と建設業について、企業規模（従業員数の区分）別に女性従業員比率の平均を出して。業種内で規模によって差が出るか比べて
socialAnnounce: |-
  gBizINFOが公開する約2万社の女性従業員比率を、業種・企業規模別に集計しました。

  自社の女性比率が同業・同規模と比べて高いか低いかの判断や、女性活躍推進の目標設定に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

gBizINFOで女性従業員比率を公表している約2万1000社を業種別に集計すると、平均は建設業の25.1%から医療・福祉の70.1%まで、約2.8倍の差がありました。企業規模別では従業員50人未満の45.3%から1000人以上の39.2%までで、差は約6ポイントです。自社の女性比率を評価するときは、全国平均より同じ業種の平均と比較するほうが、自社の位置を正確に把握できます。

経済産業省が運営する[gBizINFO](https://info.gbiz.go.jp/)には、女性活躍推進法に基づいて各企業が公表した女性従業員比率が企業ごとに収録されています。この記事では、このデータを業種別・規模別に集計し、人事担当者が目標設定や求人で使える比較の基準を作ります。

## 使用するデータ

gBizINFO の法人活動サマリ（`mart_gbizinfo_company`）を使います。女性従業員比率（`female_ratio`）は、女性活躍推進法に基づく一般事業主行動計画の公表値で、企業が自ら開示した割合（0〜100%）です。算定の基準日や対象範囲（正社員のみか、パート・契約社員を含むか）は企業ごとに異なります。

女性比率を公表している企業は、法人番号が付与された全国の企業のうち約2万社です。女性活躍推進法の公表義務の対象は、当初は「常時雇用する労働者301人以上」の企業で、2022年4月から「101人以上」に広がりました。そのため、このデータは中規模から大規模の企業に偏っており、集計結果は日本企業全体の平均ではなく、開示企業のうちおもに従業員100人以上の企業の値です。

業種は、同じテーブルの事業概要（`business_items`）に含まれる日本標準産業分類の大分類（製造業、建設業など）から取得しています。女性比率が未記入の企業は集計から除いています。まず、開示企業全体の女性比率の分布を集計します。

```chart
{
  "layer": [
    {
      "data": {"name": "dist"},
      "mark": {"type": "bar", "color": "#ec4899"},
      "encoding": {
        "tooltip": [{"field": "band", "type": "nominal"}, {"field": "n", "type": "quantitative"}],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "女性従業員比率", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "企業数（社）", "grid": true}
        }
      }
    }
  ]
}
```

開示企業全体（約2万1000社）の女性比率は、0〜10%から90〜100%まで広く分布しています。企業数が最も多いのは0〜10%の帯（約3000社）で、90〜100%の帯にも約2000社が入っています。中央値は40〜50%の帯にあります。

分布がこれだけ広いので、開示企業全体の分布と比較しても、自社が同じ業種や規模の企業の中でどの位置にいるかは分かりません。次に、業種別に平均を集計します。

## 女性比率の平均は、建設業の25.1%から医療・福祉の70.1%まで約2.8倍の差がある

企業数が100社に満たない業種と、分類不能の産業（分類コード `T`）は除いています。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "industry"},
      "mark": {"type": "bar", "color": "#ec4899"},
      "encoding": {
        "tooltip": [
          {"field": "avg_ratio", "type": "quantitative"},
          {"field": "industry", "type": "nominal"}
        ],
        "x": {
          "field": "avg_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性従業員比率の平均（%）", "grid": true}
        },
        "y": {
          "field": "industry",
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

女性従業員比率の平均が高いのは医療・福祉（70.1%）、生活関連サービス業・娯楽業（55.4%）、教育・学習支援業（53.3%）で、低いのは建設業（25.1%）、運輸業・郵便業（26.1%）、製造業（33.8%）です。

自社の女性比率は、業種平均と比較して評価する必要があります。女性比率35%の製造業の企業は業種平均（33.8%）をわずかに上回りますが、医療・福祉の企業で35%なら業種平均（70.1%）を大きく下回ります。求人で女性活躍を訴求するときも、自社の数字を業種平均と並べて示すと、読み手が高いか低いかを判断できます。

## 企業規模別の差は約6ポイントで、業種別の差より小さい

従業員数が未記入の企業は除いています。

```chart
{
  "layer": [
    {
      "data": {"name": "size"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "size_band", "type": "nominal"},
          {"field": "avg_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "size_band",
          "type": "nominal",
          "axis": {"title": "従業員数", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "avg_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性従業員比率の平均（%）", "grid": true}
        }
      }
    }
  ]
}
```

女性比率は、従業員50人未満の45.3%から1000人以上の39.2%まで、規模が大きいほどやや低くなります。差は約6ポイントで、業種による差（約45ポイント）より小さくなっています。比較の基準を作るときは、規模より業種を優先したほうが、自社の位置を正確に把握できます。

開示企業の約6割は従業員100〜999人の企業です。50人未満と1000人以上の区分は企業数が少ないので、平均の値が数社の値で動きやすくなっています。

## 業務での活用

- 目標設定: 自社の女性比率を、同じ業種・近い規模の開示企業の平均と並べ、引き上げ目標が妥当かを検討する
- 採用での訴求: 自社の数字が業種平均を上回る場合、求人や採用広報で業種平均と並べて示す
- 競合比較: 同業他社の開示値を参照し、採用市場での自社の位置を把握する

## データの出典

本記事は経済産業省の[gBizINFO](https://info.gbiz.go.jp/)が公開する法人活動サマリを、2026年7月11日時点で取得して集計しています。

Queriaは、gBizINFOの法人活動サマリを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[法人活動サマリのテーブル](/datasets/queria/gbizinfo/main/mart_gbizinfo_company)から、自社と同じ業種・規模の企業に絞って女性比率を集計できます。AIに「自社と同じ業種・規模の女性比率を知りたい」と伝えて、条件に合う企業の集計とそのSQLを出してもらうこともできます。手順は[Claude Codeで分析する](https://docs.queria.io/claude-code)ガイドにあります。

```sql id=dist
WITH b AS (SELECT LEAST(FLOOR(female_ratio / 10) * 10, 90)::INT AS lo FROM gbizinfo.main.mart_gbizinfo_company WHERE female_ratio IS NOT NULL) SELECT (lo::VARCHAR || '〜' || (lo + 10)::VARCHAR || '%') AS band, COUNT(*) AS n, lo FROM b GROUP BY lo ORDER BY lo
```

```sql id=industry
SELECT split_part(split_part(business_items, '-', 1), ':', 2) AS industry, ROUND(AVG(female_ratio), 1) AS avg_ratio, COUNT(*) AS n FROM gbizinfo.main.mart_gbizinfo_company WHERE female_ratio IS NOT NULL AND business_items IS NOT NULL AND split_part(business_items, '-', 1) NOT LIKE 'T:%' GROUP BY industry HAVING COUNT(*) >= 100 ORDER BY avg_ratio ASC
```

```sql id=size
SELECT CASE WHEN employee_number < 50 THEN '50人未満' WHEN employee_number < 100 THEN '50〜99人' WHEN employee_number < 300 THEN '100〜299人' WHEN employee_number < 1000 THEN '300〜999人' ELSE '1000人以上' END AS size_band, ROUND(AVG(female_ratio), 1) AS avg_ratio, COUNT(*) AS n, CASE WHEN employee_number < 50 THEN 1 WHEN employee_number < 100 THEN 2 WHEN employee_number < 300 THEN 3 WHEN employee_number < 1000 THEN 4 ELSE 5 END AS ord FROM gbizinfo.main.mart_gbizinfo_company WHERE female_ratio IS NOT NULL AND employee_number IS NOT NULL GROUP BY size_band, ord ORDER BY ord
```
