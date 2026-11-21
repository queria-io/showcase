---
title: 精神障害者手帳は26年で14倍、少なかった県ほど速く伸びて地域差は縮んだ
description: 精神障害者保健福祉手帳の交付件数は1997年度の10.7万件から2023年度の152万件へ14.2倍になりました。人口あたりの件数で上位10と下位10の都道府県の差は2.5倍から1.48倍に縮み、2005年度に少なかった10県はすべて3.75倍以上に伸びました
publishedAt: 2026-03-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 精神保健
  - 福祉
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 衛生行政報告例
    url: https://www.mhlw.go.jp/toukei/list/36-19.html
    publisher: 厚生労働省
  - title: 障害者手帳について
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/techou.html
    publisher: 厚生労働省
  - title: 項目定義 J 福祉・社会保障
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/J
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 精神障害者手帳の人口10万人あたり件数（J1301÷A1101）を2005年度と2023年度で都道府県別に出して、2005年度に少なかった10県と多かった10府県の伸びを比べて。
socialAnnounce: |-
  精神障害者手帳の交付件数は1997年度の10.7万件から2023年度の152万件へ、26年で14倍になりました。

  人口あたりの件数で上位10と下位10の都道府県を比べると、差は2.5倍から1.48倍に縮んでいます。
  少なかった県ほど速く伸びました。
---

精神障害者保健福祉手帳の件数は、1997年度の10万6,821件から2023年度の151万9,474件へ、26年で14.2倍になりました。人口あたりの件数は、手帳が少なかった県ほど速く伸びています。人口10万人あたりの件数が多い10の都道府県の平均は、少ない10の都道府県の平均の2.5倍でしたが、2023年度には1.48倍に縮みました。

[精神障害者保健福祉手帳](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/techou.html)は、一定程度の精神障害の状態にあると認められた人に交付される手帳で、等級は1級から3級まであります。1995年に始まりました。

## 全国の件数は26年で14.2倍になった

全国の件数は、1997年度の10万6,821件から2023年度の151万9,474件へ14.2倍になりました。集計しているのは各年度末の3月31日に交付台帳に記載されている手帳の件数で、その年度に新しく交付した件数ではありません。手帳の件数は診断を受けて申請し、認定された人の数なので、県の間の差には、受診や申請の広がり方の違いも含まれます。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"certificates\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#8b5cf6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#8b5cf6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "certificates", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "certificates",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "交付件数（件）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

増え方は近年ほど大きく、前年度からの増加は2012〜2015年度が年5万〜6万件、2021〜2023年度は7万5,649件から9万8,589件でした。2008年度はほぼ横ばい（前年度から2,970件増）で、この年度は13府県で件数が前年度から1割以上減っています。2010年度も1万6,249件増にとどまりました。この年度は5県で件数が前年度から1割以上減っており、そのうち宮城県は東日本大震災の影響で仙台市以外の市町村の数値が含まれていません（[項目定義 J](https://www.e-stat.go.jp/koumoku/koumoku_teigi/J)の注意事項）。

## 上位10と下位10の都道府県の差は、2.5倍から1.48倍に縮んだ

人口10万人あたりの件数で47都道府県を並べ、多いほうから10の都道府県の平均を少ないほうから10の平均で割ると、1997年度の2.5倍から2023年度の1.48倍まで下がりました。最も多い県と最も少ない県の比も、4.12倍から2.02倍になっています。

```chart
{
  "layer": [
    {
      "data": {"name": "gap_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"top10_bottom10\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#8b5cf6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "top10_bottom10", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "top10_bottom10",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり件数の比（倍）", "grid": true}
        },
        "color": {
          "datum": "上位10の平均 ÷ 下位10の平均",
          "type": "nominal",
          "scale": {
            "domain": ["上位10の平均 ÷ 下位10の平均", "最大の県 ÷ 最小の県"],
            "range": ["#8b5cf6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "gap_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"max_min\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "max_min", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "max_min",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり件数の比（倍）", "grid": true}
        },
        "color": {
          "datum": "最大の県 ÷ 最小の県",
          "type": "nominal",
          "scale": {
            "domain": ["上位10の平均 ÷ 下位10の平均", "最大の県 ÷ 最小の県"],
            "range": ["#8b5cf6", "#94a3b8"]
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

最大÷最小は、1つの県の件数の変化で大きく動きます。県の件数には前年度から1割以上減る年度があり（2008年度は13府県）、2015年度に最大÷最小が2.86倍に上がったのは、最も少なかった滋賀県の件数が2年続けて減ったためです。上位10と下位10の平均の比は、1つの県の変化の影響を受けにくい指標です。

```sql
SELECT * FROM drops
```

## 2005年度に少なかった10県はすべて3.75倍以上に伸びた

差が縮んだのは、件数が少なかった県が速く伸びたためです。下の図は、横軸に2005年度の人口10万人あたりの件数、縦軸に2005年度から2023年度までの伸び（人口あたりの件数の倍率）を取っています。

```chart
{
  "layer": [
    {
      "data": {"name": "convergence"},
      "mark": {"type": "point", "color": "#8b5cf6", "opacity": 0.8, "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "per_100k_2005", "type": "quantitative"},
          {"field": "growth", "type": "quantitative"}
        ],
        "x": {
          "field": "per_100k_2005",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2005年度の人口10万人あたり件数（件）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2005→2023年度の伸び（倍）", "grid": true}
        }
      }
    }
  ]
}
```

2005年度に件数が少なかった10県（福井県・岡山県・奈良県・千葉県・石川県・栃木県・埼玉県・三重県・滋賀県・高知県）は、伸びが最も小さい高知県でも3.75倍でした。多かった10府県の伸びは、最も大きい大阪府でも3.21倍で、2つの区分の伸びは重なりません。少なかった10県の2023年度の平均（10万人あたり1,162件）は、多かった10府県の平均（1,286件）より少ないものの、残りの27都道府県の平均（1,141件）を上回っています。

```sql
SELECT * FROM group_summary
```

都道府県の順位は大きく変わりました。奈良県は2005年度の45位から2023年度の6位へ、福井県は47位から20位へ上がり、3位だった青森県は37位になっています。2005年度に1位だった沖縄県も32位ですが、沖縄県は2009年度から2012年度に件数が6割減っており、順位の低下の多くはこの期間に起きています。その後は2016年度に21位まで上がり、2023年度は32位です。

```sql
SELECT * FROM okinawa_trend
```

2005年度の水準と伸びの相関（対数）は−0.81です。伸びは起点の年度の値で割るので、起点の年度の一時的な増減だけでも負の相関が出ます。起点を1997年度・2012年度・2016年度に変えても、負の相関は残ります。

```sql
SELECT * FROM convergence_corr
```

## 2023年度は広島県が10万人あたり1,536件で最も多く、山形県の761件の2.02倍

2023年度の人口10万人あたりの件数は、広島県の1,536件が最も多く、大阪府の1,506件が続きます。最も少ないのは山形県の761件で、広島県との差は2.02倍です。

```chart
{
  "height": 780,
  "layer": [
    {
      "data": {"name": "pref_rate"},
      "mark": {"type": "bar", "color": "#8b5cf6"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり交付件数（件）", "grid": true}
        },
        "y": {
          "field": "area_name",
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

手帳の交付は住所地の都道府県が行うので、県外の医療機関に通院している人も住所地の県に集計されます。

```sql
SELECT * FROM pref_table
```

## まとめ

- 精神障害者保健福祉手帳の件数は、1997年度の10万6,821件から2023年度の151万9,474件へ14.2倍になった
- 人口10万人あたりの件数で、上位10の都道府県の平均と下位10の平均の比は1997年度の2.5倍から2023年度の1.48倍に縮んだ
- 2005年度に少なかった10県はすべて3.75倍以上に伸び、多かった10府県はすべて3.21倍以下だった。奈良県は45位から6位へ、青森県は3位から37位へ動いた

自分の県が2005年度から2023年度にどれだけ伸び、順位がどう動いたかは、上の表で確認できます。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年10月6日時点で集計しています。精神障害者保健福祉手帳の交付件数（J1301）の元データは厚生労働省の[衛生行政報告例](https://www.mhlw.go.jp/toukei/list/36-19.html)の「精神障害者保健福祉手帳交付台帳登載数」で、定義は[項目定義 J 福祉・社会保障](https://www.e-stat.go.jp/koumoku/koumoku_teigi/J)によります。人口10万人あたりの値は、同じ体系の各年10月1日現在の総人口（A1101）で割っています。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[都道府県別の福祉統計テーブル](/datasets/queria/e_stat/ssds/j_pref_welfare)から、自分の県の件数を1997年度から年度ごとに確認できます。

```sql id=national_trend
SELECT year, TRY_CAST(value AS DOUBLE) AS certificates, TRY_CAST(value AS DOUBLE) - LAG(TRY_CAST(value AS DOUBLE)) OVER (ORDER BY year) AS increase FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J1301' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=gap_trend
WITH r AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100000 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1301' AND w.area_name != '全国' AND w.value IS NOT NULL AND w.year BETWEEN 1997 AND 2023 ), k AS ( SELECT year, rate, ROW_NUMBER() OVER (PARTITION BY year ORDER BY rate DESC, area_name) AS hi, ROW_NUMBER() OVER (PARTITION BY year ORDER BY rate, area_name) AS lo FROM r ) SELECT year, ROUND(MAX(rate) / MIN(rate), 2) AS max_min, ROUND(AVG(rate) FILTER (WHERE hi <= 10) / AVG(rate) FILTER (WHERE lo <= 10), 2) AS top10_bottom10, COUNT(*) AS prefs FROM k GROUP BY year ORDER BY year
```

```sql id=drops
WITH c AS ( SELECT year, area_name, CAST(value AS DOUBLE) AS cnt, LAG(CAST(value AS DOUBLE)) OVER (PARTITION BY area_name ORDER BY year) AS prev FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J1301' AND area_name != '全国' AND year BETWEEN 1997 AND 2023 ) SELECT year AS 年度, COUNT(*) AS 前年度から1割以上減った都道府県数, STRING_AGG(area_name, '・' ORDER BY cnt / prev) AS 都道府県 FROM c WHERE cnt < prev * 0.9 GROUP BY year ORDER BY year
```

```sql id=convergence
WITH r AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100000 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1301' AND w.area_name != '全国' AND w.value IS NOT NULL AND w.year BETWEEN 1997 AND 2023 ), w AS ( SELECT a.area_name, a.rate AS r05, b.rate AS r23 FROM r a JOIN r b ON a.area_name = b.area_name AND a.year = 2005 AND b.year = 2023 ) SELECT area_name, ROUND(r05, 1) AS per_100k_2005, ROUND(r23 / r05, 2) AS growth FROM w ORDER BY r05
```

```sql id=group_summary
WITH r AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100000 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1301' AND w.area_name != '全国' AND w.value IS NOT NULL AND w.year IN (2005, 2023) ), w AS ( SELECT a.area_name, a.rate AS r05, b.rate AS r23 FROM r a JOIN r b ON a.area_name = b.area_name AND a.year = 2005 AND b.year = 2023 ), g AS ( SELECT *, CASE WHEN ROW_NUMBER() OVER (ORDER BY r05, area_name) <= 10 THEN '1. 2005年度に少なかった10県' WHEN ROW_NUMBER() OVER (ORDER BY r05 DESC, area_name) <= 10 THEN '3. 2005年度に多かった10府県' ELSE '2. 残りの27都道府県' END AS grp FROM w ) SELECT grp AS 区分, ROUND(AVG(r05)) AS "2005年度（10万人あたり・平均）", ROUND(AVG(r23)) AS "2023年度（10万人あたり・平均）", ROUND(MIN(r23 / r05), 2) AS 伸びの最小, ROUND(MAX(r23 / r05), 2) AS 伸びの最大, COUNT(*) AS 都道府県数 FROM g GROUP BY grp ORDER BY grp
```

```sql id=convergence_corr
WITH r AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100000 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1301' AND w.area_name != '全国' AND w.value IS NOT NULL AND w.year BETWEEN 1997 AND 2023 ), w AS ( SELECT a.year AS base_year, a.area_name, a.rate AS r0, b.rate AS r23 FROM r a JOIN r b ON a.area_name = b.area_name AND b.year = 2023 WHERE a.year IN (1997, 2005, 2012, 2016) ) SELECT base_year AS 起点の年度, ROUND(CORR(LN(r0), LN(r23 / r0)), 2) AS "起点の水準と伸びの相関（対数）", ROUND(CORR(r0, r23), 2) AS "起点と2023年度の水準の相関", COUNT(*) AS 都道府県数 FROM w GROUP BY base_year ORDER BY base_year
```

```sql id=okinawa_trend
WITH r AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) AS cnt, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100000 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1301' AND w.area_name != '全国' AND w.value IS NOT NULL AND w.year BETWEEN 2005 AND 2023 ), k AS ( SELECT *, RANK() OVER (PARTITION BY year ORDER BY rate DESC) AS rnk FROM r ) SELECT year AS 年度, cnt AS 件数, ROUND(rate, 1) AS "10万人あたり", rnk AS 順位 FROM k WHERE area_name = '沖縄県' ORDER BY year
```

```sql id=pref_rate
WITH hand AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS hand_cnt FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J1301' AND time_name = '2023年度' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND time_name = '2023年度' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ) SELECT h.area_name, ROUND(h.hand_cnt / p.population * 100000, 1) AS per_100k FROM hand h JOIN pop p ON h.area_name = p.area_name ORDER BY per_100k DESC
```

```sql id=pref_table
WITH r AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100000 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1301' AND w.area_name != '全国' AND w.value IS NOT NULL AND w.year IN (2005, 2023) ), w AS ( SELECT a.area_name, a.rate AS r05, b.rate AS r23 FROM r a JOIN r b ON a.area_name = b.area_name AND a.year = 2005 AND b.year = 2023 ) SELECT area_name AS 都道府県, ROUND(r05, 1) AS "2005年度（10万人あたり）", RANK() OVER (ORDER BY r05 DESC) AS "2005年度の順位", ROUND(r23, 1) AS "2023年度（10万人あたり）", RANK() OVER (ORDER BY r23 DESC) AS "2023年度の順位", ROUND(r23 / r05, 2) AS "伸び（倍）" FROM w ORDER BY r23 DESC, area_name
```
