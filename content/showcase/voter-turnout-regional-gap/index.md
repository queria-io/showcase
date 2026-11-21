---
title: 参院選の投票率で、人口上位7都府県とほかの40道府県の差は10.1ポイントから0.3ポイントに縮んだ
description: 2020年の人口上位7都府県の参院選の投票率は、1983〜1995年の平均でほかの40道府県より10.1ポイント低くなっていました。2013〜2022年の平均では差は0.3ポイントで、2022年は7都府県のほうが1.2ポイント高くなっています。
publishedAt: 2026-03-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 選挙
  - 投票率
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 衆議院議員総選挙・最高裁判所裁判官国民審査結果
    url: https://www.soumu.go.jp/senkyo/senkyo_s/data/shugiin/ichiran.html
    publisher: 総務省
  - title: 参議院議員通常選挙結果
    url: https://www.soumu.go.jp/senkyo/senkyo_s/data/sangiin/ichiran.html
    publisher: 総務省
  - title: 社会・人口統計体系 項目定義（G 文化・スポーツ）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/G
    publisher: 総務省統計局
agentHint: 参院選の比例代表の投票率（G6303）を都道府県別に1983〜1995年の平均と2013〜2022年の平均で比べて、下がり幅が小さい都道府県と大きい都道府県を出して
socialAnnounce: |-
  人口の多い7都府県の参院選の投票率は、1983〜1995年の平均で、ほかの40道府県より10.1ポイント低いものでした。

  2013〜2022年の平均では差は0.3ポイント。
  2022年は7都府県のほうが高くなっています。
---

参議院選挙の投票率は、東京都・神奈川県・大阪府・愛知県・埼玉県・千葉県・兵庫県の7都府県が、1983〜1995年の5回の平均で52.6%、ほかの40道府県が62.7%で、10.1ポイントの差がありました。2013〜2022年の4回の平均では、7都府県が51.8%、40道府県が52.1%で、差は0.3ポイントです。2022年の参議院選挙では、7都府県のほうが1.2ポイント高くなりました。差が縮んだのは、40道府県の投票率が10.6ポイント下がり、7都府県の下げ幅が0.8ポイントだったためです。

都市部の人ほど選挙に行かない、とよく言われます。1980〜90年代の参議院選挙の数字はそのとおりでしたが、最近の選挙では都道府県単位の差はほぼなくなっています。

## 参院選では14回のうち13回が大都市圏のほうが低く、2022年に逆転した

使ったのは e-Stat「社会・人口統計体系」の都道府県別の文化・スポーツデータ（`g_pref_culture`）に入っている国政選挙の投票率です。投票率は投票者数を選挙期日現在の有権者数で割った値で、`year` は選挙が行われた年です（`time_name` は「1996年度」のように年度の形ですが、値は選挙期日のものです）。

```sql
SELECT cat01 AS 分類コード, item_name AS 指標, min_year AS 収録開始, max_year AS 収録最終, year_count AS 選挙の回数 FROM coverage
```

以下の数字は、衆議院選挙の小選挙区（`G6301`）と参議院選挙の比例代表（`G6303`）の値です。収録は衆議院選挙が2021年の第49回まで、参議院選挙が2022年の第26回までで、2024年10月の衆議院選挙と2025年7月の参議院選挙は入っていません。

大都市圏の7都府県は、2020年の総人口の上位7都府県です。8位の北海道は可住地1平方キロあたり230人で、7都府県のうち最も低い千葉県（1,778人）の7分の1以下です。

```sql
SELECT * FROM metro_def
```

下の図は、選挙ごとに7都府県の平均から40道府県の平均を引いた差です。平均は都道府県の投票率をそのまま平均した値で、有権者の数で重みを付けていません。東京都も鳥取県も1県として同じ重さで扱っています。

```chart
{
  "layer": [
    {
      "data": {"name": "upper_gap"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"gap\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "選挙の年", "format": "d"}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "7都府県 − 40道府県（ポイント）", "grid": true}
        },
        "color": {
          "datum": "参議院選挙（比例代表）",
          "type": "nominal",
          "scale": {"domain": ["参議院選挙（比例代表）", "衆議院選挙（小選挙区）"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "lower_gap"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"gap\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "選挙の年", "format": "d"}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "7都府県 − 40道府県（ポイント）", "grid": true}
        },
        "color": {
          "datum": "衆議院選挙（小選挙区）",
          "type": "nominal",
          "scale": {"domain": ["参議院選挙（比例代表）", "衆議院選挙（小選挙区）"], "range": ["#f97316", "#3b82f6"]},
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

参議院選挙は1983年から2022年まで14回あり、2019年までの13回はすべて7都府県のほうが低い値でした。1995年までの5回は差が7.5〜12.1ポイントあり、最も大きかったのは衆参同日選挙だった1986年です。2013年に0.7ポイントまで縮み、2016年は1.1ポイント、2019年は0.7ポイントと1ポイント前後の差が続いたあと、2022年に初めて7都府県が1.2ポイント上回りました。

衆議院選挙でも差は縮んでいます。1996年は7都府県が8.0ポイント低く、2012年は0.5ポイント、2014年は0.2ポイントまで縮みました。2017年は再び4.3ポイントに広がり、2021年は1.2ポイントです。選挙ごとの変動は大きくなっています。

7都府県で区切らずに、人口密度との相関でも確認しました。都道府県の投票率と可住地の人口密度（対数）の相関は、参議院選挙の1986年が −0.71、2022年が0.01です。人口が密集している県ほど投票率が低いという関係は、2022年の参院選では見られません。2022年に7都府県が40道府県を上回ったのは7都府県で区切ったときの結果で、相関から言えるのは、人口密度による差がなくなったということです。

```sql
SELECT year AS 選挙の年, '参議院（比例代表）' AS 選挙, metro AS 大都市圏7都府県の平均, others AS ほかの40道府県の平均, gap AS 差, metro_in_lowest7 AS 下位7都道府県に入った大都市圏, density_corr AS 人口密度との相関 FROM upper_gap UNION ALL SELECT year, '衆議院（小選挙区）', metro, others, gap, metro_in_lowest7, density_corr FROM lower_gap ORDER BY 選挙, 選挙の年
```

表の「下位7都道府県に入った大都市圏」は、47都道府県を投票率の低い順に並べた下から7つのうち、7都府県がいくつあるかです。1996年の衆議院選挙では下から7つのうち6つが7都府県でしたが、2021年の衆議院選挙では0です。参議院選挙は2016年・2019年・2022年の3回続けて0です。

## 参院選の投票率は、7都府県で0.8ポイント、40道府県で10.6ポイント下がった

どちらの区分も選挙ごとに大きく上下するので、1回の選挙を起点にすると、どの年を選ぶかで下げ幅が変わります。図の下の表は、最初の数回と最後の数回の平均です。

```chart
{
  "layer": [
    {
      "data": {"name": "upper_gap"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"metro\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "metro", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "選挙の年", "format": "d"}
        },
        "y": {
          "field": "metro",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "投票率の平均（%）", "grid": true}
        },
        "color": {
          "datum": "参院選・大都市圏7都府県",
          "type": "nominal",
          "scale": {
            "domain": ["参院選・大都市圏7都府県", "参院選・ほかの40道府県", "衆院選・大都市圏7都府県", "衆院選・ほかの40道府県"],
            "range": ["#f97316", "#3b82f6", "#f97316", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "upper_gap"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"others\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "others", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "選挙の年", "format": "d"}
        },
        "y": {
          "field": "others",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "投票率の平均（%）", "grid": true}
        },
        "color": {
          "datum": "参院選・ほかの40道府県",
          "type": "nominal",
          "scale": {
            "domain": ["参院選・大都市圏7都府県", "参院選・ほかの40道府県", "衆院選・大都市圏7都府県", "衆院選・ほかの40道府県"],
            "range": ["#f97316", "#3b82f6", "#f97316", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "lower_gap"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"metro\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 2,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "metro", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "選挙の年", "format": "d"}
        },
        "y": {
          "field": "metro",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "投票率の平均（%）", "grid": true}
        },
        "color": {
          "datum": "衆院選・大都市圏7都府県",
          "type": "nominal",
          "scale": {
            "domain": ["参院選・大都市圏7都府県", "参院選・ほかの40道府県", "衆院選・大都市圏7都府県", "衆院選・ほかの40道府県"],
            "range": ["#f97316", "#3b82f6", "#f97316", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "lower_gap"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"others\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "others", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "選挙の年", "format": "d"}
        },
        "y": {
          "field": "others",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "投票率の平均（%）", "grid": true}
        },
        "color": {
          "datum": "衆院選・ほかの40道府県",
          "type": "nominal",
          "scale": {
            "domain": ["参院選・大都市圏7都府県", "参院選・ほかの40道府県", "衆院選・大都市圏7都府県", "衆院選・ほかの40道府県"],
            "range": ["#f97316", "#3b82f6", "#f97316", "#3b82f6"]
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

```sql
SELECT * FROM period_avg
```

参議院選挙では、1983〜1995年の5回の平均と2013〜2022年の4回の平均を比較すると、7都府県は0.8ポイント、40道府県は10.6ポイント下がっています。衆議院選挙の1996〜2003年の3回と2014〜2021年の3回では、7都府県が4.3ポイント、40道府県が9.0ポイントの低下です。参議院選挙の最初の期間には、7都府県の投票率が45.2%と39.4%だった1992年と1995年が入っています。この2回は40道府県の投票率も低いので、下げ幅は両方の区分で小さく出ます。参議院選挙でも衆議院選挙でも、表の期間で比較すると40道府県のほうが大きく下がっています。

収録されている2012〜2022年の国政選挙8回のうち、2017年の衆院選を除く7回は、7都府県と40道府県の差の大きさが0.2〜1.2ポイントです。参議院選挙の都道府県単位の数字では、都市部ほど投票率が低いという傾向はなくなっています。衆議院選挙は、2017年に差が4.3ポイントに広がったように、選挙ごとの変動がまだ大きくなっています。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年10月2日時点で集計しています。投票率の元データは総務省の[衆議院議員総選挙・最高裁判所裁判官国民審査結果](https://www.soumu.go.jp/senkyo/senkyo_s/data/shugiin/ichiran.html)と[参議院議員通常選挙結果](https://www.soumu.go.jp/senkyo/senkyo_s/data/sangiin/ichiran.html)で、投票率の定義は[項目定義（G 文化・スポーツ）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/G)にあります。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の文化・スポーツテーブル](/datasets/queria/e_stat/ssds/g_pref_culture)から、自分の県の投票率を40年分並べたり、統一地方選挙の投票率と比較したりできます。

```sql id=coverage
-- 投票率の各指標の収録期間（プロットはしない）
SELECT cat01, item_name, min_year, max_year, year_count FROM e_stat.ssds.series_coverage WHERE table_name = 'g_pref_culture' AND cat01 IN ('G6301', 'G6302', 'G6303', 'G6304') ORDER BY cat01
```

```sql id=metro_def
-- 2020年の総人口の上位8都道府県（プロットはしない）
WITH p AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS pop, TRY_CAST(value AS DOUBLE) / NULLIF(( SELECT TRY_CAST(l.value AS DOUBLE) FROM e_stat.ssds.b_pref_land l WHERE l.cat01 = 'B1103' AND l.year = 2020 AND l.area_name = a.area_name ), 0) * 100 AS density FROM e_stat.ssds.a_pref_population a WHERE cat01 = 'A1101' AND year = 2020 AND area_name <> '全国' ) SELECT RANK() OVER (ORDER BY pop DESC) AS 人口の順位, area_name AS 都道府県, ROUND(pop / 10000, 0) AS 総人口_万人, ROUND(density, 0) AS 可住地1平方キロあたり人口 FROM p ORDER BY pop DESC LIMIT 8
```

```sql id=upper_gap
WITH t AS ( SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS turnout, area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6303' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2022 ), d AS ( SELECT p.year, p.area_name, TRY_CAST(p.value AS DOUBLE) / TRY_CAST(l.value AS DOUBLE) AS density FROM e_stat.ssds.a_pref_population p JOIN e_stat.ssds.b_pref_land l ON l.area_name = p.area_name AND l.year = p.year AND l.cat01 = 'B1103' WHERE p.cat01 = 'A1101' AND p.area_name <> '全国' ), r AS ( SELECT t.*, d.density, RANK() OVER (PARTITION BY t.year ORDER BY t.turnout) AS low_rank FROM t LEFT JOIN d ON d.year = t.year AND d.area_name = t.area_name ) SELECT year, COUNT(*) AS prefectures, ROUND(AVG(turnout) FILTER (WHERE metro), 2) AS metro, ROUND(AVG(turnout) FILTER (WHERE NOT metro), 2) AS others, ROUND(AVG(turnout) FILTER (WHERE metro) - AVG(turnout) FILTER (WHERE NOT metro), 2) AS gap, COUNT(*) FILTER (WHERE metro AND low_rank <= 7) AS metro_in_lowest7, ROUND(CORR(turnout, LN(density)), 2) AS density_corr FROM r GROUP BY year ORDER BY year
```

```sql id=lower_gap
WITH t AS ( SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS turnout, area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6301' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021 ), d AS ( SELECT p.year, p.area_name, TRY_CAST(p.value AS DOUBLE) / TRY_CAST(l.value AS DOUBLE) AS density FROM e_stat.ssds.a_pref_population p JOIN e_stat.ssds.b_pref_land l ON l.area_name = p.area_name AND l.year = p.year AND l.cat01 = 'B1103' WHERE p.cat01 = 'A1101' AND p.area_name <> '全国' ), r AS ( SELECT t.*, d.density, RANK() OVER (PARTITION BY t.year ORDER BY t.turnout) AS low_rank FROM t LEFT JOIN d ON d.year = t.year AND d.area_name = t.area_name ) SELECT year, COUNT(*) AS prefectures, ROUND(AVG(turnout) FILTER (WHERE metro), 2) AS metro, ROUND(AVG(turnout) FILTER (WHERE NOT metro), 2) AS others, ROUND(AVG(turnout) FILTER (WHERE metro) - AVG(turnout) FILTER (WHERE NOT metro), 2) AS gap, COUNT(*) FILTER (WHERE metro AND low_rank <= 7) AS metro_in_lowest7, ROUND(CORR(turnout, LN(density)), 2) AS density_corr FROM r GROUP BY year ORDER BY year
```

```sql id=period_avg
WITH t AS ( SELECT cat01, year, TRY_CAST(value AS DOUBLE) AS turnout, area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G6301', 'G6303') AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2022 ), p AS ( SELECT CASE WHEN cat01 = 'G6303' THEN '参議院（比例代表）' ELSE '衆議院（小選挙区）' END AS house, CASE WHEN (cat01 = 'G6303' AND year <= 1995) OR (cat01 = 'G6301' AND year <= 2003) THEN 'early' WHEN (cat01 = 'G6303' AND year >= 2013) OR (cat01 = 'G6301' AND year >= 2014) THEN 'late' END AS period, year, turnout, metro FROM t ), g AS ( SELECT house, period, MIN(year) AS y0, MAX(year) AS y1, COUNT(DISTINCT year) AS n, AVG(turnout) FILTER (WHERE metro) AS metro, AVG(turnout) FILTER (WHERE NOT metro) AS others FROM p WHERE period IS NOT NULL GROUP BY house, period ) SELECT e.house AS 選挙, e.y0 || '〜' || e.y1 || '年（' || e.n || '回）' AS 最初の期間, l.y0 || '〜' || l.y1 || '年（' || l.n || '回）' AS 最後の期間, ROUND(e.metro, 1) AS 大都市圏7都府県_最初, ROUND(l.metro, 1) AS 大都市圏7都府県_最後, ROUND(e.metro - l.metro, 1) AS 大都市圏7都府県の低下, ROUND(e.others, 1) AS ほかの40道府県_最初, ROUND(l.others, 1) AS ほかの40道府県_最後, ROUND(e.others - l.others, 1) AS ほかの40道府県の低下, ROUND(e.others - e.metro, 1) AS 差_最初, ROUND(l.others - l.metro, 1) AS 差_最後 FROM g e JOIN g l ON l.house = e.house AND l.period = 'late' WHERE e.period = 'early' ORDER BY e.house
```
