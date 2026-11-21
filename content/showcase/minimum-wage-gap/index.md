---
title: 2024年度の最低賃金の引き上げ額は、27県が東京都を上回った
description: 都道府県別の最低賃金を2010〜2024年度で比較すると、東京都より多く引き上げた道府県は2018年度まで毎年0〜2でした。2024年度は27県が東京都の50円を上回り、下回った道府県はありませんでした
publishedAt: 2026-02-26
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 最低賃金
  - 労働
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 地域別最低賃金の全国一覧
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/minimumichiran/
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 2019年度から2024年度まで、毎年の最低賃金の引き上げ額が東京都を上回った回数を都道府県別に数えて、多い順に並べて。
---

2024年度の最低賃金の引き上げ額は、27県が東京都の50円を上回り、東京都より少なく引き上げた道府県はありませんでした。2018年度までは、東京都より多く引き上げた道府県は毎年0〜2で、ほとんどの道府県が東京都より少なく引き上げていました。最高額と最低額の倍率は2014年度の1.312倍から毎年下がり、2024年度は1.223倍です。

2024年度の[地域別最低賃金](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/minimumichiran/)は、最高の東京都が1,163円、最低の秋田県が951円で、1,000円を超えたのは16都道府県でした。上位3つが東京都・神奈川県・大阪府なのは2010年度と同じです。

## 2021年度からは、東京都より多く引き上げた道府県が少なく引き上げた道府県を上回る

使ったのは e-Stat「[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)」の都道府県別労働データ（`f_pref_labor`）に入っている地域別最低賃金（`F6501`）です。単位は時間額の円で、2010年度から2024年度までの47都道府県と全国の値があります。各年度の値はその年度の秋に発効した改定後の額なので、前年度との差がその年の引き上げ額になります。都道府県ごとの額は、国の中央最低賃金審議会が示す引き上げ額の目安を参考に、各都道府県の審議会の審議を経て決まります。ここでは、全国で最も額の高い東京都を比較の基準にしています。

下の図は、各年度の引き上げ額が東京都より多かった県・同じだった県・少なかった県の数です。東京都を除く46道府県を集計しています。

```chart
{
  "layer": [
    {
      "data": {"name": "vs_tokyo"},
      "transform": [
        {"fold": ["n_below", "n_equal", "n_above"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"n_below\": \"東京都より少ない\", \"n_equal\": \"東京都と同じ\", \"n_above\": \"東京都より多い\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"n_below\",\"n_equal\",\"n_above\"], datum.__series)",
          "as": "__order"
        }
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
          "scale": {"domain": [0, 46], "zero": false, "nice": false},
          "axis": {"title": "道府県の数", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["東京都より少ない", "東京都と同じ", "東京都より多い"],
            "range": ["#94a3b8", "#93c5fd", "#ef4444"]
          },
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
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2011年度から2019年度までは、東京都より多く上げた道府県が毎年0〜2、少なく上げた道府県が28〜45でした。2016年度から2018年度の3年間は東京都の引き上げ額（25円・26円・27円）がその年の最大で、同じ額の道府県はあっても上回った道府県はありません。

2020年度は東京都が据え置き、ほかの道府県も0〜3円の引き上げだったので、この年は比較の対象から外して読みます。

2021年度からは、東京都より多く上げたところが少なく上げたところを毎年上回っています（7対0、16対11、19対18、27対0）。2024年度は東京都の50円に対して、最大は徳島県の84円でした。

```sql
SELECT year AS 年度, tokyo_inc AS 東京都の上げ幅, max_inc AS 最大, min_inc AS 最小, n_above AS 東京都より多い, n_equal AS 同じ, n_below AS 東京都より少ない FROM vs_tokyo
```

## 2010→2018年度は額の高い県ほど、2018→2024年度は額の低い県ほど多く引き上げた

1年ごとの差は数円なので、期間でまとめて比較します。2010→2018年度の8年間と、2018→2024年度の6年間それぞれについて、期首の額を横軸、期間中の引き上げ額を縦軸にして47都道府県を並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "period_points"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "w2010", "type": "quantitative"},
          {"field": "inc_2010_2018", "type": "quantitative"}
        ],
        "x": {
          "field": "w2010",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "期首の最低賃金（円）", "grid": true}
        },
        "y": {
          "field": "inc_2010_2018",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "期間中の上げ幅（円）", "grid": true}
        },
        "color": {
          "datum": "2010→2018年度（8年間）",
          "type": "nominal",
          "scale": {
            "domain": ["2010→2018年度（8年間）", "2018→2024年度（6年間）"],
            "range": ["#94a3b8", "#ef4444"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "period_points"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "w2018", "type": "quantitative"},
          {"field": "inc_2018_2024", "type": "quantitative"}
        ],
        "x": {
          "field": "w2018",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "期首の最低賃金（円）", "grid": true}
        },
        "y": {
          "field": "inc_2018_2024",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "期間中の上げ幅（円）", "grid": true}
        },
        "color": {
          "datum": "2018→2024年度（6年間）",
          "type": "nominal",
          "scale": {
            "domain": ["2010→2018年度（8年間）", "2018→2024年度（6年間）"],
            "range": ["#94a3b8", "#ef4444"]
          },
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2010→2018年度は、期首の額が高い県ほど多く引き上げています（相関0.89）。引き上げ額の上位は神奈川県165円・東京都164円・大阪府157円で、最小は福島県の115円でした。東京都を上回ったのは神奈川県だけで、45道府県が東京都より少なく引き上げています。この8年間で、最高と最低の差は179円から224円に広がりました。

2018→2024年度は反対に、期首の額が低い県ほど多く引き上げています（相関-0.57）。引き上げ額の最大は徳島県の214円で、島根県198円・鳥取県195円が続きます。最小は北海道・宮城県・奈良県・岡山県の175円で、東京都は178円でした。東京都を上回った25県には神奈川県・愛知県・千葉県・埼玉県も入っていて、額の低い県だけが多く引き上げたわけではありません。

```sql
SELECT * FROM period_summary
```

## 最高額と最低額の差は2018年度の224円が最大で、倍率は2014年度から毎年縮小している

最高額と最低額の差（棒）と、最高額が最低額の何倍か（折れ線）を年度ごとに並べます。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "gap_trend"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "gap", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "gap",
              "type": "quantitative",
              "scale": {"domain": [0, 250], "zero": false, "nice": false},
              "axis": {"title": "差（円）", "grid": true}
            },
            "color": {
              "datum": "最高と最低の差（円）",
              "type": "nominal",
              "scale": {"domain": ["最高と最低の差（円）", "最高÷最低（倍）"], "range": ["#93c5fd", "#ef4444"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "gap_trend"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ratio\"]) ? 0 : 1",
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
              {"field": "ratio", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "ratio",
              "type": "quantitative",
              "scale": {"domain": [1.2, 1.32], "zero": false, "nice": false},
              "axis": {"title": "倍率", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "最高÷最低（倍）",
              "type": "nominal",
              "scale": {"domain": ["最高と最低の差（円）", "最高÷最低（倍）"], "range": ["#93c5fd", "#ef4444"]},
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    }
  ],
  "resolve": {"scale": {"y": "independent"}},
  "config": {"legend": {"orient": "bottom"}}
}
```

差額は2010年度の179円から2018年度の224円まで毎年広がり、2024年度は212円でした。倍率は2014年度の1.312倍が最大で、そこから毎年下がり、2024年度は1.223倍と2010年度の1.279倍も下回っています。引き上げ額がほぼ同じなら、元の額が低い県ほど率では大きく上がるので、倍率は差額より先に縮小し始めました。

同じ期間に全国の値は730円から1,055円になりました。この全国の値は47都道府県の単純平均ではなく、厚生労働省が公表する全国加重平均額です。

```sql
SELECT year AS 年度, national AS 全国加重平均, highest AS 最高, lowest AS 最低, gap AS 差, ratio AS 倍率 FROM gap_trend
```

## 2024年度は、下位の9県が2円の範囲に並ぶ

2024年度の額を高い順に並べました。棒にカーソルを合わせると、前年度からの引き上げ額と順位の変化が表示されます。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_2024"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "note", "type": "nominal"},
          {"field": "w2024", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "w2024",
          "type": "quantitative",
          "scale": {"domain": [900, 1180], "zero": false, "nice": false},
          "axis": {"title": "最低賃金（円）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

下位の県は額が近く、秋田県951円、宮崎県・岩手県・沖縄県・熊本県・高知県の952円、長崎県・青森県・鹿児島県の953円と、9県が2円の幅に並びます。

順位が大きく変わった県もあります。徳島県は2023年度の896円（45位）から84円上げて980円（27位）になりました。秋田県は54円引き上げましたが、ほかの下位の県がそれ以上に引き上げたため、40位から47位になっています。

## 業務での活用

- 複数の県に事業所を持つ企業が人件費を見積もるとき、東京都と同じ額ずつ上がる前提を置くと、2018→2024年度の実績では25県で引き上げ額を小さく見積もることになります
- 自県の引き上げ額を東京都や近隣県と比較した結果は、上の表と図から年度ごとに確認できます。ここで比較しているのは法定の下限額の改定額で、実際に支払われている賃金の伸びとは異なります

## まとめ

- 東京都より多く引き上げた道府県は、2011〜2019年度は毎年0〜2でした。2021年度からは東京都より多く引き上げた道府県が少なく引き上げた道府県より多く、2024年度は27県が東京都の50円を上回り、下回った道府県はありませんでした
- 2010→2018年度は期首の額が高い県ほど多く引き上げ（相関0.89）、2018→2024年度は低い県ほど多く引き上げています（相関-0.57）
- 最高と最低の差は2018年度の224円が最大で、2024年度は212円です。倍率は2014年度の1.312倍から毎年下がり、2024年度は1.223倍でした

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別労働データを2026年9月26日時点で集計しています。元データは厚生労働省の[地域別最低賃金の全国一覧](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/minimumichiran/)で、収録は2010年度から2024年度までです。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の労働データのテーブル](/datasets/queria/e_stat/ssds/f_pref_labor)から、自県の最低賃金がどの年度にいくら上がったかを確認できます。

```sql id=vs_tokyo
WITH w AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6501' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024), d AS (SELECT a.area_name, a.year, a.v - b.v AS inc FROM w a JOIN w b ON a.area_name = b.area_name AND b.year = a.year - 1), t AS (SELECT year, inc AS tokyo_inc FROM d WHERE area_name = '東京都') SELECT d.year, t.tokyo_inc, MAX(d.inc) AS max_inc, MIN(d.inc) AS min_inc, COUNT(*) FILTER (WHERE d.inc > t.tokyo_inc) AS n_above, COUNT(*) FILTER (WHERE d.inc = t.tokyo_inc AND d.area_name != '東京都') AS n_equal, COUNT(*) FILTER (WHERE d.inc < t.tokyo_inc) AS n_below FROM d JOIN t ON d.year = t.year GROUP BY d.year, t.tokyo_inc ORDER BY d.year
```

```sql id=period_points
WITH w AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6501' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024), p AS (SELECT area_name, MAX(v) FILTER (WHERE year = 2010) AS w2010, MAX(v) FILTER (WHERE year = 2018) AS w2018, MAX(v) FILTER (WHERE year = 2024) AS w2024 FROM w GROUP BY area_name) SELECT area_name, w2010, w2018, w2024, w2018 - w2010 AS inc_2010_2018, w2024 - w2018 AS inc_2018_2024 FROM p ORDER BY area_name
```

```sql id=period_summary
WITH w AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6501' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024), p AS (SELECT area_name, MAX(v) FILTER (WHERE year = 2010) AS w2010, MAX(v) FILTER (WHERE year = 2018) AS w2018, MAX(v) FILTER (WHERE year = 2024) AS w2024 FROM w GROUP BY area_name), t AS (SELECT w2018 - w2010 AS t1, w2024 - w2018 AS t2 FROM p WHERE area_name = '東京都') SELECT '2010→2018年度' AS "期間", MAX(t.t1) AS "東京都の上げ幅（円）", MAX(w2018 - w2010) AS "最大（円）", MIN(w2018 - w2010) AS "最小（円）", COUNT(*) FILTER (WHERE w2018 - w2010 > t.t1) AS "東京都を上回った県", COUNT(*) FILTER (WHERE w2018 - w2010 < t.t1) AS "東京都を下回った道府県", ROUND(CORR(w2010, w2018 - w2010), 2) AS "期首の額と上げ幅の相関" FROM p, t UNION ALL SELECT '2018→2024年度', MAX(t.t2), MAX(w2024 - w2018), MIN(w2024 - w2018), COUNT(*) FILTER (WHERE w2024 - w2018 > t.t2), COUNT(*) FILTER (WHERE w2024 - w2018 < t.t2), ROUND(CORR(w2018, w2024 - w2018), 2) FROM p, t
```

```sql id=gap_trend
WITH w AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6501' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2024) SELECT year, MAX(v) FILTER (WHERE area_name = '全国') AS national, MAX(v) FILTER (WHERE area_name != '全国') AS highest, MIN(v) FILTER (WHERE area_name != '全国') AS lowest, MAX(v) FILTER (WHERE area_name != '全国') - MIN(v) FILTER (WHERE area_name != '全国') AS gap, ROUND(MAX(v) FILTER (WHERE area_name != '全国') / MIN(v) FILTER (WHERE area_name != '全国'), 3) AS ratio FROM w GROUP BY year ORDER BY year
```

```sql id=rank_2024
WITH w AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6501' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year IN (2023, 2024)), r AS (SELECT area_name, year, v, RANK() OVER (PARTITION BY year ORDER BY v DESC) AS rnk FROM w), p AS (SELECT area_name, MAX(v) FILTER (WHERE year = 2023) AS w2023, MAX(v) FILTER (WHERE year = 2024) AS w2024, MAX(rnk) FILTER (WHERE year = 2023) AS rank_2023, MAX(rnk) FILTER (WHERE year = 2024) AS rank_2024 FROM r GROUP BY area_name) SELECT area_name, w2023, w2024, w2024 - w2023 AS inc, rank_2023, rank_2024, '前年度から+' || CAST(CAST(w2024 - w2023 AS INTEGER) AS VARCHAR) || '円・順位 ' || CAST(rank_2023 AS VARCHAR) || '位→' || CAST(rank_2024 AS VARCHAR) || '位' AS note FROM p ORDER BY w2024 DESC, area_name
```
