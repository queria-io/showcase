---
title: 大卒初任給の最高県と最低県の比は42年で1.22倍から1.25倍になり、沖縄県だけが中央値から離れた
description: 1977〜2019年の都道府県別の大卒男性初任給を集計しました。最高県と最低県の金額の差は約3倍になりましたが、5年平均の比は1.22倍から1.25倍です。1993〜2019年の27年中24年は沖縄県が最低でした
publishedAt: 2026-03-03
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 初任給
  - 労働
  - 地域格差
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 賃金構造基本統計調査
    url: https://www.mhlw.go.jp/toukei/list/chinginkouzou.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 高校卒男性の初任給（F6401）でも、1993年以降に沖縄県が最低の年が続いているか、年ごとの最低の県を並べて確かめて
socialAnnounce: |-
  大卒初任給の県ごとの差は広がったのか。
  1977〜2019年の都道府県別データでは、金額の差は約3倍になっても、比の広がりはわずかでした。

  新卒採用の給与設定に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

大卒男性の初任給の最高県と最低県の差は、1977年の1万6,700円から2019年の4万9,400円へ、金額では約3倍になりました。最高県が最低県の何倍かを5年平均で見ると、1977〜1979年の1.22倍から2015〜2019年の1.25倍で、比はわずかしか広がっていません。沖縄県は全国の中央値の0.94倍から0.87倍に下がり、1993〜2019年の27年中24年で最低でした。

2019年に大学を出て就職した男性の初任給は、東京都で月22万4,100円、沖縄県で17万4,700円で、差は4万9,400円です。1977年の最高（東京都10万4,700円）と最低（鳥取県8万8,000円）の差は1万6,700円でした。同じ期間に、全国の初任給も10万1,000円から21万2,800円へ約2.1倍になっています。最高県が最低県の何倍かで比較すると、1977年は1.19倍、2019年は1.28倍です。1年だけの比は年によって大きく変わり、1977年はその後の数年より低い年です。

```sql
SELECT * FROM ends
```

## 大卒男性の初任給は、1977年から2019年まで同じ調査の値がある

[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)（厚生労働省）の都道府県別の値を、e-Stat「社会・人口統計体系」の都道府県別労働データ（`f_pref_labor`）から取得しています。新規学卒者の給与は学歴と性別の組み合わせで収録されていて、2019年までと2020年からで項目が分かれています。

| 学歴・性別         | 初任給（〜2019年）    | 所定内給与額（2020年〜） |
| ------------------ | --------------------- | ------------------------ |
| 高校卒（男）       | F6401（1975〜2019年） | F6407                    |
| 高校卒（女）       | F6402（1975〜2019年） | F6408                    |
| 高専・短大卒（男） | F6406（2019年のみ）   | F6409                    |
| 高専・短大卒（女） | F6404（1975〜2019年） | F6410                    |
| 大学卒（男）       | F6403（1975〜2019年） | F6411                    |
| 大学卒（女）       | F6405（2019年のみ）   | F6412                    |

この記事の「大卒初任給」は、大学卒（男）の新規学卒者初任給（`F6403`）です。[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/F)によると、新規学卒者の初任給は1976年度まで職業安定局の「新規学卒者の初任給調査」で集計され、その後は賃金構造基本統計調査で集計されています。この記事では、同じ調査の値がある1977年以降を比較します。2020年からの新規学卒者所定内給与額（`F6411`）は最後の節で扱います。

## 金額の差は約3倍になり、比はわずかに広がった

各年の47都道府県について、最高県÷最低県と、上から10番目の県÷下から10番目の県を並べました。最高県÷最低県は両端の2県だけで決まり、上から10番目÷下から10番目は47都道府県の中ほどの差を表します。2020年からの点は定義の違う系列なので、線をつないでいません。

```chart
{
  "layer": [
    {
      "data": {"name": "spread_old"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"max_min\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "max_min", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "max_min",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "倍", "grid": true}
        },
        "color": {
          "datum": "最高県÷最低県",
          "type": "nominal",
          "scale": {
            "domain": ["最高県÷最低県", "上から10番目÷下から10番目", "最高県÷最低県（2020年〜）", "上から10番目÷下から10番目（2020年〜）"],
            "range": ["#ef4444", "#3b82f6", "#fca5a5", "#93c5fd"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "spread_old"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tenth\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "tenth", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tenth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "倍", "grid": true}
        },
        "color": {
          "datum": "上から10番目÷下から10番目",
          "type": "nominal",
          "scale": {
            "domain": ["最高県÷最低県", "上から10番目÷下から10番目", "最高県÷最低県（2020年〜）", "上から10番目÷下から10番目（2020年〜）"],
            "range": ["#ef4444", "#3b82f6", "#fca5a5", "#93c5fd"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "spread_new"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "max_min", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "max_min",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "倍", "grid": true}
        },
        "color": {
          "datum": "最高県÷最低県（2020年〜）",
          "type": "nominal",
          "scale": {
            "domain": ["最高県÷最低県", "上から10番目÷下から10番目", "最高県÷最低県（2020年〜）", "上から10番目÷下から10番目（2020年〜）"],
            "range": ["#ef4444", "#3b82f6", "#fca5a5", "#93c5fd"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "spread_new"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tenth", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tenth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "倍", "grid": true}
        },
        "color": {
          "datum": "上から10番目÷下から10番目（2020年〜）",
          "type": "nominal",
          "scale": {
            "domain": ["最高県÷最低県", "上から10番目÷下から10番目", "最高県÷最低県（2020年〜）", "上から10番目÷下から10番目（2020年〜）"],
            "range": ["#ef4444", "#3b82f6", "#fca5a5", "#93c5fd"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2019.5, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

最高県÷最低県は、1977年から2019年までおおむね1.2倍前後で上下しています。2011年のように最高と最低の両方が前後の年と大きく異なり比が1.5倍になる年や、2001年のように最低の県だけが下がって1.3倍を超える年もありますが、翌年には元の水準に戻ります。賃金構造基本統計調査は事業所を抽出した標本調査なので、県ごとの1年だけの値には標本による誤差が含まれます。5年ごとの平均で並べると次のとおりです。

```sql
SELECT * FROM period_avg
```

最高県÷最低県は、1977〜1979年の1.22倍から1990〜1994年に1.19倍まで縮み、2000年代に1.2倍台半ばに戻りました。2010〜2014年の1.32倍は、比が1.5倍になった2011年を含む値です。2015〜2019年は1.25倍で、1977〜1979年をわずかに上回る水準です。上から10番目÷下から10番目はどの期間も1.07〜1.09倍で、47都道府県の中ほどの差はほとんど変わっていません。

## 中央値から離れたのは沖縄県で、沖縄県を除くと比は縮んでいる

東京都と沖縄県の初任給を、47都道府県の中央値と比較しました。

```chart
{
  "layer": [
    {
      "data": {"name": "rel"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokyo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "47都道府県の中央値に対する比", "grid": true}
        },
        "color": {
          "datum": "東京都÷中央値",
          "type": "nominal",
          "scale": {"domain": ["東京都÷中央値", "沖縄県÷中央値"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "rel"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"okinawa\"]) ? 0 : 1",
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
          {"field": "okinawa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "okinawa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "47都道府県の中央値に対する比", "grid": true}
        },
        "color": {
          "datum": "沖縄県÷中央値",
          "type": "nominal",
          "scale": {"domain": ["東京都÷中央値", "沖縄県÷中央値"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8"},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 1, "type": "quantitative"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

5年ごとの平均で見ると、東京都は中央値の1.08倍（1977〜1979年）から1990年代に1.06倍まで下がり、2000年代以降は1.09〜1.12倍です。2015〜2019年の1.09倍は、1977〜1979年とほぼ同じ水準です。沖縄県は0.94倍から2000〜2004年の0.86倍まで下がり、その後は0.87〜0.88倍です。沖縄県を除いて最高県÷最低県を計算し直すと、1977〜1979年の1.21倍に対して2015〜2019年は1.18倍で、比は縮んでいます。

最低の県も時期によって変わっています。1977〜1992年の16年間は9つの県が年によって最低になり、沖縄県が最低だったのは2年だけでした。1993〜2019年の27年間では24年が沖縄県です。1年ごとの順位には標本による誤差が含まれますが、27年中24年という偏りは誤差だけでは説明しにくいものです。

```sql
SELECT * FROM lowest
```

## 2019年は東京都の22万4,100円が最も高く、沖縄県の17万4,700円が最も低い

```map
type: map
layers:
  - from: salary_map
    geojson: geojson
    color: salary
    label: pref_name
    name: "初任給（円）"
lng: 137
lat: 36.5
zoom: 4
```

2019年は東京都（22万4,100円）に大阪府・愛知県・神奈川県など6府県が21万円台で続き、29位の和歌山県から45位の岩手県までの17道県が19万円台です。沖縄県（17万4,700円）は、46位の宮崎県（18万9,000円）よりさらに1万4,300円低くなっています。自県の初任給を東京都との金額の差で見ると、初任給全体が上がるにつれて差も大きくなります。47都道府県の中央値との比で見ると、全体の上昇の影響を除いて自県の位置を確認できます。

## 2020年からの系列でも、沖縄県は5年中4年で最低

2020年から、同じ調査の都道府県別の値は新規学卒者所定内給与額（`F6411`）に替わりました。2019年までの初任給は通勤手当を除いた額で、2020年からは通勤手当を含むので、金額は2019年までの値と比較できません。

```sql
SELECT * FROM recent
```

この系列でも、沖縄県は5年中4年で最低です。1年ごとの変動は2019年までより大きく、2023年は沖縄県が25万2,400円で東京都（24万4,500円）を上回り、2024年は群馬県が31万7,900円で最も高くなっています。最初の図で2020年からの比が高いのも、この変動を含んだ値です。5年分の値では、差が広がり始めたのか、変動が大きくなっただけなのかは判断できません。

## まとめ

- 大卒男性の初任給の最高県と最低県の差は、1977年の1万6,700円から2019年の4万9,400円へ約3倍になった。同じ期間に初任給全体も約2.1倍になっている
- 5年平均の最高県÷最低県は1.22倍（1977〜1979年）から1.25倍（2015〜2019年）で、比はわずかに広がった。沖縄県を除くと1.21倍から1.18倍に縮む
- 沖縄県は中央値の0.94倍から0.87倍へ下がり、1993〜2019年の27年中24年で最低だった

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別労働データを2026年9月24日時点で集計しています。元データは厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)で、金額は各年6月分の名目値です。

Queriaは、e-Statなどの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[都道府県別の労働データのテーブル](/datasets/queria/e_stat/ssds/f_pref_labor)から、自県の初任給と47都道府県の中での順位を年ごとに確認できます。

```sql id=ends
WITH p AS (SELECT year, area_name, CAST(ROUND(TRY_CAST(value AS DOUBLE) * 1000) AS INTEGER) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6403' AND year IN (1977, 2019) AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT year AS "年", MAX(v) FILTER (WHERE area_name = '全国') AS "全国（円）", arg_max(area_name, v) FILTER (WHERE area_name != '全国') AS "最高の県", MAX(v) FILTER (WHERE area_name != '全国') AS "最高額（円）", arg_min(area_name, v) FILTER (WHERE area_name != '全国') AS "最低の県", MIN(v) FILTER (WHERE area_name != '全国') AS "最低額（円）", MAX(v) FILTER (WHERE area_name != '全国') - MIN(v) FILTER (WHERE area_name != '全国') AS "差（円）", ROUND(MAX(v) FILTER (WHERE area_name != '全国') / MIN(v) FILTER (WHERE area_name != '全国'), 2) AS "比（最高÷最低）" FROM p GROUP BY year ORDER BY year
```

```sql id=spread_old
WITH p AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6403' AND area_name != '全国' AND year BETWEEN 1977 AND 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v DESC, area_name) AS hi, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v, area_name) AS lo FROM p) SELECT year, ROUND(MAX(v) / MIN(v), 3) AS max_min, ROUND(MAX(v) FILTER (WHERE hi = 10) / MAX(v) FILTER (WHERE lo = 10), 3) AS tenth FROM r GROUP BY year ORDER BY year
```

```sql id=spread_new
WITH p AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6411' AND area_name != '全国' AND year BETWEEN 2020 AND 2024 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v DESC, area_name) AS hi, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v, area_name) AS lo FROM p) SELECT year, ROUND(MAX(v) / MIN(v), 3) AS max_min, ROUND(MAX(v) FILTER (WHERE hi = 10) / MAX(v) FILTER (WHERE lo = 10), 3) AS tenth FROM r GROUP BY year ORDER BY year
```

```sql id=period_avg
WITH p AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6403' AND area_name != '全国' AND year BETWEEN 1977 AND 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v DESC, area_name) AS hi, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v, area_name) AS lo, MEDIAN(v) OVER (PARTITION BY year) AS med FROM p), y AS (SELECT year, MAX(v) / MIN(v) AS max_min, MAX(v) FILTER (WHERE area_name != '沖縄県') / MIN(v) FILTER (WHERE area_name != '沖縄県') AS max_min_ex, MAX(v) FILTER (WHERE hi = 10) / MAX(v) FILTER (WHERE lo = 10) AS tenth, MAX(v / med) FILTER (WHERE area_name = '東京都') AS tokyo, MAX(v / med) FILTER (WHERE area_name = '沖縄県') AS okinawa FROM r GROUP BY year), b AS (SELECT *, GREATEST(1980 + 5 * CAST(FLOOR((year - 1980) / 5) AS INTEGER), 1977) AS s FROM y) SELECT s || '〜' || MAX(year) || '年' AS "期間（平均）", ROUND(AVG(max_min), 2) AS "最高県÷最低県", ROUND(AVG(max_min_ex), 2) AS "沖縄県を除く最高県÷最低県", ROUND(AVG(tenth), 2) AS "上から10番目÷下から10番目", ROUND(AVG(tokyo), 2) AS "東京都÷中央値", ROUND(AVG(okinawa), 2) AS "沖縄県÷中央値" FROM b GROUP BY s ORDER BY s
```

```sql id=rel
WITH p AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6403' AND area_name != '全国' AND year BETWEEN 1977 AND 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), m AS (SELECT year, MEDIAN(v) AS med FROM p GROUP BY year) SELECT p.year, ROUND(MAX(v / med) FILTER (WHERE area_name = '東京都'), 3) AS tokyo, ROUND(MAX(v / med) FILTER (WHERE area_name = '沖縄県'), 3) AS okinawa FROM p JOIN m USING (year) GROUP BY p.year ORDER BY p.year
```

```sql id=lowest
WITH p AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F6403', 'F6411') AND area_name != '全国' AND year BETWEEN 1977 AND 2024 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT *, RANK() OVER (PARTITION BY year ORDER BY v) AS rk, CASE WHEN year <= 1992 THEN '1977〜1992年' WHEN year <= 2019 THEN '1993〜2019年' ELSE '2020〜2024年' END AS period FROM p), n AS (SELECT period, COUNT(DISTINCT year) AS years FROM r GROUP BY period), c AS (SELECT period, area_name, COUNT(*) AS cnt FROM r WHERE rk = 1 GROUP BY period, area_name) SELECT n.period AS "期間", n.years AS "年数", COALESCE(MAX(c.cnt) FILTER (WHERE c.area_name = '沖縄県'), 0) AS "沖縄県が最低だった年", string_agg(c.area_name || '（' || c.cnt || '）', '、' ORDER BY c.cnt DESC, c.area_name) AS "最低だった県（年数）" FROM n JOIN c USING (period) GROUP BY n.period, n.years ORDER BY n.period
```

```sql id=salary_map
SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, l.salary * 1000 AS salary FROM nlftp.boundary.prefecture p JOIN ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS salary FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6403' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) l ON p.prefecture_name = l.area_name
```

```sql id=recent
WITH p AS (SELECT year, area_name, CAST(ROUND(TRY_CAST(value AS DOUBLE) * 1000) AS INTEGER) AS v FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F6411' AND year BETWEEN 2020 AND 2024 AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT year AS "年", MAX(v) FILTER (WHERE area_name = '全国') AS "全国（円）", arg_max(area_name, v) FILTER (WHERE area_name != '全国') AS "最高の県", MAX(v) FILTER (WHERE area_name != '全国') AS "最高額（円）", arg_min(area_name, v) FILTER (WHERE area_name != '全国') AS "最低の県", MIN(v) FILTER (WHERE area_name != '全国') AS "最低額（円）", MAX(v) FILTER (WHERE area_name = '東京都') AS "東京都（円）", MAX(v) FILTER (WHERE area_name = '沖縄県') AS "沖縄県（円）" FROM p GROUP BY year ORDER BY year
```
