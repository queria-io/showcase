---
title: 商業地の地価は、駅から200m以内が2km超の約7倍
description: 2026年の地価公示で、商業地の地価の中央値は駅から200m以内が38万7,000円で、2km超の約7倍でした。住宅地は駅から200〜500mが最も高く、都道府県別の商業地の中央値は東京都が秋田県の約45倍です
publishedAt: 2026-07-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 地価
  - 不動産
  - 出店
  - 商圏分析
datasets:
  - queria/reinfolib
sources:
  - title: 地価公示
    url: https://www.mlit.go.jp/totikensangyo/totikensangyo_fr4_000043.html
    publisher: 国土交通省
  - title: 不動産情報ライブラリ
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
agentHint: 住宅地(use_category='住宅地')の地価中央値を都道府県別ランキングで2026年に出して。商業地のランキングと順位が入れ替わる県を見たい
socialAnnounce: |-
  国土交通省の地価公示データで、駅からの距離が地価をどう動かすかを用途別に読み解きました。

  商業地は駅200m以内が2km超の約7倍。出店候補地の賃料見積もりやエリア比較に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2026年の地価公示で、商業地の地価の中央値は、駅から200m以内の地点が1㎡あたり38万7,000円で、2km超の5万5,800円の約7倍でした。住宅地では、最も高いのは駅から200〜500mの地点（15万5,000円）で、200m以内の地点（7万6,700円）はそれより低くなっています。都道府県別の商業地の中央値は、東京都の141万円が秋田県の3万1,600円の約45倍です。

出店候補地の評価では、駅からの近さが来店客数と賃料の両方に影響します。国土交通省が毎年公表する[地価公示](https://www.mlit.go.jp/totikensangyo/totikensangyo_fr4_000043.html)には、全国の標準地ごとに最寄駅からの距離と1㎡あたりの価格が記録されているので、駅に近い地点がどれだけ高いか（駅近プレミアム）を数字で比較できます。この記事では、国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が提供する地価公示・地価調査の地点データを使い、用途別の地価の水準と、駅からの距離による地価の違いを集計します。

## 商業地の中央値は2026年に2010年を上回り、住宅地はまだ下回る

不動産情報ライブラリの「地価公示・地価調査ポイント」（`mart_land_prices`）を使います。1地点・1年あたり1行で、価格（`current_price`、1㎡あたりの円）、用途、最寄駅からの距離などが収録されています。調査は2種類あります。

| land_price_type | 内容                                   |
| --------------- | -------------------------------------- |
| 0               | 地価公示（国土交通省、毎年1月1日時点） |
| 1               | 地価調査（都道府県、毎年7月1日時点）   |

用途（`use_category`）は住宅地・商業地・工業地・準工業地などに分かれます。この記事では、評価時点が1月1日に統一されている地価公示（`land_price_type = 0`）だけを使い、価格が入っていない地点は除きます。代表値には中央値を使います。地価は都心の少数の地点が極端に高く、平均では多くの地点の水準から離れるためです。住宅地・商業地・工業地の中央値を2010年から2026年まで並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "trend_com"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"med\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "med", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価の中央値（円/㎡）", "grid": true}
        },
        "color": {
          "datum": "商業地",
          "type": "nominal",
          "scale": {"domain": ["商業地", "住宅地", "工業地"], "range": ["#ef4444", "#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_res"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"med\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "med", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価の中央値（円/㎡）", "grid": true}
        },
        "color": {
          "datum": "住宅地",
          "type": "nominal",
          "scale": {"domain": ["商業地", "住宅地", "工業地"], "range": ["#ef4444", "#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_ind"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"med\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "med", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "地価の中央値（円/㎡）", "grid": true}
        },
        "color": {
          "datum": "工業地",
          "type": "nominal",
          "scale": {"domain": ["商業地", "住宅地", "工業地"], "range": ["#ef4444", "#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

3用途とも2014〜2015年が最も低く、その後上がっています。商業地の中央値は2010年の13万3,000円から2015年に11万3,000円まで下がり、その後上昇して2026年は13万6,000円と2010年を上回りました。住宅地は7万7,100円から6万2,400円まで下がったあと7万4,400円まで上がりましたが、2010年の水準には届いていません。工業地は2013年以降ゆるやかに上がり続け、2026年は5万1,150円で、2010年以降で最も高くなっています。工業地の上昇の背景には物流施設の需要があると考えられ、店舗だけでなく物流拠点の立地を検討するときにも参考になります。

## 商業地は駅から200m以内が2km超の約7倍、住宅地は200〜500mが最も高い

最寄駅からの距離（`station_distance`、「1,200m」のような文字列で収録）を200m以下・200〜500m・500m〜1km・1〜2km・2km超の5つの帯に分け、2026年の地価公示で、商業地と住宅地それぞれの地価の中央値を比較しました。距離が記載されていない地点は除いています。

```chart
{
  "layer": [
    {
      "data": {"name": "decay_com"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "band", "type": "nominal"}, {"field": "med", "type": "quantitative"}],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "最寄駅からの距離", "labelAngle": 0},
          "sort": ["0-200m", "200-500m", "500m-1km", "1-2km", "2km+"]
        },
        "y": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "地価の中央値（円/㎡）", "grid": true}
        },
        "xOffset": {"datum": "商業地", "scale": {"domain": ["商業地", "住宅地"]}},
        "color": {
          "datum": "商業地",
          "type": "nominal",
          "scale": {"domain": ["商業地", "住宅地"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "decay_res"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "band", "type": "nominal"}, {"field": "med", "type": "quantitative"}],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "最寄駅からの距離", "labelAngle": 0},
          "sort": ["0-200m", "200-500m", "500m-1km", "1-2km", "2km+"]
        },
        "y": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "地価の中央値（円/㎡）", "grid": true}
        },
        "xOffset": {"datum": "住宅地", "scale": {"domain": ["商業地", "住宅地"]}},
        "color": {
          "datum": "住宅地",
          "type": "nominal",
          "scale": {"domain": ["商業地", "住宅地"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    }
  ]
}
```

商業地は、駅から遠いほど地価が下がります。駅から200m以内の中央値は38万7,000円で、2km超の5万5,800円の約7倍です。駅前に人が集まることが、地価に反映されていると考えられます。

住宅地は、駅から近いほど高いとは限りません。最も高いのは200〜500mの帯（15万5,000円）で、200m以内の帯（7万6,700円）はそれより低くなっています。駅前の土地は商業地として使われることが多く、住宅地として選ばれている標準地は少なく、条件も限られるためと考えられます。この結果は、駅から徒歩数分の住宅地が最も高く評価されるという不動産実務での見方とも一致します。出店する業態が商業利用か住居系かによって、駅からの距離による地価の違いを分けて見る必要があります。

## 商業地の中央値は、東京都の141万円が秋田県の3万1,600円の約45倍

2026年の地価公示の商業地について、都道府県ごとの中央値を47都道府県で比較しました（上位10・中間・下位10で色分け）。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "med", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "商業地の地価中央値（円/㎡）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "med", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "商業地の地価中央値（円/㎡）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "med", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "med",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "商業地の地価中央値（円/㎡）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高い東京都は中央値141万円で、最も低い秋田県（3万1,600円）の約45倍です。京都府（47万5,000円）、神奈川県（44万5,000円）、大阪府（35万円）が続き、上位は三大都市圏と政令市のある府県です。下位には秋田県・山形県・鹿児島県など地方圏の県が入っています。

中央値を使うと、東京都心の一部の極端に高い地点の影響を受けずに、その県の標準的な商業地の地価水準を比較できます。出店時の賃料を想定するときや、複数のエリアを比較するときに使えます。都道府県別の中央値は、その県のどこに標準地が置かれているかによって変わります。

## 出店評価での使い方

地価公示の地点データは、出店候補地の評価に次のように使えます。

- 賃料水準の見積もり: 商業地の中央値と駅からの距離帯ごとの地価から、候補エリアのコストを早い段階で把握する
- エリアの絞り込み: 都道府県・用途・駅からの距離で絞り込み、予算に合う地域を抽出する
- 駅近プレミアムの把握: 同じ地域の中でも駅からの距離による地価の差を確認し、出店区画の優先順位に反映する

## データの出典

本記事は国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が提供する地価公示・地価調査ポイントを、2026年7月11日時点で取得して集計しています。[地価公示](https://www.mlit.go.jp/totikensangyo/totikensangyo_fr4_000043.html)は毎年1月1日時点の、全国の標準地の評価額です。

Queriaは、国土交通省の地価公示・地価調査を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[地価公示・地価調査ポイントのテーブル](/datasets/queria/reinfolib/main/mart_land_prices)から、対象エリアの用途別の地価水準や、駅からの距離による地価の違いを確認できます。

```sql id=trend_com
SELECT year, CAST(MEDIAN(current_price) AS BIGINT) AS med FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND use_category = '商業地' AND year BETWEEN 2010 AND 2026 AND current_price IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=trend_res
SELECT year, CAST(MEDIAN(current_price) AS BIGINT) AS med FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND use_category = '住宅地' AND year BETWEEN 2010 AND 2026 AND current_price IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=trend_ind
SELECT year, CAST(MEDIAN(current_price) AS BIGINT) AS med FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND use_category = '工業地' AND year BETWEEN 2010 AND 2026 AND current_price IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=decay_com
WITH base AS (SELECT current_price, TRY_CAST(REPLACE(REPLACE(station_distance, ',', ''), 'm', '') AS INTEGER) AS dist_m FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND year = 2026 AND use_category = '商業地' AND current_price IS NOT NULL) SELECT CASE WHEN dist_m <= 200 THEN '0-200m' WHEN dist_m <= 500 THEN '200-500m' WHEN dist_m <= 1000 THEN '500m-1km' WHEN dist_m <= 2000 THEN '1-2km' ELSE '2km+' END AS band, CAST(MEDIAN(current_price) AS BIGINT) AS med FROM base WHERE dist_m IS NOT NULL GROUP BY band ORDER BY MIN(dist_m)
```

```sql id=decay_res
WITH base AS (SELECT current_price, TRY_CAST(REPLACE(REPLACE(station_distance, ',', ''), 'm', '') AS INTEGER) AS dist_m FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND year = 2026 AND use_category = '住宅地' AND current_price IS NOT NULL) SELECT CASE WHEN dist_m <= 200 THEN '0-200m' WHEN dist_m <= 500 THEN '200-500m' WHEN dist_m <= 1000 THEN '500m-1km' WHEN dist_m <= 2000 THEN '1-2km' ELSE '2km+' END AS band, CAST(MEDIAN(current_price) AS BIGINT) AS med FROM base WHERE dist_m IS NOT NULL GROUP BY band ORDER BY MIN(dist_m)
```

```sql id=rank_top
WITH ranked AS (SELECT prefecture_name AS area_name, CAST(MEDIAN(current_price) AS BIGINT) AS med, ROW_NUMBER() OVER (ORDER BY MEDIAN(current_price) DESC, prefecture_name) AS rn FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND year = 2026 AND use_category = '商業地' AND current_price IS NOT NULL GROUP BY prefecture_name) SELECT area_name, med FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT prefecture_name AS area_name, CAST(MEDIAN(current_price) AS BIGINT) AS med, ROW_NUMBER() OVER (ORDER BY MEDIAN(current_price) DESC, prefecture_name) AS rn FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND year = 2026 AND use_category = '商業地' AND current_price IS NOT NULL GROUP BY prefecture_name) SELECT area_name, med FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH ranked AS (SELECT prefecture_name AS area_name, CAST(MEDIAN(current_price) AS BIGINT) AS med, ROW_NUMBER() OVER (ORDER BY MEDIAN(current_price) DESC, prefecture_name) AS rn FROM reinfolib.main.mart_land_prices WHERE land_price_type = 0 AND year = 2026 AND use_category = '商業地' AND current_price IS NOT NULL GROUP BY prefecture_name) SELECT area_name, med FROM ranked WHERE rn > 37 ORDER BY rn
```
