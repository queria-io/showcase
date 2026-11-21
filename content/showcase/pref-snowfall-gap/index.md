---
title: 気温は47都道府県すべてで上がったが、雪の多い10道県では雪日数が減っていない
description: e-Stat「社会・人口統計体系」の気象データを1975〜2018年で集計しました。年平均気温は47都道府県すべてで上がり、1975〜1984年の平均で年60日以上雪が降っていた10道県の雪日数は86.0日から87.4日へ増えました。年30日未満だった28都府県では15.4日から12.7日へ約17%減っています。
publishedAt: 2026-04-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 気象
  - 積雪
  - 冬季気候
  - 都道府県格差
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義 B 自然環境
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/B
    publisher: 総務省統計局
agentHint: e_stat.ssds.b_pref_land の雪日数（B4107）を私の県について1975年から2018年まで出して、1975〜1984年の平均と2009〜2018年の平均を比べて。同じ期間の年平均気温（B4101）の差も並べて
socialAnnounce: |-
  都道府県別の雪日数を1975〜2018年で集計しました。

  年平均気温は47都道府県すべてで上がっているのに、1975〜1984年の平均で年60日以上降っていた10道県の雪日数は86.0日から87.4日へむしろ増えました。減ったのは同じ期間に年30日未満だった28都府県で、15.4日から12.7日へ約17%です
---

1975〜1984年と2009〜2018年の10年平均を比較すると、年平均気温は47都道府県すべてで上がり、上げ幅は平均1.16℃でした。1975〜1984年の平均で年60日以上雪が降っていた10道県では、雪日数の平均は86.0日から87.4日へ増えています。雪日数が減ったのは、年30日未満だった28都府県で、15.4日から12.7日へ約17%減りました。

除雪の体制や委託の規模、冬季の輸送計画は、温暖化で雪が減ることを前提に見直されることがあります。都道府県別の観測値では、この前提が当てはまるのは雪がもともと少ない地域です。この記事では、[e-Stat「社会・人口統計体系」](https://www.stat.go.jp/data/ssds/index.html)の都道府県別気象データを使い、雪日数の水準と44年の変化を確認しました。

## 2018年の雪日数は、北海道の131日から沖縄県の0日まで差がある

このデータは e-Stat「社会・人口統計体系」の都道府県別自然環境データ（`b_pref_land`）から取得しています。気象関連の指標と、それぞれの収録年は次のとおりです。

```sql
SELECT cat01 AS コード, replace(item_name, cat01 || '_', '') AS 内容, min_year AS 収録開始, max_year AS 収録終了, year_count AS 年数 FROM e_stat.ssds.series_coverage WHERE table_name = 'b_pref_land' AND cat01 LIKE 'B41%' ORDER BY cat01
```

指標によって収録が終わる年が異なり、雪日数（`B4107`）は2020年まで、最深積雪（`B4110`）は2007年まで、気温は2024年までです。この記事の集計期間は、この収録年に合わせています。

年間雪日数（`B4107`）で47都道府県を比較しました。雪日数は、量にかかわらず雪・しゅう雪・ふぶき・みぞれ・霧雪・細氷のいずれかが観測された日を、前年8月から当年7月まで集計した日数です（[項目定義 B 自然環境](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)）。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "snow_days_top10"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "snow_days", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "雪日数（日）", "grid": true}
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
      "data": {"name": "snow_days_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "snow_days", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "雪日数（日）", "grid": true}
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
      "data": {"name": "snow_days_bottom10"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "snow_days", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "雪日数（日）", "grid": true}
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

2018年の雪日数は北海道の131日が最も多く、青森県117日、岩手県106日、秋田県101日と続きます。下位は沖縄県0日、宮崎県と静岡県が2日、高知県3日で、東京都は11日でした。上位と下位の差は100日を超えます。

この値は都道府県庁所在地にある気象台1地点の観測値です（埼玉県は熊谷市、千葉県は銚子市、東京都は千代田区、滋賀県は彦根市、山口県は下関市）。県内全域の平均ではないので、山間部の雪の状況はこの数字には表れません。

比較の年に2018年を使っているのは、雪日数が2019年2月と2020年2月に目視観測の自動化で観測方法を変えており、前後を単純に比較できないためです（[項目定義 B 自然環境](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)）。上の表のとおり、収録も2020年で終わっています。雪日数の集計はこの記事を通して1975年から2018年までを対象にします。

## 年60日以上雪が降っていた10道県は、雪日数が1.4日増えた

44年の最初の10年と最後の10年を取り、1975〜1984年の平均と2009〜2018年の平均を県ごとに比較しました。単年ではなく10年平均で見るのは、雪日数の年変動が大きいためです。青森県は44年のうち最少81日・最多125日、秋田県は最少66日・最多120日で、単年の値は40日以上変わります。

年平均気温（`B4101`）は、同じ期間で47都道府県すべてが上がっています。

```sql
SELECT * FROM temp_change
```

上げ幅は0.73℃から1.59℃、平均で1.16℃です。下がった県はありません。

雪日数は、下の図のように基準期の水準によって増えた県と減った県に分かれます。横軸が1975〜1984年の平均雪日数、縦軸がそこから2009〜2018年の平均までの変化日数です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "snow_change"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "early", "type": "quantitative"},
          {"field": "diff", "type": "quantitative"}
        ],
        "x": {
          "field": "early",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1975〜1984年の平均雪日数（日）", "grid": true}
        },
        "y": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2009〜2018年までの変化（日）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 0, "type": "quantitative"}
      }
    }
  ]
}
```

破線より下が減った県、上が増えた県です。左側（もともと雪が少ない県）はほぼすべてが破線の下にあり、右側（雪が多い県）は破線の上下に分かれています。

1975〜1984年の平均雪日数で県を3つのグループに分けて集計しました。グループの名前はこの基準期の水準で、2018年単年の値ではありません。

```sql
SELECT * FROM snow_change_groups
```

基準期に年60日以上だった10道県は86.0日から87.4日へ1.4日増えており、減ったのは岩手県と富山県の2県だけです。基準期に年30日未満だった28都府県は15.4日から12.7日へ2.7日、率にして約17%減り、28のうち26で減っています。年平均気温の上がり方は、3つのグループでほとんど変わりません（1.02℃〜1.16℃）。

県単位で見ると、増加が最も大きいのは秋田県の5.5日増（95.8日→101.3日）、次いで青森県の3.9日増（106.1日→110.0日）です。減少が最も大きいのは滋賀県の7.4日減（42.0日→34.6日）、次いで愛知県の6.2日減（20.7日→14.5日）でした。

気温の上がり方が同じでも雪日数の反応が分かれるのは、雪の多い地域では冬季の気温がもともと十分に低く、1℃程度の上昇では降水が雪のまま降るためと考えられます。雨と雪の境目に近い地域ほど、同じ気温上昇で雪日数が大きく減ると考えられます。

この集計では、44年のうち1年だけ値が欠ける千葉県・山口県・岡山県を除き、毎年同じ44都道府県で平均しています。

## 青森県と秋田県の雪日数は、44年間で減る傾向がない

雪の多い青森県・秋田県・富山県と、少ない東京都・高知県の推移を並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "snow_days_aomori"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"snow_days\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "snow_days", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "color": {
          "datum": "青森県",
          "type": "nominal",
          "scale": {
            "domain": ["青森県", "秋田県", "富山県", "東京都", "高知県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "snow_days_akita"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"snow_days\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "snow_days", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "color": {
          "datum": "秋田県",
          "type": "nominal",
          "scale": {
            "domain": ["青森県", "秋田県", "富山県", "東京都", "高知県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "snow_days_toyama"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"snow_days\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "snow_days", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "color": {
          "datum": "富山県",
          "type": "nominal",
          "scale": {
            "domain": ["青森県", "秋田県", "富山県", "東京都", "高知県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "snow_days_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"snow_days\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "snow_days", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["青森県", "秋田県", "富山県", "東京都", "高知県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "snow_days_kochi"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"snow_days\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 9}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "snow_days", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "color": {
          "datum": "高知県",
          "type": "nominal",
          "scale": {
            "domain": ["青森県", "秋田県", "富山県", "東京都", "高知県"],
            "range": ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6"]
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

青森県と秋田県は後半に向かって減っておらず、富山県の減少も基準期比で1.3日です。最少年と最多年の差は青森県で44日、秋田県で54日、富山県で52日あるので、2〜3年の実績から増減の傾向を判断すると、逆の向きに判断することがあります。

東京都は44年のうち24年が一桁で、最も多い年でも27日でした。高知県は1日から14日です。雪の少ない県では、年ごとの差が、除雪の出動があるかないかの差になります。

## 雪日数と最深積雪の相関は0.884で、同じ雪日数でも積雪の深さには差がある

雪が多く降る地域は積雪も深くなりますが、雪日数と積雪の深さは別の指標です。最深積雪（`B4110`、単位はcm）は寒候期に観測された積雪の深さの最大値です。収録は2007年までなので、ここでは最終年の2007年で雪日数との関係を確認します。

```chart
{
  "layer": [
    {
      "data": {"name": "max_snow_depth"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "snow_days", "type": "quantitative"},
          {"field": "snow_depth", "type": "quantitative"}
        ],
        "x": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "y": {
          "field": "snow_depth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "最深積雪（cm）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "max_snow_depth"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "snow_days",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "雪日数（日）", "grid": true}
        },
        "y": {
          "field": "snow_depth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "最深積雪（cm）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

2007年の47都道府県で、雪日数と最深積雪の相関係数は0.884でした。おおむね比例しますが、同じ雪日数でも最深積雪には差があります。観測地点は県庁所在地の1地点なので、市街地が海沿いにある県と盆地にある県では、雪の積もり方の条件が異なります。

積雪荷重や融雪設備の能力は深さで決まり、除雪の出動回数や交通の乱れは日数で決まります。冬季のコストを見積もるときは、両方の指標を確認する必要があります。最深積雪は2007年で収録が終わるので、前節までの長期変化は雪日数についての結果です。

## 最低気温が最も低いのは北海道の-5.1℃

最低気温（`B4103`）は2024年まで収録されているので、最新年で集計しました。この値は日最低気温の月平均の最低値で、最も寒い月の平均です。年間で最も冷え込んだ日の気温とは異なります。水道管の凍結対策や凍結深度の目安として使われます。

```chart
{
  "layer": [
    {
      "data": {"name": "min_temp_ranking"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "min_temp", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "min_temp",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "最低気温（℃）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

2024年に0℃を下回ったのは10道県で、最も低いのは北海道の-5.1℃、次いで長野県-3.3℃、岩手県-2.9℃、青森県-1.5℃、山形県-1.3℃でした。2018年の雪日数が6日の山梨県、17日の栃木県、10日の茨城県が上位に入り、雪日数が59日の石川県や60日の福井県はこの15道県に入りません。日本海側は雪が多くても月平均の最低気温はそれほど下がらないためで、凍結のリスクが高い地域と雪が多い地域は一致しません。

## 業務でどう使うか

自治体の道路維持担当が、除雪委託の仕様と積算を見直す場面を想定します。

- 仕様書の想定出動日数は、単年の実績ではなく直近10年の平均で書く。豪雪地帯では最少年と最多年の差が44日から54日あり、直近1年の実績を使うと年によって半分になる
- 雪が減ることを根拠に想定日数を下げる改定は、豪雪地帯では観測値と合わない。この前提が当てはまるのは、もともと雪が少ない地域だけ
- 雪の少ない地域では、40年前の実績にもとづく積算が現在の水準より多くなる。見直し幅の目安は基準期比で約17%

観測は県庁所在地の1地点なので、この数字は市街地の目安です。山間部の路線がある自治体は、この数字と自治体の出動記録を比較してください。凍結対策が必要かどうかは雪日数では判断できません。最低気温が低い15道県と雪日数の多い県は一致しないためです。

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)に収録された都道府県別の自然環境データを、2026年8月18日時点で集計しています。使ったのは雪日数（`B4107`）、年平均気温（`B4101`）、最深積雪（`B4110`）、最低気温（`B4103`）の4指標で、原資料は気象庁の観測値です。指標の定義と観測地点は[項目定義 B 自然環境](https://www.e-stat.go.jp/koumoku/koumoku_teigi/B)に記載されています。

Queriaは、社会・人口統計体系の列名・単位・年の表記を統一し、カテゴリコードの説明をつけて公開しています。本記事で使った[都道府県別の自然環境テーブル](/datasets/queria/e_stat/ssds/b_pref_land)から、自分の県の雪日数を1975年から並べたり、近隣県と比較したりできます。

```sql id=snow_days_top10
WITH ranked AS (SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND year = 2018 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, snow_days FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=snow_days_mid
WITH ranked AS (SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND year = 2018 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, snow_days FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=snow_days_bottom10
WITH ranked AS (SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days, ROW_NUMBER() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC, area_name) AS rn FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND year = 2018 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, snow_days FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=snow_change
WITH v AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS d FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018), panel AS (SELECT area_name FROM v GROUP BY area_name HAVING count(*) = 44) SELECT area_name, ROUND(AVG(CASE WHEN year <= 1984 THEN d END), 1) AS early, ROUND(AVG(CASE WHEN year >= 2009 THEN d END), 1) AS late, ROUND(AVG(CASE WHEN year >= 2009 THEN d END) - AVG(CASE WHEN year <= 1984 THEN d END), 1) AS diff FROM v JOIN panel USING (area_name) GROUP BY area_name ORDER BY early DESC
```

```sql id=temp_change
WITH t AS (SELECT area_name, ROUND(AVG(CASE WHEN year >= 2009 THEN TRY_CAST(value AS DOUBLE) END) - AVG(CASE WHEN year <= 1984 THEN TRY_CAST(value AS DOUBLE) END), 2) AS diff FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4101' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018 GROUP BY area_name) SELECT count(*) AS 都道府県数, sum(CASE WHEN diff > 0 THEN 1 ELSE 0 END) AS 上がった県数, ROUND(min(diff), 2) AS 最小の上げ幅, ROUND(max(diff), 2) AS 最大の上げ幅, ROUND(avg(diff), 2) AS 平均の上げ幅 FROM t
```

```sql id=snow_change_groups
WITH s AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS d FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018), panel AS (SELECT area_name FROM s GROUP BY area_name HAVING count(*) = 44), sa AS (SELECT area_name, AVG(CASE WHEN year <= 1984 THEN d END) AS e, AVG(CASE WHEN year >= 2009 THEN d END) AS l FROM s JOIN panel USING (area_name) GROUP BY area_name), t AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS d FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4101' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018), ta AS (SELECT area_name, AVG(CASE WHEN year <= 1984 THEN d END) AS e, AVG(CASE WHEN year >= 2009 THEN d END) AS l FROM t GROUP BY area_name) SELECT CASE WHEN sa.e >= 60 THEN '年60日以上' WHEN sa.e >= 30 THEN '年30〜60日' ELSE '年30日未満' END AS グループ, count(*) AS 県数, ROUND(AVG(sa.e), 1) AS 雪日数_1975_84, ROUND(AVG(sa.l), 1) AS 雪日数_2009_18, ROUND(AVG(sa.l - sa.e), 1) AS 雪日数の差, ROUND(AVG(ta.l - ta.e), 2) AS 年平均気温の差 FROM sa JOIN ta USING (area_name) GROUP BY 1 ORDER BY 3 DESC
```

```sql id=snow_days_akita
SELECT year, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name = '秋田県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018 ORDER BY year
```

```sql id=snow_days_toyama
SELECT year, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name = '富山県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018 ORDER BY year
```

```sql id=snow_days_aomori
SELECT year, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name = '青森県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018 ORDER BY year
```

```sql id=snow_days_tokyo
SELECT year, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name = '東京都' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018 ORDER BY year
```

```sql id=snow_days_kochi
SELECT year, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND area_name = '高知県' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2018 ORDER BY year
```

```sql id=max_snow_depth
WITH snow AS (SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_depth FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4110' AND year = 2007 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), days AS (SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 0) AS snow_days FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4107' AND year = 2007 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT s.area_name, s.snow_depth, d.snow_days FROM snow s JOIN days d ON s.area_name = d.area_name ORDER BY s.snow_depth DESC
```

```sql id=min_temp_ranking
SELECT area_name, ROUND(TRY_CAST(value AS DOUBLE), 1) AS min_temp FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B4103' AND year = 2024 AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ORDER BY min_temp ASC LIMIT 15
```
