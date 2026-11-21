---
title: 上陸する台風の最大風速は北ほど3分の1下がるが、強い風が吹く範囲の広さはほとんど変わらない
description: 気象庁のベストトラックから、日本に上陸・通過した台風258地点の強さと大きさを分けて集計しました。強さの階級がつかない152地点のうち59地点は大型以上で、最大風速の中央値は北ほど下がる一方、強風域の半径の中央値は緯度帯によらず460〜490km台でした。
publishedAt: 2026-08-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 気象
  - 台風
  - 防災
datasets:
  - queria/jma
  - queria/nlftp
sources:
  - title: ベストトラックデータ（RSMC Tokyo - Typhoon Center）
    url: https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html
    publisher: 気象庁
  - title: 台風の大きさと強さ
    url: https://www.jma.go.jp/jma/kishou/know/typhoon/1-3.html
    publisher: 気象庁
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 1991年以降に上陸・通過した台風について、強風域の半径と暴風域の半径を地点ごとに出して。中心気圧の10hPaごとの帯でそれぞれの中央値も比べて
socialAnnounce: |-
  気象庁のベストトラックで、日本に上陸・通過した台風258地点を強さと大きさに分けて数えました。

  北へ行くほど最大風速は下がりますが、強風域の半径は狭くなりません。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

日本に上陸・通過した台風の258地点を集計すると、最大風速の中央値は北緯31度未満の38.6m/sから北緯37度以上の25.7m/sまで、およそ3分の1下がりました。強風域の半径の中央値は、南から491km、463km、491km、472kmで、緯度によってほとんど変わりません。最大風速が33m/s未満で強さの階級がつかない152地点のうち、59地点は強風域の半径が500km以上の大型または超大型でした。

複数の拠点を持つ企業では、台風が近づくと、拠点ごとに休業するかどうかや資材を前倒しで搬入するかを決めます。判断のときに最初に見られやすいのは、中心気圧の数値と「非常に強い台風」といった呼び方です。この2つはどちらも中心付近の激しさを表すもので、風が吹く範囲の広さは表していません。気象庁は台風の[大きさと強さ](https://www.jma.go.jp/jma/kishou/know/typhoon/1-3.html)を別々の基準で区分しています。強さは中心付近の最大風速で、大きさは強風域（風速15m/s以上の風が吹く範囲）の半径で決まります。強風域の半径が500km未満のときは大きさを表現しないので、「強い台風」という呼び方には大きさの情報が含まれません。この記事では[気象庁のベストトラック](https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html)を使い、日本の陸地に上陸または通過した台風の記録を、強さと大きさに分けて集計します。

## 集計するデータ

使うのは気象庁のベストトラック（`mart_jma_typhoon_tracks`）です。1951年以降の台風について、原則として6時間ごとの解析時刻ごとに1行があり、中心位置・中心気圧・最大風速・強風域と暴風域の半径が入っています。ここで使う列は次の5つです。

| 列                         | 内容                                                |
| -------------------------- | --------------------------------------------------- |
| `central_pressure_hpa`     | 中心気圧（hPa）                                     |
| `max_wind_speed_ms`        | 最大風速（m/s、10分間平均）                         |
| `wind30_longest_radius_nm` | 30ノット（約15m/s）以上の風域＝強風域の長径（海里） |
| `latitude`                 | 中心の緯度                                          |
| `is_landfall`              | 日本の陸地へ上陸または通過した解析時刻かどうか      |

`is_landfall` が付いているのは1991年以降の台風だけで、それより前は実際に上陸した台風でも `false` です。気象庁の報道発表の「上陸」は北海道・本州・四国・九州の海岸線に達した場合を指しますが、このフラグは離島の通過も含みます。強風域の半径は海里で記録されているので、1海里＝1.852kmで換算します。

対象は、`is_landfall` が付いていて強風域の半径が記録されている258地点です。1991年から2025年までの130個の台風が該当し、中心気圧は910〜1004hPa、強風域の半径は37〜1019kmです。同じ台風が上陸と再上陸を繰り返すと複数の地点になるので、地点数は台風の個数より多くなります。

## 中心気圧が同じ970hPaでも、強風域の半径は167kmから695kmまで分かれる

258地点を、中心気圧と強風域の半径で並べました。破線は、気象庁が大きさの階級を分ける500kmと800kmです。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "landfall_points"},
      "mark": {"type": "point", "color": "#3b82f6", "opacity": 0.6, "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "storm", "type": "nominal"},
          {"field": "p", "type": "quantitative"},
          {"field": "r30_km", "type": "quantitative"}
        ],
        "x": {
          "field": "p",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "上陸・通過時の中心気圧（hPa）", "grid": true}
        },
        "y": {
          "field": "r30_km",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "強風域の半径（km）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 500, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 800, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 1"}},
        "y": {"datum": 500, "type": "quantitative"},
        "text": {"value": "大型（500km）"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"value": {"expr": "width * 1"}},
        "y": {"datum": 800, "type": "quantitative"},
        "text": {"value": "超大型（800km）"}
      }
    }
  ]
}
```

中心気圧が低いほど強風域が広い傾向はありますが、点は縦に大きくばらついています。中心気圧が970hPaの20地点だけでも、強風域の半径は167kmから695kmまであります。半径が4倍になると風が吹く面積は16倍になるので、同じ970hPaでも備えるべき範囲は大きく違います。

## 強さの階級がつかない152地点のうち、59地点は大型以上

気象庁の階級は次のとおりです。強さは最大風速だけで、大きさは強風域の半径だけで決まります。

| 強さの階級     | 最大風速           |
| -------------- | ------------------ |
| （表現しない） | 33m/s未満          |
| 強い           | 33m/s以上44m/s未満 |
| 非常に強い     | 44m/s以上54m/s未満 |
| 猛烈な         | 54m/s以上          |

| 大きさの階級   | 強風域の半径       |
| -------------- | ------------------ |
| （表現しない） | 500km未満          |
| 大型           | 500km以上800km未満 |
| 超大型         | 800km以上          |

258地点をこの2つの階級で分類しました。強風域の半径は方向によって長さが違うので、長径（最も広い方向の半径）で判定しています。

```chart
{
  "height": 240,
  "layer": [
    {
      "data": {"name": "size_by_strength"},
      "transform": [
        {"fold": ["none_n", "large_n", "xlarge_n"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"none_n\": \"階級なし（500km未満）\", \"large_n\": \"大型（500〜800km）\", \"xlarge_n\": \"超大型（800km以上）\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"none_n\",\"large_n\",\"xlarge_n\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "strength",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "強さの階級"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "地点数", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["階級なし（500km未満）", "大型（500〜800km）", "超大型（800km以上）"],
            "range": ["#94a3b8", "#3b82f6", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "strength", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

最大風速が33m/s未満で強さの階級がつかない地点は152で、全体のおよそ6割です。そのうち57地点が大型、2地点が超大型で、59地点に大きさの階級がつきます。強さの階級がつかない地点の4割近くで、強風域の半径が500km以上でした。

最も上の「猛烈な」に該当する2地点は、どちらも強風域の半径が500km未満で、大きさの階級はつきません。中心付近の風は最も激しくても、風が吹く範囲は平均的な台風より狭い台風です。

## 北の地点ほど最大風速は下がるが、強風域の半径は南の地点の96%ある

台風は北上すると海水温の低い海域に入り、勢力が弱まります。上陸・通過地点の緯度を4つの帯に分け、最大風速と強風域の半径の中央値を並べました。

```chart
{
  "height": 300,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "lat_band"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"lat_band\"]) && isValid(datum[\"med_wind\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#ef4444",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 81}
          },
          "encoding": {
            "tooltip": [
              {"field": "lat_band", "type": "nominal"},
              {"field": "med_wind", "type": "quantitative"}
            ],
            "x": {
              "field": "lat_band",
              "type": "nominal",
              "axis": {"title": "上陸・通過地点の緯度帯", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "med_wind",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "最大風速の中央値（m/s）", "grid": true}
            },
            "color": {
              "datum": "最大風速の中央値（m/s）",
              "type": "nominal",
              "scale": {
                "domain": ["最大風速の中央値（m/s）", "強風域の半径の中央値（km）"],
                "range": ["#ef4444", "#3b82f6"]
              },
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "lat_band"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"lat_band\"]) && isValid(datum[\"med_r30\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#3b82f6",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 81}
          },
          "encoding": {
            "tooltip": [
              {"field": "lat_band", "type": "nominal"},
              {"field": "med_r30", "type": "quantitative"}
            ],
            "x": {
              "field": "lat_band",
              "type": "nominal",
              "axis": {"title": "上陸・通過地点の緯度帯", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "med_r30",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "強風域の半径の中央値（km）", "orient": "right"}
            },
            "color": {
              "datum": "強風域の半径の中央値（km）",
              "type": "nominal",
              "scale": {
                "domain": ["最大風速の中央値（m/s）", "強風域の半径の中央値（km）"],
                "range": ["#ef4444", "#3b82f6"]
              },
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

最大風速の中央値は、北緯31度未満の38.6m/sから北緯37度以上の25.7m/sまで、およそ3分の1下がります。中心気圧の中央値も955hPaから985hPaへ30hPa上がっていて、北の地点ほど勢力が弱まっています。

強風域の半径の中央値は、南から順に491km、463km、491km、472kmで、緯度による違いはほとんどありません。最も北の帯でも、最も南の帯の96%です。北上した台風は、中心付近の風は弱まっても、風が吹く範囲は狭くならないまま到達しています。中心気圧や強さの階級だけで判断すると、この点を見落とします。

## 北海道は「強い」以上が6%だが、「大型」以上は47%で沖縄県の50%とほぼ同じ

上陸・通過地点の座標に最も近い都道府県を割り当て、7地点以上ある16都道府県について、「強い」以上だった割合と「大型」以上だった割合を並べました。解析時刻の中心位置は上陸の直前で海上にあることが多いので、県境の内側にあるかどうかではなく、最も近い県で割り当てています。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "pref_share"},
      "transform": [
        {"fold": ["pct_strong", "pct_large"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"pct_strong\": \"「強い」以上だった割合\", \"pct_large\": \"「大型」以上だった割合\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"pct_strong\",\"pct_large\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["「強い」以上だった割合", "「大型」以上だった割合"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["「大型」以上だった割合", "「強い」以上だった割合"]},
        "tooltip": [
          {"field": "prefecture_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2本の棒の長さの差は、強さと大きさのどちらで評価するかで結果がどれだけ変わるかを表します。北海道は17地点のうち「強い」以上が6%（1地点）で、16都道府県の中で最も低い値です。「大型」以上は47%（8地点）で、沖縄県の50%とほとんど同じです。

本州の各県でも、大きさの割合のほうが高い県があります。兵庫県は13地点のうち「強い」以上が31%、「大型」以上が62%、和歌山県は15地点で33%と60%、愛知県は7地点で29%と57%です。逆に、熊本県は8地点で「強い」以上が88%、「大型」以上が50%、沖縄県は32地点で72%と50%で、大きさの割合のほうが低くなります。2つの割合が同じなのは、長崎県（16地点で31%と31%）、高知県（18地点で56%と56%）、神奈川県（7地点で57%と57%）の3県でした。地点数が10未満の県の割合は、数地点の違いで大きく変わるので、どちらの割合が高いかだけを参考にしてください。

「強い」以上の割合は県によって6%から88%まで分かれますが、「大型」以上の割合は20%から71%で、16都道府県のうち12県が40%台から60%台です。強さで評価すると地域の差が大きく、大きさで評価するとどの県も近い水準になります。大きさの割合のほうが高い差が最も大きいのは北海道の41ポイント、次が兵庫県の31ポイントです。強さの割合のほうが高い差が最も大きいのは熊本県の38ポイントでした。

## 業務での使い方

- 拠点ごとの警戒基準を、強さ（最大風速）と大きさ（強風域の半径）の2つで設定する。「非常に強い」以上で発動するといった1つの階級だけの基準では、強さの階級がつかない大型の台風を対象から外してしまいます
- 北日本や日本海側の拠点では、中心気圧の値で影響範囲を判断しない。上陸時の中心気圧が高くても、強風域の広さは南の拠点と変わらない前提で、営業再開までの時間を見積もります
- 自社の拠点の緯度経度から半径を指定して過去の上陸・通過地点を絞り込み、拠点ごとの頻度表を作る。上の集計は都道府県単位ですが、同じテーブルと同じ条件で、任意の座標を中心にした集計にできます
- 強風域に加えて暴風域（`wind50_longest_radius_nm`、25m/s以上の範囲）も同じ行に入っているので、休業の判断と屋外作業の中止の判断を別の閾値で設定できます

## データの出典

本記事は気象庁の[ベストトラックデータ](https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html)を2026年8月1日時点で集計しています。階級は気象庁の[台風の大きさと強さ](https://www.jma.go.jp/jma/kishou/know/typhoon/1-3.html)に従い、都道府県の割り当てには国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使いました。

Queria は、気象庁のベストトラックを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[台風経路テーブル](/datasets/queria/jma/main/mart_jma_typhoon_tracks)から、自社の拠点の近くを通った台風の記録を年ごとに確認したり、強風域と暴風域の半径を並べたりできます。

```sql id=landfall_points
SELECT CAST(central_pressure_hpa AS DOUBLE) AS p, ROUND(CAST(wind30_longest_radius_nm AS DOUBLE) * 1.852, 0) AS r30_km, ROUND(max_wind_speed_ms, 1) AS wind_ms, season || '年台風' || serial_number || '号' AS storm FROM jma.main.mart_jma_typhoon_tracks WHERE is_landfall AND wind30_longest_radius_nm IS NOT NULL ORDER BY central_pressure_hpa
```

```sql id=size_by_strength
WITH c AS (SELECT CASE WHEN max_wind_speed_ms >= 54 THEN '猛烈な' WHEN max_wind_speed_ms >= 44 THEN '非常に強い' WHEN max_wind_speed_ms >= 33 THEN '強い' ELSE '階級なし' END AS strength, CASE WHEN max_wind_speed_ms >= 54 THEN 3 WHEN max_wind_speed_ms >= 44 THEN 2 WHEN max_wind_speed_ms >= 33 THEN 1 ELSE 0 END AS ord, CAST(wind30_longest_radius_nm AS DOUBLE) * 1.852 AS r30_km FROM jma.main.mart_jma_typhoon_tracks WHERE is_landfall AND wind30_longest_radius_nm IS NOT NULL AND max_wind_speed_ms IS NOT NULL) SELECT strength, CAST(SUM(CASE WHEN r30_km < 500 THEN 1 ELSE 0 END) AS INTEGER) AS none_n, CAST(SUM(CASE WHEN r30_km >= 500 AND r30_km < 800 THEN 1 ELSE 0 END) AS INTEGER) AS large_n, CAST(SUM(CASE WHEN r30_km >= 800 THEN 1 ELSE 0 END) AS INTEGER) AS xlarge_n FROM c GROUP BY strength, ord ORDER BY ord
```

```sql id=lat_band
WITH b AS (SELECT CASE WHEN latitude < 31 THEN 0 WHEN latitude < 34 THEN 1 WHEN latitude < 37 THEN 2 ELSE 3 END AS ord, central_pressure_hpa, max_wind_speed_ms, CAST(wind30_longest_radius_nm AS DOUBLE) * 1.852 AS r30_km FROM jma.main.mart_jma_typhoon_tracks WHERE is_landfall AND wind30_longest_radius_nm IS NOT NULL) SELECT CASE ord WHEN 0 THEN '北緯31度未満' WHEN 1 THEN '北緯31〜34度' WHEN 2 THEN '北緯34〜37度' ELSE '北緯37度以上' END AS lat_band, CAST(COUNT(*) AS INTEGER) AS n, ROUND(MEDIAN(central_pressure_hpa), 0) AS med_p, ROUND(MEDIAN(max_wind_speed_ms), 1) AS med_wind, ROUND(MEDIAN(r30_km), 0) AS med_r30 FROM b GROUP BY ord ORDER BY ord
```

```sql id=pref_share
WITH lf AS (SELECT international_id, analysis_time, longitude, latitude, max_wind_speed_ms, CAST(wind30_longest_radius_nm AS DOUBLE) * 1.852 AS r30_km FROM jma.main.mart_jma_typhoon_tracks WHERE is_landfall AND wind30_longest_radius_nm IS NOT NULL), j AS (SELECT lf.*, p.prefecture_name, ROW_NUMBER() OVER (PARTITION BY lf.international_id, lf.analysis_time ORDER BY ST_Distance(p.geometry, ST_Point(lf.longitude, lf.latitude)), p.prefecture_name) AS rn FROM lf CROSS JOIN nlftp.boundary.prefecture p) SELECT prefecture_name, CAST(COUNT(*) AS INTEGER) AS n, ROUND(100.0 * SUM(CASE WHEN max_wind_speed_ms >= 33 THEN 1 ELSE 0 END) / COUNT(*), 0) AS pct_strong, ROUND(100.0 * SUM(CASE WHEN r30_km >= 500 THEN 1 ELSE 0 END) / COUNT(*), 0) AS pct_large FROM j WHERE rn = 1 GROUP BY prefecture_name HAVING COUNT(*) >= 7 ORDER BY pct_strong, prefecture_name
```
