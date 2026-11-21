---
title: 有効求人倍率が1倍前後でも、埼玉・千葉・神奈川は就職の3割が県外、北海道は4.9%
description: 2024年度の有効求人倍率は東京都の1.76倍から神奈川県の0.91倍まで開きがあります。1倍前後の県のうち、埼玉・千葉・神奈川は就職の約3割が他県で、北海道・沖縄は1割未満です。都道府県の順位は2015年度から安定しています。
publishedAt: 2026-06-16
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 労働
  - 採用
  - 有効求人倍率
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 一般職業紹介状況（職業安定業務統計）
    url: https://www.mhlw.go.jp/toukei/list/114-1.html
    publisher: 厚生労働省
  - title: 一般職業紹介状況（令和7年3月分及び令和6年度分）
    url: https://www.mhlw.go.jp/stf/newpage_57261.html
    publisher: 厚生労働省
  - title: 賃金構造基本統計調査
    url: https://www.mhlw.go.jp/toukei/list/chinginkouzou.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系 Ｆ 労働
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010106
    publisher: 総務省統計局
agentHint: 就職件数（F3105）に占める他県への就職件数（F310603）の割合を47都道府県すべてで出して、有効求人倍率（F310301）の順位と並べて比べて
socialAnnounce: |-
  有効求人倍率が1倍前後の10県を、他県への就職の割合で分けました。

  埼玉・千葉・神奈川は3割が県外就職、北海道は約5%。同じ低さでも中身が逆です。
  多拠点採用の検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2024年度の有効求人倍率は、東京都の1.76倍から神奈川県の0.91倍まで、都道府県で約1.9倍の差があります。倍率が1倍前後の県は2種類に分かれます。埼玉県・千葉県・神奈川県ではハローワーク経由の就職の約3割が他県での就職で、北海道（4.9%）・沖縄県（7.1%）では1割未満です。都道府県の順位は、2015年度と2024年度でも相関が0.74あり、年度による入れ替わりは限られています。

有効求人倍率は、ハローワークに登録された求職者1人あたり何件の求人があるかを表し、1を超えると求人が求職者を上回ります。複数の拠点で人を採用する企業は、出店や拠点新設の候補地でこの値を確認します。この記事では、厚生労働省の[一般職業紹介状況（職業安定業務統計）](https://www.mhlw.go.jp/toukei/list/114-1.html)をもとにした e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010106)の都道府県別労働データ（`f_pref_labor`）を使い、有効求人倍率の地域差と推移を集計しました。労働の指標は同じテーブルに数百種類が収録されていて、ここでは有効求人倍率（`F310301`）を使います。値はパートタイムを含む年度平均で、収録は2015年度から2024年度までの10年分です。

この倍率は、求人を受け付けたハローワークの所在地で集計されています（受理地別）。本社が全国の勤務地の求人をまとめて出すと、その求人は本社のある県に数えられます。厚生労働省は求人票の就業地で集計した値も[同じ統計から公表していて](https://www.mhlw.go.jp/stf/newpage_57261.html)、勤務地で集計すると順位は変わります。この記事の数字はすべて受理地別です。

## 全国の有効求人倍率は、2015年度から1.0倍を上回り続けている

全国の有効求人倍率の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 1, "type": "quantitative"}
      }
    }
  ]
}
```

全国の有効求人倍率は2015年度の1.23倍から上がり、2018年度に収録期間中で最も高い1.62倍になりました。2019年度は1.55倍に下がり、2020年度は1.10倍です。2022年度に1.31倍まで戻ったあと、1.29倍、1.25倍と少しずつ下がっています。全期間で点線の1.0倍を上回っていて、全国では求人が求職者を上回る状態が続いています。実際の採用に関係するのは、拠点を置く地域の水準です。

## 2024年度は東京都の1.76倍が最も高く、神奈川県の0.91倍が最も低い

2024年度の有効求人倍率を47都道府県で比較します。上位10・中間・下位10を色分けしています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
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
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
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
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
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

最も高いのは東京都の1.76倍、次いで福井県の1.73倍です。上位10には石川県（1.53倍）・岐阜県（1.52倍）・新潟県（1.46倍）が入り、香川県（1.46倍）・山口県（1.45倍）・岡山県（1.44倍）・広島県（1.43倍）・島根県（1.42倍）と中国四国の県が続きます。北陸の富山県は1.39倍で11位です。下位は神奈川県（0.91倍）・沖縄県（0.98倍）・千葉県（0.99倍）・北海道（0.99倍）で、兵庫県（1.00倍）・滋賀県（1.01倍）・埼玉県（1.04倍）も1倍近辺に並びます。最も高い東京都と最も低い神奈川県では約1.9倍の差があります。東京都の値には、全国の勤務地の求人が本社のある東京都で受理された分が含まれています。

## 倍率が高いのは北陸と中国地方、低いのは首都圏の周辺県や北海道・沖縄県

同じ値を地図にしました。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: value
    label: pref_name
    name: "有効求人倍率（倍）"
lng: 137
lat: 36.5
zoom: 4
```

最も色が濃いのは東京都ですが、面積が小さいので地図では目立ちません。ほかに色が濃いのは北陸の福井県・石川県・新潟県と岐阜県、中国地方の山口県・岡山県・広島県・島根県、香川県です。色が薄い下位10県は、首都圏の周辺県（神奈川県・千葉県・埼玉県）、北海道・沖縄県・青森県・高知県、近畿の兵庫県・滋賀県、東海の静岡県です。地図ではこの10県が同じ色に見えますが、倍率が低い理由は県によって違います。

## 1倍前後の県のうち、首都圏の周辺県は就職の約3割が他県

同じ統計には、その県のハローワークで職を得た人が何件で、うち何件が他県での就職だったかも収録されています。就職件数（`F3105`）に対する他県への就職件数（`F310603`）の割合を出すと、県境をまたぐ就職がどれくらいあるかが分かります。2024年度の全国の値は次のとおりです。

```sql
SELECT * FROM national_outflow
```

全国では就職の13.1%が他県での就職です。下位10県について同じ割合を出し、この全国平均の上下で色分けします。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "outflow_local"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "out_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "out_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "就職件数に占める他県への就職の割合（%・2024年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "県内で完結（全国平均未満）",
          "type": "nominal",
          "scale": {
            "domain": ["県内で完結（全国平均未満）", "他県への就職が多い（全国平均以上）"],
            "range": ["#94a3b8", "#3b82f6"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "outflow_cross"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "out_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "out_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "就職件数に占める他県への就職の割合（%・2024年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "他県への就職が多い（全国平均以上）",
          "type": "nominal",
          "scale": {
            "domain": ["県内で完結（全国平均未満）", "他県への就職が多い（全国平均以上）"],
            "range": ["#94a3b8", "#3b82f6"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 13.1, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

倍率が1倍前後の10県は、この割合で2つに分かれます。埼玉県は32.9%、千葉県は32.0%、神奈川県は29.7%と、ハローワーク経由の就職の3割が他県での就職です。兵庫県18.8%・滋賀県17.7%も全国平均を上回ります。これに対し北海道4.9%・沖縄県7.1%・青森県8.0%・高知県8.1%・静岡県10.6%は、いずれも全国平均を下回ります。最も低い北海道は、全国平均の4割に届きません。

首都圏の周辺県と近畿の周辺県では、求職者の多くが県外で職を得ています。これらの県の求人倍率が低いのは、求人が隣県で受理され、就職も隣県で起きているためと考えられます。ここに拠点を置く企業は、都心の求人と求職者を取り合うことになります。北海道や沖縄県では就職のほとんどが県内なので、1倍を下回る値は県内で求職者に対して求人が少ないことを表します。同じ0.9〜1.0倍でも、採用計画での意味は逆です。

就職件数と他県への就職件数はパートタイムと新規学卒者を除く一般の値で、パートタイムを含む有効求人倍率とは対象の範囲が違うので、割合は県どうしの大小の比較に使ってください。

## 都道府県の順位は、2015年度から大きくは変わっていない

年度によって順位が入れ替わるなら拠点の判断には使いにくく、地域差が安定しているなら判断材料になります。動き方の違う4都県の推移を比較します。

```chart
{
  "layer": [
    {
      "data": {"name": "ts_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "福井県", "神奈川県", "沖縄県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ts_fukui"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
        },
        "color": {
          "datum": "福井県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "福井県", "神奈川県", "沖縄県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ts_kanagawa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
        },
        "color": {
          "datum": "神奈川県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "福井県", "神奈川県", "沖縄県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ts_okinawa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "有効求人倍率（倍）", "grid": true}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "福井県", "神奈川県", "沖縄県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 1, "type": "quantitative"}
      }
    }
  ]
}
```

4都県とも収録期間中のピークは2018年度です。底の年は分かれ、福井県は2020年度の1.57倍、沖縄県は2020年度の0.72倍、東京都は2021年度の1.22倍、神奈川県は2020年度と2021年度に並んだ0.80倍が最低でした。ピークから底までの下げ幅は東京都0.91ポイント、福井県0.53ポイント、沖縄県0.46ポイント、神奈川県0.40ポイントで、東京都の変動が最も大きくなっています。福井県は最も落ちた年でも1.5倍を割らず、神奈川県と沖縄県はコロナ下で1.0倍を大きく下回りました。

各年度の47都道府県の順位と、2024年度の順位との相関は次のとおりです。

```sql
SELECT * FROM rank_stability
```

9年前の2015年度でも0.74、直近の2023年度では0.97です。景気によって倍率の水準は上下しますが、どの県の倍率が高いかという順位は年度が変わってもあまり変わりません。

## 有効求人倍率と賃金の相関は0.09

横軸に2024年度の有効求人倍率、縦軸に[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)による2024年の所定内給与額（男性一般労働者、`F620217`）を取り、47都道府県を散布図にしました。倍率は年度平均、給与は2024年6月の1か月分で、時点の取り方が異なる指標を同じ図に置いています。点線は47都道府県の中央値（有効求人倍率1.26倍、所定内給与額326.0千円）です。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "ratio", "type": "quantitative"},
          {"field": "wage", "type": "quantitative"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "有効求人倍率（倍・2024年度）", "grid": true}
        },
        "y": {
          "field": "wage",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "所定内給与額（千円・2024年6月）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1.26, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 326, "type": "quantitative"}
      }
    }
  ]
}
```

有効求人倍率と所定内給与額の相関係数は0.09で、両者にはほとんど関係がありません。右下には福井県（1.73倍・317.0千円）や岐阜県（1.52倍・321.1千円）など、倍率が高いのに賃金は中央値以下の県があります。左上には神奈川県（0.91倍・387.9千円）や千葉県（0.99倍・352.4千円）など、賃金は高いが倍率は低い県があります。この2県は他県への就職が約3割の県なので、賃金が高いのは都心の賃金水準の影響と考えられます。東京都（1.76倍・440.8千円）だけは右上に離れています。採用のしやすさと人件費は、拠点ごとに別々に評価する必要があります。

## 拠点の検討での使い方

- 候補地の倍率を見る前に、他県への就職の割合を確認する: 約3割の埼玉県・千葉県・神奈川県では、県内の倍率はその県で働く人の求人と求職者の関係を表していない
- 人件費と採用の難しさを別々に評価する: 賃金が低い地域でも倍率が高い場合があるので、両方を出店地ごとに比較する
- 勤務地で集計した値が必要なときは就業地別の値を使う: 本記事で使ったのは受理地別で、厚生労働省は同じ統計から就業地別の都道府県別倍率も公表している

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010106) の都道府県別労働データ（`f_pref_labor`）を2026年8月22日時点で集計しています。有効求人倍率・就職件数・他県への就職件数の出典は厚生労働省の[一般職業紹介状況（職業安定業務統計）](https://www.mhlw.go.jp/toukei/list/114-1.html)で、いずれも年度の値です。散布図の所定内給与額は[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)による2024年6月分の値で、男性一般労働者を対象としています。各指標の定義は e-Stat の[項目定義 Ｆ 労働](https://www.e-stat.go.jp/koumoku/koumoku_teigi/F)によります。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の労働統計テーブル](/datasets/queria/e_stat/ssds/f_pref_labor)には、有効求人倍率のほかに就職件数や賃金などの指標が入っているので、自社の拠点候補地の倍率・他県への就職の割合・賃金水準を確認できます。

```sql id=national_trend
SELECT year, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ORDER BY year
```

```sql id=rank_top
WITH ranked AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS ratio, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, ratio FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS ratio, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, ratio FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH ranked AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS ratio, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, ratio FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=map_data
WITH d AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT d.area_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, d.ratio AS value, ROW_NUMBER() OVER (ORDER BY d.area_name) - 1 AS row_id FROM d JOIN nlftp.boundary.prefecture p ON d.area_name = p.prefecture_name
```

```sql id=outflow_local
WITH r AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS ratio, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), s AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F3105' THEN TRY_CAST(value AS DOUBLE) END) AS placements, MAX(CASE WHEN cat01 = 'F310603' THEN TRY_CAST(value AS DOUBLE) END) AS outflow FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F3105', 'F310603') AND year = 2024 AND area_name != '全国' GROUP BY area_name), nat AS (SELECT MAX(CASE WHEN cat01 = 'F310603' THEN TRY_CAST(value AS DOUBLE) END) / MAX(CASE WHEN cat01 = 'F3105' THEN TRY_CAST(value AS DOUBLE) END) * 100 AS pct FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F3105', 'F310603') AND year = 2024 AND area_name = '全国'), j AS (SELECT r.area_name, r.ratio, s.outflow / s.placements * 100 AS out_pct FROM r JOIN s ON r.area_name = s.area_name WHERE r.rn > 37) SELECT area_name, ratio, ROUND(out_pct, 1) AS out_pct FROM j, nat WHERE out_pct < nat.pct ORDER BY out_pct
```

```sql id=outflow_cross
WITH r AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS ratio, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), s AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F3105' THEN TRY_CAST(value AS DOUBLE) END) AS placements, MAX(CASE WHEN cat01 = 'F310603' THEN TRY_CAST(value AS DOUBLE) END) AS outflow FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F3105', 'F310603') AND year = 2024 AND area_name != '全国' GROUP BY area_name), nat AS (SELECT MAX(CASE WHEN cat01 = 'F310603' THEN TRY_CAST(value AS DOUBLE) END) / MAX(CASE WHEN cat01 = 'F3105' THEN TRY_CAST(value AS DOUBLE) END) * 100 AS pct FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F3105', 'F310603') AND year = 2024 AND area_name = '全国'), j AS (SELECT r.area_name, r.ratio, s.outflow / s.placements * 100 AS out_pct FROM r JOIN s ON r.area_name = s.area_name WHERE r.rn > 37) SELECT area_name, ratio, ROUND(out_pct, 1) AS out_pct FROM j, nat WHERE out_pct >= nat.pct ORDER BY out_pct
```

```sql id=national_outflow
SELECT MAX(CASE WHEN cat01 = 'F3105' THEN TRY_CAST(value AS DOUBLE) END) AS "就職件数（件）", MAX(CASE WHEN cat01 = 'F310603' THEN TRY_CAST(value AS DOUBLE) END) AS "うち他県への就職（件）", ROUND(MAX(CASE WHEN cat01 = 'F310603' THEN TRY_CAST(value AS DOUBLE) END) / MAX(CASE WHEN cat01 = 'F3105' THEN TRY_CAST(value AS DOUBLE) END) * 100, 1) AS "割合（%）" FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F3105', 'F310603') AND year = 2024 AND area_name = '全国'
```

```sql id=rank_stability
WITH d AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), rk AS (SELECT area_name, year, ROW_NUMBER() OVER (PARTITION BY year ORDER BY ratio DESC, area_name) AS rn FROM d) SELECT a.year AS "年度", ROUND(CORR(a.rn, b.rn), 2) AS "2024年度との順位相関" FROM rk a JOIN rk b ON a.area_name = b.area_name AND b.year = 2024 WHERE a.year < 2024 GROUP BY a.year ORDER BY a.year
```

```sql id=ts_tokyo
SELECT year, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND area_name = '東京都' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ORDER BY year
```

```sql id=ts_fukui
SELECT year, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND area_name = '福井県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ORDER BY year
```

```sql id=ts_kanagawa
SELECT year, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND area_name = '神奈川県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ORDER BY year
```

```sql id=ts_okinawa
SELECT year, TRY_CAST(value AS DOUBLE) AS ratio FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F310301' AND area_name = '沖縄県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ORDER BY year
```

```sql id=scatter
SELECT j.area_name, TRY_CAST(j.value AS DOUBLE) AS ratio, TRY_CAST(w.value AS DOUBLE) AS wage FROM e_stat.ssds.f_pref_labor j JOIN e_stat.ssds.f_pref_labor w ON j.area_name = w.area_name AND j.year = w.year WHERE j.cat01 = 'F310301' AND w.cat01 = 'F620217' AND j.year = 2024 AND j.area_name != '全国' AND TRY_CAST(j.value AS DOUBLE) IS NOT NULL AND TRY_CAST(w.value AS DOUBLE) IS NOT NULL
```
