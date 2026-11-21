---
title: 首都圏と京阪神の外で、私立中学に入る子の割合は25年で1.5倍になった
description: 首都圏と京阪神の8都府県を除く39道府県では、2000年から2025年に中学1年生が29.7%減った一方、私立中学校の1年生は2万2千〜2万6千人台で推移し、割合は2.72%から4.07%になりました。
publishedAt: 2026-10-06
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 教育
  - 中学校
  - 学習塾
  - 地域比較
datasets:
  - queria/e_stat
sources:
  - title: 学校基本調査
    url: https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/1267995.htm
    publisher: 文部科学省
  - title: 賃金構造基本統計調査
    url: https://www.mhlw.go.jp/toukei/list/chinginkouzou.html
    publisher: 厚生労働省
agentHint: 長野県・群馬県・宮崎県について、私立中学校の1年生の数と中学1年生全体の数を2000〜2025年で毎年出して。前の年の小学6年生の数と比べて、私立中学に入った割合はどう動いた？
socialAnnounce: |-
  首都圏と京阪神を除く39道府県では、25年で中学1年生が3割減りました。
  私立中学の1年生の割合は2.72%から4.07%に上がっています。

  学習塾の教室計画に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

東京都・神奈川県・埼玉県・千葉県と京都府・大阪府・兵庫県・奈良県の8都府県を除く39道府県では、2000年から2025年に中学1年生が833,781人から586,343人へ29.7%減りました。同じ25年で、私立中学校の1年生は22,713人から26,378人の間で推移し、1年生に占める私立の割合は2.72%から4.07%へ1.5倍になっています。

学習塾が中学受験のコースを置く教室を決めるときは、首都圏と京阪神が中心になります。それ以外の地域では子どもの数が減り続けているので、私立中学に進む子も減っていると考えがちですが、学校基本調査の学年別の生徒数ではそうなっていません。

## 全国では、中学1年生が23.2%減り、私立中学の1年生は8.6%増えた

使うのは文部科学省の[学校基本調査](https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/1267995.htm)の、都道府県別・設置者別・学年別の在学者数です。毎年5月1日現在の人数で、設置者は国立・公立・私立の3つに分かれます。ここでは中学校の1年生を、設置者の計（国公私立の合計）と私立で比較します。中等教育学校の前期課程と義務教育学校の7〜9年生はこの数に入りません。公立の中高一貫校のうち中学校として設置されたものは公立に入るので、ここでいう私立中学の1年生は「中学受験をした子」全体ではなく、私立の中学校に入った子の数です。

全国の値を2000年を100とした指数で並べます。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年（5月1日現在）", "format": "d"}
        },
        "y": {
          "field": "total_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2000年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "中学1年生（国公私立の計）",
          "type": "nominal",
          "scale": {"domain": ["中学1年生（国公私立の計）", "私立中学校の1年生"], "range": ["#94a3b8", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"private_index\"]) ? 0 : 1",
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
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "private_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年（5月1日現在）", "format": "d"}
        },
        "y": {
          "field": "private_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2000年を100とした指数", "grid": true}
        },
        "color": {
          "datum": "私立中学校の1年生",
          "type": "nominal",
          "scale": {"domain": ["中学1年生（国公私立の計）", "私立中学校の1年生"], "range": ["#94a3b8", "#3b82f6"]},
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

全国の中学1年生は2000年の1,325,930人から2025年の1,018,443人へ23.2%減りました。私立中学校の1年生は77,620人から84,267人へ8.6%増え、1年生に占める割合は5.85%から8.27%になっています。私立の1年生は2007年の88,642人がこの期間の最多で、その後2017年の79,648人まで減ってから、ふたたび増えています。

```sql
SELECT year AS 年, total AS "中学1年生（人）", private AS "私立中学校の1年生（人）", share AS "私立の割合（%）" FROM national_trend WHERE year IN (2000, 2007, 2017, 2025) ORDER BY year
```

## 首都圏と京阪神の外でも、私立の割合は1.5倍になった

学校基本調査は生徒を学校の所在地で集計します。県境をまたいで私立中学に通う子は通学先の県に入るので、県ごとの値は「その県に住む子のうち私立に通う割合」になりません。そこで、通学で行き来の多い東京都・神奈川県・埼玉県・千葉県を首都圏の4都県、京都府・大阪府・兵庫県・奈良県を京阪神の4府県としてまとめ、残りの39道府県と分けて比較します。

```chart
{
  "layer": [
    {
      "data": {"name": "bloc_trend"},
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
        "invalid": "break-paths-show-domains"
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
          "axis": {"title": "年（5月1日現在）", "format": "d"}
        },
        "y": {
          "field": "metro",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "中学1年生に占める私立の割合（%）", "grid": true}
        },
        "color": {
          "datum": "首都圏の4都県",
          "type": "nominal",
          "scale": {
            "domain": ["首都圏の4都県", "京阪神の4府県", "その他の39道府県"],
            "range": ["#f97316", "#7c3aed", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bloc_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kinki\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "kinki", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年（5月1日現在）", "format": "d"}
        },
        "y": {
          "field": "kinki",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "中学1年生に占める私立の割合（%）", "grid": true}
        },
        "color": {
          "datum": "京阪神の4府県",
          "type": "nominal",
          "scale": {
            "domain": ["首都圏の4都県", "京阪神の4府県", "その他の39道府県"],
            "range": ["#f97316", "#7c3aed", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bloc_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"other\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年（5月1日現在）", "format": "d"}
        },
        "y": {
          "field": "other",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "中学1年生に占める私立の割合（%）", "grid": true}
        },
        "color": {
          "datum": "その他の39道府県",
          "type": "nominal",
          "scale": {
            "domain": ["首都圏の4都県", "京阪神の4府県", "その他の39道府県"],
            "range": ["#f97316", "#7c3aed", "#3b82f6"]
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

3つの区分とも、私立の割合は2000年より2025年のほうが高くなっています。首都圏の4都県は12.58%から15.46%、京阪神の4府県は8.77%から11.08%、その他の39道府県は2.72%から4.07%です。その他の39道府県の上がり方は2018年の3.97%までがほとんどで、2018年以降は3.97%から4.09%の間で横ばいです。

```sql
SELECT * FROM bloc_summary
```

その他の39道府県の私立の1年生は、2007年の26,378人がこの期間の最多です。2025年の23,853人は2000年より5.0%多く、2007年より9.6%少ないので、人数が増えたか減ったかはどの年と比較するかで変わります。2007年と比較しても、2007年から2025年に39道府県の中学1年生は744,422人から586,343人へ21.2%減り、私立の1年生の減り方（9.6%）より大きくなっています。直近の2年は逆で、2023年から2025年に私立の1年生は24,935人から23,853人へ4.3%減り、中学1年生全体の609,773人から586,343人への3.8%減を上回りました。

```sql
SELECT year AS 年, other_total AS "39道府県の中学1年生（人）", other_private AS "39道府県の私立の1年生（人）", other AS "私立の割合（%）" FROM bloc_trend WHERE year IN (2000, 2007, 2018, 2023, 2025) ORDER BY year
```

## 39道府県のうち24で、2000年より私立の1年生が多い

その他の39道府県を1つずつ見ると、2000年より2025年のほうが私立中学の1年生が多いのは24道府県、少ないのは15県です。青が増えた道府県、灰色が減った県です。

```chart
{
  "height": 830,
  "layer": [
    {
      "data": {"name": "other_change"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "私立中学校の1年生の増減（人、2025年−2000年）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    }
  ]
}
```

増えた人数が多いのは愛知県（+380人）、宮崎県（+320人）、静岡県（+302人）、群馬県（+261人）、長野県（+249人）です。倍率で見ると、石川県は56人から243人へ4.3倍、長野県は106人から355人へ3.3倍、島根県は38人から99人へ2.6倍、群馬県は213人から474人へ2.2倍になりました。青森県は2000年に私立中学の1年生がいませんでしたが、2025年は193人です。減ったのは三重県（−466人）、高知県（−299人）、広島県（−255人）、福岡県（−194人）などで、山形県と秋田県は2025年の私立中学の1年生が0人です。

```sql
SELECT * FROM pref_change_table
```

県単位の人数は年ごとになだらかに動くとは限りません。滋賀県は2006年の326人から2007年に527人へ、石川県は2021年の146人から2022年に271人へ、1年で大きく増えました。2007年は全国の中学1年生も前年の1,187,620人から1,226,760人へ3.3%増えた年ですが、滋賀県の増え方（62%）はそれを大きく上回ります。私立中学が少ない県では、1校の新設や定員の変更が県の人数の段差として出ると考えられます。

```sql
SELECT * FROM yearly_jumps
```

## 年収の順位が40位台でも、私立の割合が上位に入る県がある

2025年の私立中学の1年生の割合を、同じ都道府県の働く人の年収と並べます。年収は厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)の一般労働者（短時間労働者以外の常用労働者）の値で、6月分のきまって支給する現金給与額を12倍し、前年1年間の賞与その他特別給与額を足して推計しました。この年収は事業所の所在地で集計した働く人の平均で、世帯の収入ではありません。東京都で働いて神奈川県・埼玉県・千葉県に住む人の給料は東京都の側に入ります。私立の割合も学校の所在地で集計した値なので、県境をまたぐ通勤・通学の多い都府県ほど、ここでの比較は実態からずれます。

```chart
{
  "layer": [
    {
      "data": {"name": "wage_scatter"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "annual_wage", "type": "quantitative"},
          {"field": "share", "type": "quantitative"}
        ],
        "x": {
          "field": "annual_wage",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "一般労働者の推計年収（万円、2025年調査）", "grid": true}
        },
        "y": {
          "field": "share",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "中学1年生に占める私立の割合（%、2025年）", "grid": true}
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"name": "wage_scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "annual_wage",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "一般労働者の推計年収（万円、2025年調査）", "grid": true}
        },
        "y": {
          "field": "share",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "中学1年生に占める私立の割合（%、2025年）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ]
}
```

47都道府県の相関係数は0.59で、全体としては年収の高い都府県ほど私立の割合が高い傾向があります。東京都を除くと0.37、首都圏と京阪神の8都府県を除いた39道府県だけでは0.08です。首都圏と京阪神の外では、年収の水準と私立の割合にはほとんど関係がありません。

```sql
SELECT * FROM wage_corr
```

私立の割合が最も高いのは東京都の27.32%で、推計年収も678万円で1位です。2位の高知県は18.67%ですが、推計年収は431万円で47都道府県の40位です。11位の宮崎県（6.89%）は推計年収が45位でした。逆に、推計年収が3位の愛知県は私立の割合が5.05%で、17位です。

```sql
SELECT * FROM pref_table
```

## 教室計画での使い方

- 担当エリアの県の私立中学の1年生の数を2000年から毎年並べると、子どもの数とは別の動きをしているかが分かります。その他の39道府県の私立の割合は2018年まで上がり、その後は4%前後で横ばいなので、これからの教室計画では直近の数年の人数を見ます
- 生徒は学校の所在地で集計されているので、県境をまたいで通学する地域では、近隣の都府県と合わせて見ます。首都圏や京阪神では、県ごとの割合よりもまとめた区分の人数のほうが市場の大きさに近くなります
- 人数が1年で大きく増えた年は、私立中学の新設や定員の変更があった年である可能性があります。その年の学校の動きと照らし合わせると、需要の変化と供給の変化を区別できます
- 高知県や宮崎県のように、年収の順位が40位台でも私立の割合が上位15位に入る県があります。候補地を年収で絞る前に、その県の私立中学の1年生の数を確認します

## データの出典

本記事は文部科学省の[学校基本調査](https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/1267995.htm)の都道府県別・設置者別・学年別の中学校生徒数（2000〜2025年、各年5月1日現在）と、厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)の都道府県別の一般労働者の賃金（2025年調査）を、2026年10月6日時点で集計しています。

Queriaは、学校基本調査や賃金構造基本統計調査などの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[学年別の児童生徒数テーブル](/datasets/queria/e_stat/school/enrollment_by_grade)と[都道府県別の賃金テーブル](/datasets/queria/e_stat/wage_structure/prefecture_wage)から、担当エリアの私立中学の1年生の推移を2000年から確認できます。

```sql id=national_trend
-- 全国の中学1年生（国公私立の計）と私立中学校の1年生。学年別の行は男女別にしか無いので、男と女を足す
WITH t AS (
  SELECT year,
    SUM(students) FILTER (WHERE founder_code = '0') AS total,
    SUM(students) FILTER (WHERE founder_code = '3') AS private
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area = '00000' AND year BETWEEN 2000 AND 2025
  GROUP BY year
)
SELECT year, total, private,
  ROUND(100.0 * private / total, 2) AS share,
  ROUND(100.0 * total / FIRST(total) OVER (ORDER BY year), 1) AS total_index,
  ROUND(100.0 * private / FIRST(private) OVER (ORDER BY year), 1) AS private_index
FROM t
ORDER BY year
```

```sql id=bloc_trend
-- 首都圏の4都県・京阪神の4府県・その他の39道府県ごとの、中学1年生に占める私立の割合
WITH t AS (
  SELECT year,
    CASE WHEN area_name IN ('東京都', '神奈川県', '埼玉県', '千葉県') THEN 'metro'
         WHEN area_name IN ('京都府', '大阪府', '兵庫県', '奈良県') THEN 'kinki'
         ELSE 'other' END AS bloc,
    SUM(students) FILTER (WHERE founder_code = '0') AS total,
    SUM(students) FILTER (WHERE founder_code = '3') AS private
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year BETWEEN 2000 AND 2025
  GROUP BY year, bloc
)
SELECT year,
  ROUND(100.0 * SUM(private) FILTER (WHERE bloc = 'metro') / SUM(total) FILTER (WHERE bloc = 'metro'), 2) AS metro,
  ROUND(100.0 * SUM(private) FILTER (WHERE bloc = 'kinki') / SUM(total) FILTER (WHERE bloc = 'kinki'), 2) AS kinki,
  ROUND(100.0 * SUM(private) FILTER (WHERE bloc = 'other') / SUM(total) FILTER (WHERE bloc = 'other'), 2) AS other,
  SUM(total) FILTER (WHERE bloc = 'other') AS other_total,
  SUM(private) FILTER (WHERE bloc = 'other') AS other_private
FROM t
GROUP BY year
ORDER BY year
```

```sql id=bloc_summary
WITH t AS (
  SELECT year,
    CASE WHEN area_name IN ('東京都', '神奈川県', '埼玉県', '千葉県') THEN '首都圏の4都県'
         WHEN area_name IN ('京都府', '大阪府', '兵庫県', '奈良県') THEN '京阪神の4府県'
         ELSE 'その他の39道府県' END AS bloc,
    SUM(students) FILTER (WHERE founder_code = '0') AS total,
    SUM(students) FILTER (WHERE founder_code = '3') AS private
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year IN (2000, 2025)
  GROUP BY year, bloc
), w AS (
  SELECT bloc,
    MAX(total) FILTER (WHERE year = 2000) AS t0, MAX(total) FILTER (WHERE year = 2025) AS t1,
    MAX(private) FILTER (WHERE year = 2000) AS p0, MAX(private) FILTER (WHERE year = 2025) AS p1
  FROM t
  GROUP BY bloc
)
SELECT bloc AS 区分,
  t0 AS "中学1年生 2000年（人）", t1 AS "中学1年生 2025年（人）",
  ROUND(100.0 * (t1 - t0) / t0, 1) AS "中学1年生の増減（%）",
  p0 AS "私立 2000年（人）", p1 AS "私立 2025年（人）",
  ROUND(100.0 * (p1 - p0) / p0, 1) AS "私立の増減（%）",
  ROUND(100.0 * p0 / t0, 2) AS "私立の割合 2000年（%）",
  ROUND(100.0 * p1 / t1, 2) AS "私立の割合 2025年（%）"
FROM w
ORDER BY p1 DESC
```

```sql id=other_change
-- その他の39道府県の私立中学校の1年生の増減（2025年−2000年）。増えた道府県は青、減った県は灰色
WITH t AS (
  SELECT area_name,
    SUM(students) FILTER (WHERE founder_code = '3' AND year = 2000) AS p0,
    SUM(students) FILTER (WHERE founder_code = '3' AND year = 2025) AS p1
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year IN (2000, 2025)
    AND area_name NOT IN ('東京都', '神奈川県', '埼玉県', '千葉県', '京都府', '大阪府', '兵庫県', '奈良県')
  GROUP BY area_name
)
SELECT area_name, p1 - p0 AS diff,
  CASE WHEN p1 > p0 THEN '#3b82f6' ELSE '#94a3b8' END AS color
FROM t
ORDER BY p1 - p0 DESC, area_name
```

```sql id=pref_change_table
WITH t AS (
  SELECT area_name,
    SUM(students) FILTER (WHERE founder_code = '0' AND year = 2000) AS t0,
    SUM(students) FILTER (WHERE founder_code = '0' AND year = 2025) AS t1,
    SUM(students) FILTER (WHERE founder_code = '3' AND year = 2000) AS p0,
    SUM(students) FILTER (WHERE founder_code = '3' AND year = 2025) AS p1
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year IN (2000, 2025)
    AND area_name NOT IN ('東京都', '神奈川県', '埼玉県', '千葉県', '京都府', '大阪府', '兵庫県', '奈良県')
  GROUP BY area_name
)
SELECT area_name AS 道府県,
  ROUND(100.0 * (t1 - t0) / t0, 1) AS "中学1年生の増減（%）",
  p0 AS "私立 2000年（人）", p1 AS "私立 2025年（人）", p1 - p0 AS "私立の増減（人）",
  CASE WHEN p0 > 0 THEN ROUND(1.0 * p1 / p0, 2) END AS "私立の倍率"
FROM t
ORDER BY p1 - p0 DESC, area_name
```

```sql id=yearly_jumps
-- その他の39道府県で、私立中学校の1年生が前年から最も増えた年（増えた人数の上位10道府県）
WITH t AS (
  SELECT year, area_name, SUM(students) FILTER (WHERE founder_code = '3') AS private
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year BETWEEN 2000 AND 2025
    AND area_name NOT IN ('東京都', '神奈川県', '埼玉県', '千葉県', '京都府', '大阪府', '兵庫県', '奈良県')
  GROUP BY year, area_name
), d AS (
  SELECT area_name, year, private,
    LAG(private) OVER (PARTITION BY area_name ORDER BY year) AS prev
  FROM t
)
SELECT area_name AS 道府県, year AS 年, prev AS "前年（人）", private AS "その年（人）", private - prev AS "増えた人数"
FROM d
WHERE prev IS NOT NULL
QUALIFY ROW_NUMBER() OVER (PARTITION BY area_name ORDER BY private - prev DESC, year) = 1
ORDER BY private - prev DESC, area_name
LIMIT 10
```

```sql id=wage_scatter
-- 2025年の私立中学校の1年生の割合と、一般労働者の推計年収（きまって支給する現金給与額×12＋年間賞与その他特別給与額、万円）
WITH s AS (
  SELECT area_name,
    100.0 * SUM(students) FILTER (WHERE founder_code = '3') / SUM(students) FILTER (WHERE founder_code = '0') AS share
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year = 2025
  GROUP BY area_name
), w AS (
  SELECT area_name, (contractual_earnings * 12 + annual_special_earnings) / 10 AS annual_wage
  FROM e_stat.wage_structure.prefecture_wage
  WHERE year = 2025 AND sex_code = '0' AND area <> '00000'
)
SELECT s.area_name, ROUND(s.share, 2) AS share, ROUND(w.annual_wage, 0) AS annual_wage,
  CASE WHEN s.area_name IN ('東京都', '高知県', '京都府', '奈良県', '神奈川県', '大阪府', '宮崎県', '愛知県') THEN s.area_name ELSE '' END AS label,
  CASE WHEN s.area_name IN ('高知県', '宮崎県') THEN '#ef4444' ELSE '#3b82f6' END AS color
FROM s JOIN w USING (area_name)
ORDER BY s.area_name
```

```sql id=pref_table
WITH t AS (
  SELECT year, area_name,
    SUM(students) FILTER (WHERE founder_code = '0') AS total,
    SUM(students) FILTER (WHERE founder_code = '3') AS private
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year IN (2000, 2025)
  GROUP BY year, area_name
), s AS (
  SELECT area_name,
    MAX(100.0 * private / total) FILTER (WHERE year = 2000) AS s0,
    MAX(100.0 * private / total) FILTER (WHERE year = 2025) AS s1,
    MAX(private) FILTER (WHERE year = 2025) AS p1
  FROM t
  GROUP BY area_name
), w AS (
  SELECT area_name, (contractual_earnings * 12 + annual_special_earnings) / 10 AS annual_wage
  FROM e_stat.wage_structure.prefecture_wage
  WHERE year = 2025 AND sex_code = '0' AND area <> '00000'
)
SELECT s.area_name AS 都道府県,
  ROUND(s.s0, 2) AS "私立の割合 2000年（%）",
  ROUND(s.s1, 2) AS "私立の割合 2025年（%）",
  RANK() OVER (ORDER BY s.s1 DESC) AS "私立の割合の順位",
  s.p1 AS "私立 2025年（人）",
  ROUND(w.annual_wage, 0) AS "推計年収（万円）",
  RANK() OVER (ORDER BY w.annual_wage DESC) AS "推計年収の順位"
FROM s JOIN w USING (area_name)
ORDER BY s.s1 DESC, s.area_name
```

```sql id=wage_corr
-- 2025年の私立の割合と推計年収の相関係数（47都道府県・東京都を除く46道府県・首都圏と京阪神の8都府県を除く39道府県）
WITH s AS (
  SELECT area_name,
    100.0 * SUM(students) FILTER (WHERE founder_code = '3') / SUM(students) FILTER (WHERE founder_code = '0') AS share
  FROM e_stat.school.enrollment_by_grade
  WHERE school_type = 'junior_high' AND grade = 1 AND sex_code IN ('1', '2')
    AND area <> '00000' AND year = 2025
  GROUP BY area_name
), w AS (
  SELECT area_name, (contractual_earnings * 12 + annual_special_earnings) / 10 AS annual_wage
  FROM e_stat.wage_structure.prefecture_wage
  WHERE year = 2025 AND sex_code = '0' AND area <> '00000'
), j AS (
  SELECT s.area_name, s.share, w.annual_wage,
    s.area_name IN ('東京都', '神奈川県', '埼玉県', '千葉県', '京都府', '大阪府', '兵庫県', '奈良県') AS big
  FROM s JOIN w USING (area_name)
)
SELECT * FROM (
  SELECT '47都道府県' AS 範囲, COUNT(*) AS 都道府県数, ROUND(CORR(share, annual_wage), 2) AS 相関係数 FROM j
  UNION ALL
  SELECT '東京都を除く', COUNT(*), ROUND(CORR(share, annual_wage), 2) FROM j WHERE area_name <> '東京都'
  UNION ALL
  SELECT '首都圏と京阪神の8都府県を除く', COUNT(*), ROUND(CORR(share, annual_wage), 2) FROM j WHERE NOT big
)
ORDER BY 都道府県数 DESC
```
