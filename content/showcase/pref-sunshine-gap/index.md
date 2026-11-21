---
title: 日照時間の県の差の7割は12〜2月に生じ、6〜8月は新潟県が東京都より98時間長い
description: 年間の日照時間は太平洋側・内陸の都道府県が日本海側の9県より平均348時間長く、その差の7割は12〜2月の3か月で生じます。6〜8月は新潟県547時間、東京都449時間で、順位が入れ替わります。
publishedAt: 2026-03-10
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 気象
  - 気候
  - 都道府県格差
datasets:
  - queria/e_stat
  - queria/jma
sources:
  - title: 平年値（統計期間1991〜2020年）
    url: https://www.data.jma.go.jp/stats/data/mdrr/normal/index.html
    publisher: 気象庁
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（B 自然環境）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/B
    publisher: 総務省統計局
  - title: 気象観測統計指針
    url: https://www.jma.go.jp/jma/kishou/know/stats/shishin/shishin_all.pdf
    publisher: 気象庁
agentHint: 日照時間の日別平年値を3〜5月と9〜11月で県ごとに足して、春と秋にも日本海側の9県と太平洋側・内陸の差がどれだけ残るかを確かめて
socialAnnounce: |-
  日照時間の県の差は、大半が冬に生まれていました。
  日本海側の9県と太平洋側・内陸の差は年348時間、うち7割が12〜2月の3か月で生まれます。
  6〜8月は新潟県547時間、東京都449時間。夏は順位が入れ替わります。
---

年間の日照時間の平年値は、太平洋側・内陸の都道府県の平均が、日本海側の9県の平均より348時間長く、その差の70%（244時間）は12〜2月の3か月で生じます。5〜8月の4か月は日本海側の9県のほうが合計で18時間長く、6〜8月の日照時間は新潟県が547時間、東京都が449時間です。

都道府県別の年間の日照時間は、山梨県の2,225時間が最も長く、秋田県の1,527時間が最も短く、698時間の差があります。下位10県のうち9県は青森・秋田・山形・新潟・富山・石川・福井・鳥取・島根の日本海側の県です。

## 日本海側の9県との差は、11月から2月に生じる

使ったのは気象庁の[平年値](https://www.data.jma.go.jp/stats/data/mdrr/normal/index.html)のうち、日照時間の日別平年値（`jma.main.mart_jma_normals_daily` の `sunshine_hours`、1991〜2020年の30年平均）です。これを月ごとに合計し、各都道府県を代表する観測所1か所の値として扱います。代表地点は e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)が都道府県の日照時間（`B4108`）に使っている地点と同じで、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)のとおり県庁所在地の観測所です。埼玉県は熊谷、東京都は千代田区の東京、滋賀県は彦根を使っています。県内の山間部や沿岸部の違いはこの値には含まれません。

地域は、日本海側の9県（青森・秋田・山形・新潟・富山・石川・福井・鳥取・島根）、沖縄県、それ以外の37都道府県（太平洋側・内陸）の3つに分けました。気象庁の気候区分とは異なる、この記事での分け方です。北海道の代表地点の札幌は冬の日照が日本海側の県に近いものの、太平洋側・内陸に含めています。

```chart
{
  "layer": [
    {
      "data": {"name": "monthly_group"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"pacific\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "month", "type": "quantitative"},
          {"field": "pacific", "type": "quantitative"}
        ],
        "x": {
          "field": "month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "pacific",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "月間の日照時間・平年値（時間）", "grid": true}
        },
        "color": {
          "datum": "太平洋側・内陸（37都道府県の平均）",
          "type": "nominal",
          "scale": {
            "domain": ["太平洋側・内陸（37都道府県の平均）", "日本海側（9県の平均）", "沖縄県"],
            "range": ["#f97316", "#3b82f6", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "monthly_group"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"sea\"]) ? 0 : 1",
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
          {"field": "month", "type": "quantitative"},
          {"field": "sea", "type": "quantitative"}
        ],
        "x": {
          "field": "month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "sea",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "月間の日照時間・平年値（時間）", "grid": true}
        },
        "color": {
          "datum": "日本海側（9県の平均）",
          "type": "nominal",
          "scale": {
            "domain": ["太平洋側・内陸（37都道府県の平均）", "日本海側（9県の平均）", "沖縄県"],
            "range": ["#f97316", "#3b82f6", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "monthly_group"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"month\"]) && isValid(datum[\"okinawa\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "month", "type": "quantitative"},
          {"field": "okinawa", "type": "quantitative"}
        ],
        "x": {
          "field": "month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "okinawa",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "月間の日照時間・平年値（時間）", "grid": true}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["太平洋側・内陸（37都道府県の平均）", "日本海側（9県の平均）", "沖縄県"],
            "range": ["#f97316", "#3b82f6", "#22c55e"]
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

1月は太平洋側・内陸の平均が153.4時間、日本海側の9県の平均が62.3時間で、2.5倍の差があります。11月から2月まで、太平洋側・内陸は毎月150時間前後で、日本海側は60〜100時間ほどです。冬の北西の季節風が日本海で水蒸気を受け取り、山地の手前で雲と雪になるためとされています。

4月を過ぎると2つの地域の値はほぼ同じになります。5月は日本海側201.3時間・太平洋側197.7時間、6月は日本海側162.4時間・太平洋側143.0時間で、梅雨の6月は日本海側のほうが19時間長くなります。8月はどちらも195時間台です。

月ごとの差を合計すると、次のようになります。

```sql
SELECT * FROM gap_summary
```

年間の差348時間のうち、244時間（70%）が12〜2月の3か月で生じます。11月を含めた4か月では84%です。5〜8月の4か月の差を合計すると、日本海側のほうが18時間長くなります。

沖縄県は季節による変化の仕方が異なります。1月は91.2時間と日本海側に近い短さですが、7月は226.1時間で、どの地域のどの月よりも長くなります。年間で1,727時間と短めなのは、11月から5月がいずれも140時間未満のためです。

## 関東の内陸と日本海側の県では、冬と夏の順位が入れ替わる

都道府県ごとに、冬（12〜2月）と夏（6〜8月）の日照時間を並べました。横軸が冬、縦軸が夏です。

```chart
{
  "layer": [
    {
      "data": {"name": "season_pacific"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "winter", "type": "quantitative"},
          {"field": "summer", "type": "quantitative"}
        ],
        "x": {
          "field": "winter",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "冬（12〜2月）の日照時間・平年値（時間）", "grid": true}
        },
        "y": {
          "field": "summer",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "夏（6〜8月）の日照時間・平年値（時間）", "grid": true}
        },
        "color": {
          "datum": "太平洋側・内陸",
          "type": "nominal",
          "scale": {
            "domain": ["太平洋側・内陸", "日本海側", "沖縄県"],
            "range": ["#f97316", "#3b82f6", "#22c55e"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "season_sea"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "winter", "type": "quantitative"},
          {"field": "summer", "type": "quantitative"}
        ],
        "x": {
          "field": "winter",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "冬（12〜2月）の日照時間・平年値（時間）", "grid": true}
        },
        "y": {
          "field": "summer",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "夏（6〜8月）の日照時間・平年値（時間）", "grid": true}
        },
        "color": {
          "datum": "日本海側",
          "type": "nominal",
          "scale": {
            "domain": ["太平洋側・内陸", "日本海側", "沖縄県"],
            "range": ["#f97316", "#3b82f6", "#22c55e"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "season_okinawa"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "winter", "type": "quantitative"},
          {"field": "summer", "type": "quantitative"}
        ],
        "x": {
          "field": "winter",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "冬（12〜2月）の日照時間・平年値（時間）", "grid": true}
        },
        "y": {
          "field": "summer",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "夏（6〜8月）の日照時間・平年値（時間）", "grid": true}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["太平洋側・内陸", "日本海側", "沖縄県"],
            "range": ["#f97316", "#3b82f6", "#22c55e"]
          },
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

点は横に大きく広がり、縦の広がりは小さくなっています。47都道府県の最大と最小の差は、冬が468時間、夏が224時間で、年間の順位は主に冬の日照時間で決まります。

```sql
SELECT * FROM season_spread
```

関東の内陸と日本海側の県では、冬と夏の順位が入れ替わります。冬に最も日照時間が長い埼玉県（熊谷、615時間）は、夏には448時間で47都道府県中43位です。冬4位の栃木県（宇都宮）は、夏が376時間で最下位です。東京都も冬10位・夏42位です。冬45位の新潟県は夏が547時間で9位、冬44位の石川県は夏10位です。年間2位の高知県は、夏だけでは28位です。夏の1位は和歌山県の600時間、2位は沖縄県の593時間です。冬と夏の相関係数は-0.29で、冬に長い県ほど夏に短いという関係は弱いものです。兵庫県・香川県・愛媛県のように、夏が上位で冬も中位の県があるためです。

47都道府県の値と順位は次のとおりです（年間の多い順）。

```sql
SELECT area_name AS "都道府県", grp AS "地域区分", annual AS "年間（時間）", annual_rank AS "年間の順位", winter AS "冬 12〜2月（時間）", winter_rank AS "冬の順位", summer AS "夏 6〜8月（時間）", summer_rank AS "夏の順位" FROM pref_season ORDER BY annual_rank, area_name
```

## 年ごとの観測値でも、1990年以降は毎年太平洋側・内陸が日本海側を上回る

平年値は30年の平均なので、年ごとの観測値でも同じ差があるかを、社会・人口統計体系の年間日照時間（`B4108`、1975〜2024年）で確認します。2024年の最多は高知県、最少は山形県でした。

```sql
SELECT * FROM latest_extremes
```

```chart
{
  "layer": [
    {
      "data": {"name": "yearly_group"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pacific\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "pacific", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "pacific",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年間の日照時間（時間）", "grid": true}
        },
        "color": {
          "datum": "太平洋側・内陸（平均）",
          "type": "nominal",
          "scale": {"domain": ["太平洋側・内陸（平均）", "日本海側（平均）"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "yearly_group"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"sea\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "sea", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "sea",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年間の日照時間（時間）", "grid": true}
        },
        "color": {
          "datum": "日本海側（平均）",
          "type": "nominal",
          "scale": {"domain": ["太平洋側・内陸（平均）", "日本海側（平均）"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rect", "color": "#94a3b8", "opacity": 0.15},
      "encoding": {
        "x": {"datum": 1985.5, "type": "quantitative"},
        "x2": {"datum": 1989.5, "type": "quantitative"},
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
        "x": {"datum": 1987.5, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "日照計の切り替え"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

灰色の帯は、気象庁が日照計をジョルダン式から回転式へ切り替えた1986〜1989年です。[気象観測統計指針](https://www.jma.go.jp/jma/kishou/know/stats/shishin/shishin_all.pdf)は、ジョルダン式で観測した月の値を回転式に換算するとき、75時間以上の月は15時間を差し引き、75時間未満の月は0.8を掛けると定めています。同じ天気でもジョルダン式のほうが長く記録されます。社会・人口統計体系の値は切り替え前も観測値のままなので、帯の前後で水準や差の大きさは比較できません。

切り替えが終わった1990年以降は、太平洋側・内陸の平均が毎年、日本海側の平均を上回っています。差は年によって238時間から538時間まで変わり、1990年代の平均は351時間、直近10年の平均は320時間です。年ごとの変動と比較して小さな違いなので、差が縮んだとは判断できません。値が欠けている年は、その年に値のある県だけで平均しています。欠けているのは、日本海側では2015年の新潟県、太平洋側・内陸では1982年の岡山県、1993年の和歌山県、2009年の愛知県、2021年の広島県です。

```sql
SELECT * FROM gap_by_period
```

## 太陽光発電の計画にあてはめる

太陽光発電の設置や発電量の見通しを県ごとに比較するとき、年間の日照時間の順位だけでは季節ごとの違いが分かりません。

- 日本海側の県の年間348時間の不足は、84%が11〜2月の4か月で生じます。5〜8月の日照時間は太平洋側・内陸とほぼ同じなので、月別の発電見込みでは冬の減少を大きく見込み、夏は太平洋側・内陸と同じ水準を見込めます
- 関東の内陸は、埼玉県・群馬県・栃木県の冬の日照が全国で4位以内、夏は41位以下です。3県とも夏は全国で下から7番以内なので、夏の発電を年間の順位から見積もると多めになります
- 日照時間は直射日光が当たった時間の合計で、日射量とは異なります。夏は太陽が高く同じ1時間でも日射が強いので、発電量の見積もりには日射量の値を別に使います

## データの出典

本記事は気象庁の[平年値](https://www.data.jma.go.jp/stats/data/mdrr/normal/index.html)（統計期間1991〜2020年）の日別平年値と、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別の年間日照時間（`B4108`）を、2026年10月12日時点で集計しています。社会・人口統計体系の値は気象庁の観測値で、`time_name` は「年度」と表記されていますが、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)のとおり1月から12月の暦年の合計です。

Queriaは、官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[気象庁の日別平年値のテーブル](/datasets/queria/jma/main/mart_jma_normals_daily)と[都道府県別の自然環境データのテーブル](/datasets/queria/e_stat/ssds/b_pref_land)から、自分の地域の観測所の月ごとの日照時間や、気温・降水量の季節ごとの変化を確認できます。

```sql id=stations
-- 都道府県の値を代表する観測所（社会・人口統計体系の項目定義の注意事項による）と、記事の地域区分。プロットはしない
SELECT * FROM (VALUES ('北海道', '14163', '太平洋側・内陸'), ('青森県', '31312', '日本海側'), ('岩手県', '33431', '太平洋側・内陸'), ('宮城県', '34392', '太平洋側・内陸'), ('秋田県', '32402', '日本海側'), ('山形県', '35426', '日本海側'), ('福島県', '36127', '太平洋側・内陸'), ('茨城県', '40201', '太平洋側・内陸'), ('栃木県', '41277', '太平洋側・内陸'), ('群馬県', '42251', '太平洋側・内陸'), ('埼玉県', '43056', '太平洋側・内陸'), ('千葉県', '45212', '太平洋側・内陸'), ('東京都', '44132', '太平洋側・内陸'), ('神奈川県', '46106', '太平洋側・内陸'), ('新潟県', '54232', '日本海側'), ('富山県', '55102', '日本海側'), ('石川県', '56227', '日本海側'), ('福井県', '57066', '日本海側'), ('山梨県', '49142', '太平洋側・内陸'), ('長野県', '48156', '太平洋側・内陸'), ('岐阜県', '52586', '太平洋側・内陸'), ('静岡県', '50331', '太平洋側・内陸'), ('愛知県', '51106', '太平洋側・内陸'), ('三重県', '53133', '太平洋側・内陸'), ('滋賀県', '60131', '太平洋側・内陸'), ('京都府', '61286', '太平洋側・内陸'), ('大阪府', '62078', '太平洋側・内陸'), ('兵庫県', '63518', '太平洋側・内陸'), ('奈良県', '64036', '太平洋側・内陸'), ('和歌山県', '65042', '太平洋側・内陸'), ('鳥取県', '69122', '日本海側'), ('島根県', '68132', '日本海側'), ('岡山県', '66408', '太平洋側・内陸'), ('広島県', '67437', '太平洋側・内陸'), ('山口県', '81286', '太平洋側・内陸'), ('徳島県', '71106', '太平洋側・内陸'), ('香川県', '72086', '太平洋側・内陸'), ('愛媛県', '73166', '太平洋側・内陸'), ('高知県', '74182', '太平洋側・内陸'), ('福岡県', '82182', '太平洋側・内陸'), ('佐賀県', '85142', '太平洋側・内陸'), ('長崎県', '84496', '太平洋側・内陸'), ('熊本県', '86141', '太平洋側・内陸'), ('大分県', '83216', '太平洋側・内陸'), ('宮崎県', '87376', '太平洋側・内陸'), ('鹿児島県', '88317', '太平洋側・内陸'), ('沖縄県', '91197', '沖縄')) AS t(area_name, station_id, grp)
```

```sql id=monthly_group
-- 日別平年値（1991〜2020年）を月ごとに足し、地域区分ごとに県の平均をとる。2月29日の平年値は平年の合計に入れない
WITH m AS (SELECT s.area_name, s.grp, n.month, CAST(SUM(CAST(n.sunshine_hours AS DECIMAL(18, 4))) AS DOUBLE) AS h FROM jma.main.mart_jma_normals_daily n JOIN stations s USING (station_id) WHERE NOT (n.month = 2 AND n.day = 29) GROUP BY s.area_name, s.grp, n.month)
SELECT month, ROUND(AVG(h) FILTER (WHERE grp = '日本海側'), 1) AS sea, ROUND(AVG(h) FILTER (WHERE grp = '太平洋側・内陸'), 1) AS pacific, ROUND(AVG(h) FILTER (WHERE grp = '沖縄'), 1) AS okinawa FROM m GROUP BY month ORDER BY month
```

```sql id=gap_summary
-- 太平洋側・内陸の平均から日本海側の平均を引いた差を、期間ごとに足す
WITH d AS (SELECT month, pacific - sea AS gap FROM monthly_group)
SELECT ROUND(SUM(gap)) AS "年間の差（時間）", ROUND(SUM(gap) FILTER (WHERE month IN (12, 1, 2))) AS "12〜2月の差（時間）", ROUND(SUM(gap) FILTER (WHERE month IN (12, 1, 2)) / SUM(gap) * 100) AS "12〜2月の割合（%）", ROUND(SUM(gap) FILTER (WHERE month IN (11, 12, 1, 2))) AS "11〜2月の差（時間）", ROUND(SUM(gap) FILTER (WHERE month IN (11, 12, 1, 2)) / SUM(gap) * 100) AS "11〜2月の割合（%）", ROUND(SUM(gap) FILTER (WHERE month IN (5, 6, 7, 8))) AS "5〜8月の差（時間）" FROM d
```

```sql id=pref_season
-- 県ごとの年間・冬（12〜2月）・夏（6〜8月）の日照時間の平年値と順位
WITH m AS (SELECT s.area_name, s.grp, n.month, CAST(SUM(CAST(n.sunshine_hours AS DECIMAL(18, 4))) AS DOUBLE) AS h FROM jma.main.mart_jma_normals_daily n JOIN stations s USING (station_id) WHERE NOT (n.month = 2 AND n.day = 29) GROUP BY s.area_name, s.grp, n.month), p AS (SELECT area_name, grp, SUM(h) AS annual, SUM(h) FILTER (WHERE month IN (12, 1, 2)) AS winter, SUM(h) FILTER (WHERE month IN (6, 7, 8)) AS summer FROM m GROUP BY area_name, grp)
SELECT area_name, grp, ROUND(annual) AS annual, ROUND(winter) AS winter, ROUND(summer) AS summer, RANK() OVER (ORDER BY annual DESC) AS annual_rank, RANK() OVER (ORDER BY winter DESC) AS winter_rank, RANK() OVER (ORDER BY summer DESC) AS summer_rank FROM p ORDER BY annual_rank, area_name
```

```sql id=season_spread
-- 47都道府県の中での最大と最小の差（冬と夏）。プロットはしない
SELECT ROUND(MAX(winter) - MIN(winter)) AS "冬の最大と最小の差（時間）", ROUND(MAX(summer) - MIN(summer)) AS "夏の最大と最小の差（時間）", ROUND(CORR(winter, summer), 2) AS "冬と夏の相関係数" FROM pref_season
```

```sql id=yearly_group
-- 社会・人口統計体系の年間日照時間（B4108）を地域区分ごとに平均する。値の欠けた県はその年の平均から外れる
WITH v AS (SELECT b.year, s.grp, TRY_CAST(b.value AS DOUBLE) AS h FROM e_stat.ssds.b_pref_land b JOIN stations s ON b.area_name = s.area_name WHERE b.cat01 = 'B4108' AND TRY_CAST(b.value AS DOUBLE) IS NOT NULL AND b.year <= 2024)
SELECT year, ROUND(AVG(h) FILTER (WHERE grp = '日本海側')) AS sea, ROUND(AVG(h) FILTER (WHERE grp = '太平洋側・内陸')) AS pacific, ROUND(AVG(h) FILTER (WHERE grp = '太平洋側・内陸') - AVG(h) FILTER (WHERE grp = '日本海側')) AS gap, COUNT(*) FILTER (WHERE grp = '日本海側') AS sea_n FROM v GROUP BY year ORDER BY year
```

```sql id=gap_by_period
-- 日照計の切り替え（1986〜1989年）が済んだ1990年以降で、全体と最初・最後の10年の差を比べる。プロットはしない
SELECT p.label AS "期間", ROUND(AVG(g.gap)) AS "差の平均（時間）", MIN(g.gap) AS "差の最小（時間）", MAX(g.gap) AS "差の最大（時間）" FROM yearly_group g JOIN (VALUES (1, '1990〜2024年', 1990, 2024), (2, '1990〜1999年', 1990, 1999), (3, '2015〜2024年', 2015, 2024)) AS p(ord, label, y0, y1) ON g.year BETWEEN p.y0 AND p.y1 GROUP BY p.ord, p.label ORDER BY p.ord
```

```sql id=latest_extremes
-- 2024年の最多と最少。プロットはしない
WITH r AS (SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE)) AS h, RANK() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC) AS rk_desc, RANK() OVER (ORDER BY TRY_CAST(value AS DOUBLE)) AS rk_asc FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4108' AND year = 2024 AND TRY_CAST(value AS DOUBLE) IS NOT NULL)
SELECT area_name AS "都道府県", h AS "2024年の日照時間（時間）", CASE WHEN rk_desc = 1 THEN '最多' ELSE '最少' END AS "順位" FROM r WHERE rk_desc = 1 OR rk_asc = 1 ORDER BY h DESC
```

```sql id=season_pacific
SELECT area_name, winter, summer FROM pref_season WHERE grp = '太平洋側・内陸'
```

```sql id=season_sea
SELECT area_name, winter, summer FROM pref_season WHERE grp = '日本海側'
```

```sql id=season_okinawa
SELECT area_name, winter, summer FROM pref_season WHERE grp = '沖縄'
```
