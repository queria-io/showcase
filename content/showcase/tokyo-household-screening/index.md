---
title: 東京都で2013〜2026年に人口が減った20市町村のうち、14は世帯数が増えていた
description: 東京都で2013年6月〜2026年9月に人口が減った20市町村のうち、14は世帯数が増えていました。この14市町村の人口は29,612人減り、世帯数は64,822増えています。
ogDescription: 東京都の62区市町村のうち、2013年6月から2026年9月に人口が減ったのは20市町村で、うち14は世帯数が増えていました。
publishedAt: 2026-07-30
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 東京都
  - 世帯
  - 商圏分析
datasets:
  - queria/metro_tokyo
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 住民基本台帳による世帯と人口：毎月
    url: https://www.toukei.metro.tokyo.lg.jp/juukim/jm-index.htm
    publisher: 東京都
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: metro_tokyo.stats.resident_population から、2013年6月と2026年9月で人口が減って世帯数が増えた区市町村を出して、同じ条件を東京都以外の都道府県でも確かめて
socialAnnounce: |-
  候補地の絞り込みで「人口が減っている地域は外す」とすると、東京都では2013〜2026年に人口が減った20自治体が落ちます。

  うち14自治体を合わせると、人口が約3万人減る間に世帯数は約6万5千増えていました。
  Queriaは行政のオープンデータを整えて公開しています。
---

東京都の62区市町村のうち、2013年6月から2026年9月に人口が減ったのは20市町村で、そのうち14は世帯数が増えていました。この14市町村を合計すると、人口は29,612人減り、世帯数は64,822増えています。本土部の9市町はすべて多摩地域にあり、八王子市は人口が0.92%減って世帯数が14.1%増えました。

冷蔵庫・洗濯機・ソファ・通信回線などの商材は、必要な数が世帯数で決まります。それでも出店候補地の一次スクリーニングには人口が使われることが多くあります。この記事では、人口が減っている地域を候補から外す条件を[東京都の住民基本台帳](https://www.toukei.metro.tokyo.lg.jp/juukim/jm-index.htm)に当てはめ、どの自治体が候補から外れるかを確認しました。

## 人口が減った20市町村のうち、14は世帯数が増えている

2013年6月から2026年9月までの13年3か月で、62の区市町村を人口と世帯数の増減で分けました。住民基本台帳には2012年8月分から外国人の世帯が加わり、都全体の世帯数はこの月に約21万増えています。比較の起点の2013年6月は、この月より後です。

```sql
SELECT * FROM foreign_step
```

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "q_up"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_g", "type": "quantitative"},
          {"field": "hh_g", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口の増減率（%・2013年6月比）", "grid": true}
        },
        "y": {
          "field": "hh_g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "世帯数の増減率（%・2013年6月比）", "grid": true}
        },
        "color": {
          "datum": "人口も世帯数も増加（42）",
          "type": "nominal",
          "scale": {
            "domain": ["人口も世帯数も増加（42）", "人口は減少・世帯数は増加（14）", "人口も世帯数も減少（6）"],
            "range": ["#93c5fd", "#ef4444", "#64748b"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "q_flip"},
      "mark": {"type": "point", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_g", "type": "quantitative"},
          {"field": "hh_g", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口の増減率（%・2013年6月比）", "grid": true}
        },
        "y": {
          "field": "hh_g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "世帯数の増減率（%・2013年6月比）", "grid": true}
        },
        "color": {
          "datum": "人口は減少・世帯数は増加（14）",
          "type": "nominal",
          "scale": {
            "domain": ["人口も世帯数も増加（42）", "人口は減少・世帯数は増加（14）", "人口も世帯数も減少（6）"],
            "range": ["#93c5fd", "#ef4444", "#64748b"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "q_down"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_g", "type": "quantitative"},
          {"field": "hh_g", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口の増減率（%・2013年6月比）", "grid": true}
        },
        "y": {
          "field": "hh_g",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "世帯数の増減率（%・2013年6月比）", "grid": true}
        },
        "color": {
          "datum": "人口も世帯数も減少（6）",
          "type": "nominal",
          "scale": {
            "domain": ["人口も世帯数も増加（42）", "人口は減少・世帯数は増加（14）", "人口も世帯数も減少（6）"],
            "range": ["#93c5fd", "#ef4444", "#64748b"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
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
        "x": {"datum": -1, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0.95)"}},
        "text": {"value": "← 人口の条件で落ちる20自治体"}
      }
    }
  ]
}
```

人口を条件にすると、破線より左の20自治体が候補から外れます。そのうち14は、同じ期間に世帯数が増えていました（赤い点）。人口の条件で外れた候補の7割は、世帯単位の需要が増えている地域です。

人口と世帯数の両方が減っているのは6自治体だけで、人口が増えて世帯数が減った自治体はありません。人口で絞り込んだときの誤りは、世帯数が増えている地域を候補から外すことだけです。

14という数は起点の月によって少し変わります。起点を2012年8月から2014年12月までのどの月に置いても、人口で落ちる19〜20自治体のうち12〜14で世帯数が増えていて、本土部に限ると8〜9です。

```sql
SELECT * FROM baseline_check
```

候補から外れる14自治体を合計すると、この期間に人口は29,612人減り、世帯数は64,822増えています。

冷蔵庫や洗濯機、回線契約のような世帯単位の商材では、増えた世帯の数だけ需要が増えます。4人が同居していれば冷蔵庫は1台ですが、その世帯が2つの住まいに分かれれば2台必要になります。人口が約3万人減ったという数字だけでは、この64,822世帯の増加は把握できません。64,822のうち64,699は本土部の9市町の増加で、島しょ部の5村は合わせて123です。

住民基本台帳の世帯は住民票の届け出で数えるので、同じ住まいのまま世帯を分けた届け出も2世帯になります。住まいが実際に分かれたかは、住んでいる場所で世帯を数える国勢調査で確認できます。[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の国勢調査の値と、同じ2015年10月から2020年10月の住民基本台帳を並べると、本土部の9市町のうち瑞穂町を除く8つで国勢調査の一般世帯数も増えていて、そのうち7つは伸びが住民基本台帳より大きくなっています。2010年から2020年で見ると、9市町はすべて国勢調査でも増えています。島しょ部の5村では、2015年から2020年に国勢調査で増えたのは小笠原村と神津島村だけです。

```sql
SELECT * FROM census_check
```

## 人口が減って世帯数が増えた本土部の9市町は、すべて多摩地域にある

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "q_flip"},
      "transform": [
        {"fold": ["hh_g", "pop_g"], "as": ["__series", "__value"]},
        {"calculate": "{\"hh_g\": \"世帯数\", \"pop_g\": \"人口\"}[datum.__series]", "as": "__name"},
        {"calculate": "indexof([\"hh_g\",\"pop_g\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2013年6月比の増減率（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["世帯数", "人口"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["人口", "世帯数"]},
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

世帯数の伸びが最も大きいのは八王子市で、人口は0.92%減り、世帯数は14.1%増えています。291,305世帯は都内62区市町村で9番目の規模ですが、人口の条件では候補から外れます。本土部の残り8つも同じで、武蔵村山市13.5%増、瑞穂町12.2%増、あきる野市12.0%増、青梅市10.8%増、東村山市10.4%増、福生市9.7%増、羽村市7.6%増、日の出町4.3%増と続きます。残る5つは利島村・青ヶ島村・神津島村・小笠原村・御蔵島村で、人口が158人から2,457人の島しょ部です。世帯数は115〜1,502で、数世帯の転入・転出で増減率が数%変わります。

落ちる自治体がどこにあるかを、[国土数値情報の行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)の境界に重ねました。地図に載るのは本土部の53区市町村で、島しょ部の9町村は載っていません。

```map
type: map
layers:
  - from: map
    geojson: geojson
    color: grp
    label: label
lng: 139.45
lat: 35.71
zoom: 8.3
```

赤が人口減・世帯増、灰色が人口も世帯数も減った自治体です。赤の9つはすべて多摩地域で、区部は1つもありません。灰色の奥多摩町と檜原村は都の西端にあり、赤の青梅市・あきる野市・八王子市と境を接しています。本土部だけでは人口の条件で外れるのは11自治体で、そのうち9で世帯数が増えていました。多摩の西側では、世帯数が増えている市と、人口も世帯数も減っている町村が隣り合っています。

## 人口が減って世帯数が増えたのは、1世帯あたり人員が人口より大きく減ったため

世帯数は人口を1世帯あたり人員で割った値です。人口が減っても、1世帯あたり人員がそれより大きく減れば、世帯数は増えます。

青梅市では、人口が7.3%減り、1世帯あたり人員は2.28人から1.91人へ16.3%減りました。1世帯あたり人員のほうが人口より大きく減ったので、世帯数は10.8%増えました。実数では人口が138,339人から128,245人へ10,094人減り、世帯数は60,670から67,193へ6,523増えました。

62自治体で1世帯あたり人員が増えたのは中央区だけ（1.73人→1.76人）です。中央区は人口の伸び47.2%に対して世帯数の伸びが44.7%で、世帯数の伸びのほうが小さいのは中央区だけです。1世帯あたり人員が減らなければ、世帯数の伸び率は人口の伸び率を上回りません。

## 1世帯あたり人員は稲城市が2.14人、新宿区が1.51人で、同じ人口でも世帯数は1.4倍異なる

商圏人口を世帯数に直す係数が、この1世帯あたり人員です。2026年9月時点の値を62区市町村で並べました。

```chart
{
  "height": 1280,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pph", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pph",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1世帯あたり人員（人・2026年9月）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "区市町村"},
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
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pph", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pph",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1世帯あたり人員（人・2026年9月）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "区市町村"},
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
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pph", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pph",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1世帯あたり人員（人・2026年9月）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "区市町村"},
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

最も大きいのは稲城市の2.14人で、区部で最も小さいのは新宿区の1.51人です。商圏人口が同じでも、この2つでは世帯数がおよそ1.4倍異なります。人口あたりの売上原単位を都内一律に使うと、世帯単位の商材の見込みは、新宿区では世帯数で見積もった場合より少なく、稲城市では多く出ます。上位は稲城市・日の出町・武蔵村山市と多摩地域の市町が占め、区部では新宿区に次いで中野区の1.55人、豊島区の1.56人が小さい値です。全体で最も小さいのは青ヶ島村の1.37人で、115世帯の村です。

1世帯あたり人員が同じでも、世帯の構成が同じとは限りません。世帯が小さい理由には、単身世帯が多い場合と、高齢の夫婦だけが残った場合があります。

## 1世帯あたり人員がほぼ同じ杉並区と檜原村で、65歳以上のいる世帯は24.1%と70.7%

[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の家族類型を重ね、縦軸に親族世帯以外（一般世帯から親族世帯を引いた、単身と非親族の世帯）の割合、点の色に65歳以上の世帯員がいる世帯の割合を置きました。家族類型は2020年10月の調査なので、横軸の2026年9月とは6年近い差があります。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "mix"},
      "mark": {"type": "point", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pph", "type": "quantitative"},
          {"field": "nonkin_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "pph",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1世帯あたり人員（人・2026年9月）", "grid": true}
        },
        "y": {
          "field": "nonkin_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "親族世帯以外の割合（%・2020年）", "grid": true}
        },
        "color": {
          "field": "elderly_pct",
          "type": "quantitative",
          "scale": {
            "range": [
              "rgb(128,0,38)",
              "rgb(189,0,38)",
              "rgb(227,26,28)",
              "rgb(252,78,42)",
              "rgb(253,141,60)",
              "rgb(254,178,76)",
              "rgb(254,217,118)",
              "rgb(255,237,160)",
              "rgb(255,255,204)"
            ],
            "reverse": true
          }
        }
      }
    }
  ]
}
```

杉並区は1世帯あたり1.71人、檜原村は1.70人とほぼ同じですが、親族世帯以外の割合は杉並区59.5%、檜原村36.7%です。65歳以上の世帯員がいる世帯は杉並区24.1%に対し檜原村70.7%で、檜原村の小さな世帯は高齢の夫婦や一人暮らしの高齢者が中心だと考えられます。1世帯あたり人員が最大の稲城市（2.14人）と2番目の日の出町（2.09人）も、65歳以上のいる世帯は32.3%と54.3%で、20ポイント以上の差があります。

単身と非親族を合わせた割合が区部で最も高いのは新宿区の68.6%で、渋谷区66.5%・豊島区65.0%が続きます。一人暮らし向けの商材なら、この3区が有力な候補になります。

## 商圏をどう評価するか

候補地を評価する手順は次の3つです。

1. 一次スクリーニングの条件を人口から世帯数に替える。人口が減っていても世帯数が増えている地域は候補に残す
2. 商圏人口から世帯数を見積もるときは、地域ごとの1世帯あたり人員で割る。人口あたりの売上原単位を都内で横並びに使わない
3. 世帯規模が近い候補地どうしは、親族世帯以外の割合と65歳以上のいる世帯の割合を確認して品揃えを分ける。この2つの出典は5年ごとの国勢調査なので、1世帯あたり人員が2020年より後に大きく減っている地域では家族類型の構成も変わっている可能性があり、次の国勢調査の結果で品揃えの前提を再確認する

## データの出典

本記事は東京都の[住民基本台帳による世帯と人口](https://www.toukei.metro.tokyo.lg.jp/juukim/jm-index.htm)（毎月1日現在）、[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)の小地域の世帯の家族類型、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別の国勢調査の値、[国土数値情報の行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を、2026-11-06 時点で集計しています。

Queriaは、東京都が月ごとに分けて公表している世帯と人口を1つのテーブルにまとめて公開しています。本記事で使った[東京都の世帯と人口テーブル](/datasets/queria/metro_tokyo/stats/resident_population)と[国勢調査の家族類型テーブル](/datasets/queria/e_stat/census/census_small_area_household)、[市区町村の人口・世帯テーブル](/datasets/queria/e_stat/ssds/a_municipal_population)から、担当エリアの区市町村が人口の条件と世帯数の条件で候補に残るかを確認できます。

```sql id=q_up
WITH b AS (SELECT area_name, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2013-06'), l AS (SELECT area_name, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT l.area_name, ROUND((l.p::DOUBLE / b.p - 1) * 100, 2) AS pop_g, ROUND((l.h::DOUBLE / b.h - 1) * 100, 2) AS hh_g, ROUND(b.p::DOUBLE / b.h, 2) AS pph13, ROUND(l.p::DOUBLE / l.h, 2) AS pph26 FROM l JOIN b ON b.area_name = l.area_name WHERE l.p >= b.p ORDER BY pop_g
```

```sql id=q_flip
WITH b AS (SELECT area_code, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2013-06'), l AS (SELECT area_code, area_name, population_total AS p, household_total AS h, ROW_NUMBER() OVER (ORDER BY household_total DESC) AS hh_rank FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT l.area_name, l.area_code, l.hh_rank, b.p AS pop13, l.p AS pop26, b.h AS hh13, l.h AS hh26, ROUND((l.p::DOUBLE / b.p - 1) * 100, 2) AS pop_g, ROUND((l.h::DOUBLE / b.h - 1) * 100, 2) AS hh_g, ROUND(b.p::DOUBLE / b.h, 2) AS pph13, ROUND(l.p::DOUBLE / l.h, 2) AS pph26, ROUND(((l.p::DOUBLE / l.h) / (b.p::DOUBLE / b.h) - 1) * 100, 1) AS pph_g FROM l JOIN b ON b.area_code = l.area_code WHERE l.p < b.p AND l.h > b.h ORDER BY hh_g DESC
```

```sql id=q_down
WITH b AS (SELECT area_code, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2013-06'), l AS (SELECT area_code, area_name, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT l.area_name, l.area_code, ROUND((l.p::DOUBLE / b.p - 1) * 100, 2) AS pop_g, ROUND((l.h::DOUBLE / b.h - 1) * 100, 2) AS hh_g, ROUND(b.p::DOUBLE / b.h, 2) AS pph13, ROUND(l.p::DOUBLE / l.h, 2) AS pph26 FROM l JOIN b ON b.area_code = l.area_code WHERE l.p < b.p AND l.h <= b.h ORDER BY pop_g
```

```sql id=map
WITH b AS (SELECT area_code, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2013-06'), l AS (SELECT area_code, area_name, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT ST_AsGeoJSON(ST_Simplify(g.geometry, 0.002)) AS geojson, CASE WHEN l.p >= b.p THEN 0 WHEN l.h > b.h THEN 1 ELSE 2 END AS cat, CASE WHEN l.p >= b.p THEN '両方とも増加' WHEN l.h > b.h THEN '人口減・世帯増' ELSE '両方とも減少' END AS grp, l.area_name || '：人口 ' || ROUND((l.p::DOUBLE / b.p - 1) * 100, 1) || '%／世帯数 ' || ROUND((l.h::DOUBLE / b.h - 1) * 100, 1) || '%' AS label FROM nlftp.boundary.municipality g JOIN l ON l.area_code = g.lg_code JOIN b ON b.area_code = g.lg_code WHERE g.prefecture_code = '13' AND g.lg_code < '13360'
```

```sql id=rank_top
WITH ranked AS (SELECT area_name, ROUND(population_total::DOUBLE / household_total, 2) AS pph, ROW_NUMBER() OVER (ORDER BY population_total::DOUBLE / household_total DESC, area_name) AS rn FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT area_name, pph FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT area_name, ROUND(population_total::DOUBLE / household_total, 2) AS pph, ROW_NUMBER() OVER (ORDER BY population_total::DOUBLE / household_total DESC, area_name) AS rn FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT area_name, pph FROM ranked WHERE rn > 10 AND rn <= 52 ORDER BY rn
```

```sql id=rank_bottom
WITH ranked AS (SELECT area_name, ROUND(population_total::DOUBLE / household_total, 2) AS pph, ROW_NUMBER() OVER (ORDER BY population_total::DOUBLE / household_total DESC, area_name) AS rn FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT area_name, pph FROM ranked WHERE rn > 52 ORDER BY rn
```

```sql id=mix
WITH cen AS (SELECT area, MAX(CASE WHEN cat01 = '0010' THEN value END) AS total, MAX(CASE WHEN cat01 = '0020' THEN value END) AS kinship, MAX(CASE WHEN cat01 = '0090' THEN value END) AS elderly FROM e_stat.census.census_small_area_household WHERE length(area) = 5 AND area LIKE '13%' GROUP BY area), rp AS (SELECT area_code, area_name, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09') SELECT rp.area_name, rp.h AS hh, ROUND(rp.p::DOUBLE / rp.h, 2) AS pph, ROUND((cen.total - cen.kinship) / cen.total * 100, 1) AS nonkin_pct, ROUND(cen.elderly / cen.total * 100, 1) AS elderly_pct FROM rp JOIN cen ON cen.area = rp.area_code ORDER BY pph
```

```sql id=baseline_check
-- 起点の月を2012年8月〜2014年12月で動かしたときの、2026年9月までの件数の幅
WITH l AS (SELECT area_code, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09'), b AS (SELECT year_month, area_code, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month BETWEEN '2012-08' AND '2014-12'), per_month AS (SELECT b.year_month, COUNT(*) FILTER (WHERE l.p < b.p) AS pop_down, COUNT(*) FILTER (WHERE l.p < b.p AND l.h > b.h) AS flip, COUNT(*) FILTER (WHERE l.p < b.p AND l.h > b.h AND l.area_code < '13360') AS flip_mainland FROM b JOIN l ON l.area_code = b.area_code GROUP BY b.year_month) SELECT MIN(year_month) AS "起点の最初の月", MAX(year_month) AS "起点の最後の月", COUNT(*) AS "起点の月数", MIN(pop_down) || '〜' || MAX(pop_down) AS "人口が減った自治体", MIN(flip) || '〜' || MAX(flip) AS "うち世帯数が増えた自治体", MIN(flip_mainland) || '〜' || MAX(flip_mainland) AS "うち本土部" FROM per_month
```

```sql id=census_check
-- 人口で落ちて世帯数が増えた14自治体の、住民基本台帳と国勢調査の世帯数の増減
WITH b AS (SELECT area_code, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2013-06'), l AS (SELECT area_code, area_name, population_total AS p, household_total AS h FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month = '2026-09'), r AS (SELECT area_code, MAX(CASE WHEN year_month = '2015-10' THEN household_total END) AS h15, MAX(CASE WHEN year_month = '2020-10' THEN household_total END) AS h20 FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month IN ('2015-10', '2020-10') GROUP BY area_code), c AS (SELECT area, MAX(CASE WHEN year = 2010 THEN value END) AS h10, MAX(CASE WHEN year = 2015 THEN value END) AS h15, MAX(CASE WHEN year = 2020 THEN value END) AS h20 FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A710101' AND year IN (2010, 2015, 2020) AND area LIKE '13%' GROUP BY area) SELECT l.area_name AS "自治体", CASE WHEN l.area_code < '13360' THEN '本土部' ELSE '島しょ部' END AS "地域", l.h - b.h AS "住基の世帯の増加（2013年6月→2026年9月）", ROUND((r.h20::DOUBLE / r.h15 - 1) * 100, 1) AS "住基の世帯数増減率（%・2015年10月→2020年10月）", ROUND((c.h20 / c.h15 - 1) * 100, 1) AS "国勢調査の一般世帯数増減率（%・2015年→2020年）", ROUND((c.h20 / c.h10 - 1) * 100, 1) AS "国勢調査の一般世帯数増減率（%・2010年→2020年）" FROM l JOIN b ON b.area_code = l.area_code JOIN r ON r.area_code = l.area_code JOIN c ON c.area = l.area_code WHERE l.p < b.p AND l.h > b.h ORDER BY 2 DESC, 3 DESC
```

```sql id=foreign_step
-- 外国人の世帯が住民基本台帳に加わった2012年8月分の前後の、都全体（62区市町村の合計）の人口と世帯数
SELECT year_month AS "月", SUM(population_total) AS "人口", SUM(household_total) AS "世帯数" FROM metro_tokyo.stats.resident_population WHERE area_type = '区市町村' AND year_month IN ('2012-07', '2012-08') GROUP BY year_month ORDER BY year_month
```
