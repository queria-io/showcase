---
title: 人口あたりの交通事故死者が多い10県は、事故の件数では全国を下回る
description: 2022〜24年に人口あたりの交通事故死者が多い10県は、1975〜77年には人口あたりの事故件数も全国を上回っていましたが、2022〜24年は全国を下回ります。事故1,000件あたりの死者は2012年から上がり、47都道府県のうち45で上がりました。
publishedAt: 2026-03-19
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 交通安全
  - 都道府県
  - 安全
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（K 安全）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/K
    publisher: 総務省統計局
  - title: 道路の交通に関する統計
    url: https://www.e-stat.go.jp/statistics/00130002
    publisher: 警察庁
agentHint: 交通事故死傷者数に占める高齢者（K310203）の割合を都道府県別に2010〜12年と2022〜24年で出して、事故1,000件あたりの死者数が大きく上がった県ほど高齢者の割合も上がっているかを比べて
socialAnnounce: |-
  交通事故の死者と件数を都道府県別に50年分並べました。
  いま死者が多い10県は、1975〜77年には事故件数も全国を上回り、いまは下回ります。

  都道府県の交通安全計画に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

交通事故の死者は、1992年の11,452人から2024年の2,663人へ77%減りました。同じ期間に事故の件数も減っていますが、死者と件数は同じようには減っていません。事故1,000件あたりの死者は2012年を底に上がり始め、2022〜24年は2010〜12年と比較して47都道府県のうち45で上がっています。

2022〜24年に人口あたりの死者が多い10県は、1975〜77年には人口あたりの事故の件数も全国を上回っていましたが、2022〜24年の件数は全国を下回ります。死者の多い10県と少ない10都府県の差は、事故の件数ではなく、事故1,000件あたりの死者の差によるもので、2022〜24年は3倍の差があります。

## 死者は1992年から77%減った

使ったのは e-Stat「社会・人口統計体系」の都道府県別の安全データ（`k_pref_safety`）と、人口データ（`a_pref_population`）の総人口（`A1101`）です。交通事故については次の項目が1975年から2024年まで入っています。

| コード  | 内容                                             |
| ------- | ------------------------------------------------ |
| K3101   | 交通事故発生件数                                 |
| K3102   | 交通事故死傷者数                                 |
| K310201 | 交通事故死傷者数（乳幼児：0～6歳、1986年から）   |
| K310202 | 交通事故死傷者数（小学生：7～12歳、1986年から）  |
| K310203 | 交通事故死傷者数（高齢者：65歳以上、1986年から） |
| K3103   | 交通事故死者数                                   |
| K3104   | 交通事故負傷者数                                 |

ここでは交通事故死者数（`K3103`）と交通事故発生件数（`K3101`）を使います。どちらも警察庁の[道路の交通に関する統計](https://www.e-stat.go.jp/statistics/00130002)が元で、テーブルの時点名は「年度」ですが、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/K)では1月から12月の暦年計です。死者は事故から24時間以内に亡くなった人だけを集計しています。

```chart
{
  "layer": [
    {
      "data": {"name": "death_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_deaths\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_deaths", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "total_deaths",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "死者数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1992, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "text", "lineBreak": "\n", "align": "left", "fontSize": 11},
      "encoding": {
        "x": {"datum": 1992, "type": "quantitative"},
        "y": {"datum": 11452, "type": "quantitative"},
        "text": {"value": "1992年 11,452人"}
      }
    }
  ]
}
```

1975年以降で死者が最も多かったのは1992年の11,452人です。その後は前年を上回る年を挟みながら減り、2024年は2,663人でした。前年を上回ったのは1995年・2000年・2015年・2023年の4回で、いずれも増加は100人に届きません。

## 事故の件数は2004年にかけて倍になり、その後は7割減った

```chart
{
  "layer": [
    {
      "data": {"name": "accident_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_accidents\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#f97316"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_accidents", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "total_accidents",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "発生件数（件）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

件数は、人が死亡または負傷した事故（人身事故）だけを集計していて、物の損害だけの事故は含みません。件数は1975年の472,938件から2004年の952,709件へ、ほぼ倍になりました。死者が最も多かった1992年は695,346件で、そのあとも件数は増えています。2024年は290,895件で、2004年から7割減りました。

## 事故1,000件あたりの死者は、2012年から上がっている

死者数を件数で割ると、事故のうちどれだけが死亡につながったかが分かります。分母は人身事故の件数なので、正確には人身事故1,000件あたりの死者数です。

```chart
{
  "layer": [
    {
      "data": {"name": "lethality"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"deaths_per_1000\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#7c3aed"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "deaths_per_1000", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "deaths_per_1000",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "事故1,000件あたりの死者数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

事故1,000件あたりの死者は、1975年の22.82人から2012年の6.63人まで下がりました。そこから上がり、2024年は9.15人です。2012年から2024年に件数は56%減りましたが、死者は40%減にとどまっています。

同じ期間に、死傷者に占める65歳以上の割合は13.9%から16.5%に上がりました。このデータには年齢別の死者数がないので、事故1,000件あたりの死者の上昇のうち、死傷者の年齢構成の変化による分は区別できません。

```sql
SELECT year AS 年, elderly_pct AS 死傷者に占める65歳以上の割合 FROM elderly_share WHERE year >= 2008
```

## 事故1,000件あたりの死者は、47都道府県のうち45で上がった

都道府県ごとに、2010〜12年と2022〜24年の事故1,000件あたりの死者を比較しました。死者が年に数十人の県もあり、1年ごとでは値が大きく変動するので、3年分を合算しています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "leth_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "事故1,000件あたり死者数の変化率（%、2010〜12年→2022〜24年）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上がった",
          "type": "nominal",
          "scale": {"domain": ["上がった", "下がった"], "range": ["#7c3aed", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "leth_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "事故1,000件あたり死者数の変化率（%、2010〜12年→2022〜24年）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下がった",
          "type": "nominal",
          "scale": {"domain": ["上がった", "下がった"], "range": ["#7c3aed", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

下がったのは長野県（-3.0%）と群馬県（-6.4%）の2県だけです。上がり方が最も大きいのは和歌山県で、1,000件あたり8.55人から22.07人へ158.2%上がりました。

1975〜77年から2010〜12年にかけては、47都道府県すべてで下がっていました。基準を2011〜13年にすると上がったのは44、2012年と2024年の1年どうしで比較すると43です。

```sql
SELECT comparison AS 比べた期間, prefectures AS 都道府県の数, rose AS 上がった, fell AS 下がった FROM leth_robust
```

## 2022〜24年に死者の多い10県は、事故の件数が全国より少ない

2022〜24年の3年分で人口10万人あたりの死者数を計算し、多い10県と少ない10都府県を選びました。同じ県のまま、過去の期間の人口10万人あたり事故件数を集計しています。死者も件数も事故が起きた都道府県で集計するので、県外から来た車の事故も含みます。

```chart
{
  "layer": [
    {
      "data": {"name": "fixed_groups"},
      "transform": [
        {
          "fold": ["hi_acc_per_100k", "all_acc_per_100k", "lo_acc_per_100k"],
          "as": ["__series", "__value"]
        },
        {
          "calculate": "{\"hi_acc_per_100k\": \"2022〜24年に死者が多い10県\", \"all_acc_per_100k\": \"全国\", \"lo_acc_per_100k\": \"2022〜24年に死者が少ない10都府県\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"hi_acc_per_100k\",\"all_acc_per_100k\",\"lo_acc_per_100k\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "period",
          "type": "nominal",
          "axis": {"title": "期間（3年分を合算）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたりの事故件数（件／年）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["2022〜24年に死者が多い10県", "全国", "2022〜24年に死者が少ない10都府県"],
            "range": ["#ef4444", "#94a3b8", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["2022〜24年に死者が多い10県", "全国", "2022〜24年に死者が少ない10都府県"]},
        "tooltip": [
          {"field": "period", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

2022〜24年に死者が多い10県は、徳島県・愛媛県・香川県・高知県・秋田県・山梨県・岐阜県・青森県・和歌山県・三重県です。少ない10都府県は東京都・神奈川県・埼玉県・大阪府・福岡県・愛知県・宮城県・奈良県・千葉県・京都府で、三大都市圏の都府県と福岡県・宮城県が並びます。

この10県の事故件数は、1975〜77年には人口10万人あたり452件で、全国の414件と10都府県の382件を上回っていました。1990〜92年は542件で全国の537件とほぼ同じ、2010〜12年は574件で全国の543件を上回っています。2022〜24年は188件で、全国の241件と10都府県の250件を下回りました。

```sql
SELECT period AS 期間, hi_acc_per_100k AS 死者が多い10県, all_acc_per_100k AS 全国, lo_acc_per_100k AS 死者が少ない10都府県 FROM fixed_groups
```

期間ごとに死者の多い10県・少ない10都府県を選び直しても、同じ結果になります。選ばれる県は期間によって変わり、1975〜77年と2022〜24年の両方で多い10県に入るのは香川県・高知県・山梨県・三重県・徳島県の5県です。2022〜24年の事故1,000件あたりの死者は、死者が多い10県で18.41人、少ない10都府県で6.10人で、3倍の差があります。

```sql
SELECT period AS 期間, hi_acc_per_100k AS 件数_死者が多い10県, lo_acc_per_100k AS 件数_死者が少ない10都府県, hi_deaths_per_1000 AS 千件あたり死者_多い10県, lo_deaths_per_1000 AS 千件あたり死者_少ない10都府県, corr_death_vs_accident AS 死者と件数の相関係数 FROM group_compare
```

```sql
SELECT period AS 期間, hi_10 AS 死者が多い10県, lo_10 AS 死者が少ない10都府県 FROM group_members
```

47都道府県すべてで見た人口あたり死者数と人口あたり件数の相関係数は、1975〜77年の0.46から2022〜24年は-0.21になりました。いまは弱い負の相関で、件数が少ない県ほど死者が多いと言えるほどの関係ではありません。死者が最も多い徳島県（277件）や3番目の香川県（329件）のように、件数が全国を上回る県もあります。件数の多い県ほど死者も多いという1975〜77年の関係は、2022〜24年にはなくなっています。

```chart
{
  "layer": [
    {
      "data": {"name": "pref_2022_24"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "acc_per_100k", "type": "quantitative"},
          {"field": "deaths_per_100k", "type": "quantitative"}
        ],
        "x": {
          "field": "acc_per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたりの事故件数（件／年、2022〜24年）", "grid": true}
        },
        "y": {
          "field": "deaths_per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたりの死者数（人／年、2022〜24年）", "grid": true}
        }
      }
    }
  ]
}
```

人口あたりの死者は、1975年から2024年までの50年すべてで東京都が最も少なくなっています。

```sql
SELECT years AS 年数, tokyo_lowest_years AS 東京都が最も少なかった年数, first_year AS 最初の年, last_year AS 最後の年 FROM tokyo_min
```

```sql
SELECT area_name AS 都道府県, deaths_per_100k AS 人口10万人あたり死者数, acc_per_100k AS 人口10万人あたり事故件数, deaths_per_1000 AS 事故1000件あたり死者数 FROM pref_2022_24
```

## 交通安全計画での使い方

- 事故件数の減少を目標にしている地域では、件数と一緒に事故1,000件あたりの死者を集計すると、件数が減っても死者が減らない状態を早く把握できます
- 散布図と都道府県の表で、自分の県の人口あたりの死者と件数の位置を確認できます。件数が全国より少ないのに死者が多い県では、事故1,000件あたりの死者がどの期間から上がったかを、本記事と同じ3年合算で確認できます
- 2010〜12年からの上昇が大きい県では、同じ期間の県内の事故の類型や時間帯の記録と照合すると、上昇の原因を検討できます

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年10月16日時点で集計しています。交通事故の元データは警察庁の[道路の交通に関する統計](https://www.e-stat.go.jp/statistics/00130002)で、定義と時点は[項目定義（K 安全）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/K)にあります。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の安全統計テーブル](/datasets/queria/e_stat/ssds/k_pref_safety)から、自分の県の死者と件数を1975年から並べたり、高齢者の死傷者の推移と比較したりできます。

```sql id=death_trend
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS total_deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K3103' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024 GROUP BY year ORDER BY year
```

```sql id=accident_trend
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS total_accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K3101' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024 GROUP BY year ORDER BY year
```

```sql id=lethality
-- 交通事故1,000件あたりの死者数（全国。47都道府県の合計どうしで割る）
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year)
SELECT year, ROUND(SUM(deaths) / SUM(accidents) * 1000, 2) AS deaths_per_1000 FROM k GROUP BY year ORDER BY year
```

```sql id=elderly_share
-- 交通事故死傷者数に占める65歳以上の割合（%）。K310203 は1986年から
SELECT year, ROUND(SUM(CASE WHEN cat01 = 'K310203' THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 = 'K3102' THEN TRY_CAST(value AS DOUBLE) END) * 100, 1) AS elderly_pct FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3102', 'K310203') AND area_name != '全国' AND year BETWEEN 1986 AND 2024 GROUP BY year ORDER BY year
```

```sql id=leth_up
-- 都道府県別の事故1,000件あたり死者数。2010〜12年と2022〜24年をそれぞれ3年合算して比べる
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
l AS (SELECT area_name, SUM(CASE WHEN year BETWEEN 2010 AND 2012 THEN deaths END) / SUM(CASE WHEN year BETWEEN 2010 AND 2012 THEN accidents END) * 1000 AS l0, SUM(CASE WHEN year BETWEEN 2022 AND 2024 THEN deaths END) / SUM(CASE WHEN year BETWEEN 2022 AND 2024 THEN accidents END) * 1000 AS l1 FROM k GROUP BY area_name),
c AS (SELECT area_name, ROUND(l0, 2) AS l0, ROUND(l1, 2) AS l1, ROUND((l1 / l0 - 1) * 100, 1) AS chg_pct, ROW_NUMBER() OVER (ORDER BY l1 / l0 DESC, area_name) AS rn FROM l)
SELECT area_name, l0, l1, chg_pct FROM c WHERE l1 > l0 ORDER BY rn
```

```sql id=leth_down
-- leth_up と同じ計算で、下がった都道府県
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
l AS (SELECT area_name, SUM(CASE WHEN year BETWEEN 2010 AND 2012 THEN deaths END) / SUM(CASE WHEN year BETWEEN 2010 AND 2012 THEN accidents END) * 1000 AS l0, SUM(CASE WHEN year BETWEEN 2022 AND 2024 THEN deaths END) / SUM(CASE WHEN year BETWEEN 2022 AND 2024 THEN accidents END) * 1000 AS l1 FROM k GROUP BY area_name),
c AS (SELECT area_name, ROUND(l0, 2) AS l0, ROUND(l1, 2) AS l1, ROUND((l1 / l0 - 1) * 100, 1) AS chg_pct, ROW_NUMBER() OVER (ORDER BY l1 / l0 DESC, area_name) AS rn FROM l)
SELECT area_name, l0, l1, chg_pct FROM c WHERE l1 <= l0 ORDER BY rn
```

```sql id=leth_robust
-- 比べる期間を変えたときに、事故1,000件あたり死者数が上がった・下がった都道府県の数
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
w AS (SELECT * FROM (VALUES ('1975〜77年 → 2010〜12年', 1, 1975, 1977, 2010, 2012), ('2012年 → 2024年', 2, 2012, 2012, 2024, 2024), ('2010〜12年 → 2022〜24年', 3, 2010, 2012, 2022, 2024), ('2011〜13年 → 2022〜24年', 4, 2011, 2013, 2022, 2024)) AS t(comparison, ord, a0, a1, b0, b1)),
l AS (SELECT w.comparison, w.ord, k.area_name, SUM(CASE WHEN k.year BETWEEN w.a0 AND w.a1 THEN k.deaths END) / SUM(CASE WHEN k.year BETWEEN w.a0 AND w.a1 THEN k.accidents END) AS l0, SUM(CASE WHEN k.year BETWEEN w.b0 AND w.b1 THEN k.deaths END) / SUM(CASE WHEN k.year BETWEEN w.b0 AND w.b1 THEN k.accidents END) AS l1 FROM k CROSS JOIN w GROUP BY w.comparison, w.ord, k.area_name)
SELECT comparison, COUNT(*) AS prefectures, COUNT(*) FILTER (WHERE l1 > l0) AS rose, COUNT(*) FILTER (WHERE l1 < l0) AS fell FROM l GROUP BY comparison, ord ORDER BY ord
```

```sql id=group_compare
-- 期間ごとに人口10万人あたり死者数で都道府県を並べ、多い10と少ない10の事故件数・事故1,000件あたり死者数を出す。3年分を合算する
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name != '全国' AND year <= 2024),
kp AS (SELECT k.area_name, k.year, k.deaths, k.accidents, p.pop FROM k JOIN p ON k.area_name = p.area_name AND k.year = p.year),
w AS (SELECT * FROM (VALUES ('1975〜77年', 1, 1975, 1977), ('1990〜92年', 2, 1990, 1992), ('2010〜12年', 3, 2010, 2012), ('2022〜24年', 4, 2022, 2024)) AS t(period, ord, y0, y1)),
s AS (SELECT w.period, w.ord, kp.area_name, SUM(kp.deaths) AS deaths, SUM(kp.accidents) AS accidents, SUM(kp.pop) AS pop FROM kp JOIN w ON kp.year BETWEEN w.y0 AND w.y1 GROUP BY w.period, w.ord, kp.area_name),
r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY period ORDER BY deaths / pop DESC, area_name) AS rn_hi, ROW_NUMBER() OVER (PARTITION BY period ORDER BY deaths / pop ASC, area_name) AS rn_lo FROM s)
SELECT period, ord, ROUND(SUM(CASE WHEN rn_hi <= 10 THEN accidents END) / SUM(CASE WHEN rn_hi <= 10 THEN pop END) * 100000) AS hi_acc_per_100k, ROUND(SUM(CASE WHEN rn_lo <= 10 THEN accidents END) / SUM(CASE WHEN rn_lo <= 10 THEN pop END) * 100000) AS lo_acc_per_100k, ROUND(SUM(CASE WHEN rn_hi <= 10 THEN deaths END) / SUM(CASE WHEN rn_hi <= 10 THEN accidents END) * 1000, 2) AS hi_deaths_per_1000, ROUND(SUM(CASE WHEN rn_lo <= 10 THEN deaths END) / SUM(CASE WHEN rn_lo <= 10 THEN accidents END) * 1000, 2) AS lo_deaths_per_1000, ROUND(CORR(deaths / pop, accidents / pop), 2) AS corr_death_vs_accident FROM r GROUP BY period, ord ORDER BY ord
```

```sql id=group_members
-- group_compare の多い10・少ない10に入った都道府県（死者の多い順・少ない順）
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K3103' AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name != '全国' AND year <= 2024),
w AS (SELECT * FROM (VALUES ('1975〜77年', 1, 1975, 1977), ('1990〜92年', 2, 1990, 1992), ('2010〜12年', 3, 2010, 2012), ('2022〜24年', 4, 2022, 2024)) AS t(period, ord, y0, y1)),
s AS (SELECT w.period, w.ord, k.area_name, SUM(k.deaths) AS deaths, SUM(p.pop) AS pop FROM k JOIN p ON k.area_name = p.area_name AND k.year = p.year JOIN w ON k.year BETWEEN w.y0 AND w.y1 GROUP BY w.period, w.ord, k.area_name),
r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY period ORDER BY deaths / pop DESC, area_name) AS rn_hi, ROW_NUMBER() OVER (PARTITION BY period ORDER BY deaths / pop ASC, area_name) AS rn_lo FROM s)
SELECT period, string_agg(CASE WHEN rn_hi <= 10 THEN area_name END, '・' ORDER BY rn_hi) AS hi_10, string_agg(CASE WHEN rn_lo <= 10 THEN area_name END, '・' ORDER BY rn_lo) AS lo_10 FROM r GROUP BY period, ord ORDER BY ord
```

```sql id=pref_2022_24
-- 2022〜24年の3年合算。人口あたりは3年分の人口の合計で割るので、1年あたりの値になる
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year BETWEEN 2022 AND 2024 GROUP BY area_name, year),
p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name != '全国' AND year BETWEEN 2022 AND 2024)
SELECT k.area_name, ROUND(SUM(k.accidents) / SUM(p.pop) * 100000) AS acc_per_100k, ROUND(SUM(k.deaths) / SUM(p.pop) * 100000, 2) AS deaths_per_100k, ROUND(SUM(k.deaths) / SUM(k.accidents) * 1000, 2) AS deaths_per_1000 FROM k JOIN p ON k.area_name = p.area_name AND k.year = p.year GROUP BY k.area_name ORDER BY deaths_per_100k DESC, k.area_name
```

```sql id=tokyo_min
-- 人口10万人あたり死者数が最も少ない都道府県が東京都だった年の数（プロットはしない）
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K3103' AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name != '全国' AND year <= 2024),
r AS (SELECT k.year, k.area_name, ROW_NUMBER() OVER (PARTITION BY k.year ORDER BY k.deaths / p.pop, k.area_name) AS rn FROM k JOIN p ON k.area_name = p.area_name AND k.year = p.year)
SELECT COUNT(DISTINCT year) AS years, COUNT(DISTINCT CASE WHEN rn = 1 AND area_name = '東京都' THEN year END) AS tokyo_lowest_years, MIN(year) AS first_year, MAX(year) AS last_year FROM r
```

```sql id=fixed_groups
-- 2022〜24年に人口10万人あたり死者数が多かった10県・少なかった10都府県の顔ぶれを固定し、各期間の人口10万人あたり事故件数を出す
WITH k AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3103' THEN TRY_CAST(value AS DOUBLE) END) AS deaths, MAX(CASE WHEN cat01 = 'K3101' THEN TRY_CAST(value AS DOUBLE) END) AS accidents FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3101', 'K3103') AND area_name != '全国' AND year <= 2024 GROUP BY area_name, year),
p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name != '全国' AND year <= 2024),
kp AS (SELECT k.area_name, k.year, k.deaths, k.accidents, p.pop FROM k JOIN p ON k.area_name = p.area_name AND k.year = p.year),
g AS (SELECT area_name, ROW_NUMBER() OVER (ORDER BY SUM(deaths) / SUM(pop) DESC, area_name) AS rn_hi, ROW_NUMBER() OVER (ORDER BY SUM(deaths) / SUM(pop) ASC, area_name) AS rn_lo FROM kp WHERE year BETWEEN 2022 AND 2024 GROUP BY area_name),
w AS (SELECT * FROM (VALUES ('1975〜77年', 1, 1975, 1977), ('1990〜92年', 2, 1990, 1992), ('2010〜12年', 3, 2010, 2012), ('2022〜24年', 4, 2022, 2024)) AS t(period, ord, y0, y1))
SELECT w.period, w.ord, ROUND(SUM(CASE WHEN g.rn_hi <= 10 THEN kp.accidents END) / SUM(CASE WHEN g.rn_hi <= 10 THEN kp.pop END) * 100000) AS hi_acc_per_100k, ROUND(SUM(CASE WHEN g.rn_lo <= 10 THEN kp.accidents END) / SUM(CASE WHEN g.rn_lo <= 10 THEN kp.pop END) * 100000) AS lo_acc_per_100k, ROUND(SUM(kp.accidents) / SUM(kp.pop) * 100000) AS all_acc_per_100k FROM kp JOIN g ON kp.area_name = g.area_name JOIN w ON kp.year BETWEEN w.y0 AND w.y1 GROUP BY w.period, w.ord ORDER BY w.ord
```
