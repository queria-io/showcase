---
title: 介護保険給付費は23年で3倍の11.2兆円、高齢者1人あたりでは大阪府が栃木県の1.4倍
description: 介護保険給付費（費用額）は2000年度の約3.5兆円から2023年度の約11.2兆円に増えました。都道府県別の総額は東京都が鳥取県の約17倍で、65歳以上1人あたりでは大阪府の36.0万円から栃木県の26.2万円まで約1.4倍の差があります。
publishedAt: 2026-06-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 介護
  - 社会保障
  - 高齢化
  - 市場分析
datasets:
  - queria/e_stat
sources:
  - title: 介護保険事業状況報告
    url: https://www.mhlw.go.jp/toukei/list/84-1.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系 都道府県データ
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures
    publisher: 総務省統計局
agentHint: 介護保険給付費(J7102)の2000年度から2023年度への伸び率を都道府県別に出して。市場規模が大きい大都市圏ほど伸びが急だったか見たい
socialAnnounce: |-
  都道府県別の介護保険給付費（2000〜2023年度）を、市場規模と高齢者一人当たりの2軸で分析しました。

  介護サービスの出店検討や市場評価に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

介護保険給付費（費用額）は、2000年度の約3.5兆円から2023年度の約11.2兆円へ、3倍以上に増えました。2023年度の都道府県別では東京都が約1兆456億円で最も多く、最も少ない鳥取県（約598億円）のおよそ17倍です。65歳以上の人1人あたりでは全国平均が約30.8万円で、最も多い大阪府（36.0万円）と最も少ない栃木県（26.2万円）の差は約1.4倍です。

介護サービスの売上の大半は介護保険給付でまかなわれるので、地域ごとの給付費の規模と伸びは、訪問介護やデイサービス、有料老人ホームなどの新規拠点を検討するときに、その地域の市場の大きさを見積もる指標になります。この記事では、厚生労働省の[介護保険事業状況報告](https://www.mhlw.go.jp/toukei/list/84-1.html)をもとにした e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県別福祉データから介護保険給付費を取り出し、市場規模・伸び・高齢者1人あたりの3つで都道府県を比較しました。

## 介護保険給付費は23年で3倍以上に増えた

e-Stat「社会・人口統計体系」の都道府県別福祉データ（`j_pref_welfare`）には、介護保険給付の項目が3つあります。

| コード | 内容                   |
| ------ | ---------------------- |
| J7101  | 介護保険給付（件数）   |
| J7102  | 介護保険給付（費用額） |
| J7103  | 介護保険給付（支給額） |

費用額（`J7102`）はサービスにかかった総費用で、利用者の自己負担も含みます。支給額（`J7103`）はそのうち保険から給付された分です。この記事では、事業者の売上規模に近い費用額を市場規模の指標に使います。全国の費用額の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"benefit_oku\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#22c55e"}
      },
      "encoding": {
        "tooltip": [
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "benefit_oku", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "benefit_oku",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "介護保険給付費（億円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

介護保険制度が始まった2000年度の約3.5兆円から、2023年度には約11.2兆円になりました。2006年度に一度減っているのは、2005年の介護保険法改正で施設の食費・居住費が原則として保険給付の対象外になったためと考えられます。このように制度改正で給付の対象範囲が変わることがあるので、長期の推移は同じ条件の値の比較にはなりません。2007年度以降は毎年増えていて、2023年度が過去最高です。

## 給付費の総額は東京都が最も多く、鳥取県の約17倍

2023年度の費用額を都道府県別に並べ、上位10・中間27・下位10に分けました。市場規模を比較するため、給付費の金額（億円）で並べています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "size_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "benefit_oku", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "benefit_oku",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "介護保険給付費（億円）", "grid": true}
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
      "data": {"name": "size_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "benefit_oku", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "benefit_oku",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "介護保険給付費（億円）", "grid": true}
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
      "data": {"name": "size_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "benefit_oku", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "benefit_oku",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "介護保険給付費（億円）", "grid": true}
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

最も多いのは東京都の約1兆456億円で、大阪府（約8,722億円）、神奈川県（約7,306億円）と、人口の多い大都市圏が続きます。最も少ない鳥取県（約598億円）と比較すると、東京都はおよそ17倍です。給付費の総額は人口、とくに高齢者人口の多さに連動していて、金額では大都市圏が大きく上回ります。市場が大きい地域は、競合も多いと考えられます。

## 高齢者1人あたりでは、大阪府が最も多く栃木県が最も少ない

2023年度の費用額を同じ年の65歳以上人口（`A1303`）で割り、高齢者1人あたりの給付費を都道府県別に並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "per_elderly_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_elderly", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_elderly",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者一人当たり給付費（万円／人）", "grid": true}
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
      "data": {"name": "per_elderly_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_elderly", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_elderly",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者一人当たり給付費（万円／人）", "grid": true}
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
      "data": {"name": "per_elderly_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_elderly", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_elderly",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者一人当たり給付費（万円／人）", "grid": true}
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

全国平均は高齢者1人あたり約30.8万円です。上位は大阪府（36.0万円）、島根県（35.0万円）、和歌山県（34.7万円）、秋田県（34.5万円）で、下位は栃木県（26.2万円）、茨城県（26.6万円）、埼玉県（26.8万円）、千葉県（27.6万円）です。最も多い大阪府と最も少ない栃木県の差は約1.4倍です。

総額では大都市圏が上位でしたが、高齢者1人あたりでは北関東と首都圏の県が下位になり、近畿・中国・東北の県が上位になります。1人あたりの給付費は、サービス提供体制や施設の整備状況、要介護認定率の地域差を合わせて反映した値と考えられ、この値が高いことは需要が満たされていることを意味するとは限りません。

## 給付費は高齢者人口にほぼ比例する

横軸に65歳以上人口（万人）、縦軸に給付費（億円）をとった散布図です。

```chart
{
  "layer": [
    {
      "data": {"name": "size_vs_elderly"},
      "mark": {"type": "point", "color": "#22c55e", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "elderly_man", "type": "quantitative"},
          {"field": "benefit_oku", "type": "quantitative"}
        ],
        "x": {
          "field": "elderly_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "65歳以上人口（万人）", "grid": true}
        },
        "y": {
          "field": "benefit_oku",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "介護保険給付費（億円）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "size_vs_elderly"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "elderly_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "65歳以上人口（万人）", "grid": true}
        },
        "y": {
          "field": "benefit_oku",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "介護保険給付費（億円）", "grid": true}
        },
        "text": {"field": "pref_name"}
      }
    }
  ]
}
```

給付費は高齢者人口にほぼ比例していて、市場規模の大半は高齢者人口で説明できます。直線より上にある県は高齢者1人あたりの給付が多く、下にある県は少ない県です。1人あたりで上位だった大阪府は直線より上に、下位だった栃木県や茨城県は直線より下にあります。出店候補地を評価するときは、高齢者人口で市場の大きさを見積もり、この直線からのずれで1人あたりの給付の多さを補正できます。

## 業務での使い方

- 市場規模の見積もり: 候補地の高齢者人口に、近隣県や全国平均の高齢者1人あたり給付費（約30.8万円）を掛けると、地域の介護保険給付費の概算が得られる
- 需給の評価: 高齢者1人あたり給付費が全国平均を下回る地域は、高齢者数のわりに給付が少なく、サービス供給を増やす余地が残っている可能性がある
- 伸びの確認: 全国の給付費は2007年度から増え続けている。対象地域の高齢者人口の将来推計と組み合わせれば、中期の市場の伸びを見込める
- 競合の確認: 市場規模の大きい大都市圏は競合も多い。総額と1人あたりの両方を見て、候補地を比較する

この記事の数字は、候補地を最初に絞り込むための参考値です。給付費は都道府県単位の総額なので、サービス種別ごとの内訳や県内の市区町村の差は分かりません。実際の出店判断では、サービス種別ごとの需要、要介護認定者数、競合事業所の分布、人材確保のしやすさと組み合わせて評価してください。

## まとめ

- 全国の介護保険給付費（費用額）は2000年度の約3.5兆円から2023年度の約11.2兆円へ、3倍以上に増えた
- 都道府県別の給付費は高齢者人口に連動し、最も多い東京都（約1兆456億円）と最も少ない鳥取県（約598億円）でおよそ17倍の差がある
- 高齢者1人あたりの給付費は全国平均で約30.8万円。最も多い大阪府（36.0万円）と最も少ない栃木県（26.2万円）で約1.4倍の差があり、上位と下位の県は総額の順位と異なる

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県別福祉データ（`j_pref_welfare`）と人口データ（`a_pref_population`）を、2026年7月11日時点で取得して集計しています。給付費の元データは厚生労働省の[介護保険事業状況報告](https://www.mhlw.go.jp/toukei/list/84-1.html)で、対象期間は2000年度から2023年度です。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の福祉統計テーブル](/datasets/queria/e_stat/ssds/j_pref_welfare)から、自社の対象地域の給付費と高齢者1人あたりの値を計算できます。

```sql id=national_trend
SELECT year AS fiscal_year, ROUND(MAX(TRY_CAST(value AS DOUBLE)) / 100000) AS benefit_oku FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND area = '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=size_top
WITH base AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) / 100000 AS val FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), ranked AS ( SELECT area_name, ROUND(val) AS benefit_oku, ROW_NUMBER() OVER (ORDER BY val DESC, area_name) AS rn FROM base ) SELECT area_name, benefit_oku FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=size_mid
WITH base AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) / 100000 AS val FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), ranked AS ( SELECT area_name, ROUND(val) AS benefit_oku, ROW_NUMBER() OVER (ORDER BY val DESC, area_name) AS rn FROM base ) SELECT area_name, benefit_oku FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=size_bottom
WITH base AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) / 100000 AS val FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), ranked AS ( SELECT area_name, ROUND(val) AS benefit_oku, ROW_NUMBER() OVER (ORDER BY val DESC, area_name) AS rn FROM base ) SELECT area_name, benefit_oku FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=per_elderly_top
WITH ben AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), eld AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS e FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1303' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT b.area_name, ROUND(b.v / e.e / 10, 1) AS per_elderly, ROW_NUMBER() OVER (ORDER BY b.v / e.e DESC, b.area_name) AS rn FROM ben b JOIN eld e ON b.area = e.area ) SELECT area_name, per_elderly FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=per_elderly_mid
WITH ben AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), eld AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS e FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1303' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT b.area_name, ROUND(b.v / e.e / 10, 1) AS per_elderly, ROW_NUMBER() OVER (ORDER BY b.v / e.e DESC, b.area_name) AS rn FROM ben b JOIN eld e ON b.area = e.area ) SELECT area_name, per_elderly FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=per_elderly_bottom
WITH ben AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), eld AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS e FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1303' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT b.area_name, ROUND(b.v / e.e / 10, 1) AS per_elderly, ROW_NUMBER() OVER (ORDER BY b.v / e.e DESC, b.area_name) AS rn FROM ben b JOIN eld e ON b.area = e.area ) SELECT area_name, per_elderly FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=size_vs_elderly
WITH ben AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J7102' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), eld AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS e FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1303' AND year = 2023 AND area <> '00000' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ) SELECT b.area_name AS pref_name, ROUND(e.e / 10000, 1) AS elderly_man, ROUND(b.v / 100000) AS benefit_oku FROM ben b JOIN eld e ON b.area = e.area
```
