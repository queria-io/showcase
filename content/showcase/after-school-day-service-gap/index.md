---
title: 放課後等デイサービスは、子ども1万人あたりで鹿児島県が東京都の3.6倍ある
description: 全国約20万件の障害福祉サービス等事業所から、放課後等デイサービスの事業所数を都道府県別に集計しました。15歳未満人口1万人あたりの事業所数は、鹿児島県の33.0件から東京都の9.2件まで約3.6倍の差があります。
publishedAt: 2026-07-14
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 障害福祉
  - 子ども
  - 地域格差
datasets:
  - queria/mhlw
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 障害福祉サービス等情報検索（WAM NET）
    url: https://www.wam.go.jp/sfkohyoout/
    publisher: 独立行政法人福祉医療機構
  - title: 社会・人口統計体系 都道府県データ
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures
    publisher: 総務省統計局
agentHint: 都道府県ごとに児童発達支援と放課後等デイサービスの事業所数の比率を出して、未就学児向けが相対的に手厚い県を確かめて
socialAnnounce: |-
  全国20万件の障害福祉サービス等事業所を数えました。

  放課後等デイサービスの供給密度は、15歳未満人口1万人あたり鹿児島県33.0件、東京都9.2件と約3.6倍の開きがあります。
  Queriaは行政のオープンデータを整えて公開しています。
---

全国の障害福祉サービス等事業所のうち、[放課後等デイサービス](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/service/index.html)は25,020件あり、サービス種類別で2番目に多いサービスです。15歳未満人口1万人あたりの事業所数を都道府県別に求めると、最も多い鹿児島県は33.04件、最も少ない東京都は9.23件で、約3.6倍の差があります。九州・沖縄と北海道で多く、関東で少ない傾向があり、未就学児向けの児童発達支援も同じ地域傾向です。

放課後等デイサービスは、障害のある子どもが学校の放課後や長期休暇を過ごす場所で、2012年の児童福祉法改正で制度化されてから事業所が急速に増えました。

## 放課後等デイサービスは、障害福祉サービスで2番目に事業所が多い

使ったのは、厚生労働省の障害福祉サービス等情報公表制度に基づき[独立行政法人福祉医療機構（WAM NET）が公表する事業所情報](https://www.wam.go.jp/sfkohyoout/)から作った障害福祉サービス等事業所データ（`establishment`）です。障害者総合支援法・児童福祉法に基づくサービスを提供する事業所が1レコードずつ入っていて、所在地・緯度経度・法人番号・サービス種類などを持ちます。同じ法人・所在地でも、提供するサービス種類ごとに別のレコードになるので、レコード数は事業所の実数とは一致しません。

レコード数は209,452件、サービス種類は29で、47都道府県すべての事業所が入っています。件数の多いサービス種類の上位は次のとおりです。

```sql
SELECT service_type AS サービス種類, COUNT(*) AS 事業所数 FROM mhlw.shougai.establishment GROUP BY service_type ORDER BY 事業所数 DESC LIMIT 8
```

最も多いのは居宅介護（ホームヘルプ）の25,386件で、放課後等デイサービスが25,020件、重度訪問介護が21,153件、就労継続支援Ｂ型が20,783件と続きます。障害のある子ども向けの通所支援では、放課後等デイサービスと児童発達支援（16,993件）が上位にあります。放課後等デイサービスは主に就学児童（原則6〜18歳）を、児童発達支援は主に未就学児を対象にしています。

以下では放課後等デイサービスに絞って、都道府県の差を比較します。事業所数をそのまま比較すると人口の多い都道府県が上位に来るので、15歳未満人口1万人あたりの事業所数（供給密度）を求めます。15歳未満人口は[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県データ（`a_pref_population`、指標コード `A1301`）の2024年の値です。放課後等デイサービスの対象は就学児童が中心なので、15歳未満人口は規模を統一するための基準として使っています。

## 九州・沖縄と北海道で供給密度が高い

15歳未満人口1万人あたりの放課後等デイサービス事業所数を、都道府県ごとに地図にしました。色が濃いほど供給密度が高い県です。

```map
type: map
layers:
  - from: map_density
    geojson: geojson
    color: density
    label: pref_name
    name: "事業所数 / 15歳未満1万人"
lng: 137
lat: 36.5
zoom: 4
```

九州・沖縄、北海道、近畿の一部で色が濃く、関東・東北・北陸で薄くなっています。

## 最も高い鹿児島県と最も低い東京都で約3.6倍の差がある

47都道府県を供給密度の高い順に並べ、上位10・中間・下位10を色で分けました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "v", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "v",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "事業所数 / 15歳未満人口1万人", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "v", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "v",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "事業所数 / 15歳未満人口1万人", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "v", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "v",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "事業所数 / 15歳未満人口1万人", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
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

上位は鹿児島県（33.04件）、北海道（29.32件）、沖縄県（27.71件）、佐賀県（25.40件）、大阪府（25.02件）です。下位は東京都（9.23件）、新潟県（12.77件）、香川県（12.79件）、長野県（13.51件）、神奈川県（13.85件）です。東京都は15歳未満人口が全国で最も多い一方で、供給密度は最下位です。

供給密度が高い県では、子どもや家庭が選べる事業所が多いことになります。ただし、障害のある子どもの割合や通所の必要性、事業所あたりの定員は地域によって違うので、この値は需要が満たされている度合いではなく、供給体制の厚さの目安として読む必要があります。

## 放課後等デイサービスが多い県は、児童発達支援も多い

都道府県ごとに、放課後等デイサービスと児童発達支援の供給密度（15歳未満人口1万人あたりの事業所数）を散布図にしました。2つのサービスは、同じ事業所が併設していることも少なくありません。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "corr"},
      "mark": {"type": "point", "color": "#f97316", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "jihatsu", "type": "quantitative"},
          {"field": "houday", "type": "quantitative"}
        ],
        "x": {
          "field": "jihatsu",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "児童発達支援 / 15歳未満1万人", "grid": true}
        },
        "y": {
          "field": "houday",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "放課後等デイサービス / 15歳未満1万人", "grid": true}
        }
      }
    }
  ]
}
```

点はおおむね右上がりに並び、放課後等デイサービスの供給密度が高い都道府県は、児童発達支援の供給密度も高い傾向があります。鹿児島県・北海道・沖縄県・大阪府は両方とも右上にあり、東京都は両方とも左下寄りにあります。子ども向け通所支援の事業所の多さは、サービスの種類よりも都道府県ごとの違いとして表れていると考えられます。

## まとめ

- 放課後等デイサービスは25,020件で、障害福祉サービスの中で2番目に事業所が多い
- 15歳未満人口1万人あたりの事業所数は、鹿児島県の33.04件から東京都の9.23件まで約3.6倍の差があり、九州・沖縄と北海道で高く、関東で低い
- 未就学児向けの児童発達支援も同じ地域傾向で、放課後等デイサービスの多い県は児童発達支援も多い

## データの出典

本記事は、厚生労働省の障害福祉サービス等情報公表制度に基づき[独立行政法人福祉医療機構（WAM NET）が公表する事業所情報](https://www.wam.go.jp/sfkohyoout/)を2026年7月14日時点で取得して集計しています。人口には[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県データ（指標コード `A1301`、15歳未満人口）の2024年の値を使いました。

Queriaは、障害福祉サービス等情報公表システムなどの行政のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[障害福祉サービス等事業所テーブル](/datasets/queria/mhlw/shougai/shougai_establishment)から、ほかの都道府県やサービス種類の供給密度を求めたり、緯度経度を使って市区町村ごとに集計したりできます。

```sql id=map_density
WITH est AS (SELECT prefecture_code, COUNT(*) n FROM mhlw.shougai.establishment WHERE service_type = '放課後等デイサービス' GROUP BY 1), pop AS (SELECT LEFT(area, 2) pc, area_name, MAX(TRY_CAST(value AS DOUBLE)) child FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1301' AND year = 2024 AND area_name <> '全国' GROUP BY 1, 2), d AS (SELECT p.area_name, ROUND(e.n / (p.child / 10000.0), 2) v FROM pop p JOIN est e ON p.pc = e.prefecture_code) SELECT b.prefecture_name AS pref_name, ST_AsGeoJSON(b.geometry) AS geojson, d.v AS density FROM nlftp.boundary.prefecture b JOIN d ON b.prefecture_name = d.area_name
```

```sql id=rank_top
WITH est AS (SELECT prefecture_code, COUNT(*) n FROM mhlw.shougai.establishment WHERE service_type = '放課後等デイサービス' GROUP BY 1), pop AS (SELECT LEFT(area, 2) pc, area_name, MAX(TRY_CAST(value AS DOUBLE)) child FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1301' AND year = 2024 AND area_name <> '全国' GROUP BY 1, 2), d AS (SELECT p.area_name, e.n / (p.child / 10000.0) v FROM pop p JOIN est e ON p.pc = e.prefecture_code), ranked AS (SELECT area_name, ROUND(v, 2) v, ROW_NUMBER() OVER (ORDER BY v DESC, area_name) rn FROM d) SELECT area_name, v FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH est AS (SELECT prefecture_code, COUNT(*) n FROM mhlw.shougai.establishment WHERE service_type = '放課後等デイサービス' GROUP BY 1), pop AS (SELECT LEFT(area, 2) pc, area_name, MAX(TRY_CAST(value AS DOUBLE)) child FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1301' AND year = 2024 AND area_name <> '全国' GROUP BY 1, 2), d AS (SELECT p.area_name, e.n / (p.child / 10000.0) v FROM pop p JOIN est e ON p.pc = e.prefecture_code), ranked AS (SELECT area_name, ROUND(v, 2) v, ROW_NUMBER() OVER (ORDER BY v DESC, area_name) rn FROM d) SELECT area_name, v FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH est AS (SELECT prefecture_code, COUNT(*) n FROM mhlw.shougai.establishment WHERE service_type = '放課後等デイサービス' GROUP BY 1), pop AS (SELECT LEFT(area, 2) pc, area_name, MAX(TRY_CAST(value AS DOUBLE)) child FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1301' AND year = 2024 AND area_name <> '全国' GROUP BY 1, 2), d AS (SELECT p.area_name, e.n / (p.child / 10000.0) v FROM pop p JOIN est e ON p.pc = e.prefecture_code), ranked AS (SELECT area_name, ROUND(v, 2) v, ROW_NUMBER() OVER (ORDER BY v DESC, area_name) rn FROM d) SELECT area_name, v FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=corr
WITH pop AS (SELECT LEFT(area, 2) pc, area_name, MAX(TRY_CAST(value AS DOUBLE)) child FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1301' AND year = 2024 AND area_name <> '全国' GROUP BY 1, 2), hou AS (SELECT prefecture_code, COUNT(*) n FROM mhlw.shougai.establishment WHERE service_type = '放課後等デイサービス' GROUP BY 1), jid AS (SELECT prefecture_code, COUNT(*) n FROM mhlw.shougai.establishment WHERE service_type = '児童発達支援' GROUP BY 1) SELECT p.area_name AS pref, ROUND(h.n / (p.child / 10000.0), 2) houday, ROUND(j.n / (p.child / 10000.0), 2) jihatsu FROM pop p JOIN hou h ON p.pc = h.prefecture_code JOIN jid j ON p.pc = j.prefecture_code
```
