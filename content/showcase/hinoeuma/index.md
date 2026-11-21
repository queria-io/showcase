---
title: 出生数の前年比は、1980年以降で最も大きく減った年でも-5.8%
description: 全国の出生数を1980年から2023年まで43回の前年比にすると、最も大きく減ったのは2019年の-5.8%でした。2005年から2015年の10年は、全国が-5.3%だったのに対し、東京都は+17.2%増えています。
ogDescription: 全国の出生数の前年比43回のうち、最も大きく減ったのは2019年の-5.8%です。2005年から2015年は、全国の-5.3%に対して東京都が+17.2%でした。
publishedAt: 2026-02-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 出生
  - 人口
  - 丙午
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/1.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義 A 人口・世帯
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/A
    publisher: 総務省統計局
  - title: 人口動態調査
    url: https://www.mhlw.go.jp/toukei/list/81-1a.html
    publisher: 厚生労働省
agentHint: a_pref_population の cat01=A4101 を都道府県ごとに2005年と2015年で比べて、増えた県と減った県を全部出して。そのうえで自分の県について1980年から2023年までの推移を並べ、出生数が最も多かった年と、そこからの減少率を確かめて
socialAnnounce: |-
  全国の出生数の前年比を1980年から43回並べると、最大の落ち込みは2019年の-5.8%でした。

  同じデータで2005年から2015年を見ると、全国が-5.3%の10年に東京都は+17.2%。増えたのは47都道府県のうち3つだけです。
  Queriaは行政のオープンデータを整えて公開しています。
---

全国の出生数を1980年から2023年まで前年比にすると、43回のうち最も大きく減ったのは2019年の-5.8%でした。-5%を超えて減った年は4回で、1年で1割以上減った年はありません。2005年から2015年の10年は、全国の出生数が-5.3%だったのに対し、東京都は+17.2%増えました。この10年に出生数が増えたのは、47都道府県のうち東京都・沖縄県・福岡県の3つだけです。

2026年は干支の「丙午（ひのえうま）」にあたります。「丙午生まれの女性は気性が荒い」という言い伝えから、前回の1966年には出産を控える人が多く、出生数が大きく減ったとされています。2026年の出生数が丙午で減ったかどうかを判断するには、通常の年に出生数がどれくらい増減するかを知っておく必要があります。

使ったのは e-Stat「社会・人口統計体系」の都道府県別データ（`a_pref_population`）の出生数（`A4101`）と総人口（`A1101`）です。出生数は[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/A)にあるとおり[人口動態調査](https://www.mhlw.go.jp/toukei/list/81-1a.html)の「出生数」で、1月1日から12月31日までの暦年計です。収録は1980年から2023年までで、前回の丙午の1966年は含まれません。

## 全国の出生数は、43年で53.9%減った

全国の出生数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#ec4899"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1980年の1,576,889人から2023年の727,288人まで、43年で53.9%減り、半分以下になりました。グラフの線は特定の年に大きく下がってはおらず、毎年少しずつ下がり続けています。1年ごとの変化の大きさは、この折れ線では判断できません。

## 前年比の減少は、最も大きい年でも5.8%

1981年から2023年までの43回の前年比を計算しました。

```chart
{
  "layer": [
    {
      "data": {"name": "change_rate"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "change_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "change_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "変化率（%）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b"},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 0, "type": "quantitative"}
      }
    }
  ]
}
```

43回のうちマイナスは34回、プラスは9回でした。

最も大きく減ったのは2019年の-5.8%です。2023年の-5.6%、1989年の-5.1%、2022年の-5.0%が続き、-5%を超えたのはこの4回だけです。5番目は2005年の-4.3%で、それ以外は-4%台以下です。人数では、率で最大の2019年は53,161人の減少、人数で最も大きく減った1989年は67,204人の減少でした。

減少が続いた2019年から2023年までの4年間を通算しても、-15.9%です。1980年以降、1年で1割以上減った年はありません。

1980年以降の43回の中に、丙午の言い伝えで語られるような大きな減少はありません。2026年の減少が-5.8%を超えれば、1980年以降で最も大きな減少になります。通常の年と同じ数%の減少であれば、丙午の影響は通常の増減と区別できません。全国の出生数で丙午の影響を判断するときの目安は、この-5.8%です。

## 全国の出生数が5.3%減った2005年から2015年に、東京都は17.2%増えた

都道府県別に見ると、全国の値より大きく、しかも反対の方向に変化した期間があります。2005年と2015年の出生数を都道府県ごとに比較し、増減率の上位10都県と下位10県を並べました。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "rise_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年から2015年の出生数の変化率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位（変化率が高い）",
          "type": "nominal",
          "scale": {"domain": ["上位（変化率が高い）", "下位（変化率が低い）"], "range": ["#ec4899", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rise_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年から2015年の出生数の変化率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位（変化率が低い）",
          "type": "nominal",
          "scale": {"domain": ["上位（変化率が高い）", "下位（変化率が低い）"], "range": ["#ec4899", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

全国はこの10年で-5.3%（1,062,530人→1,005,721人）でした。東京都は+17.2%（96,542人→113,194人）で、16,652人増えています。増えたのは47都道府県のうち東京都・沖縄県（+5.1%）・福岡県（+4.2%）の3つだけで、4番目の熊本県は-0.4%です。下位では秋田県が-23.9%、福島県が-19.1%、青森県が-18.1%です。東京都と秋田県の差は41.1ポイントあります。

この10年の東京都の前年比10回のうち9回が増加で、2011年だけ前年を下回りました。1989年以降で東京都の出生数が最も多かったのは、2015年の113,194人です。

## 東京都の出生数は2015年から減少に転じ、2023年は2005年より10.6%少ない

東京都・大阪府・愛知県・沖縄県・秋田県の、1980年からの推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "birth_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "大阪府", "愛知県", "沖縄県", "秋田県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "birth_osaka"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "color": {
          "datum": "大阪府",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "大阪府", "愛知県", "沖縄県", "秋田県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "birth_aichi"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "color": {
          "datum": "愛知県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "大阪府", "愛知県", "沖縄県", "秋田県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "birth_okinawa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "大阪府", "愛知県", "沖縄県", "秋田県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "birth_akita"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "births",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "出生数（人）", "grid": true}
        },
        "color": {
          "datum": "秋田県",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "大阪府", "愛知県", "沖縄県", "秋田県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

東京都は2005年の96,542人まで減ったあと増加し、2015年の113,194人から再び減って、2023年には86,348人になりました。2015年からの8年で-23.7%で、2005年の水準も10.6%下回っています。増えた10年より、その後の8年の減り方のほうが速くなっています。

1980年から2023年までの通算では、東京都が-38.3%（139,953人→86,348人）、大阪府が-50.6%（111,956人→55,292人）、愛知県が-44.8%（87,697人→48,402人）です。大阪府は東京都より10ポイント以上大きく減っています。沖縄県は-38.1%（20,281人→12,549人）で東京都と同じくらいの減少率で、出生数が最も多かったのは1980年ではなく1985年の20,657人でした。秋田県は-77.9%（16,324人→3,611人）で、43年で4分の1以下になっています。全国の-53.9%は、これらの県の値をまとめた値です。

## 2023年の普通出生率は、沖縄県が秋田県の2.1倍

普通出生率（総人口に対する出生数の割合）で2023年の都道府県を比較し、上位10県と下位10道県を並べました。出生数は日本人の出生だけを集計し、総人口は国内に常住する外国人を含むため、外国人の多い地域では出生率がやや低く出ます。女性の年齢構成を統一した合計特殊出生率とは別の指標で、高齢化が進んだ地域では低く出ます。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "birth_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "birth_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "birth_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "出生率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位（出生率が高い）",
          "type": "nominal",
          "scale": {"domain": ["上位（出生率が高い）", "下位（出生率が低い）"], "range": ["#ec4899", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "birth_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "birth_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "birth_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "出生率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位（出生率が低い）",
          "type": "nominal",
          "scale": {"domain": ["上位（出生率が高い）", "下位（出生率が低い）"], "range": ["#ec4899", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高い沖縄県が0.85%、最も低い秋田県が0.40%で、2.1倍の差があります。上位には福岡県（0.67%）・佐賀県（0.65%）・熊本県（0.65%）など九州の県が多く、滋賀県（0.66%）や愛知県（0.65%）・大阪府（0.63%）も入ります。下位は秋田県・岩手県（0.47%）・青森県（0.48%）・山形県（0.50%）と東北の県が多く、北海道（0.48%）も入ります。2005年から2015年に出生数が17.2%増えた東京都は0.61%で、47都道府県のうち12位です。

## まとめ

- 全国の出生数は1,576,889人から727,288人へ、43年で53.9%減った
- 前年比で最も大きく減ったのは2019年の-5.8%。-5%を超えたのは43回中4回だけで、1割以上減った年はない。2019年から2023年までの4年間を通算しても-15.9%
- 全国が-5.3%だった2005年から2015年の10年に、東京都は+17.2%増えた。増えたのは47都道府県のうち東京都・沖縄県・福岡県の3つだけで、最も減った秋田県（-23.9%）との差は41.1ポイント
- 東京都の増加は2015年の113,194人で止まり、2023年には86,348人で、2005年の水準を10.6%下回った
- 普通出生率は沖縄県0.85%と秋田県0.40%で2.1倍、43年の減少率は東京都-38.3%と秋田県-77.9%で大きな差がある

2005年から2015年に全国の出生数は5.3%減りましたが、同じ10年の都道府県の増減率は東京都の+17.2%から秋田県の-23.9%まで、41.1ポイントの差がありました。

## データの出典

本記事は e-Stat[「社会・人口統計体系」](https://www.stat.go.jp/data/ssds/1.html)の都道府県別データ（`a_pref_population`）から、出生数（`A4101`）と総人口（`A1101`）を2026年9月20日時点で集計しています。出生数の元データは厚生労働省の[人口動態調査](https://www.mhlw.go.jp/toukei/list/81-1a.html)で、収録は1980年から2023年までです。総人口は国勢調査および人口推計の10月1日現在の値です。全国の値は都道府県の合算ではなく、データに含まれる「全国」の行を使っています。

Queriaは、行政のオープンデータを、列名・単位・カテゴリコードの体系を統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の人口・出生統計テーブル](/datasets/queria/e_stat/ssds/a_pref_population)から、担当地域の出生数を年別に並べたり、転入超過や住宅着工と組み合わせたりできます。

```sql id=trend
SELECT year, ROUND(TRY_CAST(value AS DOUBLE)) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=change_rate
WITH yearly AS ( SELECT year, ROUND(TRY_CAST(value AS DOUBLE)) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ), with_change AS ( SELECT year, births, ROUND((births - LAG(births) OVER (ORDER BY year)) * 100.0 / LAG(births) OVER (ORDER BY year), 1) AS change_pct FROM yearly ) SELECT * FROM with_change WHERE change_pct IS NOT NULL ORDER BY year
```

```sql id=rise_top
WITH b AS ( SELECT area_name, MAX(CASE WHEN year = 2005 THEN TRY_CAST(value AS DOUBLE) END) AS y05, MAX(CASE WHEN year = 2015 THEN TRY_CAST(value AS DOUBLE) END) AS y15 FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name <> '全国' GROUP BY area_name ) SELECT area_name, ROUND((y15 / y05 - 1) * 100, 1) AS pct FROM b ORDER BY pct DESC, area_name LIMIT 10
```

```sql id=rise_bottom
SELECT area_name, pct FROM ( WITH b AS ( SELECT area_name, MAX(CASE WHEN year = 2005 THEN TRY_CAST(value AS DOUBLE) END) AS y05, MAX(CASE WHEN year = 2015 THEN TRY_CAST(value AS DOUBLE) END) AS y15 FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name <> '全国' GROUP BY area_name ) SELECT area_name, ROUND((y15 / y05 - 1) * 100, 1) AS pct FROM b ORDER BY pct ASC, area_name LIMIT 10 ) ORDER BY pct DESC, area_name
```

```sql id=birth_tokyo
SELECT year, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '東京都' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=birth_osaka
SELECT year, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '大阪府' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=birth_aichi
SELECT year, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '愛知県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=birth_okinawa
SELECT year, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '沖縄県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=birth_akita
SELECT year, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND area_name = '秋田県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=birth_top
WITH births AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND TRY_CAST(value AS DOUBLE) > 0 ) SELECT b.area_name, ROUND(b.births / p.population * 100, 2) AS birth_rate FROM births b JOIN pop p ON b.area_name = p.area_name ORDER BY birth_rate DESC, b.area_name LIMIT 10
```

```sql id=birth_bottom
SELECT area_name, birth_rate FROM ( WITH births AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND TRY_CAST(value AS DOUBLE) > 0 ) SELECT b.area_name, ROUND(b.births / p.population * 100, 2) AS birth_rate FROM births b JOIN pop p ON b.area_name = p.area_name ORDER BY birth_rate ASC, b.area_name LIMIT 10 ) ORDER BY birth_rate DESC, area_name
```

```sql id=birth_rate_tokyo
WITH births AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS births FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A4101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), pop AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND TRY_CAST(value AS DOUBLE) > 0 ), ranked AS ( SELECT b.area_name, ROUND(b.births / p.population * 100, 2) AS birth_rate, RANK() OVER (ORDER BY b.births / p.population DESC) AS rank FROM births b JOIN pop p ON b.area_name = p.area_name ) SELECT area_name, birth_rate, rank FROM ranked WHERE area_name = '東京都'
```
