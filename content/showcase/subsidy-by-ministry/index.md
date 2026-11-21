---
title: 補助金1件あたりの平均額は、経済産業省が約9.4億円、農林水産省が約3,300万円
description: gBizINFOの補助金交付実績で2017〜2023年の交付を省庁別に集計しました。1件あたりの平均額は経済産業省が約9.4億円、農林水産省が約3,300万円で30倍近い差があり、交付総額は2021年の約18.4兆円が最大です
publishedAt: 2026-06-08
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 補助金
  - gBizINFO
  - 中小企業
datasets:
  - queria/gbizinfo
sources:
  - title: gBizINFO
    url: https://info.gbiz.go.jp/
    publisher: 経済産業省
  - title: gBizINFO データダウンロード
    url: https://info.gbiz.go.jp/hojin/DownloadTop
    publisher: 経済産業省
agentHint: 省庁(issuer)別に補助金1件あたりの平均交付額(amount)を2017〜2023年で出して、少数の大型案件に集中する省庁と小口を広く配る省庁を並べて
socialAnnounce: |-
  国の補助金交付実績データ（gBizINFO）を省庁別に分析しました。

  どの省庁が、どんな規模・件数で補助金を出しているのか。出し手ごとの偏りから、補助金活用の見取り図が見えてきます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
relatedDatasets: false
---

gBizINFOの補助金交付実績で2017〜2023年の交付を省庁別に集計すると、1件あたりの平均額は経済産業省が約9.4億円、農林水産省が約3,300万円で、30倍近い差がありました。交付件数は農林水産省が約19.9万件で最も多く、経済産業省は約9,300件です。交付総額は文部科学省の約22.3兆円が最も多く、年ごとの総額は2021年の約18.4兆円が最大でした。

補助金の活用を検討するときは、どの省庁がどの程度の規模・件数で補助金を交付しているかを先に把握すると、申請する制度を選びやすくなります。この記事では、経済産業省などが運営する[gBizINFO](https://info.gbiz.go.jp/)が公開する補助金交付実績データを使い、国の補助金の交付額と件数を省庁別に集計します。

## 使用するデータ

gBizINFOは、政府が保有する法人情報を法人番号で名寄せして公開するオープンデータサービスです。補助金交付実績テーブル（`mart_gbizinfo_subsidy`）には、交付先の法人番号・法人名、補助金名、交付額、支援機関（交付した省庁・庁）、交付決定日が収録されています。

このデータには、個別の事業者への交付のほか、基金や事務局へ一括で交付されたプログラム単位の大型案件も含まれます。そのため1件あたりの平均額は、1社が受け取れる金額の目安にはなりません。2024年以降は交付実績の反映に時間差があるので、2017〜2023年を対象にし、交付額（`amount`）が記録されている行だけを集計しています。

## 交付総額は2021年の約18.4兆円が最大で、2023年は約11.9兆円

2017〜2023年の交付総額を年ごとに集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_cho\"]) ? 0 : 1",
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
          {"field": "total_cho", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "total_cho",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "交付総額（兆円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

交付総額は2017年の約2.6兆円から年々増え、2021年に約18.4兆円で最大になりました。2020〜2022年は高い水準が続いており、この時期の経済対策が交付額を増やしたと考えられます。2023年は約11.9兆円に減っています。補助金の総額は、景気対策や政策の重点配分によって年ごとに大きく変わります。

## 累計交付額は文部科学省の約22.3兆円が最も多い

2017〜2023年の累計交付額を省庁別に集計し、上位14の支援機関を金額順に並べました。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "amt_rank"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "total_cho", "type": "quantitative"},
          {"field": "issuer", "type": "nominal"}
        ],
        "x": {
          "field": "total_cho",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "交付総額（兆円）", "grid": true}
        },
        "y": {
          "field": "issuer",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "支援機関"},
          "sort": null
        }
      }
    }
  ]
}
```

最も多いのは文部科学省で、累計約22.3兆円です。義務教育費国庫負担金や私立大学等経常費補助金など、毎年交付される大型の制度が金額の多くを占めています。厚生労働省（約13.0兆円）、経済産業省（約8.8兆円）、農林水産省（約6.6兆円）が続きます。金額の上位は、社会保障・産業振興・教育といった国の主要な政策分野の省庁です。

## 1件あたりの平均額は、経済産業省が約9.4億円、農林水産省が約3,300万円

同じ期間の交付件数を省庁別に集計し、上位14の支援機関を並べました。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "cnt_rank"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "cnt", "type": "quantitative"},
          {"field": "issuer", "type": "nominal"}
        ],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "交付件数", "grid": true}
        },
        "y": {
          "field": "issuer",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "支援機関"},
          "sort": null
        }
      }
    }
  ]
}
```

件数は農林水産省が約19.9万件で最も多く、厚生労働省（約11.0万件）、文部科学省（約8.3万件）が続きます。金額で3位だった経済産業省は、件数では約9,300件です。

農林水産省は交付額では4位ですが件数は最も多く、累計額を件数で割った1件あたりの平均額は約3,300万円です。農林水産省は小口の補助を多くの交付先に配っています。経済産業省は1件あたり約9.4億円で、少数の大型案件に交付が集中しています。省庁によって、1件あたりの規模は30倍近く異なります。

## 補助金活用での使い方

省庁ごとの交付の規模と件数を把握すると、補助金の検討に次のように使えます。

- 自社の事業分野を所管する省庁が、小口を多く配る省庁か、大型案件に集中する省庁かを確認し、申請して採択される可能性を判断する
- 交付総額の年次推移から、補助金が増えている時期か減っている時期かを確認し、申請の時期を検討する
- 補助金名（補助金制度）で交付先の法人を検索し、自社と近い規模・業種の採択事例を把握する

## データの出典

本記事は [gBizINFO](https://info.gbiz.go.jp/) が公開する補助金交付実績データを、2026年7月11日時点で取得して集計しています。補助金交付実績は[データダウンロードページ](https://info.gbiz.go.jp/hojin/DownloadTop)からも配布されています。

Queriaは、gBizINFOの補助金交付実績を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[補助金交付実績テーブル](/datasets/queria/gbizinfo/main/mart_gbizinfo_subsidy)から、補助金名や交付先の法人で絞り込んで、交付額や件数を集計できます。

```sql id=trend
SELECT EXTRACT(year FROM certification_date) AS year, ROUND(SUM(amount) / 1e12, 2) AS total_cho FROM gbizinfo.main.mart_gbizinfo_subsidy WHERE amount IS NOT NULL AND certification_date BETWEEN '2017-01-01' AND '2023-12-31' GROUP BY year ORDER BY year
```

```sql id=amt_rank
SELECT issuer, total_cho FROM (SELECT issuer, ROUND(SUM(amount) / 1e12, 2) AS total_cho FROM gbizinfo.main.mart_gbizinfo_subsidy WHERE amount IS NOT NULL AND certification_date BETWEEN '2017-01-01' AND '2023-12-31' GROUP BY issuer ORDER BY total_cho DESC LIMIT 14) ORDER BY total_cho ASC
```

```sql id=cnt_rank
SELECT issuer, cnt FROM (SELECT issuer, COUNT(*) AS cnt FROM gbizinfo.main.mart_gbizinfo_subsidy WHERE amount IS NOT NULL AND certification_date BETWEEN '2017-01-01' AND '2023-12-31' GROUP BY issuer ORDER BY cnt DESC LIMIT 14) ORDER BY cnt ASC
```
