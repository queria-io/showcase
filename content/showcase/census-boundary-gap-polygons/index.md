---
title: 国勢調査の町丁字等別境界データには、統計と結合できないポリゴンが87件ある
description: e-Stat の令和2年国勢調査 町丁字等別境界データには、町丁字コードも人口もない87件のポリゴンが38市区町村にあります。塩竈市では海岸線沿いに8件あり、須崎市には約10km²のものがあります。特定する SQL と、用途ごとの扱い方を説明します。
publishedAt: 2026-04-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - GIS
  - 国勢調査
  - 境界データ
  - データエンジニアリング
datasets:
  - queria/e_stat
sources:
  - title: 統計地理情報システム（統計GIS） 境界データダウンロード
    url: https://www.e-stat.go.jp/gis
    publisher: 総務省統計局
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
agentHint: 未割当ポリゴン(HCODE=8101でKEY_CODEが2桁)を都道府県別に集計して、面積の合計が大きい都道府県を出して
socialAnnounce: |-
  e-Stat 国勢調査の境界データに、定義書に記載のない87件のポリゴンが含まれています。

  町丁字コードで結合できず、空間結合やジオコーディングで集計ズレの原因になります。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

e-Stat の[令和2年国勢調査 町丁字等別境界データ](https://www.e-stat.go.jp/gis/statmap-search?page=1&type=2&aggregateUnitForBoundary=A&toukeiCode=00200521&toukeiYear=2020&serveyId=A002005212020&coordsys=1&format=gml&datum=2011)には、町丁字コードも名称も人口もないポリゴンが87件含まれています。38の市区町村にあり、宮城県塩竈市では8件が海岸線沿いに並び、高知県須崎市には面積が約10km²のものがあります。このデータは全国約22万区画のポリゴンを収録していて、[定義書](https://www.e-stat.go.jp/help/data-definition-information/downloaddata/A002005212020.pdf)は HCODE=8101 を「町丁字等」と定義しています。KEY_CODE が都道府県コード（2桁）だけになるレコードについては、定義書にも[補足説明](https://www.e-stat.go.jp/sites/default/files/pdf/gis/notes/00200521.pdf)にも記載がありません。

これらのレコードは町丁字コードがないので統計データと結合できず、空間結合や逆ジオコーディングで町丁字が「該当なし」になる原因になります。この記事では、SQL でこれらのレコードを特定し、位置と面積を地図とグラフで示します。

## 町丁字の KEY_CODE は通常9桁か11桁

町丁字等別境界データの各レコードには、ポリゴン（境界形状）とともに以下のフィールドが設定されています。

| フィールド                     | 内容                            | 例                             |
| ------------------------------ | ------------------------------- | ------------------------------ |
| KEY_CODE                       | 町丁字コード（PREF + KEYCODE2） | 13101001000                    |
| KEYCODE2                       | マッチング番号                  | 101001000                      |
| HCODE                          | 分類コード                      | 8101=町丁字等、8154=水面調査区 |
| PREF_NAME / CITY_NAME / S_NAME | 名称                            | 東京都 / 千代田区 / 永田町     |
| JINKO / SETAI                  | 人口・世帯数                    | 3056 / 2049                    |
| AREA                           | 面積（㎡）                      | 523849.2                       |

KEY_CODE は都道府県コード（2桁）と KEYCODE2 を連結した値で、統計データとのリンクキーになります。通常は9桁（大字・町）または11桁（字・丁目）です。

## KEY_CODE が2桁しかないポリゴンは87件ある

HCODE=8101（町丁字等）のレコードのうち、KEY_CODE が都道府県コード（2桁）しかないものを抽出します。これらは KEYCODE2 が NULL のため、統計データと結合できません。水面調査区（HCODE=8154）は定義書に記載のある区分なので、対象に含めていません。

```sql
SELECT KEY_CODE, PREF_NAME, CITY_NAME, S_NAME, KEYCODE2, S_AREA, KIHON1, KIHON2, HCODE, JINKO, SETAI, ROUND(AREA) AS area_m2 FROM e_stat.boundary.raw_census_boundary WHERE HCODE = 8101 AND LENGTH(KEY_CODE) = 2 ORDER BY PREF_NAME, CITY_NAME
```

令和2年のデータでは87件が該当します。別の年次のデータでは、件数も対象の市区町村も変わります。すべてのレコードで S_NAME（町丁字名称）が NULL、JINKO（人口）と SETAI（世帯数）が0です。S_AREA・KIHON1・KIHON2 もゼロ埋め（000000・0000・00）で、町丁字への帰属情報が一切ありません。

これらのレコードに共通する特徴をまとめます。

- KEY_CODE が都道府県コード（2桁）のみ。KEYCODE2 が NULL
- HCODE = 8101（町丁字等）。水面調査区（8154）ではない
- 人口0、世帯数0、名称なしで、ジオメトリ（形状）はある
- S_AREA・KIHON1・KIHON2 がすべてゼロ埋め

## 那智勝浦町・塩竈市・長崎市に多く、38の市区町村にある

87件を市区町村ごとに集計します。

```chart
{
  "layer": [
    {
      "data": {"name": "gap_by_muni"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "cnt", "type": "quantitative"},
          {"field": "municipality", "type": "nominal"}
        ],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "件数", "grid": true}
        },
        "y": {"field": "municipality", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null}
      }
    }
  ]
}
```

那智勝浦町（12件）、塩竈市（8件）、長崎市（5件）が多く、沿岸部や離島のある市区町村に多い傾向があります。群馬県伊勢崎市・埼玉県新座市・栃木県小山市・川崎市多摩区のような内陸部の市区町村にもあり、全部で38の市区町村にわたります。

## 塩竈市の未割当ポリゴンは、海岸線沿いの細い領域にある

8件がある宮城県塩竈市の未割当ポリゴンを地図に表示します。地図には列名を正規化した `stg_census_boundary` テーブルを使い、ほかの集計では元データの列名のままの `raw_census_boundary` テーブルを使っています。赤色が未割当ポリゴン、青色が通常の町丁字ポリゴンです。

```map
type: map
layers:
  - from: shiogama_normal
    geojson: geojson
    name: "通常"
  - from: shiogama_gap
    geojson: geojson
    name: "未割当"
lng: 141.02
lat: 38.32
zoom: 12
```

赤色の未割当ポリゴンは沿岸部に集まっていて、通常の町丁字ポリゴン（青色）がない海岸線沿いの細い領域にあります。

これらの未割当ポリゴンは、町丁字等の調査区に含まれなかった残りの領域と考えられます。定義書と補足説明には説明がないので、位置と属性から推定した解釈です。沿岸部では海岸線と町丁字境界の間、内陸部では道路や河川沿いの領域にあるものが見られます。

## 大半は1万㎡以下だが、須崎市には約10km²のものがある

元データの AREA フィールド（図郭から算出された面積）で、87件の面積の分布を確認します。AREA の値をそのまま使っているので、ジオメトリから計算した測地面積とは一致しません。

```chart
{
  "height": 120,
  "layer": [
    {
      "data": {"name": "gap_area_dist"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "municipality", "type": "nominal"},
          {"field": "area_m2", "type": "quantitative"},
          {"field": "y_val", "type": "quantitative"}
        ],
        "x": {
          "field": "area_m2",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "面積（㎡）", "grid": true}
        },
        "y": {
          "field": "y_val",
          "type": "quantitative",
          "scale": {"domain": [-1, 1], "zero": false, "nice": false},
          "axis": {"title": null, "labels": false, "ticks": false, "domain": false}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 10000, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

大半は1万㎡以下ですが、高知県須崎市のものは1,000万㎡（約10km²）あり、小さな町丁字より広いものもあります。面積の大きいものは、市区町村の沿岸部や離島全体を覆う領域です。

## 統計と結合するときは除外し、面積を計算するときは含める

未割当ポリゴンを含めるかどうかは、分析の目的によって決めます。町丁字等の統計データと結合する場合は、KEYCODE2 が NULL のレコードを除外します。

```sql run=false
-- KEYCODE2 が存在するレコードのみ使う
SELECT * FROM e_stat.boundary.raw_census_boundary WHERE KEYCODE2 IS NOT NULL;

-- または KEY_CODE の桁数で判定する
SELECT * FROM e_stat.boundary.raw_census_boundary WHERE LENGTH(KEY_CODE) > 2;
```

市区町村の空間カバレッジを正確に把握したい場合や、ポリゴン間に隙間がないことを前提とした面積計算を行う場合は、未割当ポリゴンを含めたほうが適切です。

### 未割当ポリゴンが影響する処理

未割当ポリゴンの存在を意識しないと、以下の処理で想定外の結果が生じることがあります。

- 空間結合（Spatial Join）: ポイントデータが未割当ポリゴンにヒットし、町丁字名・人口が NULL になる
- 統計データとのリンク: KEY_CODE で結合すると、都道府県単位のレコードが意図せずマッチする
- 逆ジオコーディング: 座標から町丁字を特定するときに、未割当ポリゴンが返されて「該当なし」になる

## GIS実務への活用

この記事の SQL は、次の業務で使えます。

- 空間結合の設計: 未割当ポリゴンの存在を前提に、結合結果の NULL チェックや除外条件を検討する
- 境界データの品質検証: 新しい年次のデータを取得したときに、同様のレコードがないか確認する
- 空間データのETLパイプライン: 目的に応じたフィルタリングをパイプラインに組み込む

## データの出典

本記事は、e-Stat の[統計地理情報システム（統計GIS）](https://www.e-stat.go.jp/gis)で公開されている[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の町丁字等別境界データを、2026年7月11日時点で取得して集計しています。対象は47都道府県の約22万区画です。

Queriaは、[国勢調査の小地域境界データ](/datasets/queria/e_stat)をはじめとする官公庁のオープンデータを、列名を正規化し、テーブルと列の説明を付けて公開しています。この記事の SQL をそのまま実行して、自分の地域の未割当ポリゴンを確認したり、手元のポイントデータとの空間結合で除外条件を試したりできます。

```sql id=gap_by_muni
SELECT PREF_NAME || ' ' || COALESCE(CITY_NAME, '(不明)') AS municipality, COUNT(*) AS cnt FROM e_stat.boundary.raw_census_boundary WHERE HCODE = 8101 AND LENGTH(KEY_CODE) = 2 GROUP BY municipality ORDER BY cnt DESC
```

```sql id=shiogama_normal
SELECT ST_AsGeoJSON(geometry) AS geojson, 1 AS z_val FROM e_stat.boundary.stg_census_boundary WHERE hcode = 8101 AND LENGTH(key_code) > 2 AND prefecture_name = '宮城県' AND city_name = '塩竈市'
```

```sql id=shiogama_gap
SELECT ST_AsGeoJSON(geometry) AS geojson, 1 AS z_val FROM e_stat.boundary.stg_census_boundary WHERE hcode = 8101 AND LENGTH(key_code) = 2 AND city_name = '塩竈市'
```

```sql id=gap_area_dist
SELECT PREF_NAME || ' ' || COALESCE(CITY_NAME, '(不明)') AS municipality, ROUND(AREA) AS area_m2, 0 AS y_val FROM e_stat.boundary.raw_census_boundary WHERE HCODE = 8101 AND LENGTH(KEY_CODE) = 2 ORDER BY AREA DESC
```
