---
title: 建物火災が人口あたり2位の東京都は、火災で亡くなる人の割合が46位だった
description: 2019〜2023年の都道府県別データでは、人口あたりの建物火災が全国2位の東京都の火災死亡率は46位でした。比較した指標の中では、高齢化率の高い県ほど火災死亡率も高い傾向が最も強く出ます。
ogDescription: 人口あたりの建物火災が全国2位の東京都の火災死亡率は46位。高齢化率の高い県ほど、火災死亡率も高い傾向がありました。
publishedAt: 2026-05-26
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 火災
  - 防災
  - 高齢化
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系 Ｋ 安全
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010111
    publisher: 総務省統計局
  - title: 社会・人口統計体系 Ａ 人口・世帯
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010101
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義 K 安全
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/K
    publisher: 総務省統計局
  - title: 令和6年版 消防白書 火災による死者の状況
    url: https://www.fdma.go.jp/publication/hakusho/r6/chapter1/section1/para1/67986.html
    publisher: 総務省消防庁
agentHint: 2014〜2018年の5年分で、都道府県別の火災死亡者数を人口10万人あたりで出して、2019〜2023年の順位と比べて
socialAnnounce: |-
  2019〜2023年の都道府県別の火災データでは、人口あたりの建物火災が全国2位の東京都は、火災で亡くなる人の割合が46位でした。

  住宅防火の対策を厚くする地域の検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2019〜2023年の5年間で、人口あたりの建物火災が全国で2番目に多い東京都は、火災で亡くなる人の割合では47都道府県の46位でした。人口あたりの建物火災が最も少ない富山県は、火災で亡くなる人の割合では18位です。比較した指標の中で県ごとの火災死亡率と相関が最も強いのは高齢化率で、相関係数は0.76でした。人口あたりの建物火災の件数との相関（0.55）より強く、この差は1980年代から広がってきました。

この記事では、e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010111)の都道府県別データで、2019〜2023年の5年間の火災と死者を人口あたりの値にして比較しました。自治体や消防で住宅用火災警報器の点検の呼びかけや高齢者宅への防火訪問を計画するとき、火事の件数が多い地域を選ぶと、亡くなる人の多い地域が対象から外れることがあります。

## 東京都は建物火災が2位で、火災で亡くなる人の割合は46位

使うのは都道府県別の「安全」のテーブル（`k_pref_safety`）にある次の指標と、人口のテーブル（`a_pref_population`）の総人口（`A1101`）・65歳以上人口（`A1303`）です。火災の指標の出典は総務省消防庁の火災年報で、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/K)では1月から12月の暦年の集計です。

| コード  | 内容             | 定義                                                                                             |
| ------- | ---------------- | ------------------------------------------------------------------------------------------------ |
| `K2101` | 出火件数         | すべての火災の件数（建物・林野・車両・船舶・航空機・その他）                                     |
| `K2102` | 建物火災出火件数 | 建物かその中の物が焼けた火災の件数                                                               |
| `K2110` | 火災死亡者数     | すべての火災で亡くなった人。負傷から48時間以内に亡くなった人を含み、消防職員・消防団員は含まない |

1年ごとの死者は県によって少なく、年ごとの振れが大きいので、2019〜2023年の5年分を合計し、5年分の人口の合計で割って、1年あたり人口10万人あたりの値にしています。次の図は、横軸に人口あたりの建物火災の件数、縦軸に人口あたりの火災による死者をとったものです。

```chart
{
  "layer": [
    {
      "data": {"name": "pref"},
      "mark": {"type": "point", "color": "#ef4444", "opacity": 0.75, "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "building_rate", "type": "quantitative"},
          {"field": "death_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "building_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "建物火災の件数（1年・人口10万人あたり）", "grid": true}
        },
        "y": {
          "field": "death_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "火災による死者（1年・人口10万人あたり）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "building_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "建物火災の件数（1年・人口10万人あたり）", "grid": true}
        },
        "y": {
          "field": "death_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "火災による死者（1年・人口10万人あたり）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

東京都の建物火災は1年に人口10万人あたり20.5件で、青森県（22.7件）に次ぐ2位です。火災で亡くなる人は0.65人で46位でした。富山県は建物火災が11.5件で47位なのに、死者は1.52人で18位です。火災による死者を建物火災の件数で割ると（分子には建物以外の火災で亡くなった人も入ります）、建物火災1,000件あたり富山県は132.2人で1位、東京都は31.9人で47位で、約4.1倍の差があります。47都道府県で人口あたりの建物火災の件数と死者の相関は0.55です。青森県のように両方とも1位の県もあり、件数の多い県ほど死者が多い傾向はありますが、東京都や富山県のように大きく外れる県があります。

火災による死者には、放火による自殺や放火殺人で亡くなった人も含まれます（[消防白書](https://www.fdma.go.jp/publication/hakusho/r6/chapter1/section1/para1/67986.html)はこれらを除いた数も公表していますが、このテーブルの都道府県別の値は含んだ数です）。5年間の死者が50人以下の県が4つ（高知県・鳥取県・徳島県・佐賀県）あり、こうした県の順位は1年に数人の違いで入れ替わります。

## 出火件数の県ごとの差は、建物以外の火災から多く来ている

県の火災の多さとしてよく使われるのは、すべての火災を合わせた出火件数（`K2101`）を人口で割った出火率です（消防庁は人口1万人あたりで公表していますが、ここでは10万人あたりに統一しています）。次の図は、その出火件数を建物火災と、それ以外の火災（林野・車両のほか、空き地・田畑・河川敷・ごみ集積場などの火災）に分けて、人口あたりで多い順に並べたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "pref"},
      "transform": [
        {"fold": ["building_rate", "other_rate"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"building_rate\": \"建物火災\", \"other_rate\": \"建物以外の火災\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"building_rate\",\"other_rate\"], datum.__series)",
          "as": "__order"
        }
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
          "axis": {"title": "出火件数（1年・人口10万人あたり）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["建物火災", "建物以外の火災"], "range": ["#ef4444", "#fca5a5"]},
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
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

出火件数が1位の大分県（43.7件）は、建物火災では10位（18.2件）で、建物以外の火災が25.5件と全国で最も多い県です。東京都が出火件数で33位にとどまるのは建物以外の火災が8.2件と少ないためで、建物火災だけなら2位です。47都道府県のばらつき（標準偏差）は、建物以外の火災が5.1件、建物火災が2.5件で、県ごとの出火件数の差の多くは建物以外の火災から来ています。

建物火災と建物以外の火災の相関は0.61です。死者との相関は、建物以外の火災が0.37、出火件数全体が0.47、建物火災が0.55で、どれも高齢化率（0.76）より弱く出ます。

```sql
SELECT prefectures AS 都道府県数, r_fire_death AS 出火件数と死者, r_building_death AS 建物火災と死者, r_other_death AS 建物以外の火災と死者, r_aged_death AS 高齢化率と死者, sd_building AS 建物火災の標準偏差, sd_other AS 建物以外の火災の標準偏差, r_building_other AS 建物火災と建物以外の火災 FROM correlations
```

## 比較した指標の中で、死亡率との相関が最も強いのは高齢化率（0.76）

次の図は、同じ5年間の高齢化率（65歳以上人口÷総人口）を横軸にとったものです。

```chart
{
  "layer": [
    {
      "data": {"name": "pref"},
      "mark": {"type": "point", "color": "#7c3aed", "opacity": 0.75, "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "aged_pct", "type": "quantitative"},
          {"field": "death_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "aged_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "65歳以上人口の割合（%、2019〜2023年）", "grid": true}
        },
        "y": {
          "field": "death_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "火災による死者（1年・人口10万人あたり）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "aged_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "65歳以上人口の割合（%、2019〜2023年）", "grid": true}
        },
        "y": {
          "field": "death_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "火災による死者（1年・人口10万人あたり）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

47都道府県で、高齢化率と火災死亡率の相関は0.76で、人口あたりの建物火災の件数（0.55）より強く並びます。高齢化率が22.7%と最も低い東京都は死亡率が46位で、38.0%と最も高い秋田県は2位です。[消防白書](https://www.fdma.go.jp/publication/hakusho/r6/chapter1/section1/para1/67986.html)も、放火自殺者等を除いた全国の火災による死者の多くが65歳以上だとしています。高齢化率の高い県は気候や住まいの形などでも高齢化率の低い県と異なるので、この相関だけで原因を高齢化に特定することはできません。

この関係は1980年代から強まってきました。次の図は、1979年から5年ずつに区切り、それぞれの期間で同じ相関を出したものです。

```chart
{
  "layer": [
    {
      "data": {"name": "window"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"period\"]) && isValid(datum[\"r_aged_death\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "period", "type": "nominal"},
          {"field": "r_aged_death", "type": "quantitative"}
        ],
        "x": {
          "field": "period",
          "type": "nominal",
          "axis": {"title": "期間", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "r_aged_death",
          "type": "quantitative",
          "scale": {"domain": [0, 1], "zero": false, "nice": false},
          "axis": {"title": "火災死亡率との相関係数（47都道府県）", "grid": true}
        },
        "color": {
          "datum": "高齢化率との相関",
          "type": "nominal",
          "scale": {"domain": ["高齢化率との相関", "建物火災の件数との相関"], "range": ["#7c3aed", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "window"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"period\"]) && isValid(datum[\"r_building_death\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "period", "type": "nominal"},
          {"field": "r_building_death", "type": "quantitative"}
        ],
        "x": {
          "field": "period",
          "type": "nominal",
          "axis": {"title": "期間", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "r_building_death",
          "type": "quantitative",
          "scale": {"domain": [0, 1], "zero": false, "nice": false},
          "axis": {"title": "火災死亡率との相関係数（47都道府県）", "grid": true}
        },
        "color": {
          "datum": "建物火災の件数との相関",
          "type": "nominal",
          "scale": {"domain": ["高齢化率との相関", "建物火災の件数との相関"], "range": ["#7c3aed", "#ef4444"]},
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

1979〜1983年には、火災死亡率との相関は人口あたりの建物火災の件数（0.48）のほうが高齢化率（0.30）より強くなっていました。その後、高齢化率との相関は上下しながら上がって2019〜2023年には0.76になり、建物火災の件数との相関（0.55）を上回っています。1994〜1998年に高齢化率との相関が0.41へ一度下がっていますが、この期間には阪神・淡路大震災のあった1995年が入っていて、兵庫県を除くと0.58です。

## 全国の建物火災は1975年からほぼ半分になり、死者は1割減った

全国で見ると、建物火災は1975年の38,455件から2023年の20,974件へ、ほぼ半分（45%減）になりました。火災による死者は1975年の1,666人に対して2023年は1,502人で、1割ほどの減少です。途中では阪神・淡路大震災のあった1995年の2,348人が最も多く、それを除くと2003年の2,240人が最多でした。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"deaths_per_1000\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "deaths_per_1000", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "deaths_per_1000",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "火災による死者 ÷ 建物火災1,000件（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

火災による死者を建物火災の件数で割った値は、1975〜1979年の1,000件あたり42〜54人から、2019〜2023年の68〜72人へ上がりました。建物火災が減ったほどには、火災で亡くなる人は減っていません。

## 住宅防火の対策地域を選ぶときにどう使えるか

- 亡くなる人を減らすことが目的なら、対策を重点的に行う地域は人口あたりの火災による死者で選びます。東京都のように建物火災が多くても亡くなる人が少ない県と、富山県のように建物火災が少なくても亡くなる人が多い県があります
- 死者の少ない県の順位は1年で大きく動くので、複数年を合計してから比較します。この記事のSQLの年の範囲を変えれば、別の5年でも同じ集計ができます
- 死者が少なく年ごとの振れが大きい単位では、死者の数だけで順位を付けると偶然に左右されます。都道府県で高齢化率と死亡率の相関が0.76あることは、そうした単位で高齢化率を死者の数と並べて見る根拠になります。市町村や地区の単位でも同じ相関があるかは、この都道府県のデータでは確認できません

## データの出典

本記事は、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010111)の都道府県別データ（Ｋ 安全、Ａ 人口・世帯）を2026-10-26時点で集計しています。火災の値の出典は総務省消防庁の火災年報で、1975〜2023年の暦年の値を使っています。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の安全のテーブル](/datasets/queria/e_stat/ssds/k_pref_safety)と[人口のテーブル](/datasets/queria/e_stat/ssds/a_pref_population)から、自分の県の火災件数や死者の推移を確認できます。

```sql id=pref
WITH k AS (SELECT area_name, SUM(CASE WHEN cat01 = 'K2101' THEN TRY_CAST(value AS DOUBLE) END) AS fires, SUM(CASE WHEN cat01 = 'K2102' THEN TRY_CAST(value AS DOUBLE) END) AS building_fires, SUM(CASE WHEN cat01 = 'K2110' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K2101', 'K2102', 'K2110') AND area_name != '全国' AND year BETWEEN 2019 AND 2023 GROUP BY area_name), a AS (SELECT area_name, SUM(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, SUM(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name != '全国' AND year BETWEEN 2019 AND 2023 GROUP BY area_name), j AS (SELECT k.area_name, k.fires / a.pop * 100000 AS fire_rate, k.building_fires / a.pop * 100000 AS building_rate, (k.fires - k.building_fires) / a.pop * 100000 AS other_rate, k.deaths / a.pop * 100000 AS death_rate, k.deaths / k.building_fires * 1000 AS deaths_per_1000, a.pop65 / a.pop * 100 AS aged_pct, k.deaths FROM k JOIN a USING (area_name)) SELECT area_name, ROUND(fire_rate, 1) AS fire_rate, RANK() OVER (ORDER BY fire_rate DESC) AS fire_rank, ROUND(building_rate, 1) AS building_rate, RANK() OVER (ORDER BY building_rate DESC) AS building_rank, ROUND(other_rate, 1) AS other_rate, RANK() OVER (ORDER BY other_rate DESC) AS other_rank, ROUND(death_rate, 2) AS death_rate, RANK() OVER (ORDER BY death_rate DESC) AS death_rank, ROUND(deaths_per_1000, 1) AS deaths_per_1000, RANK() OVER (ORDER BY deaths_per_1000 DESC) AS deaths_per_1000_rank, ROUND(aged_pct, 1) AS aged_pct, CAST(deaths AS INTEGER) AS deaths_5y, CASE WHEN area_name IN ('東京都', '富山県', '青森県', '大阪府', '神奈川県', '秋田県', '大分県', '石川県') THEN area_name ELSE '' END AS label FROM j ORDER BY fire_rate DESC, area_name
```

```sql id=correlations
-- 本文の相関係数と標準偏差（プロットはしない）。2019〜2023年の5年分を都道府県ごとに合計し、人口10万人あたりにした値どうし
WITH k AS (SELECT area_name, SUM(CASE WHEN cat01 = 'K2101' THEN TRY_CAST(value AS DOUBLE) END) AS fires, SUM(CASE WHEN cat01 = 'K2102' THEN TRY_CAST(value AS DOUBLE) END) AS building_fires, SUM(CASE WHEN cat01 = 'K2110' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K2101', 'K2102', 'K2110') AND area_name != '全国' AND year BETWEEN 2019 AND 2023 GROUP BY area_name), a AS (SELECT area_name, SUM(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, SUM(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name != '全国' AND year BETWEEN 2019 AND 2023 GROUP BY area_name), j AS (SELECT k.fires / a.pop * 100000 AS fire_rate, k.building_fires / a.pop * 100000 AS building_rate, (k.fires - k.building_fires) / a.pop * 100000 AS other_rate, k.deaths / a.pop * 100000 AS death_rate, a.pop65 / a.pop AS aged FROM k JOIN a USING (area_name)) SELECT COUNT(*) AS prefectures, ROUND(CORR(fire_rate, death_rate), 2) AS r_fire_death, ROUND(CORR(building_rate, death_rate), 2) AS r_building_death, ROUND(CORR(other_rate, death_rate), 2) AS r_other_death, ROUND(CORR(aged, death_rate), 2) AS r_aged_death, ROUND(STDDEV_POP(building_rate), 1) AS sd_building, ROUND(STDDEV_POP(other_rate), 1) AS sd_other, ROUND(CORR(building_rate, other_rate), 2) AS r_building_other FROM j
```

```sql id=window
WITH k AS (SELECT area_name, 1979 + (year - 1979) // 5 * 5 AS start_year, SUM(CASE WHEN cat01 = 'K2102' THEN TRY_CAST(value AS DOUBLE) END) AS building_fires, SUM(CASE WHEN cat01 = 'K2110' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K2102', 'K2110') AND area_name != '全国' AND year BETWEEN 1979 AND 2023 GROUP BY 1, 2), a AS (SELECT area_name, 1979 + (year - 1979) // 5 * 5 AS start_year, SUM(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, SUM(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name != '全国' AND year BETWEEN 1979 AND 2023 GROUP BY 1, 2), j AS (SELECT k.start_year, k.area_name, k.building_fires / a.pop AS building_rate, k.deaths / a.pop AS death_rate, k.deaths / k.building_fires AS dpb, a.pop65 / a.pop AS aged FROM k JOIN a USING (area_name, start_year)) SELECT start_year, start_year + 4 AS end_year, CAST(start_year AS VARCHAR) || '〜' || CAST(start_year + 4 AS VARCHAR) || '年' AS period, ROUND(CORR(aged, death_rate), 2) AS r_aged_death, ROUND(CORR(aged, death_rate) FILTER (WHERE area_name != '兵庫県'), 2) AS r_aged_death_excl_hyogo, ROUND(CORR(building_rate, death_rate), 2) AS r_building_death, ROUND(MAX(dpb) / MIN(dpb), 1) AS dpb_max_min FROM j GROUP BY start_year ORDER BY start_year
```

```sql id=national
WITH k AS (SELECT year, SUM(CASE WHEN cat01 = 'K2101' THEN TRY_CAST(value AS DOUBLE) END) AS fires, SUM(CASE WHEN cat01 = 'K2102' THEN TRY_CAST(value AS DOUBLE) END) AS building_fires, SUM(CASE WHEN cat01 = 'K2110' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K2101', 'K2102', 'K2110') AND area_name != '全国' AND year BETWEEN 1975 AND 2023 GROUP BY year) SELECT year, CAST(fires AS INTEGER) AS fires, CAST(building_fires AS INTEGER) AS building_fires, CAST(deaths AS INTEGER) AS deaths, ROUND(deaths / building_fires * 1000, 1) AS deaths_per_1000 FROM k ORDER BY year
```
