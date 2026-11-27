---
title: 補助金の申請サイトで1つの都道府県に絞った募集は、東京都が615回、栃木県は1回
description: デジタル庁のJグランツで対象地域を1つの都道府県に絞った補助金の募集1,360回のうち、615回（45%）が東京都です。事業所1万か所あたりでは東京都が10.7回、栃木県が0.1回で、82倍の差があります。
publishedAt: 2026-11-27
author:
  name: UD
  url: https://udus.dev
tags:
  - 補助金
  - 中小企業
  - Jグランツ
  - 都道府県
datasets:
  - queria/jgrants
  - queria/e_stat
sources:
  - title: Jグランツ
    url: https://www.jgrants-portal.go.jp/
    publisher: デジタル庁
  - title: 令和3年経済センサス‐活動調査
    url: https://www.stat.go.jp/data/e-census/2021/index.html
    publisher: 総務省統計局
agentHint: 自分の県を対象に1つの都道府県だけで募集された補助金を、募集回ごとに受付期間と上限額つきで一覧にして
socialAnnounce: |-
  Jグランツで1つの都道府県に絞った補助金の募集は、掲載全体で1,360回あり、615回が東京都です。栃木県は1回、茨城県は3回です。

  県内の中小企業に補助金を案内する担当者向けに、事業所数あたりの回数と年ごとの増え方も集計しました。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

デジタル庁の補助金申請サイト[Jグランツ](https://www.jgrants-portal.go.jp/)には、2026年11月27日時点で5,308回の募集回が載っています。このうち対象地域を1つの都道府県だけに絞った募集回は1,360回で、615回（45%）が東京都です。栃木県は1回、茨城県は3回、千葉県は6回で、事業所数が全国2位の大阪府も18回にとどまります。

県内の中小企業に補助金を案内する商工会議所の経営指導員は、自県の事業者が申請できる補助金をまとめて探す場面があります。Jグランツは国の補助金だけでなく、都道府県や市区町村の補助金も載せています。募集回は、補助金1件の1回ごとの受付を数える単位です。同じ補助金が年に3回募集されると3回に数えます。事業所数は、総務省の[令和3年経済センサス‐活動調査](https://www.stat.go.jp/data/e-census/2021/index.html)の、公務を除く全産業の事業所数（民営）です。

## 1つの都道府県に絞った募集回の45%は東京都で、栃木県は1回だけ

使ったのはJグランツの募集回（`jgrants.subsidy.rounds`）と、募集回ごとの対象地域（`jgrants.subsidy.round_areas`）です。対象地域は1行が1つの地域で、区分（`area_level`）は全国（`national`）、地方（`region`）、都道府県（`prefecture`）、海外（`overseas`）のどれかです。全国を対象にした募集回は、全国の1行を持ちます。ここでは、全国を含まず、対象の都道府県が1つだけの募集回を「1つの都道府県に絞った募集回」と呼びます。実施主体が国、都道府県、市区町村のどれかは区別していません。

| 対象地域                       | 募集回数 |
| ------------------------------ | -------- |
| 全国                           | 3,658    |
| 1つの都道府県                  | 1,360    |
| 複数の都道府県                 | 205      |
| 地方のみ・海外・地域の記載なし | 85       |

募集回の7割（3,658回）は全国が対象で、どの県の事業者にも申請の資格があります。県ごとに差が出るのは、1つの都道府県に絞った1,360回です。

```chart
{
  "data": { "name": "pref_rank" },
  "mark": "bar",
  "height": 1100,
  "encoding": {
    "y": { "field": "pref", "type": "nominal", "sort": "-x", "title": null },
    "x": { "field": "n", "type": "quantitative", "title": "1つの都道府県に絞った募集回数" },
    "color": {
      "field": "grp",
      "type": "nominal",
      "title": null,
      "scale": { "domain": ["東京都", "東京都以外"], "range": ["#3182bd", "#94a3b8"] }
    },
    "tooltip": [{ "field": "pref" }, { "field": "n", "format": "," }]
  }
}
```

東京都が615回、2位の北海道が64回、3位の愛知県が60回です。東京都1都の615回は、残り46道府県の合計745回の8割に当たります。栃木県の1回、茨城県の3回、香川県の4回のように、10回に満たない県が19あります。

ここで数えたのは、Jグランツに載った募集回の数です。各県が公募している補助金の総数ではありません。

## 事業所1万か所あたりでも、東京都は10.7回で栃木県の82倍

東京都は事業所数が全国で最も多いので、事業所数で割った値も確認します。経済センサスの事業所数で割ると、1つの都道府県に絞った募集回数は、事業所1万か所あたりで次のようになります。

```map
type: map
caption: 事業所1万か所あたりの、1つの都道府県に絞った募集回数
layers:
  - from: pref_rank
    area: prefecture
    code: pcode
    color: per10k
    label: pref
    name: 事業所1万か所あたりの募集回数
```

```sql
SELECT rk AS 順位, pref AS 都道府県, n AS 募集回数, est AS 事業所数, per10k AS "1万か所あたり" FROM pref_ends ORDER BY rk
```

東京都は10.66回で、2位の福井県が8.87回、3位の石川県が6.32回、4位の福島県が5.37回です。最も少ない栃木県は0.13回で、東京都はその82倍です。事業所数が全国2位の大阪府は0.51回、神奈川県は0.49回、千葉県は0.35回です。事業所数が多い県でも回数が少ない県があり、福井県や石川県のように事業所数が少なくても回数が多い県があります。

地図で濃い県は、事業所数に対して、その県だけを対象にした募集回がJグランツに多く載っている県です。その県で公募される補助金の総数を示すものではありません。

## 2021年の66回から2026年の525回に増え、掲載する県は23から47に広がった

受付開始日が属する年ごとに、1つの都道府県に絞った募集回数を、東京都と東京都以外に分けて集計しました。2026年は今後受付を始める募集回を含みます。受付開始日が2020年の1回と2027年の28回は図から除いています。

```chart
{
  "data": { "name": "by_year" },
  "mark": "bar",
  "encoding": {
    "x": { "field": "year", "type": "ordinal", "title": "受付開始日の年" },
    "y": { "field": "n", "type": "quantitative", "title": "募集回数" },
    "color": {
      "field": "grp",
      "type": "nominal",
      "title": null,
      "scale": { "domain": ["東京都", "東京都以外"], "range": ["#3182bd", "#94a3b8"] }
    },
    "tooltip": [{ "field": "year" }, { "field": "grp" }, { "field": "n", "format": "," }]
  }
}
```

```sql
SELECT year AS 年, total AS 合計, tokyo AS 東京都, other AS 東京都以外, round(tokyo * 100.0 / total) AS "東京都の割合（%）", pref_count AS 募集回のある都道府県数 FROM by_year_wide ORDER BY year
```

募集回数は2021年の66回から2026年の525回へ、Jグランツに載る募集回数は約8倍になりました。東京都は12回から228回へ19倍、東京都以外は54回から297回へ5.5倍です。東京都の割合は2021年の18%から2024年の59%まで上がり、2026年は43%です。募集回のある都道府県は2021年の23から2026年の47に増え、2026年に初めて全都道府県で1回以上の募集回が載りました。

## 自県を対象にした募集回は、県によってJグランツへの掲載数が大きく違う

1つの都道府県に絞った募集回は、県ごとの差が大きく、Jグランツの掲載数は、各県で公募される補助金の数と同じとは限りません。商工会議所や税理士の事務所で補助金を案内するときは、次の使い方ができます。

- 東京都の事業者には、Jグランツで東京都を対象に絞った615回から候補を探せます
- 栃木県や茨城県のように1回から3回しか載っていない県では、Jグランツで見つからない場合に備えて、県や市区町村の公式ページも併せて確認します
- 福井県、石川県、福島県は事業所数あたりの回数が多く、自県を対象にした募集回がJグランツで見つかりやすい県です
- 2026年は全都道府県に募集回が載ったので、自県の掲載が増えているかを、年ごとの回数で定期的に確認できます

## データの出典

本記事は、デジタル庁の補助金申請サイト[Jグランツ](https://www.jgrants-portal.go.jp/)の募集回と対象地域を2026年11月27日時点で集計し、総務省統計局の[令和3年経済センサス‐活動調査](https://www.stat.go.jp/data/e-census/2021/index.html)の都道府県別の事業所数と突き合わせています。

Queriaは、Jグランツの募集回と経済センサスの事業所数を、列名と単位を揃えて公開しています。データを集めて加工する手間をかけずに、[Jグランツの募集回テーブル](/datasets/queria/jgrants/subsidy/rounds)と[経済センサスの事業所数テーブル](/datasets/queria/e_stat/economic_census/establishment_industry)から、自県の募集回の数を確かめたり、受付期間や上限額を調べたりできます。県内の事業者に補助金を案内する担当者は、探す先を決める判断に時間を使えます。

```sql id=kinds
-- 募集回数を対象地域の区分で数える（表は本文に手書きしているため、本文の数字の裏付け）
WITH lv AS (
  SELECT round_id,
    bool_or(area_level = 'national') AS nat,
    count(DISTINCT area_name) FILTER (WHERE area_level = 'prefecture') AS np
  FROM jgrants.subsidy.round_areas
  GROUP BY round_id
)
SELECT
  CASE
    WHEN lv.nat THEN '全国'
    WHEN lv.np = 1 THEN '1つの都道府県'
    WHEN lv.np > 1 THEN '複数の都道府県'
    ELSE '地方のみ・海外・地域の記載なし'
  END AS kind,
  count(*) AS n
FROM jgrants.subsidy.rounds r
LEFT JOIN lv USING (round_id)
GROUP BY 1
ORDER BY 2 DESC
```

```sql id=one
-- 全国を含まず、対象の都道府県が1つだけの募集回（プロットはしない）
SELECT round_id, pref, pcode
FROM (
  SELECT round_id,
    bool_or(area_level = 'national') AS nat,
    count(DISTINCT area_name) FILTER (WHERE area_level = 'prefecture') AS np,
    min(area_name) FILTER (WHERE area_level = 'prefecture') AS pref,
    min(prefecture_code) FILTER (WHERE area_level = 'prefecture') AS pcode
  FROM jgrants.subsidy.round_areas
  GROUP BY round_id
)
WHERE NOT nat AND np = 1
```

```sql id=pref_rank
WITH c AS (
  SELECT pref, pcode, count(*) AS n FROM one GROUP BY 1, 2
),
e AS (
  SELECT area_name, establishments AS est
  FROM e_stat.economic_census.establishment_industry
  WHERE area_level = 'prefecture' AND industry_code = 'AR' AND organization_code = '0'
)
SELECT c.pref, c.pcode, c.n, e.est,
  round(c.n * 10000.0 / e.est, 2) AS per10k,
  CASE WHEN c.pref = '東京都' THEN '東京都' ELSE '東京都以外' END AS grp
FROM c JOIN e ON e.area_name = c.pref
ORDER BY c.n DESC, c.pref
```

```sql id=pref_ends
SELECT rank() OVER (ORDER BY per10k DESC) AS rk, pref, n, est, per10k
FROM pref_rank
QUALIFY rk <= 5 OR rk >= 43
```

```sql id=by_year
SELECT strftime(r.acceptance_start_at, '%Y') AS year,
  CASE WHEN o.pref = '東京都' THEN '東京都' ELSE '東京都以外' END AS grp,
  count(*) AS n
FROM one o JOIN jgrants.subsidy.rounds r USING (round_id)
WHERE strftime(r.acceptance_start_at, '%Y') BETWEEN '2021' AND '2026'
GROUP BY 1, 2
ORDER BY 1, 2
```

```sql id=by_year_wide
SELECT strftime(r.acceptance_start_at, '%Y') AS year,
  count(*) AS total,
  count(*) FILTER (WHERE o.pref = '東京都') AS tokyo,
  count(*) FILTER (WHERE o.pref <> '東京都') AS other,
  count(DISTINCT o.pref) AS pref_count
FROM one o JOIN jgrants.subsidy.rounds r USING (round_id)
WHERE strftime(r.acceptance_start_at, '%Y') BETWEEN '2021' AND '2026'
GROUP BY 1
```

```sql id=stats
-- 本文の数字の裏付け（プロットはしない）
SELECT
  (SELECT count(*) FROM jgrants.subsidy.rounds) AS rounds_total,
  (SELECT count(*) FROM one) AS single_total,
  (SELECT count(*) FROM one WHERE pref = '東京都') AS tokyo,
  (SELECT count(*) FROM one WHERE pref <> '東京都') AS others,
  (SELECT count(*) FROM pref_rank WHERE n < 10) AS prefs_under_10,
  (SELECT count(*) FROM one WHERE round_id IN (SELECT round_id FROM jgrants.subsidy.rounds WHERE strftime(acceptance_start_at, '%Y') = '2020')) AS y2020,
  (SELECT count(*) FROM one WHERE round_id IN (SELECT round_id FROM jgrants.subsidy.rounds WHERE strftime(acceptance_start_at, '%Y') = '2027')) AS y2027
```
