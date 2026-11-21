---
title: 津波の浸水が想定される場所に住む65歳以上は、25年で大阪市・横浜市では2万人超増え、地方の沿岸24市町村で4割以上減る
description: 津波浸水想定区域と500m四方の将来推計人口を重ねました。28道府県の区域内に住む人は2050年までに17.6%減り、65歳以上は4.6%増えます。
publishedAt: 2026-10-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 防災
  - 津波
  - 将来推計人口
  - 高齢化
datasets:
  - queria/nlftp
  - queria/soumu
sources:
  - title: 国土数値情報 津波浸水想定データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A40-2024.html
    publisher: 国土交通省
  - title: 国土数値情報 500mメッシュ別将来推計人口データ（R6国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh500r6.html
    publisher: 国土交通省
agentHint: 津波浸水想定区域のうち浸水深の下限（depth_min_m）が2m以上の範囲に中心点が入る500mメッシュだけに絞って、市区町村ごとに2025年と2050年の65歳以上人口を出して。区域全体で見たときと増減の顔ぶれが変わるかも比べて
socialAnnounce: |-
  津波の浸水想定区域と、500m四方の将来推計人口を重ねました。

  区域内の人口は2050年までに17.6%減り、65歳以上は4.6%増えます。津波避難計画の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

津波の浸水が想定される場所に住む人は、28道府県の合計で2025年の約605万人から2050年に約499万人へ17.6%減り、そのうち65歳以上は約180万人から約188万人へ4.6%増えます。市区町村別では、大阪市・横浜市・広島市で区域内の65歳以上が2万人以上増え、地方の沿岸の24市町村では4割以上減ります。

沿岸の市区町村で津波避難計画や避難行動要支援者の個別避難計画を担当している職員は、区域内にいま何人住んでいて、そのうち支援が必要な人が何人いるかをもとに計画を立てます。避難路や避難タワーのように何十年も使う設備を検討するときは、25年後に区域内に住む人の数と年齢構成も必要になります。区域内に住む人の年齢構成は、人口の増減とは別に変わります。

## 浸水が想定される場所に住む65歳以上は、2025年の約180万人から2050年に約188万人に増える

この記事では、国土交通省の国土数値情報から2つのデータを重ねます。

| テーブル                                       | 内容                                                                                                                                                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nlftp.hazard.tsunami_inundation`              | [津波浸水想定](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A40-2024.html)。都道府県が津波防災地域づくり法に基づいて設定した、最大クラスの津波で浸水する範囲のポリゴン                             |
| `nlftp.population.future_population_mesh_500m` | [500mメッシュ別将来推計人口](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh500r6.html)。500m四方の区画ごとの2025年・2035年・2050年の人口（`population_*`）と65歳以上の割合（`elderly_ratio_*`） |

区画の中心点が浸水想定区域のポリゴンに入っていれば、その区画を「浸水が想定される場所」として集計します。区画の一部だけが浸水する海沿いの区画は、中心点が区域の外なら集計に含まれないので、ここでの人数は区域に住む人のおおよその規模です。65歳以上の人数は、区画ごとに人口と65歳以上の割合を掛けて合計しています。避難行動要支援者名簿の対象は要介護度や障害の有無などで決まるので、ここでの65歳以上は、支援が必要な人を多く含む年齢層の規模の目安です。

将来推計人口は、2020年の国勢調査の区画ごとの男女・年齢の構成に、市区町村ごとの将来推計の仮定（生残率や転入・転出の傾向）を当てはめて作られています。2025年の値も、この方法による推計値です。

津波浸水想定は、提供元が商用利用と再配布を認めている28道府県だけを収録しています。宮城県・千葉県・東京都・三重県・愛媛県・大分県・宮崎県などは含まれていないので、以下の数字は28道府県の合計です。

この28道府県で、浸水が想定される場所に住む人は2025年に約605万人で、そのうち65歳以上は約180万人です。2050年には人口が約499万人まで減る一方、65歳以上は約188万人に増えます。

```chart
{
  "layer": [
    {
      "data": {"name": "zone_total"},
      "transform": [
        {"fold": ["under65", "elderly"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"under65\": \"65歳未満\", \"elderly\": \"65歳以上\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"under65\",\"elderly\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "year_label",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "津波浸水想定区域に住む人（人）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["65歳未満", "65歳以上"], "range": ["#93c5fd", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "year_label", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

人口が減るのは65歳未満です。65歳未満は約425万人から約310万人へ27.0%減り、65歳以上は4.6%増えます。区域内の65歳以上1人に対する65歳未満の人数は、2.36人から1.65人になります。避難の声かけや付き添いをする側の人数が、支援を受ける側の人数に対して3割ほど少なくなります。

同じ28道府県の区域の外でも、人口は17.7%減り、65歳以上は3.5%増えます。区域の中でも、地域全体とほぼ同じ変化が起きます。

## 区域内の65歳以上は、神奈川県で29.7%増え、石川県で37.5%減る

浸水が想定される場所に住む人について、2025年から2050年までの人口と65歳以上の増減率を道府県ごとに並べました。

```chart
{
  "height": 780,
  "layer": [
    {
      "data": {"name": "pref_change"},
      "transform": [
        {"fold": ["pop_change_pct", "elderly_change_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"pop_change_pct\": \"人口\", \"elderly_change_pct\": \"65歳以上\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"pop_change_pct\",\"elderly_change_pct\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {"field": "pref_name", "type": "nominal", "axis": {"title": ""}, "sort": null},
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2025年から2050年の増減率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["人口", "65歳以上"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["65歳以上", "人口"]},
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

人口はすべての道府県で減りますが、65歳以上が増えるのは8府県です。神奈川県が29.7%増、沖縄県が28.6%増、広島県が20.8%増と大きく、大阪府・兵庫県・愛知県も1割前後増えます。石川県は37.5%減、富山県は24.7%減で、区域内の人口の減少率に近い割合で65歳以上も減ります。

増える8府県のうち、神奈川県・大阪府・愛知県・兵庫県・広島県は、横浜市・大阪市・名古屋市・神戸市・広島市といった大都市の市街地を区域に含みます。

## 区域内の65歳以上は、大都市で増え、地方の沿岸の市町村で減る

政令指定都市の行政区を市にまとめ、2025年に浸水が想定される場所に1,000人以上が住む280市区町村を比較しました。複数の市区町村にまたがる区画は、どの市区町村にも割り当てずに除いています。福島県の沿岸部は将来推計が浜通りの市町村をまとめた1つの単位で作られているので、市区町村別の比較には含めていません。

280市区町村のうち、区域内の65歳以上が2050年までに増えるのは80、減るのは200です。増える人数が多い10市区町村は次のとおりです。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "city_rank"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "up_elderly_change_pct", "type": "quantitative"},
          {"field": "up_elderly_increase", "type": "quantitative"},
          {"field": "up_label", "type": "nominal"}
        ],
        "x": {
          "field": "up_elderly_increase",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "浸水想定区域に住む65歳以上の増加数（人、2025→2050年）", "grid": true}
        },
        "y": {"field": "up_label", "type": "nominal", "axis": {"title": ""}, "sort": null}
      }
    },
    {
      "data": {"name": "city_rank"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "up_elderly_increase",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "浸水想定区域に住む65歳以上の増加数（人、2025→2050年）", "grid": true}
        },
        "y": {"field": "up_label", "type": "nominal", "axis": {"title": ""}, "sort": null},
        "text": {"field": "up_elderly_change_pct"}
      }
    }
  ]
}
```

大阪市（25,146人増）、横浜市（24,700人増）、広島市（21,901人増）、川崎市（18,156人増）の4市は、区域内の65歳以上がそれぞれ2万人前後増えます。川崎市は区域内の人口も2050年まで増える推計で、65歳以上は34.7%増えます。ほかの市は区域内の人口が減るので、避難する人の総数は減りますが、そのうち手助けが必要になりうる人の数は増えます。

区域内の65歳以上の減少率が大きい10市町村は次のとおりです。推計は2020年の国勢調査をもとにしており、2024年の能登半島地震の後の人口の変化は含みません。人数の少ない区画の65歳以上は秘匿のため隣の区画に合算して公表されているので、区域内の人口が千人台の町ほど、増減率は区域の範囲の影響を受けやすくなります。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "city_rank"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "down_elderly_change_pct", "type": "quantitative"},
          {"field": "down_label", "type": "nominal"}
        ],
        "x": {
          "field": "down_elderly_change_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "浸水想定区域に住む65歳以上の増減率（%、2025→2050年）", "grid": true}
        },
        "y": {"field": "down_label", "type": "nominal", "axis": {"title": ""}, "sort": null}
      }
    }
  ]
}
```

高知県室戸市では区域内の65歳以上が55.2%減り、ほかの9市町も4割台の減少です。4割以上減る市町村は280のうち24あり、いずれも地方の沿岸の市町村です。人数が減るので支援の対象は少なくなりますが、上の10市町村では2050年に区域内の住民の5割から7割が65歳以上になります。

65歳以上が減る200市区町村のうち195では、65歳未満がそれより大きい割合で減ります。280市区町村のうち、区域内で65歳以上が65歳未満より多い市区町村は、2025年の15から2050年には87に増えます。支援の対象者が減る町でも、地域で支援できる人はそれ以上に減ります。

## 業務での活用

- 自分の市区町村の区域内の65歳以上が、2050年までに増えるか減るかを確認する。個別避難計画で支援者を割り当てるとき、いまの名簿の人数に加えて、25年後に対象となりうる人の規模を見込む材料になります
- 65歳以上1人あたりの65歳未満の人数を区域単位で確認し、地域で支援できる人数の見通しを立てる。65歳未満が減っていく町では、自主防災組織以外の支援の方法を早めに検討する材料になります
- 同じ県の中でも増減の向きが分かれるので、県単位の推計でなく、市区町村や区画の単位で避難計画の前提を見直す

## データの出典

本記事は国土交通省の国土数値情報から、[津波浸水想定データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A40-2024.html)と[500mメッシュ別将来推計人口データ（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh500r6.html)を、2026年10月9日時点で集計しています。将来推計人口は総務省「令和2年国勢調査」と国立社会保障・人口問題研究所「日本の地域別将来推計人口（令和5年推計）」に基づく推計値です。

Queriaは、国土数値情報を、列名と座標系を統一し、各列の意味をメタデータとして付けて公開しています。本記事で使った[津波浸水想定のテーブル](/datasets/queria/nlftp/hazard/tsunami_inundation)と[500mメッシュの将来推計人口のテーブル](/datasets/queria/nlftp/population/future_population_mesh_500m)を空間結合すると、自分の市区町村の区域に住む人の将来の人数と年齢構成を確認できます。

```sql id=zone_city
-- 500mメッシュの中心点が津波浸水想定区域に入るかで区域の内外を分け、市区町村コードごとに合計する
-- 65歳以上人口は、メッシュごとの「人口 × 65歳以上の割合」を合計して求める
WITH mesh AS (
  SELECT
    mesh_id,
    city_code,
    population_2025,
    population_2050,
    population_2025 * elderly_ratio_2025 / 100 AS elderly_2025,
    population_2050 * elderly_ratio_2050 / 100 AS elderly_2050,
    ST_Centroid(geometry) AS center
  FROM nlftp.population.future_population_mesh_500m
  WHERE left(city_code, 2) IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation)
),
hit AS (
  SELECT DISTINCT mesh.mesh_id, mesh.city_code
  FROM mesh
  JOIN nlftp.hazard.tsunami_inundation AS t ON ST_Intersects(mesh.center, t.geometry)
)
SELECT
  left(mesh.city_code, 2) AS pref_code,
  mesh.city_code,
  hit.mesh_id IS NOT NULL AS in_zone,
  sum(mesh.population_2025) AS pop_2025,
  sum(mesh.population_2050) AS pop_2050,
  sum(mesh.elderly_2025) AS elderly_2025,
  sum(mesh.elderly_2050) AS elderly_2050
FROM mesh
LEFT JOIN hit USING (mesh_id, city_code)
GROUP BY ALL
```

```sql id=zone_total
-- 28道府県の区域内の人口を65歳未満と65歳以上に分ける。区域外（out_*）は本文の比較用でプロットしない
WITH s AS (
  SELECT
    sum(pop_2025) FILTER (WHERE in_zone) AS p25,
    sum(pop_2050) FILTER (WHERE in_zone) AS p50,
    sum(elderly_2025) FILTER (WHERE in_zone) AS e25,
    sum(elderly_2050) FILTER (WHERE in_zone) AS e50,
    sum(pop_2025) FILTER (WHERE NOT in_zone) AS op25,
    sum(pop_2050) FILTER (WHERE NOT in_zone) AS op50,
    sum(elderly_2025) FILTER (WHERE NOT in_zone) AS oe25,
    sum(elderly_2050) FILTER (WHERE NOT in_zone) AS oe50
  FROM zone_city
)
SELECT
  '2025年' AS year_label,
  round(p25) AS total,
  round(p25 - e25) AS under65,
  round(e25) AS elderly,
  round((p25 - e25) / e25, 2) AS under65_per_elderly,
  NULL AS total_change_pct,
  NULL AS under65_change_pct,
  NULL AS elderly_change_pct,
  NULL AS out_total_change_pct,
  NULL AS out_elderly_change_pct
FROM s
UNION ALL
SELECT
  '2050年',
  round(p50),
  round(p50 - e50),
  round(e50),
  round((p50 - e50) / e50, 2),
  round(100 * (p50 / p25 - 1), 1),
  round(100 * ((p50 - e50) / (p25 - e25) - 1), 1),
  round(100 * (e50 / e25 - 1), 1),
  round(100 * (op50 / op25 - 1), 1),
  round(100 * (oe50 / oe25 - 1), 1)
FROM s
```

```sql id=pref_change
-- 道府県ごとの区域内の人口と65歳以上の増減率（2025→2050年）
SELECT
  p.pref_name,
  round(sum(z.pop_2025)) AS pop_2025,
  round(100 * (sum(z.pop_2050) / sum(z.pop_2025) - 1), 1) AS pop_change_pct,
  round(100 * (sum(z.elderly_2050) / sum(z.elderly_2025) - 1), 1) AS elderly_change_pct
FROM zone_city AS z
JOIN soumu.code.municipality AS p ON p.area_code = z.pref_code || '000'
WHERE z.in_zone
GROUP BY p.pref_name
ORDER BY elderly_change_pct DESC, p.pref_name
```

```sql id=city_rank
-- 区域内に2025年に1,000人以上が住む市区町村について、65歳以上の増加数の上位10（up_*）と減少率の上位10（down_*）を横に並べる
-- 件数の列（cities 以降）は全行で同じ値。本文の件数の裏付けで、プロットはしない
WITH city_zone AS (
  -- 政令指定都市の行政区は市にまとめる。浜松市は2024年の区再編前の区コード（22131〜22137）で入っているので、市にまとめるため現行の区コード 22138 に寄せる
  -- 複数の市区町村にまたがるメッシュ（city_code が "_" でつながる行）と、福島県浜通りをまとめた 07999 はどの市区町村にも当たらない
  SELECT
    coalesce(c.designated_city_name, c.municipality_name) || '（' || c.pref_name || '）' AS label,
    sum(z.pop_2025) AS pop_2025,
    sum(z.pop_2050) AS pop_2050,
    sum(z.elderly_2025) AS elderly_2025,
    sum(z.elderly_2050) AS elderly_2050
  FROM zone_city AS z
  JOIN soumu.code.municipality AS c
    ON c.area_code = CASE WHEN z.city_code IN ('22131', '22132', '22133', '22134', '22135', '22136', '22137') THEN '22138' ELSE z.city_code END
  WHERE z.in_zone
  GROUP BY ALL
  HAVING sum(z.pop_2025) >= 1000
),
up AS (
  SELECT
    row_number() OVER (ORDER BY elderly_2050 - elderly_2025 DESC, label) AS rn,
    label AS up_label,
    round(elderly_2050 - elderly_2025) AS up_elderly_increase,
    round(100 * (elderly_2050 / elderly_2025 - 1), 1) AS up_elderly_change_pct,
    round(100 * (pop_2050 / pop_2025 - 1), 1) AS up_pop_change_pct
  FROM city_zone
),
down AS (
  SELECT
    row_number() OVER (ORDER BY elderly_2050 / elderly_2025, label) AS rn,
    label AS down_label,
    round(100 * (elderly_2050 / elderly_2025 - 1), 1) AS down_elderly_change_pct,
    round(100 * elderly_2050 / pop_2050, 1) AS down_elderly_share_2050_pct
  FROM city_zone
),
counts AS (
  SELECT
    count(*) AS cities,
    count(*) FILTER (WHERE elderly_2050 > elderly_2025) AS elderly_up,
    count(*) FILTER (WHERE elderly_2050 < elderly_2025) AS elderly_down,
    count(*) FILTER (WHERE elderly_2050 <= elderly_2025 * 0.6) AS elderly_down_40pct,
    count(*) FILTER (
      WHERE elderly_2050 < elderly_2025
        AND (pop_2050 - elderly_2050) / (pop_2025 - elderly_2025) < elderly_2050 / elderly_2025
    ) AS elderly_down_under65_faster,
    count(*) FILTER (WHERE elderly_2025 > pop_2025 - elderly_2025) AS elderly_majority_2025,
    count(*) FILTER (WHERE elderly_2050 > pop_2050 - elderly_2050) AS elderly_majority_2050
  FROM city_zone
)
SELECT up.rn, up.up_label, up.up_elderly_increase, up.up_elderly_change_pct, up.up_pop_change_pct,
  down.down_label, down.down_elderly_change_pct, down.down_elderly_share_2050_pct, counts.*
FROM up
JOIN down USING (rn)
CROSS JOIN counts
WHERE up.rn <= 10
ORDER BY up.rn
```
