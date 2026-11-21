---
title: 2050年に周りの住民が2割以上減るコンビニは3店に1店。数が多いのは北海道と大阪府
description: 全国のコンビニ5.7万店の位置と1km四方の将来推計人口を重ねました。2050年に周りの住民が2割以上減る店は1万8,735店で、大阪府は1,230店と北海道に次いで多くなります。
publishedAt: 2026-10-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - コンビニ
  - 店舗開発
  - 将来推計人口
  - 商圏分析
datasets:
  - queria/alltheplaces
  - queria/nlftp
  - queria/soumu
sources:
  - title: 国土数値情報 1kmメッシュ別将来推計人口データ（R6国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html
    publisher: 国土交通省
  - title: All The Places
    url: https://www.alltheplaces.xyz/
    publisher: All The Places
agentHint: ファミリーマートとローソンの店だけに絞って、店のある1km四方の住民が2050年までに3割以上減る店を都道府県別に数えて。2割以上減る店で数えたときと上位10の顔ぶれがどう変わるかも出して
socialAnnounce: |-
  全国のコンビニ5.7万店の位置と1km四方の将来推計人口を重ねました。

  2050年に周りの住民が2割以上減る店は3店に1店です。既存店の見直しや出店計画に。
  Queriaはオープンデータを業務で使える形に整えて公開しています。
---

全国のコンビニ57,176店のうち、店のある1km四方の住民が2050年までに2割以上減る店は18,735店で、住民のいる区画にある店の32.9%でした。都道府県では、割合は青森県（93.0%）と秋田県（90.8%）が高く、店の数は北海道（1,763店）と大阪府（1,230店）が多くなります。

コンビニやドラッグストアのように店舗網を広げてきたチェーンでは、新しく出す店を選ぶことに加えて、いまある店のうちどの店が将来も客を見込めるかを判断する必要があります。店を閉じるか、移すか、売り場や営業時間を変えるかを決めるには、店ごとに周りの人口がこの先どう変わるかを知る必要があります。この記事では、全国のコンビニの位置と、1km四方の区画ごとの将来推計人口を重ね、2050年に周りの住民がどれだけ減る場所に店があるかを集計します。

## 3店に1店は、2050年に周りの住民が2割以上減る

使うデータは次の2つです。

| テーブル                                  | 内容                                                                                                                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `alltheplaces.places.place`               | [All The Places](https://www.alltheplaces.xyz/) が各社の公式サイトの店舗検索から集めた施設の一覧。1行が1施設で、ブランド（`brand`）、施設の種類（`category`）、緯度経度を持つ                    |
| `nlftp.population.future_population_mesh` | 国土数値情報の[1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)。1km四方の区画ごとの2025年・2035年・2050年の人口（`population_*`） |

施設の一覧から施設の種類がコンビニ（`category = 'convenience'`）の行を取り出すと、セブン-イレブン、ファミリーマート、ローソン、ミニストップ、セイコーマート、デイリーヤマザキ、NewDays などの店が57,176店あります。店の緯度経度から店のある1km四方の区画を求め、その区画の2025年と2050年の推計人口を比較しました。

ここでの人口は区画に住む人の数で、働きに来る人や通りがかる人は含みません。オフィス街や駅の中の店では、客の多くはこの数字に含まれない人です。1km四方の区画は店の商圏とは別のもので、店の周りの住民の増減を同じ基準で比較するために使っています。住民のいる区画にある店は56,950店です。残る226店は、住民が0人の区画か、将来推計人口の区画がない位置にあるので、以下の集計から除いています。

```chart caption="店のある1km四方の住民の、2025年から2050年までの増減率で分けたコンビニの店の数"
{
  "layer": [
    {
      "data": {"name": "bins"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "stores", "type": "quantitative"}
        ],
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "店のある1km四方の住民の増減率（2025年→2050年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "stores",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "店の数", "grid": true}
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    }
  ]
}
```

2050年までに周りの住民が2割以上減る店は18,735店で、住民のいる区画にある店の32.9%です。3割以上減る店も8,862店（15.6%）あります。住民が増える区画にある店は10,247店（18.0%）です。

店ごとの増減率の中央値は12.8%減で、日本全体の人口の減少率（15.1%減）より小さくなります。コンビニが人の多い場所に多くあるためと考えられます。それでも3店に1店は、2050年までの25年間で周りの住民の5人に1人以上が減る場所にあります。

## 割合では青森県・秋田県、店の数では北海道と大阪府が多い

都道府県ごとに、周りの住民が2割以上減る店の割合（横軸）と店の数（縦軸）を並べました。右にあるほど県内の店の多くが人の減る場所にあり、上にあるほど該当する店の数が多い県です。

```chart caption="都道府県ごとの、2050年に周りの住民が2割以上減るコンビニの割合と店の数"
{
  "layer": [
    {
      "data": {"name": "pref_labeled"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "pct_down20", "type": "quantitative"},
          {"field": "stores_down20", "type": "quantitative"}
        ],
        "x": {
          "field": "pct_down20",
          "type": "quantitative",
          "scale": {"domain": [-3, 100], "zero": false, "nice": false},
          "axis": {"title": "県内の店のうち、周りの住民が2割以上減る店の割合（%）", "grid": true}
        },
        "y": {
          "field": "stores_down20",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "周りの住民が2割以上減る店の数", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_labeled"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "pct_down20",
          "type": "quantitative",
          "scale": {"domain": [-3, 100], "zero": false, "nice": false},
          "axis": {"title": "県内の店のうち、周りの住民が2割以上減る店の割合（%）", "grid": true}
        },
        "y": {
          "field": "stores_down20",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "周りの住民が2割以上減る店の数", "grid": true}
        },
        "text": {"field": "pref_name"}
      }
    },
    {
      "data": {"name": "pref_other"},
      "mark": {"type": "point", "color": "#fca5a5", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "pct_down20", "type": "quantitative"},
          {"field": "stores_down20", "type": "quantitative"}
        ],
        "x": {
          "field": "pct_down20",
          "type": "quantitative",
          "scale": {"domain": [-3, 100], "zero": false, "nice": false},
          "axis": {"title": "県内の店のうち、周りの住民が2割以上減る店の割合（%）", "grid": true}
        },
        "y": {
          "field": "stores_down20",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "周りの住民が2割以上減る店の数", "grid": true}
        }
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

割合が最も高いのは青森県の93.0%と秋田県の90.8%で、県内のほぼすべての店で周りの住民が2割以上減ります。店の数では、青森県が557店、秋田県が405店です。

店の数が最も多いのは北海道の1,763店で、大阪府の1,230店が続きます。大阪府の割合は30.8%で全国平均と同程度ですが、県内の店が3,999店と多いので、青森県と秋田県を合わせた962店より多くなります。茨城県（729店）、静岡県（687店）、千葉県（675店）、埼玉県（670店）も、東北の各県より多くの店が該当します。首都圏・中京圏・関西圏の11都府県（埼玉・千葉・東京・神奈川・岐阜・愛知・三重・京都・大阪・兵庫・奈良）を合わせると5,585店で、全国の該当する店の29.8%です。

東京都は7,243店のうち89店（1.2%）、沖縄県は817店のうち28店（3.4%）で、この2都県だけが特に少なくなっています。

## 大阪府では、北摂の店は住民の減少が小さく、東部と南部の店は大きい

大阪府で店のある1km四方の区画を、住民の増減で3色に分けて地図にしました。1つの点が1つの区画で、区画の中心に置いています。

```map
type: map
caption: "大阪府で店のある1km四方の区画。区画の住民の2025年から2050年までの増減率で色分け"
layers:
  - from: osaka_up
    lng: lon
    lat: lat
    label: stores
    name: "住民が増える"
  - from: osaka_mid
    lng: lon
    lat: lat
    label: stores
    name: "2割未満の減少"
  - from: osaka_down
    lng: lon
    lat: lat
    label: stores
    name: "2割以上減る"
lng: 135.52
lat: 34.62
zoom: 8.6
```

北摂の吹田市（135店）と箕面市（46店）には、周りの住民が2割以上減る店が1店もありません。豊中市は7.8%、茨木市は6.1%です。東部と南部では、門真市（65店）、富田林市（34店）、河内長野市（28店）のすべての店が該当し、松原市・貝塚市・大東市も9割を超えます。該当する店の数では、東大阪市の122店が大阪市の285店に次いで多くなります。

```sql
SELECT
  city_name AS "市町村",
  stores AS "店の数",
  stores_down20 AS "周りの住民が2割以上減る店",
  pct_down20 AS "割合（%）"
FROM osaka_city
WHERE stores >= 25
ORDER BY pct_down20 DESC, city_name
```

府県単位の平均では、このように同じ府の中で市によって大きく違うことは分かりません。

## 北海道では、セイコーマートの店の65.0%で周りの住民が2割以上減る

チェーンごとに見ると、全国で周りの住民が2割以上減る店の割合は、セブン-イレブン32.3%、ファミリーマート29.7%、ローソン36.4%で、大手3社の差は数ポイントです。セイコーマートは64.9%と高くなります。

セイコーマートの店はほとんどが北海道にあるので、北海道の店だけでチェーンを比較します。

```chart caption="北海道のコンビニのうち、2050年に周りの住民が2割以上減る店の割合（北海道に200店以上あるチェーン）"
{
  "layer": [
    {
      "data": {"name": "hokkaido_chain"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "pct_down20", "type": "quantitative"},
          {"field": "brand", "type": "nominal"}
        ],
        "x": {
          "field": "pct_down20",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "周りの住民が2割以上減る店の割合（%）", "grid": true}
        },
        "y": {
          "field": "brand",
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

北海道の中でも、セイコーマートは1,070店のうち65.0%が該当し、セブン-イレブン（58.0%）、ローソン（56.4%）を上回ります。ファミリーマートは34.4%です。店のある区画の2025年の住民の中央値は、セイコーマートが2,709人、ファミリーマートが5,751人で、セイコーマートは住民の少ない区画にも店を出しています。同じ北海道の中でも、周りの住民が2割以上減る店の割合はチェーンによって30ポイント以上違います。

## 業務での使い方

- 自社の店舗リストの緯度経度から1km四方の区画のコードを計算し、同じ将来推計人口を結合すると、2050年に周りの住民が2割以上・3割以上減る店を一覧にできます。閉店・移転・業態転換を検討する店の候補を、同じ基準で並べられます
- 都道府県や市町村ごとに、該当する店の割合と数の両方を確認します。割合が高い県では店舗網全体の再編を、割合は中程度でも数が多い大都市圏の府県では店ごとの選別を検討する、というように、地域ごとに対応を分けられます
- 同じ地域に店を持つ他のチェーンと比較すると、自社の店舗網が競合より人の減る場所に偏っていないかを確認でき、出店や撤退を判断する前提にできます

## データの出典

本記事は、All The Places が各社の公式サイトの店舗検索から集めた店舗の一覧（2026年10月10日に取得されたもの）と、国土交通省の国土数値情報[1kmメッシュ別将来推計人口データ（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を、2026年10月23日時点で集計しています。将来推計人口は、2020年の国勢調査をもとにした推計値です。

Queria は、各社の店舗検索から集めた店舗の一覧と国土数値情報を、列名と座標系を統一し、各列の意味の説明を付けて公開しています。本記事で使った[店舗・施設のテーブル](/datasets/queria/alltheplaces/places/place)から自社や競合のチェーンの店を取り出したり、[1kmメッシュ別将来推計人口のテーブル](/datasets/queria/nlftp/population/future_population_mesh)で特定の地域の2050年の住民を確認したりできます。

```sql id=base
-- 店の緯度経度から店のある1km四方（3次メッシュ）のコードを計算し、将来推計人口と結合する
-- 1行は「1km四方の区画 × チェーン」で、stores がその区画にあるそのチェーンの店の数
-- 3次メッシュは緯度方向に1/120度、経度方向に1/80度の格子
-- 都府県境をまたぐメッシュは県ごとに行が分かれているので、先にメッシュごとに合計する
-- 複数の市区町村にまたがるメッシュは、コードの小さい市区町村に数える。市区町村は大阪府の分だけ残す
WITH store AS (
  SELECT
    brand,
    CAST(floor(lat * 120) AS BIGINT) AS i,
    CAST(floor((lon - 100) * 80) AS BIGINT) AS j
  FROM alltheplaces.places.place
  WHERE category = 'convenience'
),
mesh AS (
  SELECT
    mesh_id,
    sum(population_2025) AS pop_2025,
    sum(population_2050) AS pop_2050,
    min(left(city_code, 2)) AS pref_code,
    min(split_part(city_code, '_', 1)) AS city_code
  FROM nlftp.population.future_population_mesh
  GROUP BY mesh_id
)
SELECT
  s.brand,
  s.i,
  s.j,
  m.pref_code,
  CASE WHEN m.pref_code = '27' THEN m.city_code END AS city_code,
  round(m.pop_2025) AS pop_2025,
  round((m.pop_2050 / m.pop_2025 - 1) * 100, 3) AS change_pct,
  count(*) AS stores
FROM store AS s
LEFT JOIN mesh AS m
  ON m.mesh_id = lpad(CAST(s.i // 80 AS VARCHAR), 2, '0') || lpad(CAST(s.j // 80 AS VARCHAR), 2, '0')
    || CAST((s.i % 80) // 10 AS VARCHAR) || CAST((s.j % 80) // 10 AS VARCHAR)
    || CAST(s.i % 10 AS VARCHAR) || CAST(s.j % 10 AS VARCHAR)
GROUP BY ALL
ORDER BY s.i, s.j, s.brand
```

```sql id=national
-- 全国の店の数と、2050年までの増減で分けた店の数（プロットはしない）
SELECT
  count(*) AS stores,
  count(*) FILTER (WHERE pop_2025 > 0) AS stores_with_residents,
  count(*) FILTER (WHERE pop_2025 > 0 AND change_pct <= -20) AS stores_down20,
  count(*) FILTER (WHERE pop_2025 > 0 AND change_pct <= -30) AS stores_down30,
  count(*) FILTER (WHERE pop_2025 > 0 AND change_pct >= 0) AS stores_up,
  round(count(*) FILTER (WHERE pop_2025 > 0 AND change_pct <= -20) / count(*) FILTER (WHERE pop_2025 > 0) * 100, 1) AS pct_down20,
  round(count(*) FILTER (WHERE pop_2025 > 0 AND change_pct <= -30) / count(*) FILTER (WHERE pop_2025 > 0) * 100, 1) AS pct_down30,
  round(count(*) FILTER (WHERE pop_2025 > 0 AND change_pct >= 0) / count(*) FILTER (WHERE pop_2025 > 0) * 100, 1) AS pct_up,
  round(median(change_pct) FILTER (WHERE pop_2025 > 0), 1) AS median_change_pct,
  (SELECT round((sum(population_2050) / sum(population_2025) - 1) * 100, 1) FROM nlftp.population.future_population_mesh) AS japan_change_pct,
  (SELECT max(run_date) FROM alltheplaces.places.place WHERE category = 'convenience') AS run_date
FROM base, range(base.stores)
```

```sql id=bins
-- 店のある1km四方の住民の、2025年から2050年までの増減率で店を分ける
SELECT
  CASE
    WHEN change_pct <= -40 THEN 1
    WHEN change_pct <= -30 THEN 2
    WHEN change_pct <= -20 THEN 3
    WHEN change_pct <= -10 THEN 4
    WHEN change_pct < 0 THEN 5
    WHEN change_pct < 10 THEN 6
    ELSE 7
  END AS bin,
  CASE
    WHEN change_pct <= -40 THEN '40%以上減'
    WHEN change_pct <= -30 THEN '30〜40%減'
    WHEN change_pct <= -20 THEN '20〜30%減'
    WHEN change_pct <= -10 THEN '10〜20%減'
    WHEN change_pct < 0 THEN '0〜10%減'
    WHEN change_pct < 10 THEN '0〜10%増'
    ELSE '10%以上増'
  END AS label,
  CASE WHEN change_pct <= -20 THEN '#ef4444' WHEN change_pct < 0 THEN '#fca5a5' ELSE '#3b82f6' END AS color,
  count(*) AS stores
FROM base, range(base.stores)
WHERE pop_2025 > 0
GROUP BY ALL
ORDER BY bin
```

```sql id=pref
-- 都道府県ごとの店の数と、足元の住民が2割以上減る店の数と割合
SELECT
  p.pref_name,
  count(*) AS stores,
  count(*) FILTER (WHERE b.change_pct <= -20) AS stores_down20,
  round(count(*) FILTER (WHERE b.change_pct <= -20) / count(*) * 100, 1) AS pct_down20
FROM base AS b, range(b.stores)
JOIN soumu.code.municipality AS p ON p.area_code = b.pref_code || '000'
WHERE b.pop_2025 > 0
GROUP BY p.pref_name
ORDER BY stores_down20 DESC, p.pref_name
```

```sql id=pref_labeled
-- 散布図で名前を出す都道府県（足元の住民が2割以上減る店が600店以上、割合が85%以上、または5%未満）
SELECT * FROM pref
WHERE stores_down20 >= 600 OR pct_down20 >= 85 OR pct_down20 < 5
ORDER BY pref_name
```

```sql id=pref_other
-- 散布図で名前を出さない都道府県
SELECT * FROM pref
WHERE NOT (stores_down20 >= 600 OR pct_down20 >= 85 OR pct_down20 < 5)
ORDER BY pref_name
```

```sql id=metro
-- 首都圏・中京圏・関西圏の11都府県が、足元の住民が2割以上減る店に占める割合（プロットはしない）
SELECT
  sum(stores_down20) FILTER (WHERE pref_name IN ('埼玉県', '千葉県', '東京都', '神奈川県', '岐阜県', '愛知県', '三重県', '京都府', '大阪府', '兵庫県', '奈良県')) AS metro_down20,
  sum(stores_down20) AS all_down20,
  round(sum(stores_down20) FILTER (WHERE pref_name IN ('埼玉県', '千葉県', '東京都', '神奈川県', '岐阜県', '愛知県', '三重県', '京都府', '大阪府', '兵庫県', '奈良県')) / sum(stores_down20) * 100, 1) AS metro_pct,
  sum(stores_down20) FILTER (WHERE pref_name IN ('青森県', '秋田県')) AS aomori_akita_down20
FROM pref
```

```sql id=hokkaido_chain
-- 北海道の店をチェーンごとに分け、足元の住民が2割以上減る店の割合を比べる（北海道に200店以上あるチェーン）
SELECT
  brand,
  count(*) AS stores,
  round(count(*) FILTER (WHERE change_pct <= -20) / count(*) * 100, 1) AS pct_down20,
  round(median(pop_2025)) AS median_pop_2025
FROM base, range(base.stores)
WHERE pref_code = '01' AND pop_2025 > 0
GROUP BY brand
HAVING count(*) >= 200
ORDER BY pct_down20
```

```sql id=chain
-- 全国に1,000店以上あるチェーンごとの、足元の住民が2割以上減る店の割合（プロットはしない）
SELECT
  brand,
  count(*) AS stores,
  round(count(*) FILTER (WHERE change_pct <= -20) / count(*) * 100, 1) AS pct_down20
FROM base, range(base.stores)
WHERE pop_2025 > 0
GROUP BY brand
HAVING count(*) >= 1000
ORDER BY stores DESC
```

```sql id=osaka_city
-- 大阪府の市町村ごとの店の数と、足元の住民が2割以上減る店の数。政令指定都市は行政区を市にまとめる
SELECT
  coalesce(c.designated_city_name, c.municipality_name) AS city_name,
  count(*) AS stores,
  count(*) FILTER (WHERE b.change_pct <= -20) AS stores_down20,
  round(count(*) FILTER (WHERE b.change_pct <= -20) / count(*) * 100, 1) AS pct_down20
FROM base AS b, range(b.stores)
JOIN soumu.code.municipality AS c ON c.area_code = b.city_code
WHERE b.pref_code = '27' AND b.pop_2025 > 0
GROUP BY ALL
ORDER BY stores_down20 DESC, city_name
```

```sql id=osaka_down
-- 大阪府で店のある1km四方の区画のうち、住民が2割以上減る区画。緯度経度は区画の中心
SELECT
  round((i + 0.5) / 120, 5) AS lat,
  round((j + 0.5) / 80 + 100, 5) AS lon,
  sum(stores) AS stores,
  round(any_value(change_pct), 1) AS change_pct
FROM base
WHERE pref_code = '27' AND change_pct <= -20
GROUP BY i, j
ORDER BY i, j
```

```sql id=osaka_mid
-- 大阪府で店のある1km四方の区画のうち、住民の減少が2割未満の区画。緯度経度は区画の中心
SELECT
  round((i + 0.5) / 120, 5) AS lat,
  round((j + 0.5) / 80 + 100, 5) AS lon,
  sum(stores) AS stores,
  round(any_value(change_pct), 1) AS change_pct
FROM base
WHERE pref_code = '27' AND change_pct > -20 AND change_pct < 0
GROUP BY i, j
ORDER BY i, j
```

```sql id=osaka_up
-- 大阪府で店のある1km四方の区画のうち、住民が増える区画。緯度経度は区画の中心
SELECT
  round((i + 0.5) / 120, 5) AS lat,
  round((j + 0.5) / 80 + 100, 5) AS lon,
  sum(stores) AS stores,
  round(any_value(change_pct), 1) AS change_pct
FROM base
WHERE pref_code = '27' AND change_pct >= 0
GROUP BY i, j
ORDER BY i, j
```
