---
title: 運動・スポーツをした人の割合は東京都の74.5%が最も高く、青森県の52.1%と22.4ポイントの差がある
description: 都道府県別のスポーツ行動者率を2021年で比較しました。最も高い東京都は74.5%、最も低い青森県は52.1%です。1人当たり県民所得との相関係数は0.47で、栃木県・富山県・福井県は所得が高いのにスポーツ行動者率が中央値を下回っています。
publishedAt: 2026-06-21
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - スポーツ
  - 出店
  - 商圏分析
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 令和3年社会生活基本調査
    url: https://www.stat.go.jp/data/shakai/2021/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 都道府県別に、男性(cat01=G650001)と女性(cat01=G650002)のスポーツ行動者率の差を2021年で出して、男女差が大きい県と小さい県を並べて
socialAnnounce: |-
  都道府県別のスポーツ行動者率データで、住民がどれだけ運動しているかを比較しました。

  所得が高いのに運動習慣が薄い県には出店の開拓余地があります。
  フィットネス施設の商圏評価に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2021年に過去1年間で運動・スポーツをした人の割合（スポーツ行動者率）は、東京都の74.5%が最も高く、青森県の52.1%が最も低くなりました。差は22.4ポイントで、約1.4倍です。上位には大都市圏の都県が、下位には北東北や日本海側の県が並びます。1人当たり県民所得との相関係数は0.47で、栃木県・富山県・福井県は所得が中央値より高いのに、スポーツ行動者率は中央値を下回っています。

フィットネスクラブやスポーツ施設の新規出店では、商圏人口や所得水準に加えて、その地域の住民がどれだけ運動しているかが会員数に影響します。この記事では、e-Stat「社会・人口統計体系」の都道府県別の文化・スポーツデータ（`g_pref_culture`）を使い、スポーツ行動者率の地域差と推移を集計しました。スポーツ行動者率（`G6500`）は、総務省の[社会生活基本調査](https://www.stat.go.jp/data/shakai/2021/index.html)をもとに、過去1年間に運動・スポーツを行った人の割合（10歳以上）を表します。調査は5年ごとに実施され、男女別の値（男性 `G650001`、女性 `G650002`）も収録されています。「運動・スポーツ」にはウォーキングや体操など日常的な運動も含まれ、年に1回だけ運動した人も含まれるので、行動者率が高いことはフィットネスクラブの利用者が多いことと同じではありません。

## 全国のスポーツ行動者率は2021年に66.5%で、男女差は6.6ポイントに縮んだ

全国の推移を男女別に並べました。調査年は1996・2001・2006・2011・2016・2021年の6回です。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
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
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
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
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "total",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "スポーツ行動者率（％）", "grid": true}
        },
        "color": {
          "datum": "総数",
          "type": "nominal",
          "scale": {"domain": ["総数", "男性", "女性"], "range": ["#22c55e", "#3b82f6", "#ec4899"]},
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"male\"]) ? 0 : 1",
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
          {"field": "male", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "male",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "スポーツ行動者率（％）", "grid": true}
        },
        "color": {
          "datum": "男性",
          "type": "nominal",
          "scale": {"domain": ["総数", "男性", "女性"], "range": ["#22c55e", "#3b82f6", "#ec4899"]},
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"female\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "female", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "female",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "スポーツ行動者率（％）", "grid": true}
        },
        "color": {
          "datum": "女性",
          "type": "nominal",
          "scale": {"domain": ["総数", "男性", "女性"], "range": ["#22c55e", "#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

全国のスポーツ行動者率（総数）は1996年の76.0%から下がり続け、2011年に63.0%になりました。その後は上がり、2016年に68.8%、2021年は66.5%でした。2021年の調査は、新型コロナウイルスによる施設休業や外出自粛が重なった期間の行動を尋ねているので、2016年からの低下にはその影響が含まれている可能性があります。男性は一貫して女性を上回っていますが、差は縮まっています。1996年には男性81.7%・女性70.5%で11.2ポイントの差があり、2021年は男性69.9%・女性63.3%で6.6ポイントでした。女性の運動習慣が男性より伸びてきたので、女性向けの施設やプログラムの利用者も増えてきたと考えられます。

## 2021年は東京都の74.5%が最も高く、青森県の52.1%が最も低い

2021年のスポーツ行動者率を47都道府県で比較しました。上位10・中間・下位10を色分けしています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
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
          "axis": {"title": "スポーツ行動者率（％）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
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
          "axis": {"title": "スポーツ行動者率（％）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
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
          "axis": {"title": "スポーツ行動者率（％）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは東京都の74.5%で、神奈川県（71.8%）・埼玉県（69.3%）・愛知県（68.8%）・千葉県（67.4%）と大都市圏が上位に並びます。下位は青森県（52.1%）・秋田県（57.1%）・長崎県（57.8%）・山形県（58.4%）・新潟県（59.0%）で、北東北や日本海側の県が多くなっています。東京都と青森県の差は22.4ポイントで、約1.4倍です。商圏人口が同じでも、運動を習慣にしている住民の割合が異なれば、見込める会員の数も変わります。都道府県別の値は標本調査にもとづく推計で、標本の小さい県ほど誤差が大きくなります。

## 三大都市圏で高く、北東北と日本海側で低い

都道府県ごとのスポーツ行動者率を地図にしました。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: value
    label: pref_name
    name: "スポーツ行動者率（％）"
lng: 137
lat: 36.5
zoom: 4
```

関東・東海・近畿の三大都市圏は色が濃く、北東北や日本海側の県は色が薄くなっています。都市部で行動者率が高いのは、屋内ジムやスタジオなどの施設が身近にあり、天候に左右されずに運動を続けやすいためと考えられます。施設の数と運動習慣は互いに影響するので、行動者率の高い地域はすでに需要がある市場、低い地域は施設が少ないために運動が習慣になっていない可能性がある市場と考えられます。

## 栃木県・富山県・福井県は、所得が高いのにスポーツ行動者率が中央値を下回る

横軸に2021年のスポーツ行動者率、縦軸に2021年度の1人当たり県民所得（`C122101`）を取り、47都道府県を散布図にしました。点線は47都道府県の中央値（スポーツ行動者率64.0%、1人当たり県民所得2,949千円）で、統計上の基準ではありません。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#22c55e", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "rate", "type": "quantitative"},
          {"field": "income", "type": "quantitative"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "スポーツ行動者率（％・2021年）", "grid": true}
        },
        "y": {
          "field": "income",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1人当たり県民所得（千円・2021年度）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 64, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 2949, "type": "quantitative"}
      }
    }
  ]
}
```

スポーツ行動者率と1人当たり県民所得の相関係数は0.47で、所得が高い県ほど運動している人の割合も高い傾向があります。中央値で区切った4つの領域ごとに、出店の考え方が変わります。

右上には東京都（74.5%・5,761千円）・神奈川県（71.8%・3,199千円）・愛知県（68.8%・3,597千円）・埼玉県（69.3%・3,049千円）など、所得も行動者率も高い大都市圏があります。競合は多いものの、すでに需要がある市場です。右下には栃木県（62.6%・3,307千円）・富山県（59.7%・3,291千円）・福井県（61.5%・3,263千円）など、所得は高いのにスポーツ行動者率が中央値を下回る県があります。所得に余裕があるのに運動習慣がまだ広がっていないので、施設の新設や運動の動機づけによって需要が増える可能性がある市場と考えられます。左上の熊本県（66.6%・2,746千円）・福岡県（67.0%・2,733千円）・沖縄県（65.8%）は、所得が中央値以下でも運動している人の割合が高く、料金を抑えた施設でも会員が集まりやすい市場と考えられます。

## 出店計画での使い方

- 候補地の需要を見積もる: 候補地のスポーツ行動者率を確認し、人口規模が同じでも見込める会員の数が異なることを前提に計画を立てる
- 所得と行動者率の差から出店候補を探す: 所得が高いのに行動者率が低い県（栃木県・富山県・福井県など）は、施設が少ないために運動が習慣になっていない可能性があり、先に出店することを検討する
- 男女比でプログラムを設計する: 男女差は縮小していても男性のほうが高いので、女性の行動者率を高められる地域では女性向けプログラムを中心にする

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)に収録された都道府県別の文化・スポーツデータを、2026年7月11日時点で取得して集計しています。スポーツ行動者率の元データは同じく総務省統計局の[社会生活基本調査](https://www.stat.go.jp/data/shakai/2021/index.html)で、調査は5年ごとです。

Queriaは、e-Statの社会・人口統計体系の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の文化・スポーツ統計テーブル](/datasets/queria/e_stat/ssds/g_pref_culture)から、出店候補地のスポーツ行動者率を所得水準と並べて確認できます。

```sql id=national_trend
SELECT t.year AS year, TRY_CAST(t.value AS DOUBLE) AS total, TRY_CAST(m.value AS DOUBLE) AS male, TRY_CAST(f.value AS DOUBLE) AS female FROM e_stat.ssds.g_pref_culture t JOIN e_stat.ssds.g_pref_culture m ON t.year = m.year AND m.cat01 = 'G650001' AND m.area_name = '全国' JOIN e_stat.ssds.g_pref_culture f ON t.year = f.year AND f.cat01 = 'G650002' AND f.area_name = '全国' WHERE t.cat01 = 'G6500' AND t.area_name = '全国' AND TRY_CAST(t.value AS DOUBLE) IS NOT NULL ORDER BY t.year
```

```sql id=rank_top
WITH ranked AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS rate, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6500' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, rate FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS rate, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6500' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, rate FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH ranked AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS rate, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6500' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, rate FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=map_data
WITH d AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS rate FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6500' AND year = 2021 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT d.area_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, d.rate AS value, ROW_NUMBER() OVER (ORDER BY d.area_name) - 1 AS row_id FROM d JOIN nlftp.boundary.prefecture p ON d.area_name = p.prefecture_name
```

```sql id=scatter
SELECT s.area_name AS area_name, TRY_CAST(s.value AS DOUBLE) AS rate, TRY_CAST(i.value AS DOUBLE) AS income FROM e_stat.ssds.g_pref_culture s JOIN e_stat.ssds.c_pref_economy i ON s.area_name = i.area_name WHERE s.cat01 = 'G6500' AND s.year = 2021 AND i.cat01 = 'C122101' AND i.year = 2021 AND s.area_name != '全国' AND TRY_CAST(s.value AS DOUBLE) IS NOT NULL AND TRY_CAST(i.value AS DOUBLE) IS NOT NULL
```
