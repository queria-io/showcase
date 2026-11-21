---
title: 1日500人に満たない駅は13年で乗り降りが3割近く減り、減り始めたのはコロナの前だった
description: 全国6,193駅の乗降客数を2011年度から2024年度まで集計しました。全駅の合計は2024年度に2011年度の100.5%まで戻った一方、2011年度に1日500人未満だった駅の中央値は72.1%で、2019年度の時点ですでに89.7%に減っていました。
ogDescription: 全国6,193駅の乗降客数を2011年度から2024年度まで集計しました。1日500人未満の駅の中央値は、2024年度に2011年度の72.1%です。
publishedAt: 2026-08-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 鉄道
  - 公共交通
  - 出店戦略
  - 国土数値情報
datasets:
  - queria/nlftp
sources:
  - title: 国土数値情報 駅別乗降客数データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-S12-2024.html
    publisher: 国土交通省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2025.html
    publisher: 国土交通省
agentHint: nlftp.railway.station_passenger から、路線名(line_name)に「常磐線」を含む駅の2011年度と2024年度の乗降客数を駅ごとに出して、増減率の大きい順に並べて
socialAnnounce: |-
  全国6,193駅の乗降客数を2011〜2024年度で並べました。合計は2011年度並みに戻る一方、1日500人未満の駅の中央値は72%です。

  駅前の出店候補地の評価に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

全国6,193駅の乗降客数の合計は、2024年度に2011年度の100.5%まで戻りました。駅の規模ごとに見ると、2011年度に1日500人未満だった駅の中央値は2024年度に72.1（2011年度=100）で、3割近く減っています。この階級の駅は、コロナ前の2019年度の時点ですでに89.7まで減っていました。1日1万〜5万人の駅の中央値は101.4で、2011年度を上回っています。

郊外や地方都市で出店候補地を探すとき、駅前は最初に確認する場所の1つで、その駅の1日の利用者数は候補地を絞り込む材料として広く使われています。1年分の利用者数では、その駅の利用者が増えているか減っているかは判断できません。国土交通省が公表している[駅別乗降客数データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-S12-2024.html)を使い、全国の鉄道駅の1日あたり乗降客数を2011年度から2024年度まで集計しました。

## 全駅の合計は、2024年度に2011年度の水準まで戻った

このデータには、鉄道事業者が提供した資料をもとに、駅ごと・年度ごとの1日あたり乗降客数（`passenger_count`）が入っています。国土数値情報の駅データと同じ駅コード（`station_code`）を持ち、事業者名（`operator`）・路線名（`line_name`）・駅の代表点（`geometry`）が付いています。

年度によって公表される駅が変わるため、2011年度から2024年度までの14年度すべてで値がある6,193駅だけを使い、同じ駅で全期間を集計しました。乗降客数の合計の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"total_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "total_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "total_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "6,193駅の合計乗降客数（万人／日）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

2011年度の10,458万人から2019年度には11,569万人まで10.6%増え、2020年度に8,088万人に減り、2024年度は10,508万人まで戻りました。2024年度の水準は2011年度の100.5%、2019年度の90.8%です。

## 1日500人未満の駅は、2011年度から2024年度に3割近く減った

合計は、乗降客数の多い駅の増減の影響を強く受けます。2011年度時点で1日5万人以上だった駅は479駅で、全体の8%に満たない数ですが、1駅あたりの人数が大きいためです。そこで、2011年度の乗降客数で駅を5つの階級に分け、駅ごとに2011年度を100とした指数を計算し、階級ごとに中央値を求めました。

| 階級（2011年度の1日あたり乗降客数） | 駅数  |
| ----------------------------------- | ----- |
| 500人未満                           | 1,906 |
| 500〜2千人                          | 1,197 |
| 2千〜1万人                          | 1,312 |
| 1万〜5万人                          | 1,299 |
| 5万人以上                           | 479   |

乗降客数は各鉄道事業者が独自に算出した値で、事業者をまたいで統一された基準はありません。そのため、駅どうしの水準ではなく、同じ駅の年度ごとの変化を比較しています。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "bands"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"b1\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "b1", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "b1",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011年度=100とした指数（中央値）", "grid": true}
        },
        "color": {
          "datum": "500人未満",
          "type": "nominal",
          "scale": {
            "domain": ["500人未満", "500〜2千人", "2千〜1万人", "1万〜5万人", "5万人以上"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bands"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"b2\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "b2", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "b2",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011年度=100とした指数（中央値）", "grid": true}
        },
        "color": {
          "datum": "500〜2千人",
          "type": "nominal",
          "scale": {
            "domain": ["500人未満", "500〜2千人", "2千〜1万人", "1万〜5万人", "5万人以上"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bands"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"b3\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "b3", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "b3",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011年度=100とした指数（中央値）", "grid": true}
        },
        "color": {
          "datum": "2千〜1万人",
          "type": "nominal",
          "scale": {
            "domain": ["500人未満", "500〜2千人", "2千〜1万人", "1万〜5万人", "5万人以上"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bands"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"b4\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "b4", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "b4",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011年度=100とした指数（中央値）", "grid": true}
        },
        "color": {
          "datum": "1万〜5万人",
          "type": "nominal",
          "scale": {
            "domain": ["500人未満", "500〜2千人", "2千〜1万人", "1万〜5万人", "5万人以上"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bands"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"b5\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "b5", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "b5",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011年度=100とした指数（中央値）", "grid": true}
        },
        "color": {
          "datum": "5万人以上",
          "type": "nominal",
          "scale": {
            "domain": ["500人未満", "500〜2千人", "2千〜1万人", "1万〜5万人", "5万人以上"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 100, "type": "quantitative"}
      }
    }
  ]
}
```

2020年度の減少は5つの階級すべてにあります。階級による違いは、その前と後に出ています。

コロナ前の8年間で減っていたのは、1日500人未満の駅だけでした。2019年度の指数は89.7で、2011年度から1割以上減っています。500〜2千人の駅は100.0で横ばい、2千〜1万人は105.5、1万〜5万人は109.1、5万人以上は109.8で、規模が大きい駅ほど増えていました。

2024年度は、階級による差がさらに大きくなっています。1万〜5万人の駅は101.4で2011年度を上回り、5万人以上は98.7、2千〜1万人は97.7でほぼ元の水準に戻りました。500〜2千人の駅は88.6、500人未満の駅は72.1です。500人未満の駅の中央値は2021年度の69.0が最も低く、その後は2022年度73.5・2023年度72.2・2024年度72.1と、3年間ほとんど変わっていません。他の階級は2022年度以降も上がり続けていますが、この階級は元の水準に戻らないまま横ばいです。

コロナは小さな駅の減少を大きくしましたが、減少はコロナの前から始まっていました。2011年度からの13年で、1日500人未満の駅の中央値は3割近く減っています。

## 2024年度の駅の指数の中央値が2011年度を上回るのは、42都道府県のうち8都道府県

駅の代表点を[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2025.html)の都道府県ポリゴンに重ね、都道府県ごとに2024年度の指数（2011年度=100）の中央値を計算しました。14年度すべてで値がある駅が20に満たない県は、中央値が数駅で決まるため除き、42都道府県を並べています。期間の途中で公表がなかった年がある駅も除いているので、そうした駅の多い県ほど、集計に残った駅だけの値になります。

```chart
{
  "height": 880,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "idx", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "idx",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2024年度の指数（2011年度=100、県内の駅の中央値）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
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
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "idx", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "idx",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2024年度の指数（2011年度=100、県内の駅の中央値）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
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
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "idx", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "idx",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2024年度の指数（2011年度=100、県内の駅の中央値）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
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

100を超えているのは愛知県（111.2）・茨城県（108.4）・北海道（104.5）・東京都（103.3）・千葉県（103.2）・京都府（101.6）・福岡県（101.6）・大阪府（101.0）の8都道府県です。

最も低いのは高知県（59.2）で、福井県（61.4）・佐賀県（67.3）・新潟県（68.0）・徳島県（68.5）が続きます。高知県では166駅の中央値が59.2で、中央値の駅は13年で乗降客数の4割を失った計算になります。最も高い県と低い県で、およそ1.9倍の差があります。

階級別の結果と合わせると、県の中央値は、その県に乗降客数の少ない駅がどれだけ多いかによって決まっていると考えられます。県内の駅に小さな駅が多いほど、県の中央値は低くなります。

## 出店候補地の評価での使い方

現在の乗降客数と一緒に、その駅の14年分の推移を確認すると、候補地の評価が変わります。

- 候補駅の指数を計算する: 対象駅の2011年度と直近年度の比を計算すると、同じ規模の駅と比較して、その駅の増減が大きいか小さいかが分かります。現在の乗降客数が同じ2つの駅でも、2011年度から増えてきた駅と減ってきた駅では、今後見込める客数が違います
- 路線単位で確認する: `line_name` で絞り込むと、路線全体で増えているのか、特定の駅だけが増えているのかを区別できます。路線全体で減っている場合は、駅前の区画より、車で来店する客を前提にした立地を検討する材料になります
- 撤退・改装の優先順位を付ける: 既存店の最寄り駅を一覧にして指数の低い順に並べると、売上にまだ表れていない利用者の減少を先に把握できます
- 出店先の県を絞り込む: 県の中央値が100を下回る県では、駅前型の標準店が想定どおりの売上にならない可能性があります。県の中でどの規模の駅の利用者が増えているかを確認してから、区画を探す順序を決められます

## データの出典

本記事は国土交通省の[国土数値情報 駅別乗降客数データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-S12-2024.html)（2024年度）を2026年8月13日時点で集計しています。数値はすべて年度の1日あたり乗降客数で、元データは各鉄道事業者の提供資料です。都道府県への割り当てには、国土数値情報の[行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2025.html)を使っています。

Queriaは、年度ごとに列が分かれていた元データを1つのテーブルに縦持ちで並べ直し、列名・単位・文字コードを統一して、テーブルと列の説明を付けて公開しています。本記事で使った[駅別乗降客数テーブル](/datasets/queria/nlftp/railway/station_passenger)から、担当エリアの駅を名前で検索して14年分の推移を確認したり、路線ごとに集計したりできます。

```sql id=national
WITH panel AS (SELECT station_code FROM nlftp.railway.station_passenger WHERE year <= 2024 GROUP BY station_code HAVING COUNT(passenger_count) = 14 AND MAX(CASE WHEN year = 2011 THEN passenger_count END) > 0) SELECT s.year, COUNT(*) AS stations, ROUND(CAST(SUM(s.passenger_count) AS DOUBLE) / 10000, 0) AS total_man FROM nlftp.railway.station_passenger s JOIN panel p ON p.station_code = s.station_code WHERE s.passenger_count IS NOT NULL AND s.year <= 2024 GROUP BY s.year ORDER BY s.year
```

```sql id=bands
WITH panel AS (SELECT station_code, MAX(CASE WHEN year = 2011 THEN passenger_count END) AS y11 FROM nlftp.railway.station_passenger WHERE year <= 2024 GROUP BY station_code HAVING COUNT(passenger_count) = 14 AND MAX(CASE WHEN year = 2011 THEN passenger_count END) > 0) SELECT s.year, ROUND(MEDIAN(CASE WHEN p.y11 < 500 THEN CAST(s.passenger_count AS DOUBLE) / p.y11 END) * 100, 1) AS b1, ROUND(MEDIAN(CASE WHEN p.y11 >= 500 AND p.y11 < 2000 THEN CAST(s.passenger_count AS DOUBLE) / p.y11 END) * 100, 1) AS b2, ROUND(MEDIAN(CASE WHEN p.y11 >= 2000 AND p.y11 < 10000 THEN CAST(s.passenger_count AS DOUBLE) / p.y11 END) * 100, 1) AS b3, ROUND(MEDIAN(CASE WHEN p.y11 >= 10000 AND p.y11 < 50000 THEN CAST(s.passenger_count AS DOUBLE) / p.y11 END) * 100, 1) AS b4, ROUND(MEDIAN(CASE WHEN p.y11 >= 50000 THEN CAST(s.passenger_count AS DOUBLE) / p.y11 END) * 100, 1) AS b5, COUNT(*) FILTER (WHERE p.y11 < 500) AS n1, COUNT(*) FILTER (WHERE p.y11 >= 500 AND p.y11 < 2000) AS n2, COUNT(*) FILTER (WHERE p.y11 >= 2000 AND p.y11 < 10000) AS n3, COUNT(*) FILTER (WHERE p.y11 >= 10000 AND p.y11 < 50000) AS n4, COUNT(*) FILTER (WHERE p.y11 >= 50000) AS n5 FROM nlftp.railway.station_passenger s JOIN panel p ON p.station_code = s.station_code WHERE s.passenger_count IS NOT NULL AND s.year <= 2024 GROUP BY s.year ORDER BY s.year
```

```sql id=pref_top
WITH panel AS (SELECT station_code, MAX(CASE WHEN year = 2011 THEN passenger_count END) AS y11, MAX(CASE WHEN year = 2024 THEN passenger_count END) AS y24, ANY_VALUE(geometry) AS geom FROM nlftp.railway.station_passenger WHERE year <= 2024 GROUP BY station_code HAVING COUNT(passenger_count) = 14 AND MAX(CASE WHEN year = 2011 THEN passenger_count END) > 0), pref AS (SELECT b.prefecture_name, COUNT(*) AS n, MEDIAN(CAST(p.y24 AS DOUBLE) / p.y11) * 100 AS idx FROM panel p JOIN nlftp.boundary.prefecture b ON ST_Within(p.geom, b.geometry) GROUP BY b.prefecture_name HAVING COUNT(*) >= 20), ranked AS (SELECT prefecture_name, ROUND(idx, 1) AS idx, n, ROW_NUMBER() OVER (ORDER BY idx DESC, prefecture_name) AS rn FROM pref) SELECT prefecture_name, idx, n FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH panel AS (SELECT station_code, MAX(CASE WHEN year = 2011 THEN passenger_count END) AS y11, MAX(CASE WHEN year = 2024 THEN passenger_count END) AS y24, ANY_VALUE(geometry) AS geom FROM nlftp.railway.station_passenger WHERE year <= 2024 GROUP BY station_code HAVING COUNT(passenger_count) = 14 AND MAX(CASE WHEN year = 2011 THEN passenger_count END) > 0), pref AS (SELECT b.prefecture_name, COUNT(*) AS n, MEDIAN(CAST(p.y24 AS DOUBLE) / p.y11) * 100 AS idx FROM panel p JOIN nlftp.boundary.prefecture b ON ST_Within(p.geom, b.geometry) GROUP BY b.prefecture_name HAVING COUNT(*) >= 20), ranked AS (SELECT prefecture_name, ROUND(idx, 1) AS idx, n, ROW_NUMBER() OVER (ORDER BY idx DESC, prefecture_name) AS rn FROM pref) SELECT prefecture_name, idx, n FROM ranked WHERE rn > 10 AND rn <= 32 ORDER BY rn
```

```sql id=pref_bottom
WITH panel AS (SELECT station_code, MAX(CASE WHEN year = 2011 THEN passenger_count END) AS y11, MAX(CASE WHEN year = 2024 THEN passenger_count END) AS y24, ANY_VALUE(geometry) AS geom FROM nlftp.railway.station_passenger WHERE year <= 2024 GROUP BY station_code HAVING COUNT(passenger_count) = 14 AND MAX(CASE WHEN year = 2011 THEN passenger_count END) > 0), pref AS (SELECT b.prefecture_name, COUNT(*) AS n, MEDIAN(CAST(p.y24 AS DOUBLE) / p.y11) * 100 AS idx FROM panel p JOIN nlftp.boundary.prefecture b ON ST_Within(p.geom, b.geometry) GROUP BY b.prefecture_name HAVING COUNT(*) >= 20), ranked AS (SELECT prefecture_name, ROUND(idx, 1) AS idx, n, ROW_NUMBER() OVER (ORDER BY idx DESC, prefecture_name) AS rn FROM pref) SELECT prefecture_name, idx, n FROM ranked WHERE rn > 32 ORDER BY rn
```
