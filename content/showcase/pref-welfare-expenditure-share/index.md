---
title: 都道府県が福祉に使うお金の住民1人あたりの差は、1975年度の4.71倍から2022年度の1.80倍に縮んだ
description: 都道府県の民生費を住民1人あたりで比べると、最も多い県と最も少ない県の差は1975年度の4.71倍から2022年度の1.80倍に縮みました。同じ期間に、民生費に占める老人福祉費の割合は19.6%から41.5%に上がっています。
publishedAt: 2026-06-19
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 地方財政
  - 民生費
  - 社会保障
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（D 行政基盤）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/D
    publisher: 総務省統計局
  - title: 令和6年版 地方財政白書 地方経費の内容
    url: https://www.soumu.go.jp/menu_seisaku/hakusyo/chihou/r06data/2024data/r06czb01-04.html
    publisher: 総務省
agentHint: 2022年度の老人福祉費を65歳以上人口1人あたりで都道府県別に出して、住民1人あたりの民生費の順位と並べて比べて。
socialAnnounce: |-
  都道府県が福祉に使う民生費は、住民1人あたりで最も多い県と最も少ない県の差が1975年度の4.71倍から2022年度の1.80倍に縮みました。

  自県の福祉の支出を他県と比べる調査に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

47都道府県の民生費を住民1人あたりで並べると、最も多い県と最も少ない県の差は、1975年度の4.71倍から2022年度の1.80倍に縮みました。同じ期間に、民生費に占める高齢者向けの経費（老人福祉費）の割合は19.6%から41.5%に上がっています。差が縮んだ後も1人あたりの額が少ないのは千葉県・神奈川県・埼玉県・愛知県・静岡県で、千葉県と神奈川県は48年度すべてで47都道府県の44〜47位でした。

都道府県が福祉に使うお金は、地方財政では「民生費」と呼ばれます。総務省の[令和6年版 地方財政白書](https://www.soumu.go.jp/menu_seisaku/hakusyo/chihou/r06data/2024data/r06czb01-04.html)は、民生費を児童・高齢者・障害者などの福祉施設の整備と運営、生活保護の実施などに要する経費と説明しています。県の財政課や福祉部局、議会の調査担当が自県の福祉の支出を他県と比較するときは、県の間の差がどのくらいの幅にあるかを知ると、自県の値が多いか少ないかを判断できます。

## 住民1人あたりの民生費の差は、1975年度の4.71倍から2022年度の1.80倍に縮んだ

データは e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別の行政基盤テーブル（`d_pref_administration`）から取得しています。都道府県の普通会計の決算額で、単位は千円です。この記事では次の項目を使います。

| コード   | 内容                         |
| -------- | ---------------------------- |
| D3103    | 歳出決算総額（都道府県財政） |
| D310303  | 民生費（都道府県財政）       |
| D3103031 | 社会福祉費（都道府県財政）   |
| D3103032 | 老人福祉費（都道府県財政）   |
| D3103033 | 児童福祉費（都道府県財政）   |
| D3103034 | 生活保護費（都道府県財政）   |
| D3103035 | 災害救助費（都道府県財政）   |

民生費は、社会福祉費・老人福祉費・児童福祉費・生活保護費・災害救助費の5つの費目に分かれます。この記事の民生費は、民生費（`D310303`）から災害救助費（`D3103035`）を引いた額です。災害救助費は年度によって大きく増減し、2011〜2016年度は全国の民生費の構成比を0.7〜1.7ポイント押し上げているためです。住民1人あたりの額は、この民生費を同じ年の総人口（`a_pref_population` の `A1101`）で割って計算しています。収録年度は次の表のとおりで、2022年度が最新です。

```sql
SELECT * FROM coverage
```

47都道府県を住民1人あたりの民生費で並べ、最も多い都道府県と最も少ない都道府県の比と、上位10都道府県の平均と下位10都道府県の平均の比を年度ごとに計算しました。

```chart
{
  "data": {"name": "spread"},
  "mark": {"type": "line", "point": {"filled": true, "size": 16}},
  "encoding": {
    "x": {"field": "year", "type": "quantitative", "scale": {"zero": false}, "axis": {"title": "年度", "format": "d"}},
    "y": {"field": "ratio", "type": "quantitative", "scale": {"zero": false}, "axis": {"title": "住民1人あたり民生費の比（倍）", "grid": true}},
    "color": {"field": "measure", "type": "nominal", "title": null, "legend": {"orient": "top", "columns": 1, "labelLimit": 0}},
    "tooltip": [
      {"field": "year", "type": "quantitative", "title": "年度"},
      {"field": "measure", "type": "nominal", "title": "比"},
      {"field": "ratio", "type": "quantitative", "title": "倍", "format": ".2f"}
    ]
  }
}
```

最も多い都道府県と最も少ない都道府県の比は、1975年度の4.71倍（高知県と神奈川県）から2022年度の1.80倍（沖縄県と埼玉県）まで縮みました。上位10都道府県の平均と下位10都道府県の平均の比も、2.80倍から1.54倍に縮んでいます。最多÷最少は2004年度から2005年度に3.44倍から2.64倍へ下がり、2011〜2021年度は2.02〜2.20倍の間にあり、1.80倍まで下がったのは2022年度です。上位10都道府県の平均と下位10都道府県の平均の比は2021年度が1.55倍、2022年度が1.54倍で、2022年度だけの動きではありません。この間に全国の住民1人あたりの民生費は名目で0.76万円から7.41万円に増え、歳出の総額に占める民生費の割合（構成比）は5.9%から15.0%に上がりました。

ここまでの額は都道府県の普通会計の民生費で、市町村の民生費は含みません。同じテーブルにある市町村の民生費（`D320303`）を47都道府県で合計すると、2022年度は都道府県の民生費の2.67倍です。地方財政白書は、市町村の額が大きいのは児童福祉と社会福祉施設の整備・運営の事務を主に市町村が受け持ち、生活保護の事務も市町村が行うためだと説明しています。

## 民生費の41.5%が高齢者向けになり、生活保護費を除く3つの費目は県の差が縮んだ

4つの費目について、民生費に占める割合と、住民1人あたりの額の最多÷最少を1975年度と2022年度で比較します。4つの割合を足すと、丸めの誤差を除いて100%になります。

```sql
SELECT * FROM items
```

老人福祉費は1975年度に民生費の19.6%でしたが、2022年度には41.5%を占める最大の費目になりました。地方財政白書によると、都道府県の老人福祉費が民生費の中で最も大きいのは、後期高齢者医療と介護保険の会計へ負担金を出しているためです。住民1人あたりの最多÷最少は、老人福祉費が4.75倍から1.83倍、社会福祉費が10.73倍から2.29倍、児童福祉費が4.54倍から2.87倍と、3つの費目とも縮んでいます。

生活保護費だけは逆で、民生費に占める割合が24.5%から2.5%に下がり、住民1人あたりの最多÷最少は28.59倍から56.36倍に広がりました。白書は、生活保護の事務を行うのは市と、福祉事務所を置く町村だと説明しています。この分担から、都道府県の生活保護費は市に住む人が多い県ほど小さくなると考えられるので、住民1人あたりの56.36倍は、県の間の生活保護の多さの差を表していません。

## 千葉県と神奈川県は、48年度すべてで住民1人あたりの民生費が44〜47位

2022年度の住民1人あたりの民生費を47都道府県で並べます。

```chart
{
  "height": 1100,
  "data": {"name": "rank_2022"},
  "mark": "bar",
  "encoding": {
    "y": {"field": "area_name", "type": "nominal", "sort": "-x", "title": null},
    "x": {"field": "welfare_pc", "type": "quantitative", "axis": {"title": "住民1人あたり民生費（万円）", "grid": true}},
    "color": {"field": "grp", "type": "nominal", "title": null, "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3182bd", "#9ecae1", "#94a3b8"]}, "legend": {"orient": "top"}},
    "tooltip": [
      {"field": "area_name", "type": "nominal", "title": "都道府県"},
      {"field": "welfare_pc", "type": "quantitative", "title": "1人あたり民生費（万円）", "format": ".2f"},
      {"field": "rank", "type": "quantitative", "title": "順位"}
    ]
  }
}
```

最も多いのは沖縄県の10.24万円、最も少ないのは埼玉県の5.69万円です。43位から47位は愛知県・静岡県・千葉県・神奈川県・埼玉県でした。1975年度から2022年度までの48年度について、44〜47位（下から4番目まで）に入った年度の数を集計すると、千葉県と神奈川県が48年度すべて、埼玉県が46年度、静岡県が29年度、愛知県が21年度で、この5県のほかに入った県はありません。

```sql
SELECT * FROM bottom4
```

65歳以上の人口の割合は、静岡県を除く4県が47都道府県の40〜45位です。5県とも、2022年度の住民1人あたりの老人福祉費は37〜47位ですが、65歳以上の人1人あたりで比較すると、神奈川県は10.22万円で33位です（47都道府県の中央値は10.80万円）。老人福祉費を除いた民生費の住民1人あたりの額も、愛知県（38位）を除く4県は42〜47位にあります。

```sql
SELECT * FROM metro_2022
```

ここまでの順位は都道府県の会計だけのものです。同じテーブルの市町村の民生費（`D320303`、災害救助費 `D3203035` を除く）を足して住民1人あたりで並べると、2022年度の神奈川県は31位、愛知県は37位に上がります。千葉県は44位、埼玉県は46位、静岡県は47位で、県と市町村を足しても下位に残ります。大阪府は都道府県の会計だけでは23位ですが、足すと4位になります。県から市町村へ渡す支出は県と市町村の両方の民生費に計上されるので、この合計は重複を含み、地方財政白書の民生費の決算額（重複を除いた額）より大きくなります。重複の大きさは県ごとに異なる可能性があるので、足した順位は目安です。

```sql
SELECT * FROM combined_2022
```

歳出の総額に占める民生費の割合で並べると、2022年度は神奈川県が21.8%で1位、埼玉県が18.7%で2位です。この2県は民生費以外の歳出が住民1人あたりで47位と46位と少ないので、同じ民生費でも構成比が高く出ます。

## 自県の民生費を他県と比較するときの注意

- 住民1人あたりの民生費の県の差は、上位10都道府県の平均と下位10都道府県の平均の比で1975年度の2.80倍から2022年度の1.54倍に縮んでいます。自県の値は、47都道府県の中央値（2022年度は7.66万円）と比較すると、全国の中での位置を確認できます。
- 民生費の4割を占める老人福祉費には、後期高齢者医療と介護保険の会計への負担金が入ります。高齢者の人数の違いを除いて比較するときは、65歳以上の人1人あたりの額を使います。神奈川県の老人福祉費は住民1人あたりで42位、65歳以上の人1人あたりで33位です。
- 福祉の事務の多くは市町村が受け持つので、県の会計だけの順位で県の福祉の手厚さを説明しないようにします。2022年度の神奈川県は、県だけでは46位ですが、重複を含む市町村との合計では31位です。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別の行政基盤データと人口データを2026年11月16日時点で集計しています。元データは総務省の地方財政状況調査と人口推計・国勢調査で、財政の値は普通会計の年度の決算額、人口は各年10月1日現在の値です。各項目の定義は[項目定義（D 行政基盤）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/D)にあります。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の行政基盤テーブル](/datasets/queria/e_stat/ssds/d_pref_administration)から、自県と他県の民生費を、費目ごとの額や市町村の分を含めた額で、48年度分並べられます。

```sql id=base
-- 都道府県×年度の歳出・民生費（災害救助費を除く）・費目・人口。金額は千円、1人あたりは万円
-- 災害救助費は広島県の1986年度だけ値が無いので0として扱う
WITH f AS (
  SELECT year, area_name,
    SUM(CASE WHEN cat01 = 'D3103' THEN TRY_CAST(value AS DOUBLE) END) AS total,
    SUM(CASE WHEN cat01 = 'D310303' THEN TRY_CAST(value AS DOUBLE) END) AS minsei,
    COALESCE(SUM(CASE WHEN cat01 = 'D3103035' THEN TRY_CAST(value AS DOUBLE) END), 0) AS disaster,
    SUM(CASE WHEN cat01 = 'D3103031' THEN TRY_CAST(value AS DOUBLE) END) AS shakai,
    SUM(CASE WHEN cat01 = 'D3103032' THEN TRY_CAST(value AS DOUBLE) END) AS rojin,
    SUM(CASE WHEN cat01 = 'D3103033' THEN TRY_CAST(value AS DOUBLE) END) AS jido,
    SUM(CASE WHEN cat01 = 'D3103034' THEN TRY_CAST(value AS DOUBLE) END) AS hogo
  FROM e_stat.ssds.d_pref_administration
  WHERE cat01 IN ('D3103', 'D310303', 'D3103031', 'D3103032', 'D3103033', 'D3103034', 'D3103035')
    AND area_name <> '全国' AND year BETWEEN 1975 AND 2022
  GROUP BY year, area_name
), p AS (
  SELECT year, area_name,
    SUM(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop,
    SUM(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS elderly
  FROM e_stat.ssds.a_pref_population
  WHERE cat01 IN ('A1101', 'A1303') AND area_name <> '全国' AND year BETWEEN 1975 AND 2022
  GROUP BY year, area_name
)
SELECT year, area_name, total, minsei, disaster, minsei - disaster AS welfare, total - (minsei - disaster) AS other,
  shakai, rojin, jido, hogo, pop, elderly,
  (minsei - disaster) / total * 100 AS share,
  (minsei - disaster) / pop / 10 AS welfare_pc,
  (total - (minsei - disaster)) / pop / 10 AS other_pc
FROM f JOIN p USING (year, area_name)
```

```sql id=coverage
-- 使った項目と収録年度
SELECT table_name AS "テーブル", cat01 AS "コード", regexp_replace(item_name, '^[A-Z][0-9]+_', '') AS "内容", min_year AS "最初の年度", max_year AS "最後の年度"
FROM e_stat.ssds.series_coverage
WHERE (table_name = 'd_pref_administration' AND cat01 IN ('D3103', 'D310303', 'D320303', 'D3203035', 'D3103031', 'D3103032', 'D3103033', 'D3103034', 'D3103035'))
  OR (table_name = 'a_pref_population' AND cat01 IN ('A1101', 'A1303'))
ORDER BY table_name DESC, cat01
```

```sql id=national
-- 全国（47都道府県の合計）の構成比と住民1人あたり民生費。災害救助費を含めた構成比も並べる（プロットはしない）
SELECT year,
  ROUND(SUM(welfare) / SUM(total) * 100, 1) AS share,
  ROUND(SUM(minsei) / SUM(total) * 100, 1) AS share_with_disaster,
  ROUND(SUM(minsei) / SUM(total) * 100 - SUM(welfare) / SUM(total) * 100, 1) AS disaster_points,
  ROUND(SUM(welfare) / SUM(pop) / 10, 2) AS welfare_pc
FROM base GROUP BY year ORDER BY year
```

```sql id=spread
-- 住民1人あたり民生費の、最多÷最少と上位10平均÷下位10平均。max_area / min_area は最多と最少の都道府県
WITH r AS (
  SELECT year, area_name, welfare_pc, ROW_NUMBER() OVER (PARTITION BY year ORDER BY welfare_pc DESC, area_name) AS rn FROM base
)
SELECT year, '最多の都道府県÷最少の都道府県' AS measure, ROUND(MAX(welfare_pc) / MIN(welfare_pc), 2) AS ratio,
  arg_max(area_name, welfare_pc) AS max_area, arg_min(area_name, welfare_pc) AS min_area
FROM r GROUP BY year
UNION ALL
SELECT year, '上位10都道府県の平均÷下位10都道府県の平均' AS measure, ROUND(AVG(welfare_pc) FILTER (WHERE rn <= 10) / AVG(welfare_pc) FILTER (WHERE rn > 37), 2) AS ratio,
  NULL AS max_area, NULL AS min_area
FROM r GROUP BY year
ORDER BY measure, year
```

```sql id=municipal
-- 47都道府県の合計で、市町村の民生費（D320303）が都道府県の民生費（D310303 から災害救助費を除く）の何倍か（プロットはしない）
SELECT year, ROUND(SUM(CASE WHEN cat01 = 'D320303' THEN TRY_CAST(value AS DOUBLE) END) / (SUM(CASE WHEN cat01 = 'D310303' THEN TRY_CAST(value AS DOUBLE) END) - COALESCE(SUM(CASE WHEN cat01 = 'D3103035' THEN TRY_CAST(value AS DOUBLE) END), 0)), 2) AS municipal_to_pref
FROM e_stat.ssds.d_pref_administration
WHERE cat01 IN ('D310303', 'D3103035', 'D320303') AND area_name <> '全国' AND year BETWEEN 1975 AND 2022
GROUP BY year ORDER BY year
```

```sql id=combined_2022
-- 2022年度の、都道府県と市町村の民生費（どちらも災害救助費を除く）の住民1人あたりの額と順位。表には本文で触れた6府県を出す
WITH m AS (
  SELECT area_name,
    SUM(CASE WHEN cat01 = 'D320303' THEN TRY_CAST(value AS DOUBLE) END)
      - COALESCE(SUM(CASE WHEN cat01 = 'D3203035' THEN TRY_CAST(value AS DOUBLE) END), 0) AS muni
  FROM e_stat.ssds.d_pref_administration
  WHERE cat01 IN ('D320303', 'D3203035') AND area_name <> '全国' AND year = 2022
  GROUP BY area_name
), v AS (
  SELECT b.area_name, b.welfare_pc, m.muni / b.pop / 10 AS muni_pc, (b.welfare + m.muni) / b.pop / 10 AS both_pc
  FROM base b JOIN m USING (area_name) WHERE b.year = 2022
), r AS (
  SELECT *, RANK() OVER (ORDER BY welfare_pc DESC) AS r1, RANK() OVER (ORDER BY muni_pc DESC) AS r2, RANK() OVER (ORDER BY both_pc DESC) AS r3 FROM v
)
SELECT area_name AS "都道府県",
  printf('%.2f（%d位）', welfare_pc, r1) AS "都道府県の民生費（万円/人）",
  printf('%.2f（%d位）', muni_pc, r2) AS "市町村の民生費（万円/人）",
  printf('%.2f（%d位）', both_pc, r3) AS "合計（万円/人）"
FROM r WHERE area_name IN ('神奈川県', '愛知県', '千葉県', '埼玉県', '静岡県', '大阪府')
ORDER BY r1
```

```sql id=items
-- 費目ごとの、民生費に占める割合と住民1人あたりの最多÷最少（1975・2022年度）
WITH t AS (
  SELECT year, '老人福祉費' AS item, 'D3103032' AS code, rojin AS v, welfare, pop FROM base
  UNION ALL SELECT year, '社会福祉費', 'D3103031', shakai, welfare, pop FROM base
  UNION ALL SELECT year, '児童福祉費', 'D3103033', jido, welfare, pop FROM base
  UNION ALL SELECT year, '生活保護費', 'D3103034', hogo, welfare, pop FROM base
), s AS (
  SELECT item, code, year, SUM(v) / SUM(welfare) * 100 AS share, MAX(v / pop) / MIN(v / pop) AS max_min
  FROM t WHERE year IN (1975, 2022) GROUP BY item, code, year
)
SELECT item AS "費目", code AS "コード",
  ROUND(MAX(share) FILTER (WHERE year = 1975), 1) AS "民生費に占める割合 1975年度（%）",
  ROUND(MAX(share) FILTER (WHERE year = 2022), 1) AS "民生費に占める割合 2022年度（%）",
  ROUND(MAX(max_min) FILTER (WHERE year = 1975), 2) AS "1人あたり 最多÷最少 1975年度",
  ROUND(MAX(max_min) FILTER (WHERE year = 2022), 2) AS "1人あたり 最多÷最少 2022年度"
FROM s GROUP BY item, code ORDER BY "民生費に占める割合 2022年度（%）" DESC
```

```sql id=ranks
-- 年度ごとの住民1人あたり民生費・構成比・住民1人あたり民生費以外の歳出の順位（同値は同順位）
SELECT year, area_name, ROUND(share, 1) AS share, ROUND(welfare_pc, 2) AS welfare_pc, ROUND(other_pc, 2) AS other_pc,
  RANK() OVER (PARTITION BY year ORDER BY welfare_pc DESC) AS welfare_pc_rank,
  RANK() OVER (PARTITION BY year ORDER BY share DESC) AS share_rank,
  RANK() OVER (PARTITION BY year ORDER BY other_pc DESC) AS other_pc_rank
FROM base
```

```sql id=rank_2022
-- 2022年度の住民1人あたり民生費の順位と、上位10・中間・下位10の区分。構成比と民生費以外の歳出の順位も並べる
WITH r AS (
  SELECT area_name, welfare_pc, share, other_pc, welfare_pc_rank AS rank, share_rank, other_pc_rank,
    ROW_NUMBER() OVER (ORDER BY welfare_pc DESC, area_name) AS rn
  FROM ranks WHERE year = 2022
)
SELECT area_name, welfare_pc, rank, share, share_rank, other_pc, other_pc_rank,
  CASE WHEN rn <= 10 THEN '上位10' WHEN rn > 37 THEN '下位10' ELSE '中間' END AS grp
FROM r ORDER BY rn
```

```sql id=bottom4
-- 住民1人あたり民生費で下位4位（44位以下）に入った年度の数（1975〜2022年度の48年度）
SELECT area_name AS "都道府県", COUNT(*) AS "下位4位に入った年度の数", MIN(welfare_pc_rank) AS "最も高い順位", MAX(welfare_pc_rank) AS "最も低い順位"
FROM ranks WHERE welfare_pc_rank >= 44
GROUP BY area_name ORDER BY "下位4位に入った年度の数" DESC, area_name
```

```sql id=metro_2022
-- 2022年度に住民1人あたり民生費が43〜47位の5県と、47都道府県の中央値。金額は万円、括弧内は47都道府県の中の順位
WITH v AS (
  SELECT area_name, welfare_pc, rojin / pop / 10 AS rojin_pc, elderly / pop * 100 AS elderly_pct,
    rojin / elderly / 10 AS rojin_per_elderly, (welfare - rojin) / pop / 10 AS non_rojin_pc
  FROM base WHERE year = 2022
), r AS (
  SELECT *,
    RANK() OVER (ORDER BY welfare_pc DESC) AS r1, RANK() OVER (ORDER BY rojin_pc DESC) AS r2,
    RANK() OVER (ORDER BY elderly_pct DESC) AS r3, RANK() OVER (ORDER BY rojin_per_elderly DESC) AS r4,
    RANK() OVER (ORDER BY non_rojin_pc DESC) AS r5
  FROM v
), t AS (
  SELECT area_name AS "都道府県",
    printf('%.2f（%d位）', welfare_pc, r1) AS "住民1人あたり民生費",
    printf('%.2f（%d位）', rojin_pc, r2) AS "住民1人あたり老人福祉費",
    printf('%.1f%%（%d位）', elderly_pct, r3) AS "65歳以上の割合",
    printf('%.2f（%d位）', rojin_per_elderly, r4) AS "65歳以上1人あたり老人福祉費",
    printf('%.2f（%d位）', non_rojin_pc, r5) AS "老人福祉費を除く住民1人あたり民生費",
    r1 AS ord
  FROM r WHERE r1 >= 43
  UNION ALL
  SELECT '47都道府県の中央値', printf('%.2f', MEDIAN(welfare_pc)), printf('%.2f', MEDIAN(rojin_pc)), printf('%.1f%%', MEDIAN(elderly_pct)),
    printf('%.2f', MEDIAN(rojin_per_elderly)), printf('%.2f', MEDIAN(non_rojin_pc)), 99
  FROM v
)
SELECT * EXCLUDE (ord) FROM t ORDER BY ord
```
