---
title: 昼より夜にトラックが多い高速道路の地点は全国の21.9%で、東京・大阪の周りにはほとんどない
description: 道路交通センサスの時間帯別交通量で、全国の高速道路の観測地点ごとに大型車を昼と夜に分けて集計しました。夜のほうが多い地点は1,388地点のうち304地点（21.9%）で、新東名高速道路は夜のトラックが昼の約2倍です。東京都・埼玉県・千葉県・大阪府では154地点のうち5地点でした。
publishedAt: 2026-10-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 道路交通センサス
  - 物流
  - 高速道路
  - 中継輸送
datasets:
  - queria/mlit
sources:
  - title: 令和3年度 全国道路・街路交通情勢調査（道路交通センサス）
    url: https://www.mlit.go.jp/road/census/r3/
    publisher: 国土交通省
agentHint: 高速自動車国道の東名高速道路と新東名高速道路について、24時間観測した地点ごとに大型車の昼（7時台〜18時台）と夜（19時台〜翌6時台）の台数と夜昼比を出して、都道府県別に並べて比べて
socialAnnounce: |-
  全国の高速道路の観測地点ごとに、トラックを昼と夜に分けて数えました。

  夜のほうが多い地点は全国の2割で、東京・大阪の周りにはほとんどありません。
  中継輸送の拠点選びに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

全国の高速自動車国道で24時間観測した1,388地点のうち、大型車が昼より夜に多く通った地点は304地点（21.9%）でした。夜のほうが多い地点は静岡県、長野県・新潟県・富山県・福井県、福島県、岡山県から山口県の山陽自動車道の沿線に多く、東京都・埼玉県・千葉県・大阪府では154地点のうち5地点です。路線別では、新東名高速道路の夜の大型車が昼の1.94倍でした。

長距離のトラック輸送では、ドライバーの労働時間の上限が厳しくなったことを受けて、途中の拠点で荷物や車両を引き継ぐ中継輸送の拠点が各地で作られています。拠点の候補地を選ぶ物流会社の担当者には、どの区間を何時ごろ何台のトラックが通っているかの情報が必要です。国土交通省の[道路交通センサス](https://www.mlit.go.jp/road/census/r3/)（令和3年度・2021年）の時間帯別交通量を使い、全国の高速道路の観測地点ごとに、大型車を昼と夜に分けて集計しました。

## 深夜の高速道路は、通る車の8割以上が大型車

道路交通センサスの一般交通量調査は、高速道路・一般国道・都道府県道などの区間ごとに、平日1日の交通量を1時間ごとに集計しています。車はナンバープレートの分類で小型車と大型車の2つに分けられ、大型車には大型のトラックのほかバスも含まれます。Queria では、この時間帯別の値を `traffic_census_hourly`（1行 = 調査の単位区間 × 上下 × 車種 × 時間帯）、区間の路線名や形状を `traffic_census_section` に収めています。

調査の1日は朝7時台に始まり、翌朝6時台に終わります。ここでは7時台から18時台を「昼」、19時台から翌6時台を「夜」と呼びます。夜の交通量は24時間観測した地点にしかないので、以下は24時間観測した地点だけを使います。観測した日は高速道路では2021年9月から11月の平日で、上りと下りは合算しています。この記事で「高速道路」と呼ぶのは高速自動車国道で、首都高速や阪神高速などの都市高速道路は含めていません。

下の図は、通った車のうち大型車が何%かを、時間帯ごとに道路の種類別に出したものです。

```chart caption="時間帯ごとの大型車の割合（24時間観測した地点の合計、2021年）"
{
  "layer": [
    {
      "data": {"name": "hourly_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour_label\"]) && isValid(datum[\"expressway\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "hour_label", "type": "nominal"},
          {"field": "expressway", "type": "quantitative"}
        ],
        "x": {
          "field": "hour_label",
          "type": "nominal",
          "axis": {"title": "時間帯（7時台から翌6時台）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "expressway",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大型車の割合（%）", "grid": true}
        },
        "color": {
          "datum": "高速自動車国道",
          "type": "nominal",
          "scale": {
            "domain": ["高速自動車国道", "一般国道", "都道府県道"],
            "range": ["#3b82f6", "#f97316", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "hourly_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour_label\"]) && isValid(datum[\"national\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "hour_label", "type": "nominal"},
          {"field": "national", "type": "quantitative"}
        ],
        "x": {
          "field": "hour_label",
          "type": "nominal",
          "axis": {"title": "時間帯（7時台から翌6時台）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "national",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大型車の割合（%）", "grid": true}
        },
        "color": {
          "datum": "一般国道",
          "type": "nominal",
          "scale": {
            "domain": ["高速自動車国道", "一般国道", "都道府県道"],
            "range": ["#3b82f6", "#f97316", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "hourly_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour_label\"]) && isValid(datum[\"prefectural\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "hour_label", "type": "nominal"},
          {"field": "prefectural", "type": "quantitative"}
        ],
        "x": {
          "field": "hour_label",
          "type": "nominal",
          "axis": {"title": "時間帯（7時台から翌6時台）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "prefectural",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大型車の割合（%）", "grid": true}
        },
        "color": {
          "datum": "都道府県道",
          "type": "nominal",
          "scale": {
            "domain": ["高速自動車国道", "一般国道", "都道府県道"],
            "range": ["#3b82f6", "#f97316", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

高速自動車国道では、大型車の割合が昼の時間帯は24〜37%で、夜遅くなるにつれて上がり、2時台には84.7%になります。深夜の高速道路を走る車の8割以上は大型車です。一般国道でも3時台に57.7%まで上がり、深夜には大型車が小型車を上回ります。都道府県道は3時台でも32.0%にとどまります。

## 大型車が最も多く通るのは、東京都では10時台、静岡県では23時台

大型車の割合は小型車の台数によっても変わるので、この図だけではトラックの台数が夜に多いかどうかは判断できません。そこで、大型車の台数だけを時間帯ごとに集計しました。

下の図は、都県内の高速道路の観測地点で、その日に通った大型車のうち何%がその時間帯に通ったかを、首都圏の東京都、九州の福岡県、その間にある静岡県で比較したものです。

```chart caption="1日の大型車のうち、各時間帯に通った割合（高速自動車国道、2021年）"
{
  "layer": [
    {
      "data": {"name": "pref_profile"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour_label\"]) && isValid(datum[\"tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "hour_label", "type": "nominal"},
          {"field": "tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "hour_label",
          "type": "nominal",
          "axis": {"title": "時間帯（7時台から翌6時台）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "tokyo",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1日の大型車に占める割合（%）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {"domain": ["東京都", "静岡県", "福岡県"], "range": ["#94a3b8", "#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pref_profile"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour_label\"]) && isValid(datum[\"shizuoka\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "hour_label", "type": "nominal"},
          {"field": "shizuoka", "type": "quantitative"}
        ],
        "x": {
          "field": "hour_label",
          "type": "nominal",
          "axis": {"title": "時間帯（7時台から翌6時台）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "shizuoka",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1日の大型車に占める割合（%）", "grid": true}
        },
        "color": {
          "datum": "静岡県",
          "type": "nominal",
          "scale": {"domain": ["東京都", "静岡県", "福岡県"], "range": ["#94a3b8", "#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pref_profile"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour_label\"]) && isValid(datum[\"fukuoka\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "hour_label", "type": "nominal"},
          {"field": "fukuoka", "type": "quantitative"}
        ],
        "x": {
          "field": "hour_label",
          "type": "nominal",
          "axis": {"title": "時間帯（7時台から翌6時台）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "fukuoka",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1日の大型車に占める割合（%）", "grid": true}
        },
        "color": {
          "datum": "福岡県",
          "type": "nominal",
          "scale": {"domain": ["東京都", "静岡県", "福岡県"], "range": ["#94a3b8", "#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

東京都と福岡県では、大型車が最も多く通るのは10時台で、深夜2時台に最も少なくなります。静岡県では反対に、最も多いのは23時台、最も少ないのは朝の8時台です。同じ高速道路網でも、トラックが主に昼に走る地域と、主に夜に走る地域があります。

## 夜のほうが多い地点は、大都市の間の区間に多い

観測地点ごとに、夜に通った大型車の台数を昼の台数で割った値（以下「夜昼比」）を出しました。1を超える地点は、トラックが昼より夜に多く通っています。全国の高速自動車国道で24時間観測した1,388地点のうち、夜昼比が1を超えたのは304地点（21.9%）でした。

下の地図は、その1,388地点を夜昼比で色分けしたものです。色が濃いほど夜のほうが多い地点です。点は観測した区間の中心に置いています。

```map
type: map
caption: "高速自動車国道の観測地点ごとの夜昼比（夜の大型車 ÷ 昼の大型車、2021年）"
layers:
  - from: units
    lng: lng
    lat: lat
    color: night_day_ratio
    label: route_name
lng: 136.5
lat: 36.5
zoom: 4.3
```

夜昼比の高い地点は、新東名高速道路が通る静岡県、長野県・新潟県・富山県・福井県、東北自動車道が通る福島県、岡山県から山口県へ続く山陽自動車道の沿線に並んでいます。東京都・埼玉県・千葉県・大阪府では、夜昼比が1を超えた地点は4都府県の154地点のうち5地点にとどまります。

都道府県ごとに、夜に通った大型車の合計を昼の合計で割ると、静岡県は1.46で、夜のトラックが昼の1.5倍近く通っています。山口県1.19、広島県1.17、長野県1.12、岡山県1.10と続きます。反対に東京都は0.57、大阪府は0.55、福岡県は0.63で、夜のトラックは昼の6割前後です。九州・北海道・四国・沖縄の各県では、夜昼比が1を超えた地点は福岡県の1地点だけでした。

東京都・大阪府・福岡県の周りでは、トラックは主に昼に走ります。夜昼比の高い県の多くは、大都市どうしを結ぶ路線の途中にあります。夕方に大都市を出たトラックが夜のうちに途中の区間を通り、朝に目的地の近くに着く運行が多いと考えられます。名古屋の南を通る伊勢湾岸自動車道は21地点のうち18地点で夜のほうが多く、大都市の近くでも夜のほうが多い区間はあります。

夜昼比は昼と比較した夜の台数の比で、夜に通る台数とは別の値です。夜に通った大型車の台数を県ごとに合計すると、最も多いのは愛知県（全国の10.7%）で、静岡県（9.6%）、埼玉県（5.9%）が続きます。夜昼比が0.79の愛知県や0.55の埼玉県でも、夜に通るトラックの台数は多くなっています。

## 路線で見ると、新東名は夜のトラックが昼の約2倍

下の図は、24時間観測した地点が20以上ある路線について、路線全体の夜昼比を並べたものです。

```chart caption="路線ごとの夜昼比（高速自動車国道、24時間観測した地点が20以上の路線、2021年）"
{
  "layer": [
    {
      "data": {"name": "route_ratio"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "night_day_ratio", "type": "quantitative"},
          {"field": "route_name", "type": "nominal"}
        ],
        "x": {
          "field": "night_day_ratio",
          "type": "quantitative",
          "scale": {"domain": [0, 2.3], "zero": false, "nice": false},
          "axis": {"title": "夜昼比（夜の大型車 ÷ 昼の大型車）", "grid": true}
        },
        "y": {
          "field": "route_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"name": "route_ratio"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "night_day_ratio",
          "type": "quantitative",
          "scale": {"domain": [0, 2.3], "zero": false, "nice": false},
          "axis": {"title": "夜昼比（夜の大型車 ÷ 昼の大型車）", "grid": true}
        },
        "y": {
          "field": "route_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "text": {"field": "label"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

路線名は道路交通センサスの表記で、たとえば中央自動車道西宮線は一般に中央道、九州縦貫自動車道鹿児島線宮崎線は九州道・宮崎道と呼ばれる路線です。棒の右の数字は「夜のほうが多かった地点数 / 24時間観測した地点数」です。新東名高速道路は夜昼比が1.94で、夜のトラックが昼の約2倍通っています。24地点のうち22地点で夜のほうが多くなりました。長野県を通る中央自動車道西宮線は35地点のうち30地点、山陽自動車道は67地点のうち53地点、伊勢湾岸自動車道は21地点のうち18地点で夜のほうが多くなっています。

同じ東京と名古屋を結ぶ道でも、東名高速道路は夜昼比が0.93で、夜のほうが多い地点は54地点のうち12地点です。常磐自動車道（45地点）と九州縦貫自動車道鹿児島線宮崎線（47地点）は、夜のほうが多い地点がそれぞれ0地点と1地点でした。

一般国道でも、一部の地点で夜のほうが多くなっています。一般国道で24時間観測した3,170地点のうち、夜昼比が1を超えたのは14地点で、そのうち6地点が岡山県・広島県を通る国道2号でした。

## 拠点計画での使い方

- 中継輸送の拠点や大型車の休憩施設の候補地を比較するとき、候補地の近くの観測地点で、大型車が昼と夜のどちらに多いかを確認できます。夜昼比の高い区間の近くに拠点を置くなら、拠点の運営者は夜間に大型車を受け入れる駐車スペースと人員を用意することになると見込めます
- 2つの大都市を結ぶ路線で拠点を置く位置を探すとき、上の地図でその路線の点を端から順に見ると、夜のトラックが昼を上回り始める区間が分かります
- 一般国道で夜のほうが多い地点は全国で14地点と少ないものの、国道2号の岡山県・広島県の区間のように、夜のトラックが昼を上回る一般道の区間を候補地の周りで探せます

## データの出典

本記事は国土交通省の[令和3年度 全国道路・街路交通情勢調査（道路交通センサス）](https://www.mlit.go.jp/road/census/r3/)の一般交通量調査を、2026年10月25日時点で集計しています。値は地点ごとに観測した平日1日の交通量で、24時間観測した地点の観測日は大半が2021年9月から12月です。

道路交通センサスの時間帯別交通量は都道府県ごとに配布されています。Queriaは全国分の表を1つのテーブルにまとめて列名を統一し、区間の形状と各列の説明を付けて公開しています。本記事で使った[時間帯別交通量のテーブル](/datasets/queria/mlit/road/traffic_census_hourly)と[区間ごとの交通量のテーブル](/datasets/queria/mlit/road/traffic_census_section)から、自社の拠点の候補地に近い区間で、何時ごろに何台の大型車が通っているかを確認できます。

```sql id=hourly_share
-- 道路の種類ごと・時間帯ごとの大型車の割合。24時間観測した地点だけを使う
WITH h AS (
  SELECT
    CASE
      WHEN road_type_code = 1 THEN 'expressway'
      WHEN road_type_code = 3 THEN 'national'
      ELSE 'prefectural'
    END AS grp,
    hour,
    hour_order,
    SUM(volume) FILTER (WHERE vehicle_type = '大型車') AS large,
    SUM(volume) AS total
  FROM mlit.road.traffic_census_hourly
  WHERE observation_type = '観測'
    AND observation_hours_code = 2
    AND road_type_code IN (1, 3, 4, 6)
  GROUP BY ALL
)
SELECT
  hour_order,
  hour || '時台' AS hour_label,
  ROUND(100.0 * SUM(large) FILTER (WHERE grp = 'expressway') / SUM(total) FILTER (WHERE grp = 'expressway'), 1) AS expressway,
  ROUND(100.0 * SUM(large) FILTER (WHERE grp = 'national') / SUM(total) FILTER (WHERE grp = 'national'), 1) AS national,
  ROUND(100.0 * SUM(large) FILTER (WHERE grp = 'prefectural') / SUM(total) FILTER (WHERE grp = 'prefectural'), 1) AS prefectural
FROM h
GROUP BY hour_order, hour
ORDER BY hour_order
```

```sql id=pref_profile
-- 都県内の高速自動車国道で、1日の大型車のうち各時間帯に通った割合
WITH h AS (
  SELECT prefecture_code, hour, hour_order, SUM(volume) AS large
  FROM mlit.road.traffic_census_hourly
  WHERE road_type_code = 1
    AND observation_type = '観測'
    AND observation_hours_code = 2
    AND vehicle_type = '大型車'
    AND prefecture_code IN ('13', '22', '40')
  GROUP BY ALL
),
p AS (
  SELECT *, 100.0 * large / SUM(large) OVER (PARTITION BY prefecture_code) AS pct
  FROM h
)
SELECT
  hour_order,
  hour || '時台' AS hour_label,
  ROUND(MAX(pct) FILTER (WHERE prefecture_code = '13'), 2) AS tokyo,
  ROUND(MAX(pct) FILTER (WHERE prefecture_code = '22'), 2) AS shizuoka,
  ROUND(MAX(pct) FILTER (WHERE prefecture_code = '40'), 2) AS fukuoka
FROM p
GROUP BY hour_order, hour
ORDER BY hour_order
```

```sql id=units
-- 高速自動車国道の観測地点（調査の単位区間）ごとの昼と夜の大型車。上下は合算
WITH h AS (
  SELECT
    pref_city_code,
    survey_unit_id,
    ANY_VALUE(prefecture_code) AS prefecture_code,
    SUM(volume) FILTER (WHERE vehicle_type = '大型車' AND is_daytime_12h) AS day_large,
    SUM(volume) FILTER (WHERE vehicle_type = '大型車' AND NOT is_daytime_12h) AS night_large
  FROM mlit.road.traffic_census_hourly
  WHERE road_type_code = 1
    AND observation_type = '観測'
    AND observation_hours_code = 2
  GROUP BY pref_city_code, survey_unit_id
),
s AS (
  SELECT
    traffic_pref_city_code,
    traffic_survey_unit_id,
    MIN(route_name) AS route_name,
    ST_Centroid(ST_Union_Agg(geometry)) AS c
  FROM mlit.road.traffic_census_section
  WHERE road_type_code = 1 AND geometry IS NOT NULL
  GROUP BY traffic_pref_city_code, traffic_survey_unit_id
)
SELECT
  h.pref_city_code || '-' || h.survey_unit_id AS unit_id,
  h.prefecture_code,
  s.route_name,
  CAST(h.day_large AS DOUBLE) AS day_large,
  CAST(h.night_large AS DOUBLE) AS night_large,
  ROUND(CAST(h.night_large AS DOUBLE) / h.day_large, 2) AS night_day_ratio,
  ROUND(ST_X(s.c), 6) AS lng,
  ROUND(ST_Y(s.c), 6) AS lat
FROM h
JOIN s
  ON h.pref_city_code = s.traffic_pref_city_code
  AND h.survey_unit_id = s.traffic_survey_unit_id
WHERE h.day_large > 0
ORDER BY unit_id
```

```sql id=pref_night_volume
-- 県ごとの夜の大型車の台数と全国に占める割合（プロットはしない）
SELECT
  prefecture_code,
  SUM(night_large) AS night_large,
  ROUND(100.0 * SUM(night_large) / SUM(SUM(night_large)) OVER (), 1) AS night_large_pct
FROM units
GROUP BY prefecture_code
ORDER BY night_large DESC, prefecture_code
```

```sql id=summary
-- 本文の地点数（プロットはしない）
SELECT
  COUNT(*) AS units,
  SUM(CASE WHEN night_large > day_large THEN 1 ELSE 0 END) AS night_more,
  ROUND(100.0 * SUM(CASE WHEN night_large > day_large THEN 1 ELSE 0 END) / COUNT(*), 1) AS night_more_pct
FROM units
```

```sql id=pref_ratio
-- 都道府県ごとの夜昼比（プロットはしない）
SELECT
  prefecture_code,
  COUNT(*) AS units,
  SUM(CASE WHEN night_large > day_large THEN 1 ELSE 0 END) AS night_more,
  ROUND(SUM(night_large) / SUM(day_large), 2) AS night_day_ratio
FROM units
GROUP BY prefecture_code
ORDER BY night_day_ratio DESC, prefecture_code
```

```sql id=route_ratio
-- 24時間観測した地点が20以上ある路線の夜昼比
SELECT
  route_name,
  COUNT(*) AS units,
  SUM(CASE WHEN night_large > day_large THEN 1 ELSE 0 END) AS night_more,
  ROUND(SUM(night_large) / SUM(day_large), 2) AS night_day_ratio,
  SUM(CASE WHEN night_large > day_large THEN 1 ELSE 0 END) || ' / ' || COUNT(*) AS label,
  CASE WHEN SUM(night_large) > SUM(day_large) THEN '#ef4444' ELSE '#94a3b8' END AS color
FROM units
GROUP BY route_name
HAVING COUNT(*) >= 20
ORDER BY night_day_ratio DESC, route_name
```

```sql id=national_night
-- 一般国道で夜の大型車が昼を上回った地点（プロットはしない）
WITH h AS (
  SELECT
    pref_city_code,
    survey_unit_id,
    ANY_VALUE(route_number) AS route_number,
    ANY_VALUE(prefecture_code) AS prefecture_code,
    SUM(volume) FILTER (WHERE vehicle_type = '大型車' AND is_daytime_12h) AS day_large,
    SUM(volume) FILTER (WHERE vehicle_type = '大型車' AND NOT is_daytime_12h) AS night_large
  FROM mlit.road.traffic_census_hourly
  WHERE road_type_code = 3
    AND observation_type = '観測'
    AND observation_hours_code = 2
  GROUP BY pref_city_code, survey_unit_id
)
SELECT
  COUNT(*) AS units,
  SUM(CASE WHEN night_large > day_large THEN 1 ELSE 0 END) AS night_more,
  SUM(CASE WHEN night_large > day_large AND route_number = '2' THEN 1 ELSE 0 END) AS night_more_route2,
  STRING_AGG(DISTINCT CASE WHEN night_large > day_large AND route_number = '2' THEN prefecture_code END, ',') AS route2_prefs
FROM h
WHERE day_large > 0
```

```sql id=observation_dates
-- 24時間観測した地点の観測月（プロットはしない）
SELECT
  road_type_code,
  observation_date // 100 AS observation_month,
  COUNT(DISTINCT pref_city_code || '-' || survey_unit_id) AS units
FROM mlit.road.traffic_census_hourly
WHERE observation_type = '観測'
  AND observation_hours_code = 2
GROUP BY ALL
ORDER BY road_type_code, observation_month
```
