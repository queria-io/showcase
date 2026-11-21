---
title: 将来人口の伸びに対して住宅地の地価が安い市区町村は17あり、つくばエクスプレス沿線や熊本の菊池地域に集まる
description: 将来推計人口と不動産取引価格を市区町村単位で結合しました。住宅地の㎡単価が高い市区町村ほど2025→2035年の人口増減率も高く、人口が増えて地価が安い市区町村はほとんどありません。回帰直線を大きく上回る17市区町村は、つくばエクスプレス沿線・福岡都市圏・沖縄・熊本の菊池地域にあります。
publishedAt: 2026-06-15
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 将来人口
  - 不動産
  - 出店戦略
  - 地域格差
datasets:
  - queria/nlftp
  - queria/reinfolib
sources:
  - title: 国土数値情報 1kmメッシュ別将来推計人口（令和6年国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html
    publisher: 国土交通省
  - title: 不動産情報ライブラリ
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
agentHint: 熊本県の市区町村だけで、住宅地の㎡単価（2023〜2025年平均）と将来人口増減率（growth_rate_2025_2035）を並べて、菊池地域が本当に地価の出遅れといえるか確かめて
socialAnnounce: |-
  将来推計人口と不動産取引価格を市区町村単位で掛け合わせました。地価は将来人口を織り込むため「増えて安い」街は希少ですが、伸びの割に地価が出遅れたエリアは実在します。

  出店・不動産投資の候補地選びに。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

全国1,267市区町村の住宅地の㎡単価と2025→2035年の人口増減率を比較すると、㎡単価が高い市区町村ほど人口増減率も高い傾向があります。人口が増えるのは111市区町村で、その大半は地価も高い側にあり、人口が増えて地価が安い市区町村はほとんどありません。地価の水準から見込まれるより人口の伸びが大きい市区町村は17あり、つくばエクスプレス沿線、福岡都市圏、沖縄、熊本県の菊池地域に集まっています。

新規出店や不動産投資の候補地を選ぶときは、これから人口が増え、地価がまだ安い市区町村を探すことがよくあります。地価は将来の需要を見込んで決まるので、人口が増える見込みの市区町村では先に地価が上がっていると考えられます。この記事では、国土交通省の[国土数値情報](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)の将来推計人口と、[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)の不動産取引価格情報を市区町村単位で結合し、地価が将来人口をどこまで反映しているかと、人口の伸びに対して地価が安い市区町村を集計します。

## 使ったデータ

次の2つのテーブルを市区町村コードで結合します。

| データ         | テーブル                                          | 使う指標                        |
| -------------- | ------------------------------------------------- | ------------------------------- |
| 将来推計人口   | `nlftp.population.future_population_municipality` | 2025→2035年の人口増減率（%）    |
| 不動産取引価格 | `reinfolib.main.mart_trade_prices`                | 住宅地の㎡単価（実取引、円/㎡） |

将来推計人口は、国土数値情報「1kmメッシュ別将来推計人口（R6国政局推計）」を市区町村単位に集計したもので、国勢調査と国立社会保障・人口問題研究所の地域別将来推計人口に基づく推計値です。公表後に決まった大型開発や企業立地は反映されていません。住宅地の㎡単価は、不動産取引価格情報のうち `property_type = '宅地(土地)'` かつ `region = '住宅地'` の実取引を、2023〜2025年で市区町村ごとに平均した値です（㎡単価が0以下の行は除いています）。取引件数が少ないと平均が個別の物件に左右されるので、住宅地の取引が15件以上あり、人口が1万人以上の1,267市区町村に絞りました。どちらも市区町村の平均値なので、駅前と郊外のような市区町村内の差は表れません。

## 住宅地の㎡単価が高い市区町村ほど、人口増減率も高い

横軸に住宅地㎡単価（対数）、縦軸に2025→2035年の人口増減率を取って1,267市区町村を散布図にし、回帰直線を重ねました。

```chart
{
  "layer": [
    {
      "data": {"name": "trend_line"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"price_man\"]) && isValid(datum[\"y\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#475569",
        "strokeWidth": 2,
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "x": {
          "field": "price_man",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "住宅地㎡単価（万円・対数軸）", "grid": true}
        },
        "y": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口増減率 2025→2035（%）", "grid": true}
        },
        "color": {
          "datum": "市場のトレンド",
          "type": "nominal",
          "scale": {
            "domain": ["市場のトレンド", "その他", "出遅れ（狙い目）"],
            "range": ["#475569", "#cbd5e1", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "scatter_other"},
      "mark": {"type": "point", "opacity": 0.6, "filled": true, "size": 20},
      "encoding": {
        "tooltip": [
          {"field": "price_man", "type": "quantitative"},
          {"field": "growth", "type": "quantitative"}
        ],
        "x": {
          "field": "price_man",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "住宅地㎡単価（万円・対数軸）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口増減率 2025→2035（%）", "grid": true}
        },
        "color": {
          "datum": "その他",
          "type": "nominal",
          "scale": {
            "domain": ["市場のトレンド", "その他", "出遅れ（狙い目）"],
            "range": ["#475569", "#cbd5e1", "#7c3aed"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "scatter_target"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "price_man", "type": "quantitative"},
          {"field": "growth", "type": "quantitative"}
        ],
        "x": {
          "field": "price_man",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "住宅地㎡単価（万円・対数軸）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口増減率 2025→2035（%）", "grid": true}
        },
        "color": {
          "datum": "出遅れ（狙い目）",
          "type": "nominal",
          "scale": {
            "domain": ["市場のトレンド", "その他", "出遅れ（狙い目）"],
            "range": ["#475569", "#cbd5e1", "#7c3aed"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeWidth": 1, "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 0, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 12,
        "color": "#7c3aed"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 0.02"}},
        "y": {"value": {"expr": "height * (1 - 0.98)"}},
        "text": {"value": "トレンド線より上＝伸びの割に割安（出遅れ）"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

点は左下から右上に並び、住宅地㎡単価が高い市区町村ほど人口増減率も高くなっています。地価には将来の人口の動きがかなり反映されていると考えられます。1,267市区町村のうち人口が増えるのは111で、その大半は地価も高い側にあります。図の左上にあたる、地価が安く人口が増える市区町村はほとんどありません。

回帰直線より上にある市区町村は、その地価の水準から見込まれるより人口の伸びが大きい市区町村です。この記事では、人口が増え（縦軸がプラス）、回帰直線からの差が8ポイント以上の17市区町村を、人口の伸びに対して地価が安い「出遅れ」の市区町村として紫で示しました。8ポイントという基準は候補を絞るために置いたもので、統計的に決まった値ではありません。

## 出遅れの17市区町村は、つくばエクスプレス沿線・福岡都市圏・沖縄・熊本の菊池地域にある

17市区町村を地図にしました。紫が出遅れの市区町村（点の大きさは人口）、灰色は人口が増えるその他の市区町村です。

```map
type: map
layers:
  - from: map_grow
    lng: lon
    lat: lat
    name: "人口増（その他）"
  - from: map_target
    lng: lon
    lat: lat
    label: name
    name: "出遅れ（狙い目）"
lng: 136
lat: 35
zoom: 4
```

出遅れの市区町村は、つくばエクスプレス沿線（茨城県つくばみらい市・守谷市・つくば市、千葉県印西市）、福岡都市圏（福岡県粕屋町・福津市）、沖縄（中城村・八重瀬町など）、半導体関連の工場が集まる熊本県の菊池地域（大津町・菊陽町・合志市）にあります。どれも大都市圏の中心部から離れていて、地価は地方や郊外の水準ですが、人口の伸びが見込まれている地域です。鉄道の開業や工場の立地による需要の増加が、まだ地価に十分反映されていないと考えられます。

## 人口増減率が最も高いのは印西市の+5.8%、地価が最も安いのは大津町の3.6万円/㎡

17市区町村を人口増減率の高い順に並べました。棒の長さが2025→2035年の人口増減率、ラベルが住宅地㎡単価です。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "otarank"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "price_label", "type": "nominal"},
          {"field": "growth", "type": "quantitative"},
          {"field": "name", "type": "nominal"}
        ],
        "x": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口増減率 2025→2035（%）", "grid": true}
        },
        "y": {"field": "name", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null}
      }
    },
    {
      "data": {"name": "otarank"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口増減率 2025→2035（%）", "grid": true}
        },
        "y": {"field": "name", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null},
        "text": {"field": "price_label"}
      }
    }
  ]
}
```

千葉県印西市（+5.8%・8.1万円/㎡）、福岡県粕屋町（+4.9%・10.2万円/㎡）、茨城県つくばみらい市・守谷市（ともに+4.8%）などが上位です。熊本県大津町は人口増減率+2.8%で、住宅地㎡単価は3.6万円/㎡と17市区町村の中で最も安い水準です。同じ熊本県の菊陽町・合志市、茨城県つくば市（4.3万円/㎡）も、半導体関連の工場や研究学園都市があって人口が増える一方、地価は低い水準です。これらは、需要の増加が見込まれ、取得費用を抑えられる候補として、現地調査の対象になります。

## 業務での使い方

- 候補地の一覧作成: 人口の伸びに対して地価が安い（回帰直線より上の）市区町村を抽出し、現地調査に進む候補を絞る
- 取得時期の検討: 出遅れの市区町村は、需要の増加がまだ地価に反映されていない段階にあると考えられるので、地価が上がる前に取得できるかを検討する
- 既存の出店エリアとの比較: 自社の主力エリアの人口増減率と地価を基準に、同じくらいの伸びで地価がより安い候補を探す
- 撤退・縮小の判断: 回帰直線より下（人口の伸びに対して地価が高い）や、人口が減り続ける市区町村を確認し、出店のペースや投資の配分を見直す

## まとめ

- 住宅地㎡単価が高い市区町村ほど将来人口の増減率も高く、人口が増えて地価が安い市区町村はほとんどありません
- 人口の伸びに対して地価が安い市区町村が17あり、つくばエクスプレス沿線・福岡都市圏・沖縄・熊本の菊池地域にあります
- 印西市・つくばみらい市・大津町・つくば市などは、人口の増加が見込まれ、取得費用を抑えられる候補です

## データの出典

本記事は国土交通省の[国土数値情報「1kmメッシュ別将来推計人口（令和6年国政局推計）」](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を市区町村単位に集計した将来推計人口と、[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)の不動産取引価格情報を、2026年7月11日時点で取得して集計しています。人口は2025年と2035年の推計値、地価は2023〜2025年の実取引です。

Queriaは、国土数値情報や不動産取引価格などの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[将来推計人口テーブル](/datasets/queria/nlftp/population/future_population_municipality)と[不動産取引価格テーブル](/datasets/queria/reinfolib/main/mart_trade_prices)を市区町村コードで結合すると、自社の条件に合う候補地を絞り込めます。

```sql id=scatter_other
WITH price AS (SELECT LPAD(municipality_code, 5, '0') AS city_code, AVG(unit_price) AS p FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '住宅地' AND unit_price > 0 AND year BETWEEN 2023 AND 2025 GROUP BY 1 HAVING COUNT(*) >= 15), base AS (SELECT ROUND(p.p / 10000, 1) AS price_man, m.growth_rate_2025_2035 AS growth, LOG10(p.p / 10000) AS lx FROM nlftp.population.future_population_municipality m JOIN price p ON m.city_code = p.city_code WHERE m.population_2025 >= 10000), reg AS (SELECT regr_slope(growth, lx) AS b, regr_intercept(growth, lx) AS a FROM base), scored AS (SELECT base.*, growth - (reg.a + reg.b * lx) AS resid FROM base, reg) SELECT price_man, growth FROM scored WHERE NOT (growth > 0 AND resid >= 8)
```

```sql id=scatter_target
WITH price AS (SELECT LPAD(municipality_code, 5, '0') AS city_code, AVG(unit_price) AS p FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '住宅地' AND unit_price > 0 AND year BETWEEN 2023 AND 2025 GROUP BY 1 HAVING COUNT(*) >= 15), base AS (SELECT m.prefecture_name || ' ' || COALESCE(m.city_name, '') || COALESCE(' ' || m.ward_name, '') AS name, ROUND(p.p / 10000, 1) AS price_man, m.growth_rate_2025_2035 AS growth, LOG10(p.p / 10000) AS lx FROM nlftp.population.future_population_municipality m JOIN price p ON m.city_code = p.city_code WHERE m.population_2025 >= 10000), reg AS (SELECT regr_slope(growth, lx) AS b, regr_intercept(growth, lx) AS a FROM base), scored AS (SELECT base.*, growth - (reg.a + reg.b * lx) AS resid FROM base, reg) SELECT price_man, growth, name FROM scored WHERE growth > 0 AND resid >= 8
```

```sql id=trend_line
WITH price AS (SELECT LPAD(municipality_code, 5, '0') AS city_code, AVG(unit_price) AS p FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '住宅地' AND unit_price > 0 AND year BETWEEN 2023 AND 2025 GROUP BY 1 HAVING COUNT(*) >= 15), base AS (SELECT ROUND(p.p / 10000, 1) AS price_man, m.growth_rate_2025_2035 AS growth, LOG10(p.p / 10000) AS lx FROM nlftp.population.future_population_municipality m JOIN price p ON m.city_code = p.city_code WHERE m.population_2025 >= 10000), reg AS (SELECT regr_slope(growth, lx) AS b, regr_intercept(growth, lx) AS a FROM base) SELECT x AS price_man, ROUND(a + b * LOG10(x), 1) AS y FROM (SELECT MIN(price_man) AS x FROM base UNION ALL SELECT MAX(price_man) AS x FROM base), reg ORDER BY x
```

```sql id=map_grow
WITH price AS (SELECT LPAD(municipality_code, 5, '0') AS city_code, AVG(unit_price) AS p FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '住宅地' AND unit_price > 0 AND year BETWEEN 2023 AND 2025 GROUP BY 1 HAVING COUNT(*) >= 15), base AS (SELECT m.city_code, m.growth_rate_2025_2035 AS growth, LOG10(p.p / 10000) AS lx FROM nlftp.population.future_population_municipality m JOIN price p ON m.city_code = p.city_code WHERE m.population_2025 >= 10000), reg AS (SELECT regr_slope(growth, lx) AS b, regr_intercept(growth, lx) AS a FROM base), scored AS (SELECT base.*, growth - (reg.a + reg.b * lx) AS resid FROM base, reg) SELECT ROUND(ST_Y(ST_Centroid(bd.geometry)), 4) AS lat, ROUND(ST_X(ST_Centroid(bd.geometry)), 4) AS lon FROM scored s JOIN nlftp.boundary.municipality bd ON bd.lg_code = s.city_code WHERE s.growth > 0 AND s.resid < 8
```

```sql id=map_target
WITH price AS (SELECT LPAD(municipality_code, 5, '0') AS city_code, AVG(unit_price) AS p FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '住宅地' AND unit_price > 0 AND year BETWEEN 2023 AND 2025 GROUP BY 1 HAVING COUNT(*) >= 15), base AS (SELECT m.city_code, m.prefecture_name || ' ' || COALESCE(m.city_name, '') || COALESCE(' ' || m.ward_name, '') AS name, m.population_2025 AS pop, m.growth_rate_2025_2035 AS growth, LOG10(p.p / 10000) AS lx FROM nlftp.population.future_population_municipality m JOIN price p ON m.city_code = p.city_code WHERE m.population_2025 >= 10000), reg AS (SELECT regr_slope(growth, lx) AS b, regr_intercept(growth, lx) AS a FROM base), scored AS (SELECT base.*, growth - (reg.a + reg.b * lx) AS resid FROM base, reg) SELECT s.name, ROUND(ST_Y(ST_Centroid(bd.geometry)), 4) AS lat, ROUND(ST_X(ST_Centroid(bd.geometry)), 4) AS lon, s.growth, ROUND(LEAST(28, GREATEST(8, SQRT(s.pop) / 14)), 1) AS size FROM scored s JOIN nlftp.boundary.municipality bd ON bd.lg_code = s.city_code WHERE s.growth > 0 AND s.resid >= 8
```

```sql id=otarank
WITH price AS (SELECT LPAD(municipality_code, 5, '0') AS city_code, AVG(unit_price) AS p FROM reinfolib.main.mart_trade_prices WHERE property_type = '宅地(土地)' AND region = '住宅地' AND unit_price > 0 AND year BETWEEN 2023 AND 2025 GROUP BY 1 HAVING COUNT(*) >= 15), base AS (SELECT m.prefecture_name || ' ' || COALESCE(m.city_name, '') || COALESCE(' ' || m.ward_name, '') AS name, ROUND(p.p / 10000, 1) AS price_man, m.growth_rate_2025_2035 AS growth, LOG10(p.p / 10000) AS lx FROM nlftp.population.future_population_municipality m JOIN price p ON m.city_code = p.city_code WHERE m.population_2025 >= 10000), reg AS (SELECT regr_slope(growth, lx) AS b, regr_intercept(growth, lx) AS a FROM base), scored AS (SELECT base.*, growth - (reg.a + reg.b * lx) AS resid FROM base, reg) SELECT name, growth, price_man, ROUND(price_man, 1) || '万円/㎡' AS price_label FROM scored WHERE growth > 0 AND resid >= 8 ORDER BY growth DESC
```
