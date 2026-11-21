---
title: 派遣社員の割合が全国平均を上回る街には、女性が65.0%の東京の通勤圏と、48.4%の工場の町がある
description: 2020年の国勢調査で派遣社員152万人を市区町村別に集計しました。割合が最も高いのは工場のある町ですが、工場のない東京の通勤圏でも全国平均を上回ります。派遣社員に占める女性の割合は、製造業の職場が少ない市区町村で65.0%、多い市区町村で48.4%です。
ogDescription: 2020年の国勢調査で派遣社員152万人を市区町村別に集計しました。割合が最も高いのは工場のある町ですが、工場のない東京の通勤圏でも全国平均を上回り、女性の割合は65.0%から48.4%まで差があります。
publishedAt: 2026-09-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 国勢調査
  - 雇用
  - 人材サービス
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 令和2年国勢調査 就業状態等基本集計
    url: https://www.stat.go.jp/data/kokusei/2020/kekka.html
    publisher: 総務省統計局
  - title: 統計でみる市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 国勢調査の従業上の地位別就業者数から、自分の県の市区町村についてパート・アルバイト・その他（employment_status_code = '13'）の割合を出して。派遣社員（'12'）の割合と並べて、男女別でも比べて
socialAnnounce: |-
  国勢調査で、派遣で働く152万人が住む市区町村を数えました。

  工場のある町でも東京の通勤圏でも割合は全国平均を上回りますが、女性の割合は製造業の集積で48.4%から65.0%まで開きます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2020年の国勢調査で、派遣社員は全国の就業者の2.64%（1,522,141人）でした。住んでいる市区町村別では、群馬県大泉町の12.17%が最も高く、上位には滋賀県・静岡県・愛知県などの工場のある町が並びます。一方、製造業の職場がほとんどない東京の通勤圏の市区町村でも、割合は全国平均を上回ります。派遣社員に占める女性の割合は、製造業の職場が最も少ない市区町村のグループで65.0%、最も多いグループで48.4%です。

人材サービスの拠点をどこに置くか、求人をどのエリアに出すかを決めるときは、派遣で働いている人がどこに住んでいるかが手がかりになります。求人サイトの掲載件数や事業所の数からは、住まいの分布は分かりません。[令和2年国勢調査の就業状態等基本集計](https://www.stat.go.jp/data/kokusei/2020/kekka.html)は、15歳以上の就業者を「従業上の地位」で分類していて、その中に「労働者派遣事業所の派遣社員」という区分があります。全国・都道府県・市区町村の1,965地域について、この区分の人数が公表されています。

## 派遣社員は全国の就業者の38人に1人

従業上の地位は11のコードで区別されていて、全国の就業者を次のように分けています。

```sql
SELECT * FROM status_mix
```

全国の就業者57,643,225人のうち、労働者派遣事業所の派遣社員（`12`）は1,522,141人で、割合は2.64%、およそ38人に1人です。正規の職員・従業員（`11`、30,796,831人）やパート・アルバイト・その他（`13`、14,623,249人）と比較すると、雇用者の中で派遣社員は少数です。この3つは雇用者（`1`、46,942,221人）の内訳で、合計すると雇用者の数になります。以下では、派遣社員の人数を就業者の総数（`0`）で割った値を「派遣社員の割合」と呼びます。

この人数は、勤め先ではなく住んでいる市区町村で集計されています。隣の市の工場に通っている人は、住んでいる市区町村の人数に入ります。

市区町村ごとの割合を地図にしました。色が濃いほど、その市区町村に住む就業者のうち派遣社員の割合が高い地域です。色の上限は6%で、それを超える市区町村はすべて同じ濃さです。就業者の少ない町村は数十人の増減で割合が動くので、単独で濃い点が混じります（福島県の富岡町8.00%・浪江町7.66%は、どちらも就業者が1,500人に満たない町です）。

```map
type: map
layers:
  - from: city_map
    geojson: geojson
    color: dispatch_pct
    label: city_name
    name: "派遣社員の割合（%）"
lng: 137.5
lat: 36.3
zoom: 4.4
```

色が濃いのは、静岡県から愛知県・三重県・滋賀県にかけての一帯と、群馬県・栃木県の北関東です。北海道・東北・四国・九州南部は、一部の市町村を除いて色が薄くなっています。

## 割合が高い市区町村は、工場のある町に集中している

就業者が5,000人以上の市区町村を、派遣社員の割合の高い順に並べました。東京23区は、区ごとの行と「特別区部」の合計行の両方があるので、二重に集計しないよう特別区部の1件として扱っています。

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "top20"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "dispatch_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "dispatch_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "派遣社員の割合（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市区町村"},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "top20"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "dispatch_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "派遣社員の割合（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市区町村"},
          "sort": null
        },
        "text": {"field": "dispatch_pct"}
      }
    }
  ]
}
```

最も高いのは群馬県の大泉町で12.17%です。全国の2.64%の約4.6倍で、この町に住む就業者のおよそ8人に1人が派遣社員です。2位は滋賀県の竜王町（7.97%）、3位は福岡県の苅田町（6.55%）で、滋賀県湖南市、山梨県中央市、福井県越前市と続きます。上位20はすべて4.82%以上です。

対象の1,187市区町村の中央値は2.19%で、4%以上は47市区町村です。そのうち31は滋賀県（9）・静岡県（8）・愛知県（6）・三重県（4）・群馬県（4）にあり、自動車や電機の工場が集まっている地域と重なります。東京都・大阪府・千葉県の市区町村は、4%以上の47に1つも入っていません。

## 都道府県別では差が約3倍になり、首都圏の4都県が上位10に入る

同じ割合を都道府県別に集計しました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "dispatch_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "dispatch_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "派遣社員の割合（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "dispatch_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "dispatch_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "派遣社員の割合（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "dispatch_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "dispatch_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "派遣社員の割合（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高い滋賀県は3.84%、最も低い高知県は1.29%で、差は約3.0倍です。上位10には、東京都（3.19%）・神奈川県（3.17%）・千葉県（3.04%）・埼玉県（3.02%）の首都圏の4都県がすべて入っています。市区町村の上位は工場のある町でしたが、都道府県別では工場地帯以外にも全国平均を上回る地域があります。

## 製造業の職場が少ない市区町村ほど、派遣社員に占める女性の割合が高い

市区町村を、製造業の職場の多さで5つのグループに分けて比較します。社会・人口統計体系（`c_municipal_economy`）の製造業従業者数（`C3404`）を同じ体系の総人口（`A1101`）で割り、人口100人あたりの人数にしました。この従業者数は事業所の所在地で集計されていて、ほかの市区町村から通ってくる人や、派遣されて働いている人も含みます。そのため、住んでいる人の職業ではなく、その市区町村にある製造業の職場の多さを表します。

グループ1が製造業の職場が最も少ない市区町村、グループ5が最も多い市区町村です。棒が派遣社員の割合、折れ線が派遣社員に占める女性の割合です。

```chart
{
  "height": 310,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "mfg_group"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "band", "type": "nominal"},
              {"field": "dispatch_pct", "type": "quantitative"}
            ],
            "x": {
              "field": "band",
              "type": "nominal",
              "axis": {"title": "人口100人あたりの製造業従業者数", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "dispatch_pct",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "派遣社員の割合（%）", "grid": true}
            },
            "color": {
              "datum": "派遣社員の割合",
              "type": "nominal",
              "scale": {"domain": ["派遣社員の割合", "派遣社員の女性割合"], "range": ["#93c5fd", "#ec4899"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "mfg_group"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"band\"]) && isValid(datum[\"female_pct\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#ec4899",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 64}
          },
          "encoding": {
            "tooltip": [
              {"field": "band", "type": "nominal"},
              {"field": "female_pct", "type": "quantitative"}
            ],
            "x": {
              "field": "band",
              "type": "nominal",
              "axis": {"title": "人口100人あたりの製造業従業者数", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "female_pct",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "派遣社員の女性割合（%）", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "派遣社員の女性割合",
              "type": "nominal",
              "scale": {"domain": ["派遣社員の割合", "派遣社員の女性割合"], "range": ["#93c5fd", "#ec4899"]},
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    }
  ],
  "resolve": {"scale": {"y": "independent"}},
  "config": {"legend": {"orient": "bottom"}}
}
```

派遣社員の割合が最も高いのはグループ5の3.32%で、最も低いのは中間のグループ3の2.36%です。グループ1も2.78%で、グループ2・3・4より高くなっています。グループ1の内訳は、埼玉・千葉・東京・神奈川の64市区町村が3.16%、それ以外の174市区町村が2.27%です。製造業の職場がほとんどない市区町村で派遣社員の割合が高いのは、首都圏の市区町村だけです。

派遣社員に占める女性の割合は、グループ1の65.0%からグループ5の48.4%まで、グループが上がるごとに下がります。全国の派遣社員に占める女性の割合は58.1%なので、グループ1はそれより6.9ポイント高く、グループ5は9.7ポイント低くなっています。製造業の職場がほとんどない市区町村では派遣社員の3人に2人が女性で、工場が集まる市区町村では男性のほうが多くなっています。

代表的な市区町村を並べました。

```sql
SELECT * FROM contrast
```

滋賀県の竜王町は、人口100人あたりの製造業従業者が63.6人でこの11市区町村の中で最も多く、派遣社員の割合も7.97%と高い一方、派遣社員525人のうち女性は17.5%です。東京都の調布市は製造業従業者が人口100人あたり0.8人で、派遣社員の割合は3.31%、女性が71.4%です。千葉県の浦安市（72.4%）・市川市（64.8%）・船橋市（63.4%）も女性のほうが多くなっています。竜王町の派遣社員は525人なので、1つの事業所の男女構成で女性の割合が大きく変わります。

竜王町も調布市も、派遣社員の割合は全国平均の2.64%を上回っていますが、採用の対象になる人の男女構成は大きく違います。

## 業務での使い方

- 自社の商圏に入る市区町村を、就業者数と派遣社員の割合の2列で並べます。千葉県船橋市は割合が3.53%で派遣社員が10,334人、滋賀県竜王町は割合が7.97%で525人と、採用の対象になる人数は大きく違います
- 3列目に人口100人あたりの製造業従業者数を追加し、求人の内容を市区町村の特徴に合わせます。この値が大きい市区町村ほど、派遣社員に占める男性の割合が高くなります
- 同じ商圏の中で候補を比較するときは、都道府県の平均値を使わずに市区町村の値を使います。都道府県別の割合は上位と下位の差が約3.0倍で、市区町村の間の差が見えなくなります

## データの出典

本記事は[令和2年国勢調査 就業状態等基本集計](https://www.stat.go.jp/data/kokusei/2020/kekka.html)（2020年10月1日現在）と、[統計でみる市区町村のすがた](https://www.stat.go.jp/data/ssds/index.html)の製造業従業者数（2020年6月1日現在）・総人口（国勢調査と同じ2020年10月1日現在）を2026-09-12時点で集計しています。地図の境界は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、国勢調査や社会・人口統計体系などの行政のオープンデータを、列名・単位・地域コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[国勢調査の従業上の地位テーブル](/datasets/e_stat/census/census_municipality_employment_status)と[市区町村の経済基盤テーブル](/datasets/e_stat/ssds/c_municipal_economy)から、自社の商圏に入る市区町村の数字を確認したり、候補地を並べて比較したりできます。

```sql id=national
SELECT MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS workers, MAX(CASE WHEN employment_status_code = '11' AND sex_code = '0' THEN value END) AS regular, MAX(CASE WHEN employment_status_code = '13' AND sex_code = '0' THEN value END) AS parttime, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS dispatch, ROUND(MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) * 100.0 / MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END), 2) AS dispatch_pct, ROUND(MAX(CASE WHEN employment_status_code = '12' AND sex_code = '2' THEN value END) * 100.0 / MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END), 1) AS dispatch_female_pct FROM e_stat.census.census_municipality_employment_status WHERE area_name = '全国'
```

```sql id=coverage
SELECT COUNT(DISTINCT area) AS areas, COUNT(DISTINCT CASE WHEN area_level = 'prefecture' THEN area END) AS prefectures, COUNT(DISTINCT CASE WHEN area_level IN ('city', 'town_village') THEN area END) AS cities FROM e_stat.census.census_municipality_employment_status
```

```sql id=status_mix
WITH t AS (SELECT employment_status_code AS code, employment_status AS name, value FROM e_stat.census.census_municipality_employment_status WHERE area_name = '全国' AND sex_code = '0' AND is_reprint = false) SELECT code AS 'コード', name AS '従業上の地位', value AS '就業者数（人）', ROUND(value * 100.0 / (SELECT value FROM t WHERE code = '0'), 2) AS '就業者に占める割合（%）' FROM t ORDER BY CASE code WHEN '0' THEN 1 WHEN '1' THEN 2 WHEN '11' THEN 3 WHEN '12' THEN 4 WHEN '13' THEN 5 WHEN '2' THEN 6 WHEN '3' THEN 7 WHEN '4' THEN 8 WHEN '5' THEN 9 WHEN '6' THEN 10 ELSE 11 END
```

```sql id=small_towns
WITH b AS (SELECT area, area_name, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village', 'ward') GROUP BY 1, 2), pr AS (SELECT DISTINCT LEFT(area, 2) AS pcode, area_name AS pref FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture') SELECT pr.pref || ' ' || b.area_name AS area_name, b.tot AS workers, ROUND(b.hk * 100.0 / b.tot, 2) AS dispatch_pct FROM b JOIN pr ON LEFT(b.area, 2) = pr.pcode WHERE b.tot < 5000 AND b.hk * 100.0 / b.tot >= 5 ORDER BY dispatch_pct DESC
```

```sql id=city_map
WITH h AS (SELECT area, area_name, MAX(CASE WHEN employment_status_code = '12' THEN value END) AS hk, MAX(CASE WHEN employment_status_code = '0' THEN value END) AS tot FROM e_stat.census.census_municipality_employment_status WHERE sex_code = '0' AND area_level IN ('city', 'town_village', 'ward') GROUP BY 1, 2) SELECT ST_AsGeoJSON(ST_SimplifyPreserveTopology(b.geometry, 0.01)) AS geojson, ROUND(h.hk * 100.0 / h.tot, 2) AS dispatch_pct, h.area_name AS city_name FROM h JOIN nlftp.boundary.designated_city b ON b.lg_code = h.area WHERE h.hk IS NOT NULL
```

```sql id=top20
WITH b AS (SELECT area, area_name, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village') GROUP BY 1, 2), pr AS (SELECT DISTINCT LEFT(area, 2) AS pcode, area_name AS pref FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture'), ranked AS (SELECT pr.pref || ' ' || b.area_name AS area_name, ROUND(b.hk * 100.0 / b.tot, 2) AS dispatch_pct, ROW_NUMBER() OVER (ORDER BY b.hk * 1.0 / b.tot DESC, b.area_name) AS rn FROM b JOIN pr ON LEFT(b.area, 2) = pr.pcode WHERE b.tot >= 5000 AND b.hk IS NOT NULL) SELECT area_name, dispatch_pct FROM ranked WHERE rn <= 20 ORDER BY rn
```

```sql id=spread
WITH b AS (SELECT area, area_name, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village') GROUP BY 1, 2) SELECT COUNT(*) AS cities, ROUND(MEDIAN(hk * 100.0 / tot), 2) AS median_pct, SUM(CASE WHEN hk * 100.0 / tot >= 5 THEN 1 ELSE 0 END) AS cities_over5, SUM(CASE WHEN hk * 100.0 / tot >= 4 THEN 1 ELSE 0 END) AS cities_over4 FROM b WHERE tot >= 5000 AND hk IS NOT NULL
```

```sql id=top_prefs
WITH b AS (SELECT area, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village') GROUP BY 1), pr AS (SELECT DISTINCT LEFT(area, 2) AS pcode, area_name AS pref FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture') SELECT pr.pref, COUNT(*) AS cities FROM b JOIN pr ON LEFT(b.area, 2) = pr.pcode WHERE b.tot >= 5000 AND b.hk * 100.0 / b.tot >= 4 GROUP BY 1 ORDER BY cities DESC, pr.pref
```

```sql id=pref_top
WITH b AS (SELECT area_name, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture' GROUP BY 1), ranked AS (SELECT area_name, ROUND(hk * 100.0 / tot, 2) AS dispatch_pct, ROW_NUMBER() OVER (ORDER BY hk * 1.0 / tot DESC, area_name) AS rn FROM b) SELECT area_name, dispatch_pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH b AS (SELECT area_name, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture' GROUP BY 1), ranked AS (SELECT area_name, ROUND(hk * 100.0 / tot, 2) AS dispatch_pct, ROW_NUMBER() OVER (ORDER BY hk * 1.0 / tot DESC, area_name) AS rn FROM b) SELECT area_name, dispatch_pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH b AS (SELECT area_name, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture' GROUP BY 1), ranked AS (SELECT area_name, ROUND(hk * 100.0 / tot, 2) AS dispatch_pct, ROW_NUMBER() OVER (ORDER BY hk * 1.0 / tot DESC, area_name) AS rn FROM b) SELECT area_name, dispatch_pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=group1_split
WITH h AS (SELECT area, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village') GROUP BY 1), m AS (SELECT area, value AS mfg FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C3404' AND year = 2020), p AS (SELECT area, value AS pop FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A1101' AND year = 2020), j AS (SELECT h.area, h.hk, h.tot, NTILE(5) OVER (ORDER BY m.mfg / p.pop) AS q FROM h JOIN m ON m.area = h.area JOIN p ON p.area = h.area WHERE h.tot >= 5000 AND p.pop > 0 AND h.hk IS NOT NULL) SELECT CASE WHEN LEFT(area, 2) IN ('11', '12', '13', '14') THEN '埼玉・千葉・東京・神奈川' ELSE 'それ以外' END AS zone, COUNT(*) AS cities, ROUND(SUM(hk) * 100.0 / SUM(tot), 2) AS dispatch_pct FROM j WHERE q = 1 GROUP BY 1 ORDER BY dispatch_pct DESC
```

```sql id=mfg_group
WITH h AS (SELECT area, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '2' THEN value END) AS hk_f, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village') GROUP BY 1), m AS (SELECT area, value AS mfg FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C3404' AND year = 2020), p AS (SELECT area, value AS pop FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A1101' AND year = 2020), j AS (SELECT h.hk, h.hk_f, h.tot, m.mfg * 100.0 / p.pop AS mfg_per100, NTILE(5) OVER (ORDER BY m.mfg / p.pop) AS q FROM h JOIN m ON m.area = h.area JOIN p ON p.area = h.area WHERE h.tot >= 5000 AND p.pop > 0 AND h.hk IS NOT NULL) SELECT q, COUNT(*) AS cities, CAST(ROUND(MIN(mfg_per100), 1) AS VARCHAR) || '〜' || CAST(ROUND(MAX(mfg_per100), 1) AS VARCHAR) || '人' AS band, ROUND(SUM(hk) * 100.0 / SUM(tot), 2) AS dispatch_pct, ROUND(SUM(hk_f) * 100.0 / SUM(hk), 1) AS female_pct FROM j GROUP BY q ORDER BY q
```

```sql id=contrast
WITH h AS (SELECT area, area_name, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '0' THEN value END) AS hk, MAX(CASE WHEN employment_status_code = '12' AND sex_code = '2' THEN value END) AS hk_f, MAX(CASE WHEN employment_status_code = '0' AND sex_code = '0' THEN value END) AS tot FROM e_stat.census.census_municipality_employment_status WHERE area_level IN ('city', 'town_village') GROUP BY 1, 2), pr AS (SELECT DISTINCT LEFT(area, 2) AS pcode, area_name AS pref FROM e_stat.census.census_municipality_employment_status WHERE area_level = 'prefecture'), m AS (SELECT area, value AS mfg FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C3404' AND year = 2020), p AS (SELECT area, value AS pop FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A1101' AND year = 2020) SELECT pr.pref || ' ' || h.area_name AS '市区町村', ROUND(m.mfg * 100.0 / p.pop, 1) AS '人口100人あたり製造業従業者（人）', h.hk AS '派遣社員（人）', ROUND(h.hk * 100.0 / h.tot, 2) AS '就業者に占める割合（%）', ROUND(h.hk_f * 100.0 / h.hk, 1) AS '派遣社員の女性割合（%）' FROM h JOIN pr ON LEFT(h.area, 2) = pr.pcode JOIN m ON m.area = h.area JOIN p ON p.area = h.area WHERE h.area IN ('25384', '22221', '40621', '10524', '23225', '12204', '12207', '12203', '12227', '13208', '13224') ORDER BY m.mfg / p.pop DESC
```
