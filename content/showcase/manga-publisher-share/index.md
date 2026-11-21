---
title: マンガ単行本の刊行点数は約50年で30倍に増え、2012〜2021年はKADOKAWAが3位
description: メディア芸術データベースのマンガ単行本書誌31万点を集計しました。刊行点数は1970年の411点から2019年の12,684点まで約30倍に増え、2016〜2019年は年1万2千点台で頭打ちになり、2020・2021年はやや減りました。2012〜2021年の刊行点数ではKADOKAWAが講談社・小学館に次ぐ3位です。
publishedAt: 2026-07-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - メディア芸術
  - マンガ
  - 出版
datasets:
  - queria/mediaarts_db
sources:
  - title: メディア芸術データベース（MADB）
    url: https://mediaarts-db.artmuseums.go.jp/
    publisher: 文化庁・国立アートリサーチセンター
agentHint: レーベル(brand)別の刊行点数を直近10年(2012〜2021年)で多い順に並べて。出版社ランキングでは見えないレーベル単位の勢力図を見たい
socialAnnounce: |-
  メディア芸術データベースのマンガ単行本書誌31万点を数えました。

  刊行点数は約半世紀で30倍に増え、近年は頭打ち。直近10年はKADOKAWAが集英社を抜いて第3位に。
  Queriaは文化のオープンデータを整えて公開しています。
---

マンガ単行本の刊行点数は、1970年の411点から2019年の12,684点まで約30倍に増えました。2016〜2019年は年1万2千点台で増加が止まり、2020・2021年は1万1千点台にやや減っています。2012〜2021年の出版社別の刊行点数は、講談社（15,942点）、小学館（14,123点）、KADOKAWA（11,950点）、集英社（8,939点）の順でした。KADOKAWAは2014年に刊行点数が前年の約2倍になり、それ以降は集英社を上回っています。

この記事では、[メディア芸術データベース](https://mediaarts-db.artmuseums.go.jp/)（MADB）のマンガ単行本書誌から、1970年から2021年までの31万点を集計し、刊行点数の推移と出版社別の内訳を確認しました。

## マンガ単行本書誌は、単行本1巻を1行として収録している

使うのは、MADBのマンガ単行本書誌（`manga_book`）です。日本国内で刊行されたマンガ単行本を1冊（1巻）1レコードで収録し、タイトル・巻数・著者・出版者・レーベル・ISBN・刊行年などを持ちます。この記事で集計するのは刊行点数で、販売部数の情報は含みません。シリーズ名が入っていないレコードも多いので、作品数ではなく巻数で集計しています。

主な列は次のとおりです。

| カラム           | 内容                             |
| ---------------- | -------------------------------- |
| `title`          | 書名（併記の欧文タイトルを含む） |
| `volume`         | 巻次                             |
| `series_name`    | シリーズ名                       |
| `brand`          | レーベル（叢書名）               |
| `publisher_name` | 出版者                           |
| `published_year` | 刊行年                           |

集英社「ジャンプコミックス」の2020年刊行分を数冊表示しました。同じシリーズでも巻ごとに1レコードになっています。

```sql
SELECT split_part(title, ' = ', 1) AS title, volume, brand, published_year FROM mediaarts_db.main.manga_book WHERE publisher_name = '集英社' AND brand = 'ジャンプコミックス' AND published_year = 2020 AND volume IS NOT NULL AND title NOT LIKE '%,%' ORDER BY title LIMIT 6
```

出版者名は「発行元 | ［発売］発売元」の形式で入っている場合があるので、以降の集計では区切り記号の前の発行元で集計しています。角川書店は2013年にKADOKAWAへ統合されたので、両者をKADOKAWAとしてまとめています。これ以外の社名の表記ゆれや、統合・改称のあった出版社はまとめていません。

## 刊行点数は1970年から約30倍に増え、2016年以降は頭打ち

1970年から2021年まで、年ごとのマンガ単行本の刊行点数です。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"n\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#7c3aed", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "n", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行年", "format": "d"}
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行点数（点）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

刊行点数は長期にわたって増え、1970年の411点から2019年には12,684点まで、約30倍になっています。1990年代前半に大きく増え、2000年代後半以降も増加が続きました。2016年（12,486点）以降は年1万2千点台で増えなくなり、2020年（11,612点）・2021年（11,750点）はやや減っています。増加が止まった時期は、電子コミックが普及した2010年代後半とおおむね重なります。電子書籍だけで配信された作品は、このデータベースには収録されていません。

新しい年ほど書誌の収録が終わっていない可能性があり、直近の点数は今後増えることがあります。そのため集計は2021年までにしています。

## 2012〜2021年の刊行点数は、上位3社で約36%を占める

2012〜2021年の刊行点数が多い出版社の上位12社です。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "pub_top"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [{"field": "n", "type": "quantitative"}, {"field": "pub", "type": "nominal"}],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "刊行点数（点、2012〜2021年）", "grid": true}
        },
        "y": {
          "field": "pub",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "出版者"},
          "sort": null
        }
      }
    }
  ]
}
```

上位は講談社（15,942点）、小学館（14,123点）、KADOKAWA（11,950点）、集英社（8,939点）です。この期間の全刊行点数のうち、上位3社で約36%、上位10社で約61%を占めます。上位12社まで広げても65.3%で、残る約3分の1は12社以外の出版者から出ています。芳文社・一迅社・宙出版のように、特定のジャンルを専門にする出版社も一定の点数を刊行しています。

このランキングは刊行点数の順で、販売部数の順ではありません。集英社は上位4社の中では点数が少なく、点数を絞って部数の大きい作品に集中しているためと考えられます。

## KADOKAWAは2014年に刊行点数がほぼ倍になり、集英社を上回った

点数上位の5社について、1990年から2021年までの刊行点数の推移を重ねました。

```chart
{
  "layer": [
    {
      "data": {"name": "pub_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"y\"]) && isValid(datum[\"kodansha\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#7c3aed", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "y", "type": "quantitative"},
          {"field": "kodansha", "type": "quantitative"}
        ],
        "x": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行年", "format": "d"}
        },
        "y": {
          "field": "kodansha",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行点数（点）", "grid": true}
        },
        "color": {
          "datum": "講談社",
          "type": "nominal",
          "scale": {
            "domain": ["講談社", "小学館", "集英社", "KADOKAWA", "秋田書店"],
            "range": ["#7c3aed", "#3b82f6", "#22c55e", "#ef4444", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pub_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"y\"]) && isValid(datum[\"shogakukan\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#3b82f6", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "y", "type": "quantitative"},
          {"field": "shogakukan", "type": "quantitative"}
        ],
        "x": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行年", "format": "d"}
        },
        "y": {
          "field": "shogakukan",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行点数（点）", "grid": true}
        },
        "color": {
          "datum": "小学館",
          "type": "nominal",
          "scale": {
            "domain": ["講談社", "小学館", "集英社", "KADOKAWA", "秋田書店"],
            "range": ["#7c3aed", "#3b82f6", "#22c55e", "#ef4444", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pub_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"y\"]) && isValid(datum[\"shueisha\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#22c55e", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "y", "type": "quantitative"},
          {"field": "shueisha", "type": "quantitative"}
        ],
        "x": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行年", "format": "d"}
        },
        "y": {
          "field": "shueisha",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行点数（点）", "grid": true}
        },
        "color": {
          "datum": "集英社",
          "type": "nominal",
          "scale": {
            "domain": ["講談社", "小学館", "集英社", "KADOKAWA", "秋田書店"],
            "range": ["#7c3aed", "#3b82f6", "#22c55e", "#ef4444", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pub_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"y\"]) && isValid(datum[\"kadokawa\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#ef4444", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "y", "type": "quantitative"},
          {"field": "kadokawa", "type": "quantitative"}
        ],
        "x": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行年", "format": "d"}
        },
        "y": {
          "field": "kadokawa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行点数（点）", "grid": true}
        },
        "color": {
          "datum": "KADOKAWA",
          "type": "nominal",
          "scale": {
            "domain": ["講談社", "小学館", "集英社", "KADOKAWA", "秋田書店"],
            "range": ["#7c3aed", "#3b82f6", "#22c55e", "#ef4444", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pub_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"y\"]) && isValid(datum[\"akita\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#94a3b8", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "y", "type": "quantitative"},
          {"field": "akita", "type": "quantitative"}
        ],
        "x": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行年", "format": "d"}
        },
        "y": {
          "field": "akita",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "刊行点数（点）", "grid": true}
        },
        "color": {
          "datum": "秋田書店",
          "type": "nominal",
          "scale": {
            "domain": ["講談社", "小学館", "集英社", "KADOKAWA", "秋田書店"],
            "range": ["#7c3aed", "#3b82f6", "#22c55e", "#ef4444", "#94a3b8"]
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

講談社と小学館は長く1位と2位を争い、直近では年1,200〜1,700点台で推移しています。KADOKAWAは1990年（160点）の時点では上位社と大きな差がありましたが、2013年（603点）から2014年（1,163点）にかけて刊行点数がほぼ倍になり、その後は年1,300〜1,500点前後です。2013年に角川グループの出版事業がKADOKAWAへ統合された時期と重なり、統合されたレーベルの刊行が合算されたためと考えられます。

KADOKAWAは近年の刊行点数で集英社（年840〜900点前後）を上回り、講談社・小学館に次ぐ3位です。刊行点数で見ると、上位3社は講談社・小学館・KADOKAWAになっています。秋田書店は年450〜590点前後で安定しています。

## まとめ

- マンガ単行本の刊行点数は約50年で30倍に増え、2016〜2019年は年1万2千点台で頭打ちになり、2020・2021年はやや減った
- 2012〜2021年の刊行点数は上位3社で約36%、上位12社で65.3%を占め、残る約3分の1は12社以外の出版者から出ている
- KADOKAWAは2014年に刊行点数がほぼ倍になり、集英社を上回って3位になった

## データの出典

本記事は[メディア芸術データベース](https://mediaarts-db.artmuseums.go.jp/)（MADB）のマンガ単行本書誌 `mediaarts_db.main.manga_book` を、2026-07-11 時点で取得して集計しています。対象は刊行年が1970年から2021年までの310,871件で、出版社別の集計は2012年から2021年に絞っています。

Queriaは、メディア芸術データベースの列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[マンガ単行本書誌テーブル](/datasets/queria/mediaarts_db/main/manga_book)から、レーベル（`brand`）やシリーズごとに刊行点数を集計したり、特定の出版社の刊行の推移を確認したりできます。

```sql id=trend
SELECT published_year AS year, COUNT(*) AS n FROM mediaarts_db.main.manga_book WHERE published_year BETWEEN 1970 AND 2021 GROUP BY published_year ORDER BY published_year
```

```sql id=pub_top
WITH b AS (SELECT CASE WHEN split_part(publisher_name, ' | ', 1) IN ('KADOKAWA', '角川書店') THEN 'KADOKAWA' ELSE split_part(publisher_name, ' | ', 1) END AS pub, COUNT(*) AS n FROM mediaarts_db.main.manga_book WHERE published_year BETWEEN 2012 AND 2021 GROUP BY 1), r AS (SELECT pub, n, ROW_NUMBER() OVER (ORDER BY n DESC, pub) AS rn FROM b) SELECT pub, n FROM r WHERE rn <= 12 ORDER BY n ASC
```

```sql id=pub_trend
WITH s AS (SELECT published_year AS y, CASE WHEN split_part(publisher_name, ' | ', 1) IN ('KADOKAWA', '角川書店') THEN 'KADOKAWA' ELSE split_part(publisher_name, ' | ', 1) END AS pub FROM mediaarts_db.main.manga_book WHERE published_year BETWEEN 1990 AND 2021) SELECT y, SUM((pub = '講談社')::INT) AS kodansha, SUM((pub = '小学館')::INT) AS shogakukan, SUM((pub = '集英社')::INT) AS shueisha, SUM((pub = 'KADOKAWA')::INT) AS kadokawa, SUM((pub = '秋田書店')::INT) AS akita FROM s GROUP BY y ORDER BY y
```
