---
title: 財政力の上位10府県は、48年度中43年度で、決まって入るお金のうち決まった支出に回る割合が下位10県より高い
description: 東京都を除く46道府県を財政力指数で並べると、上位10の経常収支比率は1975〜2022年度の48年度のうち43年度で下位10を上回りました。東京都の経常収支比率は2013年度から10年度続けて47都道府県で最も低い値です。
publishedAt: 2026-04-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 地方財政
  - 財政力指数
  - 自治体職員
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（D 行政基盤）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/D
    publisher: 総務省統計局
  - title: 財政状況資料集
    url: https://www.soumu.go.jp/iken/zaisei/jyoukyou_shiryou/index.html
    publisher: 総務省
agentHint: 2022年度の経常収支比率と実質公債費比率を都道府県別に並べて、財政力指数が近い都道府県どうしで比べて
socialAnnounce: |-
  東京都を除くと、財政力指数の上位10府県は、決まって入る財源のうち決まった支出に回る割合が1975年度以降の48年度中43年度で下位10県を上回ります。

  財政の比較に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

東京都を除く46道府県を財政力指数で並べると、上位10府県の経常収支比率の平均は、1975年度から2022年度までの48年度のうち43年度で下位10県を上回りました。経常収支比率は、毎年度決まって入る財源のうち、人件費や借金の返済のような毎年度決まった支出に回る割合です。2022年度に経常収支比率が最も高かったのは大阪府の102.2%で、財政力指数は47都道府県で5位です。東京都の経常収支比率は2013年度から10年度続けて47都道府県で最も低くなっています。

財政力指数は、都道府県の財政の豊かさを比較するときによく使われる指標です。e-Stat [社会・人口統計体系の項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/D)は、財政力指数が高いほど「財源に余裕があるといえる」と説明しています。

## 2022年度の財政力指数は、東京都が島根県の約4.2倍

データは e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別の行政基盤テーブル（`d_pref_administration`）から取っています。都道府県の普通会計について、次の指標が収録されています。

```sql
SELECT * FROM coverage
```

この記事では財政力指数（`D2101`）と経常収支比率（`D2103`）を使います。財政力指数は、標準的に見込まれる税収などから算定した基準財政収入額を、標準的な行政サービスに要する基準財政需要額で割った値の、過去3年度の平均です。

```chart caption="都道府県の財政力指数（2022年度）"
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "fiscal_ranking"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "fiscal_strength", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "fiscal_strength",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "財政力指数", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#ef4444", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

2022年度に財政力指数が1を超えたのは東京都（1.064）だけで、愛知県（0.867）、神奈川県（0.845）が続きます。最も低い島根県（0.254）と東京都の差は約4.2倍です。

## 2022年度に経常収支比率が高い3府県は、いずれも財政力指数が10位以内

経常収支比率は、人件費・扶助費・公債費のように毎年度決まって出ていく経費に充てた一般財源が、地方税や普通交付税など毎年度決まって入ってくる一般財源（臨時財政対策債などを含む）に占める割合です。高いほど、新しい事業や施設の整備に回せる財源の割合が小さいことを表します。

```chart caption="財政力指数と経常収支比率（2022年度、47都道府県）"
{
  "layer": [
    {
      "data": {"name": "fs_cr_2022_others"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "fiscal_strength", "type": "quantitative"},
          {"field": "current_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_strength",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "財政力指数", "grid": true}
        },
        "y": {
          "field": "current_ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "経常収支比率（%）", "grid": true}
        },
        "color": {
          "datum": "道府県",
          "type": "nominal",
          "scale": {"domain": ["道府県", "東京都"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "fs_cr_2022_tokyo"},
      "mark": {"type": "point", "filled": true, "size": 121},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "fiscal_strength", "type": "quantitative"},
          {"field": "current_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_strength",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "財政力指数", "grid": true}
        },
        "y": {
          "field": "current_ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "経常収支比率（%）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {"domain": ["道府県", "東京都"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "fs_cr_2022_tokyo"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "fiscal_strength",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "財政力指数", "grid": true}
        },
        "y": {
          "field": "current_ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "経常収支比率（%）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

経常収支比率が最も高いのは大阪府（102.2%）で、兵庫県（98.7%）、神奈川県（98.5%）が続きます。3府県とも、財政力指数は47都道府県の中で10位以内です。低い側は東京都（79.5%）を除くと鳥取県（87.4%）、愛媛県（87.6%）、山口県（87.9%）で、財政力指数は47都道府県の中で27位以下です。東京都を除く46道府県で、財政力指数の順位と経常収支比率の順位の相関（1なら順位が完全に一致し、0なら関係がない）は0.44で、財政力指数の高い道府県のほうが経常収支比率も高い傾向があります。

```sql
SELECT * FROM corr_2022
```

## 1975〜2022年度の48年度のうち43年度で、上位10の経常収支比率が下位10を上回る

この傾向が2022年度だけのものかを、48年度分で確認しました。東京都は48年度のうち46年度で財政力指数が47都道府県で最も高く、ほかの道府県と大きく離れているので除いています。残る46道府県を年度ごとに財政力指数で並べ直し、上位10と下位10の経常収支比率の平均を比較しました。

```chart caption="財政力指数の上位10・下位10の経常収支比率の平均（東京都を除く46道府県、年度ごとに並べ直し）"
{
  "layer": [
    {
      "data": {"name": "group_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"top10\"]) ? 0 : 1",
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
          {"field": "top10", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "top10",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "経常収支比率（%）", "grid": true}
        },
        "color": {
          "datum": "財政力指数の上位10",
          "type": "nominal",
          "scale": {
            "domain": ["財政力指数の上位10", "財政力指数の下位10", "全国"],
            "range": ["#3b82f6", "#94a3b8", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "group_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"bottom10\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "bottom10", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "bottom10",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "経常収支比率（%）", "grid": true}
        },
        "color": {
          "datum": "財政力指数の下位10",
          "type": "nominal",
          "scale": {
            "domain": ["財政力指数の上位10", "財政力指数の下位10", "全国"],
            "range": ["#3b82f6", "#94a3b8", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "group_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"national\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "national", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "national",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "経常収支比率（%）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {
            "domain": ["財政力指数の上位10", "財政力指数の下位10", "全国"],
            "range": ["#3b82f6", "#94a3b8", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

上位10の平均が下位10を上回ったのは48年度のうち43年度で、下回ったのは1984・1985・1987・1988・2006年度の5年度です。差が最も大きかったのは1998年度で、上位10が100.5%、下位10が85.5%でした。2004年度以降は2006年度を除いて差が1.0〜4.1ポイントです。この差は、上位10・下位10それぞれの中での道府県のばらつき（2004年度以降の標準偏差の平均は上位10が2.3ポイント、下位10が2.6ポイント）と同じくらいの大きさです。個々の道府県の経常収支比率を、財政力指数の順位から推定できるほどの差ではありません。

上位・下位を何団体で区切るかを変えても、2022年度の上位10・下位10の道府県に固定して48年度を集計しても、上位の側が高い年度が大半です。

```sql
SELECT * FROM group_summary
```

年度ごとの順位の相関は、48年度のうち38年度で正でした。中央値は0.30で、財政力指数の順位だけで経常収支比率の順位が決まるほど強い関係ではありません。

```sql
SELECT * FROM yearly_corr
```

## 投資的経費を一般財源で割った値は、48年度すべてで下位10が高い

同じテーブルの投資的経費（`D2110`、道路や施設の整備などに使った経費）を一般財源（`D2109`）で割ると、48年度すべてで財政力指数の下位10の平均が上位10を上回ります。2022年度は上位10が18.5%、下位10が37.6%です。投資的経費には国庫支出金や地方債で賄う分も含まれるので、この割合は一般財源のうち投資に回った割合そのものではありません。

```chart caption="投資的経費÷一般財源の平均（東京都を除く46道府県、財政力指数で年度ごとに並べ直した上位10・下位10）"
{
  "layer": [
    {
      "data": {"name": "invest_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"top10\"]) ? 0 : 1",
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
          {"field": "top10", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "top10",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "投資的経費÷一般財源（%）", "grid": true}
        },
        "color": {
          "datum": "財政力指数の上位10",
          "type": "nominal",
          "scale": {"domain": ["財政力指数の上位10", "財政力指数の下位10"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "invest_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"bottom10\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "bottom10", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "bottom10",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "投資的経費÷一般財源（%）", "grid": true}
        },
        "color": {
          "datum": "財政力指数の下位10",
          "type": "nominal",
          "scale": {"domain": ["財政力指数の上位10", "財政力指数の下位10"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

## 東京都の経常収支比率は、2013年度から47都道府県で最も低い

財政力指数が48年度のうち46年度で最も高い東京都の経常収支比率は、時期によって47都道府県の中の順位が大きく変わっています。

```chart caption="東京都の経常収支比率の順位（47都道府県の中で低いほうから数えた順位。1が最も低い）"
{
  "layer": [
    {
      "data": {"name": "tokyo_rank"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"cr_rank_low\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "cr_rank_low", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "cr_rank_low",
          "type": "quantitative",
          "scale": {"domain": [48, 0], "zero": false, "nice": false},
          "axis": {"title": "低いほうからの順位", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {"domain": ["東京都"], "range": ["#ef4444"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1977〜1980年度の4年度は、東京都の経常収支比率が47都道府県で最も高い値でした。2005〜2008年度に最も低くなり、2013年度から2022年度までは10年度続けて最も低い値です。2022年度の東京都は79.5%で、2番目に低い鳥取県の87.4%を7.9ポイント下回ります。

## 都道府県の財政を比較するときの使い方

財政力指数が高い都道府県でも、決まって入る財源のうち新しい事業に回せる割合が大きいとは限りません。2022年度に経常収支比率が100%を超えたのは、財政力指数が47都道府県で5位の大阪府だけでした。

- 財政担当の職員が自分の都道府県の財政をほかと比較するときは、財政力指数と経常収支比率を並べると、収入の多さと、新しい事業に回せる財源の割合を分けて確認できます
- 財政力指数が近い都道府県どうしで経常収支比率を比較すると、同じ程度の財政力の中で決まった支出が重いところと軽いところが分かります。2022年度の財政力指数0.6前後では、兵庫県（0.612）が98.7%、栃木県（0.610）が93.3%、茨城県（0.621）が91.9%です
- 経常収支比率の内訳（人件費・扶助費・公債費などの割合）は、総務省が都道府県ごとに公表している[財政状況資料集](https://www.soumu.go.jp/iken/zaisei/jyoukyou_shiryou/index.html)に載っています

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別の行政基盤データを2026-11-04時点で集計しています。元データは総務省の地方財政状況調査で、数値はすべて普通会計の年度の値です。

Queriaは、e-Stat をはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の行政基盤テーブル](/datasets/queria/e_stat/ssds/d_pref_administration)から、自分の都道府県と財政力指数の近い都道府県の経常収支比率や、1975年度からの推移を確認できます。

```sql id=coverage
-- 都道府県財政（D21xx）の指標と収録年度
SELECT cat01 AS "コード", regexp_replace(item_name, '^D[0-9]+_', '') AS "内容", min_year AS "最初の年度", max_year AS "最後の年度"
FROM e_stat.ssds.series_coverage
WHERE table_name = 'd_pref_administration' AND cat01 LIKE 'D21%'
ORDER BY cat01
```

```sql id=fiscal_ranking
SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 3) AS fiscal_strength
FROM e_stat.ssds.d_pref_administration
WHERE cat01 = 'D2101' AND time_name = '2022年度' AND area_name != '全国'
  AND TRY_CAST(value AS DOUBLE) IS NOT NULL
ORDER BY fiscal_strength ASC, area_name
```

```sql id=fs_cr_2022
-- 2022年度の財政力指数と経常収支比率。順位は財政力指数の高い順と、経常収支比率の高い順
WITH w AS (
  SELECT area_name,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2101') AS fs,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2103') AS cr
  FROM e_stat.ssds.d_pref_administration
  WHERE cat01 IN ('D2101', 'D2103') AND time_name = '2022年度' AND area_name != '全国'
  GROUP BY 1
)
SELECT area_name, ROUND(fs, 3) AS fiscal_strength, ROUND(cr, 1) AS current_ratio,
  ROW_NUMBER() OVER (ORDER BY fs DESC, area_name) AS fs_rank,
  RANK() OVER (ORDER BY cr DESC) AS cr_rank_high
FROM w
ORDER BY fs DESC
```

```sql id=fs_cr_2022_others
SELECT * FROM fs_cr_2022 WHERE area_name != '東京都'
```

```sql id=fs_cr_2022_tokyo
SELECT * FROM fs_cr_2022 WHERE area_name = '東京都'
```

```sql id=corr_2022
-- 東京都を除く46道府県の、財政力指数の順位と経常収支比率の順位の相関（2022年度）
WITH r AS (
  SELECT *, RANK() OVER (ORDER BY fiscal_strength) AS rf, RANK() OVER (ORDER BY current_ratio) AS rc
  FROM fs_cr_2022
  WHERE area_name != '東京都'
)
SELECT COUNT(*) AS "道府県の数", ROUND(CORR(rf, rc), 2) AS "順位の相関"
FROM r
```

```sql id=pref_yearly
-- 東京都と全国を除く46道府県の、年度ごとの財政力指数・経常収支比率・一般財源・投資的経費
SELECT area_name, year,
  MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2101') AS fs,
  MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2103') AS cr,
  MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2109') AS general_revenue,
  MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2110') AS investment
FROM e_stat.ssds.d_pref_administration
WHERE cat01 IN ('D2101', 'D2103', 'D2109', 'D2110') AND area_name NOT IN ('全国', '東京都')
  AND year BETWEEN 1975 AND 2022
GROUP BY 1, 2
```

```sql id=group_trend
WITH r AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY fs DESC, area_name) AS rn
  FROM pref_yearly
),
g AS (
  SELECT year,
    AVG(cr) FILTER (WHERE rn <= 10) AS top10,
    AVG(cr) FILTER (WHERE rn > 36) AS bottom10,
    STDDEV_POP(cr) FILTER (WHERE rn <= 10) AS top10_sd,
    STDDEV_POP(cr) FILTER (WHERE rn > 36) AS bottom10_sd
  FROM r
  GROUP BY year
),
n AS (
  SELECT year, TRY_CAST(value AS DOUBLE) AS national
  FROM e_stat.ssds.d_pref_administration
  WHERE cat01 = 'D2103' AND area_name = '全国' AND year BETWEEN 1975 AND 2022
)
SELECT g.year, ROUND(top10, 1) AS top10, ROUND(bottom10, 1) AS bottom10,
  ROUND(top10 - bottom10, 1) AS gap, ROUND(national, 1) AS national,
  ROUND(top10_sd, 1) AS top10_sd, ROUND(bottom10_sd, 1) AS bottom10_sd,
  top10_sd AS top10_sd_raw, bottom10_sd AS bottom10_sd_raw
FROM g JOIN n USING (year)
ORDER BY g.year
```

```sql id=group_sd_since_2004
-- 2004年度以降の、上位10・下位10それぞれの中の標準偏差の平均（プロットはしない）
SELECT ROUND(AVG(top10_sd_raw), 1) AS "上位10の標準偏差の平均", ROUND(AVG(bottom10_sd_raw), 1) AS "下位10の標準偏差の平均"
FROM group_trend
WHERE year >= 2004
```

```sql id=yearly_corr
-- 年度ごとの、財政力指数の順位と経常収支比率の順位の相関（東京都を除く46道府県）
WITH r AS (
  SELECT year, RANK() OVER (PARTITION BY year ORDER BY fs) AS rf, RANK() OVER (PARTITION BY year ORDER BY cr) AS rc
  FROM pref_yearly
),
c AS (
  SELECT year, CORR(rf, rc) AS rho FROM r GROUP BY year
)
SELECT COUNT(*) AS "年度数", COUNT(*) FILTER (WHERE rho > 0) AS "相関が正の年度",
  ROUND(MEDIAN(rho), 2) AS "中央値", ROUND(MIN(rho), 2) AS "最小", ROUND(MAX(rho), 2) AS "最大"
FROM c
```

```sql id=invest_trend
-- 投資的経費÷一般財源（%）の、財政力指数の上位10・下位10の平均
WITH r AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY fs DESC, area_name) AS rn
  FROM pref_yearly
)
SELECT year,
  ROUND(AVG(investment / general_revenue) FILTER (WHERE rn <= 10) * 100, 1) AS top10,
  ROUND(AVG(investment / general_revenue) FILTER (WHERE rn > 36) * 100, 1) AS bottom10
FROM r
GROUP BY year
ORDER BY year
```

```sql id=invest_summary
-- 下位10の平均が上位10を上回った年度の数（プロットはしない）
SELECT COUNT(*) AS "年度数", COUNT(*) FILTER (WHERE bottom10 > top10) AS "下位10が上回った年度" FROM invest_trend
```

```sql id=group_summary
-- 上位・下位を5・10・15・23団体で区切った場合と、2022年度の顔ぶれに固定した場合の比較（判定は丸める前の平均で行う）
WITH m22 AS (
  SELECT area_name, ROW_NUMBER() OVER (ORDER BY fs DESC, area_name) AS rn22
  FROM pref_yearly
  WHERE year = 2022
),
r AS (
  SELECT p.*, ROW_NUMBER() OVER (PARTITION BY year ORDER BY fs DESC, area_name) AS rn, rn22
  FROM pref_yearly p JOIN m22 USING (area_name)
),
s AS (
  SELECT k, year,
    AVG(cr) FILTER (WHERE rn <= k) - AVG(cr) FILTER (WHERE rn > 46 - k) AS d_yearly,
    AVG(cr) FILTER (WHERE rn22 <= k) - AVG(cr) FILTER (WHERE rn22 > 46 - k) AS d_fixed
  FROM r, (VALUES (5), (10), (15), (23)) t(k)
  GROUP BY 1, 2
)
SELECT k AS "上位・下位の団体数", COUNT(*) AS "年度数",
  COUNT(*) FILTER (WHERE d_yearly > 0) AS "上位が高い年度（年度ごとに並べ直し）",
  STRING_AGG(year::VARCHAR, '・' ORDER BY year) FILTER (WHERE d_yearly <= 0) AS "上位が高くない年度（年度ごとに並べ直し）",
  COUNT(*) FILTER (WHERE d_fixed > 0) AS "上位が高い年度（2022年度の顔ぶれに固定）"
FROM s
GROUP BY 1
ORDER BY 1
```

```sql id=tokyo_rank
-- 東京都の財政力指数の順位（高い順）と、経常収支比率の順位（低い順。1が最も低い）
WITH w AS (
  SELECT area_name, year,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2101') AS fs,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'D2103') AS cr
  FROM e_stat.ssds.d_pref_administration
  WHERE cat01 IN ('D2101', 'D2103') AND area_name != '全国' AND year BETWEEN 1975 AND 2022
  GROUP BY 1, 2
),
r AS (
  SELECT *, RANK() OVER (PARTITION BY year ORDER BY fs DESC) AS fs_rank,
    RANK() OVER (PARTITION BY year ORDER BY cr) AS cr_rank_low
  FROM w
)
SELECT year, ROUND(fs, 3) AS fiscal_strength, fs_rank, ROUND(cr, 1) AS current_ratio, cr_rank_low
FROM r
WHERE area_name = '東京都'
ORDER BY year
```
