---
title: 人口あたりの図書館数が7位の秋田県は、1人あたりの貸出冊数が47位だった
description: 2017年度の人口1人あたり図書館貸出冊数は滋賀県7.87冊から秋田県2.65冊まで3.0倍の開きがあります。人口あたりの図書館数との相関係数は0.13で、秋田県は図書館数で7位なのに貸出冊数は47位、東京都は図書館数29位で貸出冊数2位でした。1館あたりの可住地面積の対数とは相関係数−0.64で、1館が受け持つ面積が広い県ほど貸出冊数が少ない傾向があります
publishedAt: 2026-04-04
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 図書館
  - 文化
  - 自治体職員
datasets:
  - queria/e_stat
sources:
  - title: 社会教育調査
    url: https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm
    publisher: 文部科学省
  - title: 社会・人口統計体系 項目定義（G 文化・スポーツ）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/G
    publisher: 総務省統計局
  - title: 統計でみる都道府県・市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
agentHint: 図書館館外貸出冊数（G1406）を総人口（A1101）で割った人口1人あたり貸出冊数と、人口10万人あたり図書館数（G1401）・図書館職員数（G1402）を2017年度・2018年度の都道府県別で並べ、自分の県と近い県を比べて
socialAnnounce: |-
  図書館の多い県ほど本が借りられている、とは限りませんでした。

  人口あたりの図書館数と貸出冊数の相関係数は0.13。秋田県は図書館数7位で貸出冊数47位、東京都は図書館数29位で貸出冊数2位です。

  図書館の整備水準を考える自治体の方に。
---

2017年度の人口1人あたりの図書館の貸出冊数は、滋賀県の7.87冊が最も多く、秋田県の2.65冊が最も少なく、3.0倍の差がありました。秋田県は、人口あたりの図書館数では47都道府県で7番目に多い県です。人口あたりの図書館数と貸出冊数の相関係数は0.13で、図書館数が多い県ほど貸出冊数が多いという関係はほとんどありません。1館あたりの可住地面積の対数とは相関係数が−0.64で、1館が受け持つ面積が広い県ほど貸出冊数が少なくなっています。

## 人口あたりの図書館数と貸出冊数の相関係数は0.13

文部科学省の[社会教育調査](https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm)は、公立図書館の数・職員数・蔵書冊数・館外貸出冊数などを都道府県別に集計しています。e-Stat の社会・人口統計体系には、この調査の次の指標が都道府県別に収録されています（`e_stat.ssds.g_pref_culture`）。

| コード | 内容               | 時点        |
| ------ | ------------------ | ----------- |
| G1401  | 図書館数           | 10月1日現在 |
| G1402  | 図書館職員数       | 10月1日現在 |
| G1403  | 図書館蔵書数       | 10月1日現在 |
| G1404  | 図書館登録者数     | 年度間      |
| G1405  | 図書館帯出者数     | 年度間      |
| G1406  | 図書館館外貸出冊数 | 年度間      |

貸出冊数（`G1406`）は、自動車文庫・巡回文庫での貸出を含む、1年度間の館外貸出の延べ冊数です。最新の2020年度は新型コロナウイルス感染症の拡大で多くの図書館が休館した年度なので、都道府県の比較には、その前の調査の2017年度の値を使います。

2018年10月1日現在の図書館数を人口10万人あたりに換算し、2017年度の人口1人あたり貸出冊数と並べました。人口は総人口（`A1101`、`e_stat.ssds.a_pref_population`）です。社会教育調査はおおむね3年ごとの調査で、貸出冊数は調査の前年度1年間、図書館数は調査年の10月1日現在の値です。図書館数は分館も1館として集計しています（[項目定義 G](https://www.e-stat.go.jp/koumoku/koumoku_teigi/G)）。

```chart
{
  "height": 480,
  "layer": [
    {
      "data": {"name": "lib_vs_lending"},
      "mark": {"type": "point", "color": "#8b5cf6", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "lib_per_100k", "type": "quantitative"},
          {"field": "lending_per_person", "type": "quantitative"}
        ],
        "x": {
          "field": "lib_per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり図書館数（館、2018年）", "grid": true}
        },
        "y": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "lib_vs_lending"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "lib_per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり図書館数（館、2018年）", "grid": true}
        },
        "y": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

47都道府県の人口10万人あたり図書館数と1人あたり貸出冊数の相関係数は0.13です。図書館数の上位10県のうち、貸出冊数でも上位10県に入るのは山口県・福井県・鳥取県の3県だけです。

秋田県は人口10万人あたり4.87館で図書館数は7位ですが、貸出冊数は47位です。高知県も図書館数は4位（5.80館）で、貸出冊数は40位でした。逆に東京都は2.87館で29位、大阪府は1.66館で44位ですが、貸出冊数はそれぞれ2位と9位です。貸出冊数には、他県から通勤・通学してくる人への貸出も含まれます。2015年の昼夜間人口比率が117.8%の東京都では、常住人口で割った値が、都民の利用より大きく出ている可能性があります。

```sql
SELECT area_name AS 都道府県, lib_per_100k AS 人口10万人あたり図書館数, lib_rank AS 図書館数の順位, lending_per_person AS 人口1人あたり貸出冊数, lending_rank AS 貸出冊数の順位, daytime_ratio AS 昼夜間人口比率_2015年 FROM lib_vs_lending WHERE area_name IN ('秋田県', '高知県', '東京都', '大阪府', '滋賀県') ORDER BY lib_rank
```

人口1人あたり貸出冊数と、職員数・蔵書冊数・1館あたりの可住地面積（次の節）との相関係数を並べます。表の後ろの2列は、人口あたり図書館数との相関係数と、両方の指標で上位10県に入る県の数です。

```sql
SELECT corr_libraries AS 図書館数との相関係数, corr_staff AS 職員数との相関係数, corr_books AS 蔵書冊数との相関係数, corr_area_log AS 一館あたり可住地面積の対数との相関係数, corr_lib_area AS 図書館数と一館あたり可住地面積の相関係数, top10_overlap AS 図書館数と貸出冊数の両方で上位10県に入る県の数 FROM correlations
```

人口10万人あたりの職員数と人口1人あたりの蔵書冊数は、図書館数より貸出冊数との相関が強くなっています。いずれも47都道府県の値の相関で、職員や蔵書を増やすと貸出が増えるという因果関係を示すものではありません。

## 1館あたりの可住地面積は秋田県が66.8km²で、東京都の約19倍

人口あたりの館数には、県内のどれだけの範囲に図書館が分布しているかが反映されません。人が住める土地の広さに対する館数を見るため、可住地面積（`B1103`、`e_stat.ssds.b_pref_land`、2018年度）を図書館数で割りました。図の横軸は対数目盛です。

```chart
{
  "height": 480,
  "layer": [
    {
      "data": {"name": "lib_vs_lending"},
      "mark": {"type": "point", "color": "#0ea5e9", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "km2_per_library", "type": "quantitative"},
          {"field": "lending_per_person", "type": "quantitative"}
        ],
        "x": {
          "field": "km2_per_library",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1館あたり可住地面積（km²、2018年、対数目盛）", "grid": true}
        },
        "y": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "lib_vs_lending"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "km2_per_library",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1館あたり可住地面積（km²、2018年、対数目盛）", "grid": true}
        },
        "y": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

1館あたり可住地面積の対数と1人あたり貸出冊数の相関係数は−0.64で、1館が受け持つ面積が広い県ほど貸出冊数が少ない傾向があります。人口10万人あたりの館数と1館あたり可住地面積の相関係数は−0.06で、2つの指標はほぼ独立しています。1館あたり可住地面積は都市部ほど小さくなる値なので、この相関には人口の集まり方の違いも含まれます。館を増やすと貸出が増えるという因果関係を示すものではありません。

秋田県は人口あたりでは館数7位ですが、1館あたり可住地面積は66.8km²で、東京都（3.6km²）の約19倍です。1館あたり可住地面積が最も広いのは北海道の147.2km²で、青森県（92.3km²）、宮城県（90.1km²）と東北の県が続きます。

```sql
SELECT area_name AS 都道府県, km2_per_library AS 一館あたり可住地面積_km2, area_rank AS 広い順の順位, lending_per_person AS 人口1人あたり貸出冊数 FROM lib_vs_lending WHERE area_rank <= 3 OR area_name IN ('秋田県', '福井県', '東京都') ORDER BY area_rank
```

## 人口1人あたり貸出冊数は、滋賀県7.87冊、東京都7.86冊、香川県6.51冊の順に多い

2017年度の人口1人あたり貸出冊数を、多い順に並べました。上位10県・中位・下位10県で色を分けています。

```chart
{
  "height": 680,
  "layer": [
    {
      "data": {"name": "lending_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "lending_per_person", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10県",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "中位", "下位10県"], "range": ["#ec4899", "#f9a8d4", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "lending_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "lending_per_person", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中位",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "中位", "下位10県"], "range": ["#ec4899", "#f9a8d4", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "lending_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "lending_per_person", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "lending_per_person",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口1人あたり貸出冊数（冊、2017年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10県",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "中位", "下位10県"], "range": ["#ec4899", "#f9a8d4", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

滋賀県（7.87冊）と東京都（7.86冊）がほぼ同じで最も多く、香川県（6.51冊）が続きます。少ないのは秋田県（2.65冊）、青森県（2.81冊）、宮崎県（3.14冊）で、最も多い滋賀県と最も少ない秋田県の差は3.0倍です。

## 全国の図書館数は増え続け、貸出冊数は2010年度が最も多い

```chart
{
  "layer": [
    {
      "data": {"name": "lending_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"lending_10k\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 64, "color": "#ec4899"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "lending_10k", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "lending_10k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "館外貸出冊数（万冊）", "format": ",d", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

全国の貸出冊数は2010年度の6億8,234万冊が収録期間で最も多く、2017年度は6億5,379万冊でした。2020年度は5億3,078万冊で、2017年度から18.8%減っています。2020年度は新型コロナウイルス感染症の拡大で多くの図書館が休館や利用制限を行った年度です。

```chart
{
  "layer": [
    {
      "data": {"name": "lib_count"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"lib_count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 64, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "lib_count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "lib_count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "図書館数（館）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

図書館数は2005年の2,979館から2021年の3,394館まで、調査のたびに増えています。

## 自治体の図書館政策での使い方

- 図書館の整備計画を担当する県の職員は、館数の目標を人口あたりで決める前に、1館あたり可住地面積でも自県を他県と比較できます。人口あたりの館数が同じくらいの秋田県（4.87館）と福井県（4.76館）でも、1館あたり可住地面積は秋田県が66.8km²、福井県が29.1km²で、貸出冊数は2.65冊と6.33冊です
- 貸出冊数が多い県と少ない県で職員数・蔵書冊数がどう違うかを、同じテーブルの `G1402`・`G1403` で比較できます

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)に収録された文部科学省の[社会教育調査](https://www.mext.go.jp/b_menu/toukei/chousa02/shakai/index.htm)の都道府県別データを、2026-10-22 時点で集計しています。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位を統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。記事内のSQLを実行して数字を確認したり、本記事で使った[都道府県別の社会教育統計テーブル](/datasets/queria/e_stat/ssds/g_pref_culture)で自県と近隣県の図書館数・職員数・貸出冊数の推移を比較したりできます。

```sql id=lending_trend
SELECT year, CAST(value AS DOUBLE) / 10000 AS lending_10k FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G1406' AND area = '00000' ORDER BY year
```

```sql id=lib_count
SELECT year, value AS lib_count FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G1401' AND area = '00000' AND year >= 2005 ORDER BY year
```

```sql id=national_summary
-- 本文の全国値。貸出冊数は2017年度から2020年度への変化率も出す
SELECT MAX(CASE WHEN cat01 = 'G1401' AND year = 2005 THEN value END) AS libraries_2005, MAX(CASE WHEN cat01 = 'G1401' AND year = 2021 THEN value END) AS libraries_2021, MAX(CASE WHEN cat01 = 'G1406' AND year = 2010 THEN value END) AS lending_2010, MAX(CASE WHEN cat01 = 'G1406' AND year = 2017 THEN value END) AS lending_2017, MAX(CASE WHEN cat01 = 'G1406' AND year = 2020 THEN value END) AS lending_2020, ROUND((MAX(CASE WHEN cat01 = 'G1406' AND year = 2020 THEN value END) / MAX(CASE WHEN cat01 = 'G1406' AND year = 2017 THEN value END) - 1) * 100, 1) AS change_pct_2017_2020 FROM e_stat.ssds.g_pref_culture WHERE area = '00000'
```

```sql id=pref_library
-- 貸出冊数は2017年度間、図書館数・職員数・蔵書数は2018年調査の値。人口はそれぞれの年の総人口。可住地面積は ha
WITH g AS (SELECT area, area_name, MAX(CASE WHEN cat01 = 'G1401' AND year = 2018 THEN value END) AS libraries, MAX(CASE WHEN cat01 = 'G1402' AND year = 2018 THEN value END) AS staff, MAX(CASE WHEN cat01 = 'G1403' AND year = 2018 THEN value END) AS books, MAX(CASE WHEN cat01 = 'G1406' AND year = 2017 THEN value END) AS lending FROM e_stat.ssds.g_pref_culture WHERE area <> '00000' GROUP BY area, area_name), p AS (SELECT area, MAX(CASE WHEN year = 2017 THEN value END) AS pop_2017, MAX(CASE WHEN year = 2018 THEN value END) AS pop_2018 FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year IN (2017, 2018) GROUP BY area), d AS (SELECT area, value AS daytime_ratio FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A6108' AND year = 2015), h AS (SELECT area, value AS habitable_ha FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B1103' AND year = 2018) SELECT g.area_name, libraries / pop_2018 * 100000 AS lib_per_100k, habitable_ha / 100 / libraries AS km2_per_library, daytime_ratio, staff / pop_2018 * 100000 AS staff_per_100k, books / pop_2018 AS books_per_person, lending / pop_2017 AS lending_per_person FROM g JOIN p USING (area) JOIN d USING (area) JOIN h USING (area)
```

```sql id=lending_ranking
SELECT area_name, ROUND(lending_per_person, 2) AS lending_per_person, ROW_NUMBER() OVER (ORDER BY lending_per_person DESC, area_name) AS rn FROM pref_library
```

```sql id=lending_top
SELECT area_name, lending_per_person FROM lending_ranking WHERE rn <= 10 ORDER BY rn
```

```sql id=lending_mid
SELECT area_name, lending_per_person FROM lending_ranking WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=lending_bottom
SELECT area_name, lending_per_person FROM lending_ranking WHERE rn > 37 ORDER BY rn
```

```sql id=lib_vs_lending
SELECT area_name, ROUND(lib_per_100k, 2) AS lib_per_100k, RANK() OVER (ORDER BY lib_per_100k DESC) AS lib_rank, ROUND(lending_per_person, 2) AS lending_per_person, RANK() OVER (ORDER BY lending_per_person DESC) AS lending_rank, ROUND(km2_per_library, 1) AS km2_per_library, RANK() OVER (ORDER BY km2_per_library DESC) AS area_rank, daytime_ratio FROM pref_library ORDER BY lib_per_100k DESC, area_name
```

```sql id=correlations
WITH r AS (SELECT *, RANK() OVER (ORDER BY lib_per_100k DESC) AS lib_rank, RANK() OVER (ORDER BY lending_per_person DESC) AS lending_rank FROM pref_library) SELECT ROUND(CORR(lending_per_person, lib_per_100k), 2) AS corr_libraries, ROUND(CORR(lending_per_person, staff_per_100k), 2) AS corr_staff, ROUND(CORR(lending_per_person, books_per_person), 2) AS corr_books, ROUND(CORR(lending_per_person, LN(km2_per_library)), 2) AS corr_area_log, ROUND(CORR(lib_per_100k, km2_per_library), 2) AS corr_lib_area, COUNT(*) FILTER (WHERE lib_rank <= 10 AND lending_rank <= 10) AS top10_overlap FROM r
```
