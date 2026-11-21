---
title: 千葉市の高齢化率は、区単位では21.6%〜30.4%、町丁・字単位では4.9%〜76.6%まで差がある
description: 令和2年国勢調査の小地域集計で、千葉市の町丁・字別の高齢化率を集計しました。区単位では21.6%から30.4%ですが、町丁・字単位では4.9%から76.6%まで差があり、同じ美浜区の中でも54.0%の地区と4.9%の地区があります。
publishedAt: 2026-07-06
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 国勢調査
  - 高齢化
  - 商圏分析
datasets:
  - queria/e_stat
sources:
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 令和2年国勢調査 小地域集計（統計GIS）
    url: https://www.e-stat.go.jp/gis
    publisher: 総務省統計局
agentHint: 千葉市の町丁字別に年少人口率（0170÷0010）が高い地区の上位を出して、子育て世帯が集まる新しい開発地区がどこか調べて
socialAnnounce: |-
  令和2年国勢調査の小地域集計を町丁・字まで下ろすと、千葉市の高齢化率は同じ区の中でも4.9%から76.6%まで開きます。一斉入居の住宅団地と新しい開発地区で年齢構成が層状に分かれています。

  高齢者向けサービスの商圏設計に。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

千葉市の6区の高齢化率は、中央区の21.6%から若葉区の30.4%までで、差は約9ポイントです。町丁・字ごとに集計すると、高齢化率は最も低い地区で4.9%、最も高い地区で76.6%です。同じ美浜区の中でも、高浜六丁目は54.0%、幕張西四丁目は4.9%でした。

訪問介護・配食・調剤薬局・シニア向けの小売など、高齢者向けサービスの立地を検討するときは、市区町村単位の高齢化率では範囲が広すぎることがあります。同じ市の中でも、一斉に入居した住宅団地と新しく開発された住宅地では、住民の年齢構成が大きく違うからです。この記事では、町丁・字ごとに集計されている[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計を使い、千葉市の高齢化率の分布を集計します。

## 区単位の高齢化率は、中央区の21.6%から若葉区の30.4%まで

使ったのは e-Stat の令和2年国勢調査 小地域集計（`census_small_area_age`）です。町丁・字ごとに、男女・年齢5歳階級別の人口が入っています。年齢は5歳階級のほか、次の区分の合計もあります。

| コード | 内容                     |
| ------ | ------------------------ |
| 0010   | 総数（年齢不詳含む）     |
| 0170   | 15歳未満（年少人口）     |
| 0180   | 15〜64歳（生産年齢人口） |
| 0190   | 65歳以上（老年人口）     |
| 0200   | 75歳以上                 |

高齢化率は「65歳以上人口（0190）÷ 総人口（0010）」で求めます。総人口は年齢不詳を含む値なので、年齢不詳の回答が多い地区では高齢化率がやや低くなります。境界データ（`small_area`）と町丁・字コードで結合すると、地図に描けます。千葉市の6区の値は次のとおりです。

```sql
SELECT REPLACE(b.city_name, '千葉市', '') AS 区, ROUND(SUM(CASE WHEN a.cat01 = '0010' THEN a.value END)) AS 人口, ROUND(100.0 * SUM(CASE WHEN a.cat01 = '0170' THEN a.value END) / SUM(CASE WHEN a.cat01 = '0010' THEN a.value END), 1) AS 年少人口率, ROUND(100.0 * SUM(CASE WHEN a.cat01 = '0190' THEN a.value END) / SUM(CASE WHEN a.cat01 = '0010' THEN a.value END), 1) AS 高齢化率 FROM e_stat.census.census_small_area_age a JOIN e_stat.boundary.small_area b ON a.area = b.key_code WHERE a.cat02 = '1' AND b.city_name LIKE '千葉市%' GROUP BY b.city_name ORDER BY 高齢化率 DESC
```

高齢化率は若葉区の30.4%から中央区の21.6%までで、差は約9ポイントです。若葉区・花見川区がやや高く、都心の機能が集まる中央区が最も低くなっています。

## 町丁・字別では、高齢化率は4.9%から76.6%まで分かれる

同じデータを町丁・字ごとに集計して地図にしました。人口の少ない地区では1世帯の転入・転出で高齢化率が10ポイント以上変わるので、総人口が100人以上の486地区に絞っています（秘匿されたセルも除いています）。そのため、千葉市のすべての町丁・字が地図に載っているわけではありません。

```map
type: map
layers:
  - from: aging_map
    geojson: geojson
    color: rate
    label: town
    name: "高齢化率（%）"
lng: 140.11
lat: 35.61
zoom: 10.2
```

高齢化率は最も低い地区で4.9%、最も高い地区で76.6%です。高齢化率が高い地区は市の内陸側や、丘陵に造成された住宅団地に集まり、低い地区は臨海部や近年開発が進んだエリアにあります。住宅地が開発された時期によって、住民の年齢構成が分かれていると考えられます。

## 同じ美浜区の中に、高齢化率54.0%の地区と4.9%の地区がある

高齢化率が対照的な町丁・字を取り出しました。

```sql
WITH age AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0190' THEN value END) AS sen FROM e_stat.census.census_small_area_age WHERE cat02 = '1' GROUP BY area) SELECT REPLACE(b.city_name, '千葉市', '') AS 区, b.area_name AS 町丁字, ROUND(a.tot) AS 人口, ROUND(100.0 * a.sen / a.tot, 1) AS 高齢化率 FROM age a JOIN e_stat.boundary.small_area b ON a.area = b.key_code WHERE b.area_name IN ('千城台南二丁目', '高浜六丁目', 'あすみが丘東五丁目', '幕張西四丁目') AND b.city_name LIKE '千葉市%' ORDER BY 高齢化率 DESC
```

美浜区の高浜六丁目は高齢化率54.0%で、住民の半分以上が65歳以上です。同じ美浜区の幕張西四丁目は4.9%で、高浜六丁目の10分の1以下です。美浜区の平均（26.3%）では、この2つの地区の違いは分かりません。高浜のような1970年代に一斉に入居した住宅団地では、入居した世代が同時に高齢期に入るので、高齢化率が急に上がります。あすみが丘東五丁目（緑区、5.0%）のような新しい戸建ての開発地区には子育て世帯が集まり、高齢化率は低くなっています。

## 年少人口率が低い町丁・字ほど、高齢化率が高い

町丁・字ごとに、年少人口率（15歳未満）と高齢化率（65歳以上）を散布図にしました。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "age_scatter"},
      "mark": {"type": "point", "color": "#7c3aed", "opacity": 0.5, "filled": true, "size": 36},
      "encoding": {
        "tooltip": [
          {"field": "town", "type": "nominal"},
          {"field": "young_rate", "type": "quantitative"},
          {"field": "aging_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "young_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年少人口率（15歳未満, %）", "grid": true}
        },
        "y": {
          "field": "aging_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（65歳以上, %）", "grid": true}
        }
      }
    }
  ]
}
```

点は右下がりに並び、年少人口率が低い町丁・字ほど高齢化率が高くなっています。図の左上（年少人口率が低く、高齢化率が高い）には、一斉入居のあとに子どもの世代が転出した住宅団地があります。右下（年少人口率が高く、高齢化率が低い）には、子育て世帯が流入した新しい開発地区があります。高齢者向けサービスの需要は左上の地区で大きく、右下の地区では将来の需要になると考えられます。

## 業務での使い方

- 出店・拠点配置の優先順位: 訪問介護・配食・調剤薬局などの拠点を、高齢化率と高齢者の人数が多い町丁・字から優先して検討する
- 需要の将来予測: 一斉入居の住宅団地ではこれから75歳以上の人口が増えるので、現在の高齢化率に加えて年齢構成の偏りから需要の増加を見込む
- エリアの使い分け: 子育て世帯が集まる新しい開発地区は、保育・教育・ファミリー向け小売など、高齢者向けとは別の業態の候補として扱う

高齢化率が高い地区で介護の需要が大きいとは限らず、同居家族の有無や住宅の形態によって必要なサービスは変わります。

## データの出典

本記事は総務省統計局の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計（[統計GIS](https://www.e-stat.go.jp/gis)）を、2026年7月11日時点で取得して集計しています。調査時点は2020年10月1日で、対象は千葉市の6区の町丁・字です。

Queriaは、国勢調査の小地域集計と境界データを、列名・単位・年齢区分のコードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[小地域 年齢別人口テーブル](/datasets/queria/e_stat/census/census_small_area_age)で対象の市区町村を変えると、ほかの市区町村でも同じ地図を描けます。

```sql id=aging_map
WITH age AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0190' THEN value END) AS sen FROM e_stat.census.census_small_area_age WHERE cat02 = '1' GROUP BY area) SELECT b.area_name AS town, ST_AsGeoJSON(ST_Simplify(b.geometry, 0.0003)) AS geojson, ROUND(100.0 * a.sen / a.tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY b.key_code) - 1 AS row_id FROM age a JOIN e_stat.boundary.small_area b ON a.area = b.key_code WHERE b.city_name LIKE '千葉市%' AND a.tot >= 100
```

```sql id=age_scatter
WITH age AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS tot, MAX(CASE WHEN cat01 = '0170' THEN value END) AS young, MAX(CASE WHEN cat01 = '0190' THEN value END) AS sen FROM e_stat.census.census_small_area_age WHERE cat02 = '1' GROUP BY area) SELECT b.area_name AS town, ROUND(100.0 * a.young / a.tot, 1) AS young_rate, ROUND(100.0 * a.sen / a.tot, 1) AS aging_rate FROM age a JOIN e_stat.boundary.small_area b ON a.area = b.key_code WHERE b.city_name LIKE '千葉市%' AND a.tot >= 100
```
