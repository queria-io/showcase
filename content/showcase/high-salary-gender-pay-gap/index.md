---
title: 平均年収1000万円以上の上場企業133社では、女性の正社員の賃金は男性のおよそ3分の2
description: 上場企業2,802社の有価証券報告書から、平均年収と男女の賃金の差異を比較しました。平均年収1000万円以上の133社では、女性の正社員の賃金は中央値で男性の66.4%でした。
publishedAt: 2026-10-24
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - EDINET
  - 女性活躍
  - 賃金
  - 転職
datasets:
  - queria/edinet
sources:
  - title: EDINET（金融商品取引法に基づく有価証券報告書等の開示書類に関する電子開示システム）
    url: https://disclosure2.edinet-fsa.go.jp/
    publisher: 金融庁
  - title: 「企業内容等の開示に関する内閣府令」等の改正
    url: https://www.fsa.go.jp/news/r4/sonota/20230131/20230131.html
    publisher: 金融庁
  - title: 女性活躍推進法特集ページ
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000091025.html
    publisher: 厚生労働省
agentHint: 平均年間給与(average_annual_salary)が800万円以上の上場企業を、正規雇用労働者の男女の賃金の差異(female_to_male_wage_ratio_regular)が高い順に、業種と会社名つきで並べて
socialAnnounce: |-
  上場企業の平均年収と男女の賃金の差異を並べました。

  平均年収1000万円以上の会社では、女性正社員の賃金は中央値で男性の66.4%です。
  転職先選びの判断材料に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

上場企業2,802社の有価証券報告書を集計すると、平均年収1000万円以上の133社では、女性の正社員の賃金は中央値で男性の66.4%でした。平均年収500万円未満の会社では77.8%で、平均年収が高い会社ほど正社員の男女の差が大きくなります。管理職に占める女性の割合が高い会社ほど、正社員の男女の差は小さくなっています。

転職先を探すときに見る求人票や口コミサイトの平均年収は、男女を合わせた数字です。女性に同じだけ支払われているかは書かれていません。上場企業は2023年3月期から、[有価証券報告書で男女の賃金の差異などを開示することが義務づけられ](https://www.fsa.go.jp/news/r4/sonota/20230131/20230131.html)、従業員の平均年間給与と同じ書類に載せています。金融庁の[EDINET](https://disclosure2.edinet-fsa.go.jp/)で誰でも読めますが、数千社の書類を1社ずつ開いて比較するには大きな手間がかかります。

## 対象は上場企業2,802社で、正社員の男女の賃金の差異の中央値は74.8%

使うのは、EDINET の有価証券報告書から従業員と女性活躍の指標を1書類1行にまとめたテーブル（`mart_human_capital`）と、提出会社の業種や上場区分を持つテーブル（`mart_companies`）です。2つを提出会社コード（`edinet_code`）で結合し、上場している会社について、2025年1月以降に提出した直近の有価証券報告書を1社1件ずつ取り出します。

使う列は次のとおりです。

| 列                                      | 内容                                       |
| --------------------------------------- | ------------------------------------------ |
| `average_annual_salary`                 | 平均年間給与（円、賞与と基準外賃金を含む） |
| `female_to_male_wage_ratio`             | 男女の賃金の差異（全労働者）               |
| `female_to_male_wage_ratio_regular`     | 男女の賃金の差異（正規雇用労働者）         |
| `female_to_male_wage_ratio_non_regular` | 男女の賃金の差異（非正規雇用労働者）       |
| `female_manager_ratio`                  | 管理職に占める女性労働者の割合             |

どの数字も、連結グループではなく有価証券報告書を出した会社単体のものです。持株会社のように本体の従業員が数人しかいない会社は平均年収が役員の水準に近くなるので、本体の従業員が100人以上の会社に絞ります。これで2,802社が残り、平均年間給与の中央値は664万円でした。

男女の賃金の差異は、[女性活躍推進法](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000091025.html)の定めに沿って各社が算出した「男性の平均賃金に対する女性の平均賃金の割合」です。70%なら、女性の賃金は平均して男性の7割という意味で、値が低いほど男女の差が大きいことになります。同じ仕事をした男女の比較ではなく、役職・勤続年数・働く時間の違いがすべて含まれた結果です。全労働者の差異を開示した2,416社の中央値は70.4%、正規雇用労働者（以下、正社員）の差異を開示した2,402社の中央値は74.8%でした。

## 平均年収が高い会社ほど、正社員の男女の差は開く

会社を平均年収の高さで6つに分け、それぞれの男女の賃金の差異の中央値を並べます。平均年収と2つの差異がすべて開示されている2,393社が対象です。

```chart
{
  "height": 320,
  "layer": [
    {
      "data": {"name": "by_band"},
      "transform": [
        {"fold": ["wage_regular", "wage_all"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"wage_regular\": \"正規雇用労働者\", \"wage_all\": \"全労働者\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"wage_regular\",\"wage_all\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "会社の平均年間給与", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [50, 85], "zero": false, "nice": false},
          "axis": {"title": "男性に対する女性の賃金（%、中央値）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["正規雇用労働者", "全労働者"], "range": ["#3b82f6", "#93c5fd"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["正規雇用労働者", "全労働者"]},
        "tooltip": [
          {"field": "band", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    },
    {
      "data": {"name": "by_band"},
      "transform": [
        {"fold": ["wage_regular", "wage_all"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"wage_regular\": \"正規雇用労働者\", \"wage_all\": \"全労働者\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"wage_regular\",\"wage_all\"], datum.__series)", "as": "__order"},
        {
          "calculate": "datum[{\"wage_regular\":\"wage_regular\",\"wage_all\":\"wage_all\"}[datum.__series]]",
          "as": "__text"
        },
        {"filter": "isValid(datum.__text)"}
      ],
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "会社の平均年間給与", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [50, 85], "zero": false, "nice": false},
          "axis": {"title": "男性に対する女性の賃金（%、中央値）", "grid": true}
        },
        "xOffset": {"field": "__name", "sort": ["正規雇用労働者", "全労働者"]},
        "text": {"field": "__text"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

正社員の差異は、平均年収500万円未満の250社で77.8%、800〜1000万円の392社で73.8%と、平均年収が上がるにつれておおむね下がります。1000万円以上の133社では66.4%まで下がります。平均年収が高い会社で正社員として働く女性の賃金は、男性のおよそ3分の2ということです。

全労働者の差異は、1000万円未満の5つのグループでは69.6〜71.2%とほとんど動かず、1000万円以上で65.1%に下がります。平均年収の低い側には、小売業のように非正規雇用労働者の多い業種が入っています。小売業では正社員の差異が76.1%なのに、全労働者では64.3%まで下がります。賃金の低い非正規の働き方に女性が多く就いているため、正社員どうしの差が小さくても全労働者の値が下がり、全労働者の値では平均年収による違いが見えにくくなると考えられます。

平均年収1000万円以上の133社に多いのは、建設業（23社）、卸売業（17社）、情報・通信業（15社）です。この違いが業種の違いだけによるものかを確認するため、30社以上ある19業種のそれぞれで、平均年収の高い半分と低い半分を比較しました。高い半分のほうが正社員の差異の値が低い（男女の差が大きい）業種は19のうち13で、同じ業種の中でも、多くの業種で同じ傾向があります。

## 銀行業は全労働者で53.9%と男女の差が最も大きく、小売業は正社員どうしの差が小さい

業種ごとの中央値を、全労働者の差異の値が低い順（男女の差が大きい順）に上から並べます。差異を開示した会社が15社以上ある26業種です。

```chart
{
  "height": 780,
  "layer": [
    {
      "data": {"name": "by_industry"},
      "transform": [
        {"fold": ["wage_all", "wage_regular"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"wage_all\": \"全労働者\", \"wage_regular\": \"正規雇用労働者\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"wage_all\",\"wage_regular\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "industry",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [40, 85], "zero": false, "nice": false},
          "axis": {"title": "男性に対する女性の賃金（%、中央値）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["全労働者", "正規雇用労働者"], "range": ["#93c5fd", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["正規雇用労働者", "全労働者"]},
        "tooltip": [
          {"field": "industry", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

男女の差が最も大きいのは銀行業で、全労働者の中央値は53.9%です。情報・通信業の76.2%とは22ポイント以上離れています。

全労働者の値が低い業種どうしでも、正社員の値は大きく違います。小売業は全労働者では64.3%と差が大きいのに、正社員に限ると76.1%で、対象の会社全体の正社員の中央値74.8%を上回ります。非正規雇用労働者どうしでは96.1%と、ほぼ同じ賃金です。正社員どうしでも非正規雇用労働者どうしでも差は小さいのに、全体では女性の賃金が男性の6割台になります。賃金の低い非正規の働き方に女性が多く就いていることが、差の大部分の原因と考えられます。

反対に、建設業（全労働者65.1%、正社員67.7%）と不動産業（64.0%、66.1%）は、全労働者と正社員の値がほとんど変わりません。正社員どうしの時点で、女性の賃金は男性の3分の2前後にとどまります。建設業は平均年収の中央値が850万円と26業種で最も高く、前の節の「平均年収が高い会社ほど正社員の差が大きい」傾向が、業種の単位でも表れています。銀行業は正社員でも65.3%と低いうえに、全労働者ではそこからさらに11.4ポイント下がります。正社員どうしの差に加えて、働き方の違いによる差が全労働者の値を押し下げていると考えられます。

平均年収が高くても男女の差が小さい業種もあります。医薬品は平均年収の中央値が843万円と建設業に近い水準ながら、正社員の差異は78.6%で、26業種の中で最も高い値（男女の差が最も小さい）です。平均年収の高い業種で、正社員の差異の値が低いとは限りません。

## 女性の管理職が多い会社ほど、正社員の差は小さい

同じ有価証券報告書に載っている、管理職に占める女性の割合で会社を6つに分け、正社員の差異の中央値を並べます。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "by_manager"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "wage_regular", "type": "quantitative"},
          {"field": "band", "type": "nominal"}
        ],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "管理職に占める女性の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "wage_regular",
          "type": "quantitative",
          "scale": {"domain": [50, 85], "zero": false, "nice": false},
          "axis": {"title": "正規雇用労働者の男性に対する女性の賃金（%、中央値）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "by_manager"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "管理職に占める女性の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "wage_regular",
          "type": "quantitative",
          "scale": {"domain": [50, 85], "zero": false, "nice": false},
          "axis": {"title": "正規雇用労働者の男性に対する女性の賃金（%、中央値）", "grid": true}
        },
        "text": {"field": "wage_regular"}
      }
    }
  ]
}
```

女性の管理職が1人もいない66社では、正社員の差異の中央値は70.3%です。割合が上がるにつれて差異の値は高くなり、女性管理職が30%以上の148社では77.8%になります。賃金の高い管理職に男性が多い会社ほど、正社員の平均賃金の差が大きくなると考えられます。

## 転職先を選ぶときの使い方

求人票の平均年収からは、自分がその会社でいくら受け取れるかは分かりません。この記事の数字は、次の順で使えます。

1. 業種別の図で志望する業種の棒を見て、その業界での男女の賃金の差の一般的な水準を確認します
2. 志望する会社の有価証券報告書で、全労働者と正規雇用労働者の両方の差異を確認します。正社員として応募するなら、比較するのは正規雇用労働者の値です
3. 平均年収が高い会社ほど正社員の男女の差は開きやすいので、平均年収の高い候補ほど、正規雇用労働者の差異が業種の中央値より上か下かを確認します。下回る会社は、同じ業界の中で正社員の男女の差が大きい会社なので、面接で評価や昇進の仕組みを具体的に尋ねる材料になります
4. 同じ書類の管理職に占める女性の割合も並べます。女性の管理職がいない会社の正社員の差異の中央値は70.3%で、30%以上の会社より7.5ポイント低い値です。入社後に管理職を目指すなら、候補の会社どうしでこの割合を比較し、女性の管理職がいる会社を優先して確認します

## データの出典

本記事は金融庁の[EDINET](https://disclosure2.edinet-fsa.go.jp/)で公開されている有価証券報告書のデータを、2026年10月24日時点で集計しています。各社の直近の有価証券報告書（2025年1月以降の提出分）の値で、決算期は会社ごとに異なります。

Queriaは、EDINETの有価証券報告書に記載された数値を、列名と単位を統一して1社1行のテーブルにし、列の説明を付けて公開しています。本記事で使った[従業員・女性活躍の指標テーブル](/datasets/queria/edinet/main/mart_human_capital)から志望する会社の行を検索したり、[提出会社のテーブル](/datasets/queria/edinet/main/mart_companies)と結合して同じ業種の会社を並べたりできます。

```sql id=overview
-- 本文の社数と中央値（プロットはしない）
WITH latest AS ( SELECT h.edinet_code, c.industry, h.number_of_employees, CAST(h.average_annual_salary AS DOUBLE) AS salary, h.female_to_male_wage_ratio AS wage_all, h.female_to_male_wage_ratio_regular AS wage_regular, h.female_to_male_wage_ratio_non_regular AS wage_non_regular, h.female_manager_ratio, ROW_NUMBER() OVER (PARTITION BY h.edinet_code ORDER BY h.period_end DESC, h.submit_date DESC) AS rn FROM edinet.main.mart_human_capital h JOIN edinet.main.mart_companies c USING (edinet_code) WHERE h.submit_date >= DATE '2025-01-01' AND c.listing_status = '上場' ), f AS ( SELECT * FROM latest WHERE rn = 1 AND number_of_employees >= 100 ) SELECT COUNT(*) AS n_companies, COUNT(salary) AS n_salary, COUNT(wage_all) AS n_wage, COUNT(wage_regular) AS n_wage_regular, ROUND(MEDIAN(salary) / 10000) AS salary_man, ROUND(MEDIAN(wage_all) * 100, 1) AS wage_all, ROUND(MEDIAN(wage_regular) * 100, 1) AS wage_regular FROM f
```

```sql id=by_band
WITH latest AS ( SELECT h.edinet_code, c.industry, h.number_of_employees, CAST(h.average_annual_salary AS DOUBLE) AS salary, h.female_to_male_wage_ratio AS wage_all, h.female_to_male_wage_ratio_regular AS wage_regular, h.female_to_male_wage_ratio_non_regular AS wage_non_regular, h.female_manager_ratio, ROW_NUMBER() OVER (PARTITION BY h.edinet_code ORDER BY h.period_end DESC, h.submit_date DESC) AS rn FROM edinet.main.mart_human_capital h JOIN edinet.main.mart_companies c USING (edinet_code) WHERE h.submit_date >= DATE '2025-01-01' AND c.listing_status = '上場' ), f AS ( SELECT * FROM latest WHERE rn = 1 AND number_of_employees >= 100 ) SELECT CASE WHEN salary < 5000000 THEN '500万円未満' WHEN salary < 6000000 THEN '500〜600万円' WHEN salary < 7000000 THEN '600〜700万円' WHEN salary < 8000000 THEN '700〜800万円' WHEN salary < 10000000 THEN '800〜1000万円' ELSE '1000万円以上' END AS band, COUNT(*) AS n, ROUND(MEDIAN(wage_all) * 100, 1) AS wage_all, ROUND(MEDIAN(wage_regular) * 100, 1) AS wage_regular FROM f WHERE salary IS NOT NULL AND wage_all IS NOT NULL AND wage_regular IS NOT NULL GROUP BY band ORDER BY MIN(salary)
```

```sql id=top_band_industry
-- 平均年収1000万円以上の会社に多い業種（プロットはしない）
WITH latest AS ( SELECT h.edinet_code, c.industry, h.number_of_employees, CAST(h.average_annual_salary AS DOUBLE) AS salary, h.female_to_male_wage_ratio AS wage_all, h.female_to_male_wage_ratio_regular AS wage_regular, h.female_to_male_wage_ratio_non_regular AS wage_non_regular, h.female_manager_ratio, ROW_NUMBER() OVER (PARTITION BY h.edinet_code ORDER BY h.period_end DESC, h.submit_date DESC) AS rn FROM edinet.main.mart_human_capital h JOIN edinet.main.mart_companies c USING (edinet_code) WHERE h.submit_date >= DATE '2025-01-01' AND c.listing_status = '上場' ), f AS ( SELECT * FROM latest WHERE rn = 1 AND number_of_employees >= 100 ) SELECT industry, COUNT(*) AS n FROM f WHERE salary >= 10000000 AND wage_all IS NOT NULL AND wage_regular IS NOT NULL GROUP BY industry ORDER BY n DESC, industry LIMIT 5
```

```sql id=within_industry
-- 30社以上ある業種の中で、平均年収の高い半分と低い半分の正社員の差異を比べる（プロットはしない）
WITH latest AS ( SELECT h.edinet_code, c.industry, h.number_of_employees, CAST(h.average_annual_salary AS DOUBLE) AS salary, h.female_to_male_wage_ratio AS wage_all, h.female_to_male_wage_ratio_regular AS wage_regular, h.female_to_male_wage_ratio_non_regular AS wage_non_regular, h.female_manager_ratio, ROW_NUMBER() OVER (PARTITION BY h.edinet_code ORDER BY h.period_end DESC, h.submit_date DESC) AS rn FROM edinet.main.mart_human_capital h JOIN edinet.main.mart_companies c USING (edinet_code) WHERE h.submit_date >= DATE '2025-01-01' AND c.listing_status = '上場' ), f AS ( SELECT * FROM latest WHERE rn = 1 AND number_of_employees >= 100 ), halves AS ( SELECT industry, wage_regular, NTILE(2) OVER (PARTITION BY industry ORDER BY salary, edinet_code) AS half, COUNT(*) OVER (PARTITION BY industry) AS n FROM f WHERE salary IS NOT NULL AND wage_regular IS NOT NULL ), by_ind AS ( SELECT industry, MEDIAN(wage_regular) FILTER (WHERE half = 2) AS high_half, MEDIAN(wage_regular) FILTER (WHERE half = 1) AS low_half FROM halves WHERE n >= 30 GROUP BY industry ) SELECT COUNT(*) AS n_industries, COUNT(*) FILTER (WHERE high_half < low_half) AS n_high_lower FROM by_ind
```

```sql id=by_industry
WITH latest AS ( SELECT h.edinet_code, c.industry, h.number_of_employees, CAST(h.average_annual_salary AS DOUBLE) AS salary, h.female_to_male_wage_ratio AS wage_all, h.female_to_male_wage_ratio_regular AS wage_regular, h.female_to_male_wage_ratio_non_regular AS wage_non_regular, h.female_manager_ratio, ROW_NUMBER() OVER (PARTITION BY h.edinet_code ORDER BY h.period_end DESC, h.submit_date DESC) AS rn FROM edinet.main.mart_human_capital h JOIN edinet.main.mart_companies c USING (edinet_code) WHERE h.submit_date >= DATE '2025-01-01' AND c.listing_status = '上場' ), f AS ( SELECT * FROM latest WHERE rn = 1 AND number_of_employees >= 100 ) SELECT industry, COUNT(*) AS n, ROUND(MEDIAN(salary) / 10000) AS salary_man, ROUND(MEDIAN(wage_all) * 100, 1) AS wage_all, ROUND(MEDIAN(wage_regular) * 100, 1) AS wage_regular, ROUND(MEDIAN(wage_non_regular) * 100, 1) AS wage_non_regular, ROUND((MEDIAN(wage_regular) - MEDIAN(wage_all)) * 100, 1) AS gap_pt FROM f WHERE wage_all IS NOT NULL AND wage_regular IS NOT NULL GROUP BY industry HAVING COUNT(*) >= 15 ORDER BY wage_all ASC, industry
```

```sql id=by_manager
WITH latest AS ( SELECT h.edinet_code, c.industry, h.number_of_employees, CAST(h.average_annual_salary AS DOUBLE) AS salary, h.female_to_male_wage_ratio AS wage_all, h.female_to_male_wage_ratio_regular AS wage_regular, h.female_to_male_wage_ratio_non_regular AS wage_non_regular, h.female_manager_ratio, ROW_NUMBER() OVER (PARTITION BY h.edinet_code ORDER BY h.period_end DESC, h.submit_date DESC) AS rn FROM edinet.main.mart_human_capital h JOIN edinet.main.mart_companies c USING (edinet_code) WHERE h.submit_date >= DATE '2025-01-01' AND c.listing_status = '上場' ), f AS ( SELECT * FROM latest WHERE rn = 1 AND number_of_employees >= 100 ) SELECT CASE WHEN female_manager_ratio = 0 THEN '0%' WHEN female_manager_ratio < 0.05 THEN '5%未満' WHEN female_manager_ratio < 0.1 THEN '5〜10%' WHEN female_manager_ratio < 0.2 THEN '10〜20%' WHEN female_manager_ratio < 0.3 THEN '20〜30%' ELSE '30%以上' END AS band, COUNT(*) AS n, ROUND(MEDIAN(wage_regular) * 100, 1) AS wage_regular FROM f WHERE female_manager_ratio IS NOT NULL AND wage_regular IS NOT NULL GROUP BY band ORDER BY MIN(female_manager_ratio)
```
