---
title: 送電網につながる蓄電池は3年2か月で14倍の169か所になり、最大出力の6割は4つの道県にある
description: 経済産業省の電力調査統計から、送電網につながる蓄電池の箇所数と最大出力を都道府県別・月ごとに集計しました。2023年4月から2026年6月までに12か所から169か所へ増え、最大出力の60.2%は鹿児島県・宮崎県・宮城県・北海道の4道県にあります。
ogDescription: 電力調査統計から蓄電池の箇所数と最大出力を都道府県別・月ごとに集計。2023年4月から2026年6月までに12か所から169か所へ増えた一方、最大出力の6割は4道県に集まっています。
publishedAt: 2026-09-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 蓄電池
  - 電力調査統計
  - 資源エネルギー庁
datasets:
  - queria/enecho
  - queria/nlftp
sources:
  - title: 電力調査統計
    url: https://www.enecho.meti.go.jp/statistics/electric_power/ep002/
    publisher: 資源エネルギー庁
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 自分の県と隣接する県について、蓄電池の箇所数と最大出力を2023年4月から月ごとに並べて。1か所あたりの平均出力も出して
socialAnnounce: |-
  経済産業省の電力調査統計から、送電網につながる蓄電池を都道府県別に集計しました。

  2023年4月から2026年6月までに12か所から169か所へ。ただし最大出力の6割は4道県に集まっています。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

送電網につながる蓄電池は、2023年4月の12か所・193,542kWから、2026年6月には169か所・1,800,990kWに増えました。箇所数は14.1倍、最大出力は約9.3倍です。2026年6月時点の最大出力の60.2%は、鹿児島県・宮崎県・宮城県・北海道の4道県にあります。4道県の箇所数は22か所で、全国の13.0%です。1か所の規模は40kWから300,295kWまで4桁の幅があります。

ここで扱う蓄電池は、工場や住宅に付ける蓄電池ではなく、送電網に直接接続して、電気が余るときにためて足りないときに送り出す設備です。自治体の企業誘致や産業振興の窓口には、こうした施設を建てたいという相談が持ち込まれることがあり、窓口では用地の広さや周辺への影響を判断します。この記事では、[資源エネルギー庁の電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)を使い、送電網につながる蓄電池が全国のどこに何か所あり、1か所あたりどれくらいの出力なのかを、都道府県別・月ごとに集計しました。相談を受けた案件の規模を、全国の設備と比較するための材料になります。

## 蓄電池は、電力調査統計の「新エネルギー等」の内訳に箇所数と最大出力が載っている

電力調査統計は、発電設備を電源の種類ごとに集計した統計です。都道府県ごとに、その電源の発電所が何か所あるか（箇所数）と、それらを合わせた最大出力が何キロワットか（kW）が、月ごとに記録されています。蓄電池がこのテーブルに入っているのは、送電網に電気を送り出す設備だからです。

大きな区分は水力・火力・原子力・新エネルギー等・その他の5つで、蓄電池は「新エネルギー等」の内訳として風力・太陽光・地熱と並んでいます。次の表の6行のうち、太陽光・風力・蓄電池はこの内訳にあたるので、水力・火力・原子力と合計しても都道府県の発電所総数にはなりません。蓄電池の収録は2023年4月分から始まり、それより前の月には欄そのものがありません。

```sql
SELECT '水力' AS '電源', SUM(hydro_plants) AS '箇所数', ROUND(SUM(hydro_capacity_kw)) AS '最大出力(kW)' FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' UNION ALL SELECT '火力', SUM(thermal_plants), ROUND(SUM(thermal_capacity_kw)) FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' UNION ALL SELECT '原子力', SUM(nuclear_plants), ROUND(SUM(nuclear_capacity_kw)) FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' UNION ALL SELECT '太陽光', SUM(solar_plants), ROUND(SUM(solar_capacity_kw)) FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' UNION ALL SELECT '風力', SUM(wind_plants), ROUND(SUM(wind_capacity_kw)) FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' UNION ALL SELECT '蓄電池', SUM(storage_battery_plants), ROUND(SUM(storage_battery_capacity_kw)) FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606'
```

蓄電池は169か所・1,800,990kWです。箇所数では原子力の15か所より多く風力の406か所より少なく、最大出力では太陽光19,007,140kWの1割弱にあたります。

## 3年2か月で12か所から169か所に増えた

蓄電池が収録され始めた2023年4月から2026年6月まで、全国の箇所数と最大出力を月ごとに並べます。左の軸が箇所数、右の軸が最大出力です。

```chart
{
  "height": 300,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "trend"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"t\"]) && isValid(datum[\"plants\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {"type": "line", "color": "#3b82f6", "invalid": "break-paths-show-domains"},
          "encoding": {
            "tooltip": [
              {"field": "label", "type": "nominal"},
              {"field": "t", "type": "quantitative"},
              {"field": "plants", "type": "quantitative"}
            ],
            "x": {
              "field": "t",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年", "format": "d", "tickMinStep": 1}
            },
            "y": {
              "field": "plants",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "箇所数", "grid": true}
            },
            "color": {
              "datum": "箇所数",
              "type": "nominal",
              "scale": {"domain": ["箇所数", "最大出力"], "range": ["#3b82f6", "#f97316"]},
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "trend"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {"calculate": "isValid(datum[\"t\"]) && isValid(datum[\"mw\"]) ? 0 : 1", "as": "__gap"},
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
          "encoding": {
            "tooltip": [
              {"field": "label", "type": "nominal"},
              {"field": "t", "type": "quantitative"},
              {"field": "mw", "type": "quantitative"}
            ],
            "x": {
              "field": "t",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年", "format": "d", "tickMinStep": 1}
            },
            "y": {
              "field": "mw",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "最大出力（MW）", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "最大出力",
              "type": "nominal",
              "scale": {"domain": ["箇所数", "最大出力"], "range": ["#3b82f6", "#f97316"]},
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

2023年4月は12か所・193,542kWでした。2026年6月には169か所・1,800,990kWで、箇所数は14.1倍、最大出力は約9.3倍になっています。

箇所数と最大出力は同じようには増えていません。2025年8月から10月にかけて、箇所数は40か所から62か所へ22か所増え、最大出力は389,190kWから1,064,348kWへ2.7倍になっています。この2か月に増えた出力675,158kWを増えた22か所で割ると、1か所あたり30,689kWです。既存の設備の出力が変わった分も含む平均です。2025年8月時点の1か所あたり平均9,730kWの3.2倍で、それまでより大きな設備が加わりました。

## 最大出力の60.2%は4つの道県にある

次に、2026年6月時点の最大出力を都道府県別に並べます。棒の中の数字は、その道県にある箇所数です。

```chart
{
  "height": 780,
  "layer": [
    {
      "data": {"name": "pref_capacity"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "site_label", "type": "nominal"},
          {"field": "mw", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "mw",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "蓄電池の最大出力（MW）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "pref_capacity"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "mw",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "蓄電池の最大出力（MW）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "text": {"field": "site_label"}
      }
    }
  ]
}
```

上位は鹿児島県400,947kW（7か所）、宮崎県300,295kW（1か所）、宮城県217,732kW（7か所）、北海道164,342kW（7か所）です。この4道県で1,083,316kWとなり、全国の最大出力の60.2%を占めます。箇所数では4道県の合計は22か所で、全国169か所の13.0%です。

この4道県の割合は、大きな設備が加わった2025年9〜10月を経て、10月から2026年4月までは66.9〜70.7%で推移していましたが、5月に66.3%、6月に60.2%へ下がりました。4月から6月の2か月で全国の最大出力は252,840kW増え、そのうち山口県が99,900kW、福島県が68,465kW、青森県が42,275kWを占めます。宮城県と北海道は、この2か月で出力がわずかに減っています。

```sql
SELECT * FROM recent_change
```

表の山形県の40kW減と山梨県の40kW増は同じ大きさで、1件の記録が県をまたいで移ったものと考えられます。徳島県は2026年4月分に、箇所数0のまま最大出力1,999kWが記録されていました。月ごとの記録には、こうした誤差が含まれます。

箇所数が同じ道県どうしでも、最大出力には大きな差があります。7か所ある5道県は、鹿児島県400,947kW・宮城県217,732kW・北海道164,342kW・熊本県12,874kW・兵庫県11,859kWで、鹿児島県は兵庫県の33.8倍です。11か所では福岡県70,489kWと埼玉県21,089kWで3.3倍の差があります。宮崎県は1か所だけで、最も箇所数の多い静岡県（12か所・31,291kW）の9.6倍の出力を持っています。

## 1か所しかない12府県では、最大の宮崎県と最小の山梨県で7,507倍の差がある

蓄電池が1か所だけの府県では、その1か所の最大出力がそのまま記録されているので、設備1つの規模を直接比較できます。横軸は目盛の幅が一定ではない対数目盛です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "single_site"},
      "mark": {"type": "point", "color": "#7c3aed", "filled": true, "size": 121},
      "encoding": {
        "tooltip": [
          {"field": "kw", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "kw",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "その1か所の最大出力（kW・対数目盛）", "grid": true, "tickMinStep": 1}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県", "grid": true},
          "sort": null
        }
      }
    }
  ]
}
```

最も大きいのは宮崎県の300,295kW、最も小さいのは山梨県の40kWで、その差は7,507倍です。山梨県の40kWは、前の節の表で山形県から移ったように見えた記録です。2番目に小さい岩手県の1,500kWと比較しても、宮崎県は200倍の出力です。大分県1,960kW・奈良県1,979kW・秋田県1,998kW・香川県1,998kWの4県は、2,000kWのすぐ下に集まっています。

同じ1か所の蓄電池でも、規模は4桁異なります。最も大きい宮崎県の300,295kWは、この統計に載る火力発電所495か所の1か所あたり平均309,657kWに近い出力です。ここでの出力は一度に出せる電力の大きさで、何時間流し続けられるか（蓄えられる電力量）はこの統計には記録されていません。相談を受けた案件の最大出力が分からなければ、必要な用地や送電網への接続の規模は判断できません。

## 蓄電池がある都道府県は、9から41に増えた

都道府県ごとの箇所数を地図にしました。色が濃いほど箇所数の多い都道府県です。

```map
type: map
layers:
  - from: pref_map
    geojson: geojson
    color: plants
    label: pref_name
    name: "箇所数"
lng: 137.5
lat: 38
zoom: 4
```

蓄電池が1か所以上あるのは41都道府県で、2023年4月の9都道府県から4倍以上に広がりました。2026年6月時点で1か所もないのは、山形県・神奈川県・富山県・福井県・京都府・高知県の6府県です。

色の濃い都道府県は、北海道から九州まで分布しています。箇所数の上位3県は静岡県（12か所）・福岡県（11か所）・埼玉県（11か所）で、最大出力は21,089kWから70,489kWです。出力の上位4道県には入りません。宮崎県は1か所だけで、出力は全国2位です。箇所数が多い地域と、大きな設備がある地域は、一部しか重なりません。

## 業務でどう使うか

- 立地の相談を受けたとき、その案件の最大出力を全国の設備と比較できます。1か所しかない12府県のうち6県は2,000kWに満たず、4府県が8,130kWから12,000kWの間、残る2県が48,000kW以上です。数万kW以上の案件は、1か所しかない府県の中では和歌山県・宮崎県と並ぶ規模です
- 自分の自治体が属する県と近隣の県について、箇所数と最大出力を同じ集計で並べられます。同じ箇所数でも出力が10倍以上違うことがあるので、近隣の状況は箇所数と出力を合わせて確認する必要があります
- 月ごとに記録されているので、庁内の説明資料を更新するときは、同じクエリを再実行すると最新の数字に差し替えられます

## データの出典

本記事は資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)の都道府県別・電源種別の発電所数と最大出力を、2026年10月18日時点で集計しています。対象は蓄電池の収録が始まった2023年4月分から2026年6月分までで、数値は各月時点の記録です。

Queriaは、電力調査統計の電源種別ごとの箇所数と最大出力を列にし、都道府県の境界データと結合できる形で、テーブルと列の説明をつけて公開しています。本記事で使った[都道府県別の発電所数・最大出力テーブル](/datasets/queria/enecho/electric_power/power_plants_by_prefecture)から、自分の自治体が属する県の推移を確認したり、近隣の県と比較したりできます。

```sql id=trend
SELECT CAST(year AS DOUBLE) + CAST(month - 1 AS DOUBLE) / 12 AS t, printf('%d年%d月', year, month) AS label, CAST(SUM(COALESCE(storage_battery_plants, 0)) AS INTEGER) AS plants, CAST(SUM(COALESCE(storage_battery_capacity_kw, 0)) AS DOUBLE) / 1000 AS mw, CAST(COUNT(*) FILTER (WHERE storage_battery_plants != 0) AS INTEGER) AS prefs_with_sites, ROUND(CAST(100 AS DOUBLE) * SUM(storage_battery_capacity_kw) FILTER (WHERE pref_name IN ('鹿児島県', '宮崎県', '宮城県', '北海道')) / SUM(storage_battery_capacity_kw), 1) AS top4_capacity_pct FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month BETWEEN '202304' AND '202606' GROUP BY t, label ORDER BY t
```

```sql id=concentration
WITH latest AS (SELECT pref_name, COALESCE(storage_battery_plants, 0) AS n, CAST(COALESCE(storage_battery_capacity_kw, 0) AS DOUBLE) AS kw FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606'), r AS (SELECT pref_name, n, kw, ROW_NUMBER() OVER (ORDER BY kw DESC, pref_name) AS rn FROM latest) SELECT CAST(COUNT(*) FILTER (WHERE n != 0) AS INTEGER) AS prefs_with_sites, CAST(COUNT(*) FILTER (WHERE n = 0 AND kw != 0) AS INTEGER) AS prefs_capacity_only, CAST(COUNT(*) FILTER (WHERE n = 0 AND kw = 0) AS INTEGER) AS prefs_none, CAST(SUM(n) AS INTEGER) AS total_plants, ROUND(SUM(kw), 0) AS total_kw, CAST(SUM(n) FILTER (WHERE rn BETWEEN 1 AND 4) AS INTEGER) AS top4_plants, ROUND(SUM(kw) FILTER (WHERE rn BETWEEN 1 AND 4), 0) AS top4_kw, ROUND(CAST(100 AS DOUBLE) * SUM(kw) FILTER (WHERE rn BETWEEN 1 AND 4) / SUM(kw), 1) AS top4_capacity_pct, ROUND(CAST(100 AS DOUBLE) * SUM(n) FILTER (WHERE rn BETWEEN 1 AND 4) / SUM(n), 1) AS top4_plants_pct FROM r
```

```sql id=pref_capacity
SELECT pref_name, CAST(storage_battery_plants AS INTEGER) AS plants, CAST(storage_battery_capacity_kw AS DOUBLE) / 1000 AS mw, CAST(storage_battery_plants AS VARCHAR) || 'か所' AS site_label FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' AND storage_battery_plants != 0 ORDER BY mw ASC
```

```sql id=single_site
SELECT pref_name, CAST(storage_battery_capacity_kw AS DOUBLE) AS kw FROM enecho.electric_power.power_plants_by_prefecture WHERE year_month = '202606' AND storage_battery_plants = 1 ORDER BY kw ASC
```

```sql id=recent_change
SELECT a.pref_name AS "都道府県", CAST(b.storage_battery_plants AS INTEGER) AS "箇所数（2026年4月）", CAST(a.storage_battery_plants AS INTEGER) AS "箇所数（2026年6月）", CAST(b.storage_battery_capacity_kw AS DOUBLE) AS "最大出力kW（2026年4月）", CAST(a.storage_battery_capacity_kw AS DOUBLE) AS "最大出力kW（2026年6月）", CAST(a.storage_battery_capacity_kw - b.storage_battery_capacity_kw AS DOUBLE) AS "増減kW" FROM enecho.electric_power.power_plants_by_prefecture a JOIN enecho.electric_power.power_plants_by_prefecture b ON a.pref_name = b.pref_name WHERE a.year_month = '202606' AND b.year_month = '202604' AND a.storage_battery_capacity_kw != b.storage_battery_capacity_kw ORDER BY "増減kW" DESC
```

```sql id=pref_map
SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, CAST(p.storage_battery_plants AS INTEGER) AS plants, b.prefecture_name AS pref_name FROM nlftp.boundary.prefecture b JOIN enecho.electric_power.power_plants_by_prefecture p ON b.prefecture_name = p.pref_name WHERE p.year_month = '202606' AND p.storage_battery_plants != 0
```
