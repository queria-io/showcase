---
title: 産婦人科は48年で6割減り、1施設が受け持つ妊娠の数は東京で増え秋田で半分以下になった
description: 産婦人科を掲げる病院と診療所は1975年度の9,579施設から2023年度の3,845施設へ約6割減りました。妊娠の届出数で割った1施設あたりの件数は、東京都で31.2%増え、秋田県で56.1%減っています。
ogDescription: 産婦人科を掲げる施設は48年で約6割減りました。1施設あたりの妊娠の届出数は東京都で31.2%増え、秋田県で56.1%減っています。
publishedAt: 2026-08-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 産婦人科
  - 母子保健
  - 医療施設
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 医療施設調査
    url: https://www.mhlw.go.jp/toukei/list/79-1.html
    publisher: 厚生労働省
  - title: 地域保健・健康増進事業報告
    url: https://www.mhlw.go.jp/toukei/list/32-19.html
    publisher: 厚生労働省
agentHint: 産婦人科の一般病院数（I530120）と一般診療所数（I530216）を自分の県だけ1975年度から3年ごとに並べて、妊娠の届出数（I2201）で割った1施設あたりの件数も出して。隣接する県とも比べて
socialAnnounce: |-
  産婦人科を掲げる病院と診療所は48年で6割減りました。

  妊娠の届出も同じだけ減ったため、1施設あたりの件数は東京都で31.2%増え、秋田県では56.1%減っています。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

産婦人科を掲げる病院と診療所は、1975年度の9,579施設から2023年度の3,845施設へ、約6割減りました。妊娠の届出数も同じく約6割減ったので、全国の1施設あたりの妊娠の届出数は1975年度の201.6件、2023年度の195.3件でほぼ同じです。都道府県別には、1施設あたりの件数は東京都で31.2%増え、秋田県で56.1%減っています。

市町村が産後ケアや妊婦健康診査の委託先を探すときは、県内に産婦人科がどれだけあるかを最初に確認します。市町村の区域内で委託先が見つからないときは都道府県が広域の調整を行うので、県全体でどこにどれだけあるかを把握しておく必要があります。この記事では、[総務省統計局の社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)に収録された都道府県別データを使い、1975年度から2023年度までの施設数と妊娠の届出数を並べます。

## 産婦人科を掲げる施設は48年で6割減った

このデータは社会・人口統計体系の都道府県別健康・医療データ（`i_pref_health`）から取得しています。産婦人科の施設数は、病院と診療所で別のカテゴリに分かれています。

| コード  | 内容                               | 出典                       |
| ------- | ---------------------------------- | -------------------------- |
| I530120 | 診療科目別一般病院数（産婦人科）   | 医療施設調査               |
| I530216 | 診療科目別一般診療所数（産婦人科） | 医療施設調査               |
| I2201   | 妊娠の届出数                       | 地域保健・健康増進事業報告 |

同じテーブルには産科（`I530121`）と婦人科（`I530122`）を掲げる一般病院数も別に収録されていますが、収録は1998年度からです。以下で「産婦人科の施設」と呼ぶのは、1975年度から値がある産婦人科（`I530120`・`I530216`）の2つを合わせた数です。診療科目別一般診療所数は3年ごとの医療施設静態調査でしか集計されないので、1975年度から2023年度までの3年ごとの年度を並べています。

```chart
{
  "layer": [
    {
      "data": {"name": "facilities"},
      "transform": [
        {"fold": ["hosp", "clinic"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"hosp\": \"一般病院\", \"clinic\": \"一般診療所\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"hosp\",\"clinic\"], datum.__series)", "as": "__order"}
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
          "axis": {"title": "施設数（施設）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["一般病院", "一般診療所"], "range": ["#3b82f6", "#93c5fd"]},
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

全国の産婦人科は、1975年度の9,579施設から2023年度の3,845施設まで、約6割減りました。一般病院は2,357施設から1,061施設へ、一般診療所は7,222施設から2,784施設へ減っています。診療所のほうが減り方は大きいものの、2023年度でも診療所の数は病院の2.6倍です。病院だけを集計すると、産婦人科の施設全体の3割ほどしか含まれません。

この数字は施設が掲げている診療科目の集計で、産婦人科を掲げていても分娩を扱っていない施設を含みます。分娩できる施設の数とは異なります。

## 1施設あたりの妊娠の届出数は、1975年度の201.6件と2023年度の195.3件でほぼ同じ

妊娠の届出数を施設数で割った件数を年度ごとに並べました。妊娠の届出は、母子保健法にもとづいて妊婦が住んでいる市町村に出すもので、その年度に把握された妊娠の件数です。

```chart
{
  "layer": [
    {
      "data": {"name": "load_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"per_fac\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#ec4899"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "per_fac", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "per_fac",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1施設あたりの妊娠の届出数（件）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1施設あたりの妊娠の届出数は、1975年度が201.6件、2023年度が195.3件で、ほぼ同じ水準です。妊娠の届出数も1,931,345件から750,992件へ、施設と同じく約6割減ったためです。

途中の年度では大きく変わっています。1987年度の166.4件が最も少なく、その後は増え続けて2014年度に251.4件で最も多くなり、2023年度の195.3件まで22.3%下がっています。1990年代後半から2010年代前半は施設の減り方が妊娠の減り方より速く、2014年度以降は妊娠の減り方が施設の減り方より速くなっています。

妊娠の届出は妊婦が住んでいる市町村に出されるので、この件数は分娩した施設の所在地でなく、住んでいる県に計上されます。

## 1施設あたりの件数は、東京都で31.2%増え、秋田県で56.1%減った

都道府県別に、1975年度と2023年度の1施設あたり件数を比較しました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "chg_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1施設あたり妊娠の届出数の変化率（%、1975年度→2023年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "減った県",
          "type": "nominal",
          "scale": {"domain": ["減った県", "増えた県"], "range": ["#94a3b8", "#ec4899"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "chg_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1施設あたり妊娠の届出数の変化率（%、1975年度→2023年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "増えた県",
          "type": "nominal",
          "scale": {"domain": ["減った県", "増えた県"], "range": ["#94a3b8", "#ec4899"]},
          "title": null
        }
      }
    }
  ]
}
```

増えたのは15都道府県、減ったのは32都道府県で、東京都の31.2%増から秋田県の56.1%減まで差があります。増加率が大きいのは東京都（144.6件→189.6件）、埼玉県（261.5件→324.3件）、岡山県（183.1件→226.5件）です。減少率が大きいのは秋田県（189.3件→83.0件）、新潟県（219.3件→139.7件）、和歌山県（181.6件→120.5件）、岩手県（176.7件→119.1件）です。

大都市のある県では1施設あたりの件数が増え、人口が減った県では施設が減った以上に妊娠が減って件数が下がりました。件数が下がった県では、受け入れに余裕ができたわけではなく、妊娠の数が施設の数より速く減っています。

## 1施設あたりの件数が多い県と、1施設あたりの可住地面積が広い県は異なる

施設が少ない県では、残った施設が広い範囲を受け持つので、1施設あたりの件数が少なくても産婦人科が足りているとは限りません。2023年度について、1施設あたりの可住地面積と1施設あたりの妊娠の届出数を並べました。可住地面積は同じ社会・人口統計体系の都道府県別自然環境データ（`b_pref_land`）の可住地面積（`B1103`）で、総面積から林野と湖沼を除いた面積です。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "reach_2023"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "km2_per_fac", "type": "quantitative"},
          {"field": "per_fac", "type": "quantitative"}
        ],
        "x": {
          "field": "km2_per_fac",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1施設あたりの可住地面積（km²、対数目盛）", "grid": true}
        },
        "y": {
          "field": "per_fac",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1施設あたりの妊娠の届出数（件）", "grid": true}
        },
        "color": {
          "datum": "全47県",
          "type": "nominal",
          "scale": {"domain": ["全47県", "本文で触れる県"], "range": ["#94a3b8", "#7c3aed"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "reach_named"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "km2_per_fac", "type": "quantitative"},
          {"field": "per_fac", "type": "quantitative"}
        ],
        "x": {
          "field": "km2_per_fac",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1施設あたりの可住地面積（km²、対数目盛）", "grid": true}
        },
        "y": {
          "field": "per_fac",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1施設あたりの妊娠の届出数（件）", "grid": true}
        },
        "color": {
          "datum": "本文で触れる県",
          "type": "nominal",
          "scale": {"domain": ["全47県", "本文で触れる県"], "range": ["#94a3b8", "#7c3aed"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "reach_named"},
      "mark": {"type": "text", "align": "left", "dx": 6},
      "encoding": {
        "x": {
          "field": "km2_per_fac",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1施設あたりの可住地面積（km²、対数目盛）", "grid": true}
        },
        "y": {
          "field": "per_fac",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1施設あたりの妊娠の届出数（件）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    },
    {
      "data": {"name": "reach_named_left"},
      "mark": {"type": "point", "color": "#7c3aed", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "km2_per_fac", "type": "quantitative"},
          {"field": "per_fac", "type": "quantitative"}
        ],
        "x": {
          "field": "km2_per_fac",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1施設あたりの可住地面積（km²、対数目盛）", "grid": true}
        },
        "y": {
          "field": "per_fac",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1施設あたりの妊娠の届出数（件）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "reach_named_left"},
      "mark": {"type": "text", "align": "right", "dx": -6},
      "encoding": {
        "x": {
          "field": "km2_per_fac",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1施設あたりの可住地面積（km²、対数目盛）", "grid": true}
        },
        "y": {
          "field": "per_fac",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1施設あたりの妊娠の届出数（件）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2つの値は連動していません。件数は埼玉県の324.3件から秋田県の83.0件まで3.9倍の差ですが、1施設あたりの可住地面積は北海道の166.8km²から東京都の2.8km²まで60倍近くの差があります。

件数が多いのは埼玉県（324.3件・19.0km²）、沖縄県（318.6件・28.9km²）、千葉県（254.1件・23.7km²）で、1施設あたりの可住地面積はいずれも30km²未満です。面積が広いのは北海道（176.3件・166.8km²）、山形県（149.6件・89.8km²）、岩手県（119.1件・87.2km²）で、件数はいずれも全国の195.3件を下回ります。どちらも大きいのは茨城県（242.6件・59.8km²）と栃木県（202.0件・58.9km²）で、件数は上位10県に入り、1施設あたりの可住地面積も約59km²です。

この面積は県の可住地を施設数で割った値で、住民から施設までの距離とは異なります。産婦人科は人口が集まる場所にあるので、多くの住民にとっての距離はこの値より短くなります。県内で施設が1つ閉じたときに、残りの施設が受け持つ範囲がどれだけ広がるかの目安として使えます。

## 業務でどう使うか

1施設あたりの件数と可住地面積は、次のように使えます。

- 課題の判別: 自分の県が件数の多い県か面積の広い県かを確認し、件数が多い県では委託先の受け入れ枠、面積が広い県では移動距離の負担を主な課題として、産後ケアの実施方式（宿泊型・通所型・訪問型）の組み合わせを決める
- 課題の優先順位: 1施設あたりの件数の推移を県単位で確認し、増え続けている県では委託先の追加確保を、減っている県では施設の維持を優先する
- 監視する県の選定: 施設数が20〜30施設の県では1施設の休止で県全体の受け入れ枠が3〜5%変わるので、件数の水準より施設数で監視する県を選ぶ
- 契約手続きの設計: 病院と診療所を分けて集計し、診療所の割合が大きい県では委託契約の相手が小規模施設に偏ることを前提に、書式や報告の負担を軽くする

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)の都道府県別データを2026年8月17日時点で集計しています。産婦人科の施設数の元データは厚生労働省の[医療施設調査](https://www.mhlw.go.jp/toukei/list/79-1.html)、妊娠の届出数は[地域保健・健康増進事業報告](https://www.mhlw.go.jp/toukei/list/32-19.html)で、可住地面積は同じ社会・人口統計体系の自然環境データです。数値はすべて年度の値で、収録は1975年度から2023年度までです。

Queriaは、社会・人口統計体系のように分野ごとに公表される統計を、列名・単位・年度の表記を統一し、カテゴリコードの意味をメタデータとして付けて公開しています。本記事で使った[健康・医療テーブル](/datasets/queria/e_stat/ssds/i_pref_health)と[自然環境テーブル](/datasets/queria/e_stat/ssds/b_pref_land)から、自分の県の施設数と妊娠の届出数の推移を確認したり、近隣の県と並べたりできます。

```sql id=facilities
WITH s AS (SELECT year, SUM(CASE WHEN cat01 = 'I530120' THEN TRY_CAST(value AS DOUBLE) END) AS hosp, SUM(CASE WHEN cat01 = 'I530216' THEN TRY_CAST(value AS DOUBLE) END) AS clinic FROM e_stat.ssds.i_pref_health WHERE area_name = '全国' AND cat01 IN ('I530120', 'I530216') GROUP BY year) SELECT year, hosp, clinic, hosp + clinic AS total FROM s WHERE clinic IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=load_trend
WITH s AS (SELECT year, SUM(CASE WHEN cat01 IN ('I530120', 'I530216') THEN TRY_CAST(value AS DOUBLE) END) AS fac, SUM(CASE WHEN cat01 = 'I2201' THEN TRY_CAST(value AS DOUBLE) END) AS preg, SUM(CASE WHEN cat01 = 'I530216' THEN TRY_CAST(value AS DOUBLE) END) AS clinic FROM e_stat.ssds.i_pref_health WHERE area_name = '全国' AND cat01 IN ('I530120', 'I530216', 'I2201') GROUP BY year) SELECT year, fac, preg, ROUND(preg / fac, 1) AS per_fac FROM s WHERE clinic IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=chg_down
WITH d AS (SELECT area_name, year, SUM(CASE WHEN cat01 IN ('I530120', 'I530216') THEN TRY_CAST(value AS DOUBLE) END) AS fac, SUM(CASE WHEN cat01 = 'I2201' THEN TRY_CAST(value AS DOUBLE) END) AS preg FROM e_stat.ssds.i_pref_health WHERE area_name <> '全国' AND cat01 IN ('I530120', 'I530216', 'I2201') AND year IN (1975, 2023) GROUP BY 1, 2), c AS (SELECT a.area_name, ROUND(a.preg / a.fac, 1) AS per1975, ROUND(b.preg / b.fac, 1) AS per2023, ROUND((b.preg / b.fac) / (a.preg / a.fac) * 100 - 100, 1) AS chg FROM d a JOIN d b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023), r AS (SELECT area_name, per1975, per2023, chg, ROW_NUMBER() OVER (ORDER BY chg DESC, area_name) AS rn FROM c) SELECT area_name, per1975, per2023, chg FROM r WHERE chg < 0 ORDER BY rn DESC
```

```sql id=chg_up
WITH d AS (SELECT area_name, year, SUM(CASE WHEN cat01 IN ('I530120', 'I530216') THEN TRY_CAST(value AS DOUBLE) END) AS fac, SUM(CASE WHEN cat01 = 'I2201' THEN TRY_CAST(value AS DOUBLE) END) AS preg FROM e_stat.ssds.i_pref_health WHERE area_name <> '全国' AND cat01 IN ('I530120', 'I530216', 'I2201') AND year IN (1975, 2023) GROUP BY 1, 2), c AS (SELECT a.area_name, ROUND(a.preg / a.fac, 1) AS per1975, ROUND(b.preg / b.fac, 1) AS per2023, ROUND((b.preg / b.fac) / (a.preg / a.fac) * 100 - 100, 1) AS chg FROM d a JOIN d b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023), r AS (SELECT area_name, per1975, per2023, chg, ROW_NUMBER() OVER (ORDER BY chg DESC, area_name) AS rn FROM c) SELECT area_name, per1975, per2023, chg FROM r WHERE chg >= 0 ORDER BY rn DESC
```

```sql id=reach_2023
WITH f AS (SELECT area_name, SUM(CASE WHEN cat01 IN ('I530120', 'I530216') THEN TRY_CAST(value AS DOUBLE) END) AS fac, SUM(CASE WHEN cat01 = 'I2201' THEN TRY_CAST(value AS DOUBLE) END) AS preg FROM e_stat.ssds.i_pref_health WHERE year = 2023 AND area_name <> '全国' AND cat01 IN ('I530120', 'I530216', 'I2201') GROUP BY 1), l AS (SELECT area_name, TRY_CAST(value AS DOUBLE) / 100.0 AS km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2023 AND area_name <> '全国') SELECT f.area_name, f.fac, ROUND(f.preg / f.fac, 1) AS per_fac, ROUND(l.km2 / f.fac, 1) AS km2_per_fac FROM f JOIN l ON f.area_name = l.area_name ORDER BY km2_per_fac DESC
```

```sql id=reach_named
WITH f AS (SELECT area_name, SUM(CASE WHEN cat01 IN ('I530120', 'I530216') THEN TRY_CAST(value AS DOUBLE) END) AS fac, SUM(CASE WHEN cat01 = 'I2201' THEN TRY_CAST(value AS DOUBLE) END) AS preg FROM e_stat.ssds.i_pref_health WHERE year = 2023 AND area_name IN ('埼玉県', '沖縄県', '千葉県', '茨城県', '栃木県', '東京都', '山形県', '岩手県', '秋田県') AND cat01 IN ('I530120', 'I530216', 'I2201') GROUP BY 1), l AS (SELECT area_name, TRY_CAST(value AS DOUBLE) / 100.0 AS km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2023 AND area_name <> '全国') SELECT f.area_name, ROUND(f.preg / f.fac, 1) AS per_fac, ROUND(l.km2 / f.fac, 1) AS km2_per_fac FROM f JOIN l ON f.area_name = l.area_name ORDER BY f.area_name
```

```sql id=reach_named_left
WITH f AS (SELECT area_name, SUM(CASE WHEN cat01 IN ('I530120', 'I530216') THEN TRY_CAST(value AS DOUBLE) END) AS fac, SUM(CASE WHEN cat01 = 'I2201' THEN TRY_CAST(value AS DOUBLE) END) AS preg FROM e_stat.ssds.i_pref_health WHERE year = 2023 AND area_name IN ('北海道') AND cat01 IN ('I530120', 'I530216', 'I2201') GROUP BY 1), l AS (SELECT area_name, TRY_CAST(value AS DOUBLE) / 100.0 AS km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2023 AND area_name <> '全国') SELECT f.area_name, ROUND(f.preg / f.fac, 1) AS per_fac, ROUND(l.km2 / f.fac, 1) AS km2_per_fac FROM f JOIN l ON f.area_name = l.area_name ORDER BY f.area_name
```
