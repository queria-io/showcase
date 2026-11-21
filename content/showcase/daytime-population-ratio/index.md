---
title: 千代田区の昼夜間人口比率は2374%から1355%に下がったが、昼間人口は5.7%増えた
description: 2020年の昼夜間人口比率は千代田区が1355.4%で全国最高です。2000年から比率は下がり続けましたが、昼間人口は5.7%増え、常住人口が1.85倍になっています。e-Stat の市区町村別データで、比率と通勤の流入・流出を比較しました。
publishedAt: 2026-06-22
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 昼夜間人口比率
  - 商圏分析
  - 出店戦略
  - 市区町村
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
agentHint: 昼夜間人口比率（A6108）が2020年に最も低い、流出超過のベッドタウン市区町村を下位15件で出して。どんな街が並ぶか見て
socialAnnounce: |-
  市区町村別の昼夜間人口比率と、通勤による人の流入・流出のデータを分析しました。

  出店エリアがオフィス街型か住宅地型かの見極めや、業態・営業時間の設計に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2020年の昼夜間人口比率は東京都千代田区が1355.4%で、昼間には住民の13倍を超える人がいます。この比率は2000年の2374.4%から下がり続けていますが、千代田区の昼間人口は同じ期間に855,172人から903,780人へ5.7%増えました。比率が下がったのは、常住人口が1.85倍になったためです。

昼夜間人口比率は、昼間人口を常住人口（夜間人口）で割った値です。オフィスが集まる都心では昼間に働きに来る人が住民の何倍にもなり、郊外のベッドタウンでは昼間は通勤・通学で人が出ていきます。この記事では、[e-Stat「社会・人口統計体系」](https://www.e-stat.go.jp/regional-statistics)の市区町村別データで、昼夜間人口比率と通勤・通学の流入・流出を比較し、出店エリアが「昼間型（流入超過）」か「夜間型（流出超過）」かを判断する方法を説明します。

## 2020年の比率は千代田区が1355.4%で最も高い

データは e-Stat「社会・人口統計体系」の市区町村別人口データ（`a_municipal_population`）です。国勢調査をもとに5年ごとに集計されていて、ここでは最新の2020年を使います。比率の計算には、同じテーブルにある次の指標を使います。

| コード        | 内容                                                         |
| ------------- | ------------------------------------------------------------ |
| A1101         | 総人口（常住人口＝夜間人口）                                 |
| A6107         | 昼間人口                                                     |
| A6108         | 昼夜間人口比率                                               |
| A6105 / A6106 | 流入人口（県内他市区町村／他県から従業・通学で流入する人口） |
| A6103 / A6104 | 流出人口（県内他市区町村／他県へ従業・通学で流出する人口）   |

昼夜間人口比率（`A6108`）は「昼間人口 ÷ 常住人口 × 100」で、100を超えると昼間に人が流れ込む「流入超過」、100を下回ると昼間に人が出ていく「流出超過」の街であることを示します。このテーブルは政令指定都市を市の合計と行政区の両方で収録しています。次のランキングには行政区のほうを並べているので、大阪市中央区や名古屋市中区のように区単位で出てきます。2020年の比率が高い上位15市区町村です。

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "ratio_rank"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "昼夜間人口比率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

最も高い東京都千代田区は1355.4%で、昼間には住民の13倍を超える人がいます。大阪市中央区（433.1%）、東京都中央区（374.4%）、港区（373.4%）、名古屋市中区（316.4%）など、大都市の中心業務地区が続きます。新宿区（227.1%）や渋谷区（226.1%）も、住民の2倍以上の人が昼間に流入する商業・業務地区です。

上位15には、事情の違う2種類の地域が入っています。1つは上に挙げた都市中心部のオフィス・商業地区で、流入してくる人が消費者になりやすい地域です。もう1つは、比率が別の理由で高くなっている地域です。福島県大熊町（588.5%）や富岡町・浪江町・葛尾村は、原発事故の避難指示で常住人口が大きく減ったため比率が高くなっています。4町村の常住人口は葛尾村の420人から富岡町の2,128人で、上位15のほかのどこよりも小さい値です。愛知県飛島村（282.5%）や栃木県芳賀町（200.7%）は、港湾や大規模工場など特定の事業所への通勤者で比率が高くなっています。これらの地域は、比率が高くても消費者の商圏とは言えません。昼間人口は常住人口から通勤・通学で出ていく人を引き、入ってくる人を足した値で、買い物や観光での来訪は含まないので、比率が何によって高いのかを次の流入・流出で確認します。

## 千代田区は流入85万人に対して流出1.4万人、流山市は流出が流入を上回る

昼夜間人口比率は、通勤・通学で入ってくる人と出ていく人の差で決まります。同じテーブルの流入人口（`A6105`・`A6106`の合計）と流出人口（`A6103`・`A6104`の合計）を比較すると、その市区町村に人が集まるのか、人が出ていくのかが分かります。比率が高い都心の区から、比率が100前後の市、ベッドタウンまで8市区を、比率の低い順に並べます。図の並びは流山市の78.7%から千代田区の1355.4%までです。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "flows"},
      "transform": [
        {"fold": ["inflow", "outflow"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"inflow\": \"流入人口\", \"outflow\": \"流出人口\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"inflow\",\"outflow\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業・通学による人口（人）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["流入人口", "流出人口"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["流出人口", "流入人口"]},
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

千代田区は流入人口850,924人に対して流出人口が13,824人です。流入は常住人口66,680人の12倍を超え、昼間型の商圏の例です。渋谷区（流入363,883人・流出56,422人）や大阪市中央区も流入が流出を大きく上回り、平日の昼間に需要が多いと考えられます。

武蔵野市は流入59,158人・流出47,086人で、働きに来る人と出ていく人がほぼ同じです。千葉県流山市（流入23,449人・流出66,043人）、神奈川県川崎市麻生区、奈良県生駒市、埼玉県和光市は、いずれも流出が流入を上回るベッドタウンです。これらの地域では、昼間は通勤で人が出ていき、夕方以降と週末に住民の消費があります。流入と流出のどちらが多いかで、商圏の需要が多いのが平日の昼か、夜や週末かをおおまかに判断できます。ここでの流入・流出は、2020年10月の国勢調査時点の通勤・通学の人数です。

## 千代田区と港区は、比率が下がっても昼間人口は増えた

比率がとくに高い都心の4市区について、2000年から2020年までの昼夜間人口比率の推移です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"chiyoda\"]) ? 0 : 1",
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
          {"field": "chiyoda", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "chiyoda",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "昼夜間人口比率（%）", "grid": true}
        },
        "color": {
          "datum": "東京都 千代田区",
          "type": "nominal",
          "scale": {
            "domain": ["東京都 千代田区", "大阪市 中央区", "東京都 中央区", "東京都 港区"],
            "range": ["#ef4444", "#3b82f6", "#22c55e", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"osaka\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "osaka", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "osaka",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "昼夜間人口比率（%）", "grid": true}
        },
        "color": {
          "datum": "大阪市 中央区",
          "type": "nominal",
          "scale": {
            "domain": ["東京都 千代田区", "大阪市 中央区", "東京都 中央区", "東京都 港区"],
            "range": ["#ef4444", "#3b82f6", "#22c55e", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"chuo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "chuo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "chuo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "昼夜間人口比率（%）", "grid": true}
        },
        "color": {
          "datum": "東京都 中央区",
          "type": "nominal",
          "scale": {
            "domain": ["東京都 千代田区", "大阪市 中央区", "東京都 中央区", "東京都 港区"],
            "range": ["#ef4444", "#3b82f6", "#22c55e", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"minato\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "minato", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "minato",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "昼夜間人口比率（%）", "grid": true}
        },
        "color": {
          "datum": "東京都 港区",
          "type": "nominal",
          "scale": {
            "domain": ["東京都 千代田区", "大阪市 中央区", "東京都 中央区", "東京都 港区"],
            "range": ["#ef4444", "#3b82f6", "#22c55e", "#7c3aed"]
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

千代田区の比率は2000年の2374.4%から2020年の1355.4%へ、5年ごとに下がっています。中央区（897.6%→374.4%）、大阪市中央区（947.3%→433.1%）、港区（525.7%→373.4%）も下がり続けています。

比率は昼間人口を常住人口で割った値なので、昼間人口が減っても常住人口が増えても下がります。同じ4市区の、昼間人口（`A6107`）と常住人口（`A1101`）それぞれの2000年から2020年への変化率です。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "cbd_change"},
      "transform": [
        {"fold": ["day_chg", "night_chg"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"day_chg\": \"昼間人口\", \"night_chg\": \"常住人口\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"day_chg\",\"night_chg\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2000年から2020年への変化率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["昼間人口", "常住人口"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["常住人口", "昼間人口"]},
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

千代田区の昼間人口は855,172人から903,780人へ5.7%増え、港区も837,658人から972,673人へ16.1%増えています。この2区では昼間にいる人は増えていて、比率が下がったのは常住人口が千代田区で1.85倍、港区で1.63倍になったためです。中央区は昼間人口が2.3%減った一方で、常住人口は2.33倍になりました。

大阪市中央区は、常住人口が1.87倍になった点は東京の3区と同じですが、昼間人口も523,897人から449,202人へ14.3%減りました。東京の3区で比率が下がったのは住む人が増えたためで、大阪市中央区では住む人が増えたことと働きに来る人が減ったことの両方が理由です。

比率の推移から「都心の昼間の需要が減っている」と判断すると、千代田区と港区では実際と逆の判断になります。比率が下がったエリアを候補から外す前に、昼間人口の実数が増えたか減ったかを確認してください。

## データの活用方法

昼夜間人口比率と流入・流出の人数は、次のように使えます。

- 業態・営業時間の設計: 流入超過の昼間型エリアでは平日のランチや夕方の需要に、流出超過の夜間型エリアでは夕方以降と週末の住民の需要に合わせて、業態と営業時間を決める
- 候補地の絞り込み: 比率が高い地域について、流入・流出の人数から、消費者の商圏か特定の事業所への通勤先かを区別する
- 品揃え・サービスの調整: 昼間型では調理済み食品・テイクアウトや法人向けの需要、夜間型では日用品の品揃えや家族向けのサービスに合わせて、同じ業態でも品揃えを変える
- 中長期の立地戦略: 比率の推移を見るときは、同じ期間の昼間人口の実数も確認し、比率が下がっていても昼間にいる人が増えているエリアと、昼間人口が減っているエリアを区別する

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)を e-Stat から取得し、2026年8月28日時点のデータで集計しています。使ったのは市区町村別人口データの昼夜間人口比率（`A6108`）・昼間人口（`A6107`）・総人口（`A1101`）と、流入人口（`A6105`・`A6106`）・流出人口（`A6103`・`A6104`）です。元データは[国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)で、断面は2020年、推移は2000年から2020年までの5年ごとの値です。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[市区町村別の人口・世帯データ](/datasets/queria/e_stat/ssds/a_municipal_population)から、出店候補地の昼夜間人口比率と通勤の流入・流出、2000年からの昼間人口の推移を確認できます。

```sql id=ratio_rank
SELECT area_name, ratio, night_pop FROM (WITH src AS (SELECT area_name, MAX(CASE WHEN cat01 = 'A6108' THEN TRY_CAST(value AS DOUBLE) END) AS ratio, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS night_pop FROM e_stat.ssds.a_municipal_population WHERE cat01 IN ('A6108', 'A1101') AND year = 2020 AND area_name LIKE '% %' AND area_name NOT LIKE '%特別区部%' GROUP BY area_name), parents AS (SELECT DISTINCT regexp_replace(area_name, ' [^ ]+$', '') AS p FROM src WHERE area_name LIKE '% % %') SELECT area_name, ratio, night_pop FROM src WHERE ratio IS NOT NULL AND area_name NOT IN (SELECT p FROM parents) ORDER BY ratio DESC LIMIT 15) ORDER BY ratio ASC
```

```sql id=flows
SELECT area_name, inflow, outflow, ratio FROM (SELECT area_name, MAX(CASE WHEN cat01 = 'A6105' THEN v END) + MAX(CASE WHEN cat01 = 'A6106' THEN v END) AS inflow, MAX(CASE WHEN cat01 = 'A6103' THEN v END) + MAX(CASE WHEN cat01 = 'A6104' THEN v END) AS outflow, MAX(CASE WHEN cat01 = 'A6108' THEN v END) AS ratio FROM (SELECT area_name, cat01, TRY_CAST(value AS DOUBLE) v FROM e_stat.ssds.a_municipal_population WHERE year = 2020 AND cat01 IN ('A6105', 'A6106', 'A6103', 'A6104', 'A6108')) WHERE area_name IN ('東京都 千代田区', '大阪府 大阪市 中央区', '東京都 渋谷区', '東京都 武蔵野市', '埼玉県 和光市', '奈良県 生駒市', '神奈川県 川崎市 麻生区', '千葉県 流山市') GROUP BY area_name) ORDER BY ratio ASC
```

```sql id=trend
SELECT year, MAX(CASE WHEN area_name = '東京都 千代田区' THEN v END) AS chiyoda, MAX(CASE WHEN area_name = '東京都 中央区' THEN v END) AS chuo, MAX(CASE WHEN area_name = '東京都 港区' THEN v END) AS minato, MAX(CASE WHEN area_name = '大阪府 大阪市 中央区' THEN v END) AS osaka FROM (SELECT area_name, year, TRY_CAST(value AS DOUBLE) v FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year <= 2020) GROUP BY year ORDER BY year
```

```sql id=cbd_change
WITH d AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A6107' THEN TRY_CAST(value AS DOUBLE) END) AS day_pop, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS night_pop FROM e_stat.ssds.a_municipal_population WHERE cat01 IN ('A6107', 'A1101') AND area_name IN ('東京都 千代田区', '東京都 中央区', '東京都 港区', '大阪府 大阪市 中央区') AND year IN (2000, 2020) GROUP BY area_name, year) SELECT a.area_name AS area_name, ROUND((b.day_pop / a.day_pop - 1) * 100, 1) AS day_chg, ROUND((b.night_pop / a.night_pop - 1) * 100, 1) AS night_chg, a.day_pop AS day_2000, b.day_pop AS day_2020, a.night_pop AS night_2000, b.night_pop AS night_2020 FROM d a JOIN d b ON a.area_name = b.area_name AND a.year = 2000 AND b.year = 2020 ORDER BY day_chg
```
