---
title: 人口あたりの50cc原付は、和歌山市と松山市で東京都の5倍以上。125ccまでの原付も同じ地域に多い
description: 50cc以下の原付は14年で327万台減りましたが、50cc超125cc以下の原付の増加はその6分の1です。人口あたりで多く残る地域は、50cc超の原付も多い地域でした。
publishedAt: 2026-10-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 交通
  - 地域比較
  - 市場分析
datasets:
  - queria/e_stat
sources:
  - title: 市町村税課税状況等の調（令和6年度）
    url: https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09_24.html
    publisher: 総務省
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 自分の県の市区町村ごとに、50cc以下の原付と90cc超の原付の台数を2010年度と2024年度で並べ、人口100人あたりでも比べて
socialAnnounce: |-
  50cc以下の原付の台数を人口あたりで比べました。

  和歌山市や松山市は東京都の5倍以上で、125cc以下の原付も同じ地域に多くあります。二輪販売の計画づくりに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

50cc以下の原付は、2010年度から2024年度に全国で327万台、43.9%減りました。同じ期間に50cc超125cc以下の原付は55万台増えましたが、50ccの減少の6分の1ほどです。人口100人あたりの50ccの台数は、最も多い和歌山県（10.73台）が最も少ない北海道（1.07台）の10倍で、50ccが多い県は50cc超の原付も多い県です。人口30万人を超える和歌山市や松山市でも、人口あたりの50ccは東京都の5倍以上あります。

2025年4月から、125cc以下で出力を抑えた二輪車を原付免許で運転できる[新基準原付](https://www.npa.go.jp/bureau/traffic/menkyo/menkyo_nirinsha.html)の区分が設けられ、50ccの原付に乗っている人の乗り換え先の選択肢が変わりました。二輪車の販売店や、メーカーの販売会社で地域ごとの販売計画を立てる人は、50ccの原付がどこにどれだけ残っているかを、仕入れや店舗の計画に使えます。この記事では、軽自動車税の課税の基礎になる車両の台数を、全国・都道府県・市区町村の3つの単位で2010年度から2024年度まで並べ、人口あたりの台数と14年間の減り方を比較しました。

## 全国では14年で327万台減った

使うのは e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の居住分野のテーブル（都道府県別の `h_pref_housing`、市区町村別の `h_municipal_housing`）です。元データは総務省の[市町村税課税状況等の調](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09_24.html)で、軽自動車税の賦課期日である各年度の4月1日時点の台数が入っています。原付は排気量などで次の区分に分かれています。

| コード  | 内容                                         |
| ------- | -------------------------------------------- |
| H7209   | 原動機付自転車台数（下の区分の合計）         |
| H720901 | 原動機付自転車台数（50cc以下）               |
| H720902 | 原動機付自転車台数（50cc超90cc以下）         |
| H720903 | 原動機付自転車台数（90cc超）                 |
| H720904 | 原動機付自転車台数（ミニカー）               |
| H720905 | 原動機付自転車台数（特定小型、2024年度のみ） |

この記事では50cc以下（`H720901`）を中心に、比較のために50cc超90cc以下（`H720902`）と、125cc以下のスクーターなどが入る90cc超（`H720903`）も並べます。台数は車両を主に置いている場所（主たる定置場）の市区町村で集計され、課税されない車両や、配達などに使う事業者の車両も含みます。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"c50\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "c50", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度（4月1日時点）", "format": "d"}
        },
        "y": {
          "field": "c50",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "台数", "grid": true}
        },
        "color": {
          "datum": "50cc以下",
          "type": "nominal",
          "scale": {
            "domain": ["50cc以下", "90cc超（125cc以下）", "50cc超90cc以下"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"c125\"]) ? 0 : 1",
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
          {"field": "c125", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度（4月1日時点）", "format": "d"}
        },
        "y": {
          "field": "c125",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "台数", "grid": true}
        },
        "color": {
          "datum": "90cc超（125cc以下）",
          "type": "nominal",
          "scale": {
            "domain": ["50cc以下", "90cc超（125cc以下）", "50cc超90cc以下"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"c90\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "c90", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度（4月1日時点）", "format": "d"}
        },
        "y": {
          "field": "c90",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "台数", "grid": true}
        },
        "color": {
          "datum": "50cc超90cc以下",
          "type": "nominal",
          "scale": {
            "domain": ["50cc以下", "90cc超（125cc以下）", "50cc超90cc以下"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
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

50cc以下の原付は2010年度の744万8,862台から2024年度の417万6,785台へ、43.9%減りました。減った台数は327万2,077台です。14年間、前の年より増えた年はありません。

90cc超の原付は90万218台から169万6,951台へ88.5%増えています。50cc超の2区分を合わせると増えたのは55万2,647台で、50ccの減少分の6分の1ほどです。50ccの減少は、125cc以下のスクーターへの乗り換えだけでは説明できません。

## 人口あたりでは、和歌山県が北海道の10倍

台数は人口が多いほど多くなるので、都道府県ごとに人口100人あたりの台数を計算します。分母は住民基本台帳の人口（社会・人口統計体系の `a_pref_population`、`A2301`）で、台数の時点（2024年4月1日）に最も近い2024年1月1日の値を使います。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per100", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per100",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口100人あたりの50cc以下の原付（台、2024年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
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
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per100", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per100",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口100人あたりの50cc以下の原付（台、2024年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
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
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per100", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per100",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口100人あたりの50cc以下の原付（台、2024年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
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

全国では人口100人あたり3.34台です。最も多い和歌山県は10.73台で、住民のおよそ9人に1台にあたります。続く愛媛県が8.04台、奈良県が6.84台、高知県が6.81台、京都府が6.70台で、上位10のうち山梨県を除く9つを近畿・中国・四国・九州の府県が占めます。最も少ない北海道は1.07台で、和歌山県は北海道の10倍です。下位には北海道のほか富山県（1.40台）、石川県・福井県（ともに1.65台）、秋田県（1.74台）と、北海道・北陸・東北の道県が並び、東京都も1.90台で下から6番目です。

## 50ccが多い県は、50cc超の原付も多い

50ccが少ない県で125cc以下の原付への乗り換えが進んでいるかを確認するため、都道府県ごとに、横軸に人口100人あたりの50ccの台数、縦軸に50cc超の2区分（50cc超90cc以下と90cc超で、いずれも125cc以下）を合わせた人口100人あたりの台数をとります。点にカーソルを合わせると、50ccの2010年度からの増減率も表示されます。

```chart
{
  "layer": [
    {
      "data": {"name": "pref_scatter"},
      "mark": {"type": "point", "color": "#ef4444", "opacity": 0.8, "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "per100", "type": "quantitative"},
          {"field": "over50_per100", "type": "quantitative"}
        ],
        "x": {
          "field": "per100",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口100人あたりの50cc以下の原付（台、2024年度）", "grid": true}
        },
        "y": {
          "field": "over50_per100",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口100人あたりの50cc超の原付（台、2024年度）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "per100",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口100人あたりの50cc以下の原付（台、2024年度）", "grid": true}
        },
        "y": {
          "field": "over50_per100",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口100人あたりの50cc超の原付（台、2024年度）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

点は右上がりに並びます。50cc超が多いのは京都府（3.45台）・和歌山県（3.18台）・沖縄県（3.11台）・愛媛県（3.00台）で、いずれも50ccも多い府県です。少ないのは北海道（0.57台）、秋田県・石川県・福井県（いずれも0.66台）で、50ccも少ない道県です。2024年度の時点で、50ccが少ない県ほど125cc以下の原付が多い、という形にはなっていません。原付をふだんの移動に使う地域では排気量に関係なく台数が多く、そうでない地域ではどちらも少ないと考えられます。

減り方にも地域差があります。50ccが多く残る和歌山県（−37.6%）・愛媛県（−37.1%）・沖縄県（−30.9%）は全国（−43.9%）より緩く、秋田県（−57.2%）・島根県（−58.5%）・青森県（−55.7%）は半分以上減りました。北海道は人口あたりで最も少ないのに−40.6%で全国より緩く、残っている台数が少ない県ほど減り方が速いとは限りません。

## 人口30万人を超える市でも、東京都の5倍以上

市区町村別のテーブルでも人口100人あたりの台数を計算します。人口の少ない町村は台数が少し変わるだけで値が大きく動くので、人口3万人以上の市町村の上位20を並べます。

```chart
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "muni_city"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "per100", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per100",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口100人あたりの50cc以下の原付（台、2024年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

最も多いのは和歌山県田辺市の14.98台で、愛媛県八幡浜市（13.13台）、大阪府熊取町（12.02台）が続きます。上位20のうち和歌山県が4市、愛媛県が4市町、大阪府が4市町を占めます。県庁所在地では人口35万6,472人の和歌山市が11.27台、人口50万231人の松山市が9.69台で、東京都（1.90台）のそれぞれ5.9倍、5.1倍です。人口の多い市でも、50ccがふだんの移動に使われていると考えられます。

人口の規模を問わずに並べると、上位は離島の町村です。

```sql
SELECT area_name AS 市区町村, pop AS 人口, c50 AS 台数50cc以下, per100 AS 人口100人あたり FROM muni_any
```

香川県直島町（41.5台）、東京都神津島村（33.1台）、鹿児島県与論町（30.5台）が上位に入り、島以外では和歌山県湯浅町（17.4台）が10位です。

14年間の増減でも、島の町村はほかと違う動きをしています。1,741市区町村のうち、50ccの台数が2010年度より減っていないのは7つだけで、市区町村ごとの増減率の中央値は−48.6%です。減っていない7つのうち4つは香川県直島町と東京都の利島村・御蔵島村・小笠原村で、ほかは沖縄県恩納村、東京都渋谷区、愛知県高浜市です。配達や貸し出しに使う事業者の車両も置き場所の市区町村で集計されるので、台数が少ない町村では、1つの事業者の動きで増減が決まることがあります。

```sql
SELECT area_name AS 市区町村, c2010 AS 台数2010年度, c2024 AS 台数2024年度, change_pct AS 増減率 FROM muni_not_decreased
```

## 販売計画での使い方

- 乗り換えの需要の大きさは、いま残っている台数で見積もります。和歌山市（4万192台）や松山市（4万8,473台）のように人口が多く、人口あたりの台数も多い市は、新基準原付や125cc以下のスクーターの在庫と、点検・修理の体制を増やす候補になります
- 50cc超の原付も多い府県は、排気量に関係なく原付をふだんの移動に使う人が多い地域です。乗り換え先として125cc以下の車種を品揃えに加える効果が大きいのは、こうした地域だと考えられます。減り方の速さは、需要が減っていく速さの目安として、残っている台数とは別に確認します
- 離島や観光地の町村では、台数に事業者の車両が含まれている可能性があります。人口あたりの台数がとくに多い町村は、住民の数だけで需要を見積もらず、地元の事業者の保有台数も確認してください

データは2024年4月1日時点までで、新基準原付が導入された後の台数の変化は含みません。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別・市区町村別データを2026年10月1日時点で集計しています。原付の台数の元データは総務省の[市町村税課税状況等の調](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09_24.html)（各年度4月1日時点）、人口の元データは総務省の[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)（2024年1月1日時点）です。

Queriaは官公庁の統計を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[市区町村別の居住データ](/datasets/e_stat/ssds/h_municipal_housing)や[都道府県別の居住データ](/datasets/e_stat/ssds/h_pref_housing)から、自店の商圏に入る市区町村の50ccと50cc超の原付の台数を、2010年度から確認できます。

```sql id=trend
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720901') AS c50, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720902') AS c90, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720903') AS c125 FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H720901', 'H720902', 'H720903') AND area_name != '全国' AND year BETWEEN 2010 AND 2024 GROUP BY year ORDER BY year
```

```sql id=national
WITH t AS (SELECT year, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720901') AS c50, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 IN ('H720902', 'H720903')) AS c_over50, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720903') AS c125 FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H720901', 'H720902', 'H720903') AND area_name != '全国' AND year IN (2010, 2024) GROUP BY year) SELECT a.c50 AS c50_2010, b.c50 AS c50_2024, ROUND((b.c50 / a.c50 - 1) * 100, 1) AS c50_change_pct, a.c50 - b.c50 AS c50_decrease, a.c125 AS c125_2010, b.c125 AS c125_2024, ROUND((b.c125 / a.c125 - 1) * 100, 1) AS c125_change_pct, a.c_over50 AS over50_2010, b.c_over50 AS over50_2024, b.c_over50 - a.c_over50 AS over50_increase FROM t a JOIN t b ON a.year = 2010 AND b.year = 2024
```

```sql id=pref_top
WITH v AS (SELECT area_name, SUM(TRY_CAST(value AS DOUBLE)) AS c50 FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H720901' AND year = 2024 AND area_name != '全国' GROUP BY area_name), p AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2301' AND year = 2023 AND area_name != '全国'), ranked AS (SELECT v.area_name, ROUND(v.c50 / p.pop * 100, 2) AS per100, ROW_NUMBER() OVER (ORDER BY v.c50 / p.pop DESC, v.area_name) AS rn FROM v JOIN p ON v.area_name = p.area_name) SELECT area_name, per100 FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH v AS (SELECT area_name, SUM(TRY_CAST(value AS DOUBLE)) AS c50 FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H720901' AND year = 2024 AND area_name != '全国' GROUP BY area_name), p AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2301' AND year = 2023 AND area_name != '全国'), ranked AS (SELECT v.area_name, ROUND(v.c50 / p.pop * 100, 2) AS per100, ROW_NUMBER() OVER (ORDER BY v.c50 / p.pop DESC, v.area_name) AS rn FROM v JOIN p ON v.area_name = p.area_name) SELECT area_name, per100 FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH v AS (SELECT area_name, SUM(TRY_CAST(value AS DOUBLE)) AS c50 FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H720901' AND year = 2024 AND area_name != '全国' GROUP BY area_name), p AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2301' AND year = 2023 AND area_name != '全国'), ranked AS (SELECT v.area_name, ROUND(v.c50 / p.pop * 100, 2) AS per100, ROW_NUMBER() OVER (ORDER BY v.c50 / p.pop DESC, v.area_name) AS rn FROM v JOIN p ON v.area_name = p.area_name) SELECT area_name, per100 FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=pref_national_rate
WITH v AS (SELECT SUM(TRY_CAST(value AS DOUBLE)) AS c50 FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H720901' AND year = 2024 AND area_name != '全国'), p AS (SELECT SUM(TRY_CAST(value AS DOUBLE)) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2301' AND year = 2023 AND area_name != '全国') SELECT ROUND(v.c50 / p.pop * 100, 2) AS per100 FROM v, p
```

```sql id=pref_scatter
WITH v AS (SELECT area_name, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720901' AND year = 2024) AS c50, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'H720901' AND year = 2010) AS c50_2010, SUM(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 IN ('H720902', 'H720903') AND year = 2024) AS c_over50 FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H720901', 'H720902', 'H720903') AND year IN (2010, 2024) AND area_name != '全国' GROUP BY area_name), p AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2301' AND year = 2023 AND area_name != '全国') SELECT v.area_name, ROUND(v.c50 / p.pop * 100, 2) AS per100, ROUND((v.c50 / v.c50_2010 - 1) * 100, 1) AS change_pct, ROUND(v.c_over50 / p.pop * 100, 2) AS over50_per100 FROM v JOIN p ON v.area_name = p.area_name ORDER BY v.area_name
```

```sql id=muni_city
WITH v AS (SELECT area, area_name, TRY_CAST(value AS DOUBLE) AS c50 FROM e_stat.ssds.h_municipal_housing WHERE cat01 = 'H720901' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'), p AS (SELECT area, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2301' AND year = 2023), ranked AS (SELECT v.area_name, p.pop, v.c50, ROUND(v.c50 / p.pop * 100, 2) AS per100, ROW_NUMBER() OVER (ORDER BY v.c50 / p.pop DESC, v.area_name) AS rn FROM v JOIN p ON v.area = p.area WHERE p.pop >= 30000) SELECT area_name, pop, c50, per100 FROM ranked WHERE rn <= 20 ORDER BY rn
```

```sql id=muni_any
WITH v AS (SELECT area, area_name, TRY_CAST(value AS DOUBLE) AS c50 FROM e_stat.ssds.h_municipal_housing WHERE cat01 = 'H720901' AND year = 2024 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%'), p AS (SELECT area, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2301' AND year = 2023), ranked AS (SELECT v.area_name, p.pop, v.c50, ROUND(v.c50 / p.pop * 100, 1) AS per100, ROW_NUMBER() OVER (ORDER BY v.c50 / p.pop DESC, v.area_name) AS rn FROM v JOIN p ON v.area = p.area) SELECT area_name, pop, c50, per100 FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=muni_change
WITH v AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2010) AS c2010, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS c2024 FROM e_stat.ssds.h_municipal_housing WHERE cat01 = 'H720901' AND year IN (2010, 2024) AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY area_name) SELECT COUNT(*) AS municipalities, COUNT(*) FILTER (WHERE c2024 >= c2010) AS not_decreased, ROUND(MEDIAN((c2024 / c2010 - 1) * 100), 1) AS median_change_pct FROM v
```

```sql id=muni_not_decreased
WITH v AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2010) AS c2010, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE year = 2024) AS c2024 FROM e_stat.ssds.h_municipal_housing WHERE cat01 = 'H720901' AND year IN (2010, 2024) AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' GROUP BY area_name) SELECT area_name, c2010, c2024, ROUND((c2024 / c2010 - 1) * 100, 1) AS change_pct FROM v WHERE c2024 >= c2010 ORDER BY change_pct DESC, area_name
```
