---
title: 新設法人に占める合同会社の割合は、2016年の19.3%から2024年の29.0%に上がった
description: 国税庁の法人番号データから株式会社と合同会社の新設件数を集計しました。合同会社は2016年の約2万件から2024年の約4万件に増え、新設法人に占める割合は19.3%から29.0%に上がりました。都道府県別では沖縄県が38.8%で最も高く、愛知県の21.6%の1.8倍です。
publishedAt: 2026-06-16
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 法人
  - 起業
  - 創業
datasets:
  - queria/houjin_bangou
sources:
  - title: 国税庁法人番号公表サイト
    url: https://www.houjin-bangou.nta.go.jp/
    publisher: 国税庁
agentHint: 沖縄県について、株式会社（301）と合同会社（305）の新設件数の推移を2016年以降で年別に出して。合同会社の割合がいつから高いのか見て
socialAnnounce: |-
  国税庁の法人番号データで、新設法人に占める合同会社の割合の推移と地域差を分析しました。

  創業支援メニューの設計や地域の起業動向の把握に使えます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2024年に新しく設立された株式会社と合同会社のうち、29.0%が合同会社でした。2016年の19.3%から毎年上がっています。合同会社の新設件数は2016年の約2万件から2024年の約4万件にほぼ倍増し、株式会社は8万件台から9万件台に増えた程度です。2020年から2024年の都道府県別では、合同会社の割合が最も高いのは沖縄県の38.8%で、最も低い愛知県の21.6%の1.8倍でした。

この記事では、国税庁の[法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)が公開する全件データを使い、新しく設立された法人の種別の構成を年別・都道府県別に集計しました。創業融資や相談窓口の設計、起業セミナーの企画では、設立される法人の種別がどう変化しているかが基礎データになります。グーグルやアップルの日本法人も合同会社です。

## 株式会社と合同会社の新設件数を、法人番号の指定日で集計する

国税庁の法人番号データは、法人番号が指定されたすべての法人を収録しています。各レコードには法人番号の指定年月日（`assignment_date`）と法人種別（`kind`）が含まれ、種別は次のコードで区別されています。

| コード | 法人種別 |
| ------ | -------- |
| 301    | 株式会社 |
| 302    | 有限会社 |
| 303    | 合名会社 |
| 304    | 合資会社 |
| 305    | 合同会社 |

有限会社（302）は2006年施行の会社法で新規設立ができなくなり、代わりに合同会社（305）が導入されました。この記事では、現在も新設できる株式会社（301）と合同会社（305）に絞って集計しています。合名会社（303）・合資会社（304）は件数が少ないので含めていません。

法人番号制度は2015年に始まり、その年に既存の法人へ一斉に番号が指定されたので、2015年は指定件数が突出します。そのため対象は、指定日が実際の設立とおおむね対応する2016年以降にしました。数えているのは法人番号の指定日で、登記上の設立日とは年末年始をまたぐときなどに年がずれることがあります。設立後に解散・休眠した法人も新設件数に含みます。

## 合同会社の新設件数は、2016年から2024年にほぼ倍増した

株式会社と合同会社の新設件数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kk\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "kk", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "kk",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "新設件数（件）", "grid": true}
        },
        "color": {
          "datum": "株式会社",
          "type": "nominal",
          "scale": {"domain": ["株式会社", "合同会社"], "range": ["#3b82f6", "#22c55e"]},
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"godo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "godo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "godo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "新設件数（件）", "grid": true}
        },
        "color": {
          "datum": "合同会社",
          "type": "nominal",
          "scale": {"domain": ["株式会社", "合同会社"], "range": ["#3b82f6", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

株式会社の新設件数は8万件台から9万件台に緩やかに増えた程度です。合同会社は2016年の約2万件から2024年には約4万件になり、ほぼ倍増しています。

## 新設法人に占める合同会社の割合は、毎年上がって約3割になった

株式会社と合同会社を合わせた新設件数のうち、合同会社が占める割合の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"godo_share\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#22c55e"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "godo_share", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "godo_share",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "合同会社の割合（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

合同会社の割合は2016年の19.3%から2024年の29.0%まで、毎年上がっています。新設法人のおよそ3割が合同会社です。設立費用が安く手続きが簡単なことから、株式会社に代わる選択肢として選ばれるようになったと考えられます。

## 合同会社の割合は沖縄県が38.8%で最も高く、愛知県の1.8倍

2020年から2024年に新設された株式会社と合同会社を都道府県ごとに集計し、合同会社の割合を高い順に並べました。所在地の都道府県名が空のレコードは除いています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "share", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "share",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "合同会社の割合（%）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "share", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "share",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "合同会社の割合（%）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "share", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "share",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "合同会社の割合（%）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは沖縄県の38.8%で、新設法人の4割近くが合同会社です。最も低いのは愛知県の21.6%で、大阪府も21.8%と、大都市圏のある府県では株式会社の比率が高くなっています。最上位と最下位の差は約1.8倍です。

## 創業支援での使い方

- 担当地域の合同会社の割合を全国平均や近隣県と比較し、相談窓口やセミナーで想定する法人形態の比重を決める
- 合同会社の増え方をもとに、設立手続きや会計・税務の支援メニューを、株式会社を前提にしたものから見直す
- 市区町村コード（`city_code`）で集計すると、市区町村ごとの新設法人の動きを確認できる

## データの出典

本記事は国税庁の[法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)が公開する全件データを、2026年7月11日時点で取得して集計しています。対象は法人番号の指定年月日が2016年から2024年までのレコードで、都道府県別の集計は2020年から2024年の5年分をまとめたものです。

Queriaは、国税庁の法人番号データの列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[法人番号テーブル](/datasets/queria/houjin_bangou/main/mart_houjin_bangou)から、担当地域の新設件数を種別ごとに集計できます。AIに分析を依頼する方法は[Claude Codeで分析する](https://docs.queria.io/claude-code)ガイドで紹介しています。

```sql id=trend
SELECT EXTRACT(year FROM assignment_date)::INT AS year, SUM(CASE WHEN kind = '301' THEN 1 ELSE 0 END) AS kk, SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) AS godo FROM houjin_bangou.main.mart_houjin_bangou WHERE assignment_date IS NOT NULL AND EXTRACT(year FROM assignment_date) BETWEEN 2016 AND 2024 GROUP BY year ORDER BY year
```

```sql id=share
SELECT EXTRACT(year FROM assignment_date)::INT AS year, ROUND(SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 100.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END), 1) AS godo_share FROM houjin_bangou.main.mart_houjin_bangou WHERE assignment_date IS NOT NULL AND EXTRACT(year FROM assignment_date) BETWEEN 2016 AND 2024 GROUP BY year ORDER BY year
```

```sql id=rank_top
WITH ranked AS (SELECT prefecture_name, ROUND(SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 100.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END), 1) AS share, ROW_NUMBER() OVER (ORDER BY SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 1.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END) DESC, prefecture_name) AS rn FROM houjin_bangou.main.mart_houjin_bangou WHERE assignment_date IS NOT NULL AND EXTRACT(year FROM assignment_date) BETWEEN 2020 AND 2024 AND prefecture_name IS NOT NULL AND prefecture_name != '' GROUP BY prefecture_name) SELECT prefecture_name, share FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT prefecture_name, ROUND(SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 100.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END), 1) AS share, ROW_NUMBER() OVER (ORDER BY SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 1.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END) DESC, prefecture_name) AS rn FROM houjin_bangou.main.mart_houjin_bangou WHERE assignment_date IS NOT NULL AND EXTRACT(year FROM assignment_date) BETWEEN 2020 AND 2024 AND prefecture_name IS NOT NULL AND prefecture_name != '' GROUP BY prefecture_name) SELECT prefecture_name, share FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH ranked AS (SELECT prefecture_name, ROUND(SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 100.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END), 1) AS share, ROW_NUMBER() OVER (ORDER BY SUM(CASE WHEN kind = '305' THEN 1 ELSE 0 END) * 1.0 / SUM(CASE WHEN kind IN ('301', '305') THEN 1 ELSE 0 END) DESC, prefecture_name) AS rn FROM houjin_bangou.main.mart_houjin_bangou WHERE assignment_date IS NOT NULL AND EXTRACT(year FROM assignment_date) BETWEEN 2020 AND 2024 AND prefecture_name IS NOT NULL AND prefecture_name != '' GROUP BY prefecture_name) SELECT prefecture_name, share FROM ranked WHERE rn > 37 ORDER BY rn
```
