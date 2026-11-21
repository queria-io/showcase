---
title: 江東区の中古マンションの㎡単価は、豊洲の113.1万円より西部の永代の128.0万円が高い
description: 国勢調査の小地域と不動産取引価格を丁目・町名の単位で集計しました。江東区の中古マンションの㎡単価は永代の128.0万円が最も高く、豊洲は113.1万円です。世帯数密度は1平方キロメートルあたり一桁から2万世帯前後まで、丁目ごとに差があります。
publishedAt: 2026-05-31
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
  - queria/reinfolib
sources:
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 不動産情報ライブラリ
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
agentHint: 江東区の中古マンション㎡単価を町名別に、2015〜2019年と2020〜2024年で比べて、値上がりが大きい町名を出して
socialAnnounce: |-
  住宅需要は丁目・町名まで下りると解像度が変わります。江東区の中古マンション㎡単価は永代128万円・豊洲113万円。世帯数密度も丁目で大きく差。

  物件取得や出店のエリア見極めに。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

東京都江東区の中古マンションの㎡単価（2020〜2024年の取引の中央値）は、永代の128.0万円、門前仲町の125.0万円、佐賀の124.0万円が上位で、都心に近い西部の町が高くなっています。タワーマンションで知られる臨海部の豊洲は113.1万円、有明は111.7万円です。丁目ごとの世帯数密度は、北部の新大橋・富岡・扇橋などで1平方キロメートルあたり2万世帯前後あり、臨海部の有明三・四丁目や青海二丁目では一桁から千台にとどまります。

前々回・前回の記事では、賃貸需要の代わりの指標として民営借家率を[都道府県](/showcase/housing-tenure-regional-gap)と[市区町村・区](/showcase/municipal-rental-demand-gap)の単位で集計しました。持ち家・民営借家といった住宅の所有形態は、もとの住宅・土地統計調査が標本調査なので市区町村が最小単位で、丁目・大字の値はありません。本記事では、丁目・町名の単位で取得できる2つのデータ、全数調査である[国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計（世帯数）と、[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)の不動産取引価格（中古マンション）を組み合わせ、江東区の中で住宅需要と価格がどう分布しているかを確認します。

## 使うデータは、丁目単位の世帯数と町名単位の取引価格

2つのデータを丁目・町名の単位で使います。

| データ                                | 単位             | 内容                         |
| ------------------------------------- | ---------------- | ---------------------------- |
| 国勢調査 小地域（`small_area`）       | 丁目（町丁・字） | 人口・世帯数・境界（2020年） |
| 不動産取引価格（`mart_trade_prices`） | 町名（地区）     | 中古マンションの取引価格     |

国勢調査小地域は全数調査なので、丁目単位の世帯数まで把握できます。不動産取引価格は町名（丁目番号を除いた大字・町名）単位です。中古マンションの取引価格を専有面積で割った㎡単価の中央値を、2020〜2024年の取引件数が10件以上の町名について算出します。

## 世帯数密度は、北部の住宅地で1平方キロメートルあたり2万世帯前後

江東区の丁目ごとの世帯数密度（1平方キロメートルあたりの世帯数）を地図にしました。世帯数が0の小地域と、面積が取得できない小地域は除いています。

```map
type: map
layers:
  - from: density_map
    geojson: geojson
    color: value
    label: pref_name
    name: "世帯密度（世帯/km²）"
lng: 139.81
lat: 35.655
zoom: 11.5
```

北部の住宅地（新大橋・富岡・扇橋など）や大島の集合住宅地区は、1平方キロメートルあたり2万世帯前後です。南部の臨海部は丁目ごとの差が大きく、有明三・四丁目や青海二丁目のように開発途中で世帯数密度が一桁から千台にとどまる地区がある一方、東雲一丁目のようにタワーマンションへの入居が進み1万8千世帯を超える地区もあります。世帯数密度は、その丁目に住む世帯の数、つまり住宅需要の規模を表します。世帯数は2020年の値なので、その後に竣工したマンションへの入居は含みません。

## 中古マンションの㎡単価は、永代・門前仲町・佐賀が上位

中古マンションの取引価格から算出した㎡単価の上位15町名です。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "price_rank"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "man", "type": "quantitative"},
          {"field": "district_name", "type": "nominal"}
        ],
        "x": {
          "field": "man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "中古マンション㎡単価（万円）", "grid": true}
        },
        "y": {
          "field": "district_name",
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

㎡単価が高いのは永代（128.0万円）、門前仲町（125.0万円）、佐賀（124.0万円）など、都心に近い西部の町です。タワーマンションで知られる豊洲（113.1万円）や有明（111.7万円）も高い水準ですが、上位3町名より低くなっています。新しい住宅の供給が集中した臨海部より、都心に近い西部の町のほうが単価が高いことが分かります。㎡単価は築年数・階数・間取り・駅からの距離を調整していないので、町名どうしの差には物件の違いも含まれます。

## ㎡単価は、西部と臨海部で高く、中央部と北部でやや低い

町名ごとの㎡単価を丁目の境界に塗って地図にしました。丁目名から末尾の「〜丁目」を除いて町名と照合しているので、名称が一致しない丁目と、取引件数が10件に満たない町名の丁目には色が付きません。

```map
type: map
layers:
  - from: price_map
    geojson: geojson
    color: value
    label: pref_name
    name: "㎡単価（万円）"
lng: 139.81
lat: 35.655
zoom: 11.5
```

価格は西部（永代・門前仲町・清澄など）と臨海部（豊洲・有明）で高く、その間の中央部や北部でやや低くなっています。取引のない丁目（工業地区や公園など）には色が付いていません。同じ江東区の中でも、丁目・町名の単位で集計すると、世帯数密度と価格の水準は場所によって少しずつ変わります。

## 業務への活用

丁目・町名の単位のデータは、物件取得や出店のエリアを最後に絞り込む段階で使えます。

- 立地の評価: 市区町村でエリアを絞った後、丁目ごとの世帯数密度で商圏の規模を、町名ごとの取引価格で資産価値の水準を確認する
- 需要と価格の比較: 世帯数密度が高く、価格が比較的低い丁目は、賃貸・店舗ともに費用に対して需要の大きい立地と考えられる
- 開発余地の把握: 臨海部のように世帯数密度が低い地区は、今後の住宅供給で需要が増える余地があると考えられる

所有形態（持ち家・民営借家）は市区町村が最小単位ですが、世帯数密度と取引価格は丁目・町名の単位で集計できます。都道府県・市区町村の民営借家率から丁目の世帯数密度・町名の価格まで順に確認すると、エリアの評価を細かくできます。

## データの出典

本記事は総務省統計局の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)小地域集計と、国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公開する不動産取引価格情報を、2026年7月11日時点で取得して集計しています。対象は東京都江東区です。

Queriaは、国勢調査や不動産取引価格を、列名と単位を統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[不動産取引価格のテーブル](/datasets/queria/reinfolib/main/mart_trade_prices)で対象の市区町村を変えると、ほかの区や市でも町名ごとの㎡単価を集計できます。

```sql id=density_map
SELECT s.area_name AS pref_name, ST_AsGeoJSON(ST_Simplify(s.geometry, 0.0003)) AS geojson, ROUND(s.setai / (s.area_m2 / 1000000)) AS value, ROW_NUMBER() OVER (ORDER BY s.area_name) - 1 AS row_id FROM e_stat.boundary.small_area s WHERE s.city_name = '江東区' AND s.setai > 0 AND s.area_m2 > 0
```

```sql id=price_rank
WITH p AS (SELECT district_name, ROUND(MEDIAN(trade_price / area) / 10000, 1) AS man FROM reinfolib.main.mart_trade_prices WHERE municipality = '江東区' AND property_type = '中古マンション等' AND trade_price > 0 AND area > 0 AND year BETWEEN 2020 AND 2024 GROUP BY district_name HAVING COUNT(*) >= 10) SELECT district_name, man FROM (SELECT district_name, man FROM p ORDER BY man DESC LIMIT 15) ORDER BY man ASC
```

```sql id=price_map
WITH price AS (SELECT district_name, ROUND(MEDIAN(trade_price / area) / 10000, 1) AS man FROM reinfolib.main.mart_trade_prices WHERE municipality = '江東区' AND property_type = '中古マンション等' AND trade_price > 0 AND area > 0 AND year BETWEEN 2020 AND 2024 GROUP BY district_name HAVING COUNT(*) >= 10) SELECT s.area_name AS pref_name, ST_AsGeoJSON(ST_Simplify(s.geometry, 0.0003)) AS geojson, p.man AS value, ROW_NUMBER() OVER (ORDER BY s.area_name) - 1 AS row_id FROM e_stat.boundary.small_area s JOIN price p ON REGEXP_REPLACE(s.area_name, '(一|二|三|四|五|六|七|八|九|十)+丁目$', '') = p.district_name WHERE s.city_name = '江東区' AND s.setai > 0
```
