---
title: 盗まれた自転車の64.5%、車上ねらいに遭った車の69.1%は鍵がかかっていなかった
description: 12府県の警察が公開する2024年の街頭犯罪のオープンデータ98,794件を、手口・時間帯・施錠状況で集計しました。自転車盗が72.8%を占め、施錠状況が分かる被害のうち無施錠の割合は自転車盗で64.5%、車上ねらいで69.1%です。
ogDescription: 12府県の警察が公開する2024年の街頭犯罪のオープンデータ98,794件を、手口・時間帯・施錠状況で集計しました。
publishedAt: 2026-07-22
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 街頭犯罪
  - 警察庁
  - 自転車盗
datasets:
  - queria/npa
sources:
  - title: 犯罪オープンデータのリンク集
    url: https://www.npa.go.jp/toukei/seianki/hanzaiopendatalink.html
    publisher: 警察庁
agentHint: 盗まれた自転車の無施錠率(lock_status)を府県(source_prefecture)別に出して、施錠対策が進んでいる府県とそうでない府県を比べて
socialAnnounce: |-
  都道府県警察が公開する街頭犯罪のオープンデータ2024年・約10万件を集計しました。

  手口の7割超は自転車盗で、盗まれた自転車の6割超は無施錠でした。キーを付けたまま盗まれたのは、オートバイ盗で3割、自動車盗で2割です。
  Queriaは行政のオープンデータを整えて公開しています。
---

2024年に12府県で記録された街頭犯罪98,794件のうち、72.8%（71,934件）は自転車盗でした。施錠状況が記録された被害のうち、自転車盗の64.5%、車上ねらいの69.1%は無施錠でした。自転車盗は朝7時台と夕方18時台に多く、ひったくりは夕方から夜間に多く起きていました。

ひったくりや車上ねらいなどの「街頭犯罪」について、一部の都道府県警察は被害を1件ごとに記録したオープンデータを公開しています。発生した日時と場所、手口、被害に遭った自転車や車が施錠されていたかが記録されています。この記事では、[警察庁がまとめる犯罪オープンデータのリンク集](https://www.npa.go.jp/toukei/seianki/hanzaiopendatalink.html)から各府県警察が公開している街頭犯罪データを使い、2024年（令和6年）に認知された窃盗の街頭犯罪を、手口・発生時刻・施錠状況の3つで集計します。

## 街頭犯罪の72.8%は自転車盗

このデータは、街頭犯罪にあたる窃盗を、1認知件1レコード、町丁目単位で記録したものです。各行に、発生日時・発生場所・手口・被害車両の施錠状況などが入っています。手口（`modus`）は、警察庁の様式に従って「ひったくり」「車上ねらい」「部品ねらい」「自動販売機ねらい」「自動車盗」「オートバイ盗」「自転車盗」の7種類に分かれます。手口ごとの件数です。

```sql
SELECT modus AS '手口', COUNT(*) AS '件数', ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS '構成比(%)' FROM npa.crime.theft GROUP BY modus ORDER BY COUNT(*) DESC
```

2024年に12府県（青森・福島・栃木・埼玉・千葉・神奈川・京都・大阪・徳島・佐賀・宮崎・鹿児島）で記録された街頭犯罪は98,794件でした。対象は、この形式でデータを公開している12府県だけです。最も多いのは自転車盗の71,934件で、全体の72.8%です。車上ねらい（9,184件・9.3%）、部品ねらい（7,061件・7.1%）、オートバイ盗（5,984件・6.1%）が続き、自動車盗は3,004件（3.0%）、ひったくりは295件（0.3%）でした。街頭犯罪のおよそ4件に3件が自転車盗です。

```chart
{
  "height": 240,
  "layer": [
    {
      "data": {"name": "modus_count"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "n", "type": "quantitative"}, {"field": "modus", "type": "nominal"}],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "件数（件）", "grid": true}
        },
        "y": {
          "field": "modus",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "手口"},
          "sort": null
        }
      }
    }
  ]
}
```

件数が最も多いのは大阪府の34,031件で、埼玉県19,604件、神奈川県16,679件、千葉県13,655件と、大都市のある府県が続きます。件数は人口あたりの値ではないので、府県の件数の差は治安の良し悪しを表しません。

```sql
SELECT source_prefecture AS '府県', COUNT(*) AS '件数' FROM npa.crime.theft GROUP BY source_prefecture ORDER BY COUNT(*) DESC
```

## 自転車盗は朝7時台と夕方18時台、ひったくりは夕方から夜間に多い

手口ごとに発生を時刻別に集計し、その手口の総件数に占める割合で並べました。割合にすると、件数の規模が違う手口どうしでも、多く起きる時間帯を比較できます。ここでは自転車盗・車上ねらい・ひったくりの3つを重ねています。発生時刻（`occurred_hour`）が記録されていない行は除いています。未記録の行を0時として扱うと、深夜の割合が実際より大きくなるためです。

```chart
{
  "layer": [
    {
      "data": {"name": "hourly_share"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"hour\"]) && isValid(datum[\"bike_pct\"]) ? 0 : 1",
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
          {"field": "hour", "type": "quantitative"},
          {"field": "bike_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "hour",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "発生時刻（時）", "tickMinStep": 2}
        },
        "y": {
          "field": "bike_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "手口内の時刻別シェア（%）", "grid": true}
        },
        "color": {
          "datum": "自転車盗",
          "type": "nominal",
          "scale": {
            "domain": ["自転車盗", "車上ねらい", "ひったくり"],
            "range": ["#3b82f6", "#22c55e", "#ef4444"]
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
          "calculate": "isValid(datum[\"hour\"]) && isValid(datum[\"carbreak_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "hour", "type": "quantitative"},
          {"field": "carbreak_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "hour",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "発生時刻（時）", "tickMinStep": 2}
        },
        "y": {
          "field": "carbreak_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "手口内の時刻別シェア（%）", "grid": true}
        },
        "color": {
          "datum": "車上ねらい",
          "type": "nominal",
          "scale": {
            "domain": ["自転車盗", "車上ねらい", "ひったくり"],
            "range": ["#3b82f6", "#22c55e", "#ef4444"]
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
          "calculate": "isValid(datum[\"hour\"]) && isValid(datum[\"snatch_pct\"]) ? 0 : 1",
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
          {"field": "hour", "type": "quantitative"},
          {"field": "snatch_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "hour",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "発生時刻（時）", "tickMinStep": 2}
        },
        "y": {
          "field": "snatch_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "手口内の時刻別シェア（%）", "grid": true}
        },
        "color": {
          "datum": "ひったくり",
          "type": "nominal",
          "scale": {
            "domain": ["自転車盗", "車上ねらい", "ひったくり"],
            "range": ["#3b82f6", "#22c55e", "#ef4444"]
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

自転車盗（青）は朝7時台（6.45%）に急に増え、夕方18時台（9.25%）にもう一度多くなります。通勤・通学で自転車が置かれる時間帯と重なっています。車上ねらい（緑）は朝には多くなく、日中から夕方（18時台9.67%）にかけて少しずつ増えます。ひったくり（赤）は朝にはほとんどなく、夕方から夜間（19時台10.17%、23時台7.80%）に多く起きています。

## 車上ねらいの69.1%、自転車盗の64.5%は施錠されていなかった

このデータには、被害に遭った自転車や車が施錠されていたか（`lock_status`）も記録されています。自転車盗と車上ねらいでは「施錠した／施錠せず」、オートバイ盗と自動車盗では「キーあり（付けたまま）／キーなし」です。手口ごとに、施錠状況が記録された被害のうち、無施錠だった（またはキーを付けたままだった）割合を計算しました。記録のない行と、施錠があてはまらない手口（部品ねらい・自動販売機ねらい・ひったくり）は除いています。

```chart
{
  "height": 200,
  "layer": [
    {
      "data": {"name": "unlocked"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "unlocked_pct", "type": "quantitative"},
          {"field": "modus", "type": "nominal"}
        ],
        "x": {
          "field": "unlocked_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "無施錠・キー放置の割合（%）", "grid": true}
        },
        "y": {
          "field": "modus",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "手口"},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "unlocked"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "unlocked_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "無施錠・キー放置の割合（%）", "grid": true}
        },
        "y": {
          "field": "modus",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "手口"},
          "sort": null
        },
        "text": {"field": "unlocked_pct"}
      }
    }
  ]
}
```

施錠状況が記録された被害のうち、車上ねらいの69.1%、自転車盗の64.5%は無施錠でした。件数が最も多い自転車盗では、盗まれた自転車のおよそ3台に2台は鍵がかかっていませんでした。施錠していれば防げた可能性のある被害が、多く含まれていると考えられます。オートバイ盗では32.3%、自動車盗では20.3%がキーを付けたまま盗まれていました。`lock_status` の意味は手口によって異なり、自転車と車上ねらいでは施錠の有無、オートバイと自動車ではキーを付けたままだったかを表すので、手口の間の比較は目安です。

## まとめ

- 12府県で記録された街頭犯罪98,794件のうち、72.8%が自転車盗
- 自転車盗は朝7時台と夕方18時台に多く、ひったくりは夕方から夜間に多い
- 施錠状況が記録された被害のうち、無施錠の割合は、車上ねらいで69.1%、自転車盗で64.5%。キーを付けたまま盗まれた割合は、オートバイ盗で32.3%、自動車盗で20.3%

## データの出典

本記事は、[警察庁の犯罪オープンデータのリンク集](https://www.npa.go.jp/toukei/seianki/hanzaiopendatalink.html)から取得できる各府県警察の街頭犯罪データを、2026年11月21日時点で集計しています。対象は2024年（令和6年）に認知された窃盗の街頭犯罪で、青森・福島・栃木・埼玉・千葉・神奈川・京都・大阪・徳島・佐賀・宮崎・鹿児島の12府県です。

Queria は、府県ごとに様式の異なる犯罪記録の手口・時刻・施錠状況を共通の列にし、各列の意味の説明を付けて公開しています。本記事で使った[街頭犯罪テーブル](/datasets/queria/npa/crime/theft)から、府県や手口を絞って同じ集計をしたり、発生場所ごとの件数を確認したりできます。

```sql id=modus_count
SELECT modus, COUNT(*) AS n FROM npa.crime.theft GROUP BY modus ORDER BY COUNT(*) DESC
```

```sql id=hourly_share
SELECT occurred_hour AS hour, ROUND(100.0 * SUM(CASE WHEN modus = '自転車盗' THEN 1 ELSE 0 END) / SUM(SUM(CASE WHEN modus = '自転車盗' THEN 1 ELSE 0 END)) OVER (), 2) AS bike_pct, ROUND(100.0 * SUM(CASE WHEN modus = '車上ねらい' THEN 1 ELSE 0 END) / SUM(SUM(CASE WHEN modus = '車上ねらい' THEN 1 ELSE 0 END)) OVER (), 2) AS carbreak_pct, ROUND(100.0 * SUM(CASE WHEN modus = 'ひったくり' THEN 1 ELSE 0 END) / SUM(SUM(CASE WHEN modus = 'ひったくり' THEN 1 ELSE 0 END)) OVER (), 2) AS snatch_pct FROM npa.crime.theft WHERE occurred_hour IS NOT NULL GROUP BY occurred_hour ORDER BY occurred_hour
```

```sql id=unlocked
SELECT modus, ROUND(100.0 * SUM(CASE WHEN lock_status IN ('施錠せず', 'キーあり') THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN lock_status IN ('施錠せず', 'キーなし', '施錠した', 'キーあり') THEN 1 ELSE 0 END), 0), 1) AS unlocked_pct FROM npa.crime.theft WHERE modus IN ('自転車盗', '車上ねらい', 'オートバイ盗', '自動車盗') GROUP BY modus ORDER BY unlocked_pct DESC
```
