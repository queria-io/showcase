---
title: 学歴不詳を除くと、大卒者割合の東京都と青森県の差は19.7ポイントから30.4ポイントに広がる
description: 国勢調査の最終学歴データでは2020年に卒業者の14.9%が学歴不詳で、その割合は東京26.9%・山形6.2%と開きます。不詳を除いて集計し直すと、東京と青森の大卒者割合の差は19.7ポイントから30.4ポイントに広がります。
publishedAt: 2026-02-28
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 教育
  - 学歴
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系（都道府県データ）
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010105
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（E 教育）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/E
    publisher: 総務省統計局
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
agentHint: e_pref_education の2020年データで、短大・高専卒（E9105）の割合を卒業者総数ベースと学歴判明者ベースの両方で都道府県別に出して、順位がどれだけ入れ替わるか比べて
---

2020年の国勢調査で、大学・大学院卒の人が卒業者に占める割合は、卒業者総数を分母にすると東京都が31.6%、青森県が11.8%で、差は19.7ポイントです。最終学歴を答えなかった人（学歴不詳）を分母から除くと、東京都は43.2%、青森県は12.7%になり、差は30.4ポイントに広がります。学歴不詳の割合は東京都の26.9%から山形県の6.2%まで4倍以上の差があり、分母の取り方で都道府県の順位や推移の解釈も変わります。

自治体の人材政策や企業の立地検討では、都道府県別の大卒者割合を根拠に使うことがあります。この記事では、大卒者割合を卒業者総数と学歴が判明している卒業者の2つの分母で計算し、結果がどれだけ変わるかを確認します。

使うのは、総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010105)（SSDS）に収録された都道府県別の最終学歴人口です。国勢調査を出典とし、1980年から2020年まで10年おきの5時点が入っています。

| コード | 内容                           |
| ------ | ------------------------------ |
| E9101  | 最終学歴人口（卒業者総数）     |
| E9102  | 最終学歴人口（小学校・中学校） |
| E9103  | 最終学歴人口（高校・旧中）     |
| E9105  | 最終学歴人口（短大・高専）     |
| E9106  | 最終学歴人口（大学・大学院）   |

学歴の区分は `E9102`・`E9103`・`E9105`・`E9106` の4つで、それ以外の区分はありません。専修学校・各種学校は独立した区分ではなく、入学資格と修業年限に応じて4区分のいずれかに割り振られます（[項目定義 E91](https://www.e-stat.go.jp/koumoku/koumoku_teigi/E) の別表）。そのため、4区分の合計は卒業者総数（`E9101`）と一致するはずです。

実際には一致しません。2020年の全国では卒業者総数が100,763,239人、4区分の合計が85,703,934人で、15,059,305人（14.9%）が4区分のどこにも入っていません。これが最終卒業学校の種類を答えなかった人、いわゆる学歴不詳です。

## 学歴不詳は40年で0.2%から14.9%に増えた

学歴不詳の割合を1980年から集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "unknown_trend"},
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
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
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
          "axis": {"title": "学歴不詳の割合（%）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {"domain": ["東京都", "全国", "青森県"], "range": ["#ef4444", "#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "unknown_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"national\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "national", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "national",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "学歴不詳の割合（%）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {"domain": ["東京都", "全国", "青森県"], "range": ["#ef4444", "#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "unknown_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"aomori\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "aomori", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "aomori",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "学歴不詳の割合（%）", "grid": true}
        },
        "color": {
          "datum": "青森県",
          "type": "nominal",
          "scale": {"domain": ["東京都", "全国", "青森県"], "range": ["#ef4444", "#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1980年の全国の不詳は0.2%で、ほぼゼロでした。2000年でも3.8%です。2010年に13.1%へ大きく上がり、2020年は14.9%になっています。

上がり方は地域によって大きく異なります。東京都は1980年の0.4%から2010年に27.8%まで上がり、2020年も26.9%で、卒業者の4人に1人以上が最終学歴の区分に入っていません。同じ40年で青森県は0.2%から7.3%への上昇です。1980年には両者ともほぼゼロでしたが、2020年には約3.7倍の差があります。

不詳が全国で同じように増えていれば、分母に含めても都道府県の順位は変わりません。実際には都道府県によって増え方が異なるので、比較の前に不詳の割合を確認しておく必要があります。

## 学歴不詳の割合は、東京都の26.9%から山形県の6.2%まで4.3倍の差がある

2020年の47都道府県について、卒業者に占める学歴不詳の割合を並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "unk_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unk", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "unk",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "学歴不詳の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "unk_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unk", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "unk",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "学歴不詳の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "unk_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "unk", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "unk",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "学歴不詳の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは東京都の26.9%、最も低いのは山形県の6.2%で、4.3倍の差があります。上位は東京都・沖縄県（23.6%）・大阪府（22.7%）・京都府（20.0%）・神奈川県（17.9%）で、下位10はすべて10%未満です。

大都市圏の都府県が上位に入る傾向はありますが、それだけでは説明できません。沖縄県は2番目に高く、高知県（14.8%）と北海道（14.2%）も愛知県（13.6%）より高くなっています。静岡県は7.5%で下位10に入ります。不詳の割合は、県の人口規模や都市化の程度とは必ずしも対応していません。

分母に不詳を含めたまま大卒者割合を計算すると、不詳の多い県ほど大卒者割合が低くなります。

## 学歴が判明している人を分母にすると、東京都は43.2%、青森県は12.7%

分母を学歴が判明している卒業者（4区分の合計）に変えて、2020年の47都道府県の大卒者割合を集計しました。不詳の人が判明している人と同じ学歴構成だと仮定した場合の値です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rate_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大卒者割合（%・学歴判明者ベース）", "grid": true}
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
      "data": {"name": "rate_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大卒者割合（%・学歴判明者ベース）", "grid": true}
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
      "data": {"name": "rate_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大卒者割合（%・学歴判明者ベース）", "grid": true}
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

首位は東京都の43.2%です。卒業者総数を分母にした場合の31.6%より11.6ポイント高い値です。神奈川県は35.6%（総数ベース29.2%）、大阪府は28.1%（同21.8%）です。

最下位は青森県の12.7%で、総数ベースの11.8%との差は0.9ポイントです。青森県は不詳が7.3%と少ないためです。東京都が1位、青森県が47位という順位は分母を変えても同じですが、差は総数ベースの19.7ポイントから、判明者ベースでは30.4ポイントになります。

不詳の人に大卒者が多ければ実際の値はこれより高く、少なければ低くなります。この統計にはそれを判定できる情報がないので、確認できるのは、総数ベースの値は不詳率の高い県ほど低くなるということです。

## 沖縄県は、分母を変えると35位から22位に13順位上がる

上位10・下位10の境目の近くでは、入る県が入れ替わります。上位10には、総数ベースでは滋賀県（10位）が入り、判明者ベースでは代わりに大阪府（8位）が入ります。下位10からは高知県（総数39位・判明37位）が外れ、新潟県（同37位・40位）が入ります。順位が大きく変わる県を並べました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "shift_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "shift", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "shift",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "順位の変化（プラスが上昇）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "順位が下がる",
          "type": "nominal",
          "scale": {"domain": ["順位が下がる", "順位が上がる"], "range": ["#94a3b8", "#22c55e"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "shift_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "shift", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "shift",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "順位の変化（プラスが上昇）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "順位が上がる",
          "type": "nominal",
          "scale": {"domain": ["順位が下がる", "順位が上がる"], "range": ["#94a3b8", "#22c55e"]},
          "title": null
        }
      }
    }
  ]
}
```

最も大きく変わるのは沖縄県で、13順位上がります。卒業者総数を分母にすると35位ですが、学歴が判明している人を分母にすると22位で、47都道府県のほぼ中央です。不詳率が23.6%と全国で2番目に高いことが、総数ベースの順位を下げていました。

三重県が6順位、京都府と大阪府が3順位上がります。逆に下がるのは岐阜県（5順位）・福井県（4順位）・長野県・山口県・新潟県（各3順位）で、いずれも不詳率が10%を下回る県です。

沖縄県は、判明者ベースで20.6%（全国25.6%）、総数ベースで15.8%（全国21.7%）で、どちらの分母でも全国を下回ります。変わるのは都道府県の中での順位で、下位3分の1に入るかどうかで対象地域を絞る資料では、35位と22位で扱いが変わります。

全国平均を上回るかどうかが入れ替わる県も1つあります。滋賀県は総数ベースで22.4%と全国の21.7%を上回りますが、判明者ベースでは25.5%で全国の25.6%を0.04ポイント下回ります。47都道府県のうち、全国平均との上下が入れ替わるのは滋賀県だけです。全国平均を上回る県を対象にする資料では、分母の選択で滋賀県が対象に入るかどうかが決まるので、どちらの分母を使ったかを明記する必要があります。

## 2000年から2010年に、東京都と青森県の差は総数ベースでは縮小し、判明者ベースでは拡大した

東京都と青森県の大卒者割合の差を、2つの分母それぞれで1980年から集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "gap_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"gap_known\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gap_known", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "gap_known",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "東京都と青森県の差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "学歴判明者ベース",
          "type": "nominal",
          "scale": {"domain": ["学歴判明者ベース", "卒業者総数ベース"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "gap_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"gap_total\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "gap_total", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "gap_total",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "東京都と青森県の差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "卒業者総数ベース",
          "type": "nominal",
          "scale": {"domain": ["学歴判明者ベース", "卒業者総数ベース"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1980年はどちらも13.6ポイントで、不詳がほぼゼロだったため一致します。その後、2つの値の差は広がっていきます。

2000年から2010年に、卒業者総数ベースの差は17.0ポイントから16.0ポイントへ1.0ポイント縮小しました。学歴判明者ベースでは19.3ポイントから25.3ポイントへ6.0ポイント拡大しています。同じ10年について、分母によって縮小と拡大という逆の結果になります。

この10年に、東京都の不詳率は9.0%から27.8%へ上がりました。東京都の分母に含まれる不詳が大きく増えたので、総数ベースの東京都の値が低くなり、差が縮小したように見えていました。2020年には差は総数ベースで19.7ポイント、判明者ベースで30.4ポイントとなり、どちらの線も拡大を示します。

全国の大卒者割合も同じ影響を受けています。総数ベースでは1980年の8.8%から2020年の21.7%へ約2.5倍ですが、判明者ベースでは8.9%から25.6%へ約2.9倍です。40年間の増加は、総数ベースの数字より大きくなります。

## まとめ

- 2020年の全国では卒業者の14.9%が学歴不詳で、その割合は東京都26.9%から山形県6.2%まで4.3倍の差がある
- 分母を学歴判明者に変えると東京都は31.6%から43.2%へ、青森県は11.8%から12.7%へ変わり、両者の差は19.7ポイントから30.4ポイントに広がる
- 沖縄県は不詳率が23.6%と高く、分母の取り方で順位が35位から22位へ13上がる
- 滋賀県は総数ベースでは全国平均を上回り、判明者ベースでは全国との差が0.04ポイントで下回る。47都道府県でこの境界をまたぐのは滋賀県だけ
- 2000年から2010年の東京都と青森県の差は、総数ベースでは1.0ポイント縮小、判明者ベースでは6.0ポイント拡大と、逆の結論になる

同じテーブルの同じ列を使っても、分母に何を置くかで、地域差の大きさも推移の向きも変わります。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010105) の都道府県別の最終学歴人口を2026年8月6日時点で集計しています。元データは総務省統計局の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)をはじめとする各回の国勢調査で、収録は1980年から2020年まで10年おきの5時点です。区分の定義は[項目定義 E91](https://www.e-stat.go.jp/koumoku/koumoku_teigi/E) によります。

Queriaは、e-Statの最終学歴データを、列名・単位・文字コードを統一し、カテゴリコードと項目の説明を付けて公開しています。本記事で使った[都道府県別の学歴構成テーブル](/datasets/queria/e_stat/ssds/e_pref_education)から、関心のある地域の大卒者割合を2つの分母で計算できます。

```sql id=unknown_trend
WITH p AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND area_name IN ('全国', '東京都', '青森県') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2020 GROUP BY 1, 2 ) SELECT year, ROUND(MAX(CASE WHEN area_name = '全国' THEN (tot - known) / tot * 100 END), 1) AS national, ROUND(MAX(CASE WHEN area_name = '東京都' THEN (tot - known) / tot * 100 END), 1) AS tokyo, ROUND(MAX(CASE WHEN area_name = '青森県' THEN (tot - known) / tot * 100 END), 1) AS aomori, CAST(MAX(CASE WHEN area_name = '全国' THEN tot END) AS BIGINT) AS national_total_count, CAST(MAX(CASE WHEN area_name = '全国' THEN known END) AS BIGINT) AS national_known_count, CAST(MAX(CASE WHEN area_name = '全国' THEN tot - known END) AS BIGINT) AS national_unknown_count FROM p GROUP BY 1 ORDER BY 1
```

```sql id=unk_top
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), ranked AS ( SELECT area_name, ROUND((tot - known) / tot * 100, 1) AS unk, ROW_NUMBER() OVER (ORDER BY (tot - known) / tot DESC, area_name) AS rn FROM p ) SELECT area_name, unk FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=unk_mid
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), ranked AS ( SELECT area_name, ROUND((tot - known) / tot * 100, 1) AS unk, ROW_NUMBER() OVER (ORDER BY (tot - known) / tot DESC, area_name) AS rn FROM p ) SELECT area_name, unk FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=unk_bottom
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), ranked AS ( SELECT area_name, ROUND((tot - known) / tot * 100, 1) AS unk, ROW_NUMBER() OVER (ORDER BY (tot - known) / tot DESC, area_name) AS rn FROM p ) SELECT area_name, unk FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=rate_top
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), ranked AS ( SELECT area_name, ROUND(univ / known * 100, 1) AS rate, ROUND(univ / tot * 100, 1) AS rate_total, ROW_NUMBER() OVER (ORDER BY univ / known DESC, area_name) AS rn FROM p ) SELECT area_name, rate, rate_total FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rate_mid
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), ranked AS ( SELECT area_name, ROUND(univ / known * 100, 1) AS rate, ROUND(univ / tot * 100, 1) AS rate_total, ROW_NUMBER() OVER (ORDER BY univ / known DESC, area_name) AS rn FROM p ) SELECT area_name, rate, rate_total FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rate_bottom
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), ranked AS ( SELECT area_name, ROUND(univ / known * 100, 1) AS rate, ROUND(univ / tot * 100, 1) AS rate_total, ROW_NUMBER() OVER (ORDER BY univ / known DESC, area_name) AS rn FROM p ) SELECT area_name, rate, rate_total FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=flip_detail
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), n AS ( SELECT univ / tot AS nt, univ / known AS nk FROM p WHERE area_name = '全国' ) SELECT p.area_name, ROUND(p.univ / p.tot * 100, 2) AS rate_total, ROUND(p.univ / p.known * 100, 2) AS rate_known FROM p, n WHERE p.area_name = '全国' OR ((p.univ / p.tot > n.nt) <> (p.univ / p.known > n.nk)) ORDER BY p.area_name
```

```sql id=rank_boundary
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), r AS ( SELECT area_name, ROUND(univ / tot * 100, 1) AS rate_total, ROUND(univ / known * 100, 1) AS rate, ROW_NUMBER() OVER (ORDER BY univ / tot DESC, area_name) AS rn_tot, ROW_NUMBER() OVER (ORDER BY univ / known DESC, area_name) AS rn_known FROM p ) SELECT area_name, CAST(rn_tot AS INTEGER) AS rank_total, CAST(rn_known AS INTEGER) AS rank_known, rate_total, rate FROM r WHERE (rn_tot <= 10) <> (rn_known <= 10) OR (rn_tot >= 38) <> (rn_known >= 38) OR ABS(rn_tot - rn_known) >= 3 ORDER BY rn_known
```

```sql id=shift_down
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), r AS ( SELECT area_name, ROW_NUMBER() OVER (ORDER BY univ / tot DESC, area_name) AS rn_tot, ROW_NUMBER() OVER (ORDER BY univ / known DESC, area_name) AS rn_known FROM p ) SELECT area_name, CAST(rn_tot - rn_known AS INTEGER) AS shift FROM r WHERE rn_tot - rn_known <= -3 ORDER BY shift
```

```sql id=shift_up
WITH p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY 1 ), r AS ( SELECT area_name, ROW_NUMBER() OVER (ORDER BY univ / tot DESC, area_name) AS rn_tot, ROW_NUMBER() OVER (ORDER BY univ / known DESC, area_name) AS rn_known FROM p ) SELECT area_name, CAST(rn_tot - rn_known AS INTEGER) AS shift FROM r WHERE rn_tot - rn_known >= 3 ORDER BY shift
```

```sql id=gap_trend
WITH p AS ( SELECT year, area_name, MAX(CASE WHEN cat01 = 'E9101' THEN TRY_CAST(value AS DOUBLE) END) AS tot, SUM(CASE WHEN cat01 IN ('E9102', 'E9103', 'E9105', 'E9106') THEN TRY_CAST(value AS DOUBLE) END) AS known, MAX(CASE WHEN cat01 = 'E9106' THEN TRY_CAST(value AS DOUBLE) END) AS univ FROM e_stat.ssds.e_pref_education WHERE cat01 IN ('E9101', 'E9102', 'E9103', 'E9105', 'E9106') AND area_name IN ('全国', '東京都', '青森県') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2020 GROUP BY 1, 2 ) SELECT year, ROUND(MAX(CASE WHEN area_name = '東京都' THEN univ / tot * 100 END) - MAX(CASE WHEN area_name = '青森県' THEN univ / tot * 100 END), 1) AS gap_total, ROUND(MAX(CASE WHEN area_name = '東京都' THEN univ / known * 100 END) - MAX(CASE WHEN area_name = '青森県' THEN univ / known * 100 END), 1) AS gap_known, ROUND(MAX(CASE WHEN area_name = '全国' THEN univ / tot * 100 END), 1) AS national_total, ROUND(MAX(CASE WHEN area_name = '全国' THEN univ / known * 100 END), 1) AS national_known FROM p GROUP BY 1 ORDER BY 1
```
