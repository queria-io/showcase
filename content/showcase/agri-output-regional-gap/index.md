---
title: 耕地は23%減り、1haあたりの農業産出額は38%増えた
description: 1975年から2023年の都道府県別データで農業産出額を集計しました。全国の産出額は1984年の約11.7兆円がピークで、2023年は約9.6兆円です。耕地1haあたりの産出額は約161万円から約222万円に上がり、北海道が全国の14%超を占めています。
publishedAt: 2026-04-06
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 農業
  - 食料
  - 地域格差
  - 経済
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系 都道府県データ
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures
    publisher: 総務省統計局
  - title: 生産農業所得統計
    url: https://www.maff.go.jp/j/tokei/kouhyou/nougyou_sansyutu/
    publisher: 農林水産省
agentHint: 農業産出額(C3101)を1990年と2023年で都道府県別に比べて、増加率が高い県と低い県を出して
---

日本の農業産出額は1984年の約11.7兆円がピークで、2023年は約9.6兆円でした。ピーク時の約82%です。同じ期間に耕地面積は1975年から約23%減りましたが、耕地1haあたりの産出額は約161万円から約222万円へ約38%上がっています。都道府県別では北海道が約1兆3,478億円で全国の14%超を占め、2位の鹿児島県の約2.5倍です。

使ったのは e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県別経済データで、農業産出額（指標コード `C3101`、単位は百万円）と耕地面積（`C3107`、単位はha）を1975年から2023年まで集計しました。

## 全国の農業産出額は1984年がピークで、2023年はその約82%

全国の農業産出額の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "mark": {"type": "bar", "color": "#4ade80"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "agri_output", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "agri_output",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "農業産出額（百万円）", "grid": true}
        }
      }
    }
  ]
}
```

1984年に約11.7兆円でピークになった後、2010年代前半まで減少が続きました。2016年以降は増加に転じ、2023年は約9.6兆円です。ピーク時の約82%の水準で、2015年以降は大きな増減なく推移しています。

## 北海道の産出額は2位の鹿児島県の約2.5倍

2023年の都道府県別の農業産出額です。

```chart
{
  "height": 680,
  "layer": [
    {
      "data": {"name": "ranking"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "agri_output", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "agri_output",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "農業産出額（百万円）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null}
      }
    }
  ]
}
```

北海道が約1兆3,478億円で最も多く、全国合計の14%超を占めます。2位の鹿児島県（約5,438億円）の約2.5倍です。上位には鹿児島県・茨城県・千葉県・熊本県・宮崎県が並び、大阪府（約320億円）や東京都（約220億円）は最下位に近い位置にあります。

## 宮崎県・鹿児島県は1haあたり産出額が全国平均を上回り、北海道は下回る

都道府県ごとに、耕地面積と農業産出額の関係を散布図にしました。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "farmland", "type": "quantitative"},
          {"field": "agri_output", "type": "quantitative"}
        ],
        "x": {
          "field": "farmland",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "耕地面積（ha）", "grid": true}
        },
        "y": {
          "field": "agri_output",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "農業産出額（百万円）", "grid": true}
        },
        "color": {
          "field": "output_per_ha_10kyen",
          "type": "quantitative",
          "scale": {
            "range": [
              "rgb(128,0,38)",
              "rgb(189,0,38)",
              "rgb(227,26,28)",
              "rgb(252,78,42)",
              "rgb(253,141,60)",
              "rgb(254,178,76)",
              "rgb(254,217,118)",
              "rgb(255,237,160)",
              "rgb(255,255,204)"
            ]
          }
        }
      }
    },
    {
      "data": {"name": "scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "farmland",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "耕地面積（ha）", "grid": true}
        },
        "y": {
          "field": "agri_output",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "農業産出額（百万円）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    },
    {
      "data": {"values": [{"x": 0, "y": 0}, {"x": 1200000, "y": 2640000}]},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"x\"]) && isValid(datum[\"y\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 1,
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "x": {
          "field": "x",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "耕地面積（ha）", "grid": true}
        },
        "y": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "農業産出額（百万円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 10,
        "color": "#94a3b8"
      },
      "encoding": {
        "x": {"datum": 500000, "type": "quantitative"},
        "y": {"datum": 1100000, "type": "quantitative"},
        "text": {"value": "全国平均"}
      }
    }
  ]
}
```

対角の破線は全国平均の1haあたり産出額で、線より上の県は平均より高く、下の県は平均より低くなります。北海道は耕地面積（約114万ha）も産出額も最も大きいものの、破線の下にあり、1haあたり産出額は全国平均を下回ります。宮崎県・鹿児島県などは破線の上にあり、耕地面積が少なくても1haあたり産出額が高くなっています。1haあたり産出額は、耕地をほとんど使わない畜産や施設園芸の比重が高い県で高く出るため、農業の形態の違いも含んだ値です。

## 耕地1haあたりの産出額は、1975年の約161万円から2023年の約222万円に上がった

耕地面積と農業産出額の長期推移を比較し、耕地1haあたりの産出額を計算しました。

```chart
{
  "layer": [
    {
      "data": {"name": "productivity"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"output_per_ha_10kyen\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#22c55e"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "output_per_ha_10kyen", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "output_per_ha_10kyen",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "耕地1haあたり産出額（万円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

耕地1haあたりの農業産出額は1975年の約161万円から長期的に上がり、2023年には約222万円になりました。2016年以降の上昇が大きく、農地の集約や高付加価値の作物への移行が関係していると考えられます。耕地面積が減っても面積あたりの産出額が上がったことで、全国の産出額の減少が抑えられています。

## まとめ

- 全国の農業産出額は1984年のピーク後に減少し、2023年はピーク時の約82%の水準にある
- 北海道は全国の産出額の14%超を占め、2位の鹿児島県の約2.5倍
- 耕地面積は1975年から約23%減ったが、1haあたり産出額は約38%上がった
- 宮崎県や鹿児島県など畜産が盛んな県は、耕地面積に対して産出額が大きい

農林水産省の「[生産農業所得統計](https://www.maff.go.jp/j/tokei/kouhyou/nougyou_sansyutu/)」では都道府県別・品目別の詳細データが公表されており、地域農業の振興策や食料安全保障の検討に使われています。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県別経済データ（`c_pref_economy`）を2026-07-11時点で集計しています。対象は全国と47都道府県の1975年から2023年です。

Queriaは、e-Statをはじめとする官公庁のデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別経済データのテーブル](/datasets/queria/e_stat/ssds/c_pref_economy)から、地域や年次を切り替えて同じ集計ができます。

```sql id=trend
SELECT year, MAX(TRY_CAST(value AS DOUBLE)) AS agri_output FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3101' AND area_name = '全国' AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=ranking
SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS agri_output FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3101' AND area_name != '全国' AND year = 2023 GROUP BY area_name ORDER BY agri_output DESC
```

```sql id=scatter
WITH agri AS ( SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS agri_output FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3101' AND year = 2023 GROUP BY area_name ), land AS ( SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS farmland FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3107' AND year = 2023 GROUP BY area_name ) SELECT agri.area_name, land.farmland, agri.agri_output, ROUND(agri.agri_output * 100.0 / land.farmland) AS output_per_ha_10kyen, nat.national_slope FROM agri JOIN land ON agri.area_name = land.area_name CROSS JOIN ( SELECT ROUND(a.v / l.v, 2) AS national_slope FROM (SELECT MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3101' AND year = 2023 AND area_name = '全国') a, (SELECT MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3107' AND year = 2023 AND area_name = '全国') l ) nat WHERE land.farmland > 0 AND agri.area_name != '全国' ORDER BY agri_output DESC
```

```sql id=productivity
WITH agri AS ( SELECT year, MAX(TRY_CAST(value AS DOUBLE)) AS agri_output FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3101' AND area_name = '全国' AND year <= 2023 GROUP BY year ), land AS ( SELECT year, MAX(TRY_CAST(value AS DOUBLE)) AS farmland FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3107' AND area_name = '全国' AND year <= 2023 GROUP BY year ) SELECT agri.year, agri.agri_output, land.farmland, ROUND(agri.agri_output * 100.0 / land.farmland) AS output_per_ha_10kyen FROM agri JOIN land ON agri.year = land.year ORDER BY agri.year
```
