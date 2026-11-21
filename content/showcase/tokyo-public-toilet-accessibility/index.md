---
title: 東京都の公衆トイレのオストメイト対応率は中央値25.0%で、車椅子対応の60.0%を下回る
description: 東京都の25自治体が自治体標準オープンデータセットで公開している公衆トイレ2,851件を集計しました。空欄の意味が自治体によって異なるため、比較できるのは13自治体です。13自治体の設置率の中央値は、車椅子対応60.0%、オストメイト対応25.0%でした
publishedAt: 2026-07-19
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - オープンデータ
  - 東京都
  - バリアフリー
datasets:
  - queria/metro_tokyo
sources:
  - title: 自治体標準オープンデータセット
    url: https://www.digital.go.jp/resources/data_dataset
    publisher: デジタル庁
  - title: 東京都オープンデータカタログサイト
    url: https://portal.data.metro.tokyo.lg.jp/
    publisher: 東京都
agentHint: 乳幼児向け設備(baby_facility)の設置率を自治体(org_title)別に出して、車椅子対応率(wheelchair)との差が大きい自治体を見つけて
socialAnnounce: |-
  東京都25自治体が公開する公衆トイレ2,851件を、バリアフリー設備の記録から数えました。

  「無」と書く自治体と空欄にする自治体が混在し、比較できるのは13自治体。設置率の中央値は車椅子対応60.0%に対しオストメイト対応25.0%でした。
  Queriaは行政のオープンデータを整えて公開しています。
---

東京都の25自治体が公開している公衆トイレ2,851件のうち、設備の記録を自治体どうしで比較できる13自治体では、設置率の中央値は車椅子対応が60.0%、ベビーシート等が36.4%、オストメイト対応が25.0%でした。残る12自治体は、3項目のいずれかで「無」を1件も記録していないので、空欄が「設備なし」なのか「未確認」なのかを判定できず、比較から除きました。

デジタル庁は[自治体標準オープンデータセット](https://www.digital.go.jp/resources/data_dataset)として、自治体が公開を推奨されるデータの様式を定めています。公衆トイレ一覧はその基本編の1つで、所在地や緯度経度に加えて、車椅子での利用可否、ベビーシート等の有無、オストメイト対応の有無といった設備の項目が定義されています。様式が共通なので、複数の自治体のファイルを結合すれば都全体を集計できるはずですが、実際に結合すると、設備の記録方法が自治体によって異なります。この記事では、東京都の自治体が公開した公衆トイレのデータで、バリアフリー設備がどこまで記録されているかと、記録された範囲での設置率を集計します。

## 25自治体の2,851件のうち、車椅子対応が記録されているのは63.3%

公開件数と、各項目が記録されている件数を集計しました。

```sql
SELECT '公表している自治体数' AS 項目, COUNT(DISTINCT org_title) AS 件数 FROM metro_tokyo.ods.public_toilet UNION ALL SELECT '公衆トイレの件数', COUNT(*) FROM metro_tokyo.ods.public_toilet UNION ALL SELECT '緯度経度の記録あり', COUNT(lat) FROM metro_tokyo.ods.public_toilet UNION ALL SELECT '車椅子対応の記録あり', COUNT(wheelchair) FROM metro_tokyo.ods.public_toilet UNION ALL SELECT 'ベビーシート等の記録あり', COUNT(baby_facility) FROM metro_tokyo.ods.public_toilet UNION ALL SELECT 'オストメイト対応の記録あり', COUNT(ostomate) FROM metro_tokyo.ods.public_toilet
```

設備の3項目（`wheelchair`・`baby_facility`・`ostomate`）は真偽値の列なので、`COUNT()` は値が入っている行だけを数えます。

25の自治体が2,851件を公開しています。緯度経度は2,777件（97.4%）に入っており、地図に表示する用途にはほぼ足ります。

設備の項目は記録のない行が多くあります。車椅子対応が記録されているのは1,804件で、全体の63.3%です。ベビーシート等は2,168件（76.0%）、オストメイト対応は2,057件（72.2%）です。記録のない行は、設備がないのか、確認していないだけなのかを、データからは区別できません。

## 設備のない施設を「無」と書く自治体と、空欄にする自治体がある

自治体標準オープンデータセットの様式では、これらの項目は「有」または「無」と書くことになっています。[江戸川区が公開しているファイル](https://www.opendata.metro.tokyo.lg.jp/edogawa/131237_public_toilet.csv)では、設備のない施設には「無」と書かれています。Queriaのテーブルでは「有」を `true`、「無」を `false`、空欄を `NULL` に変換しています。

オストメイト対応の項目について、自治体ごとに「有」「無」「空欄」の件数を集計しました。

```chart
{
  "height": 600,
  "layer": [
    {
      "data": {"name": "rec"},
      "transform": [
        {"fold": ["yes_n", "no_n", "blank_n"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"yes_n\": \"有\", \"no_n\": \"無\", \"blank_n\": \"空欄\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"yes_n\",\"no_n\",\"blank_n\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "org_title",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "公衆トイレ件数（件）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["有", "無", "空欄"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "org_title", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

江戸川区（498件のうち468件）や葛飾区（264件のうち262件）は、ほとんどの行に「有」または「無」が入っています。練馬区は166件のうち28件に「有」が入っているだけで、「無」は1件もありません。新宿区（144件中36件が「有」）、中央区（83件中41件が「有」）も同じです。墨田区（132件）と中野区（124件）には、オストメイト対応の記録が1件もありません。

「無」が1件もない自治体では、空欄が「設備なし」を表すのか「未確認」なのかを判定できません。空欄をすべて「設備なし」とすると、練馬区のオストメイト対応率は16.9%です。空欄を除いて記録のある28件だけで計算すると100%になります。同じデータから、16.9%と100%という大きく異なる値が出ます。

そのため、25自治体すべてを比較することはできません。以降は、車椅子対応・ベビーシート等・オストメイト対応の3項目すべてについて「無」を1件以上記録している13自治体に絞ります。

## 13自治体の設置率の中央値は、車椅子対応60.0%、オストメイト対応25.0%

13自治体について、3項目の設置率を自治体別に集計しました。分母は各項目に「有」または「無」が記録されている件数です。

```chart
{
  "height": 520,
  "layer": [
    {
      "data": {"name": "rates"},
      "transform": [
        {"fold": ["wc_rate", "baby_rate", "osto_rate"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"wc_rate\": \"車椅子対応\", \"baby_rate\": \"ベビーシート等\", \"osto_rate\": \"オストメイト対応\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"wc_rate\",\"baby_rate\",\"osto_rate\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "org_title",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "設置率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["車椅子対応", "ベビーシート等", "オストメイト対応"],
            "range": ["#3b82f6", "#22c55e", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["オストメイト対応", "ベビーシート等", "車椅子対応"]},
        "tooltip": [
          {"field": "org_title", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

13自治体の設置率の中央値は、車椅子対応が60.0%、ベビーシート等が36.4%、オストメイト対応が25.0%です。オストメイト対応は、13自治体の合計でも1,613件中330件で20.5%です。

13自治体のうち12で、車椅子対応の設置率が3項目で最も高くなっています。例外は荒川区で、車椅子対応47.6%に対しベビーシート等が54.9%です。

オストメイト用設備の設置が広く義務付けられたのは、[バリアフリー法](https://www.mlit.go.jp/sogoseisaku/barrierfree/index.html)（2006年施行）以降です。車椅子使用者用の便房はそれ以前から公共建築物の整備対象になっていたので、整備を始めた時期の違いが現在の比率に表れていると考えられます。

オストメイト対応率は、狛江市の65.0%から葛飾区の9.2%まで7倍の差があります。この差には、次の節のとおり、自治体が公衆トイレとして何を収録しているかの違いも含まれます。

## 収録件数が多い自治体ほど、オストメイト対応率が低い傾向がある

公衆トイレとして何を収録するかは、自治体ごとに異なります。公園の小規模なトイレまで収録する自治体もあれば、主要な施設に絞る自治体もあります。収録件数とオストメイト対応率を並べました。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "coverage"},
      "mark": {"type": "point", "color": "#f97316", "filled": true, "size": 121},
      "encoding": {
        "tooltip": [
          {"field": "org_title", "type": "nominal"},
          {"field": "n", "type": "quantitative"},
          {"field": "osto_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "収録件数（件）", "grid": true}
        },
        "y": {
          "field": "osto_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "オストメイト対応率（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "coverage"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "収録件数（件）", "grid": true}
        },
        "y": {
          "field": "osto_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "オストメイト対応率（%）", "grid": true}
        },
        "text": {"field": "org_title"}
      }
    }
  ]
}
```

収録件数が多い自治体ほど設置率が低くなる傾向があります。13自治体での相関係数は-0.35です。

収録件数が200件を超える江戸川区（498件・10.0%）、葛飾区（264件・9.2%）、板橋区（230件・22.6%）は、いずれも設置率が下位です。上位の狛江市（20件・65.0%）、目黒区（20件・25.0%）、国分寺市（11件・27.3%）は収録件数が20件以下です。小規模な公園トイレを多く収録するほど、設備のある施設の比率は下がります。

例外は江東区で、192件を収録しながらオストメイト対応率は54.7%です。収録件数が近い多摩市（176件・13.1%）とは4倍の差があり、収録範囲の違いだけでは説明できません。

収録範囲が自治体ごとに異なるので、この設置率で自治体を順位付けすることはできません。この設置率は、同じ自治体の中で設備の種類ごとの差を比較することや、更新ごとの変化を確認することに使えます。

## オストメイト対応のトイレは、各区の中でほぼ全域にある

13自治体のオストメイト対応トイレを地図にしました。緯度経度は「有」の330件のうち313件、「無」の1,283件のうち1,229件に入っており、残りは地図に表示されません。

```map
type: map
layers:
  - from: map_yes
    lng: lon
    lat: lat
    label: name
    name: "オストメイト対応あり"
  - from: map_no
    lng: lon
    lat: lat
    label: name
    name: "オストメイト対応なし"
lng: 139.68
lat: 35.7
zoom: 9.2
```

13自治体は、江東区・江戸川区・葛飾区・荒川区・板橋区の東部から北部にかけての区と、多摩市・調布市・小平市・国立市・狛江市・国分寺市・東久留米市の多摩地域の市です。

江東区は対応ありが105件、対応なしが87件でほぼ同数です。江戸川区（47件と421件）や葛飾区（24件と238件）では、対応なしの灰色の点が区全体に多く分布しています。

どの区でも、対応ありの点は区内のほぼ全域に分布しており、対応なしの点と分布する範囲は大きく変わりません。区による違いは、対応ありのトイレの密度です。

## まとめ

- 25自治体が2,851件を公開しているが、設備のない施設を「無」と書く自治体と空欄にする自治体があり、3項目すべてで比較できるのは13自治体
- 13自治体の設置率の中央値は、車椅子対応60.0%、ベビーシート等36.4%、オストメイト対応25.0%。13自治体のうち12で車椅子対応が最も高い
- 自治体別のオストメイト対応率は9.2%から65.0%まで差があるが、収録件数との相関係数は-0.35で、公園トイレまで収録するかどうかの違いが含まれている

様式が共通でも、記録の方法と収録範囲は自治体ごとに異なります。複数の自治体のデータを結合する前に、どの行が比較できるかを確認する必要があります。

## データの出典

本記事は、デジタル庁の[自治体標準オープンデータセット](https://www.digital.go.jp/resources/data_dataset)の様式に沿って東京都内の自治体が公開した公衆トイレ一覧を、[東京都オープンデータカタログサイト](https://portal.data.metro.tokyo.lg.jp/)から2026年7月19日時点で取得して集計しています。収録されているのは公表している25自治体の2,851件です。

Queriaは、東京都の自治体標準オープンデータセットを、列名・単位・文字コードを統一し、「有」「無」の表記を真偽値に変換して、テーブルと列の説明を付けて公開しています。本記事で使った[公衆トイレのテーブル](/datasets/queria/metro_tokyo/ods/public_toilet)から、自分の住む自治体の記録状況を確認したり、男女別の便房数や利用時間といったほかの項目を集計したりできます。

```sql id=rec
SELECT org_title, SUM(CASE WHEN ostomate IS TRUE THEN 1 ELSE 0 END) AS yes_n, SUM(CASE WHEN ostomate IS FALSE THEN 1 ELSE 0 END) AS no_n, SUM(CASE WHEN ostomate IS NULL THEN 1 ELSE 0 END) AS blank_n FROM metro_tokyo.ods.public_toilet GROUP BY org_title ORDER BY COUNT(*) DESC
```

```sql id=rates
WITH b AS (SELECT org_title, COUNT(*) AS n, SUM(CASE WHEN wheelchair IS TRUE THEN 1 ELSE 0 END) AS wt, SUM(CASE WHEN wheelchair IS FALSE THEN 1 ELSE 0 END) AS wf, SUM(CASE WHEN baby_facility IS TRUE THEN 1 ELSE 0 END) AS bt, SUM(CASE WHEN baby_facility IS FALSE THEN 1 ELSE 0 END) AS bf, SUM(CASE WHEN ostomate IS TRUE THEN 1 ELSE 0 END) AS ot, SUM(CASE WHEN ostomate IS FALSE THEN 1 ELSE 0 END) AS of_ FROM metro_tokyo.ods.public_toilet GROUP BY org_title) SELECT org_title, ROUND(wt * 100.0 / (wt + wf), 1) AS wc_rate, ROUND(bt * 100.0 / (bt + bf), 1) AS baby_rate, ROUND(ot * 100.0 / (ot + of_), 1) AS osto_rate FROM b WHERE wf > 0 AND bf > 0 AND of_ > 0 ORDER BY osto_rate DESC
```

```sql id=coverage
WITH b AS (SELECT org_title, COUNT(*) AS n, SUM(CASE WHEN wheelchair IS FALSE THEN 1 ELSE 0 END) AS wf, SUM(CASE WHEN baby_facility IS FALSE THEN 1 ELSE 0 END) AS bf, SUM(CASE WHEN ostomate IS TRUE THEN 1 ELSE 0 END) AS ot, SUM(CASE WHEN ostomate IS FALSE THEN 1 ELSE 0 END) AS of_ FROM metro_tokyo.ods.public_toilet GROUP BY org_title) SELECT org_title, n, ROUND(ot * 100.0 / (ot + of_), 1) AS osto_rate FROM b WHERE wf > 0 AND bf > 0 AND of_ > 0 ORDER BY n
```

```sql id=map_yes
WITH b AS (SELECT org_title, SUM(CASE WHEN wheelchair IS FALSE THEN 1 ELSE 0 END) AS wf, SUM(CASE WHEN baby_facility IS FALSE THEN 1 ELSE 0 END) AS bf, SUM(CASE WHEN ostomate IS FALSE THEN 1 ELSE 0 END) AS of_ FROM metro_tokyo.ods.public_toilet GROUP BY org_title) SELECT t.lat, t.lon, t.name FROM metro_tokyo.ods.public_toilet t JOIN b ON b.org_title = t.org_title WHERE b.wf > 0 AND b.bf > 0 AND b.of_ > 0 AND t.ostomate IS TRUE AND t.lat IS NOT NULL
```

```sql id=map_no
WITH b AS (SELECT org_title, SUM(CASE WHEN wheelchair IS FALSE THEN 1 ELSE 0 END) AS wf, SUM(CASE WHEN baby_facility IS FALSE THEN 1 ELSE 0 END) AS bf, SUM(CASE WHEN ostomate IS FALSE THEN 1 ELSE 0 END) AS of_ FROM metro_tokyo.ods.public_toilet GROUP BY org_title) SELECT t.lat, t.lon, t.name FROM metro_tokyo.ods.public_toilet t JOIN b ON b.org_title = t.org_title WHERE b.wf > 0 AND b.bf > 0 AND b.of_ > 0 AND t.ostomate IS FALSE AND t.lat IS NOT NULL
```
