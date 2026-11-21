---
title: 福岡市の民営借家率は、博多区67.7%・早良区38.0%で、町丁・字では最大98.6%
description: 令和2年国勢調査の小地域集計で、福岡市の民営借家率を町丁・字ごとに集計しました。区では博多区の67.7%から早良区の38.0%まで約30ポイントの差があり、町丁・字では0%から98.6%まで分かれ、中央値は45.9%です。
publishedAt: 2026-07-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 住宅
  - 不動産
  - 国勢調査
datasets:
  - queria/e_stat
sources:
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 統計地理情報システム（統計GIS） 小地域集計・境界データ
    url: https://www.e-stat.go.jp/gis
    publisher: 総務省統計局
agentHint: 福岡市の町丁・字別に持ち家率(0020÷0010)を出して、持ち家中心の地区の上位を確認して
socialAnnounce: |-
  賃貸需要を映す民営借家率を国勢調査の小地域で町丁・字まで下ろしました。福岡市は区別で博多67.7%〜早良38.0%、地区別では最大98.6%です。

  賃貸住宅の用地選定に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2020年の福岡市で、住宅に住む一般世帯のうち民間の賃貸住宅に住む世帯の割合（民営借家率）は、博多区が67.7%、早良区が38.0%で、約30ポイントの差がありました。町丁・字ごとに集計すると0%から98.6%まで分かれ、中央値は45.9%です。最も高いのは西区の九大新町（98.6%）でした。

賃貸住宅の用地を仕入れるときは、そのエリアに賃貸で住む世帯がどれだけいるかを最初に確認します。民間の賃貸住宅に住む世帯の割合が高い地区は、賃貸の需要が実績で確認できる立地です。これまでの記事では、民営借家率を[都道府県](/showcase/housing-tenure-regional-gap)と[市区町村](/showcase/municipal-rental-demand-gap)の単位で集計しました。出典の住宅・土地統計調査は標本調査なので、市区町村より細かい単位では集計できません。この記事では、全数調査である[国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計を使い、住宅の所有関係を町丁・字の単位で集計します。対象は、人口の流入が続き賃貸市場が活発な福岡市です。

## データの概要

使うのは e-Stat の令和2年国勢調査 小地域集計（`census_small_area_housing`）です。町丁・字ごとに、住宅に住む一般世帯を所有関係で区分した世帯数が入っています。区分は次の3つのコード（`cat01`）で表されます。

| コード | 内容                       |
| ------ | -------------------------- |
| 0010   | 住宅に住む一般世帯（総数） |
| 0020   | 持ち家                     |
| 0030   | 民営借家                   |

民営借家は民間の賃貸住宅で、公営住宅や UR・公社の賃貸、給与住宅は含みません。そのため持ち家と民営借家を足しても総数にはならず、差はこれらの所有形態の世帯です。この記事では、民営借家の世帯数を総数で割った民営借家率（`0030 ÷ 0010`）を賃貸需要の指標にします。

各行には秘匿区分（`cat02`）が付いています。`1` は値がある地区、`2` は合算、`3` は秘匿で、`2` と `3` は値が伏せられています。以下ではすべて `cat02 = '1'` の行に絞り、境界データ（`small_area`）と `key_code` で結合しています。`2` や `3` の行を含めると、分母と分子で欠ける地区が一致せず、比率がずれるためです。

## 区では博多区が67.7%で最も高く、早良区の38.0%と約30ポイント違う

福岡市の7区を、民営借家率の高い順に並べます。

```sql
WITH h AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0020' THEN value END) AS own, MAX(CASE WHEN cat01 = '0030' THEN value END) AS rent FROM e_stat.census.census_small_area_housing WHERE cat02 = '1' GROUP BY area) SELECT REPLACE(b.city_name, '福岡市', '') AS 区, ROUND(SUM(h.tot)) AS 世帯数, ROUND(100.0 * SUM(h.own) / SUM(h.tot), 1) AS 持ち家率, ROUND(100.0 * SUM(h.rent) / SUM(h.tot), 1) AS 民営借家率 FROM h JOIN e_stat.boundary.small_area b ON h.area = b.key_code WHERE b.city_name LIKE '福岡市%' GROUP BY b.city_name ORDER BY 民営借家率 DESC
```

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "ward_bar"},
      "transform": [
        {"fold": ["rent_rate", "own_rate"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"rent_rate\": \"民営借家率\", \"own_rate\": \"持ち家率\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"rent_rate\",\"own_rate\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "ward",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["民営借家率", "持ち家率"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["持ち家率", "民営借家率"]},
        "tooltip": [
          {"field": "ward", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

民営借家率が最も高いのは博多区の67.7%で、中央区の60.5%が続きます。2つの区は福岡市の都心にあたり、住宅の3分の2前後が民間の賃貸です。博多区は持ち家率が19.2%と低く、民営借家率は持ち家率の約3.5倍です。

市の西側・南西側にある早良区（38.0%）と西区（40.8%）では、持ち家率（早良区45.9%、西区46.8%）が民営借家率を上回ります。都心の博多区と郊外の早良区では、民営借家率に約30ポイントの差があります。用地選定では、まずこの区の差でエリアを絞れます。

## 町丁・字では0%から98.6%まで分かれ、駅に近い地区ほど高い

区の平均には、区の中の差が表れません。同じ博多区にも、賃貸中心の地区と持ち家中心の地区があります。そこで民営借家率を町丁・字ごとに集計し、境界に重ねて地図にしました。世帯数が少ない地区では1世帯の差で比率が大きく動くので、総世帯数が50以上の地区に限っています。

```map
type: map
layers:
  - from: chome_map
    geojson: geojson
    color: value
    label: chome
    name: "民営借家率（%）"
lng: 130.36
lat: 33.62
zoom: 10.3
```

民営借家率の高い地区は、博多駅・天神を含む都心部と、そこから鉄道に沿って帯状に広がっています。町丁・字ごとの民営借家率は0%から98.6%まで分かれ、中央値は45.9%です。同じ区の中でも、駅に近い地区は賃貸中心で、周縁の戸建て住宅地は持ち家中心になっています。

## 民営借家率が9割を超える地区は、大学の近くや都心の繁華街にある

総世帯数が200以上の地区のうち、民営借家率の高い上位15地区です。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "chome_rank"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "rent_rate", "type": "quantitative"},
          {"field": "chome", "type": "nominal"}
        ],
        "x": {
          "field": "rent_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "民営借家率（%）", "grid": true}
        },
        "y": {
          "field": "chome",
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

上位には民営借家率が9割前後の地区が並びます。最も高い西区 九大新町（98.6%）は、九州大学が伊都地区へ移転したときに整備された新しい市街地で、学生や大学関係者向けの賃貸住宅が集まっています。博多区 中州五丁目（93.8%）は歓楽街のある中州にあり、住宅のほとんどが賃貸です。博多区・中央区の都心部のほかに、東区 松香台二丁目（93.4%）や南区 那の川二丁目（92.3%）のように、集合住宅がまとまって建つ地区も入っています。

これらの地区では賃貸で住む世帯の割合が特に高く、賃貸住宅の需要が多いと考えられます。民営借家率が高い地区には、賃貸物件がすでに多くあるので、競合も多くなります。用地選定では、民営借家率で需要の多い地区を絞り、区や近隣の地区の水準と比較して、新しく供給できる余地があるかを判断します。

## 業務での使い方

町丁・字ごとの民営借家率を使うと、賃貸住宅の用地を段階的に絞り込めます。

- エリアの一次選定: 市区町村や区の民営借家率で、賃貸需要の高いエリアを選ぶ
- 立地の最終評価: 候補地の町丁・字の民営借家率を確認し、周辺と比較して賃貸で住む世帯が多い立地かを判断する
- 供給余地の検討: 民営借家率が高い地区の中で、近隣と比較して競合の多さと供給の余地を判断する

## データの出典

本記事は、[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計（住宅の所有関係別世帯数）と、[統計GIS](https://www.e-stat.go.jp/gis)の小地域境界データを2026年7月11日時点で取得して集計しています。値は2020年10月時点のものです。

Queria は、国勢調査の小地域集計と境界データを、所有関係の区分コードと列の意味の説明を付けて公開しています。本記事で使った[小地域 住宅の所有関係別世帯数テーブル](/datasets/queria/e_stat/census/census_small_area_housing)で対象の市区町村を切り替えると、ほかの市でも同じ地図を描けます。

```sql id=ward_bar
WITH h AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0020' THEN value END) AS own, MAX(CASE WHEN cat01 = '0030' THEN value END) AS rent FROM e_stat.census.census_small_area_housing WHERE cat02 = '1' GROUP BY area) SELECT REPLACE(b.city_name, '福岡市', '') AS ward, ROUND(100.0 * SUM(h.rent) / SUM(h.tot), 1) AS rent_rate, ROUND(100.0 * SUM(h.own) / SUM(h.tot), 1) AS own_rate FROM h JOIN e_stat.boundary.small_area b ON h.area = b.key_code WHERE b.city_name LIKE '福岡市%' GROUP BY b.city_name ORDER BY rent_rate ASC
```

```sql id=chome_map
WITH h AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0030' THEN value END) AS rent FROM e_stat.census.census_small_area_housing WHERE cat02 = '1' GROUP BY area) SELECT b.area_name AS chome, ST_AsGeoJSON(ST_Simplify(b.geometry, 0.0003)) AS geojson, ROUND(100.0 * h.rent / h.tot, 1) AS value, ROW_NUMBER() OVER (ORDER BY b.key_code) - 1 AS row_id FROM h JOIN e_stat.boundary.small_area b ON h.area = b.key_code WHERE b.city_name LIKE '福岡市%' AND h.tot >= 50 AND h.rent IS NOT NULL
```

```sql id=chome_rank
WITH h AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0030' THEN value END) AS rent FROM e_stat.census.census_small_area_housing WHERE cat02 = '1' GROUP BY area), r AS (SELECT REPLACE(b.city_name, '福岡市', '') || ' ' || b.area_name AS chome, ROUND(100.0 * h.rent / h.tot, 1) AS rent_rate FROM h JOIN e_stat.boundary.small_area b ON h.area = b.key_code WHERE b.city_name LIKE '福岡市%' AND h.tot >= 200) SELECT chome, rent_rate FROM (SELECT chome, rent_rate FROM r ORDER BY rent_rate DESC LIMIT 15) ORDER BY rent_rate ASC
```
