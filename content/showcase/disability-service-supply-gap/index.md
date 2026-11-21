---
title: 人口あたりの障害福祉サービスの指定件数は、大阪府が東京都の約3倍
description: 全国の障害福祉サービス事業所の指定約20万件を都道府県別に集計しました。人口10万人あたりの指定件数は大阪府の303.8から東京都の100.9まで約3倍、就労継続支援に占めるA型の割合は熊本県の36.8%から東京都の7.5%まで約5倍の差があります
publishedAt: 2026-07-15
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 障害福祉
  - 福祉
  - 地域格差
datasets:
  - queria/mhlw
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 障害福祉サービス等情報公表システム
    url: https://www.wam.go.jp/sfkohyoout/
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 放課後等デイサービスや児童発達支援など児童系サービスの指定件数を都道府県別に、人口10万人あたりで出して。整備量の地域差を見て
socialAnnounce: |-
  全国20万件の障害福祉サービス事業所を、サービス種別・地域別に数えました。

  人口10万人当たりの事業所数は大阪府の303.8から東京都の100.9まで開き、就労支援のA型比率も地域で大きく違います。
  Queriaは行政のオープンデータを整えて公開しています。
---

全国の障害福祉サービス事業所の指定209,452件を都道府県別に人口で割ると、人口10万人あたりの指定件数は大阪府の303.8が最も多く、東京都の100.9が最も少なく、約3倍の差がありました。就労継続支援のうち雇用契約を結ぶA型の割合は、熊本県の36.8%から東京都の7.5%まで約5倍の差があります。

障害福祉サービスは、[障害者総合支援法](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/index.html)や児童福祉法にもとづき、市町村がそれぞれの障害福祉計画・障害児福祉計画で整備を進めています。種別は、ホームヘルプのような訪問系、生活介護や短期入所といった日中活動系、就労継続支援、放課後等デイサービスなどの児童向けサービスまで多岐にわたります。この記事では、全国の事業所データをサービス種別・都道府県別に集計し、自治体の計画担当者やサービスへの参入を検討する事業者が、どの地域でどのサービスが多いか少ないかを確認できるようにします。

## データの概要

厚生労働省の[障害福祉サービス等情報公表システム](https://www.wam.go.jp/sfkohyoout/)から抽出した障害福祉サービス等事業所データ（`establishment`）を使います。障害者総合支援法・児童福祉法にもとづくサービスを提供する事業所が、所在地・緯度経度・法人番号・サービス種別・定員などとともに収録されています。1つの事業所が複数のサービス種別で指定を受けている場合は、種別ごとに別のレコードになります。この記事で集計する「指定件数」は、このサービス種別ごとの指定の数で、事業所の実数より多くなります。

レコード数は209,452件で、47都道府県すべてを含みます。指定件数の多いサービス種別の上位を集計しました。

```sql
SELECT service_type AS サービス種別, COUNT(*) AS 指定件数 FROM mhlw.shougai.establishment GROUP BY 1 ORDER BY 指定件数 DESC LIMIT 15
```

最も多いのは居宅介護（ホームヘルプ）の25,386件で、放課後等デイサービスの25,020件、重度訪問介護の21,153件が続きます。就労継続支援Ｂ型（20,783件）や児童発達支援（16,993件）も上位に入っています。上位は、訪問系のサービスと、放課後等デイサービス・児童発達支援といった児童向けサービスが占めています。

## 指定件数は訪問系が57,397件で最も多く、児童系が46,871件で続く

サービス種別を機能に応じて6つの系統に分けました。ホームヘルプなどの訪問系、生活介護や短期入所の日中活動系、就労継続支援や就労移行支援の就労系、グループホーム（共同生活援助）や施設入所支援の居住系、放課後等デイサービスや児童発達支援の児童系、計画相談支援などの相談系です。この6分類で指定件数を集計しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "categories"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__i"}]},
        {
          "calculate": "[\"#3b82f6\",\"#ec4899\",\"#22c55e\",\"#7c3aed\",\"#f97316\",\"#94a3b8\"][datum.__i - 1]",
          "as": "__color"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "n", "type": "quantitative"}, {"field": "cat", "type": "nominal"}],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "指定件数", "grid": true}
        },
        "y": {"field": "cat", "type": "nominal", "axis": {"title": null}, "sort": null},
        "color": {"field": "__color", "type": "nominal", "scale": null, "legend": null}
      }
    }
  ]
}
```

最も多いのは訪問系の57,397件で、児童系の46,871件が続きます。就労系（30,867件）と相談系（30,384件）はほぼ同じ件数で、日中活動系（24,607件）、居住系（19,326件）の順です。在宅生活のための訪問系が最も多く、児童向けサービスも訪問系に近い件数があります。

## 人口10万人あたりの指定件数は、大阪府の303.8から東京都の100.9まで約3倍の差がある

指定件数は人口の多い地域ほど多くなるので、人口で割って比較します。各都道府県の指定件数を、e-Stat「社会・人口統計体系」の都道府県別人口データ（`a_pref_population`）の総人口（`A1101`、2024年）で割り、人口10万人あたりの指定件数を求めました。値が大きいほど色が濃くなっています。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: value
    label: pref_name
    name: "10万人当たり<br>指定件数"
lng: 137
lat: 36.5
zoom: 4
```

人口10万人あたりの指定件数は大阪府の303.8が最も多く、奈良県（276.5）、鹿児島県（265.0）、沖縄県（258.2）が続きます。西日本や南九州・沖縄の色が濃く、首都圏の色が薄くなっています。東京都は100.9で47都道府県の最下位で、神奈川県（120.6）、埼玉県（125.3）、千葉県（133.7）も下位に入っています。

人口が集中する首都圏では、指定件数は多くても、人口あたりでは少なくなっています。同じ全国制度のサービスでも、人口あたりの指定件数には大阪府と東京都で約3倍の差があります。

## 就労継続支援に占めるA型の割合は、熊本県の36.8%から東京都の7.5%まで約5倍の差がある

就労継続支援には、雇用契約を結び最低賃金が保障される[A型](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/service/shurou_00017.html)と、雇用契約を結ばず作業に応じた工賃を支払うB型があります。全国の指定件数はA型が4,650件、B型が20,783件で、B型はA型の約4.5倍です。就労継続支援のうちA型が占める割合を都道府県別に計算し、47都道府県を高い順に並べました。割合は指定件数で計算しており、定員や実際に働いている人数の割合とは異なります。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "a_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"domain": [0, 40], "zero": false, "nice": false},
          "axis": {"title": "就労継続支援に占めるA型の割合（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "a_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"domain": [0, 40], "zero": false, "nice": false},
          "axis": {"title": "就労継続支援に占めるA型の割合（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "a_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"domain": [0, 40], "zero": false, "nice": false},
          "axis": {"title": "就労継続支援に占めるA型の割合（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

A型の割合が最も高いのは熊本県の36.8%で、石川県・福井県（ともに29.2%）、福岡県（28.0%）が続きます。西日本や北陸では、A型が就労継続支援の3割前後を占めています。低いほうは東京都（7.5%）、秋田県（11.4%）、山形県（11.9%）、神奈川県（12.2%）です。東京都では就労継続支援のうちA型は1割に届かず、大半が雇用契約を結ばないB型です。

## まとめ

- 指定件数は訪問系が最も多く、放課後等デイサービスや児童発達支援といった児童系が訪問系に近い件数で続く
- 人口10万人あたりの指定件数は、大阪府の303.8から東京都の100.9まで約3倍の差がある。首都圏は件数は多いが、人口あたりでは少ない
- 就労継続支援に占めるA型の割合は、熊本県の36.8%から東京都の7.5%まで約5倍の差がある

## データの出典

本記事は厚生労働省の[障害福祉サービス等情報公表システム](https://www.wam.go.jp/sfkohyoout/)が公開する事業所データを、2026年7月15日時点で取得して集計しています。人口あたりの指定件数には総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)にある2024年の総人口（`A1101`）を使い、地図の境界線には国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使いました。

Queriaは、障害福祉サービス等情報公表システムの事業所データを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[障害福祉サービス事業所テーブル](/datasets/queria/mhlw/shougai/establishment)から、自分の地域のサービス種別ごとの指定件数を集計したり、人口データと結合して人口あたりの件数を出したりできます。

```sql id=categories
SELECT CASE WHEN service_type IN ('居宅介護','重度訪問介護','同行援護','行動援護','重度障害者等包括支援') THEN '訪問系' WHEN service_type IN ('生活介護','短期入所','療養介護','自立訓練（生活訓練）','自立訓練（機能訓練）') THEN '日中活動系' WHEN service_type IN ('就労継続支援Ａ型','就労継続支援Ｂ型','就労移行支援','就労定着支援') THEN '就労系' WHEN service_type IN ('共同生活援助','施設入所支援','宿泊型自立訓練','自立生活援助') THEN '居住系' WHEN service_type IN ('放課後等デイサービス','児童発達支援','保育所等訪問支援','居宅訪問型児童発達支援','医療型児童発達支援','福祉型障害児入所施設','医療型障害児入所施設') THEN '児童系' ELSE '相談系' END AS cat, COUNT(*) AS n FROM mhlw.shougai.establishment GROUP BY 1 ORDER BY n DESC
```

```sql id=map_data
WITH est AS (SELECT prefecture_code code, COUNT(*) n FROM mhlw.shougai.establishment GROUP BY 1), pop AS (SELECT LEFT(area,2) code, MAX(value) pop FROM e_stat.ssds.a_pref_population WHERE cat01='A1101' AND year=2024 AND area <> '00000' GROUP BY 1), d AS (SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(est.n/pop.pop*100000,1) AS value FROM nlftp.boundary.prefecture p JOIN est ON p.prefecture_code=est.code JOIN pop ON p.prefecture_code=pop.code) SELECT pref_name, geojson, value, ROW_NUMBER() OVER (ORDER BY pref_name)-1 AS row_id FROM d
```

```sql id=a_top
WITH s AS (SELECT prefecture_code code, COUNT(*) FILTER (WHERE service_type='就労継続支援Ａ型') a, COUNT(*) FILTER (WHERE service_type='就労継続支援Ｂ型') b FROM mhlw.shougai.establishment GROUP BY 1), r AS (SELECT p.prefecture_name AS prefecture, ROUND(100.0*s.a/(s.a+s.b),1) AS ratio, ROW_NUMBER() OVER (ORDER BY 100.0*s.a/(s.a+s.b) DESC, p.prefecture_name) AS rn FROM s JOIN nlftp.boundary.prefecture p ON s.code=p.prefecture_code) SELECT prefecture, ratio FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=a_mid
WITH s AS (SELECT prefecture_code code, COUNT(*) FILTER (WHERE service_type='就労継続支援Ａ型') a, COUNT(*) FILTER (WHERE service_type='就労継続支援Ｂ型') b FROM mhlw.shougai.establishment GROUP BY 1), r AS (SELECT p.prefecture_name AS prefecture, ROUND(100.0*s.a/(s.a+s.b),1) AS ratio, ROW_NUMBER() OVER (ORDER BY 100.0*s.a/(s.a+s.b) DESC, p.prefecture_name) AS rn FROM s JOIN nlftp.boundary.prefecture p ON s.code=p.prefecture_code) SELECT prefecture, ratio FROM r WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=a_bottom
WITH s AS (SELECT prefecture_code code, COUNT(*) FILTER (WHERE service_type='就労継続支援Ａ型') a, COUNT(*) FILTER (WHERE service_type='就労継続支援Ｂ型') b FROM mhlw.shougai.establishment GROUP BY 1), r AS (SELECT p.prefecture_name AS prefecture, ROUND(100.0*s.a/(s.a+s.b),1) AS ratio, ROW_NUMBER() OVER (ORDER BY 100.0*s.a/(s.a+s.b) DESC, p.prefecture_name) AS rn FROM s JOIN nlftp.boundary.prefecture p ON s.code=p.prefecture_code) SELECT prefecture, ratio FROM r WHERE rn > 37 ORDER BY rn
```
