---
title: 人口が7万人増えたつくば市で、地区の半分は減っている
description: つくば市の人口は20年で7万189人増え、その82%は2005年に住民が1人もいなかった42地区の増加です。2005年から住民がいた269地区のうち156地区は人口が減っています。
publishedAt: 2026-02-14
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口
  - まちづくり
  - つくば市
datasets:
  - queria/e_stat
  - queria/tsukuba
sources:
  - title: つくば市オープンデータカタログ
    url: https://t1070170.dupf.jp/ckan/
    publisher: つくば市
  - title: 統計でみる市区町村のすがた（社会・人口統計体系）
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 外国人住民に係る住民基本台帳制度
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/c-gyousei/zairyu.html
    publisher: 総務省
agentHint: つくば市の地区別に、2005年10月と2025年10月の15歳未満（0-4・5-9・10-14）の人数を出して。減った地区と増えた地区で、子どもの減り方がどれだけ違うかを比べて
socialAnnounce: |-
  つくば市の地区別・年齢別人口を、2005年と2025年の20年で突き合わせました。

  出店候補地の商圏評価や、公共施設の配置検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

つくば市の人口は、2005年10月の19万1,582人から2025年10月の26万1,771人へ、20年で7万189人増えました。増えた人数の82%にあたる5万7,332人は、2005年に住民が1人もいなかった42地区の人口です。2005年に住民がいた269地区のうち、156地区（58%）は人口が減るか、地区の名前がなくなっています。65歳以上の割合は、新しい42地区が5.7%、人口が減った148地区が33.6%でした。

つくば市はつくばエクスプレス（TX）が開業した2005年から人口が増え続けています。市は地区ごとの人口を公開しているので、20年分を地区ごとに並べて、増えた地区と減った地区を集計しました。出店の候補地選びや、店舗・施設の配置を決めるときに、市全体の人口と地区ごとの人口がどれだけ異なるかを確認できます。

## 市全体の人口は20年で7万189人増え、毎年前年を上回っている

つくば市オープンデータの地区別・年齢別人口（`tsukuba.main.mart_tsukuba_population`）を使います。基準日（`reference_date`）ごとに、地区（`area_name`）・性別（`sex`）・5歳階級（`age_group`）別の人口が入っています。収録は2003年4月から2025年10月までで、毎年3回の基準日が置かれています。ここでは各年の10月1日の値を取り出して、年ごとの系列にしています。

```sql
SELECT * FROM data_coverage
```

```chart
{
  "layer": [
    {
      "data": {"name": "city_registry"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"population\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#2563eb",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#2563eb"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "population", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年（10月1日時点）", "format": "d", "tickMinStep": 5}
        },
        "y": {
          "field": "population",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "住民基本台帳人口（人）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "center",
        "fontSize": 10,
        "color": "#e11d48"
      },
      "encoding": {
        "x": {"datum": 2005, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 1)"}},
        "text": {"value": "TX開業"}
      }
    }
  ]
}
```

2005年10月の19万1,582人から、2025年10月には26万1,771人になりました。20年で7万189人、1.37倍です。どの年も前年を上回っています。

2011年10月から2012年10月にかけての増加は8,703人で、前年の1,522人、翌年の2,087人より大きくなっています。2012年7月に[外国人住民が住民基本台帳の記録対象になった](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/c-gyousei/zairyu.html)ためで、この年の増加分と20年の倍率には、転入以外の増加が含まれています。

## 2005年に住民がいた269地区のうち、156地区は人口が減るか名前がなくなった

2005年10月と2025年10月の人口を地区ごとに突き合わせ、2005年に住民がいたかどうかと、増えたか減ったかで4つに分けました。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "area_change_summary"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__i"}]},
            {
              "calculate": "[\"#2563eb\",\"#60a5fa\",\"#f87171\",\"#ef4444\"][datum.__i - 1]",
              "as": "__color"
            }
          ],
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "category", "type": "nominal"},
              {"field": "change", "type": "quantitative"}
            ],
            "x": {
              "field": "category",
              "type": "nominal",
              "axis": {"title": "", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "change",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "2005年10月からの増減（人）", "grid": true}
            },
            "color": {"field": "__color", "type": "nominal", "scale": null, "legend": null}
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "area_change_summary"},
          "mark": {"type": "point", "filled": true, "size": 100},
          "encoding": {
            "tooltip": [
              {"field": "areas", "type": "quantitative"},
              {"field": "category", "type": "nominal"}
            ],
            "x": {
              "field": "category",
              "type": "nominal",
              "axis": {"title": "", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "areas",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "地区数", "orient": "right"}
            },
            "color": {
              "datum": "地区数",
              "type": "nominal",
              "scale": {"domain": ["増減（人）", "地区数"], "range": ["#3b82f6", "#111827"]},
              "title": null
            }
          }
        },
        {
          "data": {"name": "area_change_summary"},
          "mark": {"type": "text", "baseline": "bottom", "dy": -6},
          "encoding": {
            "x": {
              "field": "category",
              "type": "nominal",
              "axis": {"title": "", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "areas",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "地区数", "orient": "right"}
            },
            "text": {"field": "areas"}
          }
        }
      ]
    }
  ],
  "resolve": {"scale": {"y": "independent"}},
  "config": {"legend": {"orient": "bottom"}}
}
```

```sql
SELECT category AS 区分, areas AS 地区数, pop_2005 AS 人口2005年10月, pop_2025 AS 人口2025年10月, change AS 増減 FROM area_change_summary
```

2005年10月に住民がいた地区は269ありました。そのうち148地区は2025年までに人口が減り、8地区は地区の名前がなくなっています。合わせて156地区、58%です。市全体では7万人増えていますが、地区の数では人口が減った地区のほうが多くなっています。

増えた人口の大半は、2005年に住民が1人もいなかった42地区の人口です。この42地区に2025年時点で5万7,332人が住んでいて、市全体の増加7万189人の82%を占めます。既存の地区で増えた人数は3万4,513人で、減った地区の2万896人と名前がなくなった地区の760人を差し引くと1万2,857人です。

地区は住居表示の単位で、区画整理の途中で一時的な地区名が現れて消えることがあります。23年間で延べ349の名前が現れ、2025年10月に住民がいるのは303です。ここでは2005年10月か2025年10月のどちらかに住民がいた名前だけを集計しているので、その間に現れて消えた名前は4つの区分のどれにも入りません。

## 増えた人数の上位15地区で、市全体の増加の65%を占める

増えた人数の上位15地区を並べました。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "top_growth"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "change", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "change",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年10月からの増加（人）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

```sql
SELECT area_name AS 地区, pop_2005 AS 人口2005年10月, pop_2025 AS 人口2025年10月, change AS 増加, category AS 区分 FROM top_growth
```

```sql
SELECT * FROM growth_concentration
```

上位15地区で4万5,532人分、市全体の増加の65%を占めます。そのうち12地区は2005年に住民がいなかった地区（図の青）で、この12地区だけで3万7,198人分です。既存の地区は橙で示しています。

上位はみどりの・研究学園・学園の森・島名香取台・谷田部陣場です。みどりのと研究学園はTXの駅名でもあります。既存の地区で大きく増えた竹園１丁目・竹園３丁目・吾妻１丁目は、つくば駅のある一帯にあたります。

## 1998年度から2024年度に耕地面積は1,880ha減り、住宅の着工は年2,300戸を下回らなかった

新しい地区ができる前の土地の使われ方を確認するため、e-Stat「社会・人口統計体系」の市区町村データから、つくば市（地域コード `08220`）の耕地面積（`C3107`）と着工新設住宅戸数（`H1800`）を並べます。耕地面積は経済基盤（`c_municipal_economy`）、着工新設住宅戸数は居住（`h_municipal_housing`）と別のテーブルに入っているので、年で結合しています。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "farmland_housing"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "new_houses", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "new_houses",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "着工新設住宅（戸）", "grid": true}
            },
            "color": {
              "datum": "着工新設住宅戸数",
              "type": "nominal",
              "scale": {"domain": ["着工新設住宅戸数", "耕地面積"], "range": ["#f59e0b", "#16a34a"]},
              "title": null
            }
          }
        },
        {
          "data": {"values": [{}]},
          "mark": {"type": "rule", "color": "#e11d48", "strokeDash": [6, 4]},
          "encoding": {
            "x": {"datum": 2005, "type": "ordinal"},
            "y": {"value": {"expr": "height * (1 - 0)"}},
            "y2": {"value": {"expr": "height * (1 - 1)"}}
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "farmland_housing"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"farmland_ha\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#16a34a",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 16}
          },
          "encoding": {
            "tooltip": [
              {"field": "year", "type": "quantitative"},
              {"field": "farmland_ha", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "farmland_ha",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "耕地面積（ha）", "orient": "right"}
            },
            "color": {
              "datum": "耕地面積",
              "type": "nominal",
              "scale": {"domain": ["着工新設住宅戸数", "耕地面積"], "range": ["#f59e0b", "#16a34a"]},
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

耕地面積は1998年度の1万1,730haから2024年度の9,850haまで、26年で1,880ha減りました。住宅の着工はTX開業前後の2005〜2007年度に3,422戸・3,893戸・3,954戸へ増え、その後も年2,300戸を下回っていません。2014年度の3,900戸、2021年度の3,923戸と、同じ水準の年は後にもあります。耕地面積は2003年度から2021年度までのすべての年が100haの倍数で収録されているので、この期間の年ごとの細かい増減は判定できません。

この2つの系列は市全体の値なので、減った農地が新しい地区の場所と同じかどうかは判定できません。1998年度から2024年度にかけて、市全体で耕地が増えた年はなく、住宅の着工は毎年続いていました。

## 65歳以上の割合は、新しい42地区が5.7%、人口が減った148地区が33.6%

区分ごとに、2025年10月時点の年齢構成を出しました。名前がなくなった8地区はこの時点の人口が0なので、表と図に出るのは3つの区分と市全体です。

```chart
{
  "layer": [
    {
      "data": {"name": "age_by_group"},
      "transform": [
        {"fold": ["under15_pct", "over65_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"under15_pct\": \"15歳未満\", \"over65_pct\": \"65歳以上\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"under15_pct\",\"over65_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "category",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口に占める比率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["15歳未満", "65歳以上"], "range": ["#22c55e", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["15歳未満", "65歳以上"]},
        "tooltip": [
          {"field": "category", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

```sql
SELECT category AS 区分, areas AS 地区数, population AS 人口2025年10月, under15_pct AS 年少人口比率, over65_pct AS 高齢化率 FROM age_by_group
```

2005年に無かった42地区は、15歳未満が25.8%で65歳以上が5.7%です。既存で減った148地区は、15歳未満が9.4%で65歳以上が33.6%です。65歳以上の比率には6倍近い差があります。

つくば市全体の65歳以上は19.3%です。3つの区分のうちこの値に近いのは、既存で増えた113地区の16.4%だけです。

区分ごとの平均と、個々の地区の値も異なります。地区ごとの高齢化率を市全体の19.3%と比較しました。

```sql
SELECT * FROM aging_distance
```

市全体から10ポイント以上離れた地区に住む市民は13万5,684人、市の51.8%です。人口500人未満の地区を除いても11万2,732人、43.1%が残ります。市全体の統計をもとに商圏や施設の配置を考えると、市民の4割から5割については、住んでいる地区と10ポイント以上異なる数字で判断することになります。

```sql
SELECT * FROM aging_spread
```

人口500人以上の154地区のうち、65歳以上が3割以上の地区が39、1割に満たない地区が37あります。最高は54.0%、最低は0.0%です。

## 人口が減った上位15地区のうち11地区は、65歳以上が3割を超える

減った人数の上位15地区を、2005年と2025年の65歳以上の比率とともに並べました。図の色は2025年の比率です。1世帯の転出入で比率が大きく動く小さな地区を除くため、2005年に500人以上いた地区に限っています。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "top_decline"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "change", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "change",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2005年10月からの減少（人）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "field": "over65_pct",
          "type": "quantitative",
          "scale": {
            "range": [
              "rgb(12,51,131)",
              "rgb(10,136,186)",
              "rgb(242,211,56)",
              "rgb(242,143,56)",
              "rgb(217,30,30)"
            ]
          }
        }
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

```sql
SELECT area_name AS 地区, pop_2005 AS 人口2005年10月, pop_2025 AS 人口2025年10月, change AS 増減, change_pct AS 増減率, over65_pct_2005 AS 高齢化率2005年, over65_pct AS 高齢化率2025年 FROM top_decline
```

15地区のうち11地区で65歳以上が3割を超えています。宝陽台の54.0%、森の里の53.0%、桜ニユータウンの51.7%、城山の50.2%は、いずれも住民の半数以上が65歳以上です。北条・作谷・上郷１・小田・吉沼２といった市の周辺部の地区も、34.8%から49.2%の範囲にあります。

残る4地区は3割に届きません。松代４丁目が20.4%、並木４丁目が12.9%、吾妻２丁目が3.8%、筑波大学生宿舎が0.0%です。

この15地区のうち13地区は、2005年からの20年で65歳以上の比率が10ポイント以上上がっています。森の里は12.9%から53.0%、桜ニユータウンは14.8%から51.7%、緑が丘は12.8%から45.9%です。残る2地区は筑波大学生宿舎（0.0%のまま）と吾妻２丁目（0.3%から3.8%）で、人数だけが減りました。これらの地区で子育て世帯向けの需要を見込むと、20年前の人口構成を前提に判断することになります。2005年に無かった42地区は15歳未満が25.8%で、市全体の15.1%を大きく上回ります。同じ市の中でも、地区によって想定する客層を変える必要があります。

## まとめ

- つくば市の住民基本台帳人口は2005年10月の19万1,582人から2025年10月の26万1,771人へ、20年で7万189人（1.37倍）増えた
- 増加の82%にあたる5万7,332人は、2005年10月に住民が1人もいなかった42地区の人口。2005年に住民がいた269地区のうち156地区、58%は減っている（うち8地区は名前がなくなった）
- 増加上位15地区で市全体の増加の65%を占め、そのうち12地区は2005年に住民がいなかった地区
- 65歳以上の比率は、新しい42地区が5.7%、既存で減った148地区が33.6%。市全体の19.3%から10ポイント以上離れた地区に住む市民は13万5,684人で、市の51.8%
- 人口500人以上の154地区のうち、65歳以上が3割以上の地区が39、1割未満が37。最高54.0%と最低0.0%が同じ市内にある

## データの出典

本記事は[つくば市オープンデータカタログ](https://t1070170.dupf.jp/ckan/)（CKAN）の地区別・年齢別人口を整えた `tsukuba.main.mart_tsukuba_population` と、e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)（総務省統計局）の市区町村データ `e_stat.ssds.c_municipal_economy`・`e_stat.ssds.h_municipal_housing` を、2026-09-06 時点で集計しています。人口は住民基本台帳ベースで、各年10月1日時点の値です。e-Stat 側で使った分類コードは耕地面積が C3107、着工新設住宅戸数が H1800 で、いずれも年度の値です。指標の定義は[項目定義 C 経済基盤](https://www.e-stat.go.jp/koumoku/koumoku_teigi/C)・[項目定義 H 居住](https://www.e-stat.go.jp/koumoku/koumoku_teigi/H)によります。

Queriaは、つくば市の地区別・年齢別人口の列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[つくば市の地区別・年齢別人口テーブル](/datasets/queria/tsukuba/main/mart_tsukuba_population)から、検討している地区の人口構成を確認できます。

```sql id=data_coverage
WITH per_year AS ( SELECT YEAR(reference_date) AS y, COUNT(DISTINCT reference_date) AS n FROM tsukuba.main.mart_tsukuba_population GROUP BY y ), spans AS ( SELECT MIN(reference_date) AS d0, MAX(reference_date) AS d1, COUNT(DISTINCT reference_date) AS n_dates, COUNT(DISTINCT area_name) AS n_areas FROM tsukuba.main.mart_tsukuba_population ) SELECT s.n_dates AS 時点数, s.d0 AS 最初の基準日, s.d1 AS 最後の基準日, MIN(p.n) AS 年あたり基準日数の最小, MAX(p.n) AS 年あたり基準日数の最大, s.n_areas AS 延べ地区名数 FROM spans s CROSS JOIN per_year p GROUP BY s.n_dates, s.d0, s.d1, s.n_areas
```

```sql id=city_registry
SELECT YEAR(reference_date) AS year, SUM(population) AS population, SUM(population) - LAG(SUM(population)) OVER (ORDER BY reference_date) AS change_from_prev FROM tsukuba.main.mart_tsukuba_population WHERE MONTH(reference_date) = 10 GROUP BY reference_date ORDER BY reference_date
```

```sql id=area_change_summary
WITH snap AS ( SELECT area_name, reference_date, SUM(population) AS pop FROM tsukuba.main.mart_tsukuba_population WHERE reference_date IN (DATE '2005-10-01', DATE '2025-10-01') GROUP BY area_name, reference_date ), wide AS ( SELECT area_name, COALESCE(MAX(CASE WHEN reference_date = DATE '2005-10-01' THEN pop END), 0) AS pop_2005, COALESCE(MAX(CASE WHEN reference_date = DATE '2025-10-01' THEN pop END), 0) AS pop_2025 FROM snap GROUP BY area_name ) SELECT CASE WHEN pop_2005 = 0 THEN '2005年に無かった地区' WHEN pop_2025 = 0 THEN '2025年に消えた地区' WHEN pop_2025 > pop_2005 THEN '既存で増えた地区' ELSE '既存で減った地区' END AS category, COUNT(*) AS areas, SUM(pop_2005) AS pop_2005, SUM(pop_2025) AS pop_2025, SUM(pop_2025 - pop_2005) AS change FROM wide GROUP BY category ORDER BY change DESC
```

```sql id=top_growth
WITH snap AS ( SELECT area_name, reference_date, SUM(population) AS pop FROM tsukuba.main.mart_tsukuba_population WHERE reference_date IN (DATE '2005-10-01', DATE '2025-10-01') GROUP BY area_name, reference_date ), wide AS ( SELECT area_name, COALESCE(MAX(CASE WHEN reference_date = DATE '2005-10-01' THEN pop END), 0) AS pop_2005, COALESCE(MAX(CASE WHEN reference_date = DATE '2025-10-01' THEN pop END), 0) AS pop_2025 FROM snap GROUP BY area_name ) SELECT area_name, pop_2005, pop_2025, pop_2025 - pop_2005 AS change, CASE WHEN pop_2005 = 0 THEN '2005年に無かった地区' ELSE '既存の地区' END AS category, CASE WHEN pop_2005 = 0 THEN '#2563eb' ELSE '#f59e0b' END AS color FROM wide ORDER BY change DESC, area_name LIMIT 15
```

```sql id=growth_concentration
WITH snap AS ( SELECT area_name, reference_date, SUM(population) AS pop FROM tsukuba.main.mart_tsukuba_population WHERE reference_date IN (DATE '2005-10-01', DATE '2025-10-01') GROUP BY area_name, reference_date ), wide AS ( SELECT area_name, COALESCE(MAX(CASE WHEN reference_date = DATE '2005-10-01' THEN pop END), 0) AS pop_2005, COALESCE(MAX(CASE WHEN reference_date = DATE '2025-10-01' THEN pop END), 0) AS pop_2025 FROM snap GROUP BY area_name ), ranked AS ( SELECT area_name, pop_2005, pop_2025 - pop_2005 AS change, ROW_NUMBER() OVER (ORDER BY pop_2025 - pop_2005 DESC, area_name) AS rn FROM wide ) SELECT SUM(change) AS 市全体の増減, COUNT(*) FILTER (WHERE pop_2005 > 0) AS 起点で人がいた地区数, SUM(change) FILTER (WHERE rn <= 15) AS 増加上位15地区の増減, SUM(change) FILTER (WHERE rn <= 15 AND pop_2005 = 0) AS うち2005年に無かった地区の増減, COUNT(*) FILTER (WHERE rn <= 15 AND pop_2005 = 0) AS うち2005年に無かった地区数 FROM ranked
```

```sql id=farmland_housing
WITH farm AS ( SELECT year, TRY_CAST(value AS DOUBLE) AS farmland_ha FROM e_stat.ssds.c_municipal_economy WHERE area = '08220' AND cat01 = 'C3107' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), house AS ( SELECT year, TRY_CAST(value AS DOUBLE) AS new_houses FROM e_stat.ssds.h_municipal_housing WHERE area = '08220' AND cat01 = 'H1800' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ) SELECT COALESCE(f.year, h.year) AS year, f.farmland_ha, h.new_houses FROM farm f FULL JOIN house h ON f.year = h.year WHERE COALESCE(f.year, h.year) >= 1998 ORDER BY year
```

```sql id=age_by_group
WITH snap AS ( SELECT area_name, reference_date, SUM(population) AS pop FROM tsukuba.main.mart_tsukuba_population WHERE reference_date IN (DATE '2005-10-01', DATE '2025-10-01') GROUP BY area_name, reference_date ), wide AS ( SELECT area_name, COALESCE(MAX(CASE WHEN reference_date = DATE '2005-10-01' THEN pop END), 0) AS pop_2005, COALESCE(MAX(CASE WHEN reference_date = DATE '2025-10-01' THEN pop END), 0) AS pop_2025 FROM snap GROUP BY area_name ), grouped AS ( SELECT area_name, CASE WHEN pop_2005 = 0 THEN '2005年に無かった地区' WHEN pop_2025 > pop_2005 THEN '既存で増えた地区' ELSE '既存で減った地区' END AS category FROM wide WHERE pop_2025 > 0 ), age AS ( SELECT area_name, SUM(population) AS pop, SUM(CASE WHEN age_group IN ('0-4', '5-9', '10-14') THEN population ELSE 0 END) AS under15, SUM(CASE WHEN age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) AS over65 FROM tsukuba.main.mart_tsukuba_population WHERE reference_date = DATE '2025-10-01' GROUP BY area_name ) SELECT g.category, COUNT(*) AS areas, SUM(a.pop) AS population, ROUND(SUM(a.under15) * 100.0 / SUM(a.pop), 1) AS under15_pct, ROUND(SUM(a.over65) * 100.0 / SUM(a.pop), 1) AS over65_pct FROM grouped g JOIN age a ON a.area_name = g.area_name GROUP BY g.category UNION ALL SELECT 'つくば市全体', COUNT(DISTINCT area_name), SUM(population), ROUND(SUM(CASE WHEN age_group IN ('0-4', '5-9', '10-14') THEN population ELSE 0 END) * 100.0 / SUM(population), 1), ROUND(SUM(CASE WHEN age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) * 100.0 / SUM(population), 1) FROM tsukuba.main.mart_tsukuba_population WHERE reference_date = DATE '2025-10-01' ORDER BY over65_pct
```

```sql id=aging_spread
WITH area AS ( SELECT area_name, SUM(population) AS pop, SUM(CASE WHEN age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) * 100.0 / SUM(population) AS over65_pct FROM tsukuba.main.mart_tsukuba_population WHERE reference_date = DATE '2025-10-01' GROUP BY area_name HAVING SUM(population) >= 500 ) SELECT COUNT(*) AS 人口500人以上の地区数, COUNT(*) FILTER (WHERE over65_pct >= 30) AS 高齢化率30パーセント以上, COUNT(*) FILTER (WHERE over65_pct >= 40) AS 高齢化率40パーセント以上, COUNT(*) FILTER (WHERE over65_pct < 10) AS 高齢化率10パーセント未満, ROUND(MAX(over65_pct), 1) AS 最高, ROUND(MIN(over65_pct), 1) AS 最低 FROM area
```

```sql id=aging_distance
WITH city AS ( SELECT SUM(CASE WHEN age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) * 100.0 / SUM(population) AS pct FROM tsukuba.main.mart_tsukuba_population WHERE reference_date = DATE '2025-10-01' ), area AS ( SELECT area_name, SUM(population) AS pop, SUM(CASE WHEN age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) * 100.0 / SUM(population) AS pct FROM tsukuba.main.mart_tsukuba_population WHERE reference_date = DATE '2025-10-01' GROUP BY area_name ) SELECT ROUND((SELECT pct FROM city), 1) AS 市全体の高齢化率, SUM(a.pop) AS 市の人口, SUM(a.pop) FILTER (WHERE ABS(a.pct - (SELECT pct FROM city)) >= 10) AS 市全体から10ポイント以上離れた地区の人口, ROUND(SUM(a.pop) FILTER (WHERE ABS(a.pct - (SELECT pct FROM city)) >= 10) * 100.0 / SUM(a.pop), 1) AS その比率, SUM(a.pop) FILTER (WHERE ABS(a.pct - (SELECT pct FROM city)) >= 10 AND a.pop >= 500) AS うち人口500人以上の地区の分, ROUND(SUM(a.pop) FILTER (WHERE ABS(a.pct - (SELECT pct FROM city)) >= 10 AND a.pop >= 500) * 100.0 / SUM(a.pop), 1) AS その比率500人以上 FROM area a
```

```sql id=top_decline
WITH snap AS ( SELECT area_name, reference_date, SUM(population) AS pop FROM tsukuba.main.mart_tsukuba_population WHERE reference_date IN (DATE '2005-10-01', DATE '2025-10-01') GROUP BY area_name, reference_date ), wide AS ( SELECT area_name, COALESCE(MAX(CASE WHEN reference_date = DATE '2005-10-01' THEN pop END), 0) AS pop_2005, COALESCE(MAX(CASE WHEN reference_date = DATE '2025-10-01' THEN pop END), 0) AS pop_2025 FROM snap GROUP BY area_name ), age AS ( SELECT area_name, ROUND(SUM(CASE WHEN reference_date = DATE '2005-10-01' AND age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) * 100.0 / NULLIF(SUM(CASE WHEN reference_date = DATE '2005-10-01' THEN population ELSE 0 END), 0), 1) AS over65_pct_2005, ROUND(SUM(CASE WHEN reference_date = DATE '2025-10-01' AND age_group IN ('65-69', '70-74', '75-79', '80-84', '85+') THEN population ELSE 0 END) * 100.0 / NULLIF(SUM(CASE WHEN reference_date = DATE '2025-10-01' THEN population ELSE 0 END), 0), 1) AS over65_pct FROM tsukuba.main.mart_tsukuba_population WHERE reference_date IN (DATE '2005-10-01', DATE '2025-10-01') GROUP BY area_name ) SELECT w.area_name, w.pop_2005, w.pop_2025, w.pop_2025 - w.pop_2005 AS change, ROUND((w.pop_2025 - w.pop_2005) * 100.0 / w.pop_2005, 1) AS change_pct, a.over65_pct_2005, a.over65_pct FROM wide w JOIN age a ON a.area_name = w.area_name WHERE w.pop_2005 >= 500 AND w.pop_2025 > 0 ORDER BY change ASC, w.area_name LIMIT 15
```
