---
title: 交通事故が最も多い朝8時台より、深夜3時台の事故は約17倍の割合で死亡事故になる
description: 警察庁の交通事故オープンデータ2024年の約28万件を、事故類型・時間帯・都道府県で集計しました。事故の82.6%を占める車両相互の死亡率は0.39%で、車両単独は約16倍の6.16%です。死亡率は朝8時台が0.40%、深夜3時台が6.70%でした。
ogTitle: 交通事故が最も多い朝8時台より、深夜3時台の事故は約17倍の割合で死亡事故になる
ogDescription: 警察庁の交通事故オープンデータ2024年の約28万件を、事故類型・時間帯・都道府県で集計しました。件数が多い条件と死亡率が高い条件は一致しません。
publishedAt: 2026-07-22
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 交通事故
  - 警察庁
  - 死亡率
datasets:
  - queria/npa
sources:
  - title: 交通事故統計情報のオープンデータ
    url: https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html
    publisher: 警察庁
agentHint: 深夜の時間帯(occurred_hourが0〜4時)に絞って、事故類型(accident_pattern)別の死亡率(accident_typeが死亡の割合)を出して、夜間にどの類型が特に危険か比べて
socialAnnounce: |-
  警察庁の交通事故オープンデータ2024年・約28万件を数えました。

  事故件数の8割は車両相互ですが、死亡率は車両単独が約16倍。件数が最も多い朝8時台より、死亡率が高いのは深夜3時台で約17倍でした。
  Queriaは行政のオープンデータを整えて公開しています。
---

2024年に全国で記録された人身事故282,376件のうち、死亡事故は2,591件でした。事故の82.6%を占める車どうしの「車両相互」は、死亡事故の割合（死亡率）が0.39%で、車が電柱やガードレールなどにぶつかる「車両単独」は約16倍の6.16%です。時間帯では、事故が多い朝8時台の死亡率が0.40%で最も低く、事故が少ない深夜3時台は約17倍の6.70%でした。都道府県では、大都市圏の都府県で死亡率が低く、最も高い秋田県は最も低い東京都の約6倍です。

使ったのは、警察庁が公開している[交通事故統計情報のオープンデータ](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)の2024年（令和6年）の記録です。人身事故が1件ずつ記録されていて、各行に発生日時・場所・事故類型・死傷者数などが入っています。物損のみの事故は含まれません。この記事の「死亡率」は、人身事故の件数のうち死亡事故が占める割合です。死者数を分母や分子にした致死率とは別の値で、1件の事故で複数の人が亡くなった場合も1件として集計しています。

## 事故の82.6%は車両相互だが、死亡率は車両単独が約16倍高い

事故類型（`accident_pattern`）は、当事者の組み合わせで「車両相互」「人対車両」「車両単独」「列車」の4つに分かれます。類型ごとに、事故件数・全体に占める構成比・死亡事故の件数・死者数を集計しました。

```sql
SELECT accident_pattern AS '事故類型', COUNT(*) AS '事故件数', ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS '構成比(%)', SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) AS '死亡事故件数', SUM(fatalities) AS '死者数' FROM npa.main.traffic_accident GROUP BY accident_pattern ORDER BY COUNT(*) DESC
```

事故の82.6%は自動車どうしがぶつかる「車両相互」です。死亡率（死亡事故件数 ÷ 事故件数）は、車両相互が0.39%（909 ÷ 233,191）、歩行者が巻き込まれる「人対車両」が2.46%、「車両単独」が6.16%（727 ÷ 11,803）で、車両単独は車両相互の約16倍です。踏切事故などの「列車」は66.7%ですが、件数が54件しかないので、以下では他の3類型を中心に比較します。

件数の構成比と死亡事故の構成比を並べました。

```chart
{
  "height": 240,
  "layer": [
    {
      "data": {"name": "pattern_share"},
      "transform": [
        {"fold": ["acc_share", "fatal_share"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"acc_share\": \"事故件数の構成比\", \"fatal_share\": \"死亡事故件数の構成比\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"acc_share\",\"fatal_share\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "accident_pattern",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "事故類型"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "構成比（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["事故件数の構成比", "死亡事故件数の構成比"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["死亡事故件数の構成比", "事故件数の構成比"]},
        "tooltip": [
          {"field": "accident_pattern", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

青（件数）では車両相互が大部分を占めますが、赤（死亡事故）では3つの類型がほぼ同じくらいの割合です。車両単独は件数では4.2%ですが、死亡事故では28.1%を占めます。歩行者が巻き込まれる事故や単独事故は、件数は少ない一方で、起きると死亡事故になりやすくなっています。

## 事故が多い朝8時台の死亡率は0.40%、深夜3時台は6.70%

発生時刻（`occurred_hour`）ごとに、事故件数（左軸・棒）と死亡率（右軸・線）を重ねました。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "hourly"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "hour", "type": "quantitative"},
              {"field": "accidents", "type": "quantitative"}
            ],
            "x": {
              "field": "hour",
              "type": "ordinal",
              "axis": {"title": "発生時刻（時）", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "accidents",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "事故件数（件）", "grid": true}
            },
            "color": {
              "datum": "事故件数",
              "type": "nominal",
              "scale": {"domain": ["事故件数", "死亡率"], "range": ["#93c5fd", "#ef4444"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "hourly"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"hour\"]) && isValid(datum[\"fatal_rate\"]) ? 0 : 1",
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
              {"field": "hour", "type": "quantitative"},
              {"field": "fatal_rate", "type": "quantitative"}
            ],
            "x": {
              "field": "hour",
              "type": "ordinal",
              "axis": {"title": "発生時刻（時）", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "fatal_rate",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "死亡率（%）", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "死亡率",
              "type": "nominal",
              "scale": {"domain": ["事故件数", "死亡率"], "range": ["#93c5fd", "#ef4444"]},
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

事故件数は通勤・通学の時間帯に多く、朝8時台（24,484件）と夕方17時台（25,593件）がピークです。死亡率は、件数が最も多い朝8時台が0.40%で一日で最も低く、事故が少ない深夜から早朝にかけて高くなります。3時台は6.70%で、朝8時台の約17倍です。

日中の市街地は車も歩行者も多く、接触や出会い頭の軽い事故が多く起きると考えられます。深夜は交通量が少ないので事故の件数は減りますが、速度が出やすく周りが見えにくいので、死亡事故になる割合が高くなると考えられます。

## 死亡率は秋田県が3.13%で最も高く、東京都は0.50%で最も低い

都道府県ごとに死亡率（死亡事故件数 ÷ 事故件数）を求め、高い順に47都道府県を並べました。北海道は元データで5つの方面本部に分かれているので、合算しています。

```chart
{
  "height": 1030,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "fatal_rate", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "fatal_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡率（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10（死亡率が高い）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（死亡率が高い）", "中間", "下位10（死亡率が低い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "fatal_rate", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "fatal_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡率（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（死亡率が高い）", "中間", "下位10（死亡率が低い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "fatal_rate", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "fatal_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "死亡率（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10（死亡率が低い）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（死亡率が高い）", "中間", "下位10（死亡率が低い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

死亡率が最も高いのは秋田県の3.13%で、和歌山県2.78%、福井県・岐阜県2.52%と続きます。最も低いのは東京都の0.50%で、静岡県0.50%、群馬県0.51%、大阪府・福岡県0.52%、神奈川県0.53%、愛知県0.57%と、事故件数の多い大都市圏の都府県が低い側に並びます。秋田県の死亡率は東京都の約6倍です。

都市部は交通量が多いので軽い事故の件数が多くなり、地方では幹線道路の事故や夜間の単独事故など、死亡事故になりやすい事故の割合が高いと考えられます。

## まとめ

- 事故件数の82.6%を占める車両相互の死亡率は0.39%で、件数が4.2%の車両単独は6.16%と約16倍高い
- 事故の件数は朝夕の通勤時間帯に多く、死亡率は件数の少ない深夜から早朝に高い
- 東京都をはじめ大都市圏の都府県は死亡率が0.5%台で全国で最も低く、地方の県ほど死亡率が高い

事故の件数が多い条件と、死亡事故になりやすい条件は、事故類型・時間帯・都道府県のどれで見ても一致しません。件数だけを見ると死亡事故になりやすい条件を見落とし、死亡率だけを見ると事故の総数を見誤ります。

## データの出典

本記事は警察庁の[交通事故統計情報のオープンデータ](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)のうち、2024年（令和6年）の本票を2026年7月21日時点で取得して集計しています。

Queriaは、このオープンデータの事故ごとの記録のコード値を、事故類型・時刻・都道府県などの列に変換し、テーブルと列の説明を付けて公開しています。本記事で使った[交通事故テーブル](/datasets/queria/npa/main/traffic_accident)から、特定の時間帯や道路形状に絞って死亡率を求めたり、自分の住む地域の傾向を確認したりできます。

```sql id=pattern_share
SELECT accident_pattern, ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS acc_share, ROUND(100.0 * SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) / SUM(SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END)) OVER (), 1) AS fatal_share FROM npa.main.traffic_accident GROUP BY accident_pattern ORDER BY COUNT(*) DESC
```

```sql id=hourly
SELECT occurred_hour AS hour, COUNT(*) AS accidents, ROUND(100.0 * SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) / COUNT(*), 2) AS fatal_rate FROM npa.main.traffic_accident GROUP BY occurred_hour ORDER BY occurred_hour
```

```sql id=pref_top
WITH agg AS (SELECT CASE WHEN prefecture LIKE '北海道%' THEN '北海道' ELSE prefecture END AS pref, COUNT(*) AS accidents, SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) AS fatal_acc FROM npa.main.traffic_accident GROUP BY 1), ranked AS (SELECT pref, ROUND(100.0 * fatal_acc / accidents, 2) AS fatal_rate, ROW_NUMBER() OVER (ORDER BY 100.0 * fatal_acc / accidents DESC, pref) AS rn FROM agg) SELECT pref, fatal_rate FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH agg AS (SELECT CASE WHEN prefecture LIKE '北海道%' THEN '北海道' ELSE prefecture END AS pref, COUNT(*) AS accidents, SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) AS fatal_acc FROM npa.main.traffic_accident GROUP BY 1), ranked AS (SELECT pref, ROUND(100.0 * fatal_acc / accidents, 2) AS fatal_rate, ROW_NUMBER() OVER (ORDER BY 100.0 * fatal_acc / accidents DESC, pref) AS rn FROM agg) SELECT pref, fatal_rate FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH agg AS (SELECT CASE WHEN prefecture LIKE '北海道%' THEN '北海道' ELSE prefecture END AS pref, COUNT(*) AS accidents, SUM(CASE WHEN accident_type = '死亡' THEN 1 ELSE 0 END) AS fatal_acc FROM npa.main.traffic_accident GROUP BY 1), ranked AS (SELECT pref, ROUND(100.0 * fatal_acc / accidents, 2) AS fatal_rate, ROW_NUMBER() OVER (ORDER BY 100.0 * fatal_acc / accidents DESC, pref) AS rn FROM agg) SELECT pref, fatal_rate FROM ranked WHERE rn > 37 ORDER BY rn
```
