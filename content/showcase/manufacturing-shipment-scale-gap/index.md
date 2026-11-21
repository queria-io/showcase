---
title: 1事業所あたりの製造品出荷額は山口県の39.0億円が最も多く、出荷額3位の大阪府は37位
description: 2023年の都道府県別の製造品出荷額は愛知県の58.0兆円が最も多く、1事業所あたりの出荷額では山口県の39.0億円が1位です。出荷額3位の大阪府は1事業所あたりでは37位（10.4億円）、東京都は46位（5.6億円）です。
ogDescription: 1事業所あたりの製造品出荷額は山口県の39.0億円が1位で、出荷額3位の大阪府は37位（10.4億円）です。2023年の都道府県別データで集計しました。
publishedAt: 2026-06-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 製造業
  - 工業立地
  - 経済
datasets:
  - queria/e_stat
sources:
  - title: 統計でみる都道府県・市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/
    publisher: 総務省統計局
  - title: 経済構造実態調査
    url: https://www.stat.go.jp/data/kkj/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（C 経済基盤）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/C
    publisher: 総務省統計局
  - title: 経済構造実態調査 調査の概要
    url: https://www.meti.go.jp/statistics/tyo/kkj/gaiyo.html
    publisher: 経済産業省
agentHint: 製造業事業所数(C3403)を都道府県別ランキングで2023年に出して。出荷額(C3401)の順位とどれだけずれるか、事業所が多いのに出荷額が伸びない県を見たい
socialAnnounce: |-
  都道府県別の製造品出荷額・事業所数を分析し、工業の集積度と一事業所あたりの規模の地域差を見ました。

  製造業向けの営業エリア設計や工場立地の検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2023年の製造品出荷額は愛知県の58.0兆円が最も多く、2位の静岡県の約2.9倍です。出荷額を事業所数で割った1事業所あたりの出荷額では、山口県の39.0億円が1位で、大分県（34.0億円）、三重県（31.7億円）が続きます。出荷額3位の大阪府は1事業所あたりでは37位（10.4億円）、出荷額16位の東京都は46位（5.6億円）です。

製造業向けに設備・資材・物流・保守といったサービスを提供する企業は、工場が多い地域をもとに営業エリアや拠点の配置を決めます。工場の数が多い地域と、1つひとつの工場が大きい地域は一致するとは限りません。少数の大規模なプラントが集まる地域と、中小の事業所が数多く集まる地域とでは、営業の進め方も提案する商材も変わります。

この記事では、e-Statの[社会・人口統計体系](https://www.stat.go.jp/data/ssds/)に収録された都道府県別の製造業データを使い、製造品出荷額と、1事業所あたりの出荷額の2つの指標で、工業の地域差を比較します。

## 製造品出荷額は愛知県の58.0兆円が最も多く、静岡県の約2.9倍

この統計の製造業のデータは、[経済構造実態調査](https://www.stat.go.jp/data/kkj/index.html)（製造業）などを出典としており、都道府県別に次の指標が収録されています。

| コード | 指標           | 単位   |
| ------ | -------------- | ------ |
| C3401  | 製造品出荷額等 | 百万円 |
| C3403  | 製造業事業所数 | 事業所 |
| C3404  | 製造業従業者数 | 人     |

2023年の事業所数（`C3403`）と従業者数（`C3404`）は6月1日時点、製造品出荷額等（`C3401`）は暦年の合計です。3つの指標とも[経済構造実態調査の製造業事業所調査](https://www.meti.go.jp/statistics/tyo/kkj/gaiyo.html)の値で、この調査の対象は、法人の製造業事業所のうち産業分類ごとに出荷額の上位9割を占める範囲です。個人経営の事業所は含みません。2023年の値を使い、製造品出荷額等を事業所数で割って「1事業所あたり出荷額」を求めます。まず、47都道府県の製造品出荷額の順位です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "total_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "shipment", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "shipment",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "製造品出荷額等（兆円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "total_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "shipment", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "shipment",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "製造品出荷額等（兆円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "total_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "shipment", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "shipment",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "製造品出荷額等（兆円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

製造品出荷額は愛知県が58.0兆円で最も多く、2位の静岡県（19.8兆円）の約2.9倍です。自動車を中心とする中京工業地帯の生産額の大きさを表しています。以下、大阪府（19.3兆円）、神奈川県（18.5兆円）、兵庫県（18.5兆円）と、太平洋ベルトの大都市圏と臨海工業地帯の府県が続きます。下位は沖縄県（0.5兆円）、高知県（0.7兆円）、鳥取県（0.9兆円）で、上位の県との差は100倍を超えます。

## 1事業所あたりの出荷額は、山口県が39.0億円で1位

製造品出荷額を事業所数で割ると、順位は次のように変わります。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pe_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_estab", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_estab",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "一事業所あたり出荷額（億円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pe_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_estab", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_estab",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "一事業所あたり出荷額（億円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pe_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_estab", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_estab",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "一事業所あたり出荷額（億円）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#22c55e", "#86efac", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

1事業所あたり出荷額の1位は山口県（39.0億円）で、大分県（34.0億円）、三重県（31.7億円）が続きます。いずれも石油化学・鉄鋼・素材といった装置産業のプラントが臨海部にある県で、事業所数は多くないものの、1つひとつの規模が大きい県です。出荷額の総額では17位の山口県が、1事業所あたりでは1位です。

出荷額3位の大阪府は1事業所あたりでは37位（10.4億円）、出荷額16位の東京都は46位（5.6億円）です。2つの都府には中小の事業所が数多く集まっており、出荷額の総額は大きくても、1事業所あたりの規模は小さくなっています。下位には沖縄県（5.2億円）、高知県（5.9億円）が並び、山口県とは約7.5倍の差があります。出荷額1位の愛知県は、1事業所あたりでも4位（31.3億円）です。

この指標は総額を事業所数で割った平均値です。少数の大規模プラントが出荷額の大半を占める県では、県内の事業所の多くを占める中小事業所の規模より大きな値になります。

## 全国の製造品出荷額は2022年に1991年を上回ったが、事業所数は約半分

全国の製造品出荷額の推移を1975年から並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"shipment\"]) ? 0 : 1",
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
          {"field": "shipment", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "shipment",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "製造品出荷額等（兆円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2008, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 2008, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "リーマンショック"}
      }
    }
  ]
}
```

全国の製造品出荷額は、1991年の約341兆円が2019年までの最高で、その後は減少しました。世界金融危機（リーマンショック）では、2008年の約336兆円から2009年の約265兆円へ、1年で約2割減っています。その後は少しずつ回復し、調査が替わった2020年は新型コロナの影響もあって約302兆円に減ったものの、2022年には約362兆円と1991年を上回り、2023年は約373兆円でした。

1991年と2022年では、出荷している事業所の数が違います。1991年の430,414事業所・1,135万人に対し、2022年は222,770事業所・771万人で、事業所数は約半分、従業者数は約3分の2です。約半分の事業所が、名目で6%多い金額を出荷しています。

事業所数は、調査が替わる前から減っています。工業統計が中心だった2019年までの範囲でも、1991年の430,414から2019年の185,116まで57%減りました。この系列は、2019年までが工業統計（2011年と2015年は経済センサス-活動調査）、2020年以降は経済センサス-活動調査（2021年）と経済構造実態調査（それ以外の年）の値で、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/C)には調査対象が異なるため時系列比較には十分な留意が必要と書かれています。2021年から2022年に事業所数は26%増えた一方、従業者数は3.3%増で、調査の違いによる段差があります。1991年と2022年の「約半分」は、この段差を含んだ数字です。

金額は名目値なので、近年の増加には原材料価格の上昇や円安による増加分も含まれると考えられます。離れた年の水準を比較するより、リーマンショックのように短期間で大きく変動した時期を確認するほうが、設備投資や受注の増減を把握する材料になります。

## 営業・立地戦略への活用

このデータは、製造業を顧客とする事業や工場立地の検討に次のように使えます。

- 必要な取引先数の見積もり: 山口県は総額17位ですが1事業所あたりは1位（39.0億円）で、大阪府（10.4億円）と同じ売上規模を目標にするなら、平均で計算した必要な取引先の数は4分の1強です。平均どうしの比なので、訪問先のリストを作る前に、その値が少数の大規模プラントによるものか、県全体の事業所が大きいためかを、企業情報や工業団地の立地で確認します
- 営業体制: 1事業所あたりが大きい県（山口・大分・三重など）は大口の取引先を担当者が継続して訪問する営業、小さい県（大阪・東京など）は多数の取引先に対応する代理店や販路を使う営業と、人員の配置を変えます
- 撤退ラインの設定: 総額と1事業所あたりがどちらも下位の県は、大口・小口のどちらの取引先も少ないと考えられます。専任の担当者を置かずに広域の担当者が受け持つかどうかの判断に使えます

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/)の都道府県別経済データ（`c_pref_economy`）を 2026-08-12 時点で集計しています。製造品出荷額等（`C3401`）・製造業事業所数（`C3403`）・製造業従業者数（`C3404`）のもとになっているのは、2019年までが工業統計（2011年と2015年は経済センサス-活動調査）、2020年以降は総務省統計局・経済産業省の[経済構造実態調査](https://www.stat.go.jp/data/kkj/index.html)と経済センサス-活動調査です。長期推移は1975年から2023年、都道府県別の比較は2023年を対象にしています。

Queriaは、e-Statなどの行政のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[製造業を含む経済基盤テーブル](/datasets/queria/e_stat/ssds/c_pref_economy)から、自社の営業エリアにあたる都道府県の出荷額や1事業所あたりの出荷額を確認できます。

```sql id=total_top
WITH s AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name, ROUND(v / 1000000, 1) AS shipment, ROW_NUMBER() OVER (ORDER BY v DESC, area_name) AS rn FROM s) SELECT area_name, shipment FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=total_mid
WITH s AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name, ROUND(v / 1000000, 1) AS shipment, ROW_NUMBER() OVER (ORDER BY v DESC, area_name) AS rn FROM s) SELECT area_name, shipment FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=total_bottom
WITH s AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name, ROUND(v / 1000000, 1) AS shipment, ROW_NUMBER() OVER (ORDER BY v DESC, area_name) AS rn FROM s) SELECT area_name, shipment FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=pe_top
WITH s AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), n AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3403' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT s.area_name, ROUND(s.v / n.v / 100, 1) AS per_estab, ROW_NUMBER() OVER (ORDER BY s.v / n.v DESC, s.area_name) AS rn FROM s JOIN n ON s.area_name = n.area_name) SELECT area_name, per_estab FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pe_mid
WITH s AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), n AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3403' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT s.area_name, ROUND(s.v / n.v / 100, 1) AS per_estab, ROW_NUMBER() OVER (ORDER BY s.v / n.v DESC, s.area_name) AS rn FROM s JOIN n ON s.area_name = n.area_name) SELECT area_name, per_estab FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pe_bottom
WITH s AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), n AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) v FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3403' AND year = 2023 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT s.area_name, ROUND(s.v / n.v / 100, 1) AS per_estab, ROW_NUMBER() OVER (ORDER BY s.v / n.v DESC, s.area_name) AS rn FROM s JOIN n ON s.area_name = n.area_name) SELECT area_name, per_estab FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=national_trend
SELECT s.year, s.shipment, n.estab, n.workers FROM (SELECT year, ROUND(MAX(TRY_CAST(value AS DOUBLE)) / 1000000, 1) AS shipment FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 GROUP BY year) s LEFT JOIN (SELECT year, ROUND(MAX(CASE WHEN cat01 = 'C3403' THEN TRY_CAST(value AS DOUBLE) END)) AS estab, ROUND(MAX(CASE WHEN cat01 = 'C3404' THEN TRY_CAST(value AS DOUBLE) END)) AS workers FROM e_stat.ssds.c_pref_economy WHERE area_name = '全国' AND cat01 IN ('C3403', 'C3404') GROUP BY year) n ON s.year = n.year ORDER BY s.year
```
