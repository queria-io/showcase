---
title: 津波を伝える石碑の7割は今の浸水想定区域の中。山の崩落が起こした津波を伝える熊本県の31基は、すべて区域の外だった
description: 国土地理院の自然災害伝承碑2,481基を、津波・洪水・土砂災害の想定区域と重ねて集計しました。津波を伝える碑の70.7%は今の津波浸水想定区域の中にあります。1792年の眉山崩壊を伝える熊本県の31基と1741年の寛保津波を伝える4基は、すべて区域の外にあります。
publishedAt: 2026-10-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 防災
  - 自然災害伝承碑
  - ハザードマップ
datasets:
  - queria/gsi
  - queria/nlftp
sources:
  - title: 自然災害伝承碑
    url: https://www.gsi.go.jp/bousaichiri/denshouhi.html
    publisher: 国土地理院
  - title: 国土数値情報 津波浸水想定データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A40-2024.html
    publisher: 国土交通省
  - title: 国土数値情報 洪水浸水想定区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A31a-2025.html
    publisher: 国土交通省
  - title: 国土数値情報 土砂災害警戒区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A33-2025.html
    publisher: 国土交通省
agentHint: 自分の市区町村(municipality_code)にある津波の碑(is_tsunami)を一覧にして、それぞれが津波浸水想定区域(tsunami_inundation)の中か外かと、伝える災害(disaster_name)を並べて
socialAnnounce: |-
  自然災害伝承碑2,481基をハザード区域と重ねました。

  津波の碑の7割は浸水想定区域の中。山の崩落による津波を伝える熊本県の31基は、すべて区域外です。防災教育に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

過去の津波を伝える石碑のうち、70.7%は今の津波浸水想定区域の中に建っています。洪水を伝える碑の47.9%は洪水浸水想定区域の中、土砂災害を伝える碑の38.6%は土砂災害警戒区域の中にあります。1792年の眉山崩壊で起きた津波を伝える熊本県の31基と、1741年の寛保津波を伝える4基は、すべて今の津波浸水想定区域の外にあります。

国土地理院は、市区町村の申請を受けて、過去の災害を記録した石碑を[自然災害伝承碑](https://www.gsi.go.jp/bousaichiri/denshouhi.html)として地理院地図に掲載しています。ハザードマップは、想定しうる最大規模の災害をもとに、これから起こりうる浸水や土砂災害の範囲を示したものです。この記事では、全国の伝承碑の位置を今の想定区域と重ね、過去の災害の記録と今の想定がどこまで一致するかを集計しました。市区町村で防災教育や地区防災計画を担当する方に向けた内容です。

## 全国の伝承碑は2,481基で、最も多いのは洪水を伝える碑

使ったのは国土地理院の自然災害伝承碑のデータ（`gsi.main.disaster_lore_monument`）です。1行が碑1基で、位置（緯度経度）、碑が伝える災害の名称と種別、伝承の説明文が記録されています。災害の種別は7つの真偽値の列で記録され、地震と津波を伝える碑のように、1基の碑が複数の種別を持つことがあります。

```sql id=type_counts display
-- 災害種別ごとの碑の数。1基が複数の種別を持つので、合計は全体の基数を超える
SELECT label AS 災害種別, col AS カラム, n AS 碑の数
FROM (
  SELECT 1 AS ord, '洪水' AS label, 'is_flood' AS col, COUNT(*) FILTER (WHERE is_flood) AS n FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 2, '地震', 'is_earthquake', COUNT(*) FILTER (WHERE is_earthquake) FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 3, '土砂災害', 'is_landslide', COUNT(*) FILTER (WHERE is_landslide) FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 4, '津波', 'is_tsunami', COUNT(*) FILTER (WHERE is_tsunami) FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 5, '高潮', 'is_storm_surge', COUNT(*) FILTER (WHERE is_storm_surge) FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 6, 'その他', 'is_other', COUNT(*) FILTER (WHERE is_other) FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 7, '火山災害', 'is_volcano', COUNT(*) FILTER (WHERE is_volcano) FROM gsi.main.disaster_lore_monument
  UNION ALL SELECT 8, '全体（重複なし）', '', COUNT(*) FROM gsi.main.disaster_lore_monument
)
ORDER BY ord
```

全国で2,481基が収録されています。最も多いのは洪水を伝える碑の1,112基で、地震が888基、土砂災害が629基、津波が596基です。このうち今の想定区域と比較できるのは、津波・洪水・土砂災害の3種別です。

## 津波の碑の70.7%、洪水の碑の47.9%、土砂災害の碑の38.6%が、同じ種類の想定区域の中にある

比較に使ったのは、国土数値情報の3つの区域データです。

| 区域             | テーブル                             | 中身                                             |
| ---------------- | ------------------------------------ | ------------------------------------------------ |
| 津波浸水想定区域 | `nlftp.hazard.tsunami_inundation`    | 最大クラスの津波が悪条件下で起きた場合の浸水域   |
| 洪水浸水想定区域 | `nlftp.hazard.flood_inundation`      | 河川ごとの想定最大規模の降雨による浸水域         |
| 土砂災害警戒区域 | `nlftp.hazard.landslide_hazard_area` | 都道府県が指定した土砂災害警戒区域・特別警戒区域 |

碑の位置がそれぞれの区域のポリゴンの中にあるかを判定し、碑の種別ごとに区域の中にある碑の割合を算出しました。津波と土砂災害の区域データは、オープンデータとして再配布できる都道府県の分だけが収録されています（津波は28道府県、土砂災害は41都道府県）。この2つは、区域データのある都道府県の碑だけを分母にしています。洪水は47都道府県すべてのデータがあります。

```chart caption="碑の種別ごとの、今の想定区域の中にある碑の割合（%）"
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "match_matrix"},
      "mark": {"type": "rect"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "zone_type", "type": "nominal"},
          {"field": "monument_type", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "zone_type",
          "type": "nominal",
          "axis": {"title": null, "labelAngle": 0, "orient": "top"},
          "sort": null
        },
        "y": {
          "field": "monument_type",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"range": ["#eff6ff", "#3b82f6"]},
          "legend": null
        }
      }
    },
    {
      "data": {"name": "match_matrix"},
      "transform": [{"calculate": "\"\" + format(datum[\"pct\"], \"\") + \"\"", "as": "__label"}],
      "mark": {"type": "text", "fontSize": 12},
      "encoding": {
        "x": {
          "field": "zone_type",
          "type": "nominal",
          "axis": {"title": null, "labelAngle": 0, "orient": "top"},
          "sort": null
        },
        "y": {
          "field": "monument_type",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "text": {"field": "__label"}
      }
    }
  ]
}
```

津波を伝える碑は、433基のうち306基（70.7%）が今の津波浸水想定区域の中に建っています。種別を問わずすべての碑で見ると、津波浸水想定区域の中にあるのは27.2%なので、津波の碑はその2.6倍の割合で区域の中にあります。

洪水の碑は、1,112基のうち533基（47.9%）が洪水浸水想定区域の中にあります。すべての碑では33.5%です。洪水浸水想定区域は浸水想定を作成した河川についての区域なので、それ以外の中小河川の近くにある碑は区域の外になります。土砂災害の碑は、477基のうち184基（38.6%）が土砂災害警戒区域の中にあり、すべての碑の22.7%より高い割合です。3種別とも、碑が伝える災害と同じ種類の区域で、区域の中にある割合が最も高くなっています。

土砂災害警戒区域の中にある割合を比較すると、土砂災害の碑が38.6%、津波の碑が33.1%で、差は小さくなっています。土砂災害警戒区域は斜面とその直下の細長い範囲に指定されるので、碑が集落の寺社や公園に建っていると、斜面のすぐ近くでも区域の外になります。

## 区域の外にある津波の碑のうち35基は、噴火や山の崩落で起きた津波を伝えている

碑が4基以上ある災害ごとに、津波浸水想定区域の中にある碑の割合を並べました。災害名は碑ごとに表記が異なるので、`disaster_name` から日付の括弧書きを除いた名前と発生年でまとめています。

```chart caption="伝える災害ごとの、津波浸水想定区域の中にある津波の碑の割合（碑が4基以上の災害）"
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "tsunami_by_disaster"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "bar_text", "type": "nominal"},
          {"field": "pct", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"domain": [0, 105], "zero": false, "nice": false},
          "axis": {"title": "区域の中にある碑の割合（%）", "grid": true}
        },
        "y": {
          "field": "label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"name": "tsunami_by_disaster"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"domain": [0, 105], "zero": false, "nice": false},
          "axis": {"title": "区域の中にある碑の割合（%）", "grid": true}
        },
        "y": {
          "field": "label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "text": {"field": "bar_text"}
      }
    }
  ]
}
```

昭和南海地震（1946年）の碑は70基のうち69基が区域の中にあります。安政南海地震（1854年）や宝永地震（1707年）のように170年以上前の地震による津波の碑も、多くが今の区域の中にあります。東日本大震災（2011年）の碑は69基のうち50基（72.5%）です。

碑が4基以上ある災害のうち、区域の中にある碑が1基もない災害が2つあります。1792年の眉山崩壊を伝える熊本県の31基と、1741年の寛保津波を伝える4基です。下の表は、この2つの災害を伝える碑がある道県と、伝承文の書き出しです。

```sql id=collapse_monuments display
-- 区域の中に1基も無い2つの災害の碑。所在地の道県と、伝承文の書き出し（碑ごとに文面が違うので ID の若い碑のものを載せる）
SELECT
  trim(regexp_replace(disaster_name, '\(.*?\)+', '', 'g')) AS 災害,
  regexp_extract(address, '^(.+?[都道府県])', 1) AS 所在地,
  COUNT(*) AS 碑の数,
  left(arg_min(lore, monument_id), 90) || '…' AS 伝承文の書き出し
FROM gsi.main.disaster_lore_monument
WHERE is_tsunami
  AND (disaster_name LIKE '%眉山崩壊%' OR disaster_name LIKE '%寛保津波%')
  AND LEFT(municipality_code, 2) IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation)
GROUP BY 1, 2
ORDER BY 碑の数 DESC
```

伝承文によると、眉山崩壊の津波は、雲仙岳の噴火活動中の地震で眉山が崩れ、土砂が有明海に流れ込んで起きました。寛保津波は、渡島大島の噴火のあとに北海道の沿岸に到達した津波です。どちらも、噴火や山の崩落によって起きた津波です。

津波浸水想定区域は、最大クラスの津波が悪条件下で起きた場合の浸水域として、都道府県が設定した区域です。この2つの災害の碑は、区域のデータがある熊本県と北海道に建っていますが、すべて区域の外にあります。今の想定は、噴火や山の崩落で起きる津波を前提にしていないと考えられます。

```map
type: map
caption: "津波を伝える碑の位置と、今の津波浸水想定区域の内外（区域データのある28道府県）"
layers:
  - from: tsunami_map_out
    lng: longitude
    lat: latitude
    label: hover
    name: "区域の外"
  - from: tsunami_map_in
    lng: longitude
    lat: latitude
    label: hover
    name: "区域の中"
lng: 137.5
lat: 37.5
zoom: 4
```

区域の外にある津波の碑127基のうち、眉山崩壊と寛保津波の碑は35基です。残りの多くは地震による津波の碑で、東日本大震災が19基、昭和三陸地震が17基、明治三陸地震が16基、安政南海地震が8基です。碑は浸水した場所ではなく、寺社の境内や高台に建てられることがあります。地図では、三陸や紀伊半島・四国の太平洋岸にある碑の大半が区域の中（青）にあります。

眉山崩壊と寛保津波の碑35基を除くと、津波の碑398基のうち区域の中にあるのは306基で、76.9%です。

## 江戸時代以前の洪水を伝える碑の52.8%は、今の洪水浸水想定区域の中にある

碑が伝える災害の発生年（`disaster_name` に含まれる西暦）で4つの時代に分け、同じ種類の区域の中にある碑の割合を比較しました。

```chart caption="災害の発生した時代別の、同じ種類の想定区域の中にある碑の割合"
{
  "layer": [
    {
      "data": {"name": "era_match"},
      "transform": [
        {"fold": ["ts_pct", "fl_pct", "ls_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"ts_pct\": \"津波の碑 × 津波浸水想定区域\", \"fl_pct\": \"洪水の碑 × 洪水浸水想定区域\", \"ls_pct\": \"土砂災害の碑 × 土砂災害警戒区域\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"ts_pct\",\"fl_pct\",\"ls_pct\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "era",
          "type": "nominal",
          "axis": {"title": "災害の発生した時代", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "区域の中にある碑の割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["津波の碑 × 津波浸水想定区域", "洪水の碑 × 洪水浸水想定区域", "土砂災害の碑 × 土砂災害警戒区域"],
            "range": ["#3b82f6", "#22c55e", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {
          "field": "__name",
          "sort": ["津波の碑 × 津波浸水想定区域", "洪水の碑 × 洪水浸水想定区域", "土砂災害の碑 × 土砂災害警戒区域"]
        },
        "tooltip": [
          {"field": "era", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

洪水の碑では、江戸時代以前の災害を伝える106基のうち52.8%が今の洪水浸水想定区域の中にあります。戦後から1999年までの災害の碑の43.3%より高い割合です。1868年より前の洪水を伝える碑でも、半数は今も浸水が想定される場所に建っています。

津波の碑の江戸時代以前は50.0%ですが、この118基には区域の外にある眉山崩壊と寛保津波の碑35基がすべて含まれています。35基を除くと71.1%で、明治から戦前の69.9%とほぼ同じです。土砂災害の碑は、江戸時代以前が22.8%と低いものの57基と数が少なく、明治以降はどの時代も4割前後です。

## 防災の業務での使い方

- 防災教育の教材: 区域の中にある碑は、過去に浸水した記録と、今も浸水が想定される場所が一致する地点です。ハザードマップの色だけでは伝わりにくい危険を、地元で起きた具体的な災害として住民に示せます
- ハザードマップの補足: 眉山崩壊の碑のように、噴火や山の崩落で起きた津波の記録が、今の区域の外にあることがあります。管内に区域の外の碑があれば、その碑が伝える災害を確認し、地区防災計画で扱う災害の範囲を見直す材料にできます
- 江戸時代の碑の活用: 江戸時代以前の洪水を伝える碑の52.8%は今の洪水浸水想定区域の中にあり、明治以降のどの時代の碑と比較しても同じかそれ以上の割合です。古い災害の記録も、今のハザードマップを説明する材料に使えます
- 区域の外の扱い: 土砂災害警戒区域は斜面の細い範囲に指定されるので、土砂災害の碑の6割は区域の外にあります。区域の外を安全な場所と説明せず、碑がある集落の周りに区域がどう指定されているかを地図で確認する必要があります

## データの出典

本記事は国土地理院の[自然災害伝承碑](https://www.gsi.go.jp/bousaichiri/denshouhi.html)のデータと、国土交通省の国土数値情報の[津波浸水想定データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A40-2024.html)・[洪水浸水想定区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A31a-2025.html)（2025年度）・[土砂災害警戒区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A33-2025.html)（2025年度）を、2026-10-11 時点で重ね合わせて集計しています。

Queriaは、伝承碑や国土数値情報のような行政のオープンデータを、列名と文字コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[自然災害伝承碑テーブル](/datasets/gsi/main/disaster_lore_monument)や[津波浸水想定区域テーブル](/datasets/nlftp/hazard/tsunami_inundation)から、管内の碑の伝承文や区域の範囲を確認できます。

```sql id=match_matrix
-- 碑の種別 × 想定区域の種別ごとに、区域の中にある碑の割合を出す
-- 津波・土砂災害は区域データが収録されている都道府県の碑だけを分母にする（都道府県は申請した市区町村コードの先頭2桁）
WITH m AS (
  SELECT monument_id, LEFT(municipality_code, 2) AS pref, is_tsunami, is_flood, is_landslide, geometry
  FROM gsi.main.disaster_lore_monument
),
ts_pref AS (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation),
ls_pref AS (SELECT DISTINCT prefecture_code FROM nlftp.hazard.landslide_hazard_area),
ts AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.tsunami_inundation z ON ST_Intersects(z.geometry, m.geometry)),
fl AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.flood_inundation z ON ST_Intersects(z.geometry, m.geometry)),
ls AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.landslide_hazard_area z ON ST_Intersects(z.geometry, m.geometry)),
flags AS (
  SELECT
    m.monument_id, m.is_tsunami, m.is_flood, m.is_landslide,
    m.pref IN (SELECT prefecture_code FROM ts_pref) AS ts_cov,
    m.pref IN (SELECT prefecture_code FROM ls_pref) AS ls_cov,
    ts.monument_id IS NOT NULL AS in_ts,
    fl.monument_id IS NOT NULL AS in_fl,
    ls.monument_id IS NOT NULL AS in_ls
  FROM m
  LEFT JOIN ts USING (monument_id)
  LEFT JOIN fl USING (monument_id)
  LEFT JOIN ls USING (monument_id)
),
grp AS (
  SELECT 1 AS ord, 'すべての碑' AS monument_type, * FROM flags
  UNION ALL SELECT 2, '土砂災害の碑', * FROM flags WHERE is_landslide
  UNION ALL SELECT 3, '洪水の碑', * FROM flags WHERE is_flood
  UNION ALL SELECT 4, '津波の碑', * FROM flags WHERE is_tsunami
),
cells AS (
  SELECT ord, monument_type, 1 AS zone_ord, '津波浸水想定区域' AS zone_type,
    COUNT(*) FILTER (WHERE ts_cov) AS n, COUNT(*) FILTER (WHERE ts_cov AND in_ts) AS n_in
  FROM grp GROUP BY ord, monument_type
  UNION ALL
  SELECT ord, monument_type, 2, '洪水浸水想定区域', COUNT(*), COUNT(*) FILTER (WHERE in_fl)
  FROM grp GROUP BY ord, monument_type
  UNION ALL
  SELECT ord, monument_type, 3, '土砂災害警戒区域',
    COUNT(*) FILTER (WHERE ls_cov), COUNT(*) FILTER (WHERE ls_cov AND in_ls)
  FROM grp GROUP BY ord, monument_type
)
SELECT
  monument_type, zone_type, n, n_in,
  ROUND(100 * n_in::DOUBLE / n, 1) AS pct,
  CAST(ROUND(100 * n_in::DOUBLE / n, 1) AS VARCHAR) || '%' AS label
FROM cells
ORDER BY ord, zone_ord
```

```sql id=coverage
-- 区域データが収録されている都道府県の数（プロットはしない）
SELECT
  (SELECT COUNT(DISTINCT prefecture_code) FROM nlftp.hazard.tsunami_inundation) AS tsunami_prefs,
  (SELECT COUNT(DISTINCT region_code) FILTER (WHERE region_code < '50') FROM nlftp.hazard.flood_inundation) AS flood_prefs,
  (SELECT COUNT(DISTINCT prefecture_code) FROM nlftp.hazard.landslide_hazard_area) AS landslide_prefs
```

```sql id=tsunami_by_disaster
-- 津波の碑を伝える災害ごとにまとめ、津波浸水想定区域の中にある割合を出す（区域データのある道府県の碑・4基以上の災害）
WITH m AS (
  SELECT monument_id, disaster_name, geometry,
    TRY_CAST(regexp_extract(disaster_name, '([0-9]{4})年', 1) AS INTEGER) AS disaster_year
  FROM gsi.main.disaster_lore_monument
  WHERE is_tsunami
    AND LEFT(municipality_code, 2) IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation)
),
ts AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.tsunami_inundation z ON ST_Intersects(z.geometry, m.geometry)),
named AS (
  -- 同じ災害でも日付の書き方が碑ごとに違うので、括弧書きを外した名前と発生年でまとめる
  SELECT monument_id, disaster_year, trim(regexp_replace(disaster_name, '\(.*?\)+', '', 'g')) AS name
  FROM m
),
agg AS (
  SELECT
    name || '（' || CAST(disaster_year AS VARCHAR) || '年）' AS label,
    COUNT(*) AS n,
    COUNT(ts.monument_id) AS n_in
  FROM named LEFT JOIN ts USING (monument_id)
  WHERE disaster_year IS NOT NULL
  GROUP BY name, disaster_year
  HAVING COUNT(*) >= 4
)
SELECT
  label, n, n_in,
  ROUND(100 * n_in::DOUBLE / n, 1) AS pct,
  CAST(n_in AS VARCHAR) || ' / ' || CAST(n AS VARCHAR) || '基' AS bar_text,
  CASE WHEN n_in = 0 THEN '#f97316' ELSE '#3b82f6' END AS color
FROM agg
ORDER BY pct DESC, n DESC, label
```

```sql id=tsunami_summary
-- 津波の碑の全体と、噴火・山の崩落による津波（眉山崩壊・寛保津波）を除いた場合（プロットはしない）
WITH m AS (
  SELECT monument_id, disaster_name, geometry
  FROM gsi.main.disaster_lore_monument
  WHERE is_tsunami
    AND LEFT(municipality_code, 2) IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation)
),
ts AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.tsunami_inundation z ON ST_Intersects(z.geometry, m.geometry)),
f AS (
  SELECT m.*, ts.monument_id IS NOT NULL AS in_ts,
    (disaster_name LIKE '%眉山崩壊%' OR disaster_name LIKE '%寛保津波%') AS is_collapse
  FROM m LEFT JOIN ts USING (monument_id)
)
SELECT
  COUNT(*) AS n,
  COUNT(*) FILTER (WHERE in_ts) AS n_in,
  COUNT(*) FILTER (WHERE is_collapse) AS n_collapse,
  COUNT(*) FILTER (WHERE is_collapse AND in_ts) AS n_collapse_in,
  COUNT(*) FILTER (WHERE NOT is_collapse) AS n_excl,
  ROUND(100 * COUNT(*) FILTER (WHERE NOT is_collapse AND in_ts)::DOUBLE / COUNT(*) FILTER (WHERE NOT is_collapse), 1) AS pct_excl
FROM f
```

```sql id=tsunami_map_in
-- 津波浸水想定区域の中にある津波の碑
WITH m AS (
  SELECT monument_id, monument_name, disaster_name, latitude, longitude, geometry
  FROM gsi.main.disaster_lore_monument
  WHERE is_tsunami
    AND LEFT(municipality_code, 2) IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation)
),
ts AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.tsunami_inundation z ON ST_Intersects(z.geometry, m.geometry))
SELECT latitude, longitude, monument_name || '<br>' || disaster_name AS hover
FROM m
WHERE monument_id IN (SELECT monument_id FROM ts)
ORDER BY monument_id
```

```sql id=tsunami_map_out
-- 津波浸水想定区域の外にある津波の碑
WITH m AS (
  SELECT monument_id, monument_name, disaster_name, latitude, longitude, geometry
  FROM gsi.main.disaster_lore_monument
  WHERE is_tsunami
    AND LEFT(municipality_code, 2) IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation)
),
ts AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.tsunami_inundation z ON ST_Intersects(z.geometry, m.geometry))
SELECT latitude, longitude, monument_name || '<br>' || disaster_name AS hover
FROM m
WHERE monument_id NOT IN (SELECT monument_id FROM ts)
ORDER BY monument_id
```

```sql id=era_match
-- 碑が伝える災害の発生年（disaster_name の最初の西暦）で時代を分け、同じ種類の区域の中にある碑の割合を出す
WITH m AS (
  SELECT monument_id, LEFT(municipality_code, 2) AS pref, disaster_name, is_tsunami, is_flood, is_landslide, geometry,
    TRY_CAST(regexp_extract(disaster_name, '([0-9]{4})年', 1) AS INTEGER) AS disaster_year
  FROM gsi.main.disaster_lore_monument
),
ts AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.tsunami_inundation z ON ST_Intersects(z.geometry, m.geometry) WHERE m.is_tsunami),
fl AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.flood_inundation z ON ST_Intersects(z.geometry, m.geometry) WHERE m.is_flood),
ls AS (SELECT DISTINCT m.monument_id FROM m JOIN nlftp.hazard.landslide_hazard_area z ON ST_Intersects(z.geometry, m.geometry) WHERE m.is_landslide),
f AS (
  SELECT
    CASE
      WHEN disaster_year < 1868 THEN 1
      WHEN disaster_year < 1945 THEN 2
      WHEN disaster_year < 2000 THEN 3
      ELSE 4
    END AS era_ord,
    m.is_tsunami AND m.pref IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.tsunami_inundation) AS ts_target,
    m.is_flood AS fl_target,
    m.is_landslide AND m.pref IN (SELECT DISTINCT prefecture_code FROM nlftp.hazard.landslide_hazard_area) AS ls_target,
    (m.disaster_name LIKE '%眉山崩壊%' OR m.disaster_name LIKE '%寛保津波%') AS is_collapse,
    ts.monument_id IS NOT NULL AS in_ts,
    fl.monument_id IS NOT NULL AS in_fl,
    ls.monument_id IS NOT NULL AS in_ls
  FROM m
  LEFT JOIN ts USING (monument_id)
  LEFT JOIN fl USING (monument_id)
  LEFT JOIN ls USING (monument_id)
  WHERE m.disaster_year IS NOT NULL
)
SELECT
  ['江戸時代以前', '明治〜戦前', '戦後〜1999年', '2000年以降'][era_ord] AS era,
  COUNT(*) FILTER (WHERE ts_target) AS ts_n,
  ROUND(100 * COUNT(*) FILTER (WHERE ts_target AND in_ts)::DOUBLE / COUNT(*) FILTER (WHERE ts_target), 1) AS ts_pct,
  ROUND(100 * COUNT(*) FILTER (WHERE ts_target AND in_ts AND NOT is_collapse)::DOUBLE / COUNT(*) FILTER (WHERE ts_target AND NOT is_collapse), 1) AS ts_pct_excl_collapse,
  COUNT(*) FILTER (WHERE fl_target) AS fl_n,
  ROUND(100 * COUNT(*) FILTER (WHERE fl_target AND in_fl)::DOUBLE / COUNT(*) FILTER (WHERE fl_target), 1) AS fl_pct,
  COUNT(*) FILTER (WHERE ls_target) AS ls_n,
  ROUND(100 * COUNT(*) FILTER (WHERE ls_target AND in_ls)::DOUBLE / COUNT(*) FILTER (WHERE ls_target), 1) AS ls_pct
FROM f
GROUP BY era_ord
ORDER BY era_ord
```
