---
title: 日平均気温が15℃を下回る日は、札幌と福岡で40日違う
description: 気象庁のアメダス日別平年値で、日平均気温が秋に初めて15℃を下回る日を地点ごとに求めました。札幌は10月3日、福岡は11月13日で、全国の主要地点では2か月以上の差があります。日最高気温が30℃以上の日は那覇で年101日、仙台と札幌で0日です
publishedAt: 2026-07-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 気象
  - 平年値
  - 季節需要
datasets:
  - queria/jma
sources:
  - title: 過去の気象データ検索（日別平年値・地点情報）
    url: https://www.data.jma.go.jp/stats/etrn/index.php
    publisher: 気象庁
agentHint: 主要都市ごとに、日最高気温の平年値が30度以上になる真夏日相当の期間を最初の日と最後の日で出して。都市間でその長さを比べて
socialAnnounce: |-
  気象庁アメダスの日別平年値を全国で分析しました。

  気温が下がる時期は北から南へ2か月以上ずれ、沖縄・奄美では冬が訪れません。季節商材の投入時期や在庫配分の判断に。
  Queriaは気象などのオープンデータを業務で使える形に整えて公開しています。
---

気象庁のアメダス日別平年値で、日平均気温が秋に初めて15℃を下回る日を地点ごとに求めると、札幌は10月3日、東京は11月3日、福岡は11月13日でした。札幌と福岡の差は40日ほどで、全国の主要地点では北日本・山地の9月中旬から南西諸島の12月まで、2か月以上の開きがあります。那覇・石垣島など10地点では、平年値で15℃を下回る日がありません。夏は、日最高気温の平年値が30℃以上になる日が那覇で年101日、東京で46日で、仙台と札幌では0日です。

暖房機器や鍋物、ホットドリンク、冷房や冷たい飲料、熱中症対策グッズといった季節商材は、需要が増え始める時期を外すと、品切れと売れ残りの両方が起きます。全国のチェーンで同じ時期に売り場を切り替えると、早く寒くなる地域では品切れ、遅い地域では売れ残りが起きやすくなります。この記事では、気象庁が[過去の気象データ検索](https://www.data.jma.go.jp/stats/etrn/index.php)で公開しているアメダス日別平年値を使い、地域ごとに気温がいつ下がり、夏にどれだけ暑くなるかを集計します。

## 使用するデータ

気象庁「アメダス日別平年値」（`mart_jma_normals_daily`）を使います。統計期間1991〜2020年の30年平均から求めた、観測所ごと・月日ごとの基準値です。日平均・日最高・日最低の気温、日照時間、降水量、積雪の深さが、閏日（2月29日）を含む366日ぶん入っています。

主な列は次のとおりです。

| カラム             | 内容                 |
| ------------------ | -------------------- |
| `station_id`       | アメダス観測所コード |
| `month` / `day`    | 月・日               |
| `temp_avg_c`       | 日平均気温（℃）      |
| `temp_max_c`       | 日最高気温（℃）      |
| `temp_min_c`       | 日最低気温（℃）      |
| `precipitation_mm` | 降水量（mm）         |

観測所コードで観測所マスタ（`mart_jma_stations`）と結合すると、緯度・経度・標高を取得できます。東京（観測所コード `44132`）の年始の平年値で、データの中身を確認します。

```sql
SELECT month, day, temp_avg_c, temp_max_c, temp_min_c, precipitation_mm FROM jma.main.mart_jma_normals_daily WHERE station_id = '44132' AND month = 1 AND day <= 5 ORDER BY day
```

## 日平均気温の平年値は、札幌では冬に−3.6℃まで下がり、那覇では16.8℃までしか下がらない

7つの主要都市について、日平均気温の平年値（`temp_avg_c`）を366日ぶん並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "curve_sapporo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#3b82f6", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "札幌",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_sendai"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#22c55e", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "仙台",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#64748b", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "東京",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_nagoya"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#7c3aed", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "名古屋",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_osaka"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "大阪",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_fukuoka"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#ec4899", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "福岡",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_naha"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"m\"]) && isValid(datum[\"t\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#ef4444", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [{"field": "m", "type": "quantitative"}, {"field": "t", "type": "quantitative"}],
        "x": {
          "field": "m",
          "type": "quantitative",
          "scale": {"domain": [1, 13], "zero": false, "nice": false},
          "axis": {"title": "月", "format": "d", "tickMinStep": 1}
        },
        "y": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "日平均気温（℃）", "grid": true}
        },
        "color": {
          "datum": "那覇",
          "type": "nominal",
          "scale": {
            "domain": ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "那覇"],
            "range": ["#3b82f6", "#22c55e", "#64748b", "#7c3aed", "#f97316", "#ec4899", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

札幌は最も寒い日の平年値が約 −3.6℃、最も暖かい日が約23.0℃で、年間の振れ幅は26℃以上あります。那覇は最も寒い日でも約16.8℃、最も暖かい日は約29.2℃で、冬も他の都市の春や秋と同じくらいの気温です。

商品の需要が増え始める時期は、それぞれの都市の曲線が、その商品の切り替えの目安になる気温を通る日で決まると考えられます。曲線が左右にずれている分だけ、地域ごとに需要期もずれます。那覇のように冬の気温が下がらない地域では、防寒商材の市場は小さく、冷たい商材の需要は1年を通して続くと考えられます。

## 日平均気温が15℃を下回る日は、北日本・山地の9月中旬から南西諸島の12月まで2か月以上違う

各地点で、8月1日以降に日平均気温の平年値が初めて15℃を下回る日を求めました。15℃は気象庁が定めた季節の区切りではなく、季節商材を切り替える時期の目安としてこの記事で置いた基準です。8月以降に限るのは、1月1日から探すと冬の日が該当してしまうためです。対象は気象台・測候所など職員が配置されている主要地点（151地点）で、気温を測っていない無人の観測所を除くためにこの条件にしています。青いほど早く、赤いほど遅く15℃を下回る地点です。

```map
type: map
layers:
  - from: coldmap
    lng: lon
    lat: lat
    color: doy
    label: name
    name: "冷え込み到来日"
  - from: nowinter
    lng: lon
    lat: lat
    label: name
    name: "冬が来ない地点"
lng: 136
lat: 35
zoom: 3.2
```

15℃を下回る日は、南の地点ほど遅く、同じ地域では標高の低い地点ほど遅くなります。最も早いのは奥日光や旭川などの北日本と山地の地点で、9月中旬から下旬です。関東・近畿の平野部では11月上旬、九州南部や南西諸島では12月に入ってからで、2か月以上の差があります。標高も影響するので、奥日光や軽井沢のような山地の観測所は、緯度が近い平野部の地点より早く15℃を下回ります。

地図で緑の10地点（那覇・石垣島・宮古島や奄美の名瀬など）は、平年値で日平均気温が15℃を下回る日がない地点です。これらの地域では防寒商材の需要が増え始める時期がないので、季節商戦の計画を別に立てる必要があると考えられます。

主要都市の、日平均気温が15℃を下回る最初の日は次のとおりです。

| 都市   | 平均気温が15℃を下回る最初の日 |
| ------ | ----------------------------- |
| 札幌   | 10月3日                       |
| 仙台   | 10月20日                      |
| 東京   | 11月3日                       |
| 名古屋 | 11月4日                       |
| 大阪   | 11月11日                      |
| 福岡   | 11月13日                      |
| 那覇   | （到来しない）                |

札幌と福岡では40日ほどの差があります。全国で同じ時期に防寒商材を投入すると、この差の分だけ北では品切れ、南では売れ残りが起きやすくなります。地点ごとの日付を一覧にしておくと、地域ブロックごとに売り場の切り替え時期を前後にずらせます。

## 日最高気温が30℃以上の日は、那覇で年101日、仙台と札幌で0日

夏は、暑い日が続く期間の長さに地域差があります。日最高気温の平年値が30℃以上になる日（真夏日に相当する日）を主要都市で集計しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "summer"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "days", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "days",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "真夏日相当の平年日数（日）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都市"},
          "sort": null
        }
      }
    }
  ]
}
```

那覇は年101日で最も長く、鹿児島（78日）、大阪（73日）、名古屋（68日）が続きます。東京は46日、新潟は33日です。仙台と札幌では、日最高気温の平年値が30℃に届く日がありません。平年値は30年分を平均してならした値なので、実際の真夏日の日数はこれより多くなります。この日数は、地域ごとの暑さの規模を比較する目安として使えます。

冷房・冷たい飲料・熱中症対策といった夏の商材は、需要期の長さが地域によって数倍違います。真夏日に相当する日が3か月を超える那覇と、平年値では真夏日がない仙台・札幌では、商品構成も在庫の量も変える必要があると考えられます。

## データの活用

日別平年値を地域ごとに集計すると、季節商材の計画に次のように使えます。

- 地域ブロック別の売り場の切り替え日程: 日平均気温が15℃を下回る日をもとに、防寒商材の投入時期をブロックごとに前後にずらす
- 在庫配分の重み付け: 真夏日に相当する日数の比で、夏の商材の初期投入量を地域ごとに配分する
- 別の日程で扱う市場: 15℃を下回る日がない南西諸島や、真夏日がない北日本を、別の日程の市場として扱う
- 販促の時期: 気温が早く下がる地域から順に、季節キャンペーンを始める

## データの出典

本記事は、気象庁が[過去の気象データ検索](https://www.data.jma.go.jp/stats/etrn/index.php)で公開している日別平年値と地点情報を、2026年7月11日時点で取得して集計しています。平年値は統計期間1991〜2020年の30年平均から求めた基準値です。

Queriaは、気象庁の日別平年値と観測所の情報を、列名・単位・文字コードを統一し、観測所の位置や統計期間の説明を付けて公開しています。本記事で使った[アメダス日別平年値テーブル](/datasets/queria/jma/main/mart_jma_normals_daily)と[観測所マスタ](/datasets/queria/jma/main/mart_jma_stations)から、自社の商圏に近い地点の平年値を確認できます。

```sql id=curve_sapporo
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '14163' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=curve_sendai
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '34392' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=curve_tokyo
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '44132' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=curve_nagoya
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '51106' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=curve_osaka
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '62078' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=curve_fukuoka
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '82182' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=curve_naha
SELECT (month + (day - 1) / 31.0) AS m, temp_avg_c AS t FROM jma.main.mart_jma_normals_daily WHERE station_id = '91197' AND temp_avg_c IS NOT NULL ORDER BY month, day
```

```sql id=coldmap
WITH cold AS (SELECT n.station_id, MIN(n.month * 100 + n.day) AS md FROM jma.main.mart_jma_normals_daily n WHERE n.temp_avg_c < 15 AND n.month * 100 + n.day >= 801 GROUP BY n.station_id), tempst AS (SELECT DISTINCT station_id FROM jma.main.mart_jma_normals_daily WHERE temp_avg_c IS NOT NULL) SELECT s.name, s.lat, s.lon, dayofyear(make_date(2001, cold.md // 100, cold.md % 100)) AS doy, ((cold.md // 100)::VARCHAR || '月' || (cold.md % 100)::VARCHAR || '日') AS onset_label FROM jma.main.mart_jma_stations s JOIN tempst t ON t.station_id = s.station_id JOIN cold ON cold.station_id = s.station_id WHERE s.is_office = true ORDER BY doy
```

```sql id=nowinter
WITH cold AS (SELECT n.station_id, MIN(n.month * 100 + n.day) AS md FROM jma.main.mart_jma_normals_daily n WHERE n.temp_avg_c < 15 AND n.month * 100 + n.day >= 801 GROUP BY n.station_id), tempst AS (SELECT DISTINCT station_id FROM jma.main.mart_jma_normals_daily WHERE temp_avg_c IS NOT NULL) SELECT s.name, s.lat, s.lon FROM jma.main.mart_jma_stations s JOIN tempst t ON t.station_id = s.station_id LEFT JOIN cold ON cold.station_id = s.station_id WHERE s.is_office = true AND cold.md IS NULL ORDER BY s.lat DESC
```

```sql id=summer
WITH cities(sid, city) AS (VALUES ('14163', '札幌'), ('34392', '仙台'), ('54232', '新潟'), ('44132', '東京'), ('51106', '名古屋'), ('62078', '大阪'), ('67437', '広島'), ('82182', '福岡'), ('88317', '鹿児島'), ('91197', '那覇')) SELECT c.city, COUNT(*) FILTER (WHERE n.temp_max_c >= 30) AS days FROM jma.main.mart_jma_normals_daily n JOIN cities c ON n.station_id = c.sid GROUP BY c.city ORDER BY days ASC
```
