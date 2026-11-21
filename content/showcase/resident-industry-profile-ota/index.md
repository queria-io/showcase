---
title: 知識産業で働く住民の割合は、大田区の町丁・字の間で最大6倍違う
description: 令和2年国勢調査の小地域データで、住民が働く産業の構成を集計しました。情報通信業・金融業・保険業・学術研究などの知識産業で働く住民の割合は、東京23区で最大2.3倍、大田区の町丁・字では5.1%から30.3%まで6倍近い差があります
ogDescription: 令和2年国勢調査の小地域データで、知識産業で働く住民の割合を集計しました。東京23区で最大2.3倍、大田区の町丁・字では6倍近い差があります
publishedAt: 2026-07-10
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 国勢調査
  - 小地域
  - エリアマーケティング
datasets:
  - queria/e_stat
sources:
  - title: 令和2年国勢調査 小地域集計（統計GIS）
    url: https://www.e-stat.go.jp/gis
    publisher: 総務省統計局
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
agentHint: 大田区の町丁字別に運輸・郵便業（cat01='0100'）の就業者比率を出して、羽田周辺が突出しているか確かめて
socialAnnounce: |-
  国勢調査の小地域データで、住民が働く産業の構成を町丁字単位で可視化しました。

  知識産業の比率は23区で最大2.3倍、大田区内でも6倍近い差があります。エリアの商品企画やターゲティングに。
  Queriaは国のオープンデータを業務で使える形に整えて公開しています。
---

令和2年国勢調査の小地域集計で、住民のうち情報通信業・金融業・保険業・学術研究・専門技術サービス業で働く人（この記事では「知識産業」と呼びます）の割合を集計すると、東京23区では中央区の33.3%から足立区の14.4%まで2.3倍の差がありました。大田区の区全体の割合は19.4%ですが、町丁・字別では大森南五丁目の5.1%から北千束三丁目の30.3%まで、6倍近い差があります。

賃貸住宅の商品企画や店舗の出店計画では、対象エリアにどんな住民が暮らしているかを把握する必要があります。人口や年齢構成が近い地域でも、住民の働く産業は大きく異なることがあります。国勢調査の小地域集計には、町丁・字（丁目）単位で産業大分類別の就業者数が収録されています。この就業者数は常住地ベースで、その地区に住んでいる就業者を勤め先の産業で分類した数です。専門・知識サービスで働く人が多い地区と、製造や物流の現場で働く人が多い地区では、世帯の所得水準や生活スタイルの傾向が異なると考えられます。この記事では、東京23区を比較したあと、大田区を町丁・字ごとに集計します。

## 使用するデータ

e-Stat「[令和2年国勢調査](https://www.e-stat.go.jp/gis)」の小地域（町丁・字等）別 産業大分類別就業者数（`census_small_area_industry`）を使います。就業者を農林業から公務まで20の産業大分類（`cat01`）に分けて収録しており、値は就業者数（人）です。小地域では就業者数が少ない産業の値が秘匿されるので、集計区分（`cat02`）が「無し（開示）」のセルだけを使います。地区の識別コード（`area`）は同じデータセットの境界データ（`small_area`）と共通で、`key_code` で結合すると地図に描けます。

大田区全体（就業者約35万人）の産業構成を集計しました。

```sql
WITH a AS (SELECT cat01, industry, value FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND area = '13111'), t AS (SELECT value AS total FROM a WHERE cat01 = '0010') SELECT a.industry AS 産業大分類, CAST(a.value AS BIGINT) AS 就業者数, ROUND(a.value / t.total * 100, 1) AS 構成比 FROM a, t WHERE a.cat01 IN ('0110', '0070', '0090', '0180', '0100', '0200', '0140', '0060', '0120') ORDER BY a.value DESC
```

大田区では卸売業・小売業（15.2%）と製造業（11.6%）が多く、情報通信業（10.5%）も1割を占めます。以降では、所得や職種の傾向が表れやすい情報通信業（`0090`）、金融業・保険業（`0120`）、学術研究・専門技術サービス業（`0140`）の3分類を「知識産業」としてまとめ、就業者に占める割合を指標に使います。この区分は本記事で設けたもので、統計上の分類ではありません。

## 知識産業で働く住民の割合は、23区で中央区の33.3%から足立区の14.4%まで2.3倍の差がある

23区それぞれで、知識産業で働く住民が就業者に占める割合を比較しました。上位を青、中位を薄い青、下位をグレーで色分けしています。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "ku_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "知識産業の就業者比率（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "区"}, "sort": null},
        "color": {
          "datum": "上位7区",
          "type": "nominal",
          "scale": {"domain": ["上位7区", "中位", "下位7区"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "ku_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "知識産業の就業者比率（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "区"}, "sort": null},
        "color": {
          "datum": "中位",
          "type": "nominal",
          "scale": {"domain": ["上位7区", "中位", "下位7区"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "ku_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "知識産業の就業者比率（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "区"}, "sort": null},
        "color": {
          "datum": "下位7区",
          "type": "nominal",
          "scale": {"domain": ["上位7区", "中位", "下位7区"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは中央区（33.3%）で、港区（32.5%）、渋谷区（32.1%）、千代田区（31.0%）と都心の区が続きます。目黒区（29.2%）、文京区（29.1%）も高い水準です。下位には足立区（14.4%）、葛飾区（15.7%）、江戸川区（16.4%）と城東の区が入っています。

大田区は19.4%で、23区のなかでは下位のグループです。次に、大田区を町丁・字ごとに集計します。

## 大田区の町丁・字では、知識産業の割合は5.1%から30.3%まで6倍近い差がある

大田区の町丁・字ごとの知識産業の就業者比率を地図にしました。色が濃いほど比率が高い地区です。就業者が100人未満の地区は、1人の増減で比率が数ポイント変わるので除いており、地図に載っているのは180地区です。

```map
type: map
layers:
  - from: ota_map
    geojson: geojson
    color: rate
    label: town
    name: "知識産業比率（%）"
lng: 139.72
lat: 35.565
zoom: 11.4
```

区全体では19.4%ですが、町丁・字ごとでは最も低い地区で5.1%、最も高い地区で30.3%です。比率の高い地区は北千束・南千束・田園調布・上池台といった区の西側の高台に多く、比率の低い地区は羽田・糀谷・大森南など東側の臨海部に多くあります。同じ大田区でも、丘陵の住宅地と臨海の工業地帯では、住民の働く産業がはっきり異なります。

比率の高い町丁・字と低い町丁・字を5つずつ並べました。

```sql
WITH c AS (SELECT area_name, MAX(CASE WHEN cat01 = '0010' THEN value END) AS total, SUM(CASE WHEN cat01 IN ('0090', '0120', '0140') THEN value END) AS knowledge FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND area LIKE '13111%' AND LENGTH(area) = 11 GROUP BY area_name), r AS (SELECT REPLACE(area_name, '大田区', '') AS 町丁字, CAST(total AS BIGINT) AS 就業者数, ROUND(100.0 * knowledge / total, 1) AS 知識産業比率, ROW_NUMBER() OVER (ORDER BY 100.0 * knowledge / total DESC) AS rn, COUNT(*) OVER () AS n FROM c WHERE total >= 500) SELECT 町丁字, 就業者数, 知識産業比率 FROM r WHERE rn <= 5 OR rn > n - 5 ORDER BY 知識産業比率 DESC
```

上位は北千束三丁目（30.3%）、南千束三丁目（29.7%）、田園調布五丁目（29.5%）で、下位には大森南五丁目（5.1%）、羽田五丁目（6.4%）が入っています。区全体の平均では、こうした町丁・字ごとの差は分かりません。

## 羽田では住民の21.5%が運輸業・郵便業で働き、田園調布の7倍以上

知識産業の割合が高い田園調布と低い羽田について、産業構成を比較しました。地名ごとに全丁目を合算し、主な産業大分類の構成比を集計しています。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "profile"},
      "transform": [
        {"fold": ["denen_pct", "haneda_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"denen_pct\": \"田園調布\", \"haneda_pct\": \"羽田\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"denen_pct\",\"haneda_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {"field": "industry", "type": "nominal", "axis": {"title": "産業大分類"}, "sort": null},
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "就業者に占める割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["田園調布", "羽田"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["羽田", "田園調布"]},
        "tooltip": [
          {"field": "industry", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

田園調布では情報通信業（11.3%）と学術研究・専門技術サービス業（11.3%）の割合が高く、金融業・保険業も4.8%あります。羽田は運輸業・郵便業が21.5%で、空港と物流施設が集まる立地が住民の働く産業に表れていると考えられます。田園調布の運輸業・郵便業（3.0%）とは7倍以上の差があります。製造業はどちらも1割前後です。

## データの活用

住民の産業構成を町丁・字単位で集計すると、エリアを対象にした業務で次のように使えます。

- 賃貸・分譲住宅の商品企画: 知識産業の比率が高い地区では、単身・共働きの専門職世帯に向けた住戸プランや設備のグレードを検討する
- 出店・商圏の評価: 運輸・製造の現場で働く人が多い地区と、専門職の多い地区とで、扱う業態や価格帯の仮説を変える
- 広告の配信エリア: 区単位ではなく町丁・字単位で住民の産業構成を比較し、チラシやデジタル広告の配信エリアを設計する
- 既存エリアの評価: 経験的に違いがあると感じている地区の差を、産業構成の数字で説明する

知識産業の比率は勤め先の産業による分類で、職種や役職は含まないので、比率が高いことがそのまま所得水準が高いことを表すわけではありません。

## データの出典

本記事は総務省統計局の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計（[統計GIS](https://www.e-stat.go.jp/gis)）を、2026年7月11日時点で取得して集計しています。調査時点は2020年10月1日です。

Queriaは、統計GISの国勢調査の小地域集計を、産業分類コードや秘匿区分の説明を付け、境界データと同じコードで結合できる形で公開しています。本記事で使った[産業別就業者数テーブル](/datasets/queria/e_stat/census/census_small_area_industry)と[町丁・字境界テーブル](/datasets/queria/e_stat/boundary/small_area)から、対象エリアの産業構成を町丁・字単位で集計できます。

```sql id=ku_top
WITH w AS (SELECT area_name, MAX(CASE WHEN cat01 = '0010' THEN value END) AS total, SUM(CASE WHEN cat01 IN ('0090', '0120', '0140') THEN value END) AS knowledge FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND area IN ('13101', '13102', '13103', '13104', '13105', '13106', '13107', '13108', '13109', '13110', '13111', '13112', '13113', '13114', '13115', '13116', '13117', '13118', '13119', '13120', '13121', '13122', '13123') GROUP BY area_name) SELECT area_name, ROUND(knowledge / total * 100, 1) AS pct FROM w ORDER BY knowledge / total DESC, area_name LIMIT 7
```

```sql id=ku_mid
WITH w AS (SELECT area_name, MAX(CASE WHEN cat01 = '0010' THEN value END) AS total, SUM(CASE WHEN cat01 IN ('0090', '0120', '0140') THEN value END) AS knowledge FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND area IN ('13101', '13102', '13103', '13104', '13105', '13106', '13107', '13108', '13109', '13110', '13111', '13112', '13113', '13114', '13115', '13116', '13117', '13118', '13119', '13120', '13121', '13122', '13123') GROUP BY area_name) SELECT area_name, ROUND(knowledge / total * 100, 1) AS pct FROM w ORDER BY knowledge / total DESC, area_name LIMIT 9 OFFSET 7
```

```sql id=ku_bottom
WITH w AS (SELECT area_name, MAX(CASE WHEN cat01 = '0010' THEN value END) AS total, SUM(CASE WHEN cat01 IN ('0090', '0120', '0140') THEN value END) AS knowledge FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND area IN ('13101', '13102', '13103', '13104', '13105', '13106', '13107', '13108', '13109', '13110', '13111', '13112', '13113', '13114', '13115', '13116', '13117', '13118', '13119', '13120', '13121', '13122', '13123') GROUP BY area_name) SELECT area_name, ROUND(knowledge / total * 100, 1) AS pct FROM w ORDER BY knowledge / total DESC, area_name OFFSET 16
```

```sql id=ota_map
WITH c AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS total, SUM(CASE WHEN cat01 IN ('0090', '0120', '0140') THEN value END) AS knowledge FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND area LIKE '13111%' AND LENGTH(area) = 11 GROUP BY area) SELECT b.area_name AS town, ST_AsGeoJSON(ST_Simplify(b.geometry, 0.0002)) AS geojson, ROUND(100.0 * c.knowledge / c.total, 1) AS rate, ROW_NUMBER() OVER (ORDER BY b.key_code) - 1 AS row_id FROM c JOIN e_stat.boundary.small_area b ON c.area = b.key_code WHERE b.city_name = '大田区' AND c.total >= 100 AND c.knowledge IS NOT NULL
```

```sql id=profile
WITH base AS (SELECT CASE WHEN area_name LIKE '大田区田園調布%' THEN 'denen' WHEN area_name LIKE '大田区羽田%' THEN 'haneda' END AS zone, cat01, value FROM e_stat.census.census_small_area_industry WHERE cat02 = '1' AND LENGTH(area) = 11 AND (area_name LIKE '大田区田園調布%' OR area_name LIKE '大田区羽田%')), agg AS (SELECT zone, cat01, SUM(value) AS v FROM base GROUP BY zone, cat01), tot AS (SELECT zone, v AS total FROM agg WHERE cat01 = '0010'), pct AS (SELECT a.zone, a.cat01, ROUND(a.v / t.total * 100, 1) AS p FROM agg a JOIN tot t USING (zone)) SELECT ind.name AS industry, MAX(CASE WHEN pct.zone = 'denen' THEN pct.p END) AS denen_pct, MAX(CASE WHEN pct.zone = 'haneda' THEN pct.p END) AS haneda_pct FROM (VALUES ('0060', '建設業'), ('0070', '製造業'), ('0090', '情報通信業'), ('0100', '運輸・郵便業'), ('0110', '卸売・小売業'), ('0120', '金融・保険業'), ('0140', '学術・専門技術'), ('0180', '医療・福祉')) AS ind (code, name) JOIN pct ON pct.cat01 = ind.code GROUP BY ind.name, ind.code ORDER BY ind.code
```
