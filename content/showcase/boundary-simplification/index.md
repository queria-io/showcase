---
title: 237MBの市区町村ポリゴンを3.6MBに簡素化すると、ブラウザで日本地図を描ける
description: 国土数値情報の行政区域データは、市区町村単位で頂点1,541万・WKB 237MBあり、ブラウザのDuckDB WASMではメモリ不足になります。小島除去とST_CoverageSimplifyを組み合わせると3.6MB（98.5%減）になり、隣接する境界に隙間のない地図を描けます。
publishedAt: 2026-04-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - GIS
  - 境界データ
  - DuckDB
  - データエンジニア
datasets:
  - queria/nlftp
sources:
  - title: 国土数値情報 行政区域データ（N03）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 都道府県ごとに市区町村ポリゴンの数を数えて、政令市の区を市に統合したデータと比べ、区の統合で件数が最も減る県を出して
socialAnnounce: |-
  国土数値情報の市区町村ポリゴン、頂点数1,541万・WKB 237MB。
  ブラウザのDuckDB WASMで集計するとメモリ不足に。

  小島除去＋ST_CoverageSimplifyで3.6MBに削減。
  隣接境界の一貫性を保ち、隙間のない市区町村マップを描画できます。
---

国土数値情報の行政区域データ（N03）を市区町村単位に結合すると、頂点数は1,541万、WKB で237MBになります。このままブラウザの DuckDB WASM で集計するとメモリ不足になります。頂点の間引きで95%、小島の除去と組み合わせると98.5%を削減でき、3.6MB になりました。間引きには `ST_CoverageSimplify` を使い、隣接する市区町村の境界に隙間や重なりが出ないようにしています。

ウェブアプリで日本地図を塗り分ける（コロプレス図）には、都道府県や市区町村の境界ポリゴンが必要です。国土交通省の国土数値情報が提供する[行政区域データ（N03）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)は、国土地理院の基盤地図情報をもとに作成された公的なデータで、GeoJSON・Shapefile・GML 形式で無償公開されています。QGIS などのデスクトップ GIS ではこのデータをそのまま扱えますが、Queria のように DuckDB WASM・Observable Plot・MapLibre でブラウザに描画する場合は、メモリが足りずに描画できません。Queria は行政区域データを `nlftp.boundary` スキーマで提供しており、公開の前に簡素化の処理を行いました。この記事では、ウェブ GIS やデータパイプラインに関わるエンジニアに向けて、簡素化が必要な理由と、組み合わせた手法を説明します。

## フル解像度のポリゴンはブラウザのメモリに収まらない

国土数値情報 N03 の行政区域データは、全国で約12万の個別ポリゴンでできています。離島や入り江ごとに1つのポリゴンがあり、市区町村単位に結合すると頂点数1,541万、WKB 237MB になります。

このデータをブラウザ上の DuckDB WASM で集計したところ、Out of Memory が発生しました。フル解像度のポリゴンをメモリ上に展開し、さらに `ST_AsGeoJSON` で GeoJSON 文字列（約573MB）に変換する過程で、WASM のメモリ上限に達したと考えられます。

## 頂点の間引きで95%、小島の除去と組み合わせると98.5%減る

市区町村単位に結合したフル解像度のデータ（237MB）に対して、頂点の間引きと小島の除去の効果を比較しました。表のサイズと削減率は、この記事の処理条件（小島の面積の閾値と簡素化の許容誤差）での値で、条件を変えると変わります。

| 手法           | WKB サイズ | 削減率 |
| -------------- | ---------- | ------ |
| 簡素化前       | 237 MB     | -      |
| 頂点間引きのみ | 13 MB      | 95%    |
| 小島除去のみ   | 187 MB     | 21%    |
| 両方           | 3.6 MB     | 98.5%  |

頂点の間引き（`ST_CoverageSimplify`）だけで95%を削減できます。小島の除去だけでは21%しか減りません。小島は数が多くても、1つあたりの頂点数が少ないためです。

頂点を間引いた後の13MB の大部分は、間引いても残る大量の小島のポリゴン（各3〜4頂点）です。小島の除去を組み合わせると、13MB から3.6MB に減ります。

次の地図は、頂点の間引きだけを適用したものです。本土の海岸線は滑らかになっていますが、小島や岩礁が大量の点として残っています。この比較では、間引きのみの `prefecture_thinned` と最終版の `prefecture` を同じ縮尺・同じ中心座標で並べ、差が処理の違いだけになるようにしています。

```map
type: map
layers:
  - from: thinned_pref
    geojson: geojson
    label: pref_name
lng: 128.8
lat: 32.8
zoom: 9
```

長崎県の周辺を拡大すると、五島列島の周りに小さなポリゴンが多数散らばっています。これらがサイズの大部分を占めており、地図を読むうえでは役に立っていません。

## 小島を除去してから、ST_CoverageSimplify で全市区町村をまとめて簡素化する

### ST_CoverageSimplify は隣接する境界を同じ形に簡素化する

小島を除去した後の頂点の間引きには、`ST_SimplifyPreserveTopology` ではなく `ST_CoverageSimplify` を使っています。

`ST_SimplifyPreserveTopology` は各ポリゴンを独立に簡素化します。隣接する市区町村は境界線を共有していますが、独立に簡素化すると共有する境界がそれぞれ別の形に変わり、隙間や重なりが発生します。

`ST_CoverageSimplify`（GEOS の CoverageSimplifier）は、全ポリゴンの隣接関係を考慮して、共有する境界を同じ形に簡素化するので、隙間が生じません。DuckDB 1.4.4 以降の Spatial 拡張で使用できます。

### 処理の順序

1. ST_Dump と ST_Area で、面積が極小の小島を除去する
2. ST_CoverageSimplify で、全市区町村をまとめて簡素化する（隣接する境界の一貫性を保つ）

小島の除去を先に行うのは、フル解像度の正確な面積で小島を判定するためです。簡素化した後に除去しても結果はほぼ同じですが、判定の根拠が明確なほうを採用しています。

都道府県の境界は、簡素化した市区町村の境界を dissolve して作ります。市区町村の段階で隣接する境界が一致しているので、都道府県の境界にも隙間は出ません。

同じ長崎県の周辺で、小島の除去とカバレッジ簡素化を行った後の地図です。小さな点は消え、五島列島・対馬・壱岐など主な離島だけが残っています。

```map
type: map
layers:
  - from: simplified_pref
    geojson: geojson
    label: pref_name
lng: 128.8
lat: 32.8
zoom: 9
```

## 簡素化した後も、市区町村の境界には隙間が出ない

市区町村の段階でも、`ST_CoverageSimplify` によって隣接する境界にずれがないことを確認します。次の地図は `prefecture_code = '14'` で神奈川県だけに絞っています。全国1,898の市区町村を1枚に描くと、境界のずれがあるかどうかが縮尺の中で見えなくなるためです。海岸線やカーブの細部は丸められていますが、市区町村どうしが共有する境界は同じ形に簡素化されており、隙間は発生していません。

```map
type: map
layers:
  - from: kanagawa_muni
    geojson: geojson
    label: name
lng: 139.5
lat: 35.45
zoom: 10
```

## 政令指定都市の区を市に統合したテーブルもある

`nlftp.boundary.municipality` は、政令指定都市の区（横浜市鶴見区、横浜市神奈川区など）を個別に持っています。市の単位で集計したい場合のために、区を統合した `nlftp.boundary.designated_city` も提供しています。東京23区（特別区）は独立した地方公共団体なので統合していません。

```map
type: map
layers:
  - from: kanagawa_designated
    geojson: geojson
    label: name
lng: 139.5
lat: 35.45
zoom: 10
```

前の節の神奈川県の地図（58市区町村）と比較すると、横浜市・川崎市・相模原市の区の境界が消え、市の単位（33市町村）になっています。

## まとめ

- 国土数値情報 N03 のフル解像度のポリゴンは、市区町村単位で頂点1,541万、WKB 237MB あり、ブラウザの DuckDB WASM では集計や変換の途中でメモリ不足になる
- 頂点の間引き（ST_CoverageSimplify）で95%を削減し、小島の除去で残りの13MB を3.6MB にした
- `ST_SimplifyPreserveTopology` は各ポリゴンを独立に簡素化するので、隣接する市区町村の共有境界がずれる。`ST_CoverageSimplify` を使い、共有境界を同じ形に保った
- 海岸線の細部と極小の小島は除去しているので、面積の計算や海岸線に沿った空間分析には使えない。塗り分け地図には十分な精度で、原データ（raw/stg）はフル解像度で保持している
- `nlftp.boundary.prefecture`（47都道府県）、`nlftp.boundary.municipality`（1,898市区町村、政令市の区を含む）、`nlftp.boundary.designated_city`（1,747市区町村、政令市の区を市に統合）として、すべての記事から参照できる

## データの出典

本記事は、国土交通省の国土数値情報[行政区域データ（N03）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を Queria が取り込んで簡素化した `nlftp.boundary` スキーマのテーブルを使っています。地図とサイズの数値は2026年7月11日時点のデータに基づいています。

Queria は、小島の除去とカバレッジ簡素化を済ませた[市区町村の境界データ](/datasets/queria/nlftp/boundary/municipality)を、列の意味の説明を付けて公開しています。自分で簡素化の処理を組まずに、地図の塗り分けや空間集計に使えます。

## 参考

- [K-Oxon/Japan-map-for-BI](https://github.com/K-Oxon/Japan-map-for-BI): 国土数値情報から mapshaper でポリゴンを簡素化し、Power BI / Tableau 向けの TopoJSON を公開。簡素化の手法（ポリゴン簡素化 + 小島除去 + dissolve）はこのプロジェクトを参考にした
- [smartnews-smri/japan-topography](https://github.com/smartnews-smri/japan-topography): TopoJSON の共有アーク構造で隣接境界の一貫性を保持。Queria では同じ考え方を DuckDB の `ST_CoverageSimplify` で再現した

```sql id=thinned_pref
SELECT prefecture_name AS pref_name, ST_AsGeoJSON(geometry) AS geojson, 1 AS z_val FROM nlftp.boundary.prefecture_thinned
```

```sql id=simplified_pref
SELECT prefecture_name AS pref_name, ST_AsGeoJSON(geometry) AS geojson, 1 AS z_val FROM nlftp.boundary.prefecture
```

```sql id=kanagawa_muni
SELECT city_name AS name, ST_AsGeoJSON(geometry) AS geojson, 1 AS z_val FROM nlftp.boundary.municipality WHERE prefecture_code = '14'
```

```sql id=kanagawa_designated
SELECT city_name AS name, ST_AsGeoJSON(geometry) AS geojson, 1 AS z_val FROM nlftp.boundary.designated_city WHERE prefecture_code = '14'
```
