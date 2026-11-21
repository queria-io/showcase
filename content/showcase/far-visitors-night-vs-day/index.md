---
title: 遠くから来た人の数は、太宰府市・伊勢市・京都市東山区では夜に昼の3〜4割に減り、加賀市や下呂市では夜のほうが多い
description: 国土交通省の人流オープンデータで、遠くから人が集まる177市区町村の休日の昼と深夜の滞在人口を比較しました。深夜の人数を昼の人数で割った比は町によって0.16から1.56まで分かれ、2019年と2021年の比の相関係数は0.93です。
publishedAt: 2026-11-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 観光
  - 人流
  - 宿泊
  - 地図
datasets:
  - queria/geospatial
  - queria/nlftp
sources:
  - title: 全国の人流オープンデータ
    url: https://www.geospatial.jp/ckan/dataset/mlit-1km-fromto
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2024.html
    publisher: 国土交通省
agentHint: 自分の県の市町村ごとに、休日の昼と深夜にいる「他の地方」から来た人の数を2019年と2021年で出して、深夜が昼の何倍かを並べて
socialAnnounce: |-
  遠くから来た人が休日の昼と深夜に町に何人いるか比べました。

  太宰府市や京都市東山区では夜に昼の3〜4割に減り、加賀市や下呂市では夜のほうが多くなります。宿泊施策の検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

休日の昼に他の地方から来た人が4,888人いた福岡県太宰府市では、深夜にはその人数が1,675人になります。京都市東山区では深夜の人数が昼の0.40倍、三重県伊勢市では0.42倍です。石川県加賀市では1.33倍、岐阜県下呂市では1.41倍で、深夜のほうが多くなります。遠くから人が集まる177市区町村では、この比は0.16から1.56まで分かれ、中央値は0.74でした。

使ったのは国土交通省の[全国の人流オープンデータ](https://www.geospatial.jp/ckan/dataset/mlit-1km-fromto)です。スマートフォンの位置情報から推計した市区町村ごとの滞在人口が、滞在している人の居住地ごとに記録されています。この記事では、休日の昼（11〜14時台）と深夜（1〜4時台）に、他の地方から来た人が町に何人いるかを市区町村ごとに比較しました。深夜の人数を昼の人数で割った値を「夜と昼の比」と呼びます。比が1より小さい町では深夜に遠くからの人が減り、1より大きい町では深夜のほうが多くなります。同じ人を昼と夜に追跡した割合ではなく、それぞれの時間帯に滞在していた人数の比です。

下の地図は、遠くから人が集まる177市区町村（選び方は次の節）を、2019年の夜と昼の比で色分けしたものです。色が濃いほど、深夜にも遠くからの人が多く滞在しています。

```map
type: map
caption: 休日に他の地方から来た人の、深夜の人数 ÷ 昼の人数（2019年、177市区町村）
layers:
  - from: ratio_map
    area: city
    code: city_code
    color: ratio
    label: label
    name: 夜と昼の比
lng: 137.5
lat: 37.5
zoom: 4.3
```

## 177市区町村の夜と昼の比は0.16から1.56まで分かれ、中央値は0.74

使ったのは、全国の人流オープンデータを市区町村ごとにまとめたテーブル（`city_population_by_origin`）です。1行が、市区町村・月・平日か休日か・時間帯・滞在者の居住地の組み合わせで、人数は1か月の1日あたりの平均です。滞在者の居住地は次の4つに分かれています。

| 居住地の区分 | 内容                                                   |
| ------------ | ------------------------------------------------------ |
| 同一市区町村 | その市区町村に住んでいる人                             |
| 同一都道府県 | 同じ都道府県の別の市区町村に住んでいる人               |
| 同一地方     | 同じ地方（関東・近畿など）の別の都道府県に住んでいる人 |
| 他の地方     | それ以外の地方に住んでいる人                           |

この記事では「他の地方」に住んでいる人を、遠くから来た人として扱います。地方は北海道・東北・関東・北陸・中部・近畿・中国・四国・九州・沖縄の10区分です。京都市なら近畿の外、長野県の町なら中部の外に住む人が該当します。このデータの地方の区分では、新潟県は東北、山梨県は関東、三重県は中部に入ります。時間帯は昼（11〜14時台の平均）と深夜（1〜4時台の平均）、日は休日（土曜・日曜・祝日）を使い、2019年の12か月を平均しました。政令指定都市は区ごとの値です。

遠くから人が集まる市区町村として、2019年の休日の昼に他の地方から来た人が1日2,000人以上いて、その町にいる人全体の5%以上を占める266市区町村を選びました。このうち、別の地方の都道府県と境界を接する89市区町村は除いています。たとえば岐阜県白川村は富山県・石川県（北陸）と接しているので、「他の地方」から来た人の多くが、隣の県から日帰りで来る人である可能性があります。境界を接するかどうかは、[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2024.html)の境界線で判定したので、海を挟んで隣り合う町が除外に含まれることもあります。

残る177市区町村の夜と昼の比は0.16から1.56までの範囲にあり、中央値は0.74です。0.5を下回る町が23、1以上の町が23あります。

```chart
{
  "height": 260,
  "data": { "name": "towns" },
  "mark": { "type": "bar", "color": "#3b82f6" },
  "encoding": {
    "x": {
      "field": "ratio",
      "type": "quantitative",
      "bin": { "step": 0.1 },
      "title": "夜と昼の比（深夜の人数 ÷ 昼の人数、2019年）"
    },
    "y": { "aggregate": "count", "type": "quantitative", "title": "市区町村の数" },
    "tooltip": [{ "aggregate": "count", "title": "市区町村の数" }]
  }
}
```

## 比が最も小さいのは滋賀県竜王町の0.16、最も大きいのは札幌市中央区の1.56

比の小さい15市区町村と、大きい15市区町村です。

```chart
{
  "height": 620,
  "data": { "name": "ends" },
  "mark": "bar",
  "encoding": {
    "y": { "field": "label", "type": "nominal", "sort": "x", "title": null },
    "x": { "field": "ratio", "type": "quantitative", "title": "夜と昼の比（2019年）" },
    "color": {
      "field": "grp",
      "type": "nominal",
      "title": null,
      "scale": { "domain": ["夜に減る15", "夜に多い15"], "range": ["#f97316", "#7c3aed"] }
    },
    "tooltip": [
      { "field": "label", "title": "市区町村" },
      { "field": "far_day", "title": "昼（人）", "format": "," },
      { "field": "far_night", "title": "深夜（人）", "format": "," },
      { "field": "ratio", "title": "夜と昼の比", "format": ".2f" }
    ]
  }
}
```

比が最も小さいのは滋賀県竜王町の0.16で、沖縄県南城市が0.26、長野県小布施町が0.29、福井県勝山市と北海道千歳市が0.33で続きます。福岡県太宰府市は0.34で、昼に4,888人いた他の地方の人が、深夜には1,675人になります。京都市東山区は0.40、三重県伊勢市は0.42です。比が小さい町には、寺社や景勝地のある町のほかに、新千歳空港のある千歳市のように観光地とは限らない町も入ります。このデータには訪問の目的が記録されていないので、竜王町を含め、昼に人が集まる理由は町ごとに確認する必要があります。

比が1を超える町は2種類に分かれます。1つは、札幌市中央区（1.56）、名古屋市中区（1.14）、広島市中区（1.13）、那覇市（1.07）のような都市の中心部の区です。深夜の人数には、観光で宿泊する人のほかに出張で宿泊する人も含まれます。もう1つは、沖縄県恩納村（1.53）、岐阜県下呂市（1.41）、福井県あわら市（1.38）、石川県加賀市（1.33）、石川県七尾市（1.17）、三重県鳥羽市（1.07）のような、都市から離れた町です。これらの町では、昼には町の外へ出かけている遠くからの人が深夜に町へ戻るか、夕方以降に到着して宿泊していると考えられます。

## 京都市では、区によって0.40から1.22まで分かれる

京都市の11区について、休日の昼と深夜に他の地方（近畿の外）から来た人の数を並べました。

```chart
{
  "height": 340,
  "data": { "name": "kyoto" },
  "encoding": {
    "y": {
      "field": "city_name",
      "type": "nominal",
      "sort": { "field": "ratio", "order": "ascending" },
      "title": null
    }
  },
  "layer": [
    {
      "mark": { "type": "rule", "color": "#cbd5e1", "strokeWidth": 3 },
      "encoding": {
        "x": { "field": "far_day", "type": "quantitative", "title": "他の地方から来た人（1日あたり、2019年の休日）" },
        "x2": { "field": "far_night" }
      }
    },
    {
      "mark": { "type": "point", "filled": true, "size": 90 },
      "encoding": {
        "x": { "field": "people", "type": "quantitative" },
        "color": {
          "field": "time",
          "type": "nominal",
          "title": null,
          "scale": { "domain": ["昼", "深夜"], "range": ["#f97316", "#7c3aed"] }
        },
        "tooltip": [
          { "field": "city_name", "title": "区" },
          { "field": "time", "title": "時間帯" },
          { "field": "people", "title": "人数", "format": "," },
          { "field": "ratio", "title": "夜と昼の比", "format": ".2f" }
        ]
      },
      "transform": [{ "fold": ["far_day", "far_night"], "as": ["key", "people"] }, { "calculate": "datum.key === 'far_day' ? '昼' : '深夜'", "as": "time" }]
    }
  ]
}
```

東山区は昼に16,716人いて、深夜には6,684人になります（比0.40）。右京区（0.50）、左京区（0.53）、伏見区（0.62）も深夜に大きく減ります。京都駅のある下京区は昼29,163人・深夜26,699人（0.92）、中京区は1.01で、同じく京都駅のある南区は1.22と深夜のほうが多くなります。京都市全体では0.75です。寺社の多い区では深夜に大きく減り、駅や中心部の区では深夜もほとんど減りません。

## 2019年と2021年の比の相関係数は0.93で、町の順位はほとんど変わらない

177市区町村の休日の昼にいた他の地方の人は、合計で2019年の1日223.7万人から、2021年には105.1万人に減りました。一方で、2019年と2021年の夜と昼の比の相関係数は0.93で、町の順位はほとんど変わりません。比は、その年の人出の多さではなく、宿泊施設の場所や日帰りで来られる範囲のように、年が変わっても変わらない条件で決まっていると考えられます。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": { "values": [{ "x": 0.1, "y": 0.1 }, { "x": 1.6, "y": 1.6 }] },
      "mark": { "type": "line", "color": "#94a3b8", "strokeDash": [4, 4] },
      "encoding": {
        "x": { "field": "x", "type": "quantitative" },
        "y": { "field": "y", "type": "quantitative" }
      }
    },
    {
      "data": { "name": "towns" },
      "mark": { "type": "circle", "color": "#3b82f6", "opacity": 0.6, "stroke": "#fff" },
      "encoding": {
        "x": { "field": "ratio", "type": "quantitative", "title": "夜と昼の比（2019年）" },
        "y": { "field": "ratio_2021", "type": "quantitative", "title": "夜と昼の比（2021年）" },
        "size": { "field": "far_day", "type": "quantitative", "title": "昼の人数（2019年）" },
        "tooltip": [
          { "field": "prefecture", "title": "都道府県" },
          { "field": "city_name", "title": "市区町村" },
          { "field": "ratio", "title": "2019年", "format": ".2f" },
          { "field": "ratio_2021", "title": "2021年", "format": ".2f" }
        ]
      }
    }
  ]
}
```

点線より上の町は、2021年に比が上がった町です。2019年に比が0.5を下回っていた23市区町村のうち、20で比が上がりました。この20の町では、遠くからの人が減った2年間に、昼の人数のほうが深夜の人数より大きく減っています。

## 宿泊や滞在の施策での使い方

- 自分の町の夜と昼の比を、同じ県の観光地や、同じような観光資源を持つ町と比較できます。比が小さい町では、昼に来た遠くからの人が深夜には町にいないので、宿泊施設の誘致や夜の催しを検討する材料になります
- 比が小さい町と、近くの比が大きい町を組み合わせて確認できます。京都市の東山区と下京区のように、昼に人が集まる区と深夜に人がいる区が異なる場合は、宿泊の施策を近くの自治体と周遊の計画として検討する材料になります
- 宿泊や夜の催しの施策の前後で、夜と昼の比を昼と深夜の人数と一緒に記録できます。比は昼の人数が減っただけでも上がるので、深夜の人数が増えて比が上がったときに、夜まで滞在する人が増えた目安として使えます

## データの出典

本記事は国土交通省の[全国の人流オープンデータ](https://www.geospatial.jp/ckan/dataset/mlit-1km-fromto)のうち、市区町村単位の発地別の滞在人口（2019年1月〜2021年12月）を、2026-11-13 時点で集計しています。元データは、スマートフォンの位置情報から推計した値です。地方の境界を接するかどうかの判定と地図の境界には、国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2024.html)を使っています。

Queria は、全国の人流オープンデータを、市区町村・月・時間帯・滞在者の居住地ごとに取得できるテーブルにまとめ、列の意味をメタデータに記載して公開しています。本記事で使った[市区町村別・居住地別の滞在人口のテーブル](/datasets/queria/geospatial/people_flow/city_population_by_origin)から、自分の町の昼と夜、平日と休日、月ごとの違いを確認できます。

```sql id=base
-- 市区町村（政令指定都市は区）ごと・年ごとの、休日に他の地方から来た人の昼と深夜の人数と、昼の滞在人口の合計（1日あたり、12か月の平均）
SELECT
  p.city_code,
  c.prefecture,
  c.city_name,
  p.year,
  sum(p.population) FILTER (WHERE p.time_of_day = '昼' AND p.origin = '他の地方') / 12.0 AS far_day,
  sum(p.population) FILTER (WHERE p.time_of_day = '深夜' AND p.origin = '他の地方') / 12.0 AS far_night,
  sum(p.population) FILTER (WHERE p.time_of_day = '昼') / 12.0 AS all_day
FROM geospatial.people_flow.city_population_by_origin p
JOIN geospatial.people_flow.city c USING (city_code)
WHERE p.day_type = '休日'
  AND p.time_of_day IN ('昼', '深夜')
  AND p.year IN (2019, 2021)
GROUP BY ALL
```

```sql id=border
-- 別の地方の都道府県と境を接する市区町村（政令指定都市は区）
WITH region AS (
  SELECT DISTINCT prefecture_code, region FROM geospatial.people_flow.city
)
SELECT DISTINCT m.lg_code AS city_code
FROM nlftp.boundary.municipality m
JOIN region rm ON rm.prefecture_code = m.prefecture_code
JOIN nlftp.boundary.prefecture p ON p.prefecture_code <> m.prefecture_code
JOIN region rp ON rp.prefecture_code = p.prefecture_code AND rp.region <> rm.region
WHERE ST_Intersects(m.geometry, p.geometry)
```

```sql id=candidates
-- 2019年の休日の昼に他の地方から来た人が2,000人以上で、昼の滞在人口の5%以上を占める市区町村
SELECT
  a.*,
  b.far_day AS far_day_2021,
  b.far_night AS far_night_2021,
  a.city_code IN (SELECT city_code FROM border) AS on_border
FROM base a
JOIN base b ON b.city_code = a.city_code AND b.year = 2021
WHERE a.year = 2019
  AND a.far_day >= 2000
  AND a.far_day / a.all_day >= 0.05
```

```sql id=towns
-- 別の地方と境を接する市区町村を除いた、遠くから人が集まる市区町村
SELECT
  a.city_code,
  a.prefecture,
  a.city_name,
  round(a.far_day) AS far_day,
  round(a.far_night) AS far_night,
  round(a.far_day_2021) AS far_day_2021,
  round(100 * a.far_day / a.all_day, 1) AS far_share,
  round(a.far_night / a.far_day, 2) AS ratio,
  round(a.far_night_2021 / a.far_day_2021, 2) AS ratio_2021
FROM candidates a
WHERE NOT a.on_border
```

```sql id=summary
-- 本文の件数・中央値・相関（プロットはしない）
SELECT
  (SELECT count(*) FROM candidates) AS candidates,
  (SELECT count(*) FROM candidates WHERE on_border) AS on_border,
  count(*) AS towns,
  round(sum(far_day) / 10000, 1) AS far_day_2019_man,
  round(sum(far_day_2021) / 10000, 1) AS far_day_2021_man,
  min(ratio) AS min_ratio,
  max(ratio) AS max_ratio,
  median(ratio) AS median_ratio,
  count(*) FILTER (WHERE ratio < 0.5) AS below_half,
  count(*) FILTER (WHERE ratio >= 1) AS at_least_one,
  count(*) FILTER (WHERE ratio < 0.5 AND ratio_2021 > ratio) AS below_half_rose,
  round(corr(ratio, ratio_2021), 2) AS corr_2019_2021
FROM towns
```

```sql id=ratio_map
SELECT
  city_code,
  ratio,
  prefecture || city_name || '：昼 ' || far_day::INTEGER || '人・深夜 ' || far_night::INTEGER || '人（' || ratio || '）' AS label
FROM towns
```

```sql id=ends
WITH r AS (
  SELECT
    *,
    row_number() OVER (ORDER BY ratio, city_code) AS lo,
    row_number() OVER (ORDER BY ratio DESC, city_code) AS hi
  FROM towns
)
SELECT
  prefecture || city_name AS label,
  far_day,
  far_night,
  ratio,
  CASE WHEN lo <= 15 THEN '夜に減る15' ELSE '夜に多い15' END AS grp
FROM r
WHERE lo <= 15 OR hi <= 15
ORDER BY ratio
```

```sql id=kyoto
-- 京都市の11区（2019年）。区は遠くから人が集まる市区町村の条件で絞らない
SELECT
  city_name,
  round(far_day) AS far_day,
  round(far_night) AS far_night,
  round(far_night / far_day, 2) AS ratio
FROM base
WHERE year = 2019 AND city_code LIKE '261%'
ORDER BY ratio
```

```sql id=kyoto_total
-- 京都市全体の夜と昼の比（プロットはしない）
SELECT round(sum(far_night) / sum(far_day), 2) AS ratio
FROM base
WHERE year = 2019 AND city_code LIKE '261%'
```
