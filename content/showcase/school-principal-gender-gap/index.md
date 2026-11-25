---
title: 小中学校の教諭の女性比率は都道府県で50〜64%なのに、校長は12〜49%と4倍開く
description: 学校基本調査の2025年の本務教員で、小中学校の教諭の女性比率は都道府県で49.6〜63.7%、校長は12.3〜49.2%でした。全国の校長の女性比率は4年で18.6%から24.4%に上がっています。
publishedAt: 2026-11-25
author:
  name: UD
  url: https://udus.dev
tags:
  - 学校
  - 教員
  - 男女共同参画
  - 人事
datasets:
  - queria/e_stat
sources:
  - title: 学校基本調査
    url: https://www.e-stat.go.jp/stat-search/files?toukei=00400001
    publisher: 文部科学省
agentHint: 自分の都道府県の市区町村について、小学校と中学校の校長の女性比率を2021年と2025年で出して、女性の校長が1人もいない市区町村を一覧にして
socialAnnounce: |-
  2025年の小中学校の教諭の女性比率は都道府県で50〜64%に収まりますが、校長は12〜49%と約4倍開いています。

  教育委員会の人事や男女共同参画の担当に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

小中学校の教諭に占める女性の比率は、2025年に全国で56.6%でした。校長では24.4%です。都道府県別に見ると、教諭の女性比率は49.6%から63.7%の間に収まり、47都道府県の差は14.1ポイントです。校長の女性比率は12.3%（島根県）から49.2%（石川県）まで開き、差は36.9ポイントあります。校長の女性比率は2021年の18.6%から4年で5.8ポイント上がりましたが、都道府県の順位は4年でほとんど入れ替わっていません。

都道府県や市町村の教育委員会で教職員の人事や男女共同参画を担当する人は、自県の校長の女性比率が全国のどこにあるかを知る必要があります。文部科学省の[学校基本調査](https://www.e-stat.go.jp/stat-search/files?toukei=00400001)は、小学校と中学校の本務教員の数を、職名と男女、市区町村ごとに毎年まとめています。この記事では2021年から2025年の5年分を使い、小学校と中学校を合計して集計しました。「教諭」は学級を担任する一般の教員、「校長」は学校の長です。

```sql id=nat
-- 全国の小学校と中学校の合計。本文の全国値の裏付け（プロットはしない）
SELECT year,
  CASE WHEN "position" = '校長' THEN '校長' WHEN "position" = '教諭' THEN '教諭' ELSE '教頭・副校長' END AS role,
  SUM(CASE WHEN sex = '女' THEN teachers END) AS women,
  SUM(CASE WHEN sex = '計' THEN teachers END) AS total,
  ROUND(100.0 * SUM(CASE WHEN sex = '女' THEN teachers END) / SUM(CASE WHEN sex = '計' THEN teachers END), 1) AS pct
FROM e_stat.school.municipality_teachers
WHERE area_level = 'prefecture' AND "position" IN ('校長', '教頭', '副校長', '教諭') AND year IN (2021, 2025)
GROUP BY year, CASE WHEN "position" = '校長' THEN '校長' WHEN "position" = '教諭' THEN '教諭' ELSE '教頭・副校長' END
ORDER BY role, year
```

## 教諭の女性比率はどの県も50〜64%なのに、校長は12〜49%に開く

使ったのは学校基本調査のテーブル（`e_stat.school.municipality_teachers`）です。1行が「年・学校種・地域・職名・性別」の本務教員数で、職名には校長、副校長、教頭、主幹教諭、指導教諭、教諭、助教諭、講師などがあります。都道府県の行（`area_level = 'prefecture'`）には、その県の国立・公立・私立の合計が入っています。

最初の図は、2025年の47都道府県を1点ずつ、横軸を教諭の女性比率、縦軸を校長の女性比率にして置いたものです。点は横には50〜64%の狭い範囲に並び、縦には12〜49%に散らばります。

```chart caption="2025年の小学校と中学校の合計。1点が1都道府県"
{
  "data": { "name": "gap" },
  "height": 360,
  "mark": { "type": "point", "filled": true, "size": 70, "color": "#2166ac", "opacity": 0.8 },
  "encoding": {
    "x": { "field": "teacher_pct", "type": "quantitative", "title": "教諭の女性比率（%）", "scale": { "domain": [0, 70] } },
    "y": { "field": "principal_pct", "type": "quantitative", "title": "校長の女性比率（%）", "scale": { "domain": [0, 55] } },
    "tooltip": [{ "field": "pref" }, { "field": "teacher_pct", "title": "教諭（%）", "format": ".1f" }, { "field": "principal_pct", "title": "校長（%）", "format": ".1f" }]
  }
}
```

次の図は、同じ値を都道府県ごとに、教諭の女性比率（灰色の点）と校長の女性比率（青の点）を結んだものです。校長の女性比率が高い県を上に並べています。灰色の点は右の狭い範囲に集まっています。青の点は石川県の49.2%から島根県の12.3%まで広がっています。教諭の女性比率が最も低い北海道（49.6%）の校長は13.2%、最も高い徳島県（63.7%）の校長は20.6%です。47都道府県で教諭と校長の女性比率の相関係数を取ると-0.04で、教諭の女性比率が高い県で校長の女性比率も高いという関係はありません。

```sql id=gap
SELECT area_name AS pref,
  ROUND(100.0 * SUM(CASE WHEN "position" = '校長' AND sex = '女' THEN teachers END) / SUM(CASE WHEN "position" = '校長' AND sex = '計' THEN teachers END), 1) AS principal_pct,
  ROUND(100.0 * SUM(CASE WHEN "position" = '教諭' AND sex = '女' THEN teachers END) / SUM(CASE WHEN "position" = '教諭' AND sex = '計' THEN teachers END), 1) AS teacher_pct,
  SUM(CASE WHEN "position" = '校長' AND sex = '計' THEN teachers END) AS principals
FROM e_stat.school.municipality_teachers
WHERE area_level = 'prefecture' AND year = 2025 AND "position" IN ('校長', '教諭')
GROUP BY area_name
ORDER BY principal_pct DESC, area_name
```

```sql id=gapstats
-- 本文の件数・範囲・相関の裏付け（プロットはしない）
SELECT COUNT(*) FILTER (WHERE principal_pct >= 30) AS over30, COUNT(*) FILTER (WHERE principal_pct < 20) AS under20,
  ROUND(MAX(teacher_pct) - MIN(teacher_pct), 1) AS teacher_range, ROUND(MAX(principal_pct) - MIN(principal_pct), 1) AS principal_range,
  ROUND(CORR(teacher_pct, principal_pct), 2) AS corr
FROM gap
```

```chart caption="2025年の小学校と中学校の合計。灰色が教諭、青が校長の女性比率"
{
  "data": { "name": "gap" },
  "height": 1100,
  "encoding": {
    "y": { "field": "pref", "type": "nominal", "sort": { "field": "principal_pct", "order": "descending" }, "title": null }
  },
  "layer": [
    {
      "mark": { "type": "rule", "color": "#cbd5e1", "strokeWidth": 3 },
      "encoding": {
        "x": { "field": "teacher_pct", "type": "quantitative", "title": "女性の比率（%）", "scale": { "domain": [0, 70] } },
        "x2": { "field": "principal_pct" }
      }
    },
    {
      "mark": { "type": "point", "filled": true, "size": 80 },
      "encoding": {
        "x": { "field": "teacher_pct", "type": "quantitative" },
        "color": { "datum": "教諭", "type": "nominal", "title": null, "scale": { "domain": ["教諭", "校長"], "range": ["#94a3b8", "#2166ac"] } },
        "tooltip": [{ "field": "pref" }, { "field": "teacher_pct", "title": "教諭の女性比率（%）", "format": ".1f" }]
      }
    },
    {
      "mark": { "type": "point", "filled": true, "size": 80 },
      "encoding": {
        "x": { "field": "principal_pct", "type": "quantitative" },
        "color": { "datum": "校長", "type": "nominal" },
        "tooltip": [{ "field": "pref" }, { "field": "principal_pct", "title": "校長の女性比率（%）", "format": ".1f" }, { "field": "principals", "title": "校長の人数", "format": "," }]
      }
    }
  ]
}
```

校長の女性比率が30%以上の県は2025年に10県、20%を下回る県は12県あります。教諭の女性比率は県ごとの差が14.1ポイントなのに、校長の女性比率は36.9ポイント開くので、県の差は教員全体の男女構成だけでは説明できません。

図の数値は国立・公立・私立の合計で、小学校と中学校を合わせた値です。教諭の女性比率は小学校で63.7%、中学校で44.7%と違うので、県ごとの小学校と中学校の構成比も値に影響します。公立学校の校長の任用は教育委員会が行うため、私立の校長を含むこの数値は、公立の人事の水準を示す目安として読んでください。

## 校長の女性比率は4年で上がり、中学校は8.7%から13.9%になった

次の図は、全国の小学校と中学校で、教諭、教頭・副校長、校長の女性比率が2021年から2025年にどう動いたかを示します。教頭と副校長は、校長を補佐する職名です。2つの職名があるので、まとめて集計しています。

```sql id=trend
SELECT year, school_type_name AS school,
  CASE WHEN "position" = '校長' THEN '校長' WHEN "position" = '教諭' THEN '教諭' ELSE '教頭・副校長' END AS role,
  ROUND(100.0 * SUM(CASE WHEN sex = '女' THEN teachers END) / SUM(CASE WHEN sex = '計' THEN teachers END), 1) AS pct,
  SUM(CASE WHEN sex = '女' THEN teachers END) AS women,
  SUM(CASE WHEN sex = '計' THEN teachers END) AS total
FROM e_stat.school.municipality_teachers
WHERE area_level = 'prefecture' AND "position" IN ('校長', '教頭', '副校長', '教諭')
GROUP BY year, school_type_name, CASE WHEN "position" = '校長' THEN '校長' WHEN "position" = '教諭' THEN '教諭' ELSE '教頭・副校長' END
ORDER BY school, role, year
```

```chart caption="全国の女性比率。教諭はほぼ動かず、校長と教頭・副校長が上がっている"
{
  "data": { "name": "trend" },
  "facet": { "field": "school", "type": "nominal", "title": null },
  "columns": 2,
  "spec": {
    "height": 240,
    "mark": { "type": "line", "point": true },
    "encoding": {
      "x": { "field": "year", "type": "ordinal", "title": null },
      "y": { "field": "pct", "type": "quantitative", "title": "女性の比率（%）", "scale": { "domain": [0, 70] } },
      "color": { "field": "role", "type": "nominal", "title": null, "scale": { "domain": ["教諭", "教頭・副校長", "校長"], "range": ["#94a3b8", "#64748b", "#2166ac"] } },
      "tooltip": [{ "field": "school" }, { "field": "role" }, { "field": "year" }, { "field": "pct", "title": "女性比率（%）", "format": ".1f" }, { "field": "women", "title": "女性の人数", "format": "," }]
    }
  }
}
```

小学校の校長の女性比率は23.4%（4,376人）から29.5%（5,318人）に、中学校では8.7%（777人）から13.9%（1,221人）に上がりました。中学校の女性校長は4年で1.6倍です。同じ期間に校長の総数は、小学校で18,733人から18,030人、中学校で8,977人から8,769人に減っています。教諭の女性比率は小学校で63.9%から63.7%、中学校で44.0%から44.7%で、ほぼ動いていません。

## 校長の女性比率が高い県は、4年前から教頭・副校長の女性比率も高い

2021年の教頭・副校長の女性比率を横軸に、2025年の校長の女性比率を縦軸に、47都道府県を1点ずつ置きました。

```sql id=pipe
WITH t AS (
  SELECT area_name AS pref, year,
    100.0 * SUM(CASE WHEN "position" IN ('教頭', '副校長') AND sex = '女' THEN teachers END) / SUM(CASE WHEN "position" IN ('教頭', '副校長') AND sex = '計' THEN teachers END) AS vp_pct,
    100.0 * SUM(CASE WHEN "position" = '校長' AND sex = '女' THEN teachers END) / SUM(CASE WHEN "position" = '校長' AND sex = '計' THEN teachers END) AS pr_pct
  FROM e_stat.school.municipality_teachers
  WHERE area_level = 'prefecture' AND year IN (2021, 2025) AND "position" IN ('校長', '教頭', '副校長')
  GROUP BY area_name, year)
SELECT a.pref, ROUND(a.vp_pct, 1) AS vp_2021, ROUND(a.pr_pct, 1) AS principal_2021, ROUND(b.pr_pct, 1) AS principal_2025
FROM t a JOIN t b ON a.pref = b.pref AND a.year = 2021 AND b.year = 2025
ORDER BY a.pref
```

```sql id=spread
-- 本文の相関係数と、校長の女性比率の最高と最低の差（プロットはしない）
SELECT ROUND(CORR(vp_2021, principal_2025), 2) AS corr_vp_to_principal,
  ROUND(CORR(principal_2021, principal_2025), 2) AS corr_principal_to_principal,
  ROUND(MAX(principal_2021) - MIN(principal_2021), 1) AS range_2021,
  ROUND(MAX(principal_2025) - MIN(principal_2025), 1) AS range_2025,
  COUNT(*) AS prefs
FROM pipe
```

```chart caption="2021年の教頭・副校長の女性比率（横）と2025年の校長の女性比率（縦）。1点が1都道府県"
{
  "data": { "name": "pipe" },
  "height": 380,
  "mark": { "type": "point", "filled": true, "size": 70, "color": "#2166ac", "opacity": 0.8 },
  "encoding": {
    "x": { "field": "vp_2021", "type": "quantitative", "title": "2021年の教頭・副校長の女性比率（%）", "scale": { "domain": [0, 50] } },
    "y": { "field": "principal_2025", "type": "quantitative", "title": "2025年の校長の女性比率（%）", "scale": { "domain": [0, 55] } },
    "tooltip": [{ "field": "pref" }, { "field": "vp_2021", "title": "2021年 教頭・副校長（%）", "format": ".1f" }, { "field": "principal_2025", "title": "2025年 校長（%）", "format": ".1f" }]
  }
}
```

2021年の教頭・副校長の女性比率が最も高い石川県（46.5%）は、2025年の校長の女性比率も最高の49.2%です。最も低い長崎県（10.5%）と福島県（10.7%）は、2025年の校長が12.6%と12.5%でした。47都道府県での相関係数は0.93です。2021年の校長の女性比率と2025年の校長の女性比率の相関係数も0.90で、2021年の教頭・副校長の層の水準と、校長自身の2021年の水準は、2025年の校長の女性比率を同じ程度に言い当てています。県の順位は4年でほとんど入れ替わっていません。

## 校長が1〜2人の自治体の女性比率は14.8%、21人以上は25.3%

市区町村別に見ます。自治体ごとに、小学校と中学校の校長の合計人数（東京23区は区ごと、政令指定都市は区を合算した市ごと）で5区分に分け、女性の校長が1人もいない自治体の数と、校長に占める女性の比率を集計しました。数値は国立・公立・私立の合計です。区分は各年の校長の人数で決めているので、2021年と2025年で同じ区分の自治体の顔ぶれは同じではありません。校長が1〜2人の自治体では、1人の人事異動で女性校長がいるかどうかが変わり、女性の比率が同じでも、人数が少ないほど女性が1人もいない自治体は多くなります。

```sql id=band
WITH m AS (
  SELECT year, COALESCE(city_code, area) AS city,
    SUM(CASE WHEN sex = '女' THEN teachers END) AS f,
    SUM(CASE WHEN sex = '計' THEN teachers END) AS t
  FROM e_stat.school.municipality_teachers
  WHERE area_level IN ('municipality', 'ward') AND "position" = '校長' AND year IN (2021, 2025)
  GROUP BY year, COALESCE(city_code, area)
  HAVING SUM(CASE WHEN sex = '計' THEN teachers END) > 0),
b AS (
  SELECT *, CASE WHEN t <= 2 THEN '1〜2人' WHEN t <= 5 THEN '3〜5人' WHEN t <= 10 THEN '6〜10人' WHEN t <= 20 THEN '11〜20人' ELSE '21人以上' END AS band,
    CASE WHEN t <= 2 THEN 1 WHEN t <= 5 THEN 2 WHEN t <= 10 THEN 3 WHEN t <= 20 THEN 4 ELSE 5 END AS ord
  FROM m)
SELECT year, band, ord, COUNT(*) AS cities, SUM(CASE WHEN f = 0 THEN 1 ELSE 0 END) AS no_women,
  ROUND(100.0 * SUM(CASE WHEN f = 0 THEN 1 ELSE 0 END) / COUNT(*), 1) AS no_women_pct,
  SUM(f) AS women, SUM(t) AS principals, ROUND(100.0 * SUM(f) / SUM(t), 1) AS women_pct
FROM b GROUP BY year, band, ord ORDER BY year, ord
```

```chart caption="校長の人数の区分別の、校長に占める女性の比率"
{
  "data": { "name": "band" },
  "height": 300,
  "mark": "bar",
  "encoding": {
    "x": { "field": "band", "type": "ordinal", "sort": { "field": "ord" }, "title": "市区町村の校長の人数（小学校と中学校の合計）" },
    "xOffset": { "field": "year", "type": "nominal" },
    "y": { "field": "women_pct", "type": "quantitative", "title": "女性の比率（%）" },
    "color": { "field": "year", "type": "nominal", "title": "年" },
    "tooltip": [{ "field": "band" }, { "field": "year" }, { "field": "cities", "title": "自治体数", "format": "," }, { "field": "no_women", "title": "女性校長がいない自治体", "format": "," }, { "field": "women_pct", "title": "女性比率（%）", "format": ".1f" }]
  }
}
```

```sql
SELECT year AS 年, band AS 校長の人数, cities AS 自治体数, no_women AS 女性校長がいない自治体, no_women_pct AS 割合_pct, women_pct AS 校長の女性比率_pct FROM band ORDER BY year DESC, ord
```

2025年に校長が1〜2人の266自治体では、199自治体（74.8%）に女性の校長がいません。校長に占める女性の比率は14.8%です。校長が21人以上の341自治体で女性校長がいないのは1自治体だけで、女性の比率は25.3%です。校長が1〜2人の自治体の女性比率は2021年の10.9%から14.8%に上がりましたが、21人以上の自治体との差は10ポイント以上あります。

## 業務での活用

- 都道府県の教育委員会で人事を担当する人は、自県の校長の女性比率と、教頭・副校長の女性比率を、都道府県別の図で全国と比較できます。教頭・副校長の女性比率が低い県は、4年後の校長の女性比率も低い傾向があります
- 市町村の教育委員会や男女共同参画の担当者は、自分の市区町村の校長の女性比率を、校長の人数が近い自治体の水準と比較できます。人数の区分ごとの女性比率は、最後の図と表にあります
- 都道府県の担当者は、管内で女性の校長が1人もいない市区町村を、校長の人数の区分ごとに分けて一覧にし、女性の管理職を増やす施策の対象となる地域を決められます。校長が少ない自治体は、女性の比率が同じでも0人になりやすいため、区分を分けて見ます

## データの出典

本記事は文部科学省の[学校基本調査](https://www.e-stat.go.jp/stat-search/files?toukei=00400001)の小学校と中学校の本務教員数（国立・公立・私立の計）を、2026-11-25 時点で集計しています。収録は2021年から2025年です。

Queriaは、学校基本調査の職名・男女別の教員数を、列名・単位・文字コードを揃え、テーブルと列の意味を添えて公開しています。本記事で使った[市区町村別の教員数テーブル](/datasets/queria/e_stat/school/municipality_teachers)から、自県と自分の市区町村の校長の女性比率を確かめたり、女性校長のいない自治体を探したりできます。
