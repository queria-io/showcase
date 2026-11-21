---
title: 桜は早く咲くようになったが、暖かい地方ほど咲いてから満開までが長くなった
description: そめいよしのの開花は43地点すべてで早まりました。一方で開花から満開までの日数は33地点で延び、鹿児島では1961〜1990年の平均7.1日が1996〜2025年に10.7日になりました。
publishedAt: 2026-10-19
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 気象
  - 観光
  - 気候変動
datasets:
  - queria/jma
  - queria/e_stat
sources:
  - title: 生物季節観測の情報
    url: https://www.data.jma.go.jp/sakura/data/index.html
    publisher: 気象庁
  - title: さくらの開花日と満開日の観測方法と等期日線図（平年）
    url: https://www.data.jma.go.jp/sakura/data/sakura2020.pdf
    publisher: 気象庁
  - title: 生物季節観測累年表（さくら満開）
    url: https://www.data.jma.go.jp/sakura/data/pdf/005.pdf
    publisher: 気象庁
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（B 自然環境）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/B
    publisher: 総務省統計局
agentHint: 43地点それぞれについて、2006〜2025年の開花から満開までの日数の最短・中央値・最長を出して、九州と北海道・東北で並べて
socialAnnounce: |-
  桜の開花は全国43地点すべてで早まりました。
  一方、咲いてから満開までは33地点で延び、鹿児島は18年続けて10日以上です。
  桜まつりの会期づくりや観光の告知に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

そめいよしのの開花日は、1961〜1990年と1996〜2025年の平均を比較すると、43地点すべてで早まりました。開花から満開までの日数は33地点で長くなり、鹿児島では7.1日から10.7日になっています。冬の最低気温が高い地点ほど開花から満開までが長く、43地点の相関係数は0.73です。

桜まつりのライトアップや出店、交通規制の期間は、開花予想や開花の知らせをもとに、咲き始めてから満開までに何日あるかを見込んで決めます。この記事では、気象庁が70年以上続けている観測記録を地点ごとに並べ、自治体や観光協会で桜まつりの会期を決める担当者が使えるように、開花から満開までの日数の変化を地点別に示します。

## 九州では、満開まで平均2日長くかかるようになった

使うのは、気象庁が全国の気象台で観測している[生物季節観測](https://www.data.jma.go.jp/sakura/data/index.html)のさくらの記録です。Queria では `jma.main.mart_jma_sakura_phenology` に、地点・年ごとの開花日と満開日が入っています。

| 列            | 内容                                                                                                       |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| `phenomenon`  | `開花`（標本木で5〜6輪以上の花が開いた最初の日）または `満開`（標本木で約80%以上のつぼみが開いた最初の日） |
| `species`     | 標本木の種類。多くの地点は `そめいよしの`、北海道の一部と奄美・沖縄は別の種類                              |
| `day_of_year` | 観測年の1月1日を1とした通日                                                                                |

定義は気象庁の[さくらの開花日と満開日の観測方法](https://www.data.jma.go.jp/sakura/data/sakura2020.pdf)によります。対象は、そめいよしのを観測している気象台のうち、後半で使う都道府県の気温データと同じ観測点で、1961〜1990年と1996〜2025年の両方に25年以上の記録がある43地点です。「開花から満開までの日数」は、同じ年の満開日から開花日を引いた値です。地域ごとに10年単位で平均したのが次の図です。2020年代は2020〜2025年の6年分です。

```chart
{
  "layer": [
    {
      "data": {"name": "region_kyushu"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"decade\"]) && isValid(datum[\"gap\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "decade", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "decade",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年代", "values": [1960, 1970, 1980, 1990, 2000, 2010, 2020]}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（平均）", "grid": true}
        },
        "color": {
          "datum": "九州",
          "type": "nominal",
          "scale": {
            "domain": ["九州", "東海・近畿・中国・四国", "関東・甲信・北陸", "北海道・東北"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_west"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"decade\"]) && isValid(datum[\"gap\"]) ? 0 : 1",
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
          {"field": "decade", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "decade",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年代", "values": [1960, 1970, 1980, 1990, 2000, 2010, 2020]}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（平均）", "grid": true}
        },
        "color": {
          "datum": "東海・近畿・中国・四国",
          "type": "nominal",
          "scale": {
            "domain": ["九州", "東海・近畿・中国・四国", "関東・甲信・北陸", "北海道・東北"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_east"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"decade\"]) && isValid(datum[\"gap\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "decade", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "decade",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年代", "values": [1960, 1970, 1980, 1990, 2000, 2010, 2020]}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（平均）", "grid": true}
        },
        "color": {
          "datum": "関東・甲信・北陸",
          "type": "nominal",
          "scale": {
            "domain": ["九州", "東海・近畿・中国・四国", "関東・甲信・北陸", "北海道・東北"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_north"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"decade\"]) && isValid(datum[\"gap\"]) ? 0 : 1",
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
          {"field": "decade", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "decade",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年代", "values": [1960, 1970, 1980, 1990, 2000, 2010, 2020]}
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（平均）", "grid": true}
        },
        "color": {
          "datum": "北海道・東北",
          "type": "nominal",
          "scale": {
            "domain": ["九州", "東海・近畿・中国・四国", "関東・甲信・北陸", "北海道・東北"],
            "range": ["#ef4444", "#f97316", "#22c55e", "#3b82f6"]
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

九州の6地点（福岡・佐賀・長崎・熊本・大分・鹿児島）は、1960年代に平均7.1日だった開花から満開までが、1990年代に10.3日へ延び、2020年代も9.3日と長いままです。北海道・東北の7地点は同じ期間に5.0日から4.1日へわずかに短くなりました。開花日と満開日がどの地域でも同じだけ早まったのなら、この線は横ばいになります。

## 開花は全地点で早まり、満開は鹿児島だけが遅くなった

30年ずつの平均で、1961〜1990年と1996〜2025年を比較します。開花日は43地点すべてで早まっていて、早まり方は鹿児島の1.5日から松江の8.1日までの幅があります。満開日も42地点で早まっていますが、鹿児島だけは2.1日遅くなりました。開花が早まった分より満開が早まった分が小さい地点では、そのぶん開花から満開までが延びています。地点ごとの延び縮みを並べたのが次の図です。

```chart
{
  "height": 880,
  "layer": [
    {
      "data": {"name": "shift_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "gap_change", "type": "quantitative"},
          {"field": "station_name", "type": "nominal"}
        ],
        "x": {
          "field": "gap_change",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数の変化（日、1961〜1990年平均 → 1996〜2025年平均）", "grid": true}
        },
        "y": {
          "field": "station_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "変わらないか短くなった",
          "type": "nominal",
          "scale": {"domain": ["変わらないか短くなった", "長くなった"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "shift_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "gap_change", "type": "quantitative"},
          {"field": "station_name", "type": "nominal"}
        ],
        "x": {
          "field": "gap_change",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数の変化（日、1961〜1990年平均 → 1996〜2025年平均）", "grid": true}
        },
        "y": {
          "field": "station_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "長くなった",
          "type": "nominal",
          "scale": {"domain": ["変わらないか短くなった", "長くなった"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

43地点のうち33地点で開花から満開までが長くなりました。最も延びたのは鹿児島で、7.1日から10.7日になっています。続く甲府・大分・福岡も2.5日以上延び、九州の6地点では平均2.1日長くなりました。反対に、青森（5.5日→3.9日）、山形、秋田、仙台、福島と、東北の多くの地点は短くなっています。

## 鹿児島では、18年続けて満開まで10日以上

最も延びた鹿児島を、年ごとに並べます。

```chart
{
  "layer": [
    {
      "data": {"name": "kagoshima"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（鹿児島）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1952.5, "type": "ordinal"},
        "x2": {"datum": 2025.5, "type": "ordinal"},
        "y": {"datum": 10, "type": "quantitative"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "left",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 1953, "type": "ordinal"},
        "y": {"datum": 10, "type": "quantitative"},
        "text": {"value": "10日"}
      }
    }
  ]
}
```

1953〜2007年の55年間で、満開まで10日以上かかった年は11年で、最も長くても12日でした。2008年以降は2025年まで18年続けてすべての年が10日以上で、平均は12.6日、2020年には18日かかっています。日数は少しずつ延びたのではなく、2008年から急に長くなっています。[満開日の累年表](https://www.data.jma.go.jp/sakura/data/pdf/005.pdf)では、2008年の前後とも気象台構内のそめいよしので観測しています。構内での標本木の植え替えはこの記録には書かれないので、この段差の一部が標本木の変更などの観測側の理由による可能性もあります。鹿児島では、この18年の記録から、開花の知らせから満開まで12日前後を見込むのが実際に近いと考えられます。

## 冬に冷え込まない地点ほど、満開まで長くかかる

延びた地点と縮んだ地点の違いを、冬の冷え込みで比較します。気温は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データ（`e_stat.ssds.b_pref_land`）の最低気温（`B4103`）を使います。日最低気温を月ごとに平均し、その年で最も低い月の値を取ったものです。都道府県の値は県庁所在地の気象台1地点の観測値（埼玉県は熊谷、滋賀県は彦根）で、さくらを観測している気象台と同じ気象台の値です。次の図は、横軸がその1996〜2014年の平均、縦軸が1996〜2025年の開花から満開までの日数です。東京の気温は[2014年12月の観測点の移転](https://www.jma.go.jp/jma/press/1410/03b/20141003_tokyo_rojo.html)で前後が続かないので、気温はどの地点も1996〜2014年の平均です。

```chart
{
  "layer": [
    {
      "data": {"name": "winter_other"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "station_name", "type": "nominal"},
          {"field": "winter_low", "type": "quantitative"},
          {"field": "gap_after", "type": "quantitative"}
        ],
        "x": {
          "field": "winter_low",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "最も寒い月の日最低気温の平均（℃、1996〜2014年平均）", "grid": true}
        },
        "y": {
          "field": "gap_after",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "開花から満開までの日数（1996〜2025年平均）", "grid": true}
        },
        "color": {
          "datum": "九州以外",
          "type": "nominal",
          "scale": {"domain": ["九州以外", "九州"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "winter_kyushu"},
      "mark": {"type": "point", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "station_name", "type": "nominal"},
          {"field": "winter_low", "type": "quantitative"},
          {"field": "gap_after", "type": "quantitative"}
        ],
        "x": {
          "field": "winter_low",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "最も寒い月の日最低気温の平均（℃、1996〜2014年平均）", "grid": true}
        },
        "y": {
          "field": "gap_after",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "開花から満開までの日数（1996〜2025年平均）", "grid": true}
        },
        "color": {
          "datum": "九州",
          "type": "nominal",
          "scale": {"domain": ["九州以外", "九州"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "winter_kyushu"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "winter_low",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "最も寒い月の日最低気温の平均（℃、1996〜2014年平均）", "grid": true}
        },
        "y": {
          "field": "gap_after",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "開花から満開までの日数（1996〜2025年平均）", "grid": true}
        },
        "text": {"field": "station_name"}
      }
    }
  ]
}
```

冬の最低気温が高い地点ほど、開花から満開までが長くなっています。43地点の相関係数は0.73です。最も冷え込まない鹿児島が10.7日で最も長く、最も冷え込む札幌は4.2日でした。延びた日数（前の図の値）と冬の最低気温の相関係数も0.41あり、暖かい地点ほど延び方も大きい傾向があります。例外も多く、冬が比較的暖かい東京は0.7日短くなり、冷え込む甲府は2.7日延びています。

同じ地点の中でも、冬の冷え込みが弱かった年ほど満開まで長くかかっています。1975〜2014年の40年を地点ごとに冷え込みの強い年・中くらいの年・弱い年に3等分して平均すると、次のようになります。

```chart
{
  "layer": [
    {
      "data": {"name": "winter_years_kyushu"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "その地点の40年の中での冬の冷え込み", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（平均）", "grid": true}
        },
        "xOffset": {"datum": "九州", "scale": {"domain": ["九州", "九州以外"]}},
        "color": {
          "datum": "九州",
          "type": "nominal",
          "scale": {"domain": ["九州", "九州以外"], "range": ["#ef4444", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "winter_years_other"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "gap", "type": "quantitative"}
        ],
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "その地点の40年の中での冬の冷え込み", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "開花から満開までの日数（平均）", "grid": true}
        },
        "xOffset": {"datum": "九州以外", "scale": {"domain": ["九州", "九州以外"]}},
        "color": {
          "datum": "九州以外",
          "type": "nominal",
          "scale": {"domain": ["九州", "九州以外"], "range": ["#ef4444", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

九州では冷え込みが強い年の8.5日に対して弱い年は10.2日、九州以外でも6.0日に対して7.4日です。さくらの花芽は冬に一定の低温にさらされて休眠から覚めるとされていて、暖かい冬には休眠から覚める時期が木ごと、枝ごとにばらつくと考えられます。そうであれば、最初の数輪は早く開いても8割が開くまでに時間がかかることになり、このデータの傾向と矛盾しません。この表は気温と日数の関係を示すもので、その仕組みを確認したものではありません。

## 桜まつりの会期を決めるときの使い方

- 会期の長さを、自分の地点の最近の実績から決める。鹿児島のように開花から満開まで10日以上かかる年が続く地点では、開花の知らせから満開まで告知に使える日数が長く、会期の後半を長くとれます。東北の地点では満開まで4日から5日ほどしかないので、開花予想の段階で準備を終えておく必要があります
- 暖冬の年は、満開までの日数をふだんより長めに見込む。同じ地点でも冷え込みの弱い年は満開まで1〜2日長くかかっていて、会期の後半に余裕を持たせる判断材料になります
- 「満開の週末」を宣伝する観光プロモーションでは、開花日ではなく満開日の推移を使う。開花が早まった日数と同じだけ満開の時期を前にずらすと、九州では早すぎる設定になります

## データの出典

本記事は気象庁[生物季節観測](https://www.data.jma.go.jp/sakura/data/index.html)のさくらの開花日・満開日（1953〜2025年）と、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別の最低気温（1975〜2014年）を、2026年10月19日時点で集計しています。最低気温の定義と観測地点は[項目定義 B 自然環境](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)によります。

Queriaは、気象庁や総務省のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[さくらの開花・満開のテーブル](/datasets/queria/jma/main/mart_jma_sakura_phenology)と[都道府県別の自然環境データのテーブル](/datasets/queria/e_stat/ssds/b_pref_land)から、自分の地域の気象台の開花日と満開日を1953年から並べ、開花から満開までの日数を計算できます。

```sql id=stations
-- さくらを観測している気象台のうち、社会・人口統計体系の気温（B4103）と同じ観測点で、1961年から観測が続いているもの（43地点）と地域区分。宮崎は1971年からなので含めない。プロットはしない
SELECT * FROM (VALUES ('札幌','北海道','北海道・東北'),('青森','青森県','北海道・東北'),('盛岡','岩手県','北海道・東北'),('仙台','宮城県','北海道・東北'),('秋田','秋田県','北海道・東北'),('山形','山形県','北海道・東北'),('福島','福島県','北海道・東北'),('水戸','茨城県','関東・甲信・北陸'),('宇都宮','栃木県','関東・甲信・北陸'),('前橋','群馬県','関東・甲信・北陸'),('熊谷','埼玉県','関東・甲信・北陸'),('東京','東京都','関東・甲信・北陸'),('横浜','神奈川県','関東・甲信・北陸'),('新潟','新潟県','関東・甲信・北陸'),('富山','富山県','関東・甲信・北陸'),('金沢','石川県','関東・甲信・北陸'),('福井','福井県','関東・甲信・北陸'),('甲府','山梨県','関東・甲信・北陸'),('長野','長野県','関東・甲信・北陸'),('岐阜','岐阜県','東海・近畿・中国・四国'),('静岡','静岡県','東海・近畿・中国・四国'),('名古屋','愛知県','東海・近畿・中国・四国'),('津','三重県','東海・近畿・中国・四国'),('彦根','滋賀県','東海・近畿・中国・四国'),('京都','京都府','東海・近畿・中国・四国'),('大阪','大阪府','東海・近畿・中国・四国'),('神戸','兵庫県','東海・近畿・中国・四国'),('奈良','奈良県','東海・近畿・中国・四国'),('和歌山','和歌山県','東海・近畿・中国・四国'),('鳥取','鳥取県','東海・近畿・中国・四国'),('松江','島根県','東海・近畿・中国・四国'),('岡山','岡山県','東海・近畿・中国・四国'),('広島','広島県','東海・近畿・中国・四国'),('徳島','徳島県','東海・近畿・中国・四国'),('高松','香川県','東海・近畿・中国・四国'),('松山','愛媛県','東海・近畿・中国・四国'),('高知','高知県','東海・近畿・中国・四国'),('福岡','福岡県','九州'),('佐賀','佐賀県','九州'),('長崎','長崎県','九州'),('熊本','熊本県','九州'),('大分','大分県','九州'),('鹿児島','鹿児島県','九州')) AS t(station_name, area_name, region)
```

```sql id=bloom
-- 地点・年ごとのそめいよしのの開花日と満開日（1月1日を1とした通日）
SELECT s.station_name, s.area_name, s.region, k.year, k.day_of_year AS kaika, m.day_of_year AS mankai, m.day_of_year - k.day_of_year AS gap
FROM jma.main.mart_jma_sakura_phenology k
JOIN jma.main.mart_jma_sakura_phenology m ON m.station_name = k.station_name AND m.year = k.year AND m.species = k.species AND m.phenomenon = '満開'
JOIN stations s ON s.station_name = k.station_name
WHERE k.phenomenon = '開花' AND k.species = 'そめいよしの' AND k.year <= 2025
```

```sql id=region_decade
SELECT region, (year // 10) * 10 AS decade, COUNT(*) AS n, COUNT(DISTINCT station_name) AS stations, ROUND(AVG(gap), 1) AS gap, ROUND(AVG(kaika), 1) AS kaika, ROUND(AVG(mankai), 1) AS mankai
FROM bloom
WHERE year >= 1960
GROUP BY region, decade
ORDER BY region, decade
```

```sql id=region_kyushu
SELECT decade, gap FROM region_decade WHERE region = '九州' ORDER BY decade
```

```sql id=region_west
SELECT decade, gap FROM region_decade WHERE region = '東海・近畿・中国・四国' ORDER BY decade
```

```sql id=region_east
SELECT decade, gap FROM region_decade WHERE region = '関東・甲信・北陸' ORDER BY decade
```

```sql id=region_north
SELECT decade, gap FROM region_decade WHERE region = '北海道・東北' ORDER BY decade
```

```sql id=shift
-- 1961〜1990年と1996〜2025年の30年平均。両期間とも25年以上そろう43地点
WITH p AS (
  SELECT station_name, region,
    COUNT(*) FILTER (WHERE year BETWEEN 1961 AND 1990) AS n1,
    COUNT(*) FILTER (WHERE year BETWEEN 1996 AND 2025) AS n2,
    AVG(kaika) FILTER (WHERE year BETWEEN 1961 AND 1990) AS k1,
    AVG(kaika) FILTER (WHERE year BETWEEN 1996 AND 2025) AS k2,
    AVG(mankai) FILTER (WHERE year BETWEEN 1961 AND 1990) AS m1,
    AVG(mankai) FILTER (WHERE year BETWEEN 1996 AND 2025) AS m2
  FROM bloom GROUP BY station_name, region
)
SELECT station_name, region, ROUND(k2 - k1, 1) AS kaika_change, ROUND(m2 - m1, 1) AS mankai_change, ROUND(m1 - k1, 1) AS gap_before, ROUND(m2 - k2, 1) AS gap_after, ROUND((m2 - k2) - (m1 - k1), 1) AS gap_change
FROM p WHERE n1 >= 25 AND n2 >= 25
ORDER BY gap_change DESC, station_name
```

```sql id=shift_up
-- 開花から満開までの日数が延びた地点。並び順は日数の変化の大きい順の逆
WITH r AS (SELECT *, ROW_NUMBER() OVER (ORDER BY gap_change DESC, station_name) AS rn FROM shift)
SELECT station_name, gap_change, gap_before, gap_after FROM r WHERE gap_change > 0 ORDER BY rn DESC
```

```sql id=shift_down
WITH r AS (SELECT *, ROW_NUMBER() OVER (ORDER BY gap_change DESC, station_name) AS rn FROM shift)
SELECT station_name, gap_change, gap_before, gap_after FROM r WHERE gap_change <= 0 ORDER BY rn DESC
```

```sql id=shift_summary
-- プロットはしない
SELECT COUNT(*) AS stations,
  COUNT(*) FILTER (WHERE kaika_change < 0) AS kaika_earlier,
  MIN(kaika_change) AS kaika_min, MAX(kaika_change) AS kaika_max,
  COUNT(*) FILTER (WHERE mankai_change > 0) AS mankai_later,
  COUNT(*) FILTER (WHERE gap_change > 0) AS gap_longer,
  COUNT(*) FILTER (WHERE gap_change >= 1.5) AS gap_longer_15,
  ROUND(AVG(gap_change) FILTER (WHERE region = '九州'), 1) AS kyushu_gap_change,
  ROUND(AVG(gap_change) FILTER (WHERE region = '北海道・東北'), 1) AS north_gap_change
FROM shift
```

```sql id=kagoshima
SELECT year, gap FROM bloom WHERE station_name = '鹿児島' ORDER BY year
```

```sql id=kagoshima_summary
-- プロットはしない
SELECT CASE WHEN year <= 2007 THEN '1953-2007' ELSE '2008-2025' END AS period, MIN(year) AS first_year, MAX(year) AS last_year, COUNT(*) AS years, COUNT(*) FILTER (WHERE gap >= 10) AS years_10plus, MIN(gap) AS min_gap, MAX(gap) AS max_gap, ROUND(AVG(gap), 1) AS avg_gap
FROM bloom WHERE station_name = '鹿児島'
GROUP BY period ORDER BY period
```

```sql id=winter
-- 1月前後の冷え込み（日最低気温の月平均の最低値、B4103）の1996〜2014年平均。東京の観測点が2014年12月に移転したため2014年までで切る
SELECT s.station_name, s.region, ROUND(AVG(TRY_CAST(b.value AS DOUBLE)), 2) AS winter_low, sh.gap_after, sh.gap_change
FROM e_stat.ssds.b_pref_land b
JOIN stations s ON s.area_name = b.area_name
JOIN shift sh ON sh.station_name = s.station_name
WHERE b.cat01 = 'B4103' AND b.year BETWEEN 1996 AND 2014 AND TRY_CAST(b.value AS DOUBLE) IS NOT NULL
GROUP BY s.station_name, s.region, sh.gap_after, sh.gap_change
ORDER BY winter_low
```

```sql id=winter_kyushu
SELECT station_name, winter_low, gap_after FROM winter WHERE region = '九州' ORDER BY winter_low
```

```sql id=winter_other
SELECT station_name, winter_low, gap_after FROM winter WHERE region <> '九州' ORDER BY winter_low
```

```sql id=winter_corr
-- プロットはしない
SELECT COUNT(*) AS stations, ROUND(CORR(winter_low, gap_after), 2) AS corr_gap, ROUND(CORR(winter_low, gap_change), 2) AS corr_change FROM winter
```

```sql id=winter_years
-- 同じ地点の中で、1975〜2014年の40年を1月前後の冷え込みの強い順に3等分し、開花から満開までの日数を平均する
WITH x AS (
  SELECT b2.station_name, CASE WHEN b2.region = '九州' THEN '九州' ELSE '九州以外' END AS grp, b2.year, b2.gap, TRY_CAST(e.value AS DOUBLE) AS low
  FROM bloom b2 JOIN e_stat.ssds.b_pref_land e ON e.area_name = b2.area_name AND e.year = b2.year AND e.cat01 = 'B4103'
  WHERE b2.year BETWEEN 1975 AND 2014 AND TRY_CAST(e.value AS DOUBLE) IS NOT NULL
), r AS (
  SELECT *, NTILE(3) OVER (PARTITION BY station_name ORDER BY low, year) AS t FROM x
)
SELECT grp, t, CASE t WHEN 1 THEN '冷え込みが強い年' WHEN 2 THEN '中くらいの年' ELSE '冷え込みが弱い年' END AS label, COUNT(*) AS n, ROUND(AVG(gap), 1) AS gap, ROUND(AVG(low), 1) AS low
FROM r GROUP BY grp, t ORDER BY grp, t
```

```sql id=winter_years_kyushu
SELECT label, gap FROM winter_years WHERE grp = '九州' ORDER BY t
```

```sql id=winter_years_other
SELECT label, gap FROM winter_years WHERE grp = '九州以外' ORDER BY t
```
