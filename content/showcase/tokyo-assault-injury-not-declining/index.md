---
title: 東京の刑法犯は16年で半分以下になったが、暴行と傷害は2009年と同じ約7,900件
description: 警視庁の町丁目別の認知件数で2009年と2025年を比較すると、刑法犯は20万5,501件から9万8,590件に減り、暴行と傷害は7,876件から7,888件でほぼ変わっていません。
publishedAt: 2026-11-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 犯罪
  - 防犯
  - 東京都
  - 町丁目
  - 国勢調査
datasets:
  - queria/npa
  - queria/e_stat
sources:
  - title: 区市町村の町丁別、罪種別及び手口別認知件数
    url: https://www.keishicho.metro.tokyo.lg.jp/about_mpd/jokyo_tokei/jokyo/ninchikensu.html
    publisher: 警視庁
  - title: 令和2年国勢調査 小地域集計
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
agentHint: 東京都の区市町村ごとに、暴行（violent_assault）と傷害（violent_injury）の認知件数の合計を2009年と2025年で比べて、刑法犯全体（total）の減り方と並べて出して
socialAnnounce: |-
  東京の刑法犯は2009年の20万5,501件から2025年の9万8,590件へ半分以下に減りましたが、暴行と傷害は7,876件から7,888件でほぼ同じでした。住民3,000人以上の町丁目でも、ほとんど減っていません。

  区市町村の防犯計画の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

東京都で警察が把握した刑法犯の件数（認知件数）は、2009年の20万5,501件から2025年の9万8,590件へ、半分以下になりました。人を殴る・蹴るなどの暴行と、人にけがをさせる傷害を合わせた件数は、2009年が7,876件、2025年が7,888件で、ほぼ同じです。町丁目ごとの件数に国勢調査の住民数を重ねると、住民が3,000人以上いる町丁目でも暴行と傷害は2009年の96.0%で、同じ町丁目の刑法犯全体は45.2%まで減っています。

区市町村で防犯を担当する人は、どの罪種が減り、どの罪種が減っていないかを、次の防犯計画で重点を置く対象を決める材料にできます。

## 窃盗は6割減り、暴行と傷害は2009年の水準に戻った

使うのは警視庁が毎年公表している[区市町村の町丁別、罪種別及び手口別認知件数](https://www.keishicho.metro.tokyo.lg.jp/about_mpd/jokyo_tokei/jokyo/ninchikensu.html)で、Queria では `npa` の `tokyo_town_crime` に2009年から2025年までを収録しています。1行が1つの町丁目の1年分（1月〜12月）で、刑法犯の認知件数が罪種の大分類と手口ごとに列になっています。

| 大分類     | 列                   | 主な内訳                                                            |
| ---------- | -------------------- | ------------------------------------------------------------------- |
| 凶悪犯     | `heinous_total`      | 強盗など                                                            |
| 粗暴犯     | `violent_total`      | 暴行（`violent_assault`）、傷害（`violent_injury`）、脅迫、恐喝など |
| 侵入窃盗   | `burglary_total`     | 空き巣、忍込み、事務所荒らしなど                                    |
| 非侵入窃盗 | `non_burglary_total` | 自転車盗、万引き、置引き、車上ねらいなど                            |
| その他     | `other_total`        | 詐欺、占有離脱物横領など                                            |

ここでは窃盗（侵入窃盗と非侵入窃盗の合計）と、粗暴犯のうち暴行と傷害の合計を、2009年を100とした指数で並べます。認知件数は警察が被害の届け出や通報で把握した件数なので、起きた数が同じでも、届け出や相談が増えれば件数は増えます。

```chart caption="東京都の認知件数（2009年=100）"
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ai_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ai_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 2}
        },
        "y": {
          "field": "ai_idx",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2009年=100", "grid": true}
        },
        "color": {
          "datum": "暴行・傷害",
          "type": "nominal",
          "scale": {"domain": ["暴行・傷害", "刑法犯全体", "窃盗"], "range": ["#ef4444", "#64748b", "#93c5fd"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 2}
        },
        "y": {
          "field": "total_idx",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2009年=100", "grid": true}
        },
        "color": {
          "datum": "刑法犯全体",
          "type": "nominal",
          "scale": {"domain": ["暴行・傷害", "刑法犯全体", "窃盗"], "range": ["#ef4444", "#64748b", "#93c5fd"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"theft_idx\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#93c5fd",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "theft_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d", "tickMinStep": 2}
        },
        "y": {
          "field": "theft_idx",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2009年=100", "grid": true}
        },
        "color": {
          "datum": "窃盗",
          "type": "nominal",
          "scale": {"domain": ["暴行・傷害", "刑法犯全体", "窃盗"], "range": ["#ef4444", "#64748b", "#93c5fd"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

窃盗は2009年の15万572件から2025年の6万2,444件へ減り、指数は41.5です。暴行と傷害は2015年に8,006件で最も多く、2021年には5,509件まで減りましたが、そこから4年続けて増え、2025年の指数は100.2です。内訳では、暴行が4,686件から4,867件へ増え、傷害は3,190件から3,021件へ減っています。2020年と2021年は、刑法犯全体・窃盗・暴行と傷害の3つの系列がそろって2019年より少なくなっています。

## 16年で減った10万件のうち、粗暴犯の分は207件

2009年から2025年までに減った刑法犯の件数を大分類ごとに分けると、減った分のほとんどは窃盗です。

```chart caption="東京都の刑法犯の認知件数の増減（2009年→2025年、大分類別）"
{
  "data": {"name": "change"},
  "transform": [
    {"window": [{"op": "sum", "field": "delta", "as": "cum"}]},
    {"calculate": "datum.measure === 'relative' ? datum.cum - datum.delta : 0", "as": "start"},
    {"calculate": "datum.cum", "as": "end"},
    {
      "calculate": "datum.measure !== 'relative' ? '合計' : datum.delta >= 0 ? '増加' : '減少'",
      "as": "kind"
    },
    {"calculate": "max(datum.start, datum.end)", "as": "top"}
  ],
  "encoding": {
    "x": {
      "field": "item",
      "type": "nominal",
      "sort": null,
      "title": null,
      "axis": {"labelAngle": -30}
    }
  },
  "layer": [
    {
      "mark": {"type": "bar", "clip": true},
      "encoding": {
        "y": {"field": "start", "type": "quantitative", "title": "認知件数（件）"},
        "y2": {"field": "end"},
        "color": {
          "field": "kind",
          "type": "nominal",
          "legend": null,
          "scale": {"domain": ["増加", "減少", "合計"], "range": ["#ef4444", "#3b82f6", "#64748b"]}
        },
        "tooltip": [
          {"field": "item", "title": "項目"},
          {"field": "delta", "title": "件数", "format": ","}
        ]
      }
    }
  ]
}
```

非侵入窃盗だけで8万47件減り、侵入窃盗の8,081件と合わせると、減った10万6,911件の8割を超えます。暴行・傷害のほかに脅迫や恐喝も含めた粗暴犯の大分類は207件の減少で、ほとんど変わっていません。

## 住民3,000人以上の町丁目でも、暴行と傷害は2009年の96.0%

繁華街の町丁目と住宅の多い町丁目を区別するため、町丁目ごとの件数に[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の町丁目別の住民数（e-Stat の `census_small_area_age`）を付け、住民の数で町丁目を3つに分けました。住民1,000人未満の町丁目には、新宿区の新宿３丁目・歌舞伎町１丁目や千代田区の丸の内１丁目のように、店や会社が集まり住む人の少ない場所が入ります。住民3,000人以上の町丁目は住宅の多い場所が中心ですが、北区の赤羽１丁目や中野区の中野５丁目のように、駅前の繁華街を含む町丁目も入ります。

警視庁の表と国勢調査では町丁目の表記が違う（「１丁目」と「一丁目」）ので、名前を正規化してから結合しています。住民数を付けられた町丁目は2025年に5,084か所で、東京都の刑法犯の99.5%、暴行・傷害の99.6%を含みます。住民数は2009年も2025年も2020年の値を使っているので、この図は住民あたりの率ではなく、件数の変化を比較しています。

```chart caption="住民数で分けた町丁目の認知件数（2025年、2009年=100）"
{
  "layer": [
    {
      "data": {"name": "groups"},
      "transform": [
        {"fold": ["ai_idx", "total_idx"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"ai_idx\": \"暴行・傷害\", \"total_idx\": \"刑法犯全体\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"ai_idx\",\"total_idx\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "町丁目の住民数（2020年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [0, 125], "zero": false, "nice": false},
          "axis": {"title": "2009年=100", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["暴行・傷害", "刑法犯全体"], "range": ["#ef4444", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["暴行・傷害", "刑法犯全体"]},
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    },
    {
      "data": {"name": "groups"},
      "transform": [
        {"fold": ["ai_idx", "total_idx"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"ai_idx\": \"暴行・傷害\", \"total_idx\": \"刑法犯全体\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"ai_idx\",\"total_idx\"], datum.__series)", "as": "__order"},
        {
          "calculate": "datum[{\"ai_idx\":\"ai_idx\",\"total_idx\":\"total_idx\"}[datum.__series]]",
          "as": "__text"
        },
        {"filter": "isValid(datum.__text)"}
      ],
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "町丁目の住民数（2020年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [0, 125], "zero": false, "nice": false},
          "axis": {"title": "2009年=100", "grid": true}
        },
        "xOffset": {"field": "__name", "sort": ["暴行・傷害", "刑法犯全体"]},
        "text": {"field": "__text"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 100, "type": "quantitative"}
      }
    }
  ]
}
```

住民1,000人未満の町丁目では、暴行と傷害は2009年の109.7%に増えました。住民1,000〜3,000人の町丁目では101.1%、住民3,000人以上の町丁目でも96.0%です。同じ町丁目の刑法犯全体は、3つの群とも2009年の45.2〜58.2%まで減っています。住民3,000人以上の町丁目から、2025年の暴行・傷害が多い20か所（赤羽１丁目や中野５丁目など）を除いても、残りの暴行・傷害は2009年の96.2%です。暴行と傷害は、件数の多い一部の町丁目に限らず、住む人の多い町丁目全体でほとんど減っていません。2025年の暴行・傷害の48.5%は住民3,000人以上の町丁目で起きていて、住民1,000人未満の町丁目は21.1%です。

## 2025年に暴行か傷害があった町丁目は2,596か所

下の地図は、2025年に暴行か傷害が1件以上あった2,596か所の町丁目を、その町丁目の代表点に置き、円の面積を件数に比例させたものです。2,596か所のうち1,899か所が23区、697か所が23区以外の市町村にあり、23区以外の点に載る暴行・傷害は1,369件です。

```map
type: map
caption: "2025年の暴行・傷害の認知件数（町丁目の代表点、円の面積が件数）"
layers:
  - from: map_2025
    lng: lon
    lat: lat
    label: name
lng: 139.55
lat: 35.69
zoom: 9.2
```

## 防犯計画の重点を見直すときの使い方

- 自分の区市町村の町丁目について、窃盗と暴行・傷害の件数を2009年と2025年で並べると、総数の減り方と罪種ごとの減り方の違いを、担当地域の数字で確認できます
- 住民の多い町丁目の中から暴行・傷害の件数が多い場所を抽出すると、繁華街の夜間の見回りとは別に、どんな場面で起きた暴行・傷害なのかを警察署に確認する町丁目の一覧になります
- 防犯計画の成果指標が刑法犯の総数だけだと、総数の大半を占める窃盗が減っているために、暴行と傷害がほとんど減っていないことが分かりません。罪種を分けた指標も成果指標に加えておくと、計画を見直すときの判断材料になります

## データの出典

本記事は警視庁の[区市町村の町丁別、罪種別及び手口別認知件数](https://www.keishicho.metro.tokyo.lg.jp/about_mpd/jokyo_tokei/jokyo/ninchikensu.html)（2009〜2025年）と、総務省統計局の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域集計（町丁・字等別人口）を、2026年11月1日時点で集計しています。件数はすべて1月から12月までの認知件数です。

Queria は、警視庁が年ごとに公表している町丁目別の統計を2009年から1つのテーブルにまとめ、国勢調査の小地域集計とともに、列名を統一し、各列の説明を付けて公開しています。本記事で使った[町丁目別の犯罪認知件数テーブル](/datasets/queria/npa/crime/tokyo_town_crime)と[町丁目別の年齢別人口テーブル](/datasets/queria/e_stat/census/census_small_area_age)から、自分の区市町村の町丁目ごとに、罪種ごとの件数の変化を集計できます。

```sql id=trend
-- 東京都全体の罪種別の認知件数（町丁字が不明の行も含む）
SELECT year,
  SUM(total) AS total,
  SUM(burglary_total + non_burglary_total) AS theft,
  SUM(violent_assault + violent_injury) AS ai,
  SUM(violent_assault) AS assault,
  SUM(violent_injury) AS injury,
  ROUND(100.0 * SUM(total) / FIRST_VALUE(SUM(total)) OVER (ORDER BY year), 1) AS total_idx,
  ROUND(100.0 * SUM(burglary_total + non_burglary_total) / FIRST_VALUE(SUM(burglary_total + non_burglary_total)) OVER (ORDER BY year), 1) AS theft_idx,
  ROUND(100.0 * SUM(violent_assault + violent_injury) / FIRST_VALUE(SUM(violent_assault + violent_injury)) OVER (ORDER BY year), 1) AS ai_idx
FROM npa.crime.tokyo_town_crime
WHERE year BETWEEN 2009 AND 2025
GROUP BY year
ORDER BY year
```

```sql id=change
-- 2009年から2025年への増減を罪種の大分類ごとに分ける
WITH s AS (
  SELECT
    SUM(total) FILTER (WHERE year = 2009) AS t09,
    SUM(non_burglary_total) FILTER (WHERE year = 2025) - SUM(non_burglary_total) FILTER (WHERE year = 2009) AS d_nonburg,
    SUM(burglary_total) FILTER (WHERE year = 2025) - SUM(burglary_total) FILTER (WHERE year = 2009) AS d_burg,
    SUM(other_total) FILTER (WHERE year = 2025) - SUM(other_total) FILTER (WHERE year = 2009) AS d_other,
    SUM(heinous_total) FILTER (WHERE year = 2025) - SUM(heinous_total) FILTER (WHERE year = 2009) AS d_heinous,
    SUM(violent_total) FILTER (WHERE year = 2025) - SUM(violent_total) FILTER (WHERE year = 2009) AS d_violent
  FROM npa.crime.tokyo_town_crime
  WHERE year IN (2009, 2025)
)
SELECT * FROM (
  SELECT 1 AS ord, '2009年' AS item, 'absolute' AS measure, t09 AS delta FROM s
  UNION ALL SELECT 2, '非侵入窃盗', 'relative', d_nonburg FROM s
  UNION ALL SELECT 3, '侵入窃盗', 'relative', d_burg FROM s
  UNION ALL SELECT 4, 'その他の刑法犯', 'relative', d_other FROM s
  UNION ALL SELECT 5, '凶悪犯', 'relative', d_heinous FROM s
  UNION ALL SELECT 6, '粗暴犯', 'relative', d_violent FROM s
  UNION ALL SELECT 7, '2025年', 'total', 0 FROM s
)
ORDER BY ord
```

```sql id=towns
-- 町丁目ごとの暴行・傷害と刑法犯の認知件数に、令和2年国勢調査の住民数を付ける
-- 警視庁の表は「歌舞伎町１丁目」、国勢調査は「歌舞伎町一丁目」と書くので、丁目の番号を漢数字に直して名前で結合する
WITH c AS (
  SELECT year, municipality, town,
    violent_assault + violent_injury AS ai, total
  FROM npa.crime.tokyo_town_crime
  WHERE town IS NOT NULL AND town <> '以下不詳' AND year IN (2009, 2025)
), k AS (
  SELECT * FROM (VALUES ('１', '一'), ('２', '二'), ('３', '三'), ('４', '四'), ('５', '五'), ('６', '六'), ('７', '七'), ('８', '八'), ('９', '九'), ('１０', '十'), ('１１', '十一'), ('１２', '十二'), ('１３', '十三'), ('１４', '十四'), ('１５', '十五'), ('１６', '十六'), ('１７', '十七'), ('１８', '十八'), ('１９', '十九'), ('２０', '二十'), ('２１', '二十一'), ('２２', '二十二'), ('２３', '二十三'), ('２４', '二十四'), ('２５', '二十五'), ('２６', '二十六'), ('２７', '二十七'), ('２８', '二十八'), ('２９', '二十九'), ('３０', '三十')) AS k(fw, kan)
), named AS (
  SELECT c.*,
    REPLACE(c.municipality || COALESCE(regexp_replace(c.town, '[０-９]+丁目$', '') || k.kan || '丁目', c.town), 'ヶ', 'ケ') AS nm
  FROM c LEFT JOIN k ON k.fw = regexp_extract(c.town, '([０-９]+)丁目$', 1)
), pop_raw AS (
  SELECT area, REPLACE(area_name, 'ヶ', 'ケ') AS nm, area_level, value
  FROM e_stat.census.census_small_area_age
  WHERE area LIKE '13%' AND cat01 = '0010' AND area_level IN ('small_area', 'small_area_detail')
), pop AS (
  -- 同じ名前の区画が丁目の内訳にあれば内訳を足し、無ければ町丁・字の値を使う
  SELECT nm,
    COALESCE(SUM(value) FILTER (WHERE area_level = 'small_area_detail'), SUM(value)) AS residents,
    COALESCE(MIN(area) FILTER (WHERE area_level = 'small_area_detail'), MIN(area)) AS area
  FROM pop_raw
  GROUP BY nm
)
SELECT n.year, n.municipality, n.town, p.area, p.residents, n.ai, n.total,
  CASE WHEN p.residents < 1000 THEN 1 WHEN p.residents < 3000 THEN 2 ELSE 3 END AS grp
FROM named n JOIN pop p USING (nm)
```

```sql id=coverage
-- 住民数を付けられた町丁目が、2025年の刑法犯と暴行・傷害の何%を占めるか（プロットはしない）
SELECT
  (SELECT SUM(total) FROM towns WHERE year = 2025) AS matched_total,
  (SELECT SUM(ai) FROM towns WHERE year = 2025) AS matched_ai,
  (SELECT COUNT(*) FROM towns WHERE year = 2025) AS matched_towns,
  ROUND(100.0 * (SELECT SUM(total) FROM towns WHERE year = 2025) / (SELECT total FROM trend WHERE year = 2025), 1) AS total_pct,
  ROUND(100.0 * (SELECT SUM(ai) FROM towns WHERE year = 2025) / (SELECT ai FROM trend WHERE year = 2025), 1) AS ai_pct
```

```sql id=groups
-- 住民数で町丁目を3つに分け、2009年を100とした2025年の値を出す
SELECT grp,
  CASE grp WHEN 1 THEN '住民1,000人未満' WHEN 2 THEN '住民1,000〜3,000人' ELSE '住民3,000人以上' END AS label,
  COUNT(DISTINCT area) AS towns,
  SUM(ai) FILTER (WHERE year = 2009) AS ai09,
  SUM(ai) FILTER (WHERE year = 2025) AS ai25,
  SUM(total) FILTER (WHERE year = 2009) AS total09,
  SUM(total) FILTER (WHERE year = 2025) AS total25,
  ROUND(100.0 * SUM(ai) FILTER (WHERE year = 2025) / SUM(ai) FILTER (WHERE year = 2009), 1) AS ai_idx,
  ROUND(100.0 * SUM(total) FILTER (WHERE year = 2025) / SUM(total) FILTER (WHERE year = 2009), 1) AS total_idx,
  ROUND(100.0 * SUM(ai) FILTER (WHERE year = 2025) / SUM(SUM(ai) FILTER (WHERE year = 2025)) OVER (), 1) AS ai25_share
FROM towns
GROUP BY grp
ORDER BY grp
```

```sql id=few_residents
-- 住民1,000人未満の町丁目のうち、2025年の刑法犯が多い10か所（プロットはしない）
SELECT municipality, town, residents, total, ai
FROM towns
WHERE year = 2025 AND grp = 1
ORDER BY total DESC, municipality, town
LIMIT 10
```

```sql id=map_2025
-- 2025年に暴行・傷害が1件以上あった町丁目の代表点
SELECT t.municipality || t.town AS name, t.ai, t.residents, s.y_code AS lat, s.x_code AS lon
FROM towns t JOIN e_stat.boundary.small_area s ON s.key_code = t.area
WHERE t.year = 2025 AND t.ai > 0
ORDER BY t.ai, name
```

```sql id=grp3_top
-- 住民3,000人以上の町丁目のうち、2025年の暴行・傷害が多い20か所（プロットはしない）
SELECT municipality, town, residents, ai,
  ROW_NUMBER() OVER (ORDER BY ai DESC, municipality, town) AS rn
FROM towns
WHERE year = 2025 AND grp = 3
QUALIFY rn <= 20
ORDER BY rn
```

```sql id=grp3_robust
-- 上の20か所を除いても、住民3,000人以上の町丁目の暴行・傷害が2009年の何%か（プロットはしない）
SELECT
  SUM(ai) FILTER (WHERE year = 2009) AS ai09,
  SUM(ai) FILTER (WHERE year = 2025) AS ai25,
  ROUND(100.0 * SUM(ai) FILTER (WHERE year = 2025) / SUM(ai) FILTER (WHERE year = 2009), 1) AS ai_idx
FROM towns t
WHERE grp = 3
  AND NOT EXISTS (SELECT 1 FROM grp3_top g WHERE g.municipality = t.municipality AND g.town = t.town)
```

```sql id=map_summary
-- 地図の点を23区とそれ以外に分けて数える（プロットはしない）
SELECT
  -- name は区市町村名と町丁目名をつないだもので、先頭が「〇〇区」なら23区
  CASE WHEN regexp_matches(name, '^[^市町村区]*区') THEN '23区' ELSE '23区以外' END AS area,
  COUNT(*) AS towns, SUM(ai) AS ai
FROM map_2025
GROUP BY 1
ORDER BY 1
```
