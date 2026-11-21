---
title: 宿泊客は2019年を超えたのに、京都市でホテルや飲食店の新しい建物は2018年の1割を下回った
description: 京都市のホテル・飲食店用の新築床面積は2018年の35.2万㎡から2024年は3.3万㎡へ。京都府の2021〜24年の着工は2016〜19年の21%で、47都道府県で最小です。
publishedAt: 2026-10-07
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - ホテル
  - 建築着工
  - 観光
  - 京都
  - 市区町村
datasets:
  - queria/e_stat
sources:
  - title: 建築着工統計調査
    url: https://www.e-stat.go.jp/statistics/00600120
    publisher: 国土交通省
  - title: 宿泊旅行統計調査
    url: https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html
    publisher: 観光庁
  - title: 衛生行政報告例
    url: https://www.mhlw.go.jp/toukei/list/36-19.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
agentHint: e_stat.building_starts.municipality_use の宿泊業・飲食サービス業用建築物（use_code = '56'）について、自分が出店を考えている県の市区町村ごとに、2016〜2019年と2021〜2024年の着工床面積と棟数を並べて出して。年ごとの値も見たい
socialAnnounce: |-
  ホテルや飲食店用に着工した建物の床面積を、市区町村別に2011年から2024年まで追いました。

  ホテルの出店候補地を比べるときの、競合の新規供給の把握に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

京都市でホテルや飲食店として着工した建物の床面積は、2018年の35.2万㎡から2024年は3.3万㎡に減り、2018年の9.4%になりました。京都府の2021〜2024年の着工床面積は2016〜2019年の20.7%で、47都道府県で最も小さい値です。同じ期間に、京都府の延べ宿泊者数は2019年から2024年に12.9%増えています。全国の延べ宿泊者数も2024年は2019年を8.0%上回りました。

ホテルの出店候補地を比較するときは、宿泊客の数に加えて、これから競合の客室がどれだけ増えるかを確認する必要があります。この記事では、国土交通省の[建築着工統計調査](https://www.e-stat.go.jp/statistics/00600120)から、ホテルや飲食店として着工した建物の床面積を市区町村ごとに2011年から2024年まで並べ、宿泊者数と客室数の推移と比較します。

## 京都市の着工は2018年の35.2万㎡から、2024年は3.3万㎡に

建築着工統計調査は、建築基準法の届出をもとに、床面積10㎡を超える建物の着工を全数で集計しています。Queria の `e_stat.building_starts.municipality_use` は、その市区町村別・用途別のテーブルを2011年から2024年まで収録したもので、年は1月から12月に着工した分です。用途は建物の主な使い道で18に分かれていて、この記事で使うのはそのうちの1つです。

| コード | 用途                             | 主な内容                       |
| ------ | -------------------------------- | ------------------------------ |
| `56`   | Ｍ宿泊業，飲食サービス業用建築物 | ホテル・旅館・飲食店などの建物 |
| `11`   | 計                               | 18用途の合計                   |
| `12`   | Ａ居住専用住宅                   | 戸建てやマンションなど         |
| `51`   | Ｊ卸売業，小売業用建築物         | 店舗・倉庫を含む商業の建物     |

この用途はホテル・旅館と飲食店を1つの区分で集計していて、統計の上では分けられません。以下で「ホテルや飲食店」と書くのはこの区分のことです。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "city_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo23\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tokyo23", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "着工した年", "format": "d"}
        },
        "y": {
          "field": "tokyo23",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ホテル・飲食店用の着工床面積（万㎡）", "grid": true}
        },
        "color": {
          "datum": "東京23区",
          "type": "nominal",
          "scale": {"domain": ["東京23区", "大阪市", "京都市"], "range": ["#3b82f6", "#94a3b8", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "city_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"osaka\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "osaka", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "着工した年", "format": "d"}
        },
        "y": {
          "field": "osaka",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ホテル・飲食店用の着工床面積（万㎡）", "grid": true}
        },
        "color": {
          "datum": "大阪市",
          "type": "nominal",
          "scale": {"domain": ["東京23区", "大阪市", "京都市"], "range": ["#3b82f6", "#94a3b8", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "city_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kyoto\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "kyoto", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "着工した年", "format": "d"}
        },
        "y": {
          "field": "kyoto",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ホテル・飲食店用の着工床面積（万㎡）", "grid": true}
        },
        "color": {
          "datum": "京都市",
          "type": "nominal",
          "scale": {"domain": ["東京23区", "大阪市", "京都市"], "range": ["#3b82f6", "#94a3b8", "#ec4899"]},
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

京都市でホテルや飲食店として着工した建物の床面積は、2016年の11.8万㎡から2018年に35.2万㎡まで増えたあと、2021年は3.5万㎡、2024年は3.3万㎡になりました。2024年は2018年の9.4%で、2011年から2015年の2.2万〜6.0万㎡と同じ水準です。棟数も2018年の279棟から、2021年から2024年は31〜63棟に減っています。数棟の大型案件がなくなったためではなく、着工する建物の数が減っています。

同じ時期に、東京23区は2024年に93.0万㎡と、2011年以降で最も多くなりました。全国の合計に占める東京23区の割合は、2018年の15.2%から2024年の34.5%に上がっています。

## 京都府の客室は5割増え、着工が減ったあとも2023年度まで増え続けた

着工した建物が開業するまでには時間がかかります。厚生労働省の[衛生行政報告例](https://www.mhlw.go.jp/toukei/list/36-19.html)にもとづく、旅館業法の許可を受けたホテル・旅館の客室数（`C3802`、社会・人口統計体系の `c_pref_economy`）を京都府について重ねました。客室数は各年度の3月31日現在の値で、都道府県単位なので京都府全体です。ホテル営業と旅館営業の許可を受けた施設の客室で、簡易宿所の客室は含みません。2016年から2019年に京都府で着工したホテル・飲食店の床面積の96%は京都市です。

```chart
{
  "height": 300,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "kyoto_detail"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "floor_man", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "floor_man",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "着工床面積（万㎡）", "grid": true}
            },
            "color": {
              "datum": "京都市の着工床面積（万㎡）",
              "type": "nominal",
              "scale": {"domain": ["京都市の着工床面積（万㎡）", "京都府の客室数（室）"], "range": ["#ec4899", "#64748b"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "kyoto_detail"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rooms\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#64748b",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 36}
          },
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "rooms", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "rooms",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "客室数（室）", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "京都府の客室数（室）",
              "type": "nominal",
              "scale": {"domain": ["京都市の着工床面積（万㎡）", "京都府の客室数（室）"], "range": ["#ec4899", "#64748b"]},
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    }
  ],
  "resolve": {"scale": {"y": "independent"}},
  "config": {"legend": {"orient": "bottom"}}
}
```

京都府のホテル・旅館の客室数は、2015年度の33,595室から2023年度の50,263室へ1.50倍になりました。客室は着工が減った2020年度以降も増え続け、2019年度の43,379室から2023年度までにさらに6,884室増えています。2016年から2019年に着工した建物が、その後に開業した分と考えられます。2021〜2024年の京都市の着工は年2.6万〜8.6万㎡で、2011〜2015年と同じ水準に戻っています。

## 宿泊者の増減と着工床面積の比の相関は-0.23

都道府県ごとに、2016〜2019年と2021〜2024年の4年間の着工床面積を比較し、宿泊者の増減と並べました。宿泊者は観光庁の[宿泊旅行統計調査](https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html)の延べ宿泊者数（`G7101`、社会・人口統計体系の `g_pref_culture`）で、暦年の値です。従業者10人以上の施設の宿泊者で、小さな簡易宿所などの宿泊者は含みません。ホテル・飲食店の着工床面積は、全国では2021〜2024年が2016〜2019年の65%です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "pref_compare"},
      "mark": {"type": "point", "color": "#94a3b8", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "guests_change", "type": "quantitative"},
          {"field": "floor_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "guests_change",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "延べ宿泊者数の増減（2024年 / 2019年、%）", "grid": true}
        },
        "y": {
          "field": "floor_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工床面積（2021〜24年 / 2016〜19年、%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_highlight"},
      "mark": {"type": "point", "color": "#ec4899", "filled": true, "size": 144},
      "encoding": {
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "guests_change", "type": "quantitative"},
          {"field": "floor_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "guests_change",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "延べ宿泊者数の増減（2024年 / 2019年、%）", "grid": true}
        },
        "y": {
          "field": "floor_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工床面積（2021〜24年 / 2016〜19年、%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_highlight"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "guests_change",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "延べ宿泊者数の増減（2024年 / 2019年、%）", "grid": true}
        },
        "y": {
          "field": "floor_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工床面積（2021〜24年 / 2016〜19年、%）", "grid": true}
        },
        "text": {"field": "pref"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

京都府は、2021〜2024年の着工床面積が2016〜2019年の20.7%で、47都道府県で最も小さくなりました。延べ宿泊者数は2019年から2024年に12.9%増え、増加率は47都道府県で8番目です。宿泊者が26.5%増えて増加率が2番目の東京都は、着工床面積も99.9%とほぼ同じ規模でした。

着工床面積が2016〜2019年を上回ったのは、和歌山県・長崎県・秋田県など13県で、そのうち11県は宿泊者が2019年より減っているか、増加が5%未満です。47都道府県で宿泊者の増減率と着工床面積の比の相関係数は-0.23で、宿泊者が増えた府県ほど新しい建物が多いという関係はありません。

## 2021〜2024年の着工床面積は大阪市の45.7万㎡が最も多く、京都市は10番目

2021〜2024年の着工床面積が多い15市区町村を、2016〜2019年と並べました。

```chart
{
  "height": 480,
  "layer": [
    {
      "data": {"name": "top_muni"},
      "transform": [
        {"fold": ["before_floor_man", "after_floor_man"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"before_floor_man\": \"2016〜2019年\", \"after_floor_man\": \"2021〜2024年\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"before_floor_man\",\"after_floor_man\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "ホテル・飲食店用の着工床面積（万㎡、4年間の合計）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["2016〜2019年", "2021〜2024年"], "range": ["#cbd5e1", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["2021〜2024年", "2016〜2019年"]},
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2021〜2024年に最も多かったのは大阪市の45.7万㎡ですが、2016〜2019年の128.0万㎡の36%です。2016〜2019年に大阪市に次ぐ2番目だった京都市は、105.9万㎡から18.1万㎡になり10番目です。福岡市（33%）と名古屋市（28%）も3割前後に減りました。

上位15のうち5つは東京23区の区で、中央区・千代田区・新宿区・港区・品川区が並びます。東京23区の2023年と2024年の着工床面積155.4万㎡のうち79.2%は、1年で10万㎡を超えた5つの区・年（品川区の2023年、港区の2023年、千代田区・新宿区・中央区の2024年）が占めます。

棟数は新宿区の2024年が74棟、品川区の2023年が4棟と差が大きく、品川区は4棟で25.0万㎡になりました。長崎市の19.0万㎡も、そのうち18.4万㎡は2022年の1年分（17棟）です。市区町村の単位では、1年分の着工が4年分の合計の大半を占めることがあります。

## 出店候補地を比較するときの使い方

- 候補の市区町村について、2016〜2019年と2021〜2024年の着工床面積を並べます。京都市のように宿泊者が増えているのに新築が大きく減った地域では、今後競合となる客室は、すでに開業した建物がほとんどです。東京23区のように新築が続く地域では、開業前の競合があることを前提に計画を立てます
- 4年分の合計だけで判断せず、年ごとの床面積と棟数を確認します。長崎市の2022年や品川区の2023年のように1年だけ多い場合は、その年の着工が合計の大半を占めていて、その地域で建設が続いているとは限りません。京都市の2016〜2019年のように棟数も増えていれば、多くの事業者が参入した時期と考えられます
- 着工床面積にはホテルと飲食店が含まれるので、都道府県単位の客室数（`C3802`）の増加と合わせて、増えた床面積がホテルの客室として開業しているかを確認します

## データの出典

本記事は国土交通省の[建築着工統計調査](https://www.e-stat.go.jp/statistics/00600120)の市区町村別・用途別データと、総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別データ（観光庁の[宿泊旅行統計調査](https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html)、厚生労働省の[衛生行政報告例](https://www.mhlw.go.jp/toukei/list/36-19.html)）を、2026-10-07 時点で集計しています。着工床面積と延べ宿泊者数は暦年、客室数は年度末の値です。

Queriaは、建築着工統計の市区町村別のテーブルと社会・人口統計体系を、列名と単位を統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[建築着工統計のテーブル](/datasets/e_stat/building_starts/municipality_use)から、候補地の市区町村でホテルや飲食店の新築がいつ、どれだけあったかを確認したり、[宿泊者数のテーブル](/datasets/e_stat/ssds/g_pref_culture)で県の宿泊者の推移と並べたりできます。

```sql id=city_trend
-- 京都市・大阪市・東京23区と全国の、ホテル・飲食店用の着工床面積（万㎡）
SELECT
  year,
  CAST(SUM(floor_area) FILTER (WHERE area = '26100') AS DOUBLE) / 10000 AS kyoto,
  CAST(SUM(floor_area) FILTER (WHERE area = '27100') AS DOUBLE) / 10000 AS osaka,
  CAST(SUM(floor_area) FILTER (WHERE area LIKE '131%') AS DOUBLE) / 10000 AS tokyo23,
  CAST(SUM(floor_area) AS DOUBLE) / 10000 AS national,
  CAST(SUM(floor_area) FILTER (WHERE area LIKE '131%') AS DOUBLE) / SUM(floor_area) * 100 AS tokyo23_share
FROM e_stat.building_starts.municipality_use
WHERE use_code = '56' AND area_level = 'municipality' AND year BETWEEN 2011 AND 2024
GROUP BY year
ORDER BY year
```

```sql id=kyoto_detail
-- 京都市の着工床面積・棟数と、京都府のホテル・旅館の客室数
WITH b AS (
  SELECT year, CAST(floor_area AS DOUBLE) / 10000 AS floor_man, CAST(buildings AS DOUBLE) AS buildings
  FROM e_stat.building_starts.municipality_use
  WHERE use_code = '56' AND area = '26100' AND year BETWEEN 2011 AND 2024
), r AS (
  SELECT year, TRY_CAST(value AS DOUBLE) AS rooms
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C3802' AND area_name = '京都府' AND year BETWEEN 2011 AND 2023
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL
)
SELECT b.year, b.floor_man, b.buildings, r.rooms
FROM b LEFT JOIN r USING (year)
ORDER BY b.year
```

```sql id=city_groups
-- 都市ごとの2016〜2019年と2021〜2024年の合計（プロットはしない）
WITH t AS (
  SELECT
    CASE
      WHEN area LIKE '131%' THEN '東京23区'
      WHEN area IN ('26100', '27100', '23100', '40130', '01100', '14100') THEN area_name
      WHEN parent_area = '26000' THEN '京都府（京都市以外）'
      ELSE 'その他の市区町村'
    END AS grp,
    year, floor_area, buildings
  FROM e_stat.building_starts.municipality_use
  WHERE use_code = '56' AND area_level = 'municipality' AND year BETWEEN 2016 AND 2024
)
SELECT
  grp,
  CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2016 AND 2019) AS DOUBLE) / 10000 AS before_floor_man,
  CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2021 AND 2024) AS DOUBLE) / 10000 AS after_floor_man,
  CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2021 AND 2024) AS DOUBLE) / SUM(floor_area) FILTER (WHERE year BETWEEN 2016 AND 2019) * 100 AS floor_ratio,
  CAST(SUM(buildings) FILTER (WHERE year BETWEEN 2016 AND 2019) AS DOUBLE) AS before_buildings,
  CAST(SUM(buildings) FILTER (WHERE year BETWEEN 2021 AND 2024) AS DOUBLE) AS after_buildings
FROM t
GROUP BY grp
ORDER BY before_floor_man DESC
```

```sql id=pref_compare
-- 都道府県別の着工床面積の比（2021〜24年 / 2016〜19年）と延べ宿泊者数の増減（2024年 / 2019年）
WITH c AS (
  SELECT
    parent_area,
    CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2016 AND 2019) AS DOUBLE) AS before_floor,
    CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2021 AND 2024) AS DOUBLE) AS after_floor
  FROM e_stat.building_starts.municipality_use
  WHERE use_code = '56' AND area_level = 'municipality'
  GROUP BY parent_area
), g AS (
  SELECT
    area,
    area_name AS pref,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) AS guests2019,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS guests2024
  FROM e_stat.ssds.g_pref_culture
  WHERE cat01 = 'G7101' AND area_name <> '全国'
  GROUP BY area, area_name
), j AS (
  SELECT
    g.pref,
    c.before_floor / 10000 AS before_floor_man,
    c.after_floor / 10000 AS after_floor_man,
    c.after_floor / c.before_floor * 100 AS floor_ratio,
    (g.guests2024 / g.guests2019 - 1) * 100 AS guests_change
  FROM c JOIN g ON c.parent_area = g.area
)
SELECT
  *,
  RANK() OVER (ORDER BY floor_ratio) AS floor_ratio_rank_asc,
  RANK() OVER (ORDER BY guests_change DESC) AS guests_change_rank
FROM j
ORDER BY floor_ratio, pref
```

```sql id=pref_highlight
-- 散布図で強調する京都府と東京都（pref_compare と同じ集計）
WITH c AS (
  SELECT
    parent_area,
    CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2016 AND 2019) AS DOUBLE) AS before_floor,
    CAST(SUM(floor_area) FILTER (WHERE year BETWEEN 2021 AND 2024) AS DOUBLE) AS after_floor
  FROM e_stat.building_starts.municipality_use
  WHERE use_code = '56' AND area_level = 'municipality' AND parent_area IN ('26000', '13000')
  GROUP BY parent_area
), g AS (
  SELECT
    area,
    area_name AS pref,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) AS guests2019,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS guests2024
  FROM e_stat.ssds.g_pref_culture
  WHERE cat01 = 'G7101' AND area_name IN ('京都府', '東京都')
  GROUP BY area, area_name
)
SELECT
  g.pref,
  c.after_floor / c.before_floor * 100 AS floor_ratio,
  (g.guests2024 / g.guests2019 - 1) * 100 AS guests_change
FROM c JOIN g ON c.parent_area = g.area
ORDER BY g.pref
```

```sql id=national_ratio
-- 全国の2021〜2024年と2016〜2019年の比、着工床面積が増えた県の数（プロットはしない）
WITH c AS (
  SELECT
    parent_area,
    SUM(floor_area) FILTER (WHERE year BETWEEN 2016 AND 2019) AS before_floor,
    SUM(floor_area) FILTER (WHERE year BETWEEN 2021 AND 2024) AS after_floor
  FROM e_stat.building_starts.municipality_use
  WHERE use_code = '56' AND area_level = 'municipality'
  GROUP BY parent_area
), g AS (
  SELECT
    area,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) AS guests2019,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS guests2024
  FROM e_stat.ssds.g_pref_culture
  WHERE cat01 = 'G7101' AND area_name <> '全国'
  GROUP BY area
)
SELECT
  CAST(SUM(c.after_floor) AS DOUBLE) / SUM(c.before_floor) * 100 AS national_floor_ratio,
  COUNT(*) FILTER (WHERE c.after_floor > c.before_floor) AS prefs_floor_up,
  COUNT(*) FILTER (WHERE c.after_floor > c.before_floor AND g.guests2024 / g.guests2019 < 1.05) AS prefs_floor_up_guests_under5,
  CAST(SUM(c.before_floor) FILTER (WHERE c.parent_area = '26000') AS DOUBLE) AS kyoto_pref_before_floor,
  CORR(CAST(c.after_floor AS DOUBLE) / c.before_floor, g.guests2024 / g.guests2019) AS corr_floor_guests,
  (
    SELECT (MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) / MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) - 1) * 100
    FROM e_stat.ssds.g_pref_culture
    WHERE cat01 = 'G7101' AND area_name = '全国'
  ) AS national_guests_change
FROM c JOIN g ON c.parent_area = g.area
```

```sql id=top_muni
-- 2021〜2024年の着工床面積が多い15市区町村と、2016〜2019年の値・順位
WITH p AS (
  SELECT DISTINCT area, area_name AS pref
  FROM e_stat.ssds.g_pref_culture
  WHERE cat01 = 'G7101' AND area_name <> '全国'
), m AS (
  SELECT
    b.area,
    p.pref || ' ' || b.area_name AS name,
    CAST(SUM(b.floor_area) FILTER (WHERE b.year BETWEEN 2016 AND 2019) AS DOUBLE) / 10000 AS before_floor_man,
    CAST(SUM(b.floor_area) FILTER (WHERE b.year BETWEEN 2021 AND 2024) AS DOUBLE) / 10000 AS after_floor_man
  FROM e_stat.building_starts.municipality_use b
  JOIN p ON p.area = b.parent_area
  WHERE b.use_code = '56' AND b.area_level = 'municipality'
  GROUP BY b.area, p.pref, b.area_name
), ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (ORDER BY after_floor_man DESC, area) AS rn,
    RANK() OVER (ORDER BY before_floor_man DESC NULLS LAST) AS before_rank
  FROM m
)
SELECT rn, name, before_rank, COALESCE(before_floor_man, 0) AS before_floor_man, after_floor_man
FROM ranked
WHERE rn <= 15
ORDER BY rn
```

```sql id=big_projects
-- 2023・2024年に1年で10万㎡を超えた区・市と、その棟数（プロットはしない）
SELECT year, area_name, CAST(floor_area AS DOUBLE) / 10000 AS floor_man, CAST(buildings AS DOUBLE) AS buildings
FROM e_stat.building_starts.municipality_use
WHERE use_code = '56' AND area_level = 'municipality'
  AND (area LIKE '131%' OR area = '42201') AND year BETWEEN 2021 AND 2024 AND floor_area >= 100000
ORDER BY year, floor_area DESC
```
