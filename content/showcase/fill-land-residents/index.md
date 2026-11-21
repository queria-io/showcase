---
title: 谷や斜面を埋めて造った宅地に住む人は推計391万人。住民の2割を超える市町村が17ある
description: 大規模盛土造成地と500m四方の将来推計人口を重ねました。横浜市は住民の16.5%が盛土の上に住み、住民の2割を超える市町村は全国に17あります。
publishedAt: 2026-10-22
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 防災
  - 宅地
  - 盛土
  - 将来推計人口
datasets:
  - queria/nlftp
  - queria/soumu
sources:
  - title: 国土数値情報 大規模盛土造成地データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A54-2023.html
    publisher: 国土交通省
  - title: 国土数値情報 500mメッシュ別将来推計人口データ（R6国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh500r6.html
    publisher: 国土交通省
  - title: 大規模盛土造成地の滑動崩落対策について
    url: https://www.mlit.go.jp/toshi/toshi_tobou_fr_000004.html
    publisher: 国土交通省
agentHint: 盛土の区分（fill_type）が谷埋め型の盛土造成地だけに絞って、市区町村ごとに2025年の盛土の上の推計人口と、住民に占める割合を出して。腹付け型を含めたときと上位20の顔ぶれが変わるかも比べて
socialAnnounce: |-
  大規模盛土造成地と500m四方の将来推計人口を重ねました。

  盛土の上に住む人は推計391万人、横浜市では住民の16.5%です。宅地防災の調査の優先順位づけに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

谷や斜面を埋めて造った大規模盛土造成地の上に住む人は、2025年に全国で推計約391万人で、全人口の3.2%です。横浜市だけで約62.9万人が住み、市民の16.5%にあたります。住民の2割以上が盛土の上に住む市区町村は17あり、奈良県三郷町では37.1%です。

国土交通省は、盛土の位置を示すマップの公表に続いて、地盤調査で安定性を確認する段階では優先度の高い盛土から調査する進め方を示しています。市区町村で宅地の防災を担当する人が調査の順番を決めるときには、盛土の上にいま何人が住み、2050年までに人口がどう変わるかが判断の材料になります。

## 盛土の上に住む人は、大都市圏の県に集まっている

国土交通省の国土数値情報から、次の2つのデータを重ねて集計しました。

| テーブル                                       | 内容                                                                                                                                                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nlftp.hazard.large_fill_area`                 | [大規模盛土造成地](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A54-2023.html)。谷や沢を埋めた盛土（谷埋め型）と、傾斜地に土を盛った盛土（腹付け型）のうち、一定の規模を超える造成地のポリゴン |
| `nlftp.population.future_population_mesh_500m` | [500mメッシュ別将来推計人口](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh500r6.html)。500m四方の区画ごとの2025年・2050年の人口（`population_*`）と65歳以上の割合（`elderly_ratio_*`）     |

盛土造成地のポリゴンは全国で52,530あり、盛土の区分（`fill_type`）は次の3つです。

```sql
SELECT * FROM fill_types
```

盛土造成地のマップは盛土のある場所と規模を示すもので、地震のときに危険な場所を示すものではありません。ここで集計するのは、調査や住民への説明の対象になりうる人の数です。

人数は、500m四方の区画ごとに、区画の面積のうち盛土造成地が占める割合でその区画の人口を按分して合計しています。区画の中では人が均等に住んでいると仮定した推計なので、盛土の上に住宅が密集していて周りが山林の区画では、実際より少なくなります。2025年の人口も、2020年の国勢調査をもとにした推計値です。

全国で盛土の上に住む人は、2025年に推計約391万人で、全人口の3.2%にあたります。都道府県別では神奈川県が約92.6万人で最も多く、大阪府・愛知県・千葉県・福岡県・兵庫県・東京都が続きます。神奈川県と奈良県では、県民の1割を超える人が盛土の上に住んでいます。

```chart
{
  "layer": [
    {
      "data": {"name": "pref"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "fill_2025_k", "type": "quantitative"}
        ],
        "x": {
          "field": "pref_name",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": -60},
          "sort": null
        },
        "y": {
          "field": "fill_2025_k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "盛土造成地の上の推計人口（千人、2025年）", "grid": true}
        }
      }
    }
  ]
}
```

市区町村別では、横浜市だけで推計約62.9万人が盛土の上に住んでいます。横浜市民の16.5%にあたり、全国の盛土の上に住む人の16.1%です。

## 住民の2割以上が盛土の上に住む市町村は17ある

住民に占める割合で並べると、上位は大きな市から郊外の町や市に変わります。次の図は、住民に占める盛土の上の推計人口の割合が高い20の市区町村です。福島県の浜通りなどの市町村は、将来推計人口が複数の市町村をまとめた区画で作られているため、この比較には入っていません。

```chart caption="住民に占める、盛土造成地の上に住む人の割合（推計、2025年）"
{
  "height": 530,
  "layer": [
    {
      "data": {"name": "share_top"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "fill_2025", "type": "quantitative"},
          {"field": "fill_share_pct", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "fill_share_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "住民に占める割合（%）", "grid": true}
        },
        "y": {
          "field": "label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "share_top"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "fill_share_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "住民に占める割合（%）", "grid": true}
        },
        "y": {
          "field": "label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "text": {"field": "fill_2025"}
      }
    }
  ]
}
```

奈良県三郷町では住民の37.1%、上牧町では34.4%が盛土の上に住んでいます。人数の多い市では、東京都多摩市が27.9%（約4.1万人）、神奈川県横須賀市が27.2%（約10.0万人）です。住民の2割以上が盛土の上に住む市区町村は全国に17あり、そのうち10は奈良県・大阪府・兵庫県の市町村です。

## 堺市・春日井市・札幌市では、盛土の上の人口が市全体の約2倍の割合で減る

盛土の上に住む人が1万人以上いる77の市区町村について、2025年から2050年までの人口の増減率を、盛土の上と市区町村全体で比較します。点が斜めの線より下にあれば、盛土の上のほうが速く減ります。

```chart caption="2025年から2050年までの人口の増減率。盛土の上と市区町村全体（盛土の上の推計人口が1万人以上の77市区町村）"
{
  "layer": [
    {
      "data": {"name": "change"},
      "mark": {"type": "point", "color": "#f97316", "opacity": 0.8, "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "all_change_pct", "type": "quantitative"},
          {"field": "fill_change_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "all_change_pct",
          "type": "quantitative",
          "scale": {"domain": [-45, 10], "zero": false, "nice": false},
          "axis": {"title": "市区町村全体の増減率（%）", "grid": true}
        },
        "y": {
          "field": "fill_change_pct",
          "type": "quantitative",
          "scale": {"domain": [-45, 10], "zero": false, "nice": false},
          "axis": {"title": "盛土の上の増減率（%）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": -45, "type": "quantitative"},
        "x2": {"datum": 10, "type": "quantitative"},
        "y": {"datum": -45, "type": "quantitative"},
        "y2": {"datum": 10, "type": "quantitative"}
      }
    }
  ]
}
```

77のうち48の市区町村で、盛土の上のほうが市区町村全体より速く人が減ります。多くの市では差が数ポイントで、盛土の上が5ポイントを超えて速く減るのは11、逆に5ポイントを超えて遅いのは4です。全国でまとめても盛土の上は14.0%減、全人口は15.1%減とほぼ同じです。差が大きい10市は次のとおりです。

```sql
SELECT * FROM gap
```

大阪府堺市では盛土の上の人口が34.1%減り、市全体の17.8%減のほぼ2倍の速さです。愛知県春日井市（23.2%減と10.8%減）、札幌市（22.8%減と11.4%減）も、盛土の上が市全体の約2倍の割合で減ります。この10市はいずれも、2025年の時点で盛土の上の65歳以上の割合が市全体より高く、春日井市では37.2%と26.5%で10ポイント以上違います。77の市区町村全体でも、盛土の上のほうが65歳以上の割合が高いのは50です。千葉県成田市（5.6%増と4.9%減）や沖縄県沖縄市（6.0%増と0.5%減）のように、盛土の上で人が増える市もあります。

調査や対策の工事には住民への説明や合意が要ります。上の10市のように盛土の上で高齢化と人口減少が市全体より先に進む市では、地盤の条件で決まる優先度が同じ盛土どうしなら、そうした地区を先に進めるという考え方もできます。

## 業務での活用

- 自分の市区町村で、盛土の上に住む人の数と住民に占める割合を確認する。調査の予算を議会や住民に説明するとき、何か所あるかに加えて、何人に関わる話なのかを示せます
- 自分の市区町村で、盛土の上の人口の2050年までの増減と65歳以上の割合を、市全体と比較する。盛土の上で人口減少と高齢化が先に進む市なのか、逆に人が増える市なのかが分かり、第二次スクリーニングの進め方を考える前提になります
- 隣り合う市区町村と割合を比較する。住民の2割以上が盛土の上に住む市町村は同じ府県の中に並んでいることが多いので、近隣の自治体と調査の進め方や住民への説明の仕方を共有する相手を見つけられます

## データの出典

本記事は国土交通省の国土数値情報から、[大規模盛土造成地データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A54-2023.html)と[500mメッシュ別将来推計人口データ（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh500r6.html)を、2026年10月22日時点で集計しています。将来推計人口は総務省「令和2年国勢調査」と国立社会保障・人口問題研究所「日本の地域別将来推計人口（令和5年推計）」に基づく推計値で、盛土の調査と対策の進め方は国土交通省の[大規模盛土造成地の滑動崩落対策](https://www.mlit.go.jp/toshi/toshi_tobou_fr_000004.html)にまとめられています。

Queriaは国土数値情報を、列名と座標系を統一し、各列の説明を付けて公開しています。本記事で使った[大規模盛土造成地のテーブル](/datasets/queria/nlftp/hazard/large_fill_area)と[500mメッシュの将来推計人口のテーブル](/datasets/queria/nlftp/population/future_population_mesh_500m)を SQL で重ねて、自分の市区町村の盛土の上に住む人の数と、2050年までの増減を確認できます。

```sql id=fill_types
-- 盛土の区分ごとのポリゴンの数
SELECT fill_type AS "盛土の区分", count(*) AS "ポリゴンの数"
FROM nlftp.hazard.large_fill_area
GROUP BY fill_type
ORDER BY count(*) DESC
```

```sql id=base
-- 500mメッシュごとに、盛土造成地が占める面積の割合でメッシュの人口を按分し、市区町村ごとに合計する
-- 盛土ごとに外接矩形がかかる500mメッシュのコードを緯度経度から求め、コードで結合してから面積を測る
-- 政令指定都市は行政区を市にまとめる（浜松市の再編前の区コード 2213x も市にまとめる）
-- 複数の市区町村にまたがるメッシュは先頭の市区町村に数える
-- 市区町村コード 07999 は福島県の浜通りなどの市町村をまとめて推計した区画で、muni_code は NULL になる
WITH mesh AS (
  SELECT
    m.mesh_id,
    left(m.city_code, 2) AS pref_code,
    CASE WHEN left(m.city_code, 4) = '2213' THEN '22130' ELSE c.municipality_code END AS muni_code,
    m.geometry,
    m.population_2025 AS pop_2025,
    m.population_2050 AS pop_2050,
    m.population_2025 * m.elderly_ratio_2025 / 100 AS elderly_2025
  FROM nlftp.population.future_population_mesh_500m AS m
  LEFT JOIN soumu.code.municipality AS c ON c.area_code = split_part(m.city_code, '_', 1)
),
fill_cell AS (
  -- 500mメッシュは緯度方向に1/240度、経度方向に1/160度の格子
  SELECT
    f.prefecture_code,
    f.geometry,
    lpad(CAST(i // 160 AS VARCHAR), 2, '0') || lpad(CAST(j // 160 AS VARCHAR), 2, '0')
      || CAST((i % 160) // 20 AS VARCHAR) || CAST((j % 160) // 20 AS VARCHAR)
      || CAST((i % 20) // 2 AS VARCHAR) || CAST((j % 20) // 2 AS VARCHAR)
      || CAST(1 + (i % 2) * 2 + (j % 2) AS VARCHAR) AS mesh_id
  FROM (
    SELECT
      prefecture_code,
      geometry,
      CAST(floor(ST_YMin(geometry) * 240) AS BIGINT) AS i0,
      CAST(floor(ST_YMax(geometry) * 240) AS BIGINT) AS i1,
      CAST(floor((ST_XMin(geometry) - 100) * 160) AS BIGINT) AS j0,
      CAST(floor((ST_XMax(geometry) - 100) * 160) AS BIGINT) AS j1
    FROM nlftp.hazard.large_fill_area
  ) AS f,
  generate_series(f.i0, f.i1) AS gi(i),
  generate_series(f.j0, f.j1) AS gj(j)
),
fill AS (
  SELECT
    mesh.pref_code,
    mesh.muni_code,
    ST_Area(ST_Intersection(fc.geometry, mesh.geometry)) / ST_Area(mesh.geometry) AS share,
    mesh.pop_2025,
    mesh.pop_2050,
    mesh.elderly_2025
  FROM fill_cell AS fc
  JOIN mesh ON mesh.mesh_id = fc.mesh_id AND mesh.pref_code = fc.prefecture_code
),
on_fill AS (
  SELECT
    pref_code,
    muni_code,
    sum(share * pop_2025) AS fill_2025,
    sum(share * pop_2050) AS fill_2050,
    sum(share * elderly_2025) AS fill_elderly_2025
  FROM fill
  GROUP BY ALL
),
whole AS (
  SELECT
    pref_code,
    muni_code,
    sum(pop_2025) AS all_2025,
    sum(pop_2050) AS all_2050,
    sum(elderly_2025) AS all_elderly_2025
  FROM mesh
  GROUP BY ALL
)
SELECT
  w.pref_code,
  w.muni_code,
  coalesce(o.fill_2025, 0) AS fill_2025,
  coalesce(o.fill_2050, 0) AS fill_2050,
  coalesce(o.fill_elderly_2025, 0) AS fill_elderly_2025,
  w.all_2025,
  w.all_2050,
  w.all_elderly_2025
FROM whole AS w
LEFT JOIN on_fill AS o ON o.pref_code = w.pref_code AND o.muni_code IS NOT DISTINCT FROM w.muni_code
```

```sql id=city
-- 市区町村ごとの盛土造成地の上の推計人口と、市区町村全体との比較。盛土の上の推計人口が0の市区町村は含めない
SELECT
  c.pref_name,
  coalesce(c.municipality_name, c.designated_city_name) AS city_name,
  b.muni_code,
  s.fill_sites,
  b.fill_2025,
  b.all_2025,
  b.fill_2025 / b.all_2025 * 100 AS fill_share_pct,
  (b.fill_2050 / b.fill_2025 - 1) * 100 AS fill_change_pct,
  (b.all_2050 / b.all_2025 - 1) * 100 AS all_change_pct,
  b.fill_elderly_2025 / b.fill_2025 * 100 AS fill_elderly_pct,
  b.all_elderly_2025 / b.all_2025 * 100 AS all_elderly_pct
FROM base AS b
JOIN soumu.code.municipality AS c ON c.area_code = b.muni_code
LEFT JOIN (
  SELECT municipality_code, count(*) AS fill_sites
  FROM nlftp.hazard.large_fill_area
  GROUP BY municipality_code
) AS s ON s.municipality_code = b.muni_code
WHERE b.fill_2025 > 0
```

```sql id=national
-- 全国の合計と、住民に占める割合で数えた市区町村の数（プロットはしない）
SELECT
  (SELECT count(*) FROM nlftp.hazard.large_fill_area) AS fill_rows,
  sum(fill_2025) AS fill_2025,
  sum(fill_2050) AS fill_2050,
  sum(all_2025) AS all_2025,
  sum(fill_2025) / sum(all_2025) * 100 AS fill_share_pct,
  (sum(fill_2050) / sum(fill_2025) - 1) * 100 AS fill_change_pct,
  (sum(all_2050) / sum(all_2025) - 1) * 100 AS all_change_pct,
  (SELECT count(*) FROM city) AS cities,
  (SELECT count(*) FROM city WHERE fill_share_pct >= 10) AS cities_10pct,
  (SELECT count(*) FROM city WHERE fill_share_pct >= 20) AS cities_20pct,
  (SELECT fill_2025 FROM city WHERE city_name = '横浜市') / sum(fill_2025) * 100 AS yokohama_share_of_total
FROM base
```

```sql id=pref
-- 都道府県ごとの盛土造成地の上の推計人口（2025年、千人）
SELECT p.pref_name, round(sum(b.fill_2025) / 1000, 1) AS fill_2025_k, round(sum(b.fill_2025) / sum(b.all_2025) * 100, 1) AS fill_share_pct
FROM base AS b
JOIN soumu.code.municipality AS p ON p.area_code = b.pref_code || '000'
GROUP BY p.pref_name
ORDER BY fill_2025_k DESC, p.pref_name
```

```sql id=share_top
-- 住民に占める盛土造成地の上の推計人口の割合が高い20市区町村
WITH ranked AS (
  SELECT *, row_number() OVER (ORDER BY fill_share_pct DESC, muni_code) AS rn
  FROM city
)
SELECT
  pref_name || ' ' || city_name AS label,
  round(fill_share_pct, 1) AS fill_share_pct,
  round(fill_2025) AS fill_2025,
  fill_sites
FROM ranked
WHERE rn <= 20
ORDER BY rn
```

```sql id=change
-- 盛土造成地の上の推計人口が1万人以上の市区町村。2025年から2050年の増減率を、盛土の上と市区町村全体で比べる
SELECT
  pref_name || ' ' || city_name AS label,
  round(all_change_pct, 1) AS all_change_pct,
  round(fill_change_pct, 1) AS fill_change_pct,
  round(fill_2025) AS fill_2025
FROM city
WHERE fill_2025 >= 10000
ORDER BY muni_code
```

```sql id=change_sum
-- 上の散布図の市区町村を、盛土の上のほうが速く減るかどうかで数える（プロットはしない）
SELECT
  count(*) AS cities,
  count(*) FILTER (WHERE fill_change_pct < all_change_pct) AS fill_faster,
  count(*) FILTER (WHERE fill_change_pct < all_change_pct - 5) AS fill_faster_5pt,
  count(*) FILTER (WHERE fill_change_pct > all_change_pct + 5) AS fill_slower_5pt,
  count(*) FILTER (WHERE fill_elderly_pct > all_elderly_pct) AS fill_older
FROM city
WHERE fill_2025 >= 10000
```

```sql id=gap
-- 盛土の上の推計人口が1万人以上の市区町村のうち、盛土の上の減り方が市区町村全体より大きい順に10
WITH ranked AS (
  SELECT *, row_number() OVER (ORDER BY fill_change_pct - all_change_pct, muni_code) AS rn
  FROM city
  WHERE fill_2025 >= 10000
)
SELECT
  pref_name || ' ' || city_name AS "市区町村",
  round(fill_2025) AS "盛土の上の人口（2025年）",
  round(fill_change_pct, 1) AS "盛土の上の増減率（%）",
  round(all_change_pct, 1) AS "市区町村全体の増減率（%）",
  round(fill_elderly_pct, 1) AS "盛土の上の65歳以上（%）",
  round(all_elderly_pct, 1) AS "市区町村全体の65歳以上（%）"
FROM ranked
WHERE rn <= 10
ORDER BY rn
```
