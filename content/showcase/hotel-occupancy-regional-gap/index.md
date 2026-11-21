---
title: ホテルや旅館の客室稼働率の県の差は、2019年の25.3ポイントから2024年は22.6ポイントに縮んだ
description: 客室稼働率の最も高い県と低い県の差は、2019年の25.3ポイントから2024年は22.6ポイントに縮みました。2019年に稼働率が高かった県ほど、泊められる人数が大きく増え、稼働率が下がっています。
publishedAt: 2026-03-04
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 観光
  - 宿泊
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 宿泊旅行統計調査
    url: https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html
    publisher: 観光庁
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（G 文化・スポーツ）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/G
    publisher: 総務省統計局
agentHint: 延べ宿泊者数（G7101）を定員稼働率（G7104）で割って受け入れ枠を出し、2011年から2024年まで都道府県別に並べて、枠の伸びが速まった年を県ごとに確かめて
socialAnnounce: |-
  ホテルや旅館の客室稼働率は、2019年は東京都と長野県で25.3ポイント差。
  2024年は22.6ポイント差に縮みました。

  縮めたのは東京都など2019年に稼働率が高かった県の低下です。2019年に部屋が埋まっていた県ほど、泊められる人数が増えていました。
---

ホテルや旅館の客室稼働率は、2019年は最も高い東京都（83.4%）と最も低い長野県（58.1%）で25.3ポイント違いました。2024年は東京都が80.4%、長野県が57.8%で、差は22.6ポイントに縮んでいます。2019年に稼働率が中央値以上だった24都道府県は、2024年にすべて稼働率が下がりました。これらの県ほど泊められる人数（受け入れ枠）が大きく増えており、2019年の稼働率と受け入れ枠の伸びの相関は0.66でした。

新型コロナで減ったホテルや旅館などの宿泊者は、2024年にコロナ前を上回りました。従業者10人以上の施設に泊まった延べ人数は5.41億人泊で、2019年の5.01億人泊より8.0%多くなっています。

## 2024年の客室稼働率の県の差は、2011〜2019年のどの年よりも小さい

使うのは e-Stat の「[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)」の都道府県別の文化・スポーツデータ（`g_pref_culture`）です。元は観光庁の[宿泊旅行統計調査](https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html)で、宿泊に関する次の指標が入っています。

| コード  | 内容                                                    |
| ------- | ------------------------------------------------------- |
| G7101   | 延べ宿泊者数                                            |
| G710101 | 延べ宿泊者数（県内）                                    |
| G710102 | 延べ宿泊者数（県外）                                    |
| G710103 | 延べ宿泊者数（旅館）。G710104〜G710106 はホテルの種類別 |
| G7102   | 外国人延べ宿泊者数。G710201〜G710204 は国・地域別       |
| G7103   | 実宿泊者数                                              |
| G7104   | 定員稼働率（延べ宿泊者数 ÷ 収容人数の年間合計）         |
| G7105   | 客室稼働率（利用された客室数 ÷ 客室数の年間合計）       |

どの指標も従業者10人以上の施設だけの値です。観光庁が発表の見出しに使う延べ宿泊者数は従業者10人未満の施設も含むので、この記事の数字はそれより小さくなります。

客室稼働率（`G7105`）の最も高い県と最も低い県の差を、2011年から年ごとに並べます。

```chart
{
  "layer": [
    {
      "data": {"name": "spread_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"gap\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "最高と最低の差（ポイント）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

2019年は東京都の83.4%と長野県の58.1%で、差は25.3ポイントでした。2024年も最高は東京都、最低は長野県ですが、東京都が80.4%に下がり、長野県は57.8%でほぼ変わらず、差は22.6ポイントです。2011〜2019年の差は24.1〜33.1ポイントで、2024年はどの年よりも小さくなっています。47都道府県のばらつき（標準偏差）でも、2024年の5.17は2011〜2019年の5.83〜7.31を下回ります。2020〜2022年には差がさらに小さい年がありますが、どの県も稼働率が大きく下がった中での差です。

```sql
SELECT year AS 年, top_pref AS 最も高い, top_occ AS "最高（%）", bottom_pref AS 最も低い, bottom_occ AS "最低（%）", gap AS "差（ポイント）", sd AS 標準偏差 FROM spread_trend
```

## 2019年に稼働率が中央値以上だった24都道府県は、2024年にすべて下がった

2019年と2024年の客室稼働率を県ごとに比較します。横軸が2019年の稼働率、縦軸が2024年までの増減です。

```chart
{
  "layer": [
    {
      "data": {"name": "occ_change"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "occ_2019", "type": "quantitative"},
          {"field": "diff", "type": "quantitative"}
        ],
        "x": {
          "field": "occ_2019",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年の客室稼働率（%）", "grid": true}
        },
        "y": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年から2024年の増減（ポイント）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "occ_change"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "occ_2019",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年の客室稼働率（%）", "grid": true}
        },
        "y": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年から2024年の増減（ポイント）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

2019年の稼働率の中央値は66.2%（群馬県）でした。それ以上だった24都道府県は、2024年にすべて稼働率が下がっています。下がり幅が最も大きいのは沖縄県の8.9ポイントで、佐賀県の7.4ポイント、鹿児島県の6.0ポイントが続きます。

上がったのは島根県（+6.6ポイント）、富山県（+5.6ポイント）、石川県（+5.4ポイント）、山口県（+3.2ポイント）、滋賀県（+2.9ポイント）、栃木県（+1.5ポイント）の6県で、2019年の稼働率はいずれも65.6%（石川県）以下でした。宮崎県は2019年も2024年も62.2%です。

```sql
SELECT * FROM occ_change_summary
```

2019年の水準と増減の相関は−0.47です。高かった値が次に下がることは一時的な需要の反動でも起きるので、この相関だけでは下がった理由は判定できません。

## 2019年に稼働率が高かった県ほど、泊められる人数が増えた

定員稼働率（`G7104`）は、延べ宿泊者数を「収容人数×日数」の年間合計で割った値です。延べ宿泊者数を定員稼働率で割ると、施設が1年間に泊められる延べ人数を計算できます。この記事ではこれを受け入れ枠と呼びます。受け入れ枠は従業者10人以上の施設の収容人数を合計した値なので、従業者が増えて10人に達した施設の分も、枠の増加に含まれます。

全国の宿泊者と受け入れ枠の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"capacity_oku\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "capacity_oku", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "capacity_oku",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "億人泊", "grid": true}
        },
        "color": {
          "datum": "受け入れ枠",
          "type": "nominal",
          "scale": {"domain": ["受け入れ枠", "延べ宿泊者数"], "range": ["#94a3b8", "#3b82f6"]},
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"stays_oku\"]) ? 0 : 1",
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
          {"field": "stays_oku", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "stays_oku",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "億人泊", "grid": true}
        },
        "color": {
          "datum": "延べ宿泊者数",
          "type": "nominal",
          "scale": {"domain": ["受け入れ枠", "延べ宿泊者数"], "range": ["#94a3b8", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

受け入れ枠は2018年の8.82億人泊から2019年に9.67億人泊へ増えました。宿泊者が半分近くに減った2020〜2021年も10.2億人泊台で、2024年は10.98億人泊です。2019年から2024年に、宿泊者は8.0%、受け入れ枠は13.5%増えました。

都道府県ごとに、2019年の客室稼働率と、2024年までの受け入れ枠の増減率を並べます。

```chart
{
  "layer": [
    {
      "data": {"name": "capacity"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "occ_2019", "type": "quantitative"},
          {"field": "capacity_growth", "type": "quantitative"}
        ],
        "x": {
          "field": "occ_2019",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年の客室稼働率（%）", "grid": true}
        },
        "y": {
          "field": "capacity_growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "受け入れ枠の増減率 2019→2024（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "capacity"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "occ_2019",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2019年の客室稼働率（%）", "grid": true}
        },
        "y": {
          "field": "capacity_growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "受け入れ枠の増減率 2019→2024（%）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

2019年の稼働率と受け入れ枠の伸びの相関は0.66で、稼働率が高かった県ほど枠が大きく増えています。宿泊者の伸びも2019年の稼働率が高かった県ほど大きくなっています（相関0.48）が、枠の伸びのほうが2019年の水準との関係が強くなっています。東京都は宿泊者が26.5%、枠が28.2%増えました。大阪府は宿泊者が20.5%、枠が30.6%、神奈川県は宿泊者が7.5%、枠が39.1%の増加です。沖縄県は宿泊者が8.4%減り、枠は8.9%増えました。宿泊者が増えたのに客室稼働率が下がった都道府県は19あります。

稼働率が上がった6県のうち、島根県・山口県・富山県の3県は、受け入れ枠が減っていました。島根県は宿泊者が1.6%、枠が8.2%減っています。受け入れ枠が増え、稼働率も上がった石川県・滋賀県・栃木県のうち、宿泊者の伸びが枠の伸びを上回ったのは石川県だけで、宿泊者は33.5%、枠は28.7%増えました。

客室稼働率は部屋の数、受け入れ枠は人数で測っているので、1室に泊まる人数が変わると2つの動きはずれます。滋賀県と栃木県は、人数では枠の伸びが宿泊者の伸びを上回りましたが、客室稼働率は上がりました。

```sql
SELECT * FROM capacity_summary
```

## 稼働率が上がった6県のうち3県は、受け入れ枠が減った県だった

2019年に部屋が埋まっていた県ほど泊められる人数が大きく増え、それらの県で稼働率が下がりました。稼働率が上がった6県の半分は、宿泊者がほとんど変わらないまま受け入れ枠が減った県です。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年10月10日時点で集計しています。元データは観光庁の[宿泊旅行統計調査](https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html)で、数値は1月から12月の暦年の値です。定義は[項目定義（G 文化・スポーツ）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/G)にあります。調査の対象名簿が2010年4〜6月期に切り替わっているので、2011年以降を比較しています。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の文化・観光統計テーブル](/datasets/queria/e_stat/ssds/g_pref_culture)から、任意の県の宿泊者数と稼働率を並べたり、旅館とホテルの種類ごとに宿泊者の回復を比較したりできます。

```sql id=spread_trend
WITH p AS (SELECT year, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS occ FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G7105' AND area_name != '全国' AND year BETWEEN 2011 AND 2024 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year, area_name) SELECT year, COUNT(*) AS n_pref, ARG_MAX(area_name, occ) AS top_pref, ROUND(MAX(occ), 1) AS top_occ, ARG_MIN(area_name, occ) AS bottom_pref, ROUND(MIN(occ), 1) AS bottom_occ, ROUND(ROUND(MAX(occ), 1) - ROUND(MIN(occ), 1), 1) AS gap, ROUND(STDDEV_POP(occ), 2) AS sd FROM p GROUP BY year ORDER BY year
```

```sql id=occ_change
WITH p AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) AS o19, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS o24 FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G7105' AND area_name != '全国' AND year IN (2019, 2024) GROUP BY area_name) SELECT area_name, ROUND(o19, 1) AS occ_2019, ROUND(o24, 1) AS occ_2024, ROUND(o24 - o19, 1) AS diff, RANK() OVER (ORDER BY o19 DESC) AS rank_2019 FROM p ORDER BY o19 DESC, area_name
```

```sql id=occ_change_summary
WITH p AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) AS o19, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS o24 FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G7105' AND area_name != '全国' AND year IN (2019, 2024) GROUP BY area_name), m AS (SELECT MEDIAN(o19) AS med FROM p) SELECT ROUND(m.med, 1) AS "2019年の中央値（%）", COUNT(*) FILTER (WHERE p.o19 >= m.med) AS 中央値以上の都道府県, COUNT(*) FILTER (WHERE p.o19 >= m.med AND p.o24 < p.o19) AS うち下がった, COUNT(*) FILTER (WHERE p.o24 < p.o19) AS 下がった都道府県, COUNT(*) FILTER (WHERE p.o24 = p.o19) AS 変わらない都道府県, COUNT(*) FILTER (WHERE p.o24 > p.o19) AS 上がった都道府県, ROUND(MAX(p.o19) FILTER (WHERE p.o24 > p.o19), 1) AS "上がった県の2019年の最高（%）", ROUND(CORR(p.o19, p.o24 - p.o19), 2) AS 相関_2019年の水準と増減 FROM p CROSS JOIN m GROUP BY m.med
```

```sql id=national_trend
WITH n AS (SELECT year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7101') AS stays, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7104') AS cap_rate FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G7101', 'G7104') AND area_name = '全国' AND year BETWEEN 2011 AND 2024 GROUP BY year) SELECT year, ROUND(stays / 100000000, 2) AS stays_oku, ROUND(stays / cap_rate * 100 / 100000000, 2) AS capacity_oku FROM n ORDER BY year
```

```sql id=capacity
WITH p AS (SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7101') AS stays, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7104') AS cap_rate, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7105') AS occ FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G7101', 'G7104', 'G7105') AND area_name != '全国' AND year IN (2019, 2024) GROUP BY area_name, year), w AS (SELECT area_name, MAX(occ) FILTER (WHERE year = 2019) AS o19, MAX(occ) FILTER (WHERE year = 2024) AS o24, MAX(stays) FILTER (WHERE year = 2019) AS s19, MAX(stays) FILTER (WHERE year = 2024) AS s24, MAX(stays / cap_rate * 100) FILTER (WHERE year = 2019) AS k19, MAX(stays / cap_rate * 100) FILTER (WHERE year = 2024) AS k24 FROM p GROUP BY area_name) SELECT area_name, ROUND(o19, 1) AS occ_2019, ROUND(o24 - o19, 1) AS occ_diff, ROUND((s24 / s19 - 1) * 100, 1) AS stays_growth, ROUND((k24 / k19 - 1) * 100, 1) AS capacity_growth FROM w ORDER BY o19 DESC, area_name
```

```sql id=capacity_summary
WITH p AS (SELECT area_name, year, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7101') AS stays, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7104') AS cap_rate, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G7105') AS occ FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G7101', 'G7104', 'G7105') AND year IN (2019, 2024) GROUP BY area_name, year), w AS (SELECT area_name, MAX(occ) FILTER (WHERE year = 2019) AS o19, MAX(occ) FILTER (WHERE year = 2024) AS o24, MAX(stays) FILTER (WHERE year = 2019) AS s19, MAX(stays) FILTER (WHERE year = 2024) AS s24, MAX(stays / cap_rate * 100) FILTER (WHERE year = 2019) AS k19, MAX(stays / cap_rate * 100) FILTER (WHERE year = 2024) AS k24 FROM p GROUP BY area_name) SELECT ROUND(MAX(s24 / s19 - 1) FILTER (WHERE area_name = '全国') * 100, 1) AS "全国の延べ宿泊者数の増減（%）", ROUND(MAX(k24 / k19 - 1) FILTER (WHERE area_name = '全国') * 100, 1) AS "全国の受け入れ枠の増減（%）", ROUND(MAX(k19) FILTER (WHERE area_name = '全国') / 100000000, 2) AS "全国の受け入れ枠 2019年（億人泊）", ROUND(MAX(k24) FILTER (WHERE area_name = '全国') / 100000000, 2) AS "全国の受け入れ枠 2024年（億人泊）", ROUND(CORR(o19, k24 / k19) FILTER (WHERE area_name != '全国'), 2) AS 相関_2019年の稼働率と枠の伸び, ROUND(CORR(o19, s24 / s19) FILTER (WHERE area_name != '全国'), 2) AS 相関_2019年の稼働率と宿泊者の伸び, COUNT(*) FILTER (WHERE area_name != '全国' AND s24 > s19 AND o24 < o19) AS 宿泊者が増えて稼働率が下がった, COUNT(*) FILTER (WHERE area_name != '全国' AND k24 < k19) AS 枠が減った, COUNT(*) FILTER (WHERE area_name != '全国' AND k24 < k19 AND o24 > o19) AS 枠が減って稼働率が上がった, COUNT(*) FILTER (WHERE area_name != '全国' AND o19 >= (SELECT MEDIAN(o19) FROM w WHERE area_name != '全国') AND k24 / k19 > s24 / s19) AS "2019年に中央値以上で定員稼働率が下がった" FROM w
```
