---
title: 指定緊急避難場所の17.6%は1種類の災害にしか対応していない
description: 国土地理院の指定緊急避難場所データ11万5,540か所を、8つの災害種別ごとに集計しました。地震に対応する場所は76.4%、火山現象は9.3%で、対応する災害が1種類だけの場所は17.6%です。津波に対応する場所は、海に面していない5県では0か所でした。
publishedAt: 2026-07-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 防災
  - 避難場所
  - 災害
datasets:
  - queria/gsi
  - queria/nlftp
sources:
  - title: 指定緊急避難場所・指定避難所データ
    url: https://www.gsi.go.jp/bousaichiri/hinanbasho.html
    publisher: 国土地理院
  - title: 避難場所に関すること
    url: https://www.bousai.go.jp/taisaku/hinanbasyo.html
    publisher: 内閣府
agentHint: 洪水（for_flood）に対応する指定緊急避難場所の割合を都道府県別に集計して、津波でみた沿岸と内陸の地域差と同じパターンになるか比べて。muni_nameの先頭から都道府県を取り出して
socialAnnounce: |-
  国土地理院の指定緊急避難場所11万か所を災害種別で数えました。

  地震が76%で最多、火山現象は9%。津波は沿岸に集中し、海に面しない内陸5県はゼロでした。
  Queriaは行政のオープンデータを整えて公開しています。
---

全国の指定緊急避難場所11万5,540か所のうち、地震に対応する場所は76.4%、火山現象に対応する場所は9.3%でした。対応する災害が1種類だけの場所は2万358か所（17.6%）あり、8種類すべてに対応する場所は1,795か所（1.6%）です。津波に対応する場所の割合は沖縄県で80.7%、石川県で80.0%ですが、長野県・岐阜県・埼玉県・群馬県・栃木県では0か所でした。

指定緊急避難場所は、[災害対策基本法に基づいて市町村長が災害の種類ごとに指定する場所](https://www.bousai.go.jp/taisaku/hinanbasyo.html)です（2013年の同法改正で設けられました）。避難生活を送る「指定避難所」とは別で、危険が迫ったときに命を守るために緊急に避難する場所です。津波に対応する場所、洪水に対応する場所、地震に対応する場所はそれぞれ別に指定されているので、最寄りの避難場所が、起きている災害に対応しているとは限りません。この記事では、[国土地理院が整備・公開する指定緊急避難場所データ](https://www.gsi.go.jp/bousaichiri/hinanbasho.html)を使い、全国の避難場所が災害の種類ごとにどう指定されているかを集計します。

## 地震に対応する場所は76.4%、火山現象は9.3%

使うのは国土地理院の指定緊急避難場所データ（`gsi.main.emergency_evacuation_site`）で、全国の11万5,540か所、1,698市区町村分が入っています。各施設には、対応する災害の種類が8つの真偽値の列で記録されています。

| カラム                | 災害種別               |
| --------------------- | ---------------------- |
| `for_earthquake`      | 地震                   |
| `for_flood`           | 洪水                   |
| `for_landslide`       | 崖崩れ・土石流・地滑り |
| `for_large_fire`      | 大規模な火事           |
| `for_tsunami`         | 津波                   |
| `for_inland_flooding` | 内水氾濫               |
| `for_storm_surge`     | 高潮                   |
| `for_volcano`         | 火山現象               |

災害の種類ごとに、対応する場所の数を集計しました。1か所が複数の災害に対応する場合はそれぞれの種類に数えているので、割合の合計は100%を超えます。割合の分母はどの種類でも全11万5,540か所です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "hazard_totals"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "cnt", "type": "quantitative"},
          {"field": "hazard", "type": "nominal"}
        ],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "指定数（か所）", "grid": true}
        },
        "y": {
          "field": "hazard",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "hazard_totals"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "指定数（か所）", "grid": true}
        },
        "y": {
          "field": "hazard",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "text": {"field": "pct"}
      }
    }
  ]
}
```

最も多いのは地震で、76.4%にあたる8万8,284か所が対応しています。洪水が62.1%（7万1,740か所）、崖崩れ・土石流・地滑りが58.2%（6万7,283か所）で続きます。最も少ないのは火山現象で、9.3%（1万726か所）です。地震はどの地域でも起こりうるので広く指定され、火山現象は火山の周辺に限られるので、対応する場所も少ないと考えられます。

## 対応する災害が1種類だけの場所は17.6%、8種類すべては1.6%

1か所が対応する災害の種類の数を集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "haz_count"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "n_haz", "type": "quantitative"},
          {"field": "sites", "type": "quantitative"}
        ],
        "x": {
          "field": "n_haz",
          "type": "ordinal",
          "axis": {"title": "1か所が対応する災害の種類数", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "sites",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "指定緊急避難場所の数（か所）", "grid": true}
        }
      }
    }
  ]
}
```

対応する災害が1種類だけの場所は2万358か所（17.6%）で、全体のおよそ6分の1です。最も多いのは2〜4種類に対応する場所で、8種類すべてに対応する場所は1,795か所（1.6%）です。多くの避難場所は、ある災害には指定されていても、別の災害には指定されていません。近さだけで避難先を選ぶと、その災害に対応していない場所に向かうことがあります。

## 津波に対応する場所は、沖縄県で80.7%、海に面していない5県では0か所

都道府県ごとに、指定緊急避難場所のうち津波に対応している場所の割合を地図にしました。都道府県は、市区町村名（`muni_name`）の先頭から取り出しています。北海道・東京都・京都府・大阪府は個別に判定し、それ以外は先頭から「県」までを取り出しています。この方法で都道府県名を取り出せなかった行は、地図に含まれません。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: value
    label: pref_name
    name: "津波指定率（％）"
lng: 137
lat: 37.5
zoom: 4
```

沿岸の県ほど津波に対応する場所の割合が高く、沖縄県では80.7%、石川県では80.0%の避難場所が津波に対応しています。海に面していない県では、津波への指定はほとんどありません。長野県・岐阜県・埼玉県・群馬県・栃木県の5県では、津波に対応する指定緊急避難場所は0か所です。これは海に面していないためで、避難場所の整備が遅れていることを表すものではありません。

## 火山現象に対応する場所は、青森県・長野県・福島県に多い

火山現象に対応する指定緊急避難場所が多い上位10都道府県です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "volcano_top"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "volcano_sites", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "volcano_sites",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "火山現象に対応する指定数（か所）", "grid": true}
        },
        "y": {
          "field": "pref",
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

最も多いのは青森県の1,069か所で、長野県（954か所）、福島県（921か所）、北海道（875か所）、熊本県（751か所）が続きます。いずれも活火山のある地域です。津波に対応する場所が沿岸に集まっていたのと同じように、火山現象に対応する場所も、火山のある地域に集まっています。指定は市町村長が行うので、都道府県ごとの割合や数には、自治体ごとの指定の基準の違いも含まれます。

## まとめ

- 対応する場所が最も多い災害は地震（76.4%）で、最も少ないのは火山現象（9.3%）
- 対応する災害が1種類だけの場所は17.6%で、8種類すべてに対応する場所は1.6%
- 津波に対応する場所は沿岸の県に多く、海に面していない5県では0か所。火山現象に対応する場所は、活火山のある地域に多い

避難場所は、近さに加えて、どの災害に対応しているかで選ぶ必要があります。

## データの出典

本記事は[国土地理院が公開する指定緊急避難場所データ](https://www.gsi.go.jp/bousaichiri/hinanbasho.html)を2026年7月13日時点で取得して集計しています。データは市町村からの報告に基づいて更新されるので、最新の指定状況と異なる場合があります。制度については内閣府の[避難場所に関するページ](https://www.bousai.go.jp/taisaku/hinanbasyo.html)を参照してください。

Queria は、このデータの緯度経度と災害の種類ごとのフラグを列に分け、各列の意味の説明を付けて公開しています。本記事で使った[指定緊急避難場所テーブル](/datasets/queria/gsi/main/emergency_evacuation_site)から、自分の住む市区町村で、どの災害に対応する避難場所が何か所あるかを確認できます。

```sql id=hazard_totals
SELECT hazard, cnt, ROUND(100.0*cnt/(SELECT COUNT(*) FROM gsi.main.emergency_evacuation_site),1) AS pct FROM (SELECT '地震' AS hazard, SUM(for_earthquake::INT) AS cnt FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '洪水', SUM(for_flood::INT) FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '崖崩れ・土石流・地滑り', SUM(for_landslide::INT) FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '大規模な火事', SUM(for_large_fire::INT) FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '津波', SUM(for_tsunami::INT) FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '内水氾濫', SUM(for_inland_flooding::INT) FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '高潮', SUM(for_storm_surge::INT) FROM gsi.main.emergency_evacuation_site UNION ALL SELECT '火山現象', SUM(for_volcano::INT) FROM gsi.main.emergency_evacuation_site) ORDER BY cnt
```

```sql id=haz_count
SELECT n_haz, COUNT(*) AS sites FROM (SELECT (for_flood::INT+for_landslide::INT+for_storm_surge::INT+for_earthquake::INT+for_tsunami::INT+for_large_fire::INT+for_inland_flooding::INT+for_volcano::INT) AS n_haz FROM gsi.main.emergency_evacuation_site) GROUP BY n_haz ORDER BY n_haz
```

```sql id=map_data
WITH d AS (SELECT CASE WHEN muni_name LIKE '北海道%' THEN '北海道' WHEN muni_name LIKE '東京都%' THEN '東京都' WHEN muni_name LIKE '京都府%' THEN '京都府' WHEN muni_name LIKE '大阪府%' THEN '大阪府' ELSE regexp_extract(muni_name, '^(.+?県)') END AS pref_name, ROUND(100.0*SUM(for_tsunami::INT)/COUNT(*),1) AS value FROM gsi.main.emergency_evacuation_site GROUP BY 1) SELECT d.pref_name, ST_AsGeoJSON(p.geometry) AS geojson, d.value, ROW_NUMBER() OVER (ORDER BY d.pref_name)-1 AS row_id FROM d JOIN nlftp.boundary.prefecture p ON d.pref_name = p.prefecture_name
```

```sql id=volcano_top
WITH base AS (SELECT CASE WHEN muni_name LIKE '北海道%' THEN '北海道' WHEN muni_name LIKE '東京都%' THEN '東京都' WHEN muni_name LIKE '京都府%' THEN '京都府' WHEN muni_name LIKE '大阪府%' THEN '大阪府' ELSE regexp_extract(muni_name, '^(.+?県)') END AS pref, for_volcano FROM gsi.main.emergency_evacuation_site) SELECT pref, volcano_sites FROM (SELECT pref, SUM(for_volcano::INT) AS volcano_sites FROM base GROUP BY pref ORDER BY volcano_sites DESC LIMIT 10) ORDER BY volcano_sites
```
