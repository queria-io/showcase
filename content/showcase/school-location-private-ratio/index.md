---
title: 高校が1校も無い自治体は、全国1,741のうち444（25.5%）
description: 国土数値情報の学校の位置データと市区町村境界を空間結合しました。高等学校が1校も無い自治体は1,741のうち444で、長野県では県内の49.4%の自治体に高校がありません。最寄りの高校までの直線距離の中央値は8.7kmです。
publishedAt: 2026-06-28
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 教育
  - 学校
  - 地域格差
datasets:
  - queria/nlftp
sources:
  - title: 国土数値情報 学校データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P29-v2_0.html
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: nlftp.boundary.municipality と nlftp.facility.school を ST_Contains で結合して、高等学校が1校も無い自治体を都道府県別に一覧して。そのうえで同じ自治体に中学校が何校あるかも並べて、中学校はあるのに高校が無い自治体を抽出して
socialAnnounce: |-
  学校の位置（点データ）と市区町村境界を空間結合して、高等学校が1校も無い自治体を数えました。

  全国1,741自治体のうち444。小学校が無いのは22、中学校が無いのは33なので、空白は高校から始まります。

  都道府県別の集計表からは出せない切り口です。Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

高等学校が1校も無い自治体は、全国1,741のうち444（25.5%）です。小学校が無い自治体は22、中学校が無い自治体は33なので、域内に学校が無い自治体は高校で大きく増えます。長野県では県内の自治体の49.4%に高校が無く、兵庫県と広島県では0%です。高校が無い444自治体から最寄りの高校までの直線距離は、中央値で8.7kmです。

学校の所在地は、教育サービスの商圏設計や、自治体の移住・子育て施策の検討に使われます。公表されている学校統計の多くは都道府県別の学校数で、市区町村ごとに高校があるかどうかは載っていません。この記事では、[国土数値情報の学校データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P29-v2_0.html)の学校の所在地点と、[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)の市区町村ポリゴンを空間結合し、域内に高等学校が1校も無い自治体を集計します。

## 学校データには、小学校19,330校、高等学校4,996校が収録されている

使うのは国土数値情報の学校データ（`nlftp.facility.school`）です。全国の学校が緯度経度付きの点データとして収録されており、学校ごとに学校種別（`school_class`）、設置者の区分（`administrator`、国・都道府県・市区町村・民間など）、所在地（`address`）、所在地点（`geometry`）などの列があります。この記事では、設置者が「民間」の学校を私立として扱います。この区分は設置者を表すもので、学校教育法上の「私立学校」の定義と一致するとは限りません。

主な学校種別ごとの施設数と、そのうち私立（設置者が民間）の数です。

```sql
SELECT school_class AS 種別, COUNT(*) AS 施設数, COUNT(*) FILTER (WHERE administrator = '民間') AS うち私立 FROM nlftp.facility.school WHERE school_class IN ('小学校', '中学校', '高等学校', '幼稚園', '大学', '専修学校') GROUP BY school_class ORDER BY 施設数 DESC
```

小学校が19,330校、中学校が10,082校、高等学校が4,996校、大学が1,239校です。

学校データの `admin_code`（所在する行政区域コード）は政令指定都市を市単位で持っており、たとえば札幌市の学校はすべて `01100` です。行政区域データは中央区 `01101`、北区 `01102` のように行政区ごとに分かれています。コードで結合すると政令市の学校がすべて除かれるので、`ST_Contains` で学校の点がどの市区町村ポリゴンの中にあるかを判定しています。

## 高校が無い自治体は444で、小学校が無い22、中学校が無い33より大幅に多い

市区町村ポリゴンと学校の点を空間結合し、学校種別ごとに域内に1校も無い自治体の数を集計しました。集計単位は全国1,741自治体です。政令指定都市の行政区は市にまとめ、境界データに含まれる北方領土の6村は除いています。集計するのは小学校・中学校・高等学校・大学の4種別で、義務教育学校や中等教育学校のように複数の段階にまたがる学校、特別支援学校、幼稚園・認定こども園、専修学校・各種学校、短期大学・高等専門学校は含めません。

```chart
{
  "height": 240,
  "layer": [
    {
      "data": {"name": "blank_by_level"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "blank", "type": "quantitative"},
          {"field": "level", "type": "nominal"}
        ],
        "x": {
          "field": "blank",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "その学校が1校も無い自治体の数", "grid": true}
        },
        "y": {"field": "level", "type": "nominal", "axis": {"title": "学校種別"}, "sort": null}
      }
    }
  ]
}
```

小学校が1校も無い自治体は22、中学校が無い自治体は33です。義務教育の学校は、ほぼすべての自治体にあります。この22と33は小中一貫の義務教育学校を含めていない数で、義務教育学校を含めると、小学校にあたる学校が無い自治体は2、中学校にあたる学校が無い自治体は13です。

高等学校が無い自治体は444で、全1,741自治体の25.5%です。4つに1つの自治体には高校がありません。大学が無い自治体は1,346で、77.3%です。

高校が無い444自治体のうち418は、域内に中学校があります。これらの自治体では、中学校までは域内の学校に通い、高校から自治体の外の学校に通うことになります。

この記事で集計しているのは学校の所在地点で、生徒数や定員ではありません。高校が無い自治体の生徒の多くは、隣接する自治体の高校に通っています。

## 高校が無い自治体の割合は、長野県の49.4%が最も高い

都道府県ごとに、県内の自治体のうち高校が無い自治体の割合を計算し、地図にしました。色が濃い（赤い）ほど割合が高い県です。

```map
type: map
layers:
  - from: blank_map
    geojson: geojson
    color: pct
    label: pref_name
    name: "高校が無い自治体の割合（%）"
lng: 137
lat: 36.5
zoom: 4
```

割合が最も高いのは長野県で、77自治体のうち38、49.4%に高校がありません。次いで鳥取県47.4%（19自治体中9）、高知県47.1%（34自治体中16）、熊本県46.7%（45自治体中21）、宮崎県46.2%（26自治体中12）です。県内の自治体のほぼ半分に高校が無い県が5つあります。

兵庫県と広島県は0%で、県内のすべての自治体に高校があります。長崎県4.8%、愛媛県5.0%、静岡県5.7%も低い値です。都道府県別の高校数からは、隣り合う県で高校のある自治体の割合がこれだけ違うことは分かりません。

数では北海道の52自治体が最も多く、179自治体の29.1%です。長野県の38、福島県の22、熊本県の21が続きます。北海道は自治体の数が多いので割合は3割弱ですが、高校が無い自治体の数は全国で最も多くなっています。

## 最寄りの高校までの直線距離は、中央値8.7km、最も遠い北大東村で308.6km

高校が無い自治体のポリゴンの重心から、全国の高等学校のうち最も近い1校までの距離を測り、遠い順に20自治体を並べました。測っているのは重心から学校までの直線距離（大圏距離）で、道路距離や通学時間とは異なります。重心が市街地や人口の中心と一致するとも限りません。

```chart
{
  "height": 560,
  "layer": [
    {
      "data": {"name": "blank_dist"},
      "mark": {"type": "bar", "color": "#0891b2"},
      "encoding": {
        "tooltip": [{"field": "km", "type": "quantitative"}, {"field": "name", "type": "nominal"}],
        "x": {
          "field": "km",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "最寄りの高等学校までの距離（km）", "grid": true}
        },
        "y": {"field": "name", "type": "nominal", "axis": {"title": "自治体"}, "sort": null}
      }
    }
  ]
}
```

444自治体の中央値は8.7kmで、多くの自治体では隣接する市町村の高校が通学できる距離にあります。10km以上離れている自治体が185、20km以上が38あり、遠い側に長く分布しています。

最も遠いのは沖縄県北大東村の308.6km、次いで南大東村の304.0km、与那国町の119.6kmで、上位は離島です。鹿児島県十島村95.9km、東京都青ヶ島村72.4kmも離島です。これらは海上を含めた直線距離で、実際には船や飛行機での移動や、島外の高校への進学と下宿が必要になります。

離島以外でも、北海道滝上町の34.0km、福島県檜枝岐村の32.0km、北海道新得町の25.7km、積丹町の25.6kmのように、陸続きで20kmから30km台の距離がある自治体があります。最寄りの高校までの距離は、学校の点データの座標を使うと測れます。

## 私立の割合は、小学校1.3%、高等学校28.8%、大学70.9%

学校種別ごとに、施設数に占める私立（民間）の割合を出しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "level_mix"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "private_pct", "type": "quantitative"},
          {"field": "school_class", "type": "nominal"}
        ],
        "x": {
          "field": "private_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "私立（民間）の割合（%）", "grid": true}
        },
        "y": {"field": "school_class", "type": "nominal", "axis": {"title": "学校種別"}, "sort": null}
      }
    }
  ]
}
```

私立の割合は、小学校が1.3%、中学校が7.7%で、義務教育の学校のほとんどは公立です。高等学校では28.8%で、幼稚園は66.5%、大学は70.9%、専修学校は91.9%と、教育段階が上がるほど私立の割合が高くなります。義務教育の学校は市区町村が区域全体に配置する責任を負い、幼児教育と高等教育以降は私立の割合が大きくなっています。

高校は、全域に学校を配置する義務教育から、設置者が立地を選ぶ段階に移る最初の学校段階で、そのことが444自治体に高校が無いことの背景にあると考えられます。

## 高校の私立の割合と、高校が無い自治体の割合の相関は-0.219

都道府県ごとに、高校が無い自治体の割合と、高校に占める私立の割合をとって散布図にしました。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "pref_scatter"},
      "mark": {"type": "point", "color": "#2563eb", "opacity": 0.75, "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "blank_pct", "type": "quantitative"},
          {"field": "private_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "blank_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高校が無い自治体の割合（%）", "grid": true}
        },
        "y": {
          "field": "private_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高校に占める私立の割合（%）", "grid": true}
        }
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

2つの指標の相関係数は-0.219で、弱い負の関係です。東京都は高校が無い自治体の割合が9.7%・私立の割合が55.6%、大阪府は11.6%・40.3%で左上にあり、長野県は49.4%・23.4%、徳島県は33.3%・7.7%で右下にあります。この4都府県では私立が多い都市部ほど高校が無い自治体が少なくなっていますが、全体ではこの関係は弱くなります。

福岡県は高校が無い自治体の割合が31.7%で私立の割合が36.7%、熊本県は46.7%で31.6%です。自治体の3割から半分に高校が無いのに、私立の割合は全国でも高い県です。兵庫県は高校が無い自治体の割合が0%で私立の割合が26.7%、広島県は0%で29.9%で、私立の割合が平均的な水準でも、すべての自治体に高校があります。

都道府県単位の私立の割合からは、その県の中で高校がどの自治体にあるかは分かりません。

## 大学が無い自治体は1,346で、大学の17.5%は東京都にある

都道府県別の大学数を、上位10・中間27・下位10の3グループに色分けして並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "univ_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "cnt", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大学数", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "univ_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "cnt", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大学数", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間27",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "univ_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "cnt", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "cnt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大学数", "grid": true}
        },
        "y": {"field": "pref", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間27", "下位10"], "range": ["#2563eb", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

大学数は東京都が217校で最も多く、全国1,239校の17.5%です。大阪府の89校、愛知県の76校が続き、上位3都府県で約31%を占めます。下位は鳥取県の4校、島根県の5校、佐賀県と大分県の6校です。高校は県内のどの自治体にあるかで差があり、大学はどの都府県にあるかの段階で偏っています。

高校生を対象にしたサービスでは、市区町村単位で生徒が通う高校の所在地を把握することに意味があります。大学生を対象にするなら、市場の大きさは都府県の段階でほぼ決まります。学校の段階によって、確認する地域の単位が変わります。

## まとめ

学校の位置データと市区町村境界を空間結合し、学校が無い自治体を集計しました。

- 高等学校が1校も無い自治体は全国1,741のうち444（25.5%）です。小学校が無いのは22、中学校が無いのは33で、学校が無い自治体は高校で大幅に増えます
- 高校が無い自治体の割合は長野県49.4%、鳥取県47.4%、高知県47.1%が高く、兵庫県・広島県は0%です
- 高校が無い自治体から最寄りの高校までの直線距離は中央値8.7kmです。10km以上が185自治体、20km以上が38自治体あり、最も遠いのは沖縄県北大東村の308.6kmです
- 都道府県の高校の私立の割合と、高校が無い自治体の割合の相関は-0.219で、県単位の指標から市区町村ごとの高校の有無は推定できません

## データの出典

本記事は国土交通省の[国土数値情報 学校データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P29-v2_0.html)（`nlftp.facility.school`）と[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)の市区町村境界（`nlftp.boundary.municipality`）・都道府県境界（`nlftp.boundary.prefecture`）を、2026年9月26日時点で集計しています。学校の所在地点は1時点の値です。

Queriaは、国土数値情報のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[学校データ](/datasets/queria/nlftp/facility/school)と[市区町村境界データ](/datasets/queria/nlftp/boundary/municipality)を空間結合すると、関心のある地域で、どの自治体にどの種別の学校があるかを確認できます。

```sql id=blank_by_level
WITH m AS (SELECT lg_code, prefecture_code, prefecture_name, city_name, geometry, CASE WHEN ward_name IS NULL THEN lg_code ELSE prefecture_code || city_name END AS uk FROM nlftp.boundary.municipality WHERE lg_code NOT BETWEEN '01695' AND '01700'), j AS (SELECT m.uk, COUNT(*) FILTER (WHERE s.school_class = '小学校') AS es, COUNT(*) FILTER (WHERE s.school_class = '中学校') AS jhs, COUNT(*) FILTER (WHERE s.school_class = '高等学校') AS hs, COUNT(*) FILTER (WHERE s.school_class = '大学') AS univ, COUNT(*) FILTER (WHERE s.school_class = '義務教育学校') AS cs FROM m LEFT JOIN nlftp.facility.school s ON s.school_class IN ('小学校', '中学校', '高等学校', '大学', '義務教育学校') AND ST_Contains(m.geometry, s.geometry) GROUP BY 1), x AS (SELECT COUNT(*) FILTER (WHERE hs = 0 AND jhs > 0) AS hs0_jhs1, COUNT(*) FILTER (WHERE es = 0 AND cs = 0) AS es0_cs0, COUNT(*) FILTER (WHERE jhs = 0 AND cs = 0) AS jhs0_cs0 FROM j) SELECT * FROM (SELECT 1 AS ord, '小学校' AS level, COUNT(*) FILTER (WHERE es = 0) AS blank, COUNT(*) AS units, (SELECT hs0_jhs1 FROM x) AS hs0_jhs1, (SELECT es0_cs0 FROM x) AS es0_cs0, (SELECT jhs0_cs0 FROM x) AS jhs0_cs0 FROM j UNION ALL SELECT 2, '中学校', COUNT(*) FILTER (WHERE jhs = 0), COUNT(*), (SELECT hs0_jhs1 FROM x), (SELECT es0_cs0 FROM x), (SELECT jhs0_cs0 FROM x) FROM j UNION ALL SELECT 3, '高等学校', COUNT(*) FILTER (WHERE hs = 0), COUNT(*), (SELECT hs0_jhs1 FROM x), (SELECT es0_cs0 FROM x), (SELECT jhs0_cs0 FROM x) FROM j UNION ALL SELECT 4, '大学', COUNT(*) FILTER (WHERE univ = 0), COUNT(*), (SELECT hs0_jhs1 FROM x), (SELECT es0_cs0 FROM x), (SELECT jhs0_cs0 FROM x) FROM j) ORDER BY ord
```

```sql id=blank_map
WITH m AS (SELECT lg_code, prefecture_code, geometry, CASE WHEN ward_name IS NULL THEN lg_code ELSE prefecture_code || city_name END AS uk FROM nlftp.boundary.municipality WHERE lg_code NOT BETWEEN '01695' AND '01700'), j AS (SELECT m.uk, any_value(m.prefecture_code) AS pc, COUNT(*) FILTER (WHERE s.school_class = '高等学校') AS hs FROM m LEFT JOIN nlftp.facility.school s ON s.school_class = '高等学校' AND ST_Contains(m.geometry, s.geometry) GROUP BY 1), r AS (SELECT pc, COUNT(*) FILTER (WHERE hs = 0) AS blank, COUNT(*) AS units, ROUND(COUNT(*) FILTER (WHERE hs = 0) * 100.0 / COUNT(*), 1) AS pct FROM j GROUP BY 1) SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, r.pct, r.blank, r.units FROM r JOIN nlftp.boundary.prefecture p ON r.pc = p.prefecture_code
```

```sql id=blank_dist
WITH m AS (SELECT lg_code, prefecture_code, prefecture_name, city_name, geometry, CASE WHEN ward_name IS NULL THEN lg_code ELSE prefecture_code || city_name END AS uk FROM nlftp.boundary.municipality WHERE lg_code NOT BETWEEN '01695' AND '01700'), c AS (SELECT m.uk, COUNT(*) FILTER (WHERE s.school_class = '高等学校') AS hs FROM m LEFT JOIN nlftp.facility.school s ON s.school_class = '高等学校' AND ST_Contains(m.geometry, s.geometry) GROUP BY 1), b AS (SELECT m.uk, any_value(m.prefecture_name) AS pref, any_value(m.city_name) AS city, ST_Centroid(ST_Union_Agg(m.geometry)) AS ctr FROM m JOIN c ON c.uk = m.uk WHERE c.hs = 0 GROUP BY 1), d AS (SELECT b.uk, b.pref, b.city, MIN(ST_Distance_Sphere(ST_FlipCoordinates(b.ctr), ST_FlipCoordinates(s.geometry))) / 1000 AS km FROM b, nlftp.facility.school s WHERE s.school_class = '高等学校' GROUP BY 1, 2, 3), a AS (SELECT MEDIAN(km) AS med, COUNT(*) FILTER (WHERE km >= 10) AS n10, COUNT(*) FILTER (WHERE km >= 20) AS n20, COUNT(*) AS n FROM d) SELECT d.pref || ' ' || d.city AS name, ROUND(d.km, 1) AS km, ROUND(a.med, 1) AS median_km, a.n10, a.n20, a.n FROM d, a ORDER BY d.km DESC LIMIT 20
```

```sql id=level_mix
SELECT school_class, ROUND(COUNT(*) FILTER (WHERE administrator = '民間') * 100.0 / COUNT(*), 1) AS private_pct, COUNT(*) AS total FROM nlftp.facility.school WHERE school_class IN ('小学校', '中学校', '高等学校', '幼稚園', '大学', '専修学校') GROUP BY school_class ORDER BY private_pct DESC
```

```sql id=pref_scatter
WITH m AS (SELECT lg_code, prefecture_code, prefecture_name, city_name, geometry, CASE WHEN ward_name IS NULL THEN lg_code ELSE prefecture_code || city_name END AS uk FROM nlftp.boundary.municipality WHERE lg_code NOT BETWEEN '01695' AND '01700'), j AS (SELECT m.uk, any_value(m.prefecture_name) AS pref, COUNT(*) FILTER (WHERE s.school_class = '高等学校') AS hs, COUNT(*) FILTER (WHERE s.school_class = '高等学校' AND s.administrator = '民間') AS hsp FROM m LEFT JOIN nlftp.facility.school s ON s.school_class = '高等学校' AND ST_Contains(m.geometry, s.geometry) GROUP BY 1), r AS (SELECT pref, ROUND(COUNT(*) FILTER (WHERE hs = 0) * 100.0 / COUNT(*), 1) AS blank_pct, ROUND(SUM(hsp) * 100.0 / SUM(hs), 1) AS private_pct, SUM(hs) AS hs_total FROM j GROUP BY 1) SELECT r.*, ROUND((SELECT corr(blank_pct, private_pct) FROM r), 3) AS corr_all FROM r ORDER BY blank_pct DESC
```

```sql id=univ_top
WITH base AS (SELECT p.prefecture_name AS pref, s.n AS cnt FROM (SELECT substr(admin_code, 1, 2) AS pc, COUNT(*) AS n FROM nlftp.facility.school WHERE school_class = '大学' GROUP BY 1) s JOIN nlftp.boundary.prefecture p ON s.pc = p.prefecture_code), ranked AS (SELECT pref, cnt, ROW_NUMBER() OVER (ORDER BY cnt DESC, pref) AS rn FROM base) SELECT pref, cnt FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=univ_mid
WITH base AS (SELECT p.prefecture_name AS pref, s.n AS cnt FROM (SELECT substr(admin_code, 1, 2) AS pc, COUNT(*) AS n FROM nlftp.facility.school WHERE school_class = '大学' GROUP BY 1) s JOIN nlftp.boundary.prefecture p ON s.pc = p.prefecture_code), ranked AS (SELECT pref, cnt, ROW_NUMBER() OVER (ORDER BY cnt DESC, pref) AS rn FROM base) SELECT pref, cnt FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=univ_bottom
WITH base AS (SELECT p.prefecture_name AS pref, s.n AS cnt FROM (SELECT substr(admin_code, 1, 2) AS pc, COUNT(*) AS n FROM nlftp.facility.school WHERE school_class = '大学' GROUP BY 1) s JOIN nlftp.boundary.prefecture p ON s.pc = p.prefecture_code), ranked AS (SELECT pref, cnt, ROW_NUMBER() OVER (ORDER BY cnt DESC, pref) AS rn FROM base) SELECT pref, cnt FROM ranked WHERE rn > 37 ORDER BY rn
```
