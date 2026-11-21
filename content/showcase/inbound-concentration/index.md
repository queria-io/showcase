---
title: 外国人の宿泊はコロナ前を上回ったが、増えた分の8割余りは東京・大阪・京都に入った
description: 従業者10人以上の施設で、2024年の外国人延べ宿泊者数は2019年の1.37倍。増えた3,722万人泊のうち3,142万人泊が東京・大阪・京都で、17県は2019年を下回ります。
publishedAt: 2026-02-28
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - インバウンド
  - 観光
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 宿泊旅行統計調査
    url: https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html
    publisher: 観光庁
  - title: 宿泊旅行統計調査 2024年1月〜12月分（年の確定値）報道発表資料
    url: https://www.mlit.go.jp/kankocho/content/002026765.pdf
    publisher: 観光庁
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（G 文化・スポーツ）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/G
    publisher: 総務省統計局
agentHint: 外国人延べ宿泊者数（G7102）と国・地域別（G710201〜G710204）を都道府県別に2019年と2024年で並べて、中国以外の増減を韓国・台湾・米国・その他に分けて
socialAnnounce: |-
  2024年の外国人の延べ宿泊者数は2019年の1.37倍（従業者10人以上の施設）。

  増えた3,722万人泊のうち3,142万人泊は東京都・大阪府・京都府。残る44道県の合計は12.0%増にとどまり、17県は2019年を下回っています。
---

海外から来た人がホテルや旅館に泊まった延べ人数は、2024年にコロナ前を大きく上回りました。従業者10人以上の施設で1億3,853万人泊、2019年の1億131万人泊の1.37倍です。

都道府県別に集計すると、全国で増えた3,722万人泊のうち3,142万人泊は、東京都・大阪府・京都府の3都府県が占めていました。47都道府県のうち17県は、2024年になっても2019年の人数に戻っていません。17県のうち5県は中国からの宿泊が減った分を除けば2019年を上回っていて、残る12県は中国以外の国・地域からの宿泊が減っています。台湾と韓国からの宿泊は全国では2019年より増えましたが、この12県では台湾がすべての県で、韓国が11県で2019年を下回っていました。

## 2024年は3都府県が2019年より59.5%多く、それ以外の44道県は12.0%多い

使うのは e-Stat「[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)」の都道府県別の文化・スポーツデータ（[`g_pref_culture`](/datasets/queria/e_stat/ssds/g_pref_culture)）です。もとは観光庁の[宿泊旅行統計調査](https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html)で、外国人の宿泊は次の6つが収録されています。この記事では延べ宿泊者数の5つを使います。

| コード  | 内容                       |
| ------- | -------------------------- |
| G7102   | 外国人延べ宿泊者数         |
| G710201 | 外国人延べ宿泊者数（韓国） |
| G710202 | 外国人延べ宿泊者数（中国） |
| G710203 | 外国人延べ宿泊者数（台湾） |
| G710204 | 外国人延べ宿泊者数（米国） |
| G710301 | 外国人実宿泊者数           |

ここでいう外国人は日本国内に住所を持たない人で、値は1月から12月までの暦年の合計です。[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/G)のとおり従業者10人以上の施設だけを集計しているので、観光庁が見出しに出す総数（従業者10人未満の施設を含む）より小さくなります。2024年の1億3,853万人泊は、観光庁の[2024年の確定値の報道発表資料](https://www.mlit.go.jp/kankocho/content/002026765.pdf)にある従業者10人以上の施設の国籍別の総数と一致します。この記事の2019年比は従業者10人以上の施設どうしで比較したもので、観光庁が公表する全施設の値の2019年比とは県ごとに違い、2019年を上回るか下回るかが入れ替わる県もあります。

外国人延べ宿泊者数（`G7102`）を、東京都・大阪府・京都府の合計と、それ以外の44道県の合計に分けて年ごとに並べます。2010年4〜6月期の調査から、施設の名簿の基になるデータベースと調査方法が変わったので、変更をまたがない2011年から描いています。

```chart
{
  "layer": [
    {
      "data": {"name": "big3_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"big3_man\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "big3_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "big3_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人延べ宿泊者数（万人泊）", "grid": true}
        },
        "color": {
          "datum": "東京都・大阪府・京都府",
          "type": "nominal",
          "scale": {"domain": ["東京都・大阪府・京都府", "それ以外の44道県"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "big3_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"other_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "other_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "other_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人延べ宿泊者数（万人泊）", "grid": true}
        },
        "color": {
          "datum": "それ以外の44道県",
          "type": "nominal",
          "scale": {"domain": ["東京都・大阪府・京都府", "それ以外の44道県"], "range": ["#ef4444", "#3b82f6"]},
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

2019年は3都府県が5,278万人泊、それ以外の44道県が4,853万人泊で、ほぼ半々でした。2024年は3都府県が8,419万人泊と2019年より59.5%多くなったのに対し、44道県は5,433万人泊で、2019年より12.0%多いだけです。全国に占める3都府県の割合は、2019年の52.1%から2023年は63.1%まで上がり、2024年は60.8%でした。

## 17県は2024年も2019年の人数を下回っている

都道府県ごとに、2024年の外国人延べ宿泊者数が2019年の何%にあたるかを並べます。100%を超えた30都道府県を緑、下回った17県を灰色で描いています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "recovery_above"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2024年の外国人延べ宿泊者数（2019年=100%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "2019年を上回った",
          "type": "nominal",
          "scale": {"domain": ["2019年を上回った", "2019年を下回った"], "range": ["#22c55e", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "recovery_below"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2024年の外国人延べ宿泊者数（2019年=100%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "2019年を下回った",
          "type": "nominal",
          "scale": {"domain": ["2019年を上回った", "2019年を下回った"], "range": ["#22c55e", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 100, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

最も伸びたのは石川県の192.3%で、福岡県（180.8%）、愛媛県（180.1%）、東京都（169.7%）が続きます。下回った17県のうち最も低いのは宮崎県の50.7%で、三重県（60.9%）、鳥取県（63.3%）、佐賀県（64.4%）と続きます。人数で最も減ったのは沖縄県で、2019年の542万人泊から2024年は438万人泊へ104万人泊少なくなりました。

## 17県のうち5県は中国からの減少、12県は中国以外からの減少で2019年を下回る

17県の2019年から2024年への増減を、中国からの宿泊（`G710202`）と、それ以外のすべての国・地域（`G7102` から `G710202` を引いた値）に分けて並べます。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "below_split"},
      "transform": [
        {"fold": ["china_man", "nonchina_man"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"china_man\": \"中国\", \"nonchina_man\": \"中国以外\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"china_man\",\"nonchina_man\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2019年から2024年への増減（万人泊）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["中国", "中国以外"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

```sql
SELECT area_name AS 都道府県, pct AS "2019年比（%）", total_man AS "増減（万人泊）", china_man AS "うち中国（万人泊）", nonchina_man AS "うち中国以外（万人泊）", nonchina_pct AS "中国以外の2019年比（%）" FROM below_split
```

愛知県・千葉県・静岡県・山梨県・奈良県の5県は、中国からの宿泊が減った分のほうが全体の減少より大きく、中国以外からの宿泊は2019年より増えています。愛知県は中国が84.4万人泊減った一方で中国以外が79.4万人泊増え、静岡県は中国以外が2019年の169.9%になりました。この5県は2019年の外国人延べ宿泊者数の40.0%〜70.6%が中国からで、全国の29.5%を上回っていました。全国の中国からの宿泊は2024年も2019年の84.4%にとどまっています。

残る12県は、中国以外の国・地域からの宿泊が2019年を下回っています。宮崎県は中国以外が2019年の50.1%、鳥取県は58.8%、鹿児島県は65.0%、佐賀県は68.7%です。全国では中国以外からの宿泊が2019年の158.6%に増えていて、12県はどれもこれを下回っています。12県のうち福井県は中国以外の減少が2019年の0.9%で、ほぼ横ばいです。島根県と富山県は、中国からの宿泊が2019年をわずかに上回っています。

12県の中国以外を、韓国・台湾・米国とそれ以外の国・地域に分けて、2019年比を並べます。

```sql
SELECT area_name AS 都道府県, nonchina_pct AS "中国以外（%）", korea_pct AS "韓国（%）", taiwan_pct AS "台湾（%）", usa_pct AS "米国（%）", other_pct AS "その他（%）", korea_share19 AS "2019年の韓国の割合（%）" FROM below12_nat
```

全国では台湾からの宿泊が2019年の136.6%、韓国からが185.2%に増えました。韓国からの宿泊は2019年に前年の1,195万人泊から972万人泊へ減っていたので、韓国の2019年比は低い年を基準にしています。12県では、台湾からの宿泊が12県すべてで2019年を下回り、韓国からの宿泊も滋賀県を除く11県で下回っています。12県のうち、2019年に韓国からの宿泊が全体の35%を超えていた佐賀県（37.7%）と宮崎県（35.4%）では、韓国からの宿泊が2019年の58.2%と59.4%です。一方、米国からの宿泊は12県のうち鳥取県と三重県を除く10県で2019年を上回っています。

国・地域別に分かるのは韓国・中国・台湾・米国の4つで、2024年の外国人延べ宿泊者数の54.9%にあたります。全国の推移は次のとおりです。

```chart
{
  "layer": [
    {
      "data": {"name": "nationality"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"china\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "china", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "china",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人延べ宿泊者数（万人泊）", "grid": true}
        },
        "color": {
          "datum": "中国",
          "type": "nominal",
          "scale": {
            "domain": ["中国", "台湾", "韓国", "米国"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "nationality"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"taiwan\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "taiwan", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "taiwan",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人延べ宿泊者数（万人泊）", "grid": true}
        },
        "color": {
          "datum": "台湾",
          "type": "nominal",
          "scale": {
            "domain": ["中国", "台湾", "韓国", "米国"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "nationality"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"korea\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "korea", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "korea",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人延べ宿泊者数（万人泊）", "grid": true}
        },
        "color": {
          "datum": "韓国",
          "type": "nominal",
          "scale": {
            "domain": ["中国", "台湾", "韓国", "米国"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "nationality"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"usa\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "usa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "usa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人延べ宿泊者数（万人泊）", "grid": true}
        },
        "color": {
          "datum": "米国",
          "type": "nominal",
          "scale": {
            "domain": ["中国", "台湾", "韓国", "米国"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"]
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

2019年は中国が2,985万人泊で最も多く、台湾（1,347万人泊）、韓国（972万人泊）、米国（728万人泊）の順でした。2024年は中国が2,519万人泊、台湾が1,841万人泊、韓国が1,800万人泊、米国が1,449万人泊で、4つのうち2019年を下回っているのは中国だけです。

## 観光の担当者がこのデータで確認できること

- 自分の県の2024年の外国人延べ宿泊者数が2019年の何%かを同じ従業者10人以上の施設の値で確認し、全国の136.7%や、3都府県を除いた44道県の合計の112.0%と比較する
- 自分の県の増減を、中国（`G710202`）とそれ以外に分け、中国以外が減っていれば韓国・台湾・米国（`G710201`・`G710203`・`G710204`）のどれが減ったかを確認する。全国で増えている台湾・韓国が自分の県で減っていれば、その国・地域からの宿泊が減った理由（航空路線、旅行会社の商品、受け入れ体制など）を確認する対象になる
- 中国以外の内訳は韓国・台湾・米国（`G710201`・`G710203`・`G710204`）の3つまでがこのテーブルで分かる。香港やタイなどは観光庁の都道府県別の集計表で確認する

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview) の都道府県別データ（`g_pref_culture`）を 2026-10-24 時点で集計しています。元データは観光庁の[宿泊旅行統計調査](https://www.mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html)で、収録は2009年から2024年までです。

Queria は、社会・人口統計体系などの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の文化・スポーツ統計テーブル](/datasets/queria/e_stat/ssds/g_pref_culture)から、自分の県の外国人宿泊が国・地域ごとに2019年の何%まで戻ったかを確認できます。

```sql id=pref_values
-- 外国人延べ宿泊者数（G7102）の都道府県別・年別の値。以下の view の土台
SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G7102' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2011 AND 2024
```

```sql id=big3_trend
SELECT year, ROUND(SUM(v) FILTER (WHERE area_name IN ('東京都', '大阪府', '京都府')) / 10000) AS big3_man, ROUND(SUM(v) FILTER (WHERE area_name NOT IN ('東京都', '大阪府', '京都府')) / 10000) AS other_man, ROUND(SUM(v) / 10000) AS total_man, ROUND(SUM(v) FILTER (WHERE area_name IN ('東京都', '大阪府', '京都府')) / SUM(v) * 100, 1) AS big3_share_pct, COUNT(*) AS prefs FROM pref_values GROUP BY year ORDER BY year
```

```sql id=summary
-- 本文の全国・3都府県・44道県の数字（プロットはしない）
WITH w AS (SELECT area_name, SUM(v) FILTER (WHERE year = 2019) AS y19, SUM(v) FILTER (WHERE year = 2024) AS y24 FROM pref_values GROUP BY area_name), b AS (SELECT *, area_name IN ('東京都', '大阪府', '京都府') AS big3 FROM w) SELECT ROUND(SUM(y19) / 10000) AS total19_man, ROUND(SUM(y24) / 10000) AS total24_man, ROUND(SUM(y24) / SUM(y19) * 100, 1) AS total_pct, ROUND(SUM(y24 - y19) / 10000) AS increase_man, ROUND(SUM(y24 - y19) FILTER (WHERE big3) / 10000) AS big3_increase_man, ROUND(SUM(y24 - y19) FILTER (WHERE big3) / SUM(y24 - y19) * 100, 1) AS big3_increase_share_pct, ROUND(SUM(y19) FILTER (WHERE big3) / 10000) AS big3_19_man, ROUND(SUM(y24) FILTER (WHERE big3) / 10000) AS big3_24_man, ROUND(SUM(y24) FILTER (WHERE big3) / SUM(y19) FILTER (WHERE big3) * 100, 1) AS big3_pct, ROUND(SUM(y19) FILTER (WHERE NOT big3) / 10000) AS other19_man, ROUND(SUM(y24) FILTER (WHERE NOT big3) / 10000) AS other24_man, ROUND(SUM(y24) FILTER (WHERE NOT big3) / SUM(y19) FILTER (WHERE NOT big3) * 100, 1) AS other_pct, COUNT(*) FILTER (WHERE y24 < y19) AS below_prefs, COUNT(*) FILTER (WHERE y24 >= y19) AS above_prefs FROM b
```

```sql id=recovery
WITH w AS (SELECT area_name, SUM(v) FILTER (WHERE year = 2019) AS y19, SUM(v) FILTER (WHERE year = 2024) AS y24 FROM pref_values GROUP BY area_name) SELECT area_name, ROUND(y24 / y19 * 100, 1) AS pct, ROUND(y19 / 10000) AS m19, ROUND(y24 / 10000) AS m24, ROUND((y24 - y19) / 10000) AS diff_man, ROW_NUMBER() OVER (ORDER BY y24 / y19 DESC, area_name) AS rn FROM w
```

```sql id=recovery_above
SELECT area_name, pct FROM recovery WHERE pct >= 100 ORDER BY rn
```

```sql id=recovery_below
SELECT area_name, pct FROM recovery WHERE pct < 100 ORDER BY rn
```

```sql id=nationality_pref
-- 国・地域別（G710201〜G710204）の都道府県別の2019年・2024年。全国行も含む
SELECT area_name, cat01, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2019) AS y19, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS y24 FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G7102', 'G710201', 'G710202', 'G710203', 'G710204') AND year IN (2019, 2024) GROUP BY area_name, cat01
```

```sql id=below_split
WITH s AS (SELECT area_name, MAX(y19) FILTER (WHERE cat01 = 'G7102') AS t19, MAX(y24) FILTER (WHERE cat01 = 'G7102') AS t24, MAX(y19) FILTER (WHERE cat01 = 'G710202') AS c19, MAX(y24) FILTER (WHERE cat01 = 'G710202') AS c24 FROM nationality_pref GROUP BY area_name) SELECT r.area_name, r.pct, ROUND((s.t24 - s.t19) / 10000, 1) AS total_man, ROUND((s.c24 - s.c19) / 10000, 1) AS china_man, ROUND(((s.t24 - s.c24) - (s.t19 - s.c19)) / 10000, 1) AS nonchina_man, ROUND((s.t24 - s.c24) / (s.t19 - s.c19) * 100, 1) AS nonchina_pct, ROUND(s.c19 / s.t19 * 100, 1) AS china_share19, (s.t24 - s.c24) > (s.t19 - s.c19) AS nonchina_grew FROM recovery r JOIN s USING (area_name) WHERE r.pct < 100 ORDER BY nonchina_grew DESC, r.rn
```

```sql id=below12_nat
WITH p AS (SELECT area_name, MAX(y19) FILTER (WHERE cat01 = 'G7102') AS t19, MAX(y24) FILTER (WHERE cat01 = 'G7102') AS t24, MAX(y19) FILTER (WHERE cat01 = 'G710202') AS c19, MAX(y24) FILTER (WHERE cat01 = 'G710202') AS c24, MAX(y19) FILTER (WHERE cat01 = 'G710201') AS k19, MAX(y24) FILTER (WHERE cat01 = 'G710201') AS k24, MAX(y19) FILTER (WHERE cat01 = 'G710203') AS w19, MAX(y24) FILTER (WHERE cat01 = 'G710203') AS w24, MAX(y19) FILTER (WHERE cat01 = 'G710204') AS u19, MAX(y24) FILTER (WHERE cat01 = 'G710204') AS u24 FROM nationality_pref GROUP BY area_name) SELECT b.area_name, b.nonchina_pct, ROUND(p.k24 / p.k19 * 100, 1) AS korea_pct, ROUND(p.w24 / p.w19 * 100, 1) AS taiwan_pct, ROUND(p.u24 / p.u19 * 100, 1) AS usa_pct, ROUND((p.t24 - p.c24 - p.k24 - p.w24 - p.u24) / (p.t19 - p.c19 - p.k19 - p.w19 - p.u19) * 100, 1) AS other_pct, ROUND(p.k19 / p.t19 * 100, 1) AS korea_share19, p.k24 < p.k19 AS korea_down, p.w24 < p.w19 AS taiwan_down, p.u24 > p.u19 AS usa_up FROM below_split b JOIN p USING (area_name) WHERE NOT b.nonchina_grew ORDER BY b.nonchina_pct
```

```sql id=below12_summary
-- 12県の国・地域別の件数と、全国の国・地域別の2019年比（プロットはしない）
SELECT COUNT(*) AS prefs, COUNT(*) FILTER (WHERE taiwan_down) AS taiwan_down, COUNT(*) FILTER (WHERE korea_down) AS korea_down, COUNT(*) FILTER (WHERE usa_up) AS usa_up, (SELECT ROUND(y24 / y19 * 100, 1) FROM nationality_pref WHERE area_name = '全国' AND cat01 = 'G710203') AS taiwan_pct_national, (SELECT ROUND(y24 / y19 * 100, 1) FROM nationality_pref WHERE area_name = '全国' AND cat01 = 'G710201') AS korea_pct_national FROM below12_nat
```

```sql id=below_detail
WITH s AS (SELECT area_name, MAX(y19) FILTER (WHERE cat01 = 'G7102') AS t19, MAX(y19) FILTER (WHERE cat01 = 'G710202') AS c19, MAX(y19) FILTER (WHERE cat01 = 'G710201') AS k19 FROM nationality_pref GROUP BY area_name) SELECT r.area_name, r.m19, r.m24, r.pct, ROUND(s.c19 / s.t19 * 100, 1) AS china_share, ROUND(s.k19 / s.t19 * 100, 1) AS korea_share FROM recovery r JOIN s USING (area_name) WHERE r.pct < 100 ORDER BY r.rn
```

```sql id=nationality_summary
-- 全国の国・地域別の2019年・2024年と、2019年の中国の割合（プロットはしない）。17県のうち中国の割合が全国を上回る県の数も数える
WITH n AS (SELECT cat01, y19, y24 FROM nationality_pref WHERE area_name = '全国'), t AS (SELECT y19 FROM n WHERE cat01 = 'G7102'), c AS (SELECT y19, y24 FROM n WHERE cat01 = 'G710202') SELECT ROUND(c.y19 / t.y19 * 100, 1) AS china_share_national, ROUND(c.y24 / c.y19 * 100, 1) AS china_pct, (SELECT ROUND(y24 / y19, 2) FROM n WHERE cat01 = 'G710201') AS korea_ratio, (SELECT COUNT(*) FROM below_detail WHERE china_share > c.y19 / t.y19 * 100) AS below_china_over, (SELECT COUNT(*) FROM below_detail WHERE china_share <= c.y19 / t.y19 * 100) AS below_china_under, (SELECT COUNT(*) FROM below_split WHERE nonchina_grew) AS below_nonchina_grew, (SELECT ROUND((MAX(y24) FILTER (WHERE cat01 = 'G7102') - MAX(y24) FILTER (WHERE cat01 = 'G710202')) / (MAX(y19) FILTER (WHERE cat01 = 'G7102') - MAX(y19) FILTER (WHERE cat01 = 'G710202')) * 100, 1) FROM n) AS nonchina_pct_national, (SELECT ROUND(SUM(y24) FILTER (WHERE cat01 != 'G7102') / SUM(y24) FILTER (WHERE cat01 = 'G7102') * 100, 1) FROM n) AS four_cover24 FROM t, c
```

```sql id=nationality
SELECT year, ROUND(SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G710201') / 10000) AS korea, ROUND(SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G710202') / 10000) AS china, ROUND(SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G710203') / 10000) AS taiwan, ROUND(SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G710204') / 10000) AS usa FROM e_stat.ssds.g_pref_culture WHERE area_name = '全国' AND cat01 IN ('G710201', 'G710202', 'G710203', 'G710204') AND year BETWEEN 2011 AND 2024 GROUP BY year ORDER BY year
```
