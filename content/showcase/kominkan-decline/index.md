---
title: 公民館が1館も無い市区町村は16年で172から341に増え、人口が増えた市区町村でも公民館は14.1%減った
description: 市区町村別の公民館数を2005年度から2021年度まで集計しました。1館も無い市区町村は172から341に増え、人口が増えた351市区町村でも14.1%減っています。
ogDescription: 市区町村別の公民館数を2005年度から2021年度まで集計しました。1館も無い市区町村は172から341に増えています。
publishedAt: 2026-09-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 公民館
  - 社会教育調査
  - 市区町村
datasets:
  - queria/e_stat
  - queria/soumu
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 社会教育調査
    url: https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm
    publisher: 文部科学省
  - title: 平成17年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2005/index.html
    publisher: 総務省統計局
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
agentHint: e_stat.ssds.g_municipal_culture の公民館数（G1201）と図書館数（G1401）を、自分の県の市区町村別に2005年度から2021年度まで並べて出して。どの市区町村がいつ減らしたのか見たい
socialAnnounce: |-
  市区町村別の公民館数と図書館数を、2005年度から2021年度まで数えました。

  地域向けの講座や教室の会場を探すとき、公共施設の再編計画を読むときに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

公民館が1館も無い市区町村は、2005年度の172から2021年度の341に増えました。全国1,741市区町村の19.6%です。2005年から2020年に人口が増えた351市区町村でも、公民館は14.1%減っています。都道府県別では静岡県が77.9%減で最も大きく、増えたのは沖縄県だけでした。

高齢者向けの体操教室、子育て中の親が集まるサロン、住民向けの連続講座などを地域で開くとき、会場の候補になるのが市区町村の設置する公民館です。この記事では、文部科学省の[社会教育調査](https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm)をもとにした市区町村別の公民館数を、2005年度から2021年度まで集計しました。

## 全国の公民館は1999年度から27.9%減り、図書館は1975年度の3.2倍になった

このデータは e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の「G 文化・スポーツ」分野から取得しています。市区町村別のテーブル（`g_municipal_culture`）に収録されているのは次の2つで、どちらも1995年度から2021年度までです。

| コード | 内容     |
| ------ | -------- |
| G1201  | 公民館数 |
| G1401  | 図書館数 |

公民館数は社会教育法第21条の公民館の数で、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/G)にあるとおり分館も1館として計上されます。図書館数は図書館法第2条の図書館と同法第29条の図書館同種施設のうち、地方公共団体が設置したものの数です。こちらも分館を1館と数え、学校図書館・国立の図書館・企業内図書館は含みません。どちらも10月1日現在の数字です。

都道府県別のテーブル（`g_pref_culture`）は同じ2つを1975年度から持ち、2005年度からの公民館類似施設数（`G1301`）をはじめ、この分野の指標をより幅広く収録しています。全国の推移は、こちらのテーブルから集計しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kominkan\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "kominkan", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "kominkan",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "施設数（館）", "grid": true}
        },
        "color": {
          "datum": "公民館",
          "type": "nominal",
          "scale": {"domain": ["公民館", "図書館"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"library\"]) ? 0 : 1",
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
          {"field": "library", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "library",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "施設数（館）", "grid": true}
        },
        "color": {
          "datum": "図書館",
          "type": "nominal",
          "scale": {"domain": ["公民館", "図書館"], "range": ["#f97316", "#3b82f6"]},
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

公民館は1999年度の18,257館がピークで、2021年度は13,163館です。22年で5,094館、27.9%減りました。図書館は1975年度の1,066館から2021年度の3,394館へと3.2倍になっています。社会教育調査はおおむね3年おきの調査なので、線は調査があった年度どうしをつないでいます。

この統計は社会教育法上の公民館の数なので、同じ建物がコミュニティセンターなどに変わって社会教育法の公民館でなくなった場合も、減少に含まれます。公民館でなくなった施設では、登録団体の制度・利用料・営利利用の可否は、その自治体が新しく定めたルールに変わります。

同じ調査の公民館類似施設数（`G1301`）も、2005年度の1,039から2021年度の635へ減っています。公民館から外れた施設が公民館類似施設に移ったわけではないと考えられます。

## 公民館が1館も無い市区町村は、2005年度の172から2021年度の341に増えた

会場を探すときは、全国の合計より、活動する市区町村にいくつ公民館が残っているかが必要です。市区町村ごとに集計しました。

対象は東京23区を含む1,741市区町村です。このテーブルには政令指定都市の市の合計と行政区の両方、それに東京都の「特別区部」という合計行も入っていて、そのまま合計すると二重に集計することになります。標準地域コードのテーブル（`soumu.code.municipality`）の `is_municipality` で市区町村の行だけに絞っています。市区町村の数は2005年度から2021年度まで1,741で変わらないので、平成の大合併の前後を同じ単位で比較できます。

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "zero_trend"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "zero_munis", "type": "quantitative"},
          {"field": "year", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "zero_munis",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "公民館が1館も無い市区町村（団体）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "zero_trend"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "zero_munis",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "公民館が1館も無い市区町村（団体）", "grid": true}
        },
        "text": {"field": "zero_munis"}
      }
    }
  ]
}
```

公民館が1館も無い市区町村は、2005年度の172から2021年度の341へ増えました。1,741市区町村の19.6%、およそ5分の1です。調査のたびに増えていて、減った回はありません。

この16年の増減を市区町村ごとに分けると、公民館が減ったのが633市区町村、増えたのが176、変わらなかったのが932でした。減った市区町村の減少分を合計すると4,596館、増えた市区町村の増加分は620館です。2005年度には公民館があったのに2021年度には無くなった市区町村は175あります。公民館も図書館もどちらも無い市区町村は、2021年度で94です。

公民館が減った633市区町村のうち、同じ期間に図書館が増えたのは137（21.6%）です。残る8割近くの市区町村では、公民館が減り、図書館は増えていません。全国の合計で図書館が増えていても、公民館の代わりに図書館ができたとは限りません。

## 人口が増えた市区町村でも、公民館は14.1%減った

市区町村を人口の増減で2つに分けて、公民館の増減を比較しました。人口は国勢調査の2005年と2020年、公民館と図書館は社会教育調査の2005年度と2021年度の値で、どちらも10月1日現在です。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "pop_split"},
      "transform": [
        {"fold": ["kominkan_pct", "library_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"kominkan_pct\": \"公民館\", \"library_pct\": \"図書館\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"kominkan_pct\",\"library_pct\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "grp",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年度から2021年度の変化率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["公民館", "図書館"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["公民館", "図書館"]},
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

2005年から2020年に人口が増えた市区町村は351、減った市区町村は1,390でした。人口が増えた351市区町村でも、公民館は14.1%減っています。人口が減った1,390市区町村の25.0%減より小さいものの、どちらも減っています。人口が増えている市区町村でも、公共の会場が増えているとは限りません。

図書館はどちらの群でも増えていて、人口が増えた市区町村で11.1%、減った市区町村で15.5%です。公民館が減り図書館が増える動きは人口の増減に関係なく起きていて、増減の幅は人口が減った市区町村のほうが大きくなっています。

## 静岡県は77.9%減り、石川県・愛媛県は2.7%減にとどまる

47都道府県を、2005年度から2021年度の公民館数の変化率の順に並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_high"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年度から2021年度の公民館数の変化率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "減少が小さい10",
          "type": "nominal",
          "scale": {
            "domain": ["減少が小さい10", "中間27", "減少が大きい10"],
            "range": ["#3b82f6", "#93c5fd", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年度から2021年度の公民館数の変化率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間27",
          "type": "nominal",
          "scale": {
            "domain": ["減少が小さい10", "中間27", "減少が大きい10"],
            "range": ["#3b82f6", "#93c5fd", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_low"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年度から2021年度の公民館数の変化率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "減少が大きい10",
          "type": "nominal",
          "scale": {
            "domain": ["減少が小さい10", "中間27", "減少が大きい10"],
            "range": ["#3b82f6", "#93c5fd", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ]
}
```

公民館が増えたのは沖縄県だけで、84館から88館へ4.8%増えました。残る46都道府県はすべて減っています。最も減ったのは静岡県で、226館から50館へ77.9%減りました。次いで滋賀県が188館から78館へ58.5%減、島根県が348館から156館へ55.2%減です。施設の名称と根拠法が変わった分も、この減少に含まれます。

石川県は298館から290館（2.7%減）、愛媛県は445館から433館（2.7%減）と、ほとんど変わっていません。同じ16年の間に、7割以上減った県とほぼ変わらない県があります。隣の県の状況から、自分の県の公民館の数は推測できません。

## 会場を探すときにどう使うか

- 事業を広げたい市区町村について、公民館数の推移を確認する。都道府県の平均ではなく、その市区町村の数字を見る
- 公民館が1館も無い市区町村では、図書館やコミュニティセンター、民間施設を前提に会場計画を組む。2021年度時点で341市区町村が該当する
- 自治体が公共施設の再編を議論しているときは、その自治体がこれまでに何館減らしてきたかを先に確認する。すでに減らした自治体とこれから減らす自治体では、数年後に残る会場の数が変わる
- 公民館が残っている市区町村でも、社会教育法上の公民館のままかを自治体のサイトで確認する。名称が変われば利用登録や利用料の扱いも変わる

## データの出典

本記事は e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)（総務省統計局）に収録された `e_stat.ssds.g_municipal_culture`・`e_stat.ssds.g_pref_culture`・`e_stat.ssds.a_municipal_population`・`soumu.code.municipality` を2026年9月13日時点で取得して集計しています。公民館数（G1201）と図書館数（G1401）のもとになっているのは文部科学省の[社会教育調査](https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm)、総人口（A1101）は総務省の国勢調査（[平成17年](https://www.stat.go.jp/data/kokusei/2005/index.html)・[令和2年](https://www.stat.go.jp/data/kokusei/2020/index.html)）です。

Queriaは、省庁ごとに別々に公表されるこれらのオープンデータを、列名・単位・文字コードを統一し、同じ地域コードで結合できる形で公開しています。本記事で使った[市区町村別の文化・スポーツテーブル](/datasets/queria/e_stat/ssds/g_municipal_culture)で担当エリアの公民館数の推移を確認したり、[市区町村別の人口テーブル](/datasets/queria/e_stat/ssds/a_municipal_population)と結合して人口あたりの館数を出したりできます。

```sql id=g_categories
SELECT 'g_municipal_culture' AS table_name, cat01, MAX(item_name) AS item_name, MIN(year) AS min_year, MAX(year) AS max_year FROM e_stat.ssds.g_municipal_culture GROUP BY cat01 UNION ALL SELECT 'g_pref_culture', cat01, MAX(item_name), MIN(year), MAX(year) FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G1201', 'G1301', 'G1401') GROUP BY cat01 ORDER BY 1, 2
```

```sql id=similar_facilities
SELECT year, TRY_CAST(value AS DOUBLE) AS similar_facilities FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G1301' AND area = '00000' AND value IS NOT NULL AND year <= 2021 ORDER BY year
```

```sql id=national
SELECT year, MAX(CASE WHEN cat01 = 'G1201' THEN TRY_CAST(value AS DOUBLE) END) AS kominkan, MAX(CASE WHEN cat01 = 'G1401' THEN TRY_CAST(value AS DOUBLE) END) AS library FROM e_stat.ssds.g_pref_culture WHERE area = '00000' AND cat01 IN ('G1201', 'G1401') AND value IS NOT NULL AND year <= 2021 GROUP BY year ORDER BY year
```

```sql id=zero_trend
SELECT year, CAST(SUM(CASE WHEN TRY_CAST(g.value AS DOUBLE) = 0 THEN 1 ELSE 0 END) AS INTEGER) AS zero_munis, COUNT(*) AS munis FROM e_stat.ssds.g_municipal_culture g JOIN soumu.code.municipality m ON g.area = m.area_code AND m.is_municipality WHERE g.cat01 = 'G1201' AND g.year >= 2005 AND g.year <= 2021 GROUP BY year ORDER BY year
```

```sql id=change_mix
WITH fac AS (SELECT g.area, MAX(CASE WHEN g.cat01 = 'G1201' AND g.year = 2005 THEN TRY_CAST(g.value AS DOUBLE) END) AS k05, MAX(CASE WHEN g.cat01 = 'G1201' AND g.year = 2021 THEN TRY_CAST(g.value AS DOUBLE) END) AS k21, MAX(CASE WHEN g.cat01 = 'G1401' AND g.year = 2005 THEN TRY_CAST(g.value AS DOUBLE) END) AS l05, MAX(CASE WHEN g.cat01 = 'G1401' AND g.year = 2021 THEN TRY_CAST(g.value AS DOUBLE) END) AS l21 FROM e_stat.ssds.g_municipal_culture g JOIN soumu.code.municipality m ON g.area = m.area_code AND m.is_municipality WHERE g.year IN (2005, 2021) GROUP BY g.area) SELECT COUNT(*) AS munis, CAST(SUM(CASE WHEN k21 < k05 THEN 1 ELSE 0 END) AS INTEGER) AS kominkan_decreased, CAST(SUM(CASE WHEN k21 > k05 THEN 1 ELSE 0 END) AS INTEGER) AS kominkan_increased, CAST(SUM(CASE WHEN k21 = k05 THEN 1 ELSE 0 END) AS INTEGER) AS kominkan_unchanged, SUM(CASE WHEN k21 < k05 THEN k05 - k21 ELSE 0 END) AS halls_lost, SUM(CASE WHEN k21 > k05 THEN k21 - k05 ELSE 0 END) AS halls_added, CAST(SUM(CASE WHEN k05 > 0 AND k21 = 0 THEN 1 ELSE 0 END) AS INTEGER) AS became_zero, CAST(SUM(CASE WHEN k21 < k05 AND l21 > l05 THEN 1 ELSE 0 END) AS INTEGER) AS kominkan_down_library_up, CAST(SUM(CASE WHEN k21 = 0 AND l21 = 0 THEN 1 ELSE 0 END) AS INTEGER) AS neither_2021 FROM fac
```

```sql id=pop_split
WITH fac AS (SELECT g.area, MAX(CASE WHEN g.cat01 = 'G1201' AND g.year = 2005 THEN TRY_CAST(g.value AS DOUBLE) END) AS k05, MAX(CASE WHEN g.cat01 = 'G1201' AND g.year = 2021 THEN TRY_CAST(g.value AS DOUBLE) END) AS k21, MAX(CASE WHEN g.cat01 = 'G1401' AND g.year = 2005 THEN TRY_CAST(g.value AS DOUBLE) END) AS l05, MAX(CASE WHEN g.cat01 = 'G1401' AND g.year = 2021 THEN TRY_CAST(g.value AS DOUBLE) END) AS l21 FROM e_stat.ssds.g_municipal_culture g JOIN soumu.code.municipality m ON g.area = m.area_code AND m.is_municipality WHERE g.year IN (2005, 2021) GROUP BY g.area), pop AS (SELECT p.area, MAX(CASE WHEN p.year = 2005 THEN TRY_CAST(p.value AS DOUBLE) END) AS p05, MAX(CASE WHEN p.year = 2020 THEN TRY_CAST(p.value AS DOUBLE) END) AS p20 FROM e_stat.ssds.a_municipal_population p JOIN soumu.code.municipality m ON p.area = m.area_code AND m.is_municipality WHERE p.cat01 = 'A1101' AND p.year IN (2005, 2020) GROUP BY p.area) SELECT CASE WHEN pop.p20 > pop.p05 THEN '人口が増えた市区町村' ELSE '人口が減った市区町村' END AS grp, COUNT(*) AS munis, ROUND((SUM(fac.k21) - SUM(fac.k05)) * 100.0 / SUM(fac.k05), 1) AS kominkan_pct, ROUND((SUM(fac.l21) - SUM(fac.l05)) * 100.0 / SUM(fac.l05), 1) AS library_pct FROM fac JOIN pop ON fac.area = pop.area WHERE fac.k05 IS NOT NULL AND fac.k21 IS NOT NULL AND fac.l05 IS NOT NULL AND fac.l21 IS NOT NULL AND pop.p05 IS NOT NULL AND pop.p20 IS NOT NULL GROUP BY 1 ORDER BY 1
```

```sql id=pref_high
WITH pref AS (SELECT area_name, MAX(CASE WHEN year = 2005 THEN TRY_CAST(value AS DOUBLE) END) AS k05, MAX(CASE WHEN year = 2021 THEN TRY_CAST(value AS DOUBLE) END) AS k21 FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G1201' AND year IN (2005, 2021) AND area <> '00000' GROUP BY area_name), ranked AS (SELECT area_name, k05, k21, ROUND((k21 - k05) * 100.0 / k05, 1) AS pct, ROW_NUMBER() OVER (ORDER BY (k21 - k05) / k05 DESC, area_name) AS rn FROM pref WHERE k05 > 0) SELECT area_name, k05, k21, pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH pref AS (SELECT area_name, MAX(CASE WHEN year = 2005 THEN TRY_CAST(value AS DOUBLE) END) AS k05, MAX(CASE WHEN year = 2021 THEN TRY_CAST(value AS DOUBLE) END) AS k21 FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G1201' AND year IN (2005, 2021) AND area <> '00000' GROUP BY area_name), ranked AS (SELECT area_name, k05, k21, ROUND((k21 - k05) * 100.0 / k05, 1) AS pct, ROW_NUMBER() OVER (ORDER BY (k21 - k05) / k05 DESC, area_name) AS rn FROM pref WHERE k05 > 0) SELECT area_name, k05, k21, pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_low
WITH pref AS (SELECT area_name, MAX(CASE WHEN year = 2005 THEN TRY_CAST(value AS DOUBLE) END) AS k05, MAX(CASE WHEN year = 2021 THEN TRY_CAST(value AS DOUBLE) END) AS k21 FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G1201' AND year IN (2005, 2021) AND area <> '00000' GROUP BY area_name), ranked AS (SELECT area_name, k05, k21, ROUND((k21 - k05) * 100.0 / k05, 1) AS pct, ROW_NUMBER() OVER (ORDER BY (k21 - k05) / k05 DESC, area_name) AS rn FROM pref WHERE k05 > 0) SELECT area_name, k05, k21, pct FROM ranked WHERE rn > 37 ORDER BY rn
```
