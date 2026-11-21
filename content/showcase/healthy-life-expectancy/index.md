---
title: 男性の健康寿命は、最も長い大分県と最も短い岩手県で2.33歳違う
description: 平均寿命と健康寿命の差（不健康な期間）は、男性で約8.9年、女性で約12.3年です。2019年の男性の健康寿命は大分県73.72歳、岩手県71.39歳で2.33歳の差があり、健康寿命と平均寿命の都道府県の相関は0.471でした。
publishedAt: 2026-02-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 健康
  - 寿命
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 統計でみる都道府県・市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 令和2年都道府県別生命表の概況
    url: https://www.mhlw.go.jp/toukei/saikin/hw/life/tdfk20/index.html
    publisher: 厚生労働省
  - title: 健康寿命の令和元年値について（第16回健康日本21（第二次）推進専門委員会 資料3-1）
    url: https://www.mhlw.go.jp/content/10904750/000872952.pdf
    publisher: 厚生労働省
agentHint: 女性の健康寿命（cat01=I1602）の2019年の都道府県ランキングを出して、男性で上位だった大分・山梨と同じ顔ぶれになるか比べて。女性の平均寿命（I1102）との差＝不健康な期間も都道府県別に出して
---

2019年の男性の健康寿命は、最も長い大分県が73.72歳、最も短い岩手県が71.39歳で、2.33歳の差がありました。全国では、平均寿命と健康寿命の差（不健康な期間）が男性で約8.9年、女性で約12.3年です。健康寿命と平均寿命の都道府県の相関は0.471で、平均寿命が2位の長野県は、健康寿命では30位でした。

全国の平均寿命は、2020年で男性81.56歳、女性87.71歳です。日常生活に制限のない期間を表す「健康寿命」は、2019年で男性72.68歳、女性75.38歳でした。この記事では、e-Stat の「[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)」の都道府県データを使い、健康寿命の全国の推移と都道府県の差を集計します。健康寿命は、平均寿命と同じ生命表と人口動態統計に、[国民生活基礎調査](https://www.mhlw.go.jp/toukei/list/20-21.html)で「健康上の問題で日常生活に影響がない」と答えた人の割合を組み合わせて算出されます（[健康寿命の令和元年値について](https://www.mhlw.go.jp/content/10904750/000872952.pdf)）。死亡の記録は2つの指標で共通で、健康寿命だけが健康状態を本人の回答で測っています。

## 平均寿命と健康寿命の差は、10年でわずかしか縮んでいない

全国の平均寿命（0歳の平均余命）と健康寿命を、男女別に重ねました。上の線が平均寿命、下の線が健康寿命で、その間が「不健康な期間」です。

```chart
{
  "layer": [
    {
      "data": {"name": "le_male"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"years\"]) ? 0 : 1",
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
          {"field": "years", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "years",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年齢（歳）", "grid": true}
        },
        "color": {
          "datum": "平均寿命（男性）",
          "type": "nominal",
          "scale": {
            "domain": ["平均寿命（男性）", "平均寿命（女性）", "健康寿命（男性）", "健康寿命（女性）"],
            "range": ["#3b82f6", "#ec4899", "#22c55e", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "le_female"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"years\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "years", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "years",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年齢（歳）", "grid": true}
        },
        "color": {
          "datum": "平均寿命（女性）",
          "type": "nominal",
          "scale": {
            "domain": ["平均寿命（男性）", "平均寿命（女性）", "健康寿命（男性）", "健康寿命（女性）"],
            "range": ["#3b82f6", "#ec4899", "#22c55e", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "hle_male"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"years\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "years", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "years",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年齢（歳）", "grid": true}
        },
        "color": {
          "datum": "健康寿命（男性）",
          "type": "nominal",
          "scale": {
            "domain": ["平均寿命（男性）", "平均寿命（女性）", "健康寿命（男性）", "健康寿命（女性）"],
            "range": ["#3b82f6", "#ec4899", "#22c55e", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "hle_female"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"years\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "years", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "years",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年齢（歳）", "grid": true}
        },
        "color": {
          "datum": "健康寿命（女性）",
          "type": "nominal",
          "scale": {
            "domain": ["平均寿命（男性）", "平均寿命（女性）", "健康寿命（男性）", "健康寿命（女性）"],
            "range": ["#3b82f6", "#ec4899", "#22c55e", "#f97316"]
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

平均寿命と健康寿命はどちらも延びていますが、2つの差の縮まり方は小さくなっています。男性の不健康な期間は、2010年が約9.1年（平均寿命79.55歳 − 健康寿命70.42歳）、2019年の健康寿命と2020年の平均寿命の差が約8.9年（81.56歳 − 72.68歳）です。女性は約12.7年（86.30歳 − 73.62歳）から約12.3年（87.71歳 − 75.38歳）です。2010年は同じ年どうしの差、2019年は翌年の平均寿命との差です。翌年の平均寿命のほうが長い分だけ2019年の差は大きくなるので、同じ年どうしで比較すれば、差の縮小はこれより大きくなります。

2016年の健康寿命は46都道府県の集計です。熊本地震のため、この年の国民生活基礎調査では熊本県が調査されていません。

## 男性の健康寿命は大分県が73.72歳で最も長く、岩手県の71.39歳と2.33歳違う

2019年の男性の健康寿命を、都道府県ごとに並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "hle_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "healthy_years", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "healthy_years",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "健康寿命（歳）", "grid": true}
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
      "data": {"name": "hle_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "healthy_years", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "healthy_years",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "健康寿命（歳）", "grid": true}
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
      "data": {"name": "hle_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "healthy_years", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "healthy_years",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "健康寿命（歳）", "grid": true}
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

男性の健康寿命が最も長いのは大分県（73.72歳）で、山梨県（73.57歳）、埼玉県（73.48歳）が続きます。最も短いのは岩手県（71.39歳）で、愛媛県（71.50歳）、鳥取県（71.58歳）が続きます。大分県と岩手県の差は2.33歳です。

都道府県ごとの健康寿命は標本調査に基づく推計で、[公表資料](https://www.mhlw.go.jp/content/10904750/000872952.pdf)には95%信頼区間が記載されています。信頼区間は隣り合う順位の差より広いので、1つや2つの順位の差は、実際の違いとは言えません。以下で順位を挙げるのは、上位と下位のように大きく離れた県を比較するためです。

## 健康寿命と平均寿命の相関は0.471で、長野県は平均寿命2位・健康寿命30位

2019年の男性の健康寿命を横軸、2020年の男性の平均寿命を縦軸にして、47都道府県を並べました。2つの指標の相関は0.471です。どちらも死亡の記録から作った生命表をもとにしていますが、都道府県の順位は一致しない部分が多くあります。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "le_hle"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "hle", "type": "quantitative"},
          {"field": "le", "type": "quantitative"}
        ],
        "x": {
          "field": "hle",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "健康寿命（2019年・男性、歳）", "grid": true}
        },
        "y": {
          "field": "le",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "平均寿命（2020年・男性、歳）", "grid": true}
        }
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

健康寿命が1位の大分県は、平均寿命では12位（81.88歳）です。健康寿命3位の埼玉県は平均寿命24位（81.44歳）、7位の鹿児島県は38位（80.95歳）です。逆に、平均寿命2位の長野県（82.68歳）は健康寿命30位（72.55歳）、9位の熊本県（81.91歳）は健康寿命37位（72.24歳）です。健康寿命の上位10県のうち、平均寿命でも上位10県に入るのは、滋賀県（平均寿命1位・健康寿命4位）と福井県（7位・10位）の2県だけです。

都道府県の差は、健康寿命が2.33歳、平均寿命が3.46歳です。平均寿命の上位の県から、健康寿命の上位の県を推測することはできません。

## 不健康な期間は長野県が10.13年で最も長い

平均寿命と健康寿命の差を「不健康な期間」と呼びます。この記事では、それぞれの最新値である2019年の健康寿命と2020年の平均寿命の差として計算しています。健康寿命は3年ごと、平均寿命は5年ごとの値で、同じ年がそろうのは2010年が最後だからです。平均寿命は年々延びているので、この差は同じ年どうしで計算した場合よりわずかに大きくなります。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "gap_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unhealthy_years", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "unhealthy_years",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "不健康な期間（年）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10（長い）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（長い）", "中間", "下位10（短い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "gap_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unhealthy_years", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "unhealthy_years",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "不健康な期間（年）", "grid": true}
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
          "scale": {
            "domain": ["上位10（長い）", "中間", "下位10（短い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "gap_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unhealthy_years", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "unhealthy_years",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "不健康な期間（年）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10（短い）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（長い）", "中間", "下位10（短い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ]
}
```

不健康な期間が最も長いのは長野県（10.13年）です。平均寿命82.68歳に対して、健康寿命が72.55歳と中位だからです。長野県の健康寿命の順位は、2010年の6位から2019年の30位に下がっています。

不健康な期間が最も短いのは青森県（7.54年）です。これは、健康寿命が71.73歳で下位10県に入り、平均寿命も79.27歳で47都道府県のうち最も短いためです。不健康な期間が短いことは、健康でいられる年数が長いことを表してはいないので、健康寿命の水準と合わせて比較する必要があります。

## 2010年から2019年に、大分県の健康寿命は3.87歳延び、39位から1位になった

2010年から2019年にかけての男性の健康寿命の延びを、延びの大きい10県と小さい10県で比較します。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "imp_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "improvement", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "improvement",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "健康寿命の変化（歳）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10（改善大）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（改善大）", "中間", "下位10（改善小）"],
            "range": ["#22c55e", "#86efac", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "imp_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "improvement", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "improvement",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "健康寿命の変化（歳）", "grid": true}
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
          "scale": {
            "domain": ["上位10（改善大）", "中間", "下位10（改善小）"],
            "range": ["#22c55e", "#86efac", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "imp_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "improvement", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "improvement",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "健康寿命の変化（歳）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10（改善小）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（改善大）", "中間", "下位10（改善小）"],
            "range": ["#22c55e", "#86efac", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ]
}
```

大分県は9年間で3.87歳延び、2010年の39位から2019年の1位になりました。長崎県（+3.15歳）と東京都（+2.95歳、33位から14位）も大きく延びています。2010年に1位だった愛知県は延びが1.11歳で18位に、3位だった千葉県は0.99歳で26位に下がりました。延びが最も小さい県でも1歳前後は延びているので、順位の入れ替わりは、健康寿命が短くなったためではなく、延び方の違いによるものです。

数位分の順位の上下は、推計の信頼区間の範囲に収まります。大分県の+3.87歳や東京都の+2.95歳のように延びが大きい県の変化は、推計の幅を考えても確かな変化と言えます。

## まとめ

- 平均寿命と健康寿命の差（不健康な期間）は、男性約8.9年、女性約12.3年で、過去10年でわずかしか縮んでいない
- 男性の健康寿命の都道府県の差は2.33歳で、大分県・山梨県が長く、岩手県・愛媛県が短い
- 健康寿命と平均寿命の相関は0.471。健康寿命1位の大分県は平均寿命12位、平均寿命2位の長野県は健康寿命30位
- 健康寿命の順位は9年で大きく入れ替わり、大分県は39位から1位に、2010年に1位だった愛知県は18位になった（都道府県の値は信頼区間のある推計なので、数位分の上下は誤差の範囲）

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)（総務省統計局）の `e_stat.ssds.i_pref_health` を2026年8月30日時点で集計しています。使った分類コードは、平均寿命が男性 I1101・女性 I1102、健康寿命が男性 I1601・女性 I1602 です。健康寿命は2010年から2019年までの4時点、平均寿命は1975年から2020年までの10時点の値が入っています。元データは厚生労働省の[令和2年都道府県別生命表](https://www.mhlw.go.jp/toukei/saikin/hw/life/tdfk20/index.html)と[健康寿命の令和元年値について](https://www.mhlw.go.jp/content/10904750/000872952.pdf)で、健康寿命は簡易生命表・人口動態統計・国民生活基礎調査・推計人口からサリバン法で算出された値です。指標の定義は[項目定義 I 健康・医療](https://www.e-stat.go.jp/koumoku/koumoku_teigi/I) によります。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の健康・寿命統計テーブル](/datasets/queria/e_stat/ssds/i_pref_health)から、任意の都道府県の健康寿命と平均寿命を取り出せます。

```sql id=le_male
SELECT year, TRY_CAST(value AS DOUBLE) AS years FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1101' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year >= 2000 ORDER BY year
```

```sql id=le_female
SELECT year, TRY_CAST(value AS DOUBLE) AS years FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1102' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year >= 2000 ORDER BY year
```

```sql id=hle_male
SELECT year, TRY_CAST(value AS DOUBLE) AS years FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year >= 2000 ORDER BY year
```

```sql id=hle_female
SELECT year, TRY_CAST(value AS DOUBLE) AS years FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1602' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year >= 2000 ORDER BY year
```

```sql id=hle_top
WITH ranked AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS healthy_years, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) SELECT area_name, healthy_years FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=hle_mid
WITH ranked AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS healthy_years, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) SELECT area_name, healthy_years FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=hle_bottom
WITH ranked AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS healthy_years, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) SELECT area_name, healthy_years FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=gap_top
WITH healthy AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS hle FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), life AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS le FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1101' AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), ranked AS ( SELECT h.area_name, ROUND(l.le - h.hle, 2) AS unhealthy_years, ROW_NUMBER() OVER (ORDER BY (l.le - h.hle) DESC, h.area_name) AS rn FROM healthy h JOIN life l ON h.area_name = l.area_name ) SELECT area_name, unhealthy_years FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=gap_mid
WITH healthy AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS hle FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), life AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS le FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1101' AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), ranked AS ( SELECT h.area_name, ROUND(l.le - h.hle, 2) AS unhealthy_years, ROW_NUMBER() OVER (ORDER BY (l.le - h.hle) DESC, h.area_name) AS rn FROM healthy h JOIN life l ON h.area_name = l.area_name ) SELECT area_name, unhealthy_years FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=gap_bottom
WITH healthy AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS hle FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), life AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS le FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1101' AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), ranked AS ( SELECT h.area_name, ROUND(l.le - h.hle, 2) AS unhealthy_years, ROW_NUMBER() OVER (ORDER BY (l.le - h.hle) DESC, h.area_name) AS rn FROM healthy h JOIN life l ON h.area_name = l.area_name ) SELECT area_name, unhealthy_years FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=imp_top
WITH y2010 AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS v2010 FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2010 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), y2019 AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS v2019 FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), ranked AS ( SELECT a.area_name, ROUND(b.v2019 - a.v2010, 2) AS improvement, ROW_NUMBER() OVER (ORDER BY (b.v2019 - a.v2010) DESC, a.area_name) AS rn FROM y2010 a JOIN y2019 b ON a.area_name = b.area_name ) SELECT area_name, improvement FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=imp_mid
WITH y2010 AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS v2010 FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2010 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), y2019 AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS v2019 FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), ranked AS ( SELECT a.area_name, ROUND(b.v2019 - a.v2010, 2) AS improvement, ROW_NUMBER() OVER (ORDER BY (b.v2019 - a.v2010) DESC, a.area_name) AS rn FROM y2010 a JOIN y2019 b ON a.area_name = b.area_name ) SELECT area_name, improvement FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=imp_bottom
WITH y2010 AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS v2010 FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2010 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), y2019 AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS v2019 FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), ranked AS ( SELECT a.area_name, ROUND(b.v2019 - a.v2010, 2) AS improvement, ROW_NUMBER() OVER (ORDER BY (b.v2019 - a.v2010) DESC, a.area_name) AS rn FROM y2010 a JOIN y2019 b ON a.area_name = b.area_name ) SELECT area_name, improvement FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=le_hle
WITH h AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS hle FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), l AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS le FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1101' AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) SELECT h.area_name, h.hle, l.le, RANK() OVER (ORDER BY h.hle DESC) AS hle_rank, RANK() OVER (ORDER BY l.le DESC) AS le_rank FROM h JOIN l ON h.area_name = l.area_name ORDER BY h.area_name
```

```sql id=spread
WITH h AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS hle FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year = 2019 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), l AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS le FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1101' AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ) SELECT COUNT(*) AS pref_count, ROUND(MAX(hle) - MIN(hle), 2) AS hle_range, ROUND(MAX(le) - MIN(le), 2) AS le_range, ROUND(CORR(hle, le), 3) AS corr_hle_le FROM h JOIN l ON h.area_name = l.area_name
```

```sql id=rank_shift
WITH y AS ( SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I1601' AND year IN (2010, 2019) AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name != '全国' ), r AS ( SELECT year, area_name, v, RANK() OVER (PARTITION BY year ORDER BY v DESC) AS rn FROM y ) SELECT a.area_name, a.rn AS rank_2010, b.rn AS rank_2019, ROUND(b.v - a.v, 2) AS change_years FROM r a JOIN r b ON a.area_name = b.area_name AND a.year = 2010 AND b.year = 2019 ORDER BY a.area_name
```

```sql id=coverage
SELECT cat01, MIN(year) AS min_year, MAX(year) AS max_year, COUNT(DISTINCT year) AS year_count FROM e_stat.ssds.i_pref_health WHERE cat01 IN ('I1101', 'I1102', 'I1601', 'I1602') AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY cat01 ORDER BY cat01
```

```sql id=pref_counts
SELECT year, COUNT(DISTINCT CASE WHEN cat01 = 'I1101' THEN area_name END) AS le_pref, COUNT(DISTINCT CASE WHEN cat01 = 'I1601' THEN area_name END) AS hle_pref FROM e_stat.ssds.i_pref_health WHERE cat01 IN ('I1101', 'I1601') AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year >= 2000 GROUP BY year ORDER BY year
```
