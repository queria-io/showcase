---
title: ごみのリサイクル率を下げたのは住民団体の集団回収の減少で、その割合は46都道府県で減った
description: 全国のごみのリサイクル率は2010年度の20.8%から2023年度の19.5%へ下がりました。押し下げたのは住民団体による資源の集団回収の減少で、リサイクル率に占めるその割合は2010年度から46都道府県で減りました。
publishedAt: 2026-06-21
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 環境
  - 廃棄物
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/1.html
    publisher: 総務省統計局
  - title: 一般廃棄物処理実態調査結果
    url: https://www.env.go.jp/recycle/waste_tech/ippan/index.html
    publisher: 環境省
  - title: 一般廃棄物処理実態調査 調査の概要
    url: https://www.env.go.jp/recycle/waste_tech/ippan/about.pdf
    publisher: 環境省
  - title: 一般廃棄物処理実態調査 用語の解説
    url: https://www.env.go.jp/recycle/waste_tech/ippan/glossary.pdf
    publisher: 環境省
agentHint: リサイクル率を集団回収の分と市町村の分に分けて、都道府県別に2015年度と2023年度で比べて。集団回収量（H560904）が2019年度から2020年度に大きく減った県も出して
socialAnnounce: |-
  ごみのリサイクル率は2010年度の20.8%から2023年度は19.5%へ。押し下げたのは住民団体の集団回収の減少で、回収量はほぼ半分になりました。

  ごみ処理計画のリサイクル率目標の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
relatedDatasets: false
---

全国のごみのリサイクル率は、データのある1999年度以降では2010年度の20.8%が最も高く、2023年度は19.5%に下がりました。リサイクル率を中身ごとに分けると、率を下げたのは、市町村に登録した住民団体が自分たちで資源を集める「集団回収」の減少です。集団回収量は2010年度の272.9万tから2023年度の140.0万tへほぼ半分になり、リサイクル率に占める集団回収の分は、奈良県を除く46都道府県で減りました。市町村が資源にした分は、率に占める割合では上がっています。

## 全国では、集団回収の分が2.4ポイント減り、市町村の分は1.1ポイント増えた

データは e-Stat の「[社会・人口統計体系](https://www.stat.go.jp/data/ssds/1.html)」の都道府県別の居住データ（`h_pref_housing`）です。元は環境省の[一般廃棄物処理実態調査](https://www.env.go.jp/recycle/waste_tech/ippan/index.html)で、ごみの処理に関する次の項目が都道府県ごと・年度ごとに入っています。

| コード  | 内容                       | 単位 |
| ------- | -------------------------- | ---- |
| H5612   | ごみ処理量（総量）         | t    |
| H561201 | ごみ処理量（直接資源化）   | t    |
| H5613   | 中間処理後再生利用量       | t    |
| H560904 | ごみ総排出量（集団回収量） | t    |
| H5614   | ごみのリサイクル率         | %    |

環境省の[用語の解説](https://www.env.go.jp/recycle/waste_tech/ippan/glossary.pdf)では、リサイクル率を「（直接資源化量＋中間処理後再生利用量＋集団回収量）÷（ごみ処理量＋集団回収量）×100」と定めています。直接資源化量は市町村が集めた資源を処理施設を通さずに再生業者へ渡した量、中間処理後再生利用量は処理施設で選別・処理したあとに資源にした量です。この2つを「市町村の分」、集団回収量を「集団回収の分」として同じ分母で割ると、リサイクル率は2つの値の合計になります。

この式で計算した値は、2005〜2023年度の全国と47都道府県の912行すべてで、公表されたリサイクル率（`H5614`）と一致します。以下では、集団回収の分を計算し、リサイクル率から引いた残りを市町村の分としています。

```chart
{
  "layer": [
    {
      "data": {"name": "nation_trend"},
      "transform": [
        {"fold": ["muni_pt", "shudan_pt"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"muni_pt\": \"市町村の分\", \"shudan_pt\": \"集団回収の分\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"muni_pt\",\"shudan_pt\"], datum.__series)", "as": "__order"}
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
          "axis": {"title": "全国のリサイクル率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["市町村の分", "集団回収の分"], "range": ["#3b82f6", "#f97316"]},
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

全国では、集団回収の分が2010年度の6.0%から2023年度の3.6%へ2.4ポイント減り、市町村の分は14.8%から15.9%へ1.1ポイント増えました。集団回収の減り方が市町村の伸びを上回ったため、合計のリサイクル率が下がっています。市町村の分が上がったのは、分母のごみ処理量と集団回収量の合計が4,552.0万tから3,907.5万tへ14%減り、市町村が資源にした量の減少は7%だったためです。市町村が資源にした量そのものは減っています。集団回収量は2019年度の192.0万tから2020年度の164.3万tへ1年で14%減り、2023年度まで戻っていません。

集団回収として数えるのは、市町村による用具の貸し出しや補助金の交付を受けて市町村に登録された住民団体が回収した量だけです（[調査の概要](https://www.env.go.jp/recycle/waste_tech/ippan/about.pdf)）。リサイクル率の分母も、市町村が処理したごみと集団回収量の合計なので、登録された住民団体以外の回収に出された資源は、分子にも分母にも入りません。そのため、集団回収の分が減ったことは、住民が資源を出さなくなったことを表すとは限りません。

## 集団回収の分は、奈良県を除く46都道府県で減った

同じ分け方で、都道府県ごとに2010年度から2023年度までの増減を計算しました。オレンジが集団回収の分、青が市町村の分の増減で、2つを足すと黒い点（リサイクル率の増減）になります。上から、リサイクル率が大きく下がった順に並べています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_change"},
      "transform": [
        {"fold": ["shudan_change", "muni_change"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"shudan_change\": \"集団回収の分の増減\", \"muni_change\": \"市町村の分の増減\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"shudan_change\",\"muni_change\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2010年度から2023年度の増減（ポイント）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["集団回収の分の増減", "市町村の分の増減", "リサイクル率の増減"],
            "range": ["#f97316", "#3b82f6", "#0f172a"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    },
    {
      "data": {"name": "pref_change"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "total_change", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "total_change",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2010年度から2023年度の増減（ポイント）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "リサイクル率の増減",
          "type": "nominal",
          "scale": {
            "domain": ["集団回収の分の増減", "市町村の分の増減", "リサイクル率の増減"],
            "range": ["#f97316", "#3b82f6", "#0f172a"]
          },
          "title": null
        }
      }
    }
  ]
}
```

集団回収の分が減ったのは、奈良県（5.4%→6.6%）を除く46都道府県です。リサイクル率が下がったのは34県で、このうち13県は市町村の分が上がっていました。岐阜県は市町村の分が12.3%から14.3%へ上がりましたが、集団回収の分が10.1%から2.8%へ7.3ポイント減り、リサイクル率は22.4%から17.1%へ下がっています。13県のうち10県では、市町村が資源にした量そのものは減っていて、ごみ全体がそれより大きく減ったので、市町村の分が上がっています。量でも増えたのは、愛知県（3.4%増）、兵庫県（6.6%増）、群馬県（0.4%増）の3県です。

北海道は2010年度・2023年度とも22.8%で変わりません。リサイクル率が上がった12都府県でも、奈良県を除く11都府県では集団回収の分が減っています。このうち岡山県は市町村が資源にした量が31.0%、富山県は42.9%増え、市町村の分がそれぞれ7.5ポイント、5.5ポイント伸びました。

起点を2005・2010・2015年度にすると、2023年度までに集団回収の分が減った都道府県は43・46・47です。2020年度を起点にした3年間でも38あります。

```sql
SELECT base_year AS 起点の年度, prefectures AS 都道府県数, shudan_down AS 集団回収の分が減った, total_down AS リサイクル率が下がった, muni_up AS 市町村の分が上がった FROM base_years
```

## リサイクル率が下がった34県のうち21県では、市町村の分も下がった

リサイクル率が下がった34県のうち21県では、市町村の分も下がっていました。市町村の分の下げ幅が大きいのは山口県（34.6%→20.2%）と三重県（26.7%→18.0%）で、どちらもリサイクル率の下げ幅の大半を市町村の分が占めています。21県のうち11県では、市町村の分の下げ幅が集団回収の分の下げ幅を上回りました。これらの県では、リサイクル率の低下の主な原因は市町村の分の低下です。

市町村の分の中身の中間処理後再生利用量には、焼却灰・飛灰のセメント原料化や、ごみから作る固形燃料（RDF・RPF）も含まれます（[用語の解説](https://www.env.go.jp/recycle/waste_tech/ippan/glossary.pdf)）。環境省はこれらを除いたリサイクル率 R' も別に定めていますが、社会・人口統計体系に入っているのは除く前のリサイクル率だけです。そのため、市町村の分は、分別の状況が同じでも、焼却施設の処理方法が変わると変化することがあります。

47都道府県の値は次の表のとおりです。

```sql
SELECT area_name AS 都道府県, total_2010 AS リサイクル率_2010年度, total_2023 AS リサイクル率_2023年度, shudan_2010 AS 集団回収の分_2010年度, shudan_2023 AS 集団回収の分_2023年度, muni_2010 AS 市町村の分_2010年度, muni_2023 AS 市町村の分_2023年度, muni_amount_change_pct AS 市町村が資源にした量の増減率, pattern AS 型 FROM pref_change
```

## 業務での使い方

- リサイクル率が目標を下回ったときは、まず集団回収の分と市町村の分に分けます。集団回収の分が大きく減り、市町村の分が横ばいなら、分別の呼びかけより先に、集団回収の補助を受けている登録団体の数と回収量の推移を確認します。市町村の分も下がっているなら、市町村が資源にした量の推移から見ます
- 集団回収の分が減っている場合は、集団回収量（`H560904`）と直接資源化量（`H561201`）の推移を並べます。直接資源化量が増えていれば、住民団体が集めていた資源の一部が市町村の収集に移った可能性があります。どちらも減っていれば、資源は率の分子にも分母にも入らない回収に移ったか、排出される量そのものが減ったと考えられます。全国では、集団回収量とともに直接資源化量も2010年度の217.0万tから2023年度の181.9万tへ減っていて、どちらも減っている場合にあたります
- 市町村の分が1年で数ポイント動いた年度は、その年に焼却施設や資源化施設の処理方法が変わっていないかを確認します

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/1.html) の都道府県別データを2026年10月30日時点で集計しています。元データは環境省の[一般廃棄物処理実態調査](https://www.env.go.jp/recycle/waste_tech/ippan/index.html)で、社会・人口統計体系に入っているのは2023年度の調査結果までです。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の居住・生活環境データ](/datasets/queria/e_stat/ssds/h_pref_housing)から、担当する県の集団回収量や資源化量の推移を取り出し、リサイクル率を集団回収の分と市町村の分に分けて計算できます。

```sql id=nation_trend
-- 全国のリサイクル率と、その内訳。市町村の分はリサイクル率から集団回収の分を引いた値
WITH b AS ( SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H560904') AS shudan, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H561201') AS direct, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5613') AS after_proc, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5612') AS processed, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5614') AS published FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H560904', 'H561201', 'H5613', 'H5612', 'H5614') AND year BETWEEN 2005 AND 2023 GROUP BY area_name, year ), c AS ( SELECT area_name, year, shudan, direct, published, direct + after_proc AS muni_t, processed + shudan AS denom_t, ROUND(100 * (shudan + direct + after_proc) / (processed + shudan), 1) AS total_pt, ROUND(100 * shudan / (processed + shudan), 1) AS shudan_pt FROM b ), d AS ( SELECT *, ROUND(total_pt - shudan_pt, 1) AS muni_pt FROM c ) SELECT year, total_pt, shudan_pt, muni_pt, ROUND(shudan / 10000, 1) AS shudan_10kt, ROUND(muni_t / 10000, 1) AS muni_10kt, ROUND(direct / 10000, 1) AS direct_10kt, ROUND(denom_t / 10000, 1) AS denom_10kt FROM d WHERE area_name = '全国' ORDER BY year
```

```sql id=formula_check
-- 計算したリサイクル率と、公表されたリサイクル率（H5614）が一致する行数（プロットはしない）
WITH b AS ( SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H560904') AS shudan, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H561201') AS direct, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5613') AS after_proc, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5612') AS processed, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5614') AS published FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H560904', 'H561201', 'H5613', 'H5612', 'H5614') AND year BETWEEN 2005 AND 2023 GROUP BY area_name, year ), c AS ( SELECT area_name, year, shudan, direct, published, direct + after_proc AS muni_t, processed + shudan AS denom_t, ROUND(100 * (shudan + direct + after_proc) / (processed + shudan), 1) AS total_pt, ROUND(100 * shudan / (processed + shudan), 1) AS shudan_pt FROM b ), d AS ( SELECT *, ROUND(total_pt - shudan_pt, 1) AS muni_pt FROM c ) SELECT COUNT(*) AS rows_compared, COUNT(*) FILTER (WHERE total_pt = published) AS rows_matched, MIN(year) AS first_year, MAX(year) AS last_year FROM d
```

```sql id=nation_peak
-- 全国のリサイクル率（H5614）の収録期間と最高値（プロットはしない）
SELECT MIN(year) AS first_year, MAX(year) AS last_year, MAX(TRY_CAST(value AS DOUBLE)) AS peak_rate, ARG_MAX(year, TRY_CAST(value AS DOUBLE)) AS peak_year FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H5614' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023
```

```sql id=pref_change
-- 都道府県別の2010年度と2023年度。リサイクル率の増減の小さい順（下がった順）
WITH b AS ( SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H560904') AS shudan, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H561201') AS direct, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5613') AS after_proc, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5612') AS processed, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5614') AS published FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H560904', 'H561201', 'H5613', 'H5612', 'H5614') AND year BETWEEN 2005 AND 2023 GROUP BY area_name, year ), c AS ( SELECT area_name, year, shudan, direct, published, direct + after_proc AS muni_t, processed + shudan AS denom_t, ROUND(100 * (shudan + direct + after_proc) / (processed + shudan), 1) AS total_pt, ROUND(100 * shudan / (processed + shudan), 1) AS shudan_pt FROM b ), d AS ( SELECT *, ROUND(total_pt - shudan_pt, 1) AS muni_pt FROM c ) , r AS ( SELECT a.area_name, a.total_pt AS total_2010, z.total_pt AS total_2023, a.shudan_pt AS shudan_2010, z.shudan_pt AS shudan_2023, a.muni_pt AS muni_2010, z.muni_pt AS muni_2023, a.muni_t AS muni_t_2010, z.muni_t AS muni_t_2023 FROM d a JOIN d z ON a.area_name = z.area_name AND a.year = 2010 AND z.year = 2023 WHERE a.area_name <> '全国' ) SELECT area_name, total_2010, total_2023, ROUND(total_2023 - total_2010, 1) AS total_change, shudan_2010, shudan_2023, ROUND(shudan_2023 - shudan_2010, 1) AS shudan_change, muni_2010, muni_2023, ROUND(muni_2023 - muni_2010, 1) AS muni_change, ROUND(100 * (muni_t_2023 / muni_t_2010 - 1), 1) AS muni_amount_change_pct, CASE WHEN total_2023 < total_2010 AND muni_2023 > muni_2010 THEN '下がった（市町村の分は上がった）' WHEN total_2023 < total_2010 THEN '下がった（市町村の分も下がった）' WHEN total_2023 = total_2010 THEN '変わらない' ELSE '上がった' END AS pattern FROM r ORDER BY total_change, area_name
```

```sql id=pattern_counts
-- リサイクル率の増減の型ごとの都道府県数と、そのうち集団回収の分が減った数（プロットはしない）
WITH b AS ( SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H560904') AS shudan, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H561201') AS direct, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5613') AS after_proc, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5612') AS processed, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5614') AS published FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H560904', 'H561201', 'H5613', 'H5612', 'H5614') AND year BETWEEN 2005 AND 2023 GROUP BY area_name, year ), c AS ( SELECT area_name, year, shudan, direct, published, direct + after_proc AS muni_t, processed + shudan AS denom_t, ROUND(100 * (shudan + direct + after_proc) / (processed + shudan), 1) AS total_pt, ROUND(100 * shudan / (processed + shudan), 1) AS shudan_pt FROM b ), d AS ( SELECT *, ROUND(total_pt - shudan_pt, 1) AS muni_pt FROM c ) , r AS ( SELECT a.area_name, a.total_pt AS total_2010, z.total_pt AS total_2023, a.shudan_pt AS shudan_2010, z.shudan_pt AS shudan_2023, a.muni_pt AS muni_2010, z.muni_pt AS muni_2023, a.muni_t AS muni_t_2010, z.muni_t AS muni_t_2023 FROM d a JOIN d z ON a.area_name = z.area_name AND a.year = 2010 AND z.year = 2023 WHERE a.area_name <> '全国' ), p AS ( SELECT *, CASE WHEN total_2023 < total_2010 AND muni_2023 > muni_2010 THEN '下がった（市町村の分は上がった）' WHEN total_2023 < total_2010 THEN '下がった（市町村の分も下がった）' WHEN total_2023 = total_2010 THEN '変わらない' ELSE '上がった' END AS pattern FROM r ) SELECT pattern, COUNT(*) AS prefectures, COUNT(*) FILTER (WHERE shudan_2023 < shudan_2010) AS shudan_down, COUNT(*) FILTER (WHERE muni_2023 > muni_2010) AS muni_up, COUNT(*) FILTER (WHERE muni_t_2023 < muni_t_2010) AS muni_amount_down, COUNT(*) FILTER (WHERE ROUND(muni_2023 - muni_2010, 1) < ROUND(shudan_2023 - shudan_2010, 1)) AS muni_drop_larger, STRING_AGG(area_name, '、' ORDER BY total_2023 - total_2010, area_name) AS members FROM p GROUP BY pattern ORDER BY pattern
```

```sql id=base_years
-- 起点の年度を変えたときに、2023年度までに集団回収の分が減った都道府県の数（プロットはしない）
WITH b AS ( SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H560904') AS shudan, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H561201') AS direct, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5613') AS after_proc, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5612') AS processed, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H5614') AS published FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H560904', 'H561201', 'H5613', 'H5612', 'H5614') AND year BETWEEN 2005 AND 2023 GROUP BY area_name, year ), c AS ( SELECT area_name, year, shudan, direct, published, direct + after_proc AS muni_t, processed + shudan AS denom_t, ROUND(100 * (shudan + direct + after_proc) / (processed + shudan), 1) AS total_pt, ROUND(100 * shudan / (processed + shudan), 1) AS shudan_pt FROM b ), d AS ( SELECT *, ROUND(total_pt - shudan_pt, 1) AS muni_pt FROM c ) SELECT a.year AS base_year, COUNT(*) AS prefectures, COUNT(*) FILTER (WHERE z.shudan_pt < a.shudan_pt) AS shudan_down, COUNT(*) FILTER (WHERE z.total_pt < a.total_pt) AS total_down, COUNT(*) FILTER (WHERE z.muni_pt > a.muni_pt) AS muni_up FROM d a JOIN d z ON a.area_name = z.area_name AND z.year = 2023 WHERE a.area_name <> '全国' AND a.year IN (2005, 2010, 2015, 2020) GROUP BY a.year ORDER BY a.year
```
