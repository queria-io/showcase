---
title: 持ち家の割合は45年で60.5%から63.5%に上がり、下がったのは社宅と公的賃貸だった
description: 住宅・土地統計調査の1978年から2023年までの10回分で、所有関係が判明した住宅に占める持ち家の割合は60.5%から63.5%へ上がっています。同じ45年で給与住宅は5.7%から2.4%、公営・UR・公社の借家は7.6%から4.6%へ下がり、給与住宅は47都道府県すべてで下がりました。
ogDescription: 住宅・土地統計調査の1978年から2023年までの10回分で、所有関係が判明した住宅に占める持ち家の割合は60.5%から63.5%へ上がっています。同じ45年で給与住宅は5.7%から2.4%、公営・UR・公社の借家は7.6%から4.6%へ下がりました。
publishedAt: 2026-05-31
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 住宅
  - 賃貸
  - 不動産
datasets:
  - queria/e_stat
sources:
  - title: 令和5年住宅・土地統計調査 調査の結果
    url: https://www.stat.go.jp/data/jyutaku/2023/tyousake.html
    publisher: 総務省統計局
  - title: 令和5年住宅・土地統計調査 推定値の大きさ別標準誤差率
    url: https://www.stat.go.jp/data/jyutaku/2023/zuhyou/sui_01_chiiki.xlsx
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics
    publisher: 総務省統計局
  - title: 項目定義 H 居住
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/H
    publisher: 総務省統計局
agentHint: 市区町村別の住宅テーブル（h_municipal_housing）で、給与住宅数（H1323）と公営・UR・公社の借家数（H1321）が2003年から2023年にどれだけ減ったかを自分の県の市区町村ごとに出して。民営借家数（H1322）の増加と並べて比べたい
socialAnnounce: |-
  住宅・土地統計調査45年分を数え直しました。所有関係が判明した住宅では持ち家の割合が1978年60.5%→2023年63.5%。減ったのは給与住宅と公的賃貸の割合です。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

住宅・土地統計調査の1978年から2023年までの10回分を集計すると、所有関係が判明した住宅に占める持ち家の割合は60.5%から63.5%へ3.0ポイント上がっていました。同じ45年で、社宅や公務員住宅を含む給与住宅の割合は5.7%から2.4%へ、公営・UR・公社の借家の割合は7.6%から4.6%へ下がっています。民営借家の割合は26.2%から29.4%に上がりました。

賃貸住宅が増えた理由として、持ち家を買わない世帯が増えたという説明がよく使われます。全国の数字では、民営借家の割合は持ち家からではなく、給与住宅と公的賃貸の分を取って上がっています。

## 所有関係が不詳の住宅を分母から除くと、持ち家率は3.0ポイント上がっている

住宅の所有関係は、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics)の都道府県別住宅データ（`h_pref_housing`）に次のコードで収録されています。[項目定義 H 居住](https://www.e-stat.go.jp/koumoku/koumoku_teigi/H)によると、いずれも10月1日時点の戸数です。

| コード | 内容                   | 定義                                                                                       |
| ------ | ---------------------- | ------------------------------------------------------------------------------------------ |
| H1310  | 持ち家数               | 居住している世帯が全部または一部を所有している住宅                                         |
| H1320  | 借家数                 | 下の3区分の合計                                                                            |
| H1321  | 公営・UR・公社の借家数 | 都道府県・市区町村・UR・住宅供給公社が所有または管理する賃貸住宅のうち、給与住宅でないもの |
| H1322  | 民営借家数             | 国・都道府県・市区町村・UR・公社以外が所有または管理する賃貸住宅のうち、給与住宅でないもの |
| H1323  | 給与住宅数             | 社宅・公務員住宅など、勤め先が職務の都合や給与の一部として住まわせる住宅                   |
| H1101  | 居住世帯あり住宅数     | 持ち家数と借家数の合計に、所有関係が不詳の住宅を加えたもの                                 |

本文の持ち家率・民営借家率などの比率は、持ち家数（`H1310`）と借家数（`H1320`）の合計を分母にしています。所有関係が不詳の住宅は、45年で0.22%から4.18%に増えています。居住世帯あり住宅数（`H1101`）を分母にすると、不詳が増えた分だけすべての区分の割合が下がるので、分母から除きました。この割合は、不詳の住宅も判明した住宅と同じ構成を持つと仮定した値です。

```sql
SELECT year AS 調査年, unknown_pct AS '所有関係が不詳の割合（%）', own_rate_stock AS '持ち家率・不詳を分母に含む（%）', own_rate AS '持ち家率・判明分のみ（%）' FROM national_tenure
```

不詳を分母に含めた持ち家率は、1978年が60.4%、2023年が60.9%で、45年間ほとんど変わっていないように見えます。判明分だけで集計すると60.5%から63.5%になり、3.0ポイント上がっています。持ち家率が横ばいに見えるのは、不詳の住宅が増えたためです。

## 給与住宅は5.7%から2.4%に、公営・UR・公社の借家は7.6%から4.6%に下がった

持ち家以外の住宅は借家で、借家は3区分に分かれます。4区分の割合を10回分並べました。

```chart
{
  "height": 320,
  "layer": [
    {
      "data": {"name": "national_tenure"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"private_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ea580c",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "private_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "values": [1978, 1988, 1998, 2008, 2018, 2023]}
        },
        "y": {
          "field": "private_rate",
          "type": "quantitative",
          "scale": {"domain": [0, 40], "zero": false, "nice": false},
          "axis": {"title": "所有関係が判明した住宅に占める割合（%）"}
        },
        "color": {
          "datum": "民営借家",
          "type": "nominal",
          "scale": {
            "domain": ["民営借家", "公営・UR・公社の借家", "給与住宅"],
            "range": ["#ea580c", "#16a34a", "#9333ea"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national_tenure"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"public_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#16a34a",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "public_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "values": [1978, 1988, 1998, 2008, 2018, 2023]}
        },
        "y": {
          "field": "public_rate",
          "type": "quantitative",
          "scale": {"domain": [0, 40], "zero": false, "nice": false},
          "axis": {"title": "所有関係が判明した住宅に占める割合（%）"}
        },
        "color": {
          "datum": "公営・UR・公社の借家",
          "type": "nominal",
          "scale": {
            "domain": ["民営借家", "公営・UR・公社の借家", "給与住宅"],
            "range": ["#ea580c", "#16a34a", "#9333ea"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national_tenure"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"company_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#9333ea",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "company_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "values": [1978, 1988, 1998, 2008, 2018, 2023]}
        },
        "y": {
          "field": "company_rate",
          "type": "quantitative",
          "scale": {"domain": [0, 40], "zero": false, "nice": false},
          "axis": {"title": "所有関係が判明した住宅に占める割合（%）"}
        },
        "color": {
          "datum": "給与住宅",
          "type": "nominal",
          "scale": {
            "domain": ["民営借家", "公営・UR・公社の借家", "給与住宅"],
            "range": ["#ea580c", "#16a34a", "#9333ea"]
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

給与住宅は5.7%から2.4%へ3.3ポイント、公営・UR・公社の借家は7.6%から4.6%へ3.0ポイント下がりました。上がったのは、民営借家の3.2ポイント（26.2%から29.4%）と持ち家の3.0ポイントです。持ち家率は1983年の62.6%から1993年の60.8%まで一度下がってから上がり、民営借家率は2018年の29.5%が最も高い値です。公営・UR・公社の借家の割合は1983年が最も高く、それ以降は毎回前回を下回っています。

戸数で見ると、45年で減ったのは給与住宅だけです。

```sql
SELECT year AS 調査年, stock_units AS '居住世帯あり住宅数（戸）', own_units AS '持ち家数（戸）', private_units AS '民営借家数（戸）', public_units AS '公営・UR・公社の借家数（戸）', company_units AS '給与住宅数（戸）' FROM national_tenure
```

給与住宅は1,838,800戸から1,302,100戸へ29.2%減りました。最も少なかったのは2018年の1,099,900戸で、2023年はそこから18.4%増えています。公営・UR・公社の借家は2003年の3,118,600戸が最も多く、2023年の2,476,200戸はそこから20.6%少なくなっています。2023年の戸数は1978年の2,442,000戸をわずかに上回っており、45年で比較するとほぼ同じです。所有関係が判明した住宅が1.66倍になった間に、給与住宅は減り、公的賃貸はほとんど増えなかったので、両者の割合が下がりました。

民営借家は8,408,300戸から15,683,500戸へ1.87倍になりました。民営借家の割合が3.2ポイント上がった分は、持ち家ではなく、勤め先が用意する住宅と、自治体・URが用意する住宅の割合が下がった分にあたります。

## 持ち家率は20都道府県で上がり、27県で下がった

1978年から2023年への持ち家率の変化を、47都道府県について算出しました。

```chart
{
  "height": 880,
  "layer": [
    {
      "data": {"name": "pref_change_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1978年から2023年への持ち家率の変化（ポイント）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "datum": "下がった県",
          "type": "nominal",
          "scale": {"domain": ["下がった県", "上がった都道府県"], "range": ["#dc2626", "#2563eb"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_change_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1978年から2023年への持ち家率の変化（ポイント）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "datum": "上がった都道府県",
          "type": "nominal",
          "scale": {"domain": ["下がった県", "上がった都道府県"], "range": ["#dc2626", "#2563eb"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

持ち家率が上がったのは20都道府県、下がったのは27県です。全国の3.0ポイントの上昇は、都道府県に共通する動きではありません。最も上がったのは大阪府で44.2%から57.1%へ、最も下がったのは沖縄県で63.4%から45.7%へ変わっています。

住宅・土地統計調査は標本調査なので、都道府県の値は推計値です。標準誤差は推定値が小さい県ほど大きく、2023年調査の[推定値の大きさ別標準誤差率](https://www.stat.go.jp/data/jyutaku/2023/zuhyou/sui_01_chiiki.xlsx)（都道府県・甲乙両調査票）を次の表の戸数に当てはめると、県ごとの誤差を確認できます。図の1ポイント前後の変化は、県によっては誤差の範囲に入ります。5ポイント以上変わった17都道府県と、次に示す増減の向きの一致は、誤差の影響を受けません。2013年と2018年の調査は、福島第一原発事故の避難地域を抽出の対象から除いています。

47都道府県の持ち家率と、所有関係4区分の45年間の変化は次のとおりです。

```sql
SELECT * FROM pref_tenure_change
```

4区分ごとに、割合が上がった都道府県と下がった都道府県の数を集計しました。

```sql
SELECT * FROM direction_counts
```

給与住宅の割合は47都道府県すべてで下がり、低下幅の中央値は2.3ポイントです。公営・UR・公社の借家は44都道府県で下がりました。上がったのは沖縄県・高知県と島根県の3県で、島根県の増加は47都道府県の表で 0 と表示されるほど小さく、上がったとは判断できない大きさです。民営借家は41都道府県で上がり、下がったのは東京都・神奈川県・大阪府・兵庫県・奈良県・和歌山県の6都府県です。この6都府県はいずれも持ち家率が上がっており、持ち家率の上昇幅が大きい上位7つのうち6つを占めます（残る1つは北海道です）。

47都道府県すべてで給与住宅の割合が下がっているので、この低下は県ごとの抽出のばらつきでは説明できません。給与住宅と公的賃貸の割合が下がった分をどの区分が占めたかは、地域によって異なります。民営借家の割合が下がった関東・関西の6都府県では、持ち家の割合が上がりました。残る41都道府県では民営借家の割合が上がっていますが、そのうち8道府県は持ち家の上昇幅のほうが大きく、北海道は持ち家が8.4ポイント、民営借家が4.3ポイント上がっています。

## 持ち家率の都道府県の差は、44.2ポイントから33.0ポイントに縮んだ

持ち家率の最も高い都道府県と最も低い都道府県の差の推移です。

```sql
SELECT * FROM spread_by_year
```

1978年は最も高い富山県の85.0%と最も低い東京都の40.8%で、44.2ポイントの差がありました。2023年は秋田県の78.7%と沖縄県の45.7%で、33.0ポイントです。差が最も小さかったのは2018年の30.9ポイントで、2023年はそこから2.1ポイント広がっています。最も低い都道府県が東京都から沖縄県に変わったのも2018年からです。

## 沖縄県の持ち家率は17.7ポイント下がったが、持ち家の戸数は1.53倍に増えた

持ち家率が下がった27県のうち、沖縄県の低下幅が最も大きくなっています。沖縄県の戸数を並べました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "okinawa_units"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"stock_units\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "stock_units", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "values": [1978, 1988, 1998, 2008, 2018, 2023]}
        },
        "y": {
          "field": "stock_units",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "戸数"}
        },
        "color": {
          "datum": "居住世帯あり住宅数",
          "type": "nominal",
          "scale": {
            "domain": ["居住世帯あり住宅数", "持ち家", "民営借家"],
            "range": ["#64748b", "#2563eb", "#ea580c"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "okinawa_units"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"own_units\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "own_units", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "values": [1978, 1988, 1998, 2008, 2018, 2023]}
        },
        "y": {
          "field": "own_units",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "戸数"}
        },
        "color": {
          "datum": "持ち家",
          "type": "nominal",
          "scale": {
            "domain": ["居住世帯あり住宅数", "持ち家", "民営借家"],
            "range": ["#64748b", "#2563eb", "#ea580c"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "okinawa_units"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"private_units\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ea580c",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "private_units", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "values": [1978, 1988, 1998, 2008, 2018, 2023]}
        },
        "y": {
          "field": "private_units",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "戸数"}
        },
        "color": {
          "datum": "民営借家",
          "type": "nominal",
          "scale": {
            "domain": ["居住世帯あり住宅数", "持ち家", "民営借家"],
            "range": ["#64748b", "#2563eb", "#ea580c"]
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

沖縄県の持ち家は175,000戸から267,100戸へ1.53倍に増えています。同じ45年で民営借家が83,100戸から278,600戸へ3.35倍になり、居住世帯あり住宅数は2.27倍になりました。増えた住宅の半分以上が民営借家だったので、持ち家率が下がりました。持ち家の戸数は2013年の258,100戸から2018年の255,900戸へ一度減り、2023年に増えています。

## まとめ

- 全国の持ち家率は1978年の60.5%から2023年の63.5%へ3.0ポイント上がっています。横ばいに見えるのは、所有関係が不詳の住宅が0.22%から4.18%に増え、それを分母に含めているためです
- 45年で割合が下がったのは給与住宅（5.7%から2.4%）と公営・UR・公社の借家（7.6%から4.6%）で、上がったのは民営借家（26.2%から29.4%）と持ち家（60.5%から63.5%）です
- 給与住宅の割合は47都道府県すべてで、公営・UR・公社の借家は44都道府県で下がっています。関東・関西の6都府県では民営借家の割合も下がり、持ち家の割合が上がりました
- 持ち家率は20都道府県で上がり、27県で下がっています。都道府県の差は1978年の44.2ポイントから2023年の33.0ポイントに縮んでいます
- 沖縄県は持ち家率が17.7ポイント下がって全国で最も低くなりましたが、持ち家の戸数は1.53倍に増えています。民営借家が3.35倍に増えたことで、持ち家率が下がりました

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics)の都道府県別住宅データ（`h_pref_housing`）を 2026-09-12 時点で取得して集計しています。元データは総務省統計局の住宅・土地統計調査で、1978年から2023年までの5年ごと10回分、各回10月1日時点の値です。1998年より前の4回は住宅統計調査の名称で実施されています。最新回は[令和5年調査](https://www.stat.go.jp/data/jyutaku/2023/tyousake.html)で、標本誤差の判定にはその[推定値の大きさ別標準誤差率](https://www.stat.go.jp/data/jyutaku/2023/zuhyou/sui_01_chiiki.xlsx)の都道府県・甲乙両調査票の表を使いました。

Queriaは、住宅・土地統計調査などの行政のオープンデータを、列名・単位・地域コードの体系を統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[都道府県別の住宅テーブル](/datasets/queria/e_stat/ssds/h_pref_housing)から、自社の商圏に入る地域の所有関係を確認できます。

```sql id=national_tenure
WITH d AS (SELECT DISTINCT year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name = '全国' AND cat01 IN ('H1101', 'H1310', 'H1320', 'H1321', 'H1322', 'H1323') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), b AS (SELECT year, MAX(v) FILTER (WHERE cat01 = 'H1101') AS stock, MAX(v) FILTER (WHERE cat01 = 'H1310') + MAX(v) FILTER (WHERE cat01 = 'H1320') AS base, MAX(v) FILTER (WHERE cat01 = 'H1310') AS own, MAX(v) FILTER (WHERE cat01 = 'H1321') AS pub, MAX(v) FILTER (WHERE cat01 = 'H1322') AS priv, MAX(v) FILTER (WHERE cat01 = 'H1323') AS corp FROM d GROUP BY year) SELECT year, ROUND(own / base * 100, 1) AS own_rate, ROUND(priv / base * 100, 1) AS private_rate, ROUND(pub / base * 100, 1) AS public_rate, ROUND(corp / base * 100, 1) AS company_rate, ROUND(own / stock * 100, 1) AS own_rate_stock, ROUND((stock - base) / stock * 100, 2) AS unknown_pct, CAST(stock AS BIGINT) AS stock_units, CAST(own AS BIGINT) AS own_units, CAST(priv AS BIGINT) AS private_units, CAST(pub AS BIGINT) AS public_units, CAST(corp AS BIGINT) AS company_units FROM b ORDER BY year
```

```sql id=pref_change_down
WITH d AS (SELECT DISTINCT area_name, year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND year IN (1978, 2023) AND cat01 IN ('H1310', 'H1320') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT area_name, year, MAX(v) FILTER (WHERE cat01 = 'H1310') / (MAX(v) FILTER (WHERE cat01 = 'H1310') + MAX(v) FILTER (WHERE cat01 = 'H1320')) * 100 AS o FROM d GROUP BY area_name, year), c AS (SELECT area_name, MAX(o) FILTER (WHERE year = 2023) - MAX(o) FILTER (WHERE year = 1978) AS raw FROM r GROUP BY area_name), k AS (SELECT area_name, raw, ROUND(raw, 1) AS chg, ROW_NUMBER() OVER (ORDER BY raw DESC, area_name) AS rn FROM c) SELECT area_name, chg FROM k WHERE raw < 0 ORDER BY rn DESC
```

```sql id=pref_change_up
WITH d AS (SELECT DISTINCT area_name, year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND year IN (1978, 2023) AND cat01 IN ('H1310', 'H1320') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT area_name, year, MAX(v) FILTER (WHERE cat01 = 'H1310') / (MAX(v) FILTER (WHERE cat01 = 'H1310') + MAX(v) FILTER (WHERE cat01 = 'H1320')) * 100 AS o FROM d GROUP BY area_name, year), c AS (SELECT area_name, MAX(o) FILTER (WHERE year = 2023) - MAX(o) FILTER (WHERE year = 1978) AS raw FROM r GROUP BY area_name), k AS (SELECT area_name, raw, ROUND(raw, 1) AS chg, ROW_NUMBER() OVER (ORDER BY raw DESC, area_name) AS rn FROM c) SELECT area_name, chg FROM k WHERE raw > 0 ORDER BY rn DESC
```

```sql id=direction_counts
WITH d AS (SELECT DISTINCT area_name, year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND year IN (1978, 2023) AND cat01 IN ('H1310', 'H1320', 'H1321', 'H1322', 'H1323') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), b AS (SELECT area_name, year, MAX(v) FILTER (WHERE cat01 = 'H1310') + MAX(v) FILTER (WHERE cat01 = 'H1320') AS base, MAX(v) FILTER (WHERE cat01 = 'H1310') AS own, MAX(v) FILTER (WHERE cat01 = 'H1321') AS pub, MAX(v) FILTER (WHERE cat01 = 'H1322') AS priv, MAX(v) FILTER (WHERE cat01 = 'H1323') AS corp FROM d GROUP BY area_name, year), c AS (SELECT area_name, MAX(own / base) FILTER (WHERE year = 2023) * 100 - MAX(own / base) FILTER (WHERE year = 1978) * 100 AS d_own, MAX(priv / base) FILTER (WHERE year = 2023) * 100 - MAX(priv / base) FILTER (WHERE year = 1978) * 100 AS d_priv, MAX(pub / base) FILTER (WHERE year = 2023) * 100 - MAX(pub / base) FILTER (WHERE year = 1978) * 100 AS d_pub, MAX(corp / base) FILTER (WHERE year = 2023) * 100 - MAX(corp / base) FILTER (WHERE year = 1978) * 100 AS d_corp FROM b GROUP BY area_name), u AS (SELECT '持ち家' AS kind, d_own AS chg FROM c UNION ALL SELECT '民営借家', d_priv FROM c UNION ALL SELECT '公営・UR・公社の借家', d_pub FROM c UNION ALL SELECT '給与住宅', d_corp FROM c) SELECT kind AS "所有関係", count(*) FILTER (WHERE chg > 0) AS "上がった数", count(*) FILTER (WHERE chg < 0) AS "下がった数", ROUND(MAX(chg), 1) AS "変化の最大値（ポイント）", ROUND(MEDIAN(chg), 1) AS "変化の中央値（ポイント）", ROUND(MIN(chg), 1) AS "変化の最小値（ポイント）" FROM u GROUP BY kind ORDER BY CASE kind WHEN '持ち家' THEN 1 WHEN '民営借家' THEN 2 WHEN '公営・UR・公社の借家' THEN 3 ELSE 4 END
```

```sql id=pref_tenure_change
WITH d AS (SELECT DISTINCT area_name, year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND year IN (1978, 2023) AND cat01 IN ('H1310', 'H1320', 'H1321', 'H1322', 'H1323') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), b AS (SELECT area_name, year, MAX(v) FILTER (WHERE cat01 = 'H1310') + MAX(v) FILTER (WHERE cat01 = 'H1320') AS base, MAX(v) FILTER (WHERE cat01 = 'H1310') AS own, MAX(v) FILTER (WHERE cat01 = 'H1321') AS pub, MAX(v) FILTER (WHERE cat01 = 'H1322') AS priv, MAX(v) FILTER (WHERE cat01 = 'H1323') AS corp FROM d GROUP BY area_name, year), r AS (SELECT area_name, MAX(own / base * 100) FILTER (WHERE year = 1978) AS o78, MAX(own / base * 100) FILTER (WHERE year = 2023) AS o23, MAX(priv / base * 100) FILTER (WHERE year = 2023) - MAX(priv / base * 100) FILTER (WHERE year = 1978) AS d_priv, MAX(pub / base * 100) FILTER (WHERE year = 2023) - MAX(pub / base * 100) FILTER (WHERE year = 1978) AS d_pub, MAX(corp / base * 100) FILTER (WHERE year = 2023) - MAX(corp / base * 100) FILTER (WHERE year = 1978) AS d_corp, MAX(own) FILTER (WHERE year = 2023) AS own23, MAX(base) FILTER (WHERE year = 2023) AS base23 FROM b GROUP BY area_name) SELECT area_name AS "都道府県", ROUND(o78, 1) AS "1978年の持ち家率（%）", ROUND(o23, 1) AS "2023年の持ち家率（%）", ROUND(o23 - o78, 1) AS "持ち家の変化（ポイント）", ROUND(d_priv, 1) AS "民営借家の変化（ポイント）", ROUND(d_pub, 1) AS "公営・UR・公社の変化（ポイント）", ROUND(d_corp, 1) AS "給与住宅の変化（ポイント）", CAST(own23 AS BIGINT) AS "2023年の持ち家数（戸）", CAST(base23 - own23 AS BIGINT) AS "2023年の借家数（戸）" FROM r ORDER BY o23 - o78 DESC, area_name
```

```sql id=spread_by_year
WITH d AS (SELECT DISTINCT area_name, year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND cat01 IN ('H1310', 'H1320') AND TRY_CAST(value AS DOUBLE) IS NOT NULL), r AS (SELECT area_name, year, MAX(v) FILTER (WHERE cat01 = 'H1310') / (MAX(v) FILTER (WHERE cat01 = 'H1310') + MAX(v) FILTER (WHERE cat01 = 'H1320')) * 100 AS o FROM d GROUP BY area_name, year) SELECT year AS "調査年", ARG_MAX(area_name, o) AS "最も高い都道府県", ROUND(MAX(o), 1) AS "最高の持ち家率（%）", ARG_MIN(area_name, o) AS "最も低い都道府県", ROUND(MIN(o), 1) AS "最低の持ち家率（%）", ROUND(ROUND(MAX(o), 1) - ROUND(MIN(o), 1), 1) AS "差（ポイント）" FROM r GROUP BY year ORDER BY "調査年"
```

```sql id=okinawa_units
WITH d AS (SELECT DISTINCT year, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.h_pref_housing WHERE area_name = '沖縄県' AND cat01 IN ('H1101', 'H1310', 'H1322') AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT year, CAST(MAX(v) FILTER (WHERE cat01 = 'H1101') AS BIGINT) AS stock_units, CAST(MAX(v) FILTER (WHERE cat01 = 'H1310') AS BIGINT) AS own_units, CAST(MAX(v) FILTER (WHERE cat01 = 'H1322') AS BIGINT) AS private_units FROM d GROUP BY year ORDER BY year
```
