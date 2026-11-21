---
title: 刑法犯は2年で13.5万件増え、増加分の4分の3は窃盗犯だった
description: 1975年から2023年の都道府県別データで刑法犯認知件数を集計しました。2021年から2023年の増加13.5万件のうち75%は窃盗犯で、知能犯は1割です。人口10万人あたりの犯罪率は大阪府が約915件、岩手県が約246件で、約3.7倍の差があります。
publishedAt: 2026-02-27
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 犯罪
  - 治安
  - 安全
  - 窃盗
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 犯罪統計
    url: https://www.npa.go.jp/publications/statistics/sousa/statistics.html
    publisher: 警察庁
agentHint: e_stat.ssds.k_pref_safety の K4201 と内訳5類型を使って、自分の県の2021年と2023年の認知件数の差を類型別に出して。全国の内訳と構成比も並べて比べたい
---

刑法犯の認知件数は2021年の約57万件から増加に転じ、2023年は約70万件になりました。2年で13.5万件の増加で、そのうち10.2万件、4分の3が窃盗犯の増加です。詐欺などを含む知能犯の増加は1.3万件で、全体の1割でした。2002年のピークからの減少215万件でも、88%は窃盗犯の減少です。

使ったのは e-Stat「社会・人口統計体系」の都道府県別データです。刑法犯認知件数の長期推移、直近の増加の犯罪類型別の内訳、人口あたり犯罪率の地域差を集計しました。

## 刑法犯認知件数は2002年の285万件から2021年の57万件へ80%減り、2023年は70万件

1975年から2023年までの刑法犯認知件数の推移です。認知件数は暦年（1月から12月）の合計で、e-Statの[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/K)でも「暦年計」とされています。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crimes\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "area",
        "color": "rgba(59,130,246,0.15)",
        "invalid": "break-paths-show-domains",
        "opacity": 1
      },
      "encoding": {
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crimes",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "認知件数", "grid": true}
        },
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crimes\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "crimes", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crimes",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "認知件数", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1975年の約123万件から1990年代半ばまで緩やかに増加したあと、1996年からの6年で181万件から285万件へ57%増え、2002年にピークを迎えました。その後は大きく減り、2021年には約57万件になりました。ピークからの減少率は80%です。2022年からは増加に転じ、2023年は約70万件です。それでもピークの4分の1で、1975年の水準も下回っています。この値は警察が認知した件数なので、被害の届出や警察の受理・計上の運用が変わると、犯罪の発生件数が同じでも変わります。

## 2002年からの減少215万件のうち、88%は窃盗犯の減少

犯罪類型別の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "crime_theft"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "認知件数", "grid": true}
        },
        "color": {
          "datum": "窃盗犯",
          "type": "nominal",
          "scale": {
            "domain": ["窃盗犯", "粗暴犯", "知能犯", "凶悪犯", "風俗犯"],
            "range": ["#3b82f6", "#f97316", "#8b5cf6", "#ef4444", "#14b8a6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "crime_violent"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "認知件数", "grid": true}
        },
        "color": {
          "datum": "粗暴犯",
          "type": "nominal",
          "scale": {
            "domain": ["窃盗犯", "粗暴犯", "知能犯", "凶悪犯", "風俗犯"],
            "range": ["#3b82f6", "#f97316", "#8b5cf6", "#ef4444", "#14b8a6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "crime_intellectual"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#8b5cf6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "認知件数", "grid": true}
        },
        "color": {
          "datum": "知能犯",
          "type": "nominal",
          "scale": {
            "domain": ["窃盗犯", "粗暴犯", "知能犯", "凶悪犯", "風俗犯"],
            "range": ["#3b82f6", "#f97316", "#8b5cf6", "#ef4444", "#14b8a6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "crime_heinous"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "認知件数", "grid": true}
        },
        "color": {
          "datum": "凶悪犯",
          "type": "nominal",
          "scale": {
            "domain": ["窃盗犯", "粗暴犯", "知能犯", "凶悪犯", "風俗犯"],
            "range": ["#3b82f6", "#f97316", "#8b5cf6", "#ef4444", "#14b8a6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "crime_public_morals"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"count\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#14b8a6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "count", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "count",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "認知件数", "grid": true}
        },
        "color": {
          "datum": "風俗犯",
          "type": "nominal",
          "scale": {
            "domain": ["窃盗犯", "粗暴犯", "知能犯", "凶悪犯", "風俗犯"],
            "range": ["#3b82f6", "#f97316", "#8b5cf6", "#ef4444", "#14b8a6"]
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

大きく変化しているのは窃盗犯だけで、他の4類型はいずれも目盛りの下端に重なっています。窃盗犯の推移は、1つ前の図の刑法犯総数とほぼ同じ形です。窃盗犯は2002年の約238万件から2023年の約48万件へ80%減りました。この間の刑法犯全体の減少215万件のうち、窃盗犯だけで189万件、率にして88%を占めます。

知能犯（詐欺・横領・偽造などを含む）の収録は2005年からで、それ以前の年はデータにありません。図の線も2005年から始まります。2023年の約5.0万件は2010年以降で最も多い値ですが、収録開始年である2005年の約9.8万件の半分ほどです。

## 2021年からの増加13.5万件のうち、4分の3は窃盗犯

類型ごとに2021年と2023年の差を計算しました。

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "change_21_23"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "increase", "type": "quantitative"},
          {"field": "category", "type": "nominal"}
        ],
        "x": {
          "field": "increase",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2021年から2023年の増加件数", "grid": true}
        },
        "y": {
          "field": "category",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        }
      }
    }
  ]
}
```

窃盗犯の増加が10.2万件で、刑法犯全体の増加13.5万件の75%を占めます。知能犯の増加は1.3万件で、全体の1割です。

窃盗犯は2021年の時点で刑法犯の67.2%を占めていました。増加分に占める75.4%はその1.12倍で、構成比と大きくは変わりません。長期の減少でも、2002年の構成比83.3%に対して減少分に占める割合は88.1%でした。窃盗犯が総数の増減の大部分を占めるのは、窃盗犯の件数がもともと多いためです。

増加率では、知能犯が窃盗犯を上回ります。2021年から2023年で知能犯は36.5%増え、窃盗犯は26.7%増えました。件数の増加への寄与は窃盗犯が大きく、増加率は知能犯が高くなっています。

この5類型の合計は刑法犯の総数と一致しません。どの類型にも入らない「その他の刑法犯」があり、2023年は約9.4万件がここに含まれます。上の図では、その他の刑法犯も1本の棒として並べています。

## 45県のうち43県で増加の半分以上が窃盗犯、島根県では窃盗犯が減った

都道府県ごとに同じ差を計算しました。総数が増えた45県について、増加分のうち窃盗犯が占める割合を並べています。

```chart
{
  "height": 930,
  "layer": [
    {
      "data": {"name": "pref_contrib"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "theft_contrib_pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "theft_contrib_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "増加分に占める窃盗犯の割合（2021年→2023年、%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null}
      }
    }
  ]
}
```

45県のうち43県は増加の半分以上を窃盗犯が占め、割合の中央値は72.3%です。半分を下回るのは奈良県の43.6%と島根県の2県だけでした。総数そのものが減った山形県（73件減）と富山県（45件減）は、割合が定義できないので図から外しています。

島根県は総数が107件（5.8%）増えるあいだに窃盗犯が31件（2.5%）減っており、窃盗犯が減りながら総数が増えたのはこの1県だけです。反対側の端は大分県で、総数の106件増に対して窃盗犯が170件増えました。窃盗犯以外の類型が減ったぶん、総数の伸びが窃盗犯の伸びを下回っています。

## 2023年の人口10万人あたりの犯罪率は、大阪府が岩手県の約3.7倍

件数で並べると人口の多い都道府県が上位に来るので、人口10万人あたりの犯罪率で比較します。分母は同じ年の総人口（`A1101`、10月1日現在）です。認知件数は事件が起きた場所で集計されるため、昼間に人が流入する都府県ほどこの値は高く出ます。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "crime_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "crime_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "crime_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "crime_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "crime_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "crime_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
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

大阪府が人口10万人あたり約915件で最も高く、群馬県、茨城県、兵庫県が続きます。最も低い岩手県は約246件で、大阪府との間に約3.7倍の差があります。上位10都府県には大都市圏に加えて北関東の3県（群馬県・茨城県・栃木県）と香川県が入ります。下位10県のうち東北は山形県・秋田県・岩手県の3県で、同じ東北でも宮城県は18位、福島県は24位です。地方ごとに順位がまとまっているわけではありません。

## 犯罪率の順位は、おもに窃盗犯の順位を表している

刑法犯に占める窃盗犯の割合は都道府県ごとに56.2%から78.2%で、中央値は66.5%です。総数の3分の2が窃盗犯なので、総数の順位は窃盗犯の順位に近くなります。実際に、両者の順位の差は平均2.5位です。

47都道府県について、人口10万人あたりの窃盗犯認知件数と、窃盗犯を除いた認知件数を並べました。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "theft_vs_other"},
      "mark": {"type": "point", "color": "#3b82f6", "opacity": 0.75, "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "theft_rate", "type": "quantitative"},
          {"field": "other_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "theft_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり窃盗犯認知件数", "grid": true}
        },
        "y": {
          "field": "other_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり窃盗犯以外の認知件数", "grid": true}
        }
      }
    }
  ]
}
```

2つの相関係数は0.675で、窃盗犯の多い県で他の犯罪も多いとは限りません。窃盗犯を除いて並べ直すと上位5県は兵庫県・香川県・大阪府・福岡県・沖縄県で、総数の上位5県（大阪府・群馬県・茨城県・兵庫県・埼玉県）とは3県が入れ替わります。順位のずれは平均5.6位、最大は栃木県の20位（総数で8位、窃盗犯を除くと28位）です。

人口あたりの犯罪率の順位は、おもに窃盗犯の多さの順位です。

## 大阪府の犯罪率は2001年の約3,710件から2023年の約915件に下がり、低下の89%は窃盗犯

大阪府・東京都・愛知県・秋田県の犯罪率の推移を、全国平均と比較しました。

```chart
{
  "layer": [
    {
      "data": {"name": "cr_osaka"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crime_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "crime_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "color": {
          "datum": "大阪府",
          "type": "nominal",
          "scale": {
            "domain": ["大阪府", "大阪府（窃盗犯のみ）", "愛知県", "東京都", "全国平均", "秋田県"],
            "range": ["#ef4444", "#ef4444", "#f97316", "#3b82f6", "#64748b", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "cr_osaka_theft"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"theft_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 2,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "theft_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "theft_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "color": {
          "datum": "大阪府（窃盗犯のみ）",
          "type": "nominal",
          "scale": {
            "domain": ["大阪府", "大阪府（窃盗犯のみ）", "愛知県", "東京都", "全国平均", "秋田県"],
            "range": ["#ef4444", "#ef4444", "#f97316", "#3b82f6", "#64748b", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "cr_aichi"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crime_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "crime_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "color": {
          "datum": "愛知県",
          "type": "nominal",
          "scale": {
            "domain": ["大阪府", "大阪府（窃盗犯のみ）", "愛知県", "東京都", "全国平均", "秋田県"],
            "range": ["#ef4444", "#ef4444", "#f97316", "#3b82f6", "#64748b", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "cr_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crime_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "crime_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["大阪府", "大阪府（窃盗犯のみ）", "愛知県", "東京都", "全国平均", "秋田県"],
            "range": ["#ef4444", "#ef4444", "#f97316", "#3b82f6", "#64748b", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "cr_national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crime_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "crime_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "color": {
          "datum": "全国平均",
          "type": "nominal",
          "scale": {
            "domain": ["大阪府", "大阪府（窃盗犯のみ）", "愛知県", "東京都", "全国平均", "秋田県"],
            "range": ["#ef4444", "#ef4444", "#f97316", "#3b82f6", "#64748b", "#22c55e"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "cr_akita"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"crime_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "crime_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "crime_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり認知件数", "grid": true}
        },
        "color": {
          "datum": "秋田県",
          "type": "nominal",
          "scale": {
            "domain": ["大阪府", "大阪府（窃盗犯のみ）", "愛知県", "東京都", "全国平均", "秋田県"],
            "range": ["#ef4444", "#ef4444", "#f97316", "#3b82f6", "#64748b", "#22c55e"]
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

大阪府は2001年にピークの約3,710件になり、そこから大きく下がって2023年には約915件です。点線は大阪府の窃盗犯だけの値で、2001年の約3,156件から2023年の約665件に下がっています。大阪府の犯罪率の低下のうち、89%は窃盗犯の低下です。

愛知県は2003年の約3,148件をピークに大幅な減少へ向かいました。東京都のピークは2002年の約2,460件で、2023年は約633件です。秋田県はもともと低い水準で推移しており、2023年の約263件は大阪府のピーク時の14分の1です。どの地域でも犯罪率は下がりましたが、地域間の差は残っています。

## まとめ

- 刑法犯認知件数は2002年の285万件から2021年の57万件へ80%減り、2023年は70万件まで戻した。それでもピークの4分の1で、1975年の123万件も下回る
- 2002年から2023年にかけての減少215万件のうち、88%は窃盗犯の減少
- 2021年から2023年の増加13.5万件のうち、75%も窃盗犯の増加。知能犯の増加は1割
- 島根県では、総数が107件増えるあいだに窃盗犯が31件減っている
- 人口10万人あたりの犯罪率は大阪府915件・岩手県246件で約3.7倍の差がある。窃盗犯を除いて並べ直すと上位5県のうち3県が入れ替わり、この順位はおもに窃盗犯の順位を表している

減少した期間でも増加した期間でも、都道府県の順位でも、刑法犯の総数の変化の大部分は窃盗犯によるものでした。知能犯は2023年に5.0万件で、2010年以降で最も多くなっていますが、2年間の増加13.5万件に占める割合は1割です。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview/prefectures)の都道府県データを2026年8月24日時点で集計しています。使ったのは安全統計の `K4201_刑法犯認知件数` とその内訳（`K420101_凶悪犯`・`K420102_粗暴犯`・`K420103_窃盗犯`・`K420104_知能犯`・`K420105_風俗犯`）、および人口統計の `A1101_総人口` です。認知件数の元データは警察庁の[犯罪統計](https://www.npa.go.jp/publications/statistics/sousa/statistics.html)で、収録は1975年から2023年まで、知能犯のみ2005年からです。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の安全・犯罪統計テーブル](/datasets/queria/e_stat/ssds/k_pref_safety)から、自分の県の認知件数を類型別・年次別に集計できます。

```sql id=trend
SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ORDER BY year
```

```sql id=crime_theft
SELECT year, value AS count FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420103' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ORDER BY year
```

```sql id=crime_violent
SELECT year, value AS count FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420102' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ORDER BY year
```

```sql id=crime_intellectual
SELECT year, value AS count FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420104' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ORDER BY year
```

```sql id=crime_heinous
SELECT year, value AS count FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420101' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ORDER BY year
```

```sql id=crime_public_morals
SELECT year, value AS count FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420105' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ORDER BY year
```

```sql id=change_21_23
WITH y AS ( SELECT cat01, MAX(CASE WHEN year = 2021 THEN TRY_CAST(value AS DOUBLE) END) AS y2021, MAX(CASE WHEN year = 2023 THEN TRY_CAST(value AS DOUBLE) END) AS y2023 FROM e_stat.ssds.k_pref_safety WHERE area_name = '全国' AND value IS NOT NULL AND cat01 IN ('K4201', 'K420101', 'K420102', 'K420103', 'K420104', 'K420105') AND year IN (2021, 2023) GROUP BY cat01 ), named AS ( SELECT CASE cat01 WHEN 'K420101' THEN '凶悪犯' WHEN 'K420102' THEN '粗暴犯' WHEN 'K420103' THEN '窃盗犯' WHEN 'K420104' THEN '知能犯' WHEN 'K420105' THEN '風俗犯' END AS category, y2021, y2023 FROM y WHERE cat01 <> 'K4201' ), other AS ( SELECT 'その他の刑法犯' AS category, (SELECT y2021 FROM y WHERE cat01 = 'K4201') - (SELECT SUM(y2021) FROM named) AS y2021, (SELECT y2023 FROM y WHERE cat01 = 'K4201') - (SELECT SUM(y2023) FROM named) AS y2023 ) SELECT category, y2021, y2023, y2023 - y2021 AS increase FROM (SELECT * FROM named UNION ALL SELECT * FROM other) ORDER BY increase
```

```sql id=pref_change
WITH y AS ( SELECT area_name, cat01, MAX(CASE WHEN year = 2021 THEN TRY_CAST(value AS DOUBLE) END) AS y2021, MAX(CASE WHEN year = 2023 THEN TRY_CAST(value AS DOUBLE) END) AS y2023 FROM e_stat.ssds.k_pref_safety WHERE area_name <> '全国' AND value IS NOT NULL AND cat01 IN ('K4201', 'K420103') AND year IN (2021, 2023) GROUP BY area_name, cat01 ), w AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'K4201' THEN y2021 END) AS total_2021, MAX(CASE WHEN cat01 = 'K420103' THEN y2021 END) AS theft_2021, MAX(CASE WHEN cat01 = 'K4201' THEN y2023 - y2021 END) AS total_change, MAX(CASE WHEN cat01 = 'K420103' THEN y2023 - y2021 END) AS theft_change FROM y GROUP BY area_name ), j AS ( SELECT area_name, total_change, theft_change, ROUND(total_change * 100.0 / total_2021, 1) AS total_change_pct, ROUND(theft_change * 100.0 / theft_2021, 1) AS theft_change_pct, CASE WHEN total_change > 0 THEN ROUND(theft_change * 100.0 / total_change, 1) END AS theft_contrib_pct FROM w ), stat AS ( SELECT COUNT(*) FILTER (WHERE total_change > 0) AS n_up, COUNT(*) FILTER (WHERE total_change < 0) AS n_down, COUNT(*) FILTER (WHERE theft_contrib_pct >= 50) AS n_theft_led, ROUND(MEDIAN(theft_contrib_pct), 1) AS median_contrib FROM j ) SELECT j.area_name, j.total_change, j.theft_change, j.total_change_pct, j.theft_change_pct, j.theft_contrib_pct, stat.n_up, stat.n_down, stat.n_theft_led, stat.median_contrib FROM j CROSS JOIN stat ORDER BY j.total_change_pct DESC
```

```sql id=pref_contrib
WITH y AS ( SELECT area_name, cat01, MAX(CASE WHEN year = 2021 THEN TRY_CAST(value AS DOUBLE) END) AS y2021, MAX(CASE WHEN year = 2023 THEN TRY_CAST(value AS DOUBLE) END) AS y2023 FROM e_stat.ssds.k_pref_safety WHERE area_name <> '全国' AND value IS NOT NULL AND cat01 IN ('K4201', 'K420103') AND year IN (2021, 2023) GROUP BY area_name, cat01 ), w AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'K4201' THEN y2023 - y2021 END) AS total_change, MAX(CASE WHEN cat01 = 'K420103' THEN y2023 - y2021 END) AS theft_change FROM y GROUP BY area_name ) SELECT area_name, total_change, theft_change, ROUND(theft_change * 100.0 / total_change, 1) AS theft_contrib_pct FROM w WHERE total_change > 0 ORDER BY theft_contrib_pct DESC
```

```sql id=theft_vs_other
WITH t AS ( SELECT area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name <> '全国' AND year = 2023 ), th AS ( SELECT area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420103' AND value IS NOT NULL AND area_name <> '全国' AND year = 2023 ), p AS ( SELECT area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name <> '全国' AND year = 2023 ), j AS ( SELECT t.area_name, ROUND(t.v / p.v * 100000, 1) AS total_rate, ROUND(th.v / p.v * 100000, 1) AS theft_rate, ROUND((t.v - th.v) / p.v * 100000, 1) AS other_rate, ROUND(th.v / t.v * 100, 1) AS theft_share FROM t JOIN th ON t.area = th.area JOIN p ON t.area = p.area ), r AS ( SELECT area_name, total_rate, theft_rate, other_rate, theft_share, RANK() OVER (ORDER BY total_rate DESC, area_name) AS rank_total, RANK() OVER (ORDER BY theft_rate DESC, area_name) AS rank_theft, RANK() OVER (ORDER BY other_rate DESC, area_name) AS rank_other FROM j ), stat AS ( SELECT ROUND(CORR(theft_rate, other_rate), 3) AS corr_theft_other, ROUND(AVG(ABS(rank_total - rank_theft)), 1) AS avg_gap_theft, ROUND(AVG(ABS(rank_total - rank_other)), 1) AS avg_gap_other, MAX(ABS(rank_total - rank_other)) AS max_gap_other, ROUND(MEDIAN(theft_share), 1) AS median_share, MIN(theft_share) AS min_share, MAX(theft_share) AS max_share FROM r ) SELECT r.area_name, r.total_rate, r.theft_rate, r.other_rate, r.theft_share, r.rank_total, r.rank_theft, r.rank_other, stat.corr_theft_other, stat.avg_gap_theft, stat.avg_gap_other, stat.max_gap_other, stat.median_share, stat.min_share, stat.max_share FROM r CROSS JOIN stat ORDER BY r.rank_total
```

```sql id=cr_osaka_theft
WITH crime AS ( SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K420103' AND value IS NOT NULL AND area_name = '大阪府' AND year <= 2023 ), pop AS ( SELECT year, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name = '大阪府' AND year <= 2023 ) SELECT c.year, ROUND(c.crimes / p.population * 100000, 1) AS theft_rate FROM crime c JOIN pop p ON c.year = p.year ORDER BY c.year
```

```sql id=crime_top
WITH crime AS ( SELECT area, area_name, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name != '全国' AND year = 2023 ), pop AS ( SELECT area, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name != '全国' AND year = 2023 ), ranked AS ( SELECT c.area_name, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate, ROW_NUMBER() OVER (ORDER BY c.crimes / p.population DESC, c.area_name) AS rn FROM crime c JOIN pop p ON c.area = p.area ) SELECT area_name, crime_rate FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=crime_mid
WITH crime AS ( SELECT area, area_name, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name != '全国' AND year = 2023 ), pop AS ( SELECT area, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name != '全国' AND year = 2023 ), ranked AS ( SELECT c.area_name, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate, ROW_NUMBER() OVER (ORDER BY c.crimes / p.population DESC, c.area_name) AS rn FROM crime c JOIN pop p ON c.area = p.area ) SELECT area_name, crime_rate FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=crime_bottom
WITH crime AS ( SELECT area, area_name, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name != '全国' AND year = 2023 ), pop AS ( SELECT area, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name != '全国' AND year = 2023 ), ranked AS ( SELECT c.area_name, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate, ROW_NUMBER() OVER (ORDER BY c.crimes / p.population DESC, c.area_name) AS rn FROM crime c JOIN pop p ON c.area = p.area ) SELECT area_name, crime_rate FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=cr_osaka
WITH crime AS ( SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name = '大阪府' AND year <= 2023 ), pop AS ( SELECT year, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name = '大阪府' AND year <= 2023 ) SELECT c.year, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate FROM crime c JOIN pop p ON c.year = p.year ORDER BY c.year
```

```sql id=cr_aichi
WITH crime AS ( SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name = '愛知県' AND year <= 2023 ), pop AS ( SELECT year, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name = '愛知県' AND year <= 2023 ) SELECT c.year, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate FROM crime c JOIN pop p ON c.year = p.year ORDER BY c.year
```

```sql id=cr_tokyo
WITH crime AS ( SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name = '東京都' AND year <= 2023 ), pop AS ( SELECT year, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name = '東京都' AND year <= 2023 ) SELECT c.year, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate FROM crime c JOIN pop p ON c.year = p.year ORDER BY c.year
```

```sql id=cr_national
WITH crime AS ( SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ), pop AS ( SELECT year, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name = '全国' AND year <= 2023 ) SELECT c.year, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate FROM crime c JOIN pop p ON c.year = p.year ORDER BY c.year
```

```sql id=cr_akita
WITH crime AS ( SELECT year, value AS crimes FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K4201' AND value IS NOT NULL AND area_name = '秋田県' AND year <= 2023 ), pop AS ( SELECT year, value AS population FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND value IS NOT NULL AND area_name = '秋田県' AND year <= 2023 ) SELECT c.year, ROUND(c.crimes / p.population * 100000, 1) AS crime_rate FROM crime c JOIN pop p ON c.year = p.year ORDER BY c.year
```
