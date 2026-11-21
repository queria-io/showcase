---
title: いちばん冷える月の最低気温が氷点下の都道府県は29から12に減り、最も上がったのは今も氷点下の12道県
description: 1975〜2024年の気象データで、1年でいちばん冷える月の最低気温を都道府県別に集計しました。氷点下だった29都道府県は12に減り、上がり幅が最も大きいのは今も氷点下の12道県の2.30℃でした。
publishedAt: 2026-03-02
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 気候変動
  - 気温
  - 都道府県
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/1.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（B 自然環境）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/B
    publisher: 総務省統計局
  - title: 地上観測地点「東京」の移転について
    url: https://www.jma.go.jp/jma/press/1410/03b/20141003_tokyo_rojo.html
    publisher: 気象庁
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: b_pref_land の最低気温（B4103）を自分の都道府県について1975年から2024年まで並べて。0℃を下回った年が最後にいつかを出して、最高気温（B4102）の上がり幅とも比べて
socialAnnounce: |-
  1年でいちばん冷える月の最低気温を、47都道府県で50年分集計しました。

  氷点下だった29都道府県は12に減り、上がり幅が最大なのは今も氷点下の12道県です。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

1年でいちばん冷える月の最低気温（日最低気温の月平均）が氷点下の都道府県は、1975〜1984年の10年平均では29、2015〜2024年の10年平均では12でした。17府県が氷点下から氷点上に移り、この17府県には2024年時点で3,002万人、全国の24.2%が住んでいます。上がり幅が最も大きいのは、今も氷点下の12道県で、平均2.30℃でした。

e-Stat[「社会・人口統計体系」](https://www.stat.go.jp/data/ssds/1.html)の都道府県別データには、年平均気温に加えて、1年でいちばん暑い月といちばん寒い月の値も1975年から2024年まで収録されています。3つを並べると、47都道府県の平均の上がり幅はほとんど同じで、約2℃の上昇で0℃を上回ったかどうかが都道府県によって異なります。

## 年平均気温・最高気温・最低気温は、どれも約2℃上がった

気象のデータは都道府県別テーブル（`b_pref_land`）に入っています。気温に関わるカテゴリは3つあります。

| コード | 内容                                   |
| ------ | -------------------------------------- |
| B4101  | 年平均気温                             |
| B4102  | 最高気温（日最高気温の月平均の最高値） |
| B4103  | 最低気温（日最低気温の月平均の最低値） |

最低気温（`B4103`）は、その年でいちばん冷えた月について、日ごとの最低気温を平均した値です。1日の最低記録ではなく月の平均なので、その年の寒さの水準を表します。

都道府県の値は、1地点の気象台の観測値です。[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)は「都道府県庁所在地のデータを掲載している。ただし、埼玉県は熊谷市、東京都は千代田区、滋賀県は彦根市における気象台の観測値である」としています。同じ都道府県の中でも標高や海からの距離で気温は違いますが、その違いはこの値には含まれません。

3つのカテゴリについて、前期（1975〜1984年）と後期（2015〜2024年）の10年平均を47都道府県で平均し、差を計算しました。

```sql
SELECT * FROM indicator_summary
```

上がり幅は年平均気温が1.73℃、最高気温が2.00℃、最低気温が2.07℃で、暑い月と寒い月の上がり幅にほとんど差はありません。

最高気温は30.64℃から32.65℃に上がりました。最低気温は-0.91℃から1.16℃に上がり、氷点下から氷点上に変わっています。

## 47都道府県の平均が0℃を下回った最後の年は2018年

47都道府県の最低気温を年ごとに平均した推移です。青い棒が0℃を下回った年です。

```chart
{
  "layer": [
    {
      "data": {"name": "min_temp_trend"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "avg_min", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "avg_min",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "最低気温の47都道府県平均（℃）", "grid": true}
        },
        "color": {
          "field": "is_below",
          "type": "quantitative",
          "scale": {"range": ["#ea580c", "#0369a1"]}
        }
      }
    }
  ]
}
```

年ごとの変動は大きく、2020年の2.50℃から1977年の-2.13℃まで4.6℃の差があります。0℃を下回る年は1980年代までに集中していて、最後は2018年（-0.16℃）です。

## 氷点下だった29都道府県のうち17府県が氷点上に移った

47都道府県それぞれについて前期と後期の10年平均を小数第2位まで出し、0℃を下回るかどうかで分けました。前期に氷点下だったのは29都道府県、後期は12道県で、17府県が氷点下から氷点上に移りました。前期がちょうど0.00℃の高知県と0.01℃の広島県は、氷点下に含めていません。

10年平均でなく年ごとに集計しても同じ傾向です。1年でいちばん冷える月の最低気温が0℃を下回った都道府県の数は、前期の10年間で年平均28.3、後期の10年間で14.1でした。

```sql
SELECT * FROM below_count_summary
```

3つの区分を地図にしました。

```map
type: map
layers:
  - from: pref_group_map
    geojson: geojson
    color: grp
    label: hover_text
lng: 137
lat: 36.5
zoom: 4
```

濃い橙で塗られているのが、氷点上に移った17府県です。新潟・富山・石川・福井の北陸4県、愛知・岐阜・三重、京都・滋賀・奈良、鳥取・島根・岡山・山口、香川、熊本、群馬で、いずれも関東以西です。北海道と東北の県は含まれていません。前期の値は群馬県の-2.31℃から香川県の-0.07℃までで、前期から0℃に近かった府県です。

青いままなのが、後期も氷点下の12道県です。北海道と東北6県に、茨城・栃木・埼玉・山梨・長野が加わります。淡い橙は前期から氷点上だった18都府県で、千葉・東京・神奈川と静岡、大阪・兵庫・和歌山、徳島・愛媛・高知、広島、福岡・佐賀・長崎・大分・宮崎・鹿児島、沖縄です。

この値は月の平均なので、後期の値が0.01℃の群馬県や0.24℃の新潟県でも、氷点下まで下がる日は今もあります。

## 上がり幅は3つの区分とも約2℃で、区分を分けたのは前期の水準

区分ごとに、前期・後期の平均と上がり幅、2024年の総人口（`A1101`）を並べました。

```sql
SELECT * FROM group_summary
```

上がり幅は、前期から氷点上の18都府県が2.04℃、氷点上に移った17府県が1.95℃、後期も氷点下の12道県が2.30℃です。3つとも2℃前後で、最も大きいのは後期も氷点下の12道県でした。最低気温が最も大きく上がった地域でも、氷点下のままです。

47都道府県の上がり幅は0.75〜3.13℃の範囲にあります。前期の水準は北海道の-9.24℃から沖縄県の13.21℃まで、22℃以上の差があります。前期の水準と上がり幅の相関は-0.33で、寒い地点ほどわずかに大きく上がっていますが、22℃の差と比較すると小さな違いです。0℃を上回ったかどうかは、ほぼ前期の水準で決まっています。

上がり幅が最も小さい東京都の0.75℃は、観測地点の移転を含む値です。気象庁は2014年12月に「東京」の観測地点を大手町から北の丸公園へ[移しています](https://www.jma.go.jp/jma/press/1410/03b/20141003_tokyo_rojo.html)。移転の前後の10年ずつ（2005〜2014年と2015〜2024年）を比較すると、最低気温は47都道府県の平均で0.74℃上がり、最も上がった奈良県では1.31℃でしたが、東京都は0.70℃下がっています。下がったのは東京都と岡山県（0.37℃）の2つだけです。後期の10年はすべて移転後なので、東京都の上がり幅には移転による差が含まれます。東京都を除く46道府県の上がり幅は1.49〜3.13℃です。

```sql
SELECT * FROM tokyo_step
```

前期の水準を横軸、後期の水準を縦軸にとると、47都道府県は斜めに並びます。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter_above"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "hover_text", "type": "nominal"},
          {"field": "ev", "type": "quantitative"},
          {"field": "rv", "type": "quantitative"}
        ],
        "x": {
          "field": "ev",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "前期（1975〜1984年）の最低気温（℃）", "grid": true}
        },
        "y": {
          "field": "rv",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "後期（2015〜2024年）の最低気温（℃）", "grid": true}
        },
        "color": {
          "datum": "もともと氷点上",
          "type": "nominal",
          "scale": {
            "domain": ["もともと氷点上", "氷点上に移った", "依然として氷点下"],
            "range": ["#fdba74", "#ea580c", "#0369a1"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "scatter_crossed"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "hover_text", "type": "nominal"},
          {"field": "ev", "type": "quantitative"},
          {"field": "rv", "type": "quantitative"}
        ],
        "x": {
          "field": "ev",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "前期（1975〜1984年）の最低気温（℃）", "grid": true}
        },
        "y": {
          "field": "rv",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "後期（2015〜2024年）の最低気温（℃）", "grid": true}
        },
        "color": {
          "datum": "氷点上に移った",
          "type": "nominal",
          "scale": {
            "domain": ["もともと氷点上", "氷点上に移った", "依然として氷点下"],
            "range": ["#fdba74", "#ea580c", "#0369a1"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "scatter_still"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "hover_text", "type": "nominal"},
          {"field": "ev", "type": "quantitative"},
          {"field": "rv", "type": "quantitative"}
        ],
        "x": {
          "field": "ev",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "前期（1975〜1984年）の最低気温（℃）", "grid": true}
        },
        "y": {
          "field": "rv",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "後期（2015〜2024年）の最低気温（℃）", "grid": true}
        },
        "color": {
          "datum": "依然として氷点下",
          "type": "nominal",
          "scale": {
            "domain": ["もともと氷点上", "氷点上に移った", "依然として氷点下"],
            "range": ["#fdba74", "#ea580c", "#0369a1"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeWidth": 1.5, "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": -10, "type": "quantitative"},
        "x2": {"datum": 15, "type": "quantitative"},
        "y": {"datum": -10, "type": "quantitative"},
        "y2": {"datum": 15, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#dc2626", "strokeWidth": 1, "strokeDash": [2, 3]},
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#dc2626", "strokeWidth": 1, "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 0, "type": "quantitative"}
      }
    }
  ]
}
```

破線は前期と後期の値が同じ位置です。47点すべてが破線より上にあり、破線からの縦方向の差（上がり幅）は0.75〜3.13℃の範囲にあります。赤い点線が0℃です。横軸が0より左、縦軸が0より上の区画（前期は氷点下、後期は氷点上）にある17点が、区分の変わった府県です。左下にある12点は、上がり幅は大きかったものの0℃を上回りませんでした。

## 47都道府県の前期と後期の値

前期と後期の値、上がり幅、区分です。

```sql
SELECT * FROM pref_all
```

この表から、都道府県ごとに、いちばん冷える月の最低気温が0℃を上回っているかどうかを確認できます。

## まとめ

- 47都道府県の平均の上がり幅は、前期（1975〜1984年）から後期（2015〜2024年）にかけて年平均気温1.73℃・最高気温2.00℃・最低気温2.07℃で、暑い月と寒い月でほとんど差がない
- 1年でいちばん冷える月の最低気温が氷点下だった都道府県は29から12に減り、17府県が氷点上に移った。この17府県には2024年時点で3,002万人、全国の24.2%が住んでいる
- 上がり幅が最も大きかったのは、区分の変わらなかった12道県の2.30℃だった。0℃を上回ったかどうかは、上がり幅でなく前期の水準で決まっている

## データの出典

本記事は e-Stat[「社会・人口統計体系」](https://www.stat.go.jp/data/ssds/1.html)の都道府県別データから、年平均気温（`B4101`）・最高気温（`B4102`）・最低気温（`B4103`）と総人口（`A1101`）を2026年9月18日時点で集計しています。気温の元データは気象庁の過去の気象データで、収録は1975年から2024年までです。`time_name` は「年度」表記ですが、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)の時点は「暦年平均」で、値は暦年のものです。地図の境界は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、行政のオープンデータを、列名・単位・カテゴリコードの体系を統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[都道府県別の土地・気象テーブル](/datasets/queria/e_stat/ssds/b_pref_land)から、自分の担当地域のいちばん冷える月の最低気温の推移を確認したり、降水量や日照時間と並べたりできます。

```sql id=indicator_summary
WITH base AS (SELECT cat01, year, AVG(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.b_pref_land WHERE cat01 IN ('B4101', 'B4102', 'B4103') AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY cat01, year) SELECT CASE cat01 WHEN 'B4102' THEN '最高気温（B4102）' WHEN 'B4101' THEN '年平均気温（B4101）' ELSE '最低気温（B4103）' END AS 指標, ROUND(AVG(v) FILTER (WHERE year BETWEEN 1975 AND 1984), 2) AS 前期1975から1984年, ROUND(AVG(v) FILTER (WHERE year BETWEEN 2015 AND 2024), 2) AS 後期2015から2024年, ROUND(AVG(v) FILTER (WHERE year BETWEEN 2015 AND 2024) - AVG(v) FILTER (WHERE year BETWEEN 1975 AND 1984), 2) AS 上がり幅 FROM base GROUP BY cat01 ORDER BY cat01
```

```sql id=min_temp_trend
SELECT year, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) AS avg_min, CASE WHEN AVG(TRY_CAST(value AS DOUBLE)) < 0 THEN 1 ELSE 0 END AS is_below FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=below_count_summary
WITH yearly AS (SELECT year, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) < 0) AS below FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year) SELECT ROUND(AVG(below) FILTER (WHERE year BETWEEN 1975 AND 1984), 1) AS 前期の年平均都道府県数, ROUND(AVG(below) FILTER (WHERE year BETWEEN 2015 AND 2024), 1) AS 後期の年平均都道府県数 FROM yearly
```

```sql id=pref_group_map
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), zones AS (SELECT early.area_name, early.v AS ev, recent.v AS rv, CASE WHEN early.v < 0 AND recent.v >= 0 THEN 1 WHEN early.v < 0 THEN 2 ELSE 0 END AS grp_id FROM early JOIN recent USING (area_name)) SELECT z.area_name AS pref_name, ST_AsGeoJSON(ST_Simplify(p.geometry, 0.005)) AS geojson, z.grp_id AS value, CASE z.grp_id WHEN 0 THEN 'もともと氷点上' WHEN 1 THEN '氷点上に移った' ELSE '依然として氷点下' END AS grp, z.area_name || '：' || CASE z.grp_id WHEN 0 THEN 'もともと氷点上' WHEN 1 THEN '氷点上に移った' ELSE '依然として氷点下' END || '（' || CAST(z.ev AS VARCHAR) || '℃ → ' || CAST(z.rv AS VARCHAR) || '℃）' AS hover_text, ROW_NUMBER() OVER (ORDER BY z.area_name) - 1 AS row_id FROM zones z JOIN nlftp.boundary.prefecture p ON z.area_name = p.prefecture_name ORDER BY z.area_name
```

```sql id=group_summary
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), zones AS (SELECT early.area_name, early.v AS ev, recent.v AS rv, CASE WHEN early.v < 0 AND recent.v >= 0 THEN 1 WHEN early.v < 0 THEN 2 ELSE 0 END AS grp_id FROM early JOIN recent USING (area_name)), pop AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS p FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT CASE z.grp_id WHEN 0 THEN 'もともと氷点上' WHEN 1 THEN '氷点上に移った' ELSE '依然として氷点下' END AS 区分, COUNT(*) AS 都道府県数, ROUND(AVG(z.ev), 2) AS 前期の平均, ROUND(AVG(z.rv), 2) AS 後期の平均, ROUND(AVG(z.rv - z.ev), 2) AS 平均の上がり幅, ROUND(SUM(pop.p) / 10000) AS 人口万人, ROUND(SUM(pop.p) * 100.0 / SUM(SUM(pop.p)) OVER (), 1) AS 人口比 FROM zones z JOIN pop ON z.area_name = pop.area_name GROUP BY z.grp_id ORDER BY z.grp_id
```

```sql id=scatter_above
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), zones AS (SELECT early.area_name, early.v AS ev, recent.v AS rv, CASE WHEN early.v < 0 AND recent.v >= 0 THEN 1 WHEN early.v < 0 THEN 2 ELSE 0 END AS grp_id FROM early JOIN recent USING (area_name)) SELECT area_name, ev, rv, area_name || '：' || CAST(ev AS VARCHAR) || '℃ → ' || CAST(rv AS VARCHAR) || '℃' AS hover_text FROM zones WHERE grp_id = 0 ORDER BY area_name
```

```sql id=scatter_crossed
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), zones AS (SELECT early.area_name, early.v AS ev, recent.v AS rv, CASE WHEN early.v < 0 AND recent.v >= 0 THEN 1 WHEN early.v < 0 THEN 2 ELSE 0 END AS grp_id FROM early JOIN recent USING (area_name)) SELECT area_name, ev, rv, area_name || '：' || CAST(ev AS VARCHAR) || '℃ → ' || CAST(rv AS VARCHAR) || '℃' AS hover_text FROM zones WHERE grp_id = 1 ORDER BY area_name
```

```sql id=scatter_still
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), zones AS (SELECT early.area_name, early.v AS ev, recent.v AS rv, CASE WHEN early.v < 0 AND recent.v >= 0 THEN 1 WHEN early.v < 0 THEN 2 ELSE 0 END AS grp_id FROM early JOIN recent USING (area_name)) SELECT area_name, ev, rv, area_name || '：' || CAST(ev AS VARCHAR) || '℃ → ' || CAST(rv AS VARCHAR) || '℃' AS hover_text FROM zones WHERE grp_id = 2 ORDER BY area_name
```

```sql id=rise_extremes
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), zones AS (SELECT early.area_name, early.v AS ev, recent.v AS rv FROM early JOIN recent USING (area_name)) SELECT ROUND(MIN(rv - ev), 2) AS 上がり幅の最小, ROUND(MIN(rv - ev) FILTER (WHERE area_name <> '東京都'), 2) AS 東京都を除く上がり幅の最小, ROUND(MAX(rv - ev), 2) AS 上がり幅の最大, ROUND(MIN(ev), 2) AS 前期の最小, ROUND(MAX(ev), 2) AS 前期の最大, ROUND(CORR(ev, rv - ev), 2) AS 前期と上がり幅の相関 FROM zones
```

```sql id=tokyo_step
WITH t AS (SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year BETWEEN 2005 AND 2014) AS a, AVG(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year BETWEEN 2015 AND 2024) AS b FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT ROUND(AVG(b - a), 2) AS 平均の変化, ROUND(MAX(b - a) FILTER (WHERE area_name = '東京都'), 2) AS 東京都の変化, ROUND(MAX(b - a) FILTER (WHERE area_name = '岡山県'), 2) AS 岡山県の変化, ARG_MAX(area_name, b - a) AS 最も上がった都道府県, ROUND(MAX(b - a), 2) AS 最大, COUNT(*) FILTER (WHERE b - a < 0) AS 下がった都道府県数 FROM t
```

```sql id=pref_all
WITH early AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 1975 AND 1984 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), recent AS (SELECT area_name, ROUND(AVG(TRY_CAST(value AS DOUBLE)), 2) + 0.0 AS v FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year BETWEEN 2015 AND 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT early.area_name AS 都道府県, CASE WHEN early.v < 0 AND recent.v >= 0 THEN '氷点上に移った' WHEN early.v < 0 THEN '依然として氷点下' ELSE 'もともと氷点上' END AS 区分, early.v AS 前期1975から1984年, recent.v AS 後期2015から2024年, ROUND(recent.v - early.v, 2) AS 上がり幅 FROM early JOIN recent USING (area_name) ORDER BY recent.v DESC, early.area_name
```
