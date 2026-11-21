---
title: 足立区の人口は2050年まで+0.6%でも、1kmメッシュでは+11.6%から-23.1%まで分かれる
description: 1kmメッシュ別の将来推計人口で、東京都足立区の2025年から2050年の人口の増減と高齢化率を集計しました。区全体では+0.6%の横ばいですが、メッシュ別の増減率は+11.6%から-23.1%まで分かれ、2050年の高齢化率は29.0%から38.9%です。
publishedAt: 2026-07-08
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 将来推計人口
  - 商圏分析
  - 出店戦略
  - 高齢化
  - メッシュ
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 1kmメッシュ別将来推計人口データ（R6国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html
    publisher: 国土交通省
  - title: 日本の地域別将来推計人口（令和5年推計）
    url: https://www.ipss.go.jp/
    publisher: 国立社会保障・人口問題研究所
agentHint: 足立区（city_code='13121'）のメッシュごとに、2025→2035年と2035→2050年で人口がどう動くかを population_2025・population_2035・population_2050 から出して、減少が後半に加速するのか前半から始まるのか比べて。population_2025が50人以上のメッシュで
socialAnnounce: |-
  商圏の将来需要は市区町村平均では横ばいでも、1kmメッシュで見ると伸びる区画と縮む区画に割れます。足立区は全体+0.6%でも区内は+11.6%〜-23.1%。

  出店戦略やシニア需要の見極めに。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

東京都足立区の人口は、2025年の約53.2万人から2050年に約53.6万人へと、25年間で+0.6%のほぼ横ばいと推計されています。区内を1kmメッシュに分けると、47メッシュのうち23メッシュで人口が増え、24メッシュで減ります。増減率は最も増えるメッシュで+11.6%、最も減るメッシュで-23.1%です。2050年の高齢化率も、メッシュによって29.0%から38.9%まで差があります。

出店やサービス拠点の配置では、10年後・20年後もその商圏に需要が残るかを見積もる必要があります。市区町村単位の将来推計人口では、同じ区の中で再開発が進む区画と人口が減る区画の違いが分かりません。この記事では、[国土数値情報](https://nlftp.mlit.go.jp/ksj/)の1kmメッシュ別将来推計人口を使い、足立区の区内の違いを集計します。

## 使ったデータ

国土数値情報の[1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)は、総務省「令和2年国勢調査」と[国立社会保障・人口問題研究所](https://www.ipss.go.jp/)「日本の地域別将来推計人口（令和5年推計）」に基づき、全国を約1km四方のメッシュに区切って将来の人口を推計したデータです。推計の対象は居住者の人口で、昼間に通勤や買い物で訪れる人は含みません。

| カラム                                                    | 内容                                |
| --------------------------------------------------------- | ----------------------------------- |
| `population_2025` / `population_2035` / `population_2050` | 各年の推計人口（メッシュ内）        |
| `elderly_ratio_2025` / `elderly_ratio_2050`               | 65歳以上人口の割合（%）             |
| `growth_rate_2025_2050`                                   | 2025年から2050年への人口増減率（%） |
| `geometry`                                                | 1kmメッシュの境界ポリゴン           |
| `city_code`                                               | メッシュが属する市区町村コード      |

足立区（`city_code` = 13121）のメッシュのうち、2025年の推計人口が50人以上の47メッシュを集計しました。人口が数人のメッシュでは、数人の増減で増減率が数十パーセント動くので除いています。メッシュは行政界と関係のない格子なので、区の境界にかかるメッシュには隣の自治体の人口も含まれます。

メッシュには地名が付いていないので、各メッシュの中心に最も近い町丁字（[国勢調査の小地域](https://www.stat.go.jp/data/kokusei/2020/index.html)境界）の名前を代表地名として付けています。グラフにカーソルを合わせると「◯◯周辺」とおおよその場所が表示されます。1kmメッシュは複数の町丁字にまたがるので、この地名は位置の目安です。

## 区全体は横ばいでも、47メッシュのうち23で増え、24で減る

47メッシュの2025年から2050年への人口増減率を、増える順に並べました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "growth_pos"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rn", "type": "quantitative"},
          {"field": "g", "type": "quantitative"}
        ],
        "x": {
          "field": "rn",
          "type": "ordinal",
          "axis": {
            "title": "メッシュ（2025→2050 増減率の高い順）",
            "labelAngle": 0,
            "labels": false,
            "labelOverlap": "greedy"
          },
          "sort": null
        },
        "y": {
          "field": "g",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口増減率（%）", "grid": true}
        },
        "color": {
          "datum": "人口が増える区画",
          "type": "nominal",
          "scale": {"domain": ["人口が増える区画", "人口が減る区画"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "growth_neg"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rn", "type": "quantitative"},
          {"field": "g", "type": "quantitative"}
        ],
        "x": {
          "field": "rn",
          "type": "ordinal",
          "axis": {
            "title": "メッシュ（2025→2050 増減率の高い順）",
            "labelAngle": 0,
            "labels": false,
            "labelOverlap": "greedy"
          },
          "sort": null
        },
        "y": {
          "field": "g",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口増減率（%）", "grid": true}
        },
        "color": {
          "datum": "人口が減る区画",
          "type": "nominal",
          "scale": {"domain": ["人口が増える区画", "人口が減る区画"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 0.5, "type": "ordinal"},
        "x2": {"datum": 47.5, "type": "ordinal"},
        "y": {"datum": 0.6, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 47.5, "type": "ordinal"},
        "y": {"datum": 0.6, "type": "quantitative"},
        "text": {"value": "足立区全体 +0.6%"}
      }
    }
  ]
}
```

増減率は最も増えるメッシュで+11.6%、最も減るメッシュで-23.1%で、中央値は-0.1%です。区全体の+0.6%という横ばいは、人口が増えるメッシュと減るメッシュの増減が相殺された結果です。区全体の数字だけで出店の可否を判断すると、区内で人口が増える商圏と減る商圏の違いを見落とします。

## 2050年の高齢化率は、メッシュによって29.0%から38.9%まで差がある

2050年の高齢化率（65歳以上人口の割合）をメッシュごとに地図にしました。色が濃いほど高齢化率が高いメッシュです。

```map
type: map
layers:
  - from: elderly_map
    geojson: geojson
    color: value
    label: name
    name: "高齢化率（%）"
lng: 139.79
lat: 35.787
zoom: 11.8
```

足立区ではすべてのメッシュで2050年の高齢化率が29%以上になり、区全体（メッシュの単純平均ではなく人口で加重した平均）では31.9%です。区内でも高齢化率の高いメッシュと低いメッシュが隣り合っていて、シニア向けの需要がどこに多いかは区の平均では分かりません。高齢化率の高いメッシュでは、医療・介護・調剤やシニア向けの小売・宅配の需要が相対的に大きくなると考えられます。

## 人口の増減と高齢化率で、メッシュを4つのタイプに分けられる

横軸に人口の増減率、縦軸に2050年の高齢化率を取りました。円の大きさは2025年の人口です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "segment"},
      "mark": {"type": "point", "color": "#7c3aed", "opacity": 0.55, "filled": true, "size": 36},
      "encoding": {
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "g", "type": "quantitative"},
          {"field": "e50", "type": "quantitative"}
        ],
        "x": {
          "field": "g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2025→2050 人口増減率（%）", "grid": true}
        },
        "y": {
          "field": "e50",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2050年 高齢化率（%）", "grid": true}
        },
        "size": {
          "field": "sz",
          "type": "quantitative",
          "legend": null,
          "scale": {"range": [16, 900]}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"datum": 28, "type": "quantitative"},
        "y2": {"datum": 40, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": -25, "type": "quantitative"},
        "x2": {"datum": 15, "type": "quantitative"},
        "y": {"datum": 31.9, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 10,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"datum": 39.5, "type": "quantitative"},
        "text": {"value": "増減の境"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 10,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 14, "type": "quantitative"},
        "y": {"datum": 31.9, "type": "quantitative"},
        "text": {"value": "区平均 高齢化率 31.9%"}
      }
    }
  ]
}
```

散布図の4つの領域は、次のような商圏に対応すると考えられます。

- 右下（人口が増え、高齢化率が相対的に低い）: 子育て世帯が流入して人口が増えるファミリー向けの商圏
- 右上（人口が増え、高齢化率も高い）: 人口を保ちながら高齢者の割合が上がる商圏で、シニア向けサービスの需要が増える
- 左上（人口が減り、高齢化率が高い）: 人口が減りながら高齢化する商圏で、撤退や、残る高齢者向けの業態への転換を検討する対象になる

人口の多いメッシュ（大きな円）でも、増減率は+6.7%から-3.1%まで分かれています。今の人口が多いことは、将来も需要が残ることを意味しません。

推計には、再開発や大規模住宅の供給などの個別の計画は織り込まれていないので、計画が進む区画では実際の人口が推計と異なる可能性があります。

## 業務での使い方

- 商圏の将来需要の確認: 市区町村で候補エリアを絞ったあと、メッシュ単位の将来人口で、その商圏の需要が今後も残るかを確認する
- シニア需要が増える区画の特定: 2050年の高齢化率と人口を組み合わせ、医療・介護・調剤やシニア向け小売の需要が多くなる立地を事前に把握する
- 出店計画の調整: 人口が増える区画と減る区画を同じ地図で比較し、成長する商圏への出店と、縮小する商圏からの撤退・業態転換を一緒に計画する

## データの出典

本記事は国土数値情報の[1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を2026-07-11時点で取得して集計しています。推計のもとになっているのは令和2年国勢調査と、[国立社会保障・人口問題研究所](https://www.ipss.go.jp/)の「日本の地域別将来推計人口（令和5年推計）」です。

Queriaは、国土数値情報の将来推計人口などの地理データを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[1kmメッシュ別将来推計人口のテーブル](/datasets/queria/nlftp/population/future_population_mesh)で `city_code` を検討中の市区町村に変えると、同じ集計ができます。

```sql id=growth_pos
WITH r AS (SELECT mesh_id, growth_rate_2025_2050 AS g, ROW_NUMBER() OVER (ORDER BY growth_rate_2025_2050 DESC, mesh_id) AS rn FROM nlftp.population.future_population_mesh WHERE city_code = '13121' AND population_2025 >= 50) SELECT rn, ROUND(g, 1) AS g FROM r WHERE g > 0 ORDER BY rn
```

```sql id=growth_neg
WITH r AS (SELECT mesh_id, growth_rate_2025_2050 AS g, ROW_NUMBER() OVER (ORDER BY growth_rate_2025_2050 DESC, mesh_id) AS rn FROM nlftp.population.future_population_mesh WHERE city_code = '13121' AND population_2025 >= 50) SELECT rn, ROUND(g, 1) AS g FROM r WHERE g <= 0 ORDER BY rn
```

```sql id=elderly_map
WITH sa AS (SELECT area_name, ST_Centroid(geometry) AS sc FROM e_stat.boundary.small_area WHERE city_name = '足立区'), m AS (SELECT mesh_id, geometry AS geom, elderly_ratio_2050 AS e50, population_2025 AS pop, ST_Centroid(geometry) AS c FROM nlftp.population.future_population_mesh WHERE city_code = '13121' AND population_2025 >= 50), named AS (SELECT m.mesh_id, m.geom, m.e50, m.pop, sa.area_name, ROW_NUMBER() OVER (PARTITION BY m.mesh_id ORDER BY ST_Distance_Sphere(ST_FlipCoordinates(sa.sc), ST_FlipCoordinates(m.c))) AS rn FROM m JOIN sa ON true) SELECT ROUND(e50, 1) AS value, ROUND(pop) AS pop, area_name AS name, ROW_NUMBER() OVER (ORDER BY mesh_id) - 1 AS row_id, ST_AsGeoJSON(geom) AS geojson FROM named WHERE rn = 1
```

```sql id=segment
WITH sa AS (SELECT area_name, ST_Centroid(geometry) AS sc FROM e_stat.boundary.small_area WHERE city_name = '足立区'), m AS (SELECT mesh_id, growth_rate_2025_2050 AS g, elderly_ratio_2050 AS e50, population_2025 AS pop, ST_Centroid(geometry) AS c FROM nlftp.population.future_population_mesh WHERE city_code = '13121' AND population_2025 >= 50), named AS (SELECT m.mesh_id, m.g, m.e50, m.pop, sa.area_name, ROW_NUMBER() OVER (PARTITION BY m.mesh_id ORDER BY ST_Distance_Sphere(ST_FlipCoordinates(sa.sc), ST_FlipCoordinates(m.c))) AS rn FROM m JOIN sa ON true) SELECT ROUND(g, 1) AS g, ROUND(e50, 1) AS e50, ROUND(pop) AS pop, ROUND(SQRT(pop) / 4.0, 1) AS sz, area_name AS name FROM named WHERE rn = 1
```
