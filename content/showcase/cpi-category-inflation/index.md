---
title: 消費者物価の7割超の品目が値上がりする状態は52か月続き、消費税の引き上げのあとの12か月より長い
description: 消費者物価指数で値段を調べている品目のうち、前年同月より値上がりした品目の割合は2022年6月から2026年9月まで52か月続けて7割を超えました。消費税の引き上げのあと7割を超えていた期間は、1997年・2014年・2019年のどれも12か月です。
publishedAt: 2026-06-24
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 物価
  - 消費者物価指数
  - インフレ
datasets:
  - queria/e_stat
sources:
  - title: 消費者物価指数（CPI）
    url: https://www.stat.go.jp/data/cpi/
    publisher: 総務省統計局
  - title: 2020年基準 消費者物価指数の解説
    url: https://www.stat.go.jp/data/cpi/2020/kaisetsu/index.html
    publisher: 総務省統計局
agentHint: 2026年9月に前年同月より10%以上値上がりした品目を、上昇率の大きい順に品目名と指数で出して
socialAnnounce: |-
  消費者物価指数の品目のうち前年同月より値上がりした品目の割合は、2022年6月から52か月続けて7割超。消費税の引き上げのあとは、どれも12か月で7割を割りました。

  販売価格の改定の判断に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2026年9月は、消費者物価指数の575品目のうち434品目（75.5%）が前年同月より値上がりしていました。値上がりした品目が7割を超える月は2022年6月から52か月続いています。1997年・2014年・2019年の消費税の引き上げのあとに7割を超えていた期間は、どれも12か月で終わっています。

総務省統計局の[消費者物価指数（CPI）](https://www.stat.go.jp/data/cpi/)は、家計が買う商品とサービスの値段を品目ごとに毎月調査しています。米・キャベツ・電気代・家賃・授業料・宿泊料などが1品目ずつ指数になっていて、2026年9月に前年同月の指数と比較できる品目は575あります。品目ごとに前年同月の指数と比較し、値上がりした品目の割合を集計すると、値上がりが一部の品目に限られているのか、ほとんどの品目に及んでいるのかが分かります。

## 7割を超える期間は、消費税の引き上げのあとは12か月で終わり、2022年6月からは52か月続いている

下の図は、品目ごとの指数を前年同月と比較し、値上がりした品目の割合を毎月出したものです。品目は、指数の分類コード（`cat01`）が1000以上のものです。1000未満のコードは「食料」「光熱・水道」のような品目をまとめた分類なので、集計に含めていません。指数が前年同月とまったく同じ品目は、値上がりした品目に入れていません。

1品目を1件として集計しているので、米も切り花も同じ重みです。家計の支出に占める割合で重み付けした総合指数の上昇率とは別の数字で、割合が高くても総合指数の上昇率が高いとは限りません。また、品目は5年ごとの基準改定で入れ替わり、比較できる品目の数は1971年1月の233から2026年9月の575まで増えています。

```chart caption="前年同月より指数が上がった品目の割合（全国、月次）"
{
  "layer": [
    {
      "data": {"name": "monthly_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"up_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 1.5,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "month", "type": "temporal"},
          {"field": "up_pct", "type": "quantitative"}
        ],
        "x": {"field": "month", "type": "temporal", "axis": {"title": "年月"}},
        "y": {
          "field": "up_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "値上がりした品目の割合（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeWidth": 1, "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 70, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 0.52"}},
        "y": {"datum": 70, "type": "quantitative"},
        "text": {"value": "7割"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

値上がりした品目の割合が基準以上の月が12か月以上続いた期間を並べたのが次の表です。基準は6割・7割・8割の3通りです。

```sql
SELECT threshold AS "基準（%）", start_month AS 始まり, end_month AS 終わり, months AS 月数, up_pct_max AS "値上がりした品目の割合の最高（%）", cpi_yoy_avg AS "総合指数の前年同月比の平均（%）", cpi_yoy_max AS "総合指数の前年同月比の最大（%）" FROM streaks ORDER BY threshold, start_month
```

7割の基準では、1997年4月・2014年4月・2019年10月から始まった期間はどれもちょうど12か月で終わっています。いずれも消費税が引き上げられた月です。消費者物価指数は消費税を含んだ値段で調べているので（[2020年基準 消費者物価指数の解説](https://www.stat.go.jp/data/cpi/2020/kaisetsu/index.html)）、税率が上がると課税される品目の指数が一斉に上がり、前年同月との比較にその差が出るのは12か月の間だけです。1989年4月の消費税の導入から始まった期間は、導入から1年を過ぎても1992年6月まで続き、39か月になりました。

2022年6月からの期間は52か月で、2026年9月の時点でまだ続いています。7割の基準でこれより長いのは1972年11月から1978年4月までの66か月だけで、1979年11月から1983年7月までの45か月や、1989年4月からの39か月よりも長くなっています。基準を6割に下げると2022年以降の期間は2022年2月からの56か月になり、これを上回るのは186か月の期間だけです。この期間は、比較できる最初の月の1971年1月にすでに6割を超えていて、1986年6月まで続きました。

一方で、8割の基準では2022年以降の期間は2023年2月から2024年1月までの12か月で、2014年4月からの期間と同じ長さです。7割の基準で見た期間中の最高も、2022年6月からの期間は2023年9月の86.6%で、2014年4月からの期間の91.1%を下回ります。2022年以降の値上がりは、2014年の消費税の引き上げのときより多くの品目に一度に及んだわけではありません。違うのは、7割を超える状態が12か月で終わらずに続いている長さです。

基準を1%刻みで動かした結果が次の表です。60〜70%のどこに基準を置いても、2022年からの期間は52〜56か月続いていて、消費税が引き上げられた1997年4月・2014年4月・2019年10月から始まった期間（最長でも27か月、64%以上では最長でも12か月）の2倍以上です。ただし、2026年2〜5月の値上がりした品目の割合は70.2〜71.0%まで下がりました。基準を71%にすると2022年からの期間は2026年1月で、72%にすると2025年12月で途切れます。7割の基準でも、2026年5月は573品目のうち402品目で、1品目少なければ7割を割っていました。

```sql
SELECT threshold AS "基準（%）", cur_start AS "2023年9月を含む期間の始まり", cur_end AS 終わり, cur_months AS 月数, tax_max AS "消費税の引き上げ（1997年・2014年・2019年）の月から始まった期間の最長（月数）", prior_max AS "2021年までに終わった期間の最長（月数）", prior_start AS その始まり FROM threshold_sensitivity ORDER BY threshold
```

指数から計算した総合指数の前年同月比は、2022年6月からの期間で平均2.8%、最大でも4.4%です。1972年11月からの66か月の平均12.1%と比較すると4分の1以下で、1989年4月からの期間の平均2.9%とほぼ同じです。総合指数の上昇率は1970年代ほど高くありませんが、値上がりした品目の割合が7割を超えたまま続いている長さは、7割の基準では1970年代に次ぐ長さです。

## 値上がりした品目の割合は2023年9月の86.6%が最も高く、2026年は7割台前半から半ばで推移している

2019年以降の月を、値上がりした品目と値下がりした品目の割合に分けて並べました。

```chart caption="前年同月より指数が上がった品目と下がった品目の割合（全国、2019年1月〜2026年9月）"
{
  "layer": [
    {
      "data": {"name": "recent_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"up_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "month", "type": "temporal"},
          {"field": "up_pct", "type": "quantitative"}
        ],
        "x": {"field": "month", "type": "temporal", "axis": {"title": "年月"}},
        "y": {
          "field": "up_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "品目の割合（%）", "grid": true}
        },
        "color": {
          "datum": "値上がりした品目",
          "type": "nominal",
          "scale": {"domain": ["値上がりした品目", "値下がりした品目"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "recent_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"down_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "month", "type": "temporal"},
          {"field": "down_pct", "type": "quantitative"}
        ],
        "x": {"field": "month", "type": "temporal", "axis": {"title": "年月"}},
        "y": {
          "field": "down_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "品目の割合（%）", "grid": true}
        },
        "color": {
          "datum": "値下がりした品目",
          "type": "nominal",
          "scale": {"domain": ["値上がりした品目", "値下がりした品目"], "range": ["#ef4444", "#3b82f6"]},
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

2019年以降で値上がりした品目の割合が最も高かったのは2023年9月の86.6%です。その後は下がり、2026年1〜9月は70.2〜75.5%で推移しています。値下がりした品目の割合は2023年9月の7.5%から、2026年9月には19.3%まで増えました。

## 2026年9月に値下がりした品目は、教育・保育の料金と米・野菜が多い

2026年9月に前年同月より指数が下がった111品目のうち、下がり幅の大きい15品目です。

```sql
SELECT item AS 品目, idx_2025_09 AS "2025年9月の指数", idx_2026_09 AS "2026年9月の指数", change_pct AS "前年同月比（%）" FROM falling_items
```

下がり幅が最も大きいのは学校給食（小学校）で、指数は78.4から1.5になりました。15品目のうち4品目は、学校給食（小学校・中学校）・私立高校の授業料（81.1→25.3）・保育所保育料といった教育や保育の料金です。これらは店が値札を付け替える値段ではなく、家計が払う額が国や自治体の負担の仕組みで動く料金です。ほかの多くは、うるち米と、にんじん・たまねぎ・トマトなどの野菜です。

米類の指数は2020年以降では2025年11月の223.4が最も高く、2026年9月には164.9まで下がりました。2020年の2倍を超えていた水準からは下がりましたが、2020年より6割以上高い状態です。

```chart caption="米類の指数（全国、2020年=100）"
{
  "layer": [
    {
      "data": {"name": "rice_monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"idx\"]) ? 0 : 1",
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
          {"field": "month", "type": "temporal"},
          {"field": "idx", "type": "quantitative"}
        ],
        "x": {"field": "month", "type": "temporal", "axis": {"title": "年月"}},
        "y": {
          "field": "idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "指数（2020年=100）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

米類の指数が2025年11月を最高に下がり続けている2026年9月も、575品目のうち75.5%が前年同月より値上がりしていて、値下がりした品目は19.3%です。

## 販売価格の改定を担当する人が読むとき

- 消費者向けの商品やサービスの値上げを検討するときは、近い品目の指数を前年同月と比較します。2026年9月は、575品目のうち75.5%が値上がり、19.3%が値下がり、5.2%が横ばいでした。自社の商品に近い品目が値下がりした19.3%に入っていれば、消費者はその品目で前年より安い値段を目にしています
- 値上がりした品目の割合が7割を超える状態は、消費税の引き上げのあとは12か月で終わりましたが、2022年6月からは52か月続きました。ただし2026年5月は、1品目少なければ7割を割る402品目まで下がっています。毎月の品目別の指数から、記事の SQL と同じ方法で割合を集計し直します。7割を下回る月が続き、6割も割るようになれば、値上がりが広い品目に及ぶ状態は終わりつつあると考えられます

## データの出典

本記事は総務省統計局の[消費者物価指数（CPI）](https://www.stat.go.jp/data/cpi/)の全国の月次の指数（2020年=100）を 2026-11-02 時点で集計しています。収録されているのは2026年9月分までです。

Queriaは e-Stat などの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[消費者物価指数テーブル](/datasets/queria/e_stat/cpi/price_index)から、自社の商品やサービスに近い品目の指数を月ごとに確認できます。

```sql id=monthly_share
-- 品目（cat01 が 1000 以上）ごとに前年同月の指数と比べ、値上がりした品目と値下がりした品目を数える
WITH m AS (
  SELECT cat01, year, CAST(regexp_extract(time_name, '年([0-9]+)月', 1) AS INTEGER) AS mon, TRY_CAST(value AS DOUBLE) AS v
  FROM e_stat.cpi.price_index
  WHERE tab_name = '指数' AND area_name = '全国' AND time_name LIKE '%月' AND cat01 >= '1000'
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2026
)
SELECT printf('%04d-%02d', a.year, a.mon) AS month, a.year, a.mon,
  COUNT(*) AS items,
  COUNT(*) FILTER (WHERE a.v > b.v) AS up_items,
  COUNT(*) FILTER (WHERE a.v < b.v) AS down_items,
  ROUND(100.0 * COUNT(*) FILTER (WHERE a.v > b.v) / COUNT(*), 1) AS up_pct,
  ROUND(100.0 * COUNT(*) FILTER (WHERE a.v < b.v) / COUNT(*), 1) AS down_pct
FROM m a
JOIN m b ON a.cat01 = b.cat01 AND b.year = a.year - 1 AND b.mon = a.mon
GROUP BY a.year, a.mon
ORDER BY a.year, a.mon
```

```sql id=total_yoy
-- 総合指数（0001）の前年同月比。品目と同じく接続した指数どうしで比べる（プロットはしない）
WITH t AS (
  SELECT year, CAST(regexp_extract(time_name, '年([0-9]+)月', 1) AS INTEGER) AS mon, TRY_CAST(value AS DOUBLE) AS v
  FROM e_stat.cpi.price_index
  WHERE tab_name = '指数' AND area_name = '全国' AND time_name LIKE '%月' AND cat01 = '0001'
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2026
)
SELECT a.year, a.mon, 100 * (a.v / b.v - 1) AS yoy
FROM t a
JOIN t b ON b.year = a.year - 1 AND b.mon = a.mon
ORDER BY a.year, a.mon
```

```sql id=streaks
-- 値上がりした品目の割合が基準（6割・7割・8割）以上の月が12か月以上続いた期間（丸める前の割合で判定）
WITH s AS (
  SELECT year * 12 + mon - 1 AS k, year, mon, 100.0 * up_items / items AS up, up_pct FROM monthly_share
),
th AS (SELECT * FROM (VALUES (60), (70), (80)) AS v(threshold)),
f AS (
  SELECT th.threshold, s.k, s.year, s.mon, s.up_pct, s.k - ROW_NUMBER() OVER (PARTITION BY th.threshold ORDER BY s.k) AS g
  FROM s, th
  WHERE s.up >= th.threshold
),
runs AS (
  SELECT threshold, g, MIN(k) AS k0, MAX(k) AS k1, COUNT(*) AS months, MAX(up_pct) AS up_pct_max FROM f GROUP BY threshold, g HAVING COUNT(*) >= 12
)
SELECT r.threshold,
  printf('%d年%d月', r.k0 // 12, r.k0 % 12 + 1) AS start_month,
  printf('%d年%d月', r.k1 // 12, r.k1 % 12 + 1) AS end_month,
  r.months,
  r.up_pct_max,
  ROUND(AVG(t.yoy), 1) AS cpi_yoy_avg,
  ROUND(MAX(t.yoy), 1) AS cpi_yoy_max,
  r.k0 AS start_key
FROM runs r
JOIN total_yoy t ON t.year * 12 + t.mon - 1 BETWEEN r.k0 AND r.k1
GROUP BY r.threshold, r.k0, r.k1, r.months, r.up_pct_max
ORDER BY r.threshold, r.k0
```

```sql id=threshold_sensitivity
-- 基準を60〜75%で1%ずつ動かし、2023年9月を含む連続期間・消費税が引き上げられた月から始まった期間・2021年までに終わった期間の長さを比べる（丸める前の割合で判定）
WITH s AS (
  SELECT year * 12 + mon - 1 AS k, 100.0 * up_items / items AS up FROM monthly_share
),
th AS (SELECT range AS threshold FROM range(60, 76)),
f AS (
  SELECT th.threshold, s.k, s.k - ROW_NUMBER() OVER (PARTITION BY th.threshold ORDER BY s.k) AS g
  FROM s, th
  WHERE s.up >= th.threshold
),
runs AS (
  SELECT threshold, MIN(k) AS k0, MAX(k) AS k1, COUNT(*) AS months FROM f GROUP BY threshold, g
)
SELECT threshold,
  printf('%d年%d月', MAX(k0) FILTER (WHERE 2023 * 12 + 8 BETWEEN k0 AND k1) // 12, MAX(k0) FILTER (WHERE 2023 * 12 + 8 BETWEEN k0 AND k1) % 12 + 1) AS cur_start,
  printf('%d年%d月', MAX(k1) FILTER (WHERE 2023 * 12 + 8 BETWEEN k0 AND k1) // 12, MAX(k1) FILTER (WHERE 2023 * 12 + 8 BETWEEN k0 AND k1) % 12 + 1) AS cur_end,
  MAX(months) FILTER (WHERE 2023 * 12 + 8 BETWEEN k0 AND k1) AS cur_months,
  MAX(months) FILTER (WHERE k0 IN (1997 * 12 + 3, 2014 * 12 + 3, 2019 * 12 + 9)) AS tax_max,
  MAX(months) FILTER (WHERE k1 < 2022 * 12) AS prior_max,
  printf('%d年%d月', ARG_MAX(k0, months) FILTER (WHERE k1 < 2022 * 12) // 12, ARG_MAX(k0, months) FILTER (WHERE k1 < 2022 * 12) % 12 + 1) AS prior_start
FROM runs
GROUP BY threshold
ORDER BY threshold
```

```sql id=recent_share
SELECT month, up_pct, down_pct FROM monthly_share WHERE year >= 2019 ORDER BY year, mon
```

```sql id=falling_items
-- 2026年9月に前年同月より指数が下がった品目のうち、下がり幅の大きい15品目
WITH m AS (
  SELECT cat01, SUBSTR(item_name, 6) AS item, year, TRY_CAST(value AS DOUBLE) AS v
  FROM e_stat.cpi.price_index
  WHERE tab_name = '指数' AND area_name = '全国' AND time_name IN ('2025年9月', '2026年9月') AND cat01 >= '1000'
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL
)
SELECT a.item, b.v AS idx_2025_09, a.v AS idx_2026_09, ROUND(100 * (a.v / b.v - 1), 1) AS change_pct
FROM m a
JOIN m b ON a.cat01 = b.cat01 AND a.year = 2026 AND b.year = 2025
WHERE a.v < b.v
ORDER BY change_pct, a.cat01
LIMIT 15
```

```sql id=rice_monthly
SELECT printf('%04d-%02d', year, CAST(regexp_extract(time_name, '年([0-9]+)月', 1) AS INTEGER)) AS month, TRY_CAST(value AS DOUBLE) AS idx
FROM e_stat.cpi.price_index
WHERE tab_name = '指数' AND area_name = '全国' AND cat01 = '0004' AND time_name LIKE '%月'
  AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2020 AND 2026
ORDER BY month
```
