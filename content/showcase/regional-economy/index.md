---
title: 住民の所得が高い県ほど、自治体が使えるお金は少ない
description: 納税者1人あたり課税対象所得と1人あたり地方税の相関は+0.84。地方交付税を足すと-0.56へ反転し、所得上位10の都府県で財源も上位10に入るものは0になります（2022年度）
publishedAt: 2026-02-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 経済
  - 地方財政
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 統計でみる都道府県・市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 地方財政状況調査関係資料
    url: https://www.soumu.go.jp/iken/jokyo_chousa_shiryo.html
    publisher: 総務省
  - title: 市町村税課税状況等の調
    url: https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09.html
    publisher: 総務省
agentHint: e_stat.ssds.d_municipal_administration の市町村財政の地方税（D320101）と地方交付税（D320108）を、e_stat.ssds.a_municipal_population の総人口（A1101）で割って市区町村ごとの1人あたり財源を出して、e_stat.ssds.c_municipal_economy の課税対象所得（C120110）と納税義務者数（C120120）から作る所得と並べ、都道府県で見えた逆転が市区町村でも起きているか調べて
socialAnnounce: |-
  住民の所得が高い県ほど、自治体が使えるお金は少ない。

  所得と地方税の相関は+0.84。地方交付税を足すと-0.56へ反転し、所得上位10の都府県で財源も上位10に入るものは0でした。
  1985年度から38年、一度も逆転は解けていません。
---

2022年度の都道府県データで、納税者1人あたりの課税対象所得と住民1人あたりの地方税の相関は+0.843でした。地方交付税を足すと相関は-0.562になり、順位どうしでは-0.802で、所得の順位と財源の順位はほぼ逆になります。所得の上位10の都府県のうち、住民1人あたりの財源でも上位10に入る都府県は0でした。この関係は1985年度から2022年度まで変わっていません。

使うのは e-Stat の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)の2022年度の都道府県データです。住民の所得は、納税義務者（所得割）1人あたりの課税対象所得です。所得割の課税を受けない人は分子にも分母にも入らないので、県民の平均所得とは異なります。自治体の財源は、使い道を自治体が決められる地方税と地方交付税の合計で、2022年度の一般財源の95.5%を占めます。

## 地方税は所得の高い県ほど多く、地方交付税を足すと所得の高い県ほど少なくなる

横軸に住民の所得、縦軸に住民1人あたりの金額をとり、地方税だけの場合と、地方交付税を足した場合を重ねました。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "income_vs_resources"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "income", "type": "quantitative"},
          {"field": "tax_pc", "type": "quantitative"}
        ],
        "x": {
          "field": "income",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "納税者1人あたり課税対象所得（千円）", "grid": true}
        },
        "y": {
          "field": "tax_pc",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "住民1人あたりの金額（千円）", "grid": true}
        },
        "color": {
          "datum": "地方税のみ",
          "type": "nominal",
          "scale": {"domain": ["地方税のみ", "地方税＋地方交付税"], "range": ["#2563eb", "#ea580c"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "income_vs_resources"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "income", "type": "quantitative"},
          {"field": "total_pc", "type": "quantitative"}
        ],
        "x": {
          "field": "income",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "納税者1人あたり課税対象所得（千円）", "grid": true}
        },
        "y": {
          "field": "total_pc",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "住民1人あたりの金額（千円）", "grid": true}
        },
        "color": {
          "datum": "地方税＋地方交付税",
          "type": "nominal",
          "scale": {"domain": ["地方税のみ", "地方税＋地方交付税"], "range": ["#2563eb", "#ea580c"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

青い点は右上がりです。納税者1人あたり課税対象所得と住民1人あたり地方税の相関は+0.843で、所得が高い県ほど地方税も多く入ります。オレンジの点は右下がりで、地方交付税を足すと相関は-0.562になります。順位どうしの相関は-0.802で、所得の順位と財源の順位はほぼ逆です。

この2つの相関係数は、右端に離れている東京都の影響を強く受けます。東京都を除いた46道府県では、地方税との相関は+0.693に下がり、財源との相関は-0.799に強まります。どちらも向きは変わりません。

```sql
SELECT * FROM correlations
```

```sql
SELECT * FROM outlier_check
```

所得の上位10の都府県のうち、住民1人あたりの財源でも上位10に入る都府県は0です。6都府県は財源では下位10に入り、所得の下位10県のうち5県が財源で上位10に入ります。

## 財源の下位10県には、大都市のある府県が並ぶ

住民1人あたりの地方税と地方交付税の合計で、47都道府県を並べます。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "resource_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "total_pc", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "total_pc",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "住民1人あたり地方税＋地方交付税（千円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "resource_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "total_pc", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "total_pc",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "住民1人あたり地方税＋地方交付税（千円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "resource_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "total_pc", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "total_pc",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "住民1人あたり地方税＋地方交付税（千円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

1位は島根県の799.6千円、最下位は埼玉県の366.2千円で、2.18倍の差があります。下位10は茨城県・栃木県・兵庫県・福岡県・静岡県・大阪府・愛知県・千葉県・神奈川県・埼玉県です。所得の上位5都県は東京都・神奈川県・愛知県・兵庫県・千葉県で、東京都を除く4県がこの下位10に入っています。

東京都は、地方税が住民1人あたり581.4千円で全国1位ですが、地方交付税は5.8千円しか入らないので、合計では18位です。

```sql
SELECT * FROM rank_table
```

## 所得と財源の順位が逆になる関係は、1985年度から続いている

所得と財源の両方の指標がある1985年度から、年ごとに47都道府県の所得の順位と、地方税の順位・財源の順位の相関を計算しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "corr_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tax_corr\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tax_corr", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "tax_corr",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "順位どうしの相関", "grid": true}
        },
        "color": {
          "datum": "所得順位と地方税順位",
          "type": "nominal",
          "scale": {"domain": ["所得順位と地方税順位", "所得順位と財源順位"], "range": ["#2563eb", "#ea580c"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "corr_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_corr\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ea580c",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_corr", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "total_corr",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "順位どうしの相関", "grid": true}
        },
        "color": {
          "datum": "所得順位と財源順位",
          "type": "nominal",
          "scale": {"domain": ["所得順位と地方税順位", "所得順位と財源順位"], "range": ["#2563eb", "#ea580c"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

順位は値が小さいほど上位なので、正の相関は所得が高い県ほど順位も高いことを表します。地方税との相関は38年間ずっと正で、財源との相関は一度も正になっていません。財源との相関は1985年度の-0.608から強まり、2009年度以降は-0.78から-0.83の範囲にあります。

## 住民1人あたりの財源が多い県は、住民1人あたりの基準財政需要額が大きい県

この関係は、地方交付税の算定方法によるものです。地方交付税の大部分を占める普通交付税は、基準財政需要額が基準財政収入額を超える自治体に、その差額を基本として交付されます（残りは災害などの事情に応じた特別交付税です）。基準財政需要額は人口に加えて面積や道路の延長なども使って計算されるので、人口が少なく面積の広い県ほど、住民1人あたりの額が大きくなります。

```sql
SELECT * FROM need_summary
```

```sql
SELECT * FROM need_extremes
```

住民1人あたりの基準財政需要額は、島根県の719.2千円から神奈川県の299.7千円まで2.4倍の幅があり、可住地1平方キロあたり人口の対数との相関は-0.748です。人口密度が低い県ほど、同じ水準の行政サービスを提供するのに必要な額が大きく見積もられます。財源はこの需要額との差を埋めるように配られるので、住民1人あたりの財源が多い県で、行政サービスが手厚いとは言えません。

所得の高い県は大都市圏に多く、行政の費用が多くかかる県は人口密度の低い県に多くあります。地方交付税は費用の多い県に多く配られるので、所得と財源の順位は38年間逆になっています。

## まとめ

- 納税者1人あたり課税対象所得と住民1人あたり地方税の相関は+0.843で、所得の高い県ほど地方税が多い
- 地方交付税を足すと相関は-0.562、順位どうしでは-0.802で、順位はほぼ逆になる。所得の上位10の都府県のうち、財源でも上位10に入るのは0
- 住民1人あたりの財源は島根県の799.6千円が最も多く、埼玉県の366.2千円が最も少なく、2.18倍の差がある。東京都は地方税が1位でも地方交付税がほとんど入らず18位
- 所得と財源の順位が逆になる関係は1985年度から2022年度まで続き、2009年度以降の相関は-0.78から-0.83
- 住民1人あたりの財源が多い県は、住民1人あたりの基準財政需要額が大きい県で、行政サービスが手厚いことを表してはいない
- 相関係数は東京都の影響を受ける。東京都を除く46道府県では、地方税との相関が+0.693、財源との相関が-0.799

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)（総務省統計局）の `e_stat.ssds.d_pref_administration`、`e_stat.ssds.c_pref_economy`、`e_stat.ssds.a_pref_population`、`e_stat.ssds.b_pref_land` を2026年9月2日時点で集計しています。使った分類コードは、地方税が D310101（都道府県財政）と D320101（市町村財政）、地方交付税が D310103 と D320108、基準財政需要額が D2106 と D2206、課税対象所得が C120110、納税義務者数（所得割）が C120120、総人口が A1101、可住地面積が B1103、割合の分母にした一般財源が D2109（都道府県財政）と D2209（市町村財政）です。金額の単位はいずれも千円で、都道府県分と市町村分を合計しています。

元データは総務省の[地方財政状況調査](https://www.soumu.go.jp/iken/jokyo_chousa_shiryo.html)と[市町村税課税状況等の調](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09.html)です。指標の定義は[項目定義 C 経済基盤](https://www.e-stat.go.jp/koumoku/koumoku_teigi/C)・[項目定義 D 行政基盤](https://www.e-stat.go.jp/koumoku/koumoku_teigi/D)・[項目定義 A 人口・世帯](https://www.e-stat.go.jp/koumoku/koumoku_teigi/A)によります。財政の金額は年度の決算額、課税対象所得と納税義務者数は7月1日現在の課税状況（課税の対象は前年の所得）、総人口は10月1日現在の値です。財政の3系列は2022年度が最新で、課税対象所得は2024年度まで入っています。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の行財政データのテーブル](/datasets/queria/e_stat/ssds/d_pref_administration)から、任意の都道府県の地方税・地方交付税・基準財政需要額を取り出せます。

```sql
SELECT * FROM coverage
```

```sql
SELECT * FROM revenue_share
```

```sql id=income_vs_resources
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101') THEN TRY_CAST(value AS DOUBLE) END) AS tax, SUM(CASE WHEN cat01 IN ('D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS grants FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), inc AS ( SELECT area_name, SUM(CASE WHEN cat01 = 'C120110' THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 = 'C120120' THEN TRY_CAST(value AS DOUBLE) END) AS income FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C120110', 'C120120') AND year = 2022 AND area_name <> '全国' GROUP BY area_name ) SELECT f.area_name, ROUND(i.income, 1) AS income, ROUND(f.tax / p.people, 1) AS tax_pc, ROUND((f.tax + f.grants) / p.people, 1) AS total_pc FROM fin f JOIN pop p ON p.area_name = f.area_name JOIN inc i ON i.area_name = f.area_name ORDER BY income DESC
```

```sql id=correlations
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101') THEN TRY_CAST(value AS DOUBLE) END) AS tax, SUM(CASE WHEN cat01 IN ('D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS grants FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), inc AS ( SELECT area_name, SUM(CASE WHEN cat01 = 'C120110' THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 = 'C120120' THEN TRY_CAST(value AS DOUBLE) END) AS income FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C120110', 'C120120') AND year = 2022 AND area_name <> '全国' GROUP BY area_name ), base AS ( SELECT i.income, f.tax / p.people AS tax_pc, (f.tax + f.grants) / p.people AS total_pc, RANK() OVER (ORDER BY i.income DESC) AS income_rank, RANK() OVER (ORDER BY (f.tax + f.grants) / p.people DESC) AS total_rank FROM fin f JOIN pop p ON p.area_name = f.area_name JOIN inc i ON i.area_name = f.area_name ) SELECT COUNT(*) AS 都道府県数, ROUND(CORR(income, tax_pc), 3) AS 所得と地方税の相関, ROUND(CORR(income, total_pc), 3) AS 所得と地方税プラス交付税の相関, ROUND(CORR(income_rank, total_rank), 3) AS 所得順位と財源順位の相関, SUM(CASE WHEN income_rank <= 10 AND total_rank <= 10 THEN 1 ELSE 0 END) AS 所得も財源も上位10の県数, SUM(CASE WHEN income_rank <= 10 AND total_rank >= 38 THEN 1 ELSE 0 END) AS 所得上位10かつ財源下位10の県数, SUM(CASE WHEN income_rank >= 38 AND total_rank <= 10 THEN 1 ELSE 0 END) AS 所得下位10かつ財源上位10の県数, ROUND(MAX(total_pc) / MIN(total_pc), 2) AS 財源の最大最小比 FROM base
```

```sql id=resource_top
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101', 'D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS resources FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), ranked AS ( SELECT f.area_name, ROUND(f.resources / p.people, 1) AS total_pc, ROW_NUMBER() OVER (ORDER BY f.resources / p.people DESC, f.area_name) AS rn FROM fin f JOIN pop p ON p.area_name = f.area_name ) SELECT area_name, total_pc FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=resource_mid
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101', 'D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS resources FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), ranked AS ( SELECT f.area_name, ROUND(f.resources / p.people, 1) AS total_pc, ROW_NUMBER() OVER (ORDER BY f.resources / p.people DESC, f.area_name) AS rn FROM fin f JOIN pop p ON p.area_name = f.area_name ) SELECT area_name, total_pc FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=resource_bottom
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101', 'D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS resources FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), ranked AS ( SELECT f.area_name, ROUND(f.resources / p.people, 1) AS total_pc, ROW_NUMBER() OVER (ORDER BY f.resources / p.people DESC, f.area_name) AS rn FROM fin f JOIN pop p ON p.area_name = f.area_name ) SELECT area_name, total_pc FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=rank_table
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101') THEN TRY_CAST(value AS DOUBLE) END) AS tax, SUM(CASE WHEN cat01 IN ('D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS grants FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), inc AS ( SELECT area_name, SUM(CASE WHEN cat01 = 'C120110' THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 = 'C120120' THEN TRY_CAST(value AS DOUBLE) END) AS income FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C120110', 'C120120') AND year = 2022 AND area_name <> '全国' GROUP BY area_name ), base AS ( SELECT f.area_name, i.income, f.tax / p.people AS tax_pc, f.grants / p.people AS grant_pc, (f.tax + f.grants) / p.people AS total_pc FROM fin f JOIN pop p ON p.area_name = f.area_name JOIN inc i ON i.area_name = f.area_name ) SELECT area_name AS 都道府県, RANK() OVER (ORDER BY income DESC) AS 所得順位, ROUND(income, 1) AS 納税者1人あたり課税対象所得, RANK() OVER (ORDER BY tax_pc DESC) AS 地方税順位, ROUND(tax_pc, 1) AS 住民1人あたり地方税, ROUND(grant_pc, 1) AS 住民1人あたり地方交付税, RANK() OVER (ORDER BY total_pc DESC) AS 財源順位, ROUND(total_pc, 1) AS 住民1人あたり財源 FROM base ORDER BY 所得順位
```

```sql id=corr_trend
WITH fin AS ( SELECT year, area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101') THEN TRY_CAST(value AS DOUBLE) END) AS tax, SUM(CASE WHEN cat01 IN ('D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS grants FROM e_stat.ssds.d_pref_administration WHERE area_name <> '全国' GROUP BY year, area_name ), pop AS ( SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' ), inc AS ( SELECT year, area_name, SUM(CASE WHEN cat01 = 'C120110' THEN TRY_CAST(value AS DOUBLE) END) / NULLIF(SUM(CASE WHEN cat01 = 'C120120' THEN TRY_CAST(value AS DOUBLE) END), 0) AS income FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C120110', 'C120120') AND area_name <> '全国' GROUP BY year, area_name ), ranked AS ( SELECT f.year, RANK() OVER (PARTITION BY f.year ORDER BY i.income DESC) AS income_rank, RANK() OVER (PARTITION BY f.year ORDER BY f.tax / p.people DESC) AS tax_rank, RANK() OVER (PARTITION BY f.year ORDER BY (f.tax + f.grants) / p.people DESC) AS total_rank FROM fin f JOIN pop p ON p.year = f.year AND p.area_name = f.area_name JOIN inc i ON i.year = f.year AND i.area_name = f.area_name WHERE f.year <= 2022 AND f.tax IS NOT NULL AND f.grants IS NOT NULL AND i.income IS NOT NULL AND p.people > 0 ) SELECT year, ROUND(CORR(income_rank, tax_rank), 3) AS tax_corr, ROUND(CORR(income_rank, total_rank), 3) AS total_corr FROM ranked GROUP BY year HAVING COUNT(*) = 47 ORDER BY year
```

```sql id=need_summary
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D2106', 'D2206') THEN TRY_CAST(value AS DOUBLE) END) AS need, SUM(CASE WHEN cat01 IN ('D310101', 'D320101', 'D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS resources FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), land AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) / 100.0 AS habitable_km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area_name <> '全国' ), base AS ( SELECT f.area_name, f.need / p.people AS need_pc, f.resources / p.people AS total_pc, p.people / l.habitable_km2 AS density FROM fin f JOIN pop p ON p.area_name = f.area_name JOIN land l ON l.area_name = f.area_name ) SELECT ROUND(MAX(need_pc), 1) AS 基準財政需要額の最大, ROUND(MIN(need_pc), 1) AS 基準財政需要額の最小, ROUND(MAX(need_pc) / MIN(need_pc), 2) AS 最大最小比, ROUND(CORR(LN(density), need_pc), 3) AS 可住地人口密度対数との相関, ROUND(CORR(need_pc, total_pc), 3) AS 財源との相関 FROM base
```

```sql id=need_extremes
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D2106', 'D2206') THEN TRY_CAST(value AS DOUBLE) END) AS need FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), land AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) / 100.0 AS habitable_km2 FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2022 AND area_name <> '全国' ), ranked AS ( SELECT f.area_name, ROUND(f.need / p.people, 1) AS need_pc, ROUND(p.people / l.habitable_km2, 0) AS density, ROW_NUMBER() OVER (ORDER BY f.need / p.people DESC, f.area_name) AS rn FROM fin f JOIN pop p ON p.area_name = f.area_name JOIN land l ON l.area_name = f.area_name ) SELECT area_name AS 都道府県, need_pc AS 住民1人あたり基準財政需要額, density AS 可住地1平方キロあたり人口 FROM ranked WHERE rn <= 5 OR rn > 42 ORDER BY rn
```

```sql id=outlier_check
WITH fin AS ( SELECT area_name, SUM(CASE WHEN cat01 IN ('D310101', 'D320101') THEN TRY_CAST(value AS DOUBLE) END) AS tax, SUM(CASE WHEN cat01 IN ('D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) AS grants FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国' GROUP BY area_name ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2022 AND area_name <> '全国' ), inc AS ( SELECT area_name, SUM(CASE WHEN cat01 = 'C120110' THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 = 'C120120' THEN TRY_CAST(value AS DOUBLE) END) AS income FROM e_stat.ssds.c_pref_economy WHERE cat01 IN ('C120110', 'C120120') AND year = 2022 AND area_name <> '全国' GROUP BY area_name ), base AS ( SELECT f.area_name, i.income, f.tax / p.people AS tax_pc, (f.tax + f.grants) / p.people AS total_pc FROM fin f JOIN pop p ON p.area_name = f.area_name JOIN inc i ON i.area_name = f.area_name ) SELECT '47都道府県' AS 対象, ROUND(CORR(income, tax_pc), 3) AS 所得と地方税の相関, ROUND(CORR(income, total_pc), 3) AS 所得と財源の相関 FROM base UNION ALL SELECT '東京都を除く46道府県', ROUND(CORR(income, tax_pc), 3), ROUND(CORR(income, total_pc), 3) FROM base WHERE area_name <> '東京都'
```

```sql id=revenue_share
SELECT ROUND(SUM(CASE WHEN cat01 IN ('D310101', 'D320101') THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 IN ('D2109', 'D2209') THEN TRY_CAST(value AS DOUBLE) END) * 100, 1) AS 地方税の割合, ROUND(SUM(CASE WHEN cat01 IN ('D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 IN ('D2109', 'D2209') THEN TRY_CAST(value AS DOUBLE) END) * 100, 1) AS 地方交付税の割合, ROUND(SUM(CASE WHEN cat01 IN ('D310101', 'D320101', 'D310103', 'D320108') THEN TRY_CAST(value AS DOUBLE) END) / SUM(CASE WHEN cat01 IN ('D2109', 'D2209') THEN TRY_CAST(value AS DOUBLE) END) * 100, 1) AS 合計 FROM e_stat.ssds.d_pref_administration WHERE year = 2022 AND area_name <> '全国'
```

```sql id=coverage
SELECT table_name AS テーブル, cat01 AS 分類コード, item_name AS 指標, min_year AS 収録開始, max_year AS 収録最終, year_count AS 収録年数 FROM e_stat.ssds.series_coverage WHERE (table_name = 'd_pref_administration' AND cat01 IN ('D310101', 'D320101', 'D310103', 'D320108', 'D2106', 'D2206', 'D2109', 'D2209')) OR (table_name = 'c_pref_economy' AND cat01 IN ('C120110', 'C120120')) OR (table_name = 'a_pref_population' AND cat01 = 'A1101') OR (table_name = 'b_pref_land' AND cat01 = 'B1103') ORDER BY table_name, cat01
```
