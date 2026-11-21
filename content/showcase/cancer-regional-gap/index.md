---
title: がんで亡くなる割合は2004年から低下 県別の最高は北海道27.1%
description: 死亡に占めるがんの割合は2004年の31.2%を最高に、2023年は24.3%まで下がりました。都道府県別では北海道の27.1%が最も高く、鹿児島県の21.3%が最も低くなっています
publishedAt: 2026-03-06
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 健康
  - がん
  - 地域格差
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 人口動態調査
    url: https://www.mhlw.go.jp/toukei/list/81-1a.html
    publisher: 厚生労働省
  - title: 項目定義 I 健康・医療
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/I
    publisher: 総務省統計局
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 心疾患(I9105)と脳血管疾患(I9106)についても、死亡数(A4200)に占める割合を都道府県別に出して、がんの割合が高い県と低い県で何が入れ替わっているか比べて
socialAnnounce: |-
  がんで亡くなる人は50年で2.81倍に増えましたが、死亡に占める割合は2004年の31.2%を最高に2023年は24.3%まで下がっています。

  都道府県別では北海道が27.1%で最も高く、鹿児島県が21.3%で最も低くなっています
---

2023年に47都道府県でがんで亡くなった人は38万2,419人で、1975年の13万6,281人の2.81倍です。がんは1981年以降、日本の死因の第1位です。

死亡した人のうちがんで亡くなった人の割合は、2023年は24.3%で、最高だった2004年の31.2%より6.9ポイント低い値です。都道府県別に見ると、この割合が最も高いのは北海道の27.1%、最も低いのは鹿児島県の21.3%でした。

## 1975年から2023年に、がんと心疾患の死亡者数は増え、脳血管疾患は減った

e-Stat「社会・人口統計体系」の都道府県別健康データ（`i_pref_health`）から、生活習慣病に関する3つの指標を使います。

| コード | 内容                                   |
| ------ | -------------------------------------- |
| I9102  | 悪性新生物（腫瘍）による死亡者数       |
| I9105  | 心疾患（高血圧性を除く）による死亡者数 |
| I9106  | 脳血管疾患による死亡者数               |

いずれも出典は人口動態調査で、[項目定義 I](https://www.e-stat.go.jp/koumoku/koumoku_teigi/I) の「時点又は期間」は暦年計です。テーブルの `time_name` は「2023年度」と表示されますが、集計されているのは1月から12月までの1年間です。

```chart
{
  "layer": [
    {
      "data": {"name": "deaths_cancer"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"deaths\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "deaths", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "deaths",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "死亡者数（人）", "grid": true}
        },
        "color": {
          "datum": "がん",
          "type": "nominal",
          "scale": {"domain": ["がん", "心疾患", "脳血管疾患"], "range": ["#ef4444", "#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "deaths_heart"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"deaths\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "deaths", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "deaths",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "死亡者数（人）", "grid": true}
        },
        "color": {
          "datum": "心疾患",
          "type": "nominal",
          "scale": {"domain": ["がん", "心疾患", "脳血管疾患"], "range": ["#ef4444", "#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "deaths_cerebro"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"deaths\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "deaths", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "deaths",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "死亡者数（人）", "grid": true}
        },
        "color": {
          "datum": "脳血管疾患",
          "type": "nominal",
          "scale": {"domain": ["がん", "心疾患", "脳血管疾患"], "range": ["#ef4444", "#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

がんは1975年の13万6,281人から2023年の38万2,419人まで増えました。心疾患も9万9,029人から23万1,048人へ増えています。脳血管疾患だけが逆で、1975年の17万4,084人が2023年には10万4,493人まで減りました。

グラフの1995年前後には段差があります。死因簡単分類表は1978年まで第8回、1979年から1994年まで第9回、1995年から第10回の分類が使われています。この切り替えの前後で、心疾患は1993年の17万9,996人から1995年の13万8,972人へ、脳血管疾患は逆に11万8,632人から14万6,362人へ動いています。がんも1994年の24万3,471人から1995年の26万2,799人へ、前後の年より大きく増えました。1995年をまたぐ倍率には、分類の変更による増減が含まれています。

## 死亡に占めるがんの割合は2004年から6.9ポイント下がった

がんの死亡者数が増えたのは、死亡者そのものが増えたからでもあります。同じ49年間で、あらゆる死因を合わせた死亡数は70万262人から157万5,084人へ2.25倍になりました。がんの死亡者数を人口動態調査の死亡数（`A4200`、e-Stat「社会・人口統計体系」の都道府県別人口データ `a_pref_population`）で割り、死亡全体に占めるがんの割合を集計します。

```chart
{
  "layer": [
    {
      "data": {"name": "share_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"cancer_share\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "cancer_share", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "cancer_share",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "死亡に占めるがんの割合（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

1975年に19.5%だった割合は2000年代前半に31%前後まで上がり、最高は2004年の31.2%です。そこからは上下しながら下がって2023年は24.3%で、最高の年との差は6.9ポイントあります。2004年以降は前年より上がった年も何度かあり、6.9ポイントは2004年と2023年の差です。2004年と2023年はどちらも第10回分類のもとの値なので、この6.9ポイントに分類の変更は入りません。

がんの死亡者数は、2004年の32万89人から2023年の38万2,419人へ1.19倍に増えています。同じ期間に死亡数は102万6,610人から157万5,084人へ1.53倍になりました。割合が下がったのは、がん以外の死因による死亡のほうが速く増えたためです。

割合の低下は、新型コロナウイルス感染症の流行より前から続いています。流行前の2019年の時点で、割合は27.3%まで下がっていました。流行期の2022年は、死亡数が前年から9.0%増えて156万8,098人になりました。

## 都道府県別では北海道が27.1%で最も高い

2023年のがん死亡者数を、その都道府県の死亡数で割った割合を47都道府県で並べました。棒は0から描いています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "share_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cancer_share", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "cancer_share",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡に占めるがんの割合（%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#dc2626", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "share_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cancer_share", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "cancer_share",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡に占めるがんの割合（%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#dc2626", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "share_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cancer_share", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "cancer_share",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡に占めるがんの割合（%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#dc2626", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

1位は北海道の27.1%です。福岡県25.6%・大阪府25.5%・神奈川県25.4%・愛知県25.4%が続きます。最下位は鹿児島県の21.3%、その上が長野県21.6%・香川県21.9%でした。最大と最小の比は1.27倍です。

下位10県のうち7県は九州の4県（鹿児島県・大分県・熊本県・宮崎県）と四国の3県（香川県・徳島県・愛媛県）で、残りは長野県・山形県・山梨県です。上位には大都市圏の都府県、下位には九州と四国の県が多く入っています。

この割合と高齢化率の相関係数は−0.527で、高齢化率が高い県ほど割合が低い傾向があります。高齢化が進んだ県では、がん以外の死因が死亡に占める比重が大きくなるためと考えられます。上位に大都市圏が並ぶのはこの傾向どおりです。北海道は高齢化率が33.0%で47都道府県の19番目と平均より高いにもかかわらず、割合は47都道府県で最も高く、この傾向に当てはまりません。

```sql
SELECT * FROM rank_compare
```

## 人口10万人あたりでは秋田県が435.1で最も高い

同じ2023年のがん死亡者数を総人口（`A1101`）で割り、人口10万人あたりの死亡率を地図にしました。地図の境界線は国土数値情報の行政区域データです。

```map
type: map
layers:
  - from: cancer_map
    geojson: geojson
    color: value
    label: pref_name
    name: "がん死亡率（人口10万対）"
lng: 137
lat: 36.5
zoom: 4
```

東北地方と北海道の色が濃くなっています。高いほうは秋田県435.1・青森県426.9・北海道399.3、低いほうは沖縄県231.9・東京都243.3・滋賀県261.3で、最大と最小の比は1.88倍です。

この率は年齢構成を調整していない粗死亡率です。がんで亡くなる人の多くは高齢者なので、高齢者の多い県ほど高くなります。65歳以上人口（`A1303`）が総人口に占める割合と比較します。

```chart
{
  "layer": [
    {
      "data": {"name": "elderly_scatter"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "elderly_rate", "type": "quantitative"},
          {"field": "cancer_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "elderly_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（%）", "grid": true}
        },
        "y": {
          "field": "cancer_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "がん死亡率（人口10万対）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "elderly_scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "elderly_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（%）", "grid": true}
        },
        "y": {
          "field": "cancer_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "がん死亡率（人口10万対）", "grid": true}
        },
        "text": {"field": "pref_name"}
      }
    }
  ]
}
```

```sql
SELECT * FROM correlations
```

47都道府県で相関係数は0.911です。粗死亡率が最も高い秋田県は高齢化率39.1%で47都道府県の最高、粗死亡率が最も低い沖縄県は23.8%、次に低い東京都は22.8%で最低です。人口あたりの死亡率の並びは、ほぼ高齢化率の並びになります。

人口あたりの死亡率で1.88倍の差がある秋田県と沖縄県は、死亡に占めるがんの割合では22.7%と22.5%で、差は0.2ポイントです。

## まとめ

- 2023年に47都道府県でがんで亡くなったのは38万2,419人で、1975年の2.81倍。同じ期間に死亡数全体も2.25倍になった
- 死亡に占めるがんの割合は2004年の31.2%が最高で、2023年は24.3%。差は6.9ポイントで、流行前の2019年の時点ですでに27.3%まで下がっていた
- 都道府県別のこの割合は北海道の27.1%が最も高く、鹿児島県の21.3%が最も低い。上位には大都市圏が入り、下位10県のうち7県は九州と四国の県
- 割合と高齢化率の相関係数は−0.527。北海道は高齢化率が33.0%で47都道府県の19番目と平均より高いが、割合は最も高い
- 総人口で割った死亡率では秋田県435.1・沖縄県231.9で1.88倍開くが、この並びは高齢化率の並びとほぼ同じ（相関0.911）

## データの出典

本記事は総務省統計局[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)の都道府県別データを e-Stat から取得し、2026年9月14日時点で集計しています。死因別死亡者数・死亡数の元データは厚生労働省の[人口動態調査](https://www.mhlw.go.jp/toukei/list/81-1a.html)で、集計期間は暦年です。地図の境界線には国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、e-Statの社会・人口統計体系を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の健康統計テーブル](/datasets/queria/e_stat/ssds/i_pref_health)から、疾患や年次を切り替えて都道府県を比較できます。

```sql id=deaths_cancer
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS deaths FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=deaths_heart
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS deaths FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9105' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=deaths_cerebro
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS deaths FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9106' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=share_trend
WITH c AS ( SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year ), d AS ( SELECT year, SUM(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4200' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year ) SELECT c.year AS year, CAST(c.v AS BIGINT) AS cancer_deaths, CAST(d.v AS BIGINT) AS total_deaths, CAST(ROUND(c.v / d.v * 100, 1) AS DOUBLE) AS cancer_share FROM c JOIN d ON c.year = d.year WHERE c.year BETWEEN 1975 AND 2023 ORDER BY c.year
```

```sql id=cancer_map
WITH cancer AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer_deaths FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), rates AS ( SELECT c.area_name, ROUND(c.cancer_deaths / p.population * 100000, 1) AS cancer_rate FROM cancer c JOIN pop p ON c.area_name = p.area_name ) SELECT r.area_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, r.cancer_rate AS value, ROW_NUMBER() OVER (ORDER BY r.area_name) - 1 AS row_id FROM rates r JOIN nlftp.boundary.prefecture p ON r.area_name = p.prefecture_name
```

```sql id=elderly_scatter
WITH cancer AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer_deaths FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), pop_total AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), pop_elderly AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS elderly FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1303' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) SELECT c.area_name AS pref_name, ROUND(c.cancer_deaths / pt.population * 100000, 1) AS cancer_rate, ROUND(pe.elderly / pt.population * 100, 1) AS elderly_rate FROM cancer c JOIN pop_total pt ON c.area_name = pt.area_name JOIN pop_elderly pe ON c.area_name = pe.area_name
```

```sql id=correlations
WITH c AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS elderly, MAX(CASE WHEN cat01 = 'A4200' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303', 'A4200') AND year = 2023 AND area_name != '全国' GROUP BY area_name ) SELECT COUNT(*) AS prefectures, CAST(ROUND(CORR(c.cancer / p.pop, p.elderly / p.pop), 3) AS DOUBLE) AS corr_crude_vs_elderly, CAST(ROUND(CORR(c.cancer / p.deaths, p.elderly / p.pop), 3) AS DOUBLE) AS corr_share_vs_elderly, CAST(ROUND(MAX(c.cancer / p.pop) / MIN(c.cancer / p.pop), 2) AS DOUBLE) AS crude_max_min_ratio, CAST(ROUND(MAX(c.cancer / p.deaths) / MIN(c.cancer / p.deaths), 2) AS DOUBLE) AS share_max_min_ratio FROM c JOIN p ON c.area_name = p.area_name
```

```sql id=rank_compare
WITH c AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS elderly, MAX(CASE WHEN cat01 = 'A4200' THEN TRY_CAST(value AS DOUBLE) END) AS deaths FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303', 'A4200') AND year = 2023 AND area_name != '全国' GROUP BY area_name ) SELECT c.area_name AS pref_name, CAST(ROUND(c.cancer / p.deaths * 100, 1) AS DOUBLE) AS cancer_share, RANK() OVER (ORDER BY c.cancer / p.deaths DESC) AS share_rank, CAST(ROUND(c.cancer / p.pop * 100000, 1) AS DOUBLE) AS crude_rate, RANK() OVER (ORDER BY c.cancer / p.pop DESC) AS crude_rank, CAST(ROUND(p.elderly / p.pop * 100, 1) AS DOUBLE) AS elderly_rate, RANK() OVER (ORDER BY p.elderly / p.pop DESC) AS elderly_rank FROM c JOIN p ON c.area_name = p.area_name ORDER BY share_rank
```

```sql id=share_top
WITH c AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS deaths FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4200' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), s AS ( SELECT c.area_name AS pref_name, c.cancer / p.deaths * 100 AS v FROM c JOIN p ON c.area_name = p.area_name ), ranked AS ( SELECT pref_name, CAST(ROUND(v, 1) AS DOUBLE) AS cancer_share, ROW_NUMBER() OVER (ORDER BY v DESC, pref_name) AS rn FROM s ) SELECT pref_name, cancer_share FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=share_mid
WITH c AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS deaths FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4200' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), s AS ( SELECT c.area_name AS pref_name, c.cancer / p.deaths * 100 AS v FROM c JOIN p ON c.area_name = p.area_name ), ranked AS ( SELECT pref_name, CAST(ROUND(v, 1) AS DOUBLE) AS cancer_share, ROW_NUMBER() OVER (ORDER BY v DESC, pref_name) AS rn FROM s ) SELECT pref_name, cancer_share FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=share_bottom
WITH c AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS cancer FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I9102' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS deaths FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4200' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), s AS ( SELECT c.area_name AS pref_name, c.cancer / p.deaths * 100 AS v FROM c JOIN p ON c.area_name = p.area_name ), ranked AS ( SELECT pref_name, CAST(ROUND(v, 1) AS DOUBLE) AS cancer_share, ROW_NUMBER() OVER (ORDER BY v DESC, pref_name) AS rn FROM s ) SELECT pref_name, cancer_share FROM ranked WHERE rn > 37 ORDER BY rn
```
