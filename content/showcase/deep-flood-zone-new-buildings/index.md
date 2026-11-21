---
title: 2010年代に岐阜市で建った建物の65%は、洪水で3m以上浸かると想定される場所にあります
description: 3D都市モデルPLATEAUの建物の建築年と洪水の浸水深を重ねました。岐阜市では2010年代に建った建物の65.3%が3m以上浸かる想定の場所にあり、1950〜2000年代に建った建物の50.5%を上回ります。
publishedAt: 2026-11-15
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 防災
  - 洪水
  - 都市計画
  - PLATEAU
datasets:
  - queria/plateau
sources:
  - title: 3D都市モデル PLATEAU オープンデータ
    url: https://www.mlit.go.jp/plateau/open-data/
    publisher: 国土交通省
  - title: 洪水浸水想定区域図・洪水ハザードマップ
    url: https://www.mlit.go.jp/river/bousai/main/saigai/tisiki/syozaiti/index.html
    publisher: 国土交通省
agentHint: 埼玉県の市町だけに絞って、洪水で3m以上浸かると想定される場所に建つ建物の割合を建った年代ごとに出して。1950〜2000年代と2010年代でどの市町が上がったかも比べて
socialAnnounce: |-
  PLATEAUの建物の建築年と浸水深を重ねました。

  岐阜市で2010年代に建った建物の65.3%は3m以上浸かる想定の場所にあります。1950〜2000年代の建物では50.5%です。防災指針の検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

岐阜市で2010年代に建った建物の65.3%は、洪水で3m以上浸かると想定される場所にあります。1950〜2000年代に建った建物では50.5%でした。建築年の分かる97市町村で建物の建築年と浸水深を1棟ずつ重ねると、3m以上浸かる場所に建つ割合は、2010年代に建った建物でも1950〜2000年代に建った建物より下がっていませんでした（11.1%と11.7%）。岐阜市と岡山市では上がっています。

立地適正化計画の防災指針では、浸水が深い場所にどれだけの建物と人がいるかを集計します。その建物が古い市街地に残る建物なのか、いまも新しく建っている建物なのかは、建築年と浸水深を重ねると判定できます。

## 岐阜市では、2010年代に建った建物の65.3%が3m以上浸かる場所にある

この記事では、国土交通省の[3D都市モデル PLATEAU](https://www.mlit.go.jp/plateau/open-data/)の建物データを使います。

| テーブル                     | 内容                                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `plateau.bldg.building`      | 建物1棟が1行。用途・高さ・階数のほか、一部の市区町村では建築年（`year_of_construction`）を持つ                   |
| `plateau.bldg.building_risk` | 建物1棟と浸水・土砂災害の想定1つが1行。洪水は河川と想定の規模ごとに浸水深の区分（`rank`）と深さ（`depth`）を持つ |
| `plateau.bldg.source`        | 取り込んだ市区町村と、PLATEAU のデータの年度                                                                     |

浸水深は、[洪水浸水想定区域](https://www.mlit.go.jp/river/bousai/main/saigai/tisiki/syozaiti/index.html)のうち、想定し得る最大規模の降雨で川があふれた場合（`scale` が L2）の値です。1棟に複数の川の想定が付くときは、最も深いものを使います。

建築年が分かり、洪水の想定が付いていて、属性のもとになった都市計画基礎調査が2021年以降の97市町村について、1950年から2019年までに建った約323万棟を集計しました。建築年は今も残っている建物にしか無いので、古い年代の割合は、その年代に建って今も残る建物のうちの割合です。

次の図は、建った年代ごとに、3m以上浸かると想定される場所に建つ建物の割合を示しています。

```chart caption="洪水で3m以上浸かると想定される場所に建つ建物の割合（建った年代別）"
{
  "data": {"name": "buildings"},
  "height": 320,
  "transform": [
    {"calculate": "datum.city === '岐阜県 岐阜市' ? '岐阜市' : datum.city === '岡山県 岡山市' ? '岡山市' : 'ほかの95市町村'", "as": "series"},
    {"calculate": "datum.depth_class === '3m以上' ? datum.buildings : 0", "as": "deep"},
    {"aggregate": [{"op": "sum", "field": "deep", "as": "deep"}, {"op": "sum", "field": "buildings", "as": "total"}], "groupby": ["series", "decade"]},
    {"calculate": "datum.deep / datum.total * 100", "as": "pct"},
    {"calculate": "datum.decade + '年代'", "as": "label"}
  ],
  "mark": {"type": "line", "point": true},
  "encoding": {
    "x": {"field": "label", "type": "ordinal", "title": "建った年代"},
    "y": {"field": "pct", "type": "quantitative", "title": "3m以上浸かる想定の場所に建つ割合（%）"},
    "color": {"field": "series", "type": "nominal", "title": null, "sort": ["岐阜市", "岡山市", "ほかの95市町村"]},
    "tooltip": [
      {"field": "series", "title": "市町村"},
      {"field": "label", "title": "建った年代"},
      {"field": "pct", "title": "割合（%）", "format": ".1f"},
      {"field": "deep", "title": "3m以上の場所の棟数", "format": ","},
      {"field": "total", "title": "棟数", "format": ","}
    ]
  }
}
```

岐阜市では、1950〜2000年代に建った建物の50.5%が3m以上浸かる想定の場所にあります。2010年代に建った建物では65.3%で、18,830棟のうち12,305棟です。2000年代の56.8%からも上がっています。岡山市も、1950〜2000年代の28.7%に対して2010年代は39.2%です。

ほかの95市町村をまとめると、割合は1970年代から2010年代まで7.0〜7.4%の間にあり、下がっていません。97市町村の合計では、1950〜2000年代に建った建物の11.1%に対して、2010年代は11.7%です。1950〜60年代は12.7%ですが、この年代に建って取り壊された建物は数に入らないので、当時建った建物全体の割合とは比較できません。1980〜2000年代の10.7〜10.8%から2010年代に上がった分は、岐阜市と岡山市によるものです。

## 32市町のうち21で、2010年代に建った建物のほうが深い場所にある

3m以上浸かる想定の場所に、建築年の分かる建物が1,000棟以上ある32市町について、1950〜2000年代に建った建物と2010年代に建った建物で、3m以上の場所に建つ割合を比較しました。灰色の点が1950〜2000年代、色の付いた点が2010年代で、色は2010年代のほうが高いか低いかを表します。

```chart caption="3m以上浸かる想定の場所に建つ建物の割合。1950〜2000年代に建った建物と2010年代に建った建物（3m以上の場所に建築年の分かる建物が1,000棟以上ある32市町）"
{
  "data": {"name": "buildings"},
  "height": 640,
  "transform": [
    {"calculate": "datum.decade >= 2010 ? 'new' : 'old'", "as": "period"},
    {"calculate": "datum.depth_class === '3m以上' ? datum.buildings : 0", "as": "deep"},
    {"aggregate": [{"op": "sum", "field": "deep", "as": "deep"}, {"op": "sum", "field": "buildings", "as": "total"}], "groupby": ["city", "period"]},
    {"joinaggregate": [{"op": "sum", "field": "deep", "as": "deep_all"}], "groupby": ["city"]},
    {"filter": "datum.deep_all >= 1000"},
    {"calculate": "datum.deep / datum.total * 100", "as": "pct"},
    {"pivot": "period", "value": "pct", "groupby": ["city"]},
    {"calculate": "datum.new >= datum.old ? '2010年代のほうが高い' : '2010年代のほうが低い'", "as": "dir"}
  ],
  "encoding": {
    "y": {"field": "city", "type": "nominal", "sort": {"field": "new", "order": "descending"}, "title": null}
  },
  "layer": [
    {
      "mark": {"type": "rule", "strokeWidth": 3},
      "encoding": {
        "x": {"field": "old", "type": "quantitative", "title": "3m以上浸かる想定の場所に建つ割合（%）"},
        "x2": {"field": "new"},
        "color": {"field": "dir", "type": "nominal", "title": null, "scale": {"domain": ["2010年代のほうが高い", "2010年代のほうが低い"], "range": ["#2166ac", "#b2182b"]}}
      }
    },
    {
      "mark": {"type": "point", "filled": true, "size": 60, "color": "#94a3b8"},
      "encoding": {
        "x": {"field": "old", "type": "quantitative"},
        "tooltip": [{"field": "city", "title": "市町"}, {"field": "old", "title": "1950〜2000年代（%）", "format": ".1f"}, {"field": "new", "title": "2010年代（%）", "format": ".1f"}]
      }
    },
    {
      "mark": {"type": "point", "filled": true, "size": 80},
      "encoding": {
        "x": {"field": "new", "type": "quantitative"},
        "color": {"field": "dir", "type": "nominal"},
        "tooltip": [{"field": "city", "title": "市町"}, {"field": "old", "title": "1950〜2000年代（%）", "format": ".1f"}, {"field": "new", "title": "2010年代（%）", "format": ".1f"}]
      }
    }
  ]
}
```

32市町のうち21で、2010年代に建った建物のほうが3m以上の場所に建つ割合が高くなっています。岐阜市・岡山市のほか、大阪府守口市は50.6%から65.1%、広島県竹原市は28.1%から44.3%、埼玉県吉見町は44.7%から64.1%、高知県いの町は65.7%から83.0%です。下がったのは11市町で、埼玉県戸田市は67.2%から58.3%、富士見市は27.9%から19.3%になりました。

## 自分の市町村で集計するには

- 防災指針で居住誘導区域から浸水の深い区域を外すかを検討するとき、その区域にある建物を建った年代で分けると、古い市街地の建物が中心なのか、新しい住宅地が広がっているのかが分かります。新しい住宅地が広がっている区域は、建て替えの時期を待って移転を促すことが難しいので、避難の計画を先に詰める対象になります
- 岐阜市・岡山市のように2010年代の建物の割合が上がっている市では、`building` の代表点（`lng`・`lat`）で2010年代に建った建物を地図に置き、浸水深の区分で色を分けると、深い場所で建物が増えた地区を特定できます
- 2010年代に深い場所に建った建物を `building` の用途と階数で分けると、深く浸かったときに上の階へ逃げられない平屋の住宅のように、避難計画で対策が必要な新しい建物を集計できます

## データの出典

本記事は国土交通省の [3D都市モデル PLATEAU](https://www.mlit.go.jp/plateau/open-data/) の建物データ（建築年は各市町村の都市計画基礎調査、浸水深は[洪水浸水想定区域](https://www.mlit.go.jp/river/bousai/main/saigai/tisiki/syozaiti/index.html)の想定最大規模）を、2026-11-15 時点で集計しています。

Queriaは、PLATEAU の建物を1棟1行のテーブルにし、浸水・土砂災害の想定を建物ごとに結合して公開しています。本記事で使った[建物のテーブル](/datasets/queria/plateau/bldg/building)と[建物ごとの浸水深のテーブル](/datasets/queria/plateau/bldg/building_risk)から、自分の市町村の建物を年代や用途で分けて集計できます。

```sql id=buildings
-- 建った年代・浸水深の区分ごとの棟数（市町村別）
-- 対象: 建築年が分かり、洪水（想定最大規模）の想定が付き、都市計画基礎調査が2021年以降の市町村
WITH risk AS (
  -- 建物ごとの最も深い浸水深（想定最大規模の洪水、全河川）
  SELECT gml_id, max(TRY_CAST(rank_code AS INTEGER)) >= 3 OR max(depth) >= 3 AS deep
  FROM plateau.bldg.building_risk
  WHERE hazard = '洪水' AND scale LIKE 'L2%'
  GROUP BY gml_id
),
flood_cities AS (
  SELECT DISTINCT city_code FROM plateau.bldg.building_risk
  WHERE hazard = '洪水' AND scale LIKE 'L2%'
)
SELECT
  s.prefecture_name || ' ' || s.city_name AS city,
  b.year_of_construction // 10 * 10 AS decade,
  CASE WHEN r.deep THEN '3m以上' WHEN r.gml_id IS NOT NULL THEN '3m未満' ELSE '想定なし' END AS depth_class,
  count(*) AS buildings
FROM plateau.bldg.building b
JOIN plateau.bldg.source s ON s.city_code = b.source_city_code
LEFT JOIN risk r USING (gml_id)
WHERE b.year_of_construction BETWEEN 1950 AND 2019
  AND b.survey_year >= 2021
  AND b.city_code IN (SELECT city_code FROM flood_cities)
GROUP BY ALL
ORDER BY city, decade, depth_class
```
