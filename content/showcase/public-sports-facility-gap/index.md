---
title: 公共スポーツ施設が全国平均より多い35県のうち34県は、人口の減り方も全国平均より大きい
description: e-Statの社会体育施設データで、人口10万人あたりの公共スポーツ施設数と人口増減率を都道府県別に比較しました。最も多い秋田県は90.7施設で、最も少ない大阪府の約6.7倍です。施設数と2010〜2021年の人口増減率の相関係数は約マイナス0.7でした。
publishedAt: 2026-06-06
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - スポーツ
  - 公共施設
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会教育調査
    url: https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm
    publisher: 文部科学省
agentHint: 公共スポーツ施設を種別ごと（G3102の内訳）に分けて、秋田県と大阪府で人口10万人あたりの数を比べて、どの種別で供給差が大きいか見て
socialAnnounce: |-
  公共スポーツ施設の供給量と人口減少を、都道府県別に重ねてみました。

  供給が多い県ほど人口も減っていて、施設の統廃合をどこから検討すべきかが見えてきます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

人口10万人あたりの公共スポーツ施設数は、最も多い秋田県が90.7施設、最も少ない大阪府が13.6施設で、約6.7倍の差があります。人口あたりの施設数と2010〜2021年の人口増減率の相関係数は約マイナス0.7で、施設が多い県ほど人口が減っています。全国平均（36.4施設）より施設が多い35県のうち34県は、人口の減り方も全国平均（マイナス2.0%）より大きくなっていました。

体育館や運動広場、屋内プールといった公共スポーツ施設の多くは、高度経済成長期から1990年代にかけて整備され、いま一斉に更新時期を迎えています。自治体の公共施設マネジメント担当者が施設の維持・統廃合を検討するときは、自分の地域が全国と比較してどれだけの施設を持っているかを確認する必要があります。この記事では、[e-Stat「社会・人口統計体系」](https://www.e-stat.go.jp/regional-statistics/ssdsview) の都道府県別文化・スポーツデータ（`g_pref_culture` テーブル）を使い、公共スポーツ施設の数を都道府県別に集計しました。社会体育施設に関する主なカテゴリは次のとおりです。

| コード  | 内容                               |
| ------- | ---------------------------------- |
| G3102   | 社会体育施設数                     |
| G310203 | 多目的運動広場数（公共）           |
| G310206 | 体育館数（公共）                   |
| G310202 | 野球場・ソフトボール場数（公共）   |
| G310204 | 水泳プール数（屋内、屋外）（公共） |

このデータで分かるのは施設の数だけで、大規模アリーナと小さな地区体育館も同じ1施設として数えられています。学校の体育館やグラウンドの開放分、民間のスポーツクラブは含みません。

## 全国の公共スポーツ施設は、2005年から約5%減った

社会体育施設数（`G3102`）の全国の総数の推移です。このデータは文部科学省の社会教育調査にもとづいていて、調査がおおむね3年ごとなので、調査実施年の値をつないでいます。

```chart
{
  "layer": [
    {
      "data": {"name": "facility_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#7c3aed"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "total",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "社会体育施設数（施設）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

全国の公共スポーツ施設数は、1999年以降おおむね4万6千〜4万8千施設で推移しています。2005年の約4万8千施設が最も多く、その後は緩やかに減り、2021年は45,658施設で、2005年から約5%減りました。人口減少と財政の制約のなかで、新設より統廃合・複合化が進んでいると考えられます。

## 最も多いのは多目的運動広場で、体育館、野球場・ソフトボール場が続く

社会体育施設は、種目ごとの施設の合計です。2021年時点で施設数の多い種類を並べました。`G3102` の下位コードだけを集計し、施設数が0の種別を除いた上位10種類です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "facility_type"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "cnt", "type": "quantitative"},
          {"field": "facility_type", "type": "nominal"}
        ],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "施設数（公共・2021年）", "grid": true}
        },
        "y": {"field": "facility_type", "type": "nominal", "axis": {"title": ""}, "sort": null}
      }
    }
  ]
}
```

最も多いのは多目的運動広場（7,711施設）で、体育館（7,145施設）、野球場・ソフトボール場（6,150施設）が続きます。屋外の運動スペースが上位に並びます。屋内プールやテニスコート、武道場なども一定数あり、種目ごとに維持コストや更新単価は大きく異なります。施設マネジメントでは、この種別の構成をもとに優先順位を付ける必要があります。

## 人口10万人あたりでは、秋田県が90.7施設で大阪府の約6.7倍

施設の総数を都道府県の人口で割り、人口10万人あたりの公共スポーツ施設数を出しました。人口は推計人口（`A1101`）を使い、47都道府県を上位10・中間27・下位10の3グループに分けて並べています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり公共スポーツ施設数", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#7c3aed", "#c4b5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり公共スポーツ施設数", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#7c3aed", "#c4b5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり公共スポーツ施設数", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#7c3aed", "#c4b5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も多いのは秋田県（90.7施設）で、鳥取県（90.2施設）、長野県（89.9施設）が続きます。最も少ないのは大阪府（13.6施設）で、東京都（15.9施設）、神奈川県（17.2施設）と大都市が下位に並びます。秋田県と大阪府の差は約6.7倍です。

施設の総数は大阪府が1,194施設、秋田県が857施設で、大阪府のほうが多くなっています。人口が約9倍異なるので、人口あたりでは秋田県のほうが多くなります。

## 人口が多い県ほど、人口あたりの施設数は少ない

横軸に人口、縦軸に人口10万人あたりの施設数を取った散布図です。

```chart
{
  "layer": [
    {
      "data": {"name": "pref_scatter"},
      "mark": {"type": "point", "color": "#7c3aed", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_man", "type": "quantitative"},
          {"field": "per_100k", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口（万人）", "grid": true}
        },
        "y": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり施設数", "grid": true}
        }
      }
    }
  ]
}
```

人口が多い県ほど、人口あたりの施設数は少なくなっています。人口100万人未満の県の多くは60〜90施設で、人口500万人を超える大都市圏は20施設前後です。

北海道は人口が約518万人と多いものの、71.9施設と多くなっています。住む場所が広く分散しているので、住民が利用できる範囲に施設を置くには多くの施設が必要になるためと考えられます。人口あたりの施設数は面積や人口密度を考慮していないので、可住地が広い道県では高く出ます。

## 施設が全国平均より多い35県のうち34県は、人口の減り方も全国平均より大きい

施設マネジメントでは、今後の利用者の増減も判断材料になります。総務省は全自治体に[公共施設等総合管理計画](https://www.soumu.go.jp/iken/koushinhiyou.html)の策定を求めており、この計画では人口の見通しと施設の保有量を比較して、施設の量と配置を見直します。

横軸に2010年から2021年の人口増減率、縦軸に人口10万人あたりの施設数を取り、47都道府県の平均（36.4施設、人口増減率マイナス2.0%）の線で4つの領域に分けました。この線は47都道府県の平均で、制度上定められた基準ではありません。点の色は、全国平均より施設が多い県（赤）と少ない県（青）を表します。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "quad_high"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_chg", "type": "quantitative"},
          {"field": "per_100k", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_chg",
          "type": "quantitative",
          "scale": {"domain": [-15, 9], "zero": false, "nice": false},
          "axis": {"title": "人口増減率（2010→2021年・%）", "grid": true}
        },
        "y": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたり施設数", "grid": true}
        },
        "color": {
          "datum": "供給が全国平均より多い",
          "type": "nominal",
          "scale": {"domain": ["供給が全国平均より多い", "供給が全国平均より少ない"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "quad_low"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_chg", "type": "quantitative"},
          {"field": "per_100k", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_chg",
          "type": "quantitative",
          "scale": {"domain": [-15, 9], "zero": false, "nice": false},
          "axis": {"title": "人口増減率（2010→2021年・%）", "grid": true}
        },
        "y": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "人口10万人あたり施設数", "grid": true}
        },
        "color": {
          "datum": "供給が全国平均より少ない",
          "type": "nominal",
          "scale": {"domain": ["供給が全国平均より多い", "供給が全国平均より少ない"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": -2, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": -15, "type": "quantitative"},
        "x2": {"datum": 9, "type": "quantitative"},
        "y": {"datum": 36.4, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 10,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": -2, "type": "quantitative"},
        "y": {"datum": 99, "type": "quantitative"},
        "text": {"value": "全国平均 -2.0%"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 10,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 8.5, "type": "quantitative"},
        "y": {"datum": 36.4, "type": "quantitative"},
        "text": {"value": "全国平均 36.4施設"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 11,
        "color": "#ef4444"
      },
      "encoding": {
        "x": {"datum": -14.5, "type": "quantitative"},
        "y": {"datum": 92, "type": "quantitative"},
        "text": {"value": "供給多い × 人口減\n統廃合・複合化の検討余地"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 11,
        "color": "#3b82f6"
      },
      "encoding": {
        "x": {"datum": 8.5, "type": "quantitative"},
        "y": {"datum": 6, "type": "quantitative"},
        "text": {"value": "供給少ない × 人口維持・増\n拡充・利便性向上の余地"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

人口あたりの施設数と人口増減率の相関係数は約マイナス0.7で、人口あたりの施設が多い県ほど人口が減っています。秋田県（90.7施設・人口マイナス13.0%）や島根県（78.8施設・人口マイナス7.3%）は左上にあり、全国平均の2倍を超える施設を持ちながら人口が減っています。施設をそのまま維持すると、住民1人あたりの維持・更新の負担が大きくなります。

全国平均より施設が多い35県のうち34県は、人口の減り方も全国平均（マイナス2.0%）より大きく、左上の領域にあります。東京都（15.9施設・人口プラス6.5%）や沖縄県（29.6施設・人口プラス5.4%）は右下にあり、施設が少ないので、利用機会の確保や施設の利便性向上が課題になります。

## 自分の県がどの領域にあるかで、検討する方向が変わる

- 左上（施設が多く、人口が減っている）: 統廃合・複合化・広域での共同利用を優先して検討する。更新単価の高いプールや体育館から、近隣施設との統合や民間活用ができるかを確認する
- 左下（施設が少なく、人口が減っている）: 残す施設を絞り込み、機能の集約と老朽化対策に予算を充てる
- 右下（施設が少なく、人口が維持・増加している）: 施設が不足していないかを確認する。種別の構成を見て、住民の利用が多い施設の利便性向上や利用時間の拡大を検討する

どの領域でも、運動広場・体育館・プールなど施設の種別ごとに維持コストと更新時期は異なります。自分の県の施設数の順位と人口の推移を、公共施設等総合管理計画の見直しに反映できます。都道府県単位の集計なので、県内のどの市町村に施設が多いかは、市町村単位のデータで確認する必要があります。

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)に収録された都道府県別の文化・スポーツデータと人口データを、2026年7月11日時点で取得して集計しています。施設数の元データは文部科学省の[社会教育調査](https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm)で、推移のグラフは1999・2002・2005・2008・2011・2015・2018・2021年の調査実施年をつないでいます。人口増減率は2010年と2021年の推計人口から計算しています。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の文化・スポーツ施設データ](/datasets/queria/e_stat/ssds/g_pref_culture)から、自分の県の施設数と人口の推移を全国平均と比較し、どの領域にあるかを確認できます。

```sql id=facility_trend
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS total FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year >= 1999 AND year <= 2021 GROUP BY year ORDER BY year
```

```sql id=facility_type
SELECT replace(split_part(item_name, '_', 2), '（公共）', '') AS facility_type, SUM(TRY_CAST(value AS DOUBLE)) AS cnt FROM e_stat.ssds.g_pref_culture WHERE cat01 LIKE 'G3102%' AND cat01 <> 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY facility_type HAVING SUM(TRY_CAST(value AS DOUBLE)) > 0 ORDER BY cnt DESC LIMIT 10
```

```sql id=pref_top
WITH fac AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT f.area_name, ROUND(f.val / p.val * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY f.val / p.val DESC, f.area_name) AS rn FROM fac f JOIN pop p ON f.area = p.area ) SELECT area_name, per_100k FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH fac AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT f.area_name, ROUND(f.val / p.val * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY f.val / p.val DESC, f.area_name) AS rn FROM fac f JOIN pop p ON f.area = p.area ) SELECT area_name, per_100k FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH fac AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT f.area_name, ROUND(f.val / p.val * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY f.val / p.val DESC, f.area_name) AS rn FROM fac f JOIN pop p ON f.area = p.area ) SELECT area_name, per_100k FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=pref_scatter
WITH fac AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ) SELECT f.area_name, ROUND(p.val / 10000, 1) AS pop_man, ROUND(f.val / p.val * 100000, 1) AS per_100k FROM fac f JOIN pop p ON f.area = p.area ORDER BY p.val DESC
```

```sql id=quad_high
WITH fac AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), p21 AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), p10 AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2010 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ) SELECT f.area_name, ROUND(f.val / p21.p * 100000, 1) AS per_100k, ROUND((p21.p - p10.p) / p10.p * 100, 1) AS pop_chg FROM fac f JOIN p21 ON f.area = p21.area JOIN p10 ON f.area = p10.area WHERE f.val / p21.p * 100000 > 36.4 ORDER BY per_100k DESC
```

```sql id=quad_low
WITH fac AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G3102' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), p21 AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2021 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), p10 AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2010 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ) SELECT f.area_name, ROUND(f.val / p21.p * 100000, 1) AS per_100k, ROUND((p21.p - p10.p) / p10.p * 100, 1) AS pop_chg FROM fac f JOIN p21 ON f.area = p21.area JOIN p10 ON f.area = p10.area WHERE f.val / p21.p * 100000 <= 36.4 ORDER BY per_100k DESC
```
