---
title: 前年度より借金返済が重くなった市区町村は、2010〜15年度の1割前後から18年度以降は4割超へ
description: 市区町村の実質公債費比率の平均は2008〜2016年度に14.06%から7.55%へ下がり、その後の5年度で下がったのは0.50ポイントでした。前年度より比率を上げた団体は2010〜2015年度の毎年1割前後から、2018〜2021年度は毎年4割を超えています。
publishedAt: 2026-06-04
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 財政
  - 自治体
  - 公債費
  - 地方財政
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（D 行政基盤）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/D
    publisher: 総務省統計局
  - title: 地方公共団体の財政の健全化 早期健全化基準と財政再生基準
    url: https://www.soumu.go.jp/iken/zaisei/kenzenka/index3.html
    publisher: 総務省
  - title: 令和5年版 地方財政白書 令和3年度決算に基づく健全化判断比率等の状況
    url: https://www.soumu.go.jp/menu_seisaku/hakusyo/chihou/r05data/2023data/r05czb01-09.html
    publisher: 総務省
agentHint: 2016年度から2021年度に実質公債費比率(D2211)が3ポイント以上上がった市区町村を、都道府県別の団体数で数えて。2021年度の財政力指数(D2201)も並べて
socialAnnounce: |-
  市区町村の借金返済の重さ（実質公債費比率）が前年度より重くなった団体は、2010〜2015年度の毎年1割前後から、2018〜2021年度は毎年4割超に増えました。

  地方財政の比較に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

市区町村の借金返済の重さを表す実質公債費比率は、2008年度から2016年度にかけて全国でそろって下がりました。2010〜2015年度は、毎年8割を超える市区町村が前年度より比率を下げています。2018年度以降は、毎年4割を超える団体が前年度より比率を上げていて、全国の平均の前年度からの下げ幅は2017年度から年0.2ポイント未満に縮みました。

この記事では、1,741の市区町村について2008〜2021年度の実質公債費比率を並べ、平均の下げ幅がいつ縮み、どの団体で比率が上がっているのかを集計しました。

## 実質公債費比率は18%以上で地方債の発行に許可が要る

データは e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別の行政基盤テーブル（`d_municipal_administration`）から取っています。市区町村の財政について、次の指標が収録されています。

```sql
SELECT * FROM coverage
```

この記事では実質公債費比率（`D2211`）を中心に使います。[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/D)では、地方債の元利償還金とそれに準じる支出から交付税で手当てされる分などを除いた額が、標準財政規模に対してどれだけあるかを表す比率で、値は過去3か年の平均です。18%以上になると地方債の発行に許可が要り、25%が早期健全化基準、35%が財政再生基準です（[総務省の基準の説明](https://www.soumu.go.jp/iken/zaisei/kenzenka/index3.html)）。借金の残高にあたる将来負担比率（`D2212`）は最後の節で使います。

集計の単位は市町村と東京23区の1,741団体です。政令指定都市は市の値を使い、行政区の行は集計に含めていません。

## 全国の平均は2016年度までの8年度で6.51ポイント下がり、その後の5年度は0.50ポイント

市区町村の実質公債費比率を単純に平均すると、2008年度の14.06%から2016年度の7.55%まで、8年度で6.51ポイント下がりました。そのあと2021年度までの5年度で下がったのは0.50ポイントで、前年度からの下げ幅は毎年0.03〜0.17ポイントでした。2021年度は7.05%です。

```chart caption="市区町村の実質公債費比率の平均（2008〜2021年度）"
{
  "layer": [
    {
      "data": {"name": "debt_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"avg_ratio\"]) ? 0 : 1",
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
          {"field": "avg_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "avg_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "実質公債費比率の平均（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeWidth": 1, "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2016, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 2016, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "2016年度"}
      }
    }
  ]
}
```

実質公債費比率は過去3か年の平均なので、ある年度の返済の増減は、その年度を含む3年度の値に少しずつ表れます。

## 前年度より比率を上げた団体は、1割前後から4割超に増えた

各団体の比率を前年度と比較し、上げた団体と下げた団体を年度ごとに集計しました。

```chart caption="実質公債費比率を前年度より上げた市区町村と下げた市区町村の数"
{
  "layer": [
    {
      "data": {"name": "up_down"},
      "transform": [
        {"fold": ["down", "same", "up"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"down\": \"下げた\", \"same\": \"変わらない\", \"up\": \"上げた\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"down\",\"same\",\"up\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["下げた", "変わらない", "上げた"], "range": ["#93c5fd", "#cbd5e1", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "year", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

2010〜2015年度は、前年度より比率を下げた団体が毎年83.1〜88.6%、上げた団体が9.2〜12.6%でした。2016年度に22.1%、2017年度に38.5%と増え、2018〜2021年度は毎年40.7〜45.7%です。2019年度は上げた団体が795、下げた団体が819で、ほぼ同じ数でした。

```sql
SELECT year AS "年度", up AS "上げた", same AS "変わらない", down AS "下げた", up_share AS "上げた団体の割合(%)", down_share AS "下げた団体の割合(%)" FROM up_down
```

## 2014年度に比率が最も低かった組では、349団体のうち225団体が比率を上げた

2014年度の比率で市区町村を5つの組に分け、2016年度から2021年度までの5年度の変化を比較しました。比較する期間より前の2014年度で組を分けたのは、2016年度に偶然低く出た団体がその後上がるだけの動きが、組の差に混ざりにくくするためです。

```sql
SELECT * FROM quintile
```

2014年度に比率が最も低かった組では、349団体のうち225団体が2016年度から2021年度までに比率を上げ、平均は1.77%から2.59%になりました。最も高かった組で上げたのは348団体のうち59団体で、平均は13.06%から10.62%に下がっています。2017年度以降の全国の平均の下げ幅が小さいのは、比率の高い組の比率が下がり、低い組の多くの団体が比率を上げたためです。

比率が18%以上の団体は、2008年度の383団体から2016年度に12団体、2021年度に1団体まで減りました。2021年度の1団体は北海道夕張市で、比率は68.3%です。

```chart caption="実質公債費比率が18%以上の市区町村の数"
{
  "layer": [
    {
      "data": {"name": "debt_trend"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "n18", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "n18",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "18%以上の市区町村数", "grid": true}
        }
      }
    }
  ]
}
```

夕張市の比率は2008〜2021年度で2016年度の76.8%が最も高く、2021年度は68.3%です。

```sql
SELECT year AS "年度", ratio AS "夕張市の実質公債費比率(%)" FROM yubari
```

## 2021年度の都道府県ごとの平均は、島根県が11.32%で最も高く、東京都が0.45%で最も低い

2021年度の比率を、都道府県ごとにその中の市区町村の単純平均で地図にしました。人口の多い市も少ない村も1団体として扱っています。

```map
type: map
caption: "市区町村の実質公債費比率の都道府県別平均（2021年度）"
layers:
  - from: debt_map
    geojson: geojson
    color: value
    label: pref_name
    name: "実質公債費比率(%)"
lng: 137.5
lat: 38.2
zoom: 4.1
```

平均が最も高いのは島根県（11.32%）で、富山県（10.66%）、岩手県（10.45%）、新潟県（9.67%）、青森県（9.60%）が続きます。最も低いのは東京都（0.45%）で、愛知県（2.52%）、神奈川県（4.24%）、大阪府（4.72%）が続きます。

```sql
SELECT * FROM pref_rank WHERE "順位" <= 5 OR "順位" >= 43
```

市区町村ごとに見ると、財政力指数（`D2201`）が0.7以上の団体で、比率が低く出ています。財政力指数は、標準的な税収入などを標準的な行政に要る経費で割った値の過去3年度平均です。2021年度の財政力指数が0.7未満の団体は比率の平均が7.45〜8.49%で、0.7以上1.0未満は4.66%、1.0以上は3.06%でした。

```sql
SELECT * FROM fi_group
```

## 将来負担比率が算定されない団体は2011年度の406から816へ

借金の残高の重さを表す将来負担比率は、地方債の残高などの将来負担額から、基金や交付税で手当てされる見込みの額などの充当可能財源等を引いて計算します（[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/D)）。充当可能財源等のほうが大きい団体は比率が算定されません。このテーブルで将来負担比率に値が入っていない行は、同じ年度の実質公債費比率には値があり、0未満の値も1件もないので、算定されなかった団体として集計しました。2011〜2013年度には両方の値が無い団体が毎年1つあり、集計から除いています。

```chart caption="将来負担比率が算定されなかった市区町村の数"
{
  "layer": [
    {
      "data": {"name": "stock"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "no_burden", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "no_burden",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        }
      }
    }
  ]
}
```

将来負担比率が算定されなかった団体は、2011年度の406から2021年度の816へ増え、1,741団体の半数近くになりました。2016年度から2021年度にかけても672から816へ増えています。毎年の返済の重さの平均は2016年度から2021年度に0.50ポイントしか下がっていませんが、借金の残高を基金などで賄える団体はその後も増えています。

```sql
SELECT year AS "年度", no_burden AS "算定されなかった団体", with_burden AS "値がある団体", both_missing AS "両方の値が無い団体", negative AS "0未満の値", max_ratio AS "最も高い値(%)" FROM stock
```

## 自分の自治体の財政を比較するとき

- 財政担当の職員が議会や住民に自分の市町村の比率の上がり方を説明するときは、2014年度に同じ組にいた団体の2016→2021年度の平均の変化と比較できます。最も低い組の平均は0.82ポイント上がり、最も高い組の平均は2.44ポイント下がっています
- 比率が低い団体の比率が上がることは、借金の返済が財政を圧迫し始めたことを直ちには意味しません。2021年度に18%以上の団体は1団体だけです。財政力指数の同じ区分の平均と比較すると、財政力の近い団体の中で比率が高いか低いかを確認できます
- 実質公債費比率が上がっていても、将来負担比率が算定されていない団体は、借金の残高を基金などで賄える状態にあります。財政担当の職員は、毎年の返済の重さと借金の残高を分けて示すと、将来負担比率が算定されていない団体なら、比率が上がっても残高の面では余裕があることを議会や住民に説明できます

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別の行政基盤データを 2026-11-10 時点で集計しています。元データは総務省の地方財政状況調査で、数値はすべて年度の値です。2021年度に実質公債費比率が18%以上の市区町村が1団体であることは、[令和5年版 地方財政白書](https://www.soumu.go.jp/menu_seisaku/hakusyo/chihou/r05data/2023data/r05czb01-09.html)の記述と一致します。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[市区町村別の行政基盤テーブル](/datasets/queria/e_stat/ssds/d_municipal_administration)から、自分の市町村と財政力の近い団体の比率の推移を確認できます。

```sql id=coverage
-- 市区町村財政（D22xx）の指標と収録年度
SELECT cat01 AS "コード", regexp_replace(item_name, '^D[0-9]+_', '') AS "内容", min_year AS "最初の年度", max_year AS "最後の年度"
FROM e_stat.ssds.series_coverage
WHERE table_name = 'd_municipal_administration' AND cat01 LIKE 'D22%'
ORDER BY cat01
```

```sql id=debt_trend
-- 市区町村（政令市の行政区と特別区部の合計行を除く1,741団体）の実質公債費比率の平均・中央値と、18%以上・25%以上の団体数
WITH base AS (
  SELECT area, year, MAX(TRY_CAST(value AS DOUBLE)) AS v
  FROM e_stat.ssds.d_municipal_administration
  WHERE cat01 = 'D2211' AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'
  GROUP BY area, year
)
SELECT year, COUNT(v) AS n, ROUND(AVG(v), 2) AS avg_ratio, ROUND(AVG(v) - LAG(AVG(v)) OVER (ORDER BY year), 2) AS change_from_prev, MEDIAN(v) AS median_ratio,
  COUNT(*) FILTER (WHERE v >= 18) AS n18, COUNT(*) FILTER (WHERE v >= 25) AS n25
FROM base
WHERE v IS NOT NULL AND year BETWEEN 2008 AND 2021
GROUP BY year
ORDER BY year
```

```sql id=up_down
-- 前年度と比べて実質公債費比率を上げた・変わらない・下げた団体の数（両年度に値がある団体）
WITH base AS (
  SELECT area, year, MAX(TRY_CAST(value AS DOUBLE)) AS v
  FROM e_stat.ssds.d_municipal_administration
  WHERE cat01 = 'D2211' AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'
  GROUP BY area, year
), d AS (
  SELECT year, v - LAG(v) OVER (PARTITION BY area ORDER BY year) AS dv
  FROM base
  WHERE v IS NOT NULL
)
SELECT year,
  COUNT(*) FILTER (WHERE dv > 0) AS up,
  COUNT(*) FILTER (WHERE dv = 0) AS same,
  COUNT(*) FILTER (WHERE dv < 0) AS down,
  ROUND(100.0 * COUNT(*) FILTER (WHERE dv > 0) / COUNT(*), 1) AS up_share,
  ROUND(100.0 * COUNT(*) FILTER (WHERE dv < 0) / COUNT(*), 1) AS down_share
FROM d
WHERE dv IS NOT NULL AND year BETWEEN 2009 AND 2021
GROUP BY year
ORDER BY year
```

```sql id=quintile
-- 2014年度の比率で5組に分け、2016年度から2021年度の変化と、比率を上げた団体の数を比べる
WITH base AS (
  SELECT area, year, MAX(TRY_CAST(value AS DOUBLE)) AS v
  FROM e_stat.ssds.d_municipal_administration
  WHERE cat01 = 'D2211' AND year IN (2014, 2016, 2021) AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'
  GROUP BY area, year
), w AS (
  SELECT area, MAX(v) FILTER (WHERE year = 2014) AS v14, MAX(v) FILTER (WHERE year = 2016) AS v16, MAX(v) FILTER (WHERE year = 2021) AS v21
  FROM base
  GROUP BY area
), g AS (
  SELECT *, NTILE(5) OVER (ORDER BY v14, area) AS q
  FROM w
  WHERE v14 IS NOT NULL AND v16 IS NOT NULL AND v21 IS NOT NULL
)
SELECT q AS "2014年度の低いほうから", COUNT(*) AS "団体数", MIN(v14) || '〜' || MAX(v14) AS "2014年度の範囲(%)",
  ROUND(AVG(v16), 2) AS "2016年度の平均(%)", ROUND(AVG(v21), 2) AS "2021年度の平均(%)",
  ROUND(AVG(v21) - AVG(v16), 2) AS "変化(ポイント)",
  COUNT(*) FILTER (WHERE v21 > v16) AS "2016→2021年度に上げた団体"
FROM g
GROUP BY q
ORDER BY q
```

```sql id=yubari
SELECT year, MAX(TRY_CAST(value AS DOUBLE)) AS ratio
FROM e_stat.ssds.d_municipal_administration
WHERE cat01 = 'D2211' AND year BETWEEN 2008 AND 2021 AND area_name = '北海道 夕張市'
GROUP BY year
ORDER BY year
```

```sql id=pref_base
-- 都道府県ごとの市区町村の単純平均（2021年度）
WITH base AS (
  SELECT split_part(area_name, ' ', 1) AS pref, area, MAX(TRY_CAST(value AS DOUBLE)) AS v
  FROM e_stat.ssds.d_municipal_administration
  WHERE year = 2021 AND cat01 = 'D2211' AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'
  GROUP BY pref, area
)
SELECT pref, COUNT(v) AS n, ROUND(AVG(v), 2) AS v
FROM base
WHERE v IS NOT NULL
GROUP BY pref
ORDER BY pref
```

```sql id=pref_rank
SELECT RANK() OVER (ORDER BY v DESC) AS "順位", pref AS "都道府県", n AS "市区町村数", v AS "平均(%)"
FROM pref_base
ORDER BY v DESC, pref
```

```sql id=debt_map
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, a.v AS value
FROM nlftp.boundary.prefecture p
JOIN pref_base a ON p.prefecture_name = a.pref
```

```sql id=fi_group
-- 2021年度の財政力指数の区分ごとの実質公債費比率
WITH d AS (
  SELECT area, cat01, MAX(TRY_CAST(value AS DOUBLE)) AS v
  FROM e_stat.ssds.d_municipal_administration
  WHERE year = 2021 AND cat01 IN ('D2201', 'D2211') AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'
  GROUP BY area, cat01
), w AS (
  SELECT area, MAX(v) FILTER (WHERE cat01 = 'D2201') AS fi, MAX(v) FILTER (WHERE cat01 = 'D2211') AS r
  FROM d
  GROUP BY area
)
SELECT CASE WHEN fi < 0.3 THEN '0.3未満' WHEN fi < 0.5 THEN '0.3以上0.5未満' WHEN fi < 0.7 THEN '0.5以上0.7未満' WHEN fi < 1.0 THEN '0.7以上1.0未満' ELSE '1.0以上' END AS "財政力指数",
  COUNT(*) AS "団体数", ROUND(AVG(r), 2) AS "実質公債費比率の平均(%)", ROUND(MEDIAN(r), 2) AS "中央値(%)"
FROM w
WHERE fi IS NOT NULL AND r IS NOT NULL
GROUP BY 1
ORDER BY MIN(fi)
```

```sql id=stock
-- 将来負担比率（D2212）に値が無く、同じ年度の実質公債費比率（D2211）には値がある団体を「算定されなかった団体」として数える
WITH b AS (
  SELECT area, year, cat01, MAX(TRY_CAST(value AS DOUBLE)) AS v
  FROM e_stat.ssds.d_municipal_administration
  WHERE cat01 IN ('D2211', 'D2212') AND year BETWEEN 2011 AND 2021 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'
  GROUP BY area, year, cat01
), w AS (
  SELECT area, year, MAX(v) FILTER (WHERE cat01 = 'D2211') AS r, MAX(v) FILTER (WHERE cat01 = 'D2212') AS f
  FROM b
  GROUP BY area, year
)
SELECT year, COUNT(*) AS n,
  COUNT(*) FILTER (WHERE f IS NULL AND r IS NOT NULL) AS no_burden,
  COUNT(f) AS with_burden,
  COUNT(*) FILTER (WHERE f IS NULL AND r IS NULL) AS both_missing,
  COUNT(*) FILTER (WHERE f < 0) AS negative,
  MAX(f) AS max_ratio
FROM w
GROUP BY year
ORDER BY year
```
