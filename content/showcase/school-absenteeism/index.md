---
title: 不登校の小中学生は32年で5.2倍の34.6万人になり、都道府県では宮城県が福井県の1.8倍
description: 小中学校の不登校児童生徒数は1991年度からの32年間で約5.2倍に増え、2023年度は34.6万人で小中学生の3.76%です。都道府県別の不登校率は宮城県の4.73%から福井県の2.69%まで1.8倍の差があり、いじめ認知件数との相関は見られませんでした。
publishedAt: 2026-02-28
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 教育
  - 不登校
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 児童生徒の問題行動・不登校等生徒指導上の諸課題に関する調査
    url: https://www.mext.go.jp/b_menu/toukei/chousa01/shidou/1267646.htm
    publisher: 文部科学省
agentHint: 沖縄県の不登校率(cat01のE250802・E350502を在籍数E2501・E3501で割った値)を2003年から2023年まで年ごとに出して、全国平均とどれだけ開いていったか比べて
---

2023年度に不登校とされた小中学生は346,482人で、1991年度の66,817人から32年間で5.2倍に増えました。同じ年度の小中学生の在籍数は9,227,193人なので、全体の3.76%、およそ27人に1人にあたります。都道府県別の不登校率は宮城県の4.73%が最も高く、福井県の2.69%の1.8倍です。

教育委員会で指導主事やスクールカウンセラーの配置を検討するときは、自分の県の不登校の人数がどの水準にあり、どのくらいの速さで増えてきたかを確認する必要があります。この記事では、e-Stat「[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)」の都道府県別教育データ（`e_pref_education`）を使い、1991年度から2023年度までの推移と都道府県間の差を集計しました。

## 不登校の小学生は10.3倍、中学生は4.0倍に増えた

このテーブルには、長期欠席（年度間30日以上）の児童生徒数が理由別に収録されています。使うのは次のカテゴリです。

| コード  | 内容                                   |
| ------- | -------------------------------------- |
| E2508   | 小学校長期欠席児童数（年度間30日以上） |
| E250801 | 小学校長期欠席児童数（病気）           |
| E250802 | 小学校長期欠席児童数（不登校）         |
| E3505   | 中学校長期欠席生徒数（年度間30日以上） |
| E350501 | 中学校長期欠席生徒数（病気）           |
| E350502 | 中学校長期欠席生徒数（不登校）         |

ここで扱う「不登校」は、長期欠席のうち病気や経済的理由を除いたもの、小学校長期欠席児童数（不登校）（`E250802`）と中学校長期欠席生徒数（不登校）（`E350502`）です。全国の推移を小学校・中学校別に並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "count_elem"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "不登校児童生徒数（人）", "grid": true}
        },
        "color": {
          "datum": "小学校",
          "type": "nominal",
          "scale": {"domain": ["小学校", "中学校"], "range": ["#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "count_middle"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "不登校児童生徒数（人）", "grid": true}
        },
        "color": {
          "datum": "中学校",
          "type": "nominal",
          "scale": {"domain": ["小学校", "中学校"], "range": ["#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

中学校の不登校は1991年度の54,172人から2023年度の216,112人へ4.0倍に、小学校は12,645人から130,370人へ10.3倍に増えました。合計では66,817人から346,482人で、32年間で5.2倍です。1997年度から1998年度にかけては、小学校が25%、中学校が20%増えています。小学校の前後の年の増加率は6.5%と0.1%で、この1年だけが大きく増えています。5.2倍にはこの1年の増加が含まれています。

小学校・中学校とも、直近で最も少なかったのは2012年度（小学校21,243人、中学校91,249人）で、そこから増加に転じています。2013年度から2016年度までの3年間は小学校で26%増、中学校で8%増でしたが、2016年度から2023年度の7年間では小学校が4.3倍、中学校が2.1倍になりました。

## 中学校の不登校率は6.80%で、1991年度の6.5倍

児童生徒数が少子化で減り続けているので、在籍数で割った不登校率でも推移を確認しました。分母には小学校児童数（`E2501`）と中学校生徒数（`E3501`）を使います。

```chart
{
  "layer": [
    {
      "data": {"name": "rate_elem"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "不登校率（%）", "grid": true}
        },
        "color": {
          "datum": "小学校",
          "type": "nominal",
          "scale": {"domain": ["小学校", "中学校"], "range": ["#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rate_middle"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "不登校率（%）", "grid": true}
        },
        "color": {
          "datum": "中学校",
          "type": "nominal",
          "scale": {"domain": ["小学校", "中学校"], "range": ["#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

中学校の不登校率は1991年度の1.04%から2023年度の6.80%へ、6.5倍になりました。35人学級なら1クラスに2人強です。小学校は0.14%から2.15%で、15.4倍になりました。

不登校率は2001年度から2012年度にかけて横ばいから微減で推移し（中学校2.81%→2.57%、小学校0.36%→0.31%）、2013年度以降に再び上昇に転じています。この間、2013年9月に[いじめ防止対策推進法](https://www.mext.go.jp/a_menu/shotou/seitoshidou/1337278.htm)が施行され、2017年2月には教育機会確保法（[義務教育の段階における普通教育に相当する教育の機会の確保等に関する法律](https://laws.e-gov.go.jp/law/428AC1000000105)）が全面施行されました。文部科学省は2019年10月の[通知](https://www.mext.go.jp/a_menu/shotou/seitoshidou/1422155.htm)で、不登校を「問題行動」と判断してはならないと明示しています。統計上の増加が始まった時期は、学校が長期欠席をどう記録するかの前提が変わった時期と重なっています。

## 2023年度の不登校率は宮城県4.73%、福井県2.69%で、1.8倍の差がある

2023年度の不登校率の上位・下位それぞれ10県を並べました。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "pref_rate_high"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "不登校率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位（不登校率が高い）",
          "type": "nominal",
          "scale": {"domain": ["上位（不登校率が高い）", "下位（不登校率が低い）"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_rate_low"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "不登校率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位（不登校率が低い）",
          "type": "nominal",
          "scale": {"domain": ["上位（不登校率が高い）", "下位（不登校率が低い）"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは宮城県（4.73%）、最も低いのは福井県（2.69%）で、1.8倍の差があります。上位10県は宮城県・島根県・長野県・沖縄県・福岡県・静岡県・北海道・栃木県・熊本県・広島県で、東京都・大阪府・神奈川県・愛知県は含まれません。下位10県には千葉県（3.20%）と埼玉県（3.16%）が入っています。不登校率の高さは、大都市圏かどうかでは説明できません。

最も低い4県（福井県2.69%、岡山県2.89%、岩手県3.00%、香川県3.04%）は3%前後で、最も高い宮城県との差は1.5ポイント以上あります。

## 2003年度からの増加幅は沖縄県が+3.65ポイントで最も大きい

2003年度と2023年度の不登校率を比較し、増加幅が大きかった都道府県を並べました。

```chart
{
  "height": 330,
  "layer": [
    {
      "data": {"name": "rate_change"},
      "transform": [
        {"fold": ["rate_2003", "rate_change"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"rate_2003\": \"2003年度\", \"rate_change\": \"2023年度増加分\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"rate_2003\",\"rate_change\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "不登校率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["2003年度", "2023年度増加分"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

変化幅が最も大きいのは沖縄県（1.00% → 4.65%、+3.65ポイント）で、20年間で不登校率が4.65倍になりました。宮城県（+3.58ポイント）、長野県（+3.47ポイント）、北海道（+3.36ポイント）が続きます。

この15県はいずれも+2.8ポイント以上の増加で、倍率は島根県の3.06倍から北海道の4.91倍までです。15県のうち13県は2003年度の不登校率が1.2%以下でした。当時から高かった島根県（1.54%）は、増加幅では15県中7位ですが、倍率では最小の3.06倍です。同じだけポイントが増えても、出発点が低い県ほど倍率は大きくなります。

## いじめ認知件数と不登校率の相関係数は-0.001

不登校の要因として、いじめが議論されることがあります。同じテーブルには都道府県別いじめ認知件数（`E9502`、2013年度以降）が収録されているので、2023年度の値を小中学生100人あたりに直し、不登校率との関係を散布図にしました。認知件数は高等学校と特別支援学校を含む全学校種の合計で、分母は小中学生だけなので、この値は県ごとの比較に使うもので、小中学校のいじめ発生率ではありません。

```chart
{
  "layer": [
    {
      "data": {"name": "ijime_vs_futoko"},
      "mark": {"type": "point", "color": "#8b5cf6", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "ijime_rate", "type": "quantitative"},
          {"field": "futoko_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "ijime_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "小中学生100人あたりいじめ認知件数（件）", "grid": true}
        },
        "y": {
          "field": "futoko_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "不登校率（%）", "grid": true}
        }
      }
    }
  ]
}
```

47都道府県での相関係数は-0.001で、両者の間に関係は見られません。認知件数が最も多い山形県（100人あたり16.5件）の不登校率は3.2%で下位に近く、最も少ない長崎県（2.4件）は3.6%と中位です。不登校率が最も高い宮城県（4.7%）の認知件数は8.9件で、47都道府県中16番目です。

いじめの認知件数は、学校がどこまでをいじめとして把握し報告するかによって大きく変わります。都道府県別のこの2つの指標からは、いじめの多さで不登校率の県間の差を説明することはできません。

## まとめ

- 不登校児童生徒数は1991年度の66,817人から2023年度の346,482人へ、32年間で5.2倍に増えた
- 少子化で在籍数が減るなかで不登校率は上昇し、2023年度は小中学生の3.76%、およそ27人に1人にあたる
- 都道府県間には最大1.8倍（宮城県4.73%、福井県2.69%）の差がある。2003年度からの増加幅が大きい15県でも、増加の倍率は3.06倍から4.91倍まで差がある
- 都道府県別のいじめ認知件数と不登校率の相関係数は-0.001で、県間の差を説明しない

増加が始まった2013年度以降は、いじめ防止対策推進法の施行（2013年）、教育機会確保法の全面施行（2017年）、不登校を問題行動と判断しないとする文部科学省通知（2019年）と、制度の変化が続いた時期にあたります。学校以外の学びの場が制度上認められたことで、報告される人数と実態の関係も変わってきました。増加の理由を考えるときは、子どもの状況の変化と、記録の仕方の変化の両方を考慮する必要があります。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別教育データ（`e_pref_education`）を 2026-07-30 時点で集計しています。元データは文部科学省の[児童生徒の問題行動・不登校等生徒指導上の諸課題に関する調査](https://www.mext.go.jp/b_menu/toukei/chousa01/shidou/1267646.htm)で、数値はすべて年度の値です。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の教育データのテーブル](/datasets/queria/e_stat/ssds/e_pref_education)から、自分の都道府県の不登校率を年度ごとに出し、全国や他の都道府県と比較できます。

```sql id=overview_2023
WITH t AS ( SELECT SUM(CASE WHEN cat01 IN ('E250802', 'E350502') THEN value ELSE 0 END) AS futoko, SUM(CASE WHEN cat01 IN ('E2501', 'E3501') THEN value ELSE 0 END) AS students FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E250802', 'E350502', 'E2501', 'E3501') AND value IS NOT NULL AND year = 2023 AND area_name != '全国' ) SELECT futoko AS futoko_total, students AS student_total, ROUND(futoko / students * 100, 2) AS futoko_rate, ROUND(students / futoko, 1) AS one_in FROM t
```

```sql id=count_elem
SELECT year, SUM(value) AS count FROM e_stat.ssds.e_pref_education WHERE cat01 = 'E250802' AND value IS NOT NULL AND year <= 2023 AND area_name != '全国' GROUP BY year ORDER BY year
```

```sql id=count_middle
SELECT year, SUM(value) AS count FROM e_stat.ssds.e_pref_education WHERE cat01 = 'E350502' AND value IS NOT NULL AND year <= 2023 AND area_name != '全国' GROUP BY year ORDER BY year
```

```sql id=rate_elem
WITH stats AS ( SELECT year, SUM(CASE WHEN cat01 = 'E250802' THEN value ELSE 0 END) AS elem_futoko, SUM(CASE WHEN cat01 = 'E2501' THEN value ELSE 0 END) AS elem_students FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E250802', 'E2501') AND value IS NOT NULL AND year <= 2023 AND area_name != '全国' GROUP BY year ) SELECT year, ROUND(elem_futoko / elem_students * 100, 2) AS rate FROM stats WHERE elem_students > 0 AND elem_futoko > 0 ORDER BY year
```

```sql id=rate_middle
WITH stats AS ( SELECT year, SUM(CASE WHEN cat01 = 'E350502' THEN value ELSE 0 END) AS middle_futoko, SUM(CASE WHEN cat01 = 'E3501' THEN value ELSE 0 END) AS middle_students FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E350502', 'E3501') AND value IS NOT NULL AND year <= 2023 AND area_name != '全国' GROUP BY year ) SELECT year, ROUND(middle_futoko / middle_students * 100, 2) AS rate FROM stats WHERE middle_students > 0 AND middle_futoko > 0 ORDER BY year
```

```sql id=pref_rate_high
WITH totals AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('E250802', 'E350502') THEN value ELSE 0 END) AS futoko, SUM(CASE WHEN cat01 IN ('E2501', 'E3501') THEN value ELSE 0 END) AS students FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E250802', 'E350502', 'E2501', 'E3501') AND value IS NOT NULL AND year = 2023 AND area_name != '全国' GROUP BY area_name ), rates AS ( SELECT area_name, ROUND(futoko / students * 100, 2) AS rate FROM totals WHERE students > 0 ), ranked AS ( SELECT *, ROW_NUMBER() OVER (ORDER BY rate DESC, area_name) AS rn FROM rates ) SELECT area_name, rate FROM ranked WHERE rn <= 10 ORDER BY rate DESC, area_name
```

```sql id=pref_rate_low
WITH totals AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('E250802', 'E350502') THEN value ELSE 0 END) AS futoko, SUM(CASE WHEN cat01 IN ('E2501', 'E3501') THEN value ELSE 0 END) AS students FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E250802', 'E350502', 'E2501', 'E3501') AND value IS NOT NULL AND year = 2023 AND area_name != '全国' GROUP BY area_name ), rates AS ( SELECT area_name, ROUND(futoko / students * 100, 2) AS rate FROM totals WHERE students > 0 ), ranked AS ( SELECT *, ROW_NUMBER() OVER (ORDER BY rate ASC, area_name) AS rn FROM rates ) SELECT area_name, rate FROM ranked WHERE rn <= 10 ORDER BY rate DESC, area_name
```

```sql id=rate_change
WITH agg AS ( SELECT area_name, year, SUM(CASE WHEN cat01 IN ('E250802', 'E350502') THEN value ELSE 0 END) AS futoko, SUM(CASE WHEN cat01 IN ('E2501', 'E3501') THEN value ELSE 0 END) AS students FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E250802', 'E350502', 'E2501', 'E3501') AND value IS NOT NULL AND year IN (2003, 2023) AND area_name != '全国' GROUP BY area_name, year ), changes AS ( SELECT area_name, MAX(CASE WHEN year = 2003 THEN ROUND(futoko / students * 100, 2) END) AS rate_2003, MAX(CASE WHEN year = 2023 THEN ROUND(futoko / students * 100, 2) END) AS rate_2023 FROM agg WHERE students > 0 GROUP BY area_name HAVING rate_2003 IS NOT NULL AND rate_2023 IS NOT NULL ), ranked AS ( SELECT *, ROUND(rate_2023 - rate_2003, 2) AS rate_change, ROUND(rate_2023 / rate_2003, 2) AS ratio, ROW_NUMBER() OVER (ORDER BY rate_2023 - rate_2003 DESC, area_name) AS rn FROM changes ) SELECT area_name, rate_2003, rate_2023, rate_change, ratio FROM ranked WHERE rn <= 15 ORDER BY rate_change DESC, area_name
```

```sql id=ijime_vs_futoko
WITH totals AS ( SELECT area_name, SUM(CASE WHEN cat01 = 'E9502' THEN value ELSE 0 END) AS ijime_total, SUM(CASE WHEN cat01 IN ('E250802', 'E350502') THEN value ELSE 0 END) AS futoko_total, SUM(CASE WHEN cat01 IN ('E2501', 'E3501') THEN value ELSE 0 END) AS student_total FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9502', 'E250802', 'E350502', 'E2501', 'E3501') AND value IS NOT NULL AND year = 2023 AND area_name != '全国' GROUP BY area_name ) SELECT area_name, ROUND(ijime_total / student_total * 100, 1) AS ijime_rate, ROUND(futoko_total / student_total * 100, 1) AS futoko_rate FROM totals WHERE student_total > 0 ORDER BY area_name
```

```sql id=ijime_corr
WITH totals AS ( SELECT area_name, SUM(CASE WHEN cat01 = 'E9502' THEN value ELSE 0 END) AS ijime_total, SUM(CASE WHEN cat01 IN ('E250802', 'E350502') THEN value ELSE 0 END) AS futoko_total, SUM(CASE WHEN cat01 IN ('E2501', 'E3501') THEN value ELSE 0 END) AS student_total FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9502', 'E250802', 'E350502', 'E2501', 'E3501') AND value IS NOT NULL AND year = 2023 AND area_name != '全国' GROUP BY area_name ), rates AS ( SELECT ROUND(ijime_total / student_total * 100, 1) AS ijime_rate, ROUND(futoko_total / student_total * 100, 1) AS futoko_rate FROM totals WHERE student_total > 0 ) SELECT COUNT(*) AS n_pref, ROUND(corr(ijime_rate, futoko_rate), 3) AS correlation FROM rates
```
