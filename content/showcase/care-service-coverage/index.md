---
title: 居宅介護支援は98.6%の市区町村にあり、定期巡回は33.7%にしかない
description: 全国の介護サービス事業所をサービス種類ごとに集計し、事業所がある市区町村の割合を求めました。居宅介護支援は98.6%の市区町村にあり、24時間対応の定期巡回・随時対応は33.7%です。
publishedAt: 2026-07-12
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 介護
  - 高齢者福祉
  - 地域包括ケア
datasets:
  - queria/mhlw
sources:
  - title: 介護サービス情報公表システム オープンデータ
    url: https://www.mhlw.go.jp/stf/kaigo-kouhyou_opendata.html
    publisher: 厚生労働省
agentHint: 介護医療院の県内市区町村カバー率を都道府県別に出して、定期巡回サービスと同じく都市部に集中しているか比べて
socialAnnounce: |-
  全国の介護サービス事業所を、サービス種類ごとに数えました。

  ケアマネジメントは98.6%の市区町村に届く一方、24時間対応の定期巡回は33.7%どまりです。
  Queriaは行政のオープンデータを整えて公開しています。
---

全国の介護事業所がある1,888市区町村のうち、ケアプランを作る居宅介護支援の事業所がある市区町村は98.6%です。訪問介護と特別養護老人ホームも94.1%の市区町村にあります。一方、24時間対応の定期巡回・随時対応型訪問介護看護の事業所がある市区町村は33.7%、夜間対応型訪問介護は7.4%です。定期巡回の事業所がある市区町村の割合を都道府県別に見ると、神奈川県の70.7%から高知県の6.1%まで差があります。

国は、団塊の世代が75歳以上になる2025年に向けて、住まい・医療・介護・生活支援を地域で一体に提供する[地域包括ケアシステム](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/kaigo_koureisha/chiiki-houkatsu/index.html)の構築を進めてきました。この記事では、介護サービス事業所のデータから、サービス種類ごとに事業所がある市区町村の割合を集計します。

## 事業所数が多いのは居宅介護支援・訪問介護・通所介護

使ったのは、厚生労働省の[介護サービス情報公表システム](https://www.mhlw.go.jp/stf/kaigo-kouhyou_opendata.html)から作った介護サービス事業所データ（`establishment`）です。介護保険の対象となるサービスを提供する事業所が1レコードずつ入っていて、所在地・緯度経度・法人番号・サービス種類・定員などを持ちます。同じ法人・所在地でも、提供するサービス種類ごとに別のレコードになるので、レコード数は事業所の実数とは一致しません。

47都道府県すべての事業所が入っていて、市区町村は1,888です（政令指定都市の行政区を1つの市区町村として集計しています）。事業所数の多いサービス種類の上位は次のとおりです。

```sql
SELECT service_type AS サービス種類, COUNT(*) AS 事業所数, COUNT(DISTINCT city_code) AS 市区町村数 FROM mhlw.kaigo.establishment WHERE city_code IS NOT NULL AND city_code <> '' GROUP BY service_type ORDER BY 事業所数 DESC LIMIT 8
```

最も多いのは居宅介護支援（ケアマネジャーがケアプランを作る事業所）の36,491件で、訪問介護が35,191件、通所介護（デイサービス）が24,758件と続きます。表には、事業所数とあわせて事業所がある市区町村の数も載せています。

## 基幹サービスは9割前後の市区町村にあり、新しいサービスは3割前後にとどまる

サービス種類ごとに、事業所が1つ以上ある市区町村の数を1,888で割った割合を「カバー率」と呼びます。代表的な16のサービスを、カバー率の高い順に並べました。市区町村コードが空のレコードは集計から除いています。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "coverage"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__i"}]},
        {
          "calculate": "[\"#3b82f6\",\"#3b82f6\",\"#3b82f6\",\"#3b82f6\",\"#3b82f6\",\"#3b82f6\",\"#93c5fd\",\"#93c5fd\",\"#93c5fd\",\"#93c5fd\",\"#93c5fd\",\"#94a3b8\",\"#94a3b8\",\"#94a3b8\",\"#94a3b8\",\"#94a3b8\"][datum.__i - 1]",
          "as": "__color"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cov", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "cov",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "カバー率（%）", "grid": true}
        },
        "y": {"field": "label", "type": "nominal", "axis": {"title": null}, "sort": null},
        "color": {"field": "__color", "type": "nominal", "scale": null, "legend": null}
      }
    }
  ]
}
```

居宅介護支援（98.6%）、介護老人福祉施設（特養）と訪問介護（ともに94.1%）、通所介護（91.1%）、認知症グループホーム（90.3%）、訪問看護（80.8%）は、8〜9割以上の市区町村にあります。

下位には、制度化が新しいサービスや提供が難しいサービスが並びます。訪問介護と看護を組み合わせて24時間対応する定期巡回・随時対応（33.7%）、医療と介護を一体で提供する介護医療院（29.0%）、訪問看護を組み込んだ看護小規模多機能（28.8%）は、3割前後の市区町村にしかありません。夜間対応型訪問介護は7.4%で、9割以上の市区町村に事業所がありません。在宅の重度者や医療が必要な人を対象にしたサービスほど、事業所がある市区町村が少なくなっています。

## 定期巡回の事業所がある市区町村は、神奈川県で70.7%、高知県で6.1%

[24時間365日の在宅生活を支えるサービス](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/kaigo_koureisha/gaiyo/teikijunkai.html)として地域包括ケアの中心に位置づけられている定期巡回・随時対応について、都道府県ごとに、県内で事業所がある市区町村の割合を求めました。47都道府県を割合の高い順に並べています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "teiki_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cov", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "cov",
          "type": "quantitative",
          "scale": {"domain": [0, 80], "zero": false, "nice": false},
          "axis": {"title": "県内市区町村のカバー率（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "teiki_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cov", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "cov",
          "type": "quantitative",
          "scale": {"domain": [0, 80], "zero": false, "nice": false},
          "axis": {"title": "県内市区町村のカバー率（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "teiki_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "cov", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "cov",
          "type": "quantitative",
          "scale": {"domain": [0, 80], "zero": false, "nice": false},
          "axis": {"title": "県内市区町村のカバー率（%）", "grid": true}
        },
        "y": {"field": "prefecture", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

上位は神奈川県（70.7%）、東京都（70.0%）、兵庫県（67.3%）、埼玉県（63.9%）で、都市部の都府県では県内の7割前後の市区町村に事業所があります。

下位は高知県（6.1%）、徳島県・沖縄県（ともに8.3%）、青森県・和歌山県（ともに10.0%）で、事業所がある市区町村は1割前後です。市町村数の多い北海道も17.6%です。広い面積に集落が点在する地域では、24時間対応の巡回サービスの採算を取りにくいことが背景にあると考えられます。この割合は市区町村の数で求めていて、面積の違いは反映していません。

## まとめ

- 居宅介護支援・訪問介護・通所介護・特養などの基幹サービスは、9割前後の市区町村に事業所がある
- 定期巡回・介護医療院・看護小規模多機能など、在宅の重度者や医療が必要な人向けの新しいサービスは、事業所がある市区町村が3割前後にとどまる
- 定期巡回の事業所がある市区町村の割合は、神奈川県の70.7%から高知県の6.1%まで、都市部で高く地方で低い

## データの出典

本記事は厚生労働省の[介護サービス情報公表システム](https://www.mhlw.go.jp/stf/kaigo-kouhyou_opendata.html)が公開する介護サービス事業所データを、2026年7月12日時点で取得して集計しています。

Queriaは、介護サービス情報公表システムなどの行政のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[介護サービス事業所テーブル](/datasets/queria/mhlw/kaigo/establishment)には市区町村コードと緯度経度も入っているので、特定の市区町村の事業所の一覧を作ったり、サービスが1つもない自治体を抽出したり、事業所の分布を地図で確認したりできます。外部ツールからの接続方法は[ガイド](https://docs.queria.io)にまとめています。自分の地域について詳しく分析したい場合は[お問い合わせ](/contact)からご相談ください。

```sql id=coverage
WITH base AS (SELECT * FROM mhlw.kaigo.establishment WHERE city_code IS NOT NULL AND city_code <> ''), tot AS (SELECT COUNT(DISTINCT city_code) t FROM base) SELECT CASE service_type WHEN '介護老人福祉施設' THEN '介護老人福祉施設(特養)' WHEN '通所介護' THEN '通所介護(デイ)' WHEN '認知症対応型共同生活介護' THEN '認知症グループホーム' WHEN '通所リハビリテーション' THEN '通所リハ' WHEN '介護老人保健施設' THEN '介護老人保健施設(老健)' WHEN '小規模多機能型居宅介護' THEN '小規模多機能' WHEN '認知症対応型通所介護' THEN '認知症デイ' WHEN '特定施設入居者生活介護（有料老人ホーム）' THEN '有料老人ホーム' WHEN '訪問入浴介護' THEN '訪問入浴' WHEN '定期巡回・随時対応型訪問介護看護' THEN '定期巡回・随時対応' WHEN '看護小規模多機能型居宅介護（複合型サービス）' THEN '看護小規模多機能' ELSE service_type END AS label, ROUND(COUNT(DISTINCT city_code) * 100.0 / (SELECT t FROM tot), 1) AS cov FROM base WHERE service_type IN ('居宅介護支援','訪問介護','介護老人福祉施設','通所介護','認知症対応型共同生活介護','訪問看護','通所リハビリテーション','介護老人保健施設','小規模多機能型居宅介護','認知症対応型通所介護','特定施設入居者生活介護（有料老人ホーム）','訪問入浴介護','定期巡回・随時対応型訪問介護看護','介護医療院','看護小規模多機能型居宅介護（複合型サービス）','夜間対応型訪問介護') GROUP BY service_type ORDER BY cov DESC, label
```

```sql id=teiki_top
WITH base AS (SELECT * FROM mhlw.kaigo.establishment WHERE city_code IS NOT NULL AND city_code <> ''), d AS (SELECT prefecture, COUNT(DISTINCT city_code) munis FROM base GROUP BY prefecture), n AS (SELECT prefecture, COUNT(DISTINCT city_code) w FROM base WHERE service_type = '定期巡回・随時対応型訪問介護看護' GROUP BY prefecture), r AS (SELECT d.prefecture, ROUND(COALESCE(n.w, 0) * 100.0 / d.munis, 1) cov, ROW_NUMBER() OVER (ORDER BY ROUND(COALESCE(n.w, 0) * 100.0 / d.munis, 1) DESC, d.prefecture) rn FROM d LEFT JOIN n USING (prefecture)) SELECT prefecture, cov FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=teiki_mid
WITH base AS (SELECT * FROM mhlw.kaigo.establishment WHERE city_code IS NOT NULL AND city_code <> ''), d AS (SELECT prefecture, COUNT(DISTINCT city_code) munis FROM base GROUP BY prefecture), n AS (SELECT prefecture, COUNT(DISTINCT city_code) w FROM base WHERE service_type = '定期巡回・随時対応型訪問介護看護' GROUP BY prefecture), r AS (SELECT d.prefecture, ROUND(COALESCE(n.w, 0) * 100.0 / d.munis, 1) cov, ROW_NUMBER() OVER (ORDER BY ROUND(COALESCE(n.w, 0) * 100.0 / d.munis, 1) DESC, d.prefecture) rn FROM d LEFT JOIN n USING (prefecture)) SELECT prefecture, cov FROM r WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=teiki_bottom
WITH base AS (SELECT * FROM mhlw.kaigo.establishment WHERE city_code IS NOT NULL AND city_code <> ''), d AS (SELECT prefecture, COUNT(DISTINCT city_code) munis FROM base GROUP BY prefecture), n AS (SELECT prefecture, COUNT(DISTINCT city_code) w FROM base WHERE service_type = '定期巡回・随時対応型訪問介護看護' GROUP BY prefecture), r AS (SELECT d.prefecture, ROUND(COALESCE(n.w, 0) * 100.0 / d.munis, 1) cov, ROW_NUMBER() OVER (ORDER BY ROUND(COALESCE(n.w, 0) * 100.0 / d.munis, 1) DESC, d.prefecture) rn FROM d LEFT JOIN n USING (prefecture)) SELECT prefecture, cov FROM r WHERE rn > 37 ORDER BY rn
```
