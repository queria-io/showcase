---
title: 使う量より多くの電気を送り出す市区町村は410あり、最も多いのは水力が最大の電源の166市区町村
description: 市区町村ごとに送電網へ流した電力量と受け取った電力量を比較しました。2024年度に送り出しが上回ったのは1,741のうち410で、最も多いのは水力が最大の電源の166市区町村、太陽光は65市区町村です。
ogDescription: 市区町村ごとに送電網へ流した電力量と受け取った電力量を比較しました。2024年度に送り出しが上回ったのは1,741のうち410です。
publishedAt: 2026-08-27
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 電力
  - 再生可能エネルギー
  - 市区町村
  - 脱炭素
datasets:
  - queria/enecho
  - queria/nlftp
sources:
  - title: 電力調査統計
    url: https://www.enecho.meti.go.jp/statistics/electric_power/ep002/
    publisher: 経済産業省 資源エネルギー庁
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 自分の市区町村について、2022年度から2024年度までの需要電力量と電源別の逆潮流量を月ごとに出して。水力・風力・太陽光それぞれが需要の何%にあたるかも比べて
socialAnnounce: |-
  市区町村ごとに、送電網へ流した電気と受け取った電気を突き合わせました。

  2024年度に送り出しが上回ったのは1,741のうち410。最も多いのは水力が最大の電源の166市区町村です。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2024年度に、送電網へ送り出した電力量が受け取った電力量を上回った市区町村は、1,741のうち410（23.5%）でした。410を最も多く送り出している電源で分類すると、水力が166市区町村で最も多く、火力が104、太陽光が65です。送り出しが上回る市区町村は、2022年度の373から3年で37増えました。

自治体が[地方公共団体実行計画（区域施策編）](https://www.env.go.jp/policy/local_keikaku/)を作るときは、区域内の再生可能エネルギーの導入量を目標として書きます。太陽光パネルの設置容量は把握していても、自分の町が電気を送り出している側か受け取っている側かを、すべての電源について実際の電力量で確認している担当者は多くないと考えられます。

この確認に使えるデータが、2022年度から公表されています。資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)には、市区町村ごとの需要電力量と逆潮流量が、それぞれ月単位で収録されています。この2つを同じ市区町村で並べると、その町が送電網から受け取った電力量と、送電網へ送り出した電力量を比較できます。

## 送り出しが受け取りを上回る市区町村は、1,741のうち410

使うのは2つのテーブルです。需要電力量（`power_demand_by_municipality`）は、小売電気事業者がその市区町村の需要家へ供給した電力量で、単位はMWhです。逆潮流量（`reverse_power_flow_by_municipality`）は、その市区町村にある発電設備から送電網へ流れ出た電力量で、水力・火力・原子力・風力・地熱・太陽光・バイオマス・蓄電池・その他の電源別に分かれています。発電した場所でそのまま消費される自家消費分は、どちらの値にも含まれず、ここで比較するのは送電網を通った電力量だけです。

収録は2022年4月から2025年3月までの36か月分、1,747市区町村です。政令指定都市は市単位、東京都特別区は区単位で、以下では需要電力量に値のある1,741市区町村を対象にします。

2024年度の全国合計では、需要電力量が831.0TWh、逆潮流量が881.0TWhで、逆潮流量は需要の106.0%です。全国ではほぼ同じ量が送電網を出入りしていますが、市区町村ごとには大きく異なります。1,741のうち410で、年間の逆潮流量が需要電力量を上回りました。全体の23.5%です。

この410を、その町で最も多く送り出している電源で分類しました。分類には上の9電源すべてを使い、最も量の多い1つをその町の電源としています。

```chart
{
  "height": 240,
  "layer": [
    {
      "data": {"name": "by_source"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "towns", "type": "quantitative"},
          {"field": "lead_src", "type": "nominal"}
        ],
        "x": {
          "field": "towns",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "y": {
          "field": "lead_src",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "最大の電源"},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "by_source"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "towns",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "y": {
          "field": "lead_src",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "最大の電源"},
          "sort": null
        },
        "text": {"field": "towns"}
      }
    }
  ]
}
```

最も多いのは水力の166市区町村で、410の4割です。2番目は火力の104で、太陽光は65で3番目です。以下、風力が45、バイオマスが16、原子力が8、地熱が6と続きます。水力・太陽光・風力・バイオマス・地熱を合わせた298市区町村、410の72.7%は、再生可能エネルギーが最大の電源です。

太陽光が最大の電源の町は、送り出す側の町のうち65です。水力が最大の電源の町は、その2.5倍あります。

送り出しの規模には大きな差があります。比率が最も高いのは福井県高浜町で、逆潮流量が需要の34,021%、つまり340倍です。福井県おおい町（31,728%）、北海道厚真町（25,066%）、佐賀県玄海町（23,060%）が続き、上位10市区町村のうち9つは原子力または火力が最大の電源です。平均はこれらの大きな値の影響を受けるので、以下では中央値で比較します。中央値は火力が336.8%、水力が281.9%、風力が246.3%、太陽光が141.7%で、太陽光の町は他の電源の町より需要に近い水準です。

410のうち52市区町村は、比率が100%から110%の範囲にあります。このうち25は火力が最大の電源で、東京都大島町・八丈町、沖縄県宮古島市、長崎県対馬市など、本土の送電網とつながっていない島が大半です。島内の発電所が島内の需要に供給する独立した系統なので、これらの町は域外へ電気を供給しているわけではありません。

## 送り出しが上回る市区町村は、2022年度の373から3年で37増えた

このデータは2022年度から3年度分あります。年度ごとに集計すると、送り出しが上回る市区町村は増えています。

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"fold": ["over_towns", "renewable_towns"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"over_towns\": \"送り出しが上回る市区町村\", \"renewable_towns\": \"うち再生可能エネルギーが最大の電源\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"over_towns\",\"renewable_towns\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "fiscal_year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["送り出しが上回る市区町村", "うち再生可能エネルギーが最大の電源"],
            "range": ["#3b82f6", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["送り出しが上回る市区町村", "うち再生可能エネルギーが最大の電源"]},
        "tooltip": [
          {"field": "fiscal_year", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"fold": ["over_towns", "renewable_towns"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"over_towns\": \"送り出しが上回る市区町村\", \"renewable_towns\": \"うち再生可能エネルギーが最大の電源\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"over_towns\",\"renewable_towns\"], datum.__series)",
          "as": "__order"
        },
        {
          "calculate": "datum[{\"over_towns\":\"over_towns\",\"renewable_towns\":\"renewable_towns\"}[datum.__series]]",
          "as": "__text"
        },
        {"filter": "isValid(datum.__text)"}
      ],
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "fiscal_year",
          "type": "ordinal",
          "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "xOffset": {"field": "__name", "sort": ["送り出しが上回る市区町村", "うち再生可能エネルギーが最大の電源"]},
        "text": {"field": "__text"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

2022年度は373、2023年度は403、2024年度は410でした。3年で37市区町村増えています。同じ期間に再生可能エネルギーが最大の電源である市区町村は258から298へ40増えており、全体の増加数37を上回ります。差の3は、原子力または火力が最大の電源である市区町村が115から112へ減った分です。対象の1,741市区町村は3年度とも同じです。

## 送り出しが上回る市区町村は北海道の55が最も多く、宮崎県は半数が該当する

410市区町村の分布を都道府県別に地図にしました。色が濃いほど、その都道府県で送り出しが上回る市区町村が多いことを表します。

```map
type: map
layers:
  - from: pref_map
    geojson: geojson
    color: over_towns
    label: pref_name
    name: "市区町村数"
lng: 137
lat: 36.5
zoom: 4
```

最も多いのは北海道の55市区町村で、福島県26、長野県24、鹿児島県18、高知県14と続きます。北海道と長野県はもともと市区町村の数が多い県です。宮崎県は26市町村のうち13、つまり半数が該当します。埼玉県と滋賀県はどちらも0で、県内のすべての市区町村が受け取る側です。

## 送り出しが減る季節は、水力は冬、風力は夏、太陽光は冬

最大の電源が水力の166市区町村、風力の45市区町村、太陽光の65市区町村について、それぞれのグループの合計で月ごとの比率を出しました。100%の線は、そのグループ全体で送り出しと受け取りが同じになる水準です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fy_month\"]) && isValid(datum[\"hydro_ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "fy_month", "type": "quantitative"},
          {"field": "hydro_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "fy_month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "hydro_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "逆潮流量 ÷ 需要電力量（%）", "grid": true}
        },
        "color": {
          "datum": "水力の166市区町村",
          "type": "nominal",
          "scale": {
            "domain": ["水力の166市区町村", "風力の45市区町村", "太陽光の65市区町村"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fy_month\"]) && isValid(datum[\"wind_ratio\"]) ? 0 : 1",
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
          {"field": "fy_month", "type": "quantitative"},
          {"field": "wind_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "fy_month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "wind_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "逆潮流量 ÷ 需要電力量（%）", "grid": true}
        },
        "color": {
          "datum": "風力の45市区町村",
          "type": "nominal",
          "scale": {
            "domain": ["水力の166市区町村", "風力の45市区町村", "太陽光の65市区町村"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fy_month\"]) && isValid(datum[\"solar_ratio\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "fy_month", "type": "quantitative"},
          {"field": "solar_ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "fy_month",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "solar_ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "逆潮流量 ÷ 需要電力量（%）", "grid": true}
        },
        "color": {
          "datum": "太陽光の65市区町村",
          "type": "nominal",
          "scale": {
            "domain": ["水力の166市区町村", "風力の45市区町村", "太陽光の65市区町村"],
            "range": ["#22c55e", "#3b82f6", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 100, "type": "quantitative"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

3つのグループは、比率が高い月と低い月が異なります。水力の町は7月の465.46%が最も高く、2月の190.58%が最も低く、春から夏にかけて高く、冬に下がります。風力の町は12月の366.37%が最も高く、8月の145.59%が最も低くなっています。風力の町が最も低い8月は、水力の町も314.8%まで下がる一方、太陽光の町は152.85%と年間でも高い水準です。

変動の大きさも電源で違います。水力と風力の町は最も低い月でも需要の1.9倍から1.5倍を送り出しており、年間を通じて送り出す側です。太陽光の町は5月の201.51%から1月の99.96%まで下がり、1月だけを見ると受け取る側になります。年間の合計では上回っていても、月によっては受け取る側になる水準です。

区域内の再エネ導入量を設備容量で合計しても、この季節による違いは分かりません。年間の合計で送り出しが上回っていても、どの月にどれだけ減るかは主な電源によって決まります。地域新電力のように区域内の電源から区域内へ供給する仕組みを検討するときは、送り出しが減る季節にどこから電気を調達するかを決める必要があります。

## 業務での使い方

- 自分の自治体が送り出す側か受け取る側かを、実際に送電網を流れた電力量で確認する。区域施策編で再エネ導入量の目標を立てるときの基礎になります
- 区域内で最も多く送り出している電源を特定し、その電源の送り出しが減る季節を月別に把握する。太陽光が主な電源なら冬、水力なら冬から早春、風力なら夏です
- 隣接する市区町村の月別の値と並べて、送り出しが減る季節が互いに異なるかを確認する。都道府県単位の集計では分からない組み合わせが見つかります

## データの出典

本記事は資源エネルギー庁[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)の統計表6-(1)「市町村別需要電力量」と6-(2)「市町村別逆潮流量」を、2026年8月27日時点で集計しています。収録期間は2022年4月から2025年3月までの36か月で、年度は4月始まりです。数値の単位はMWhです。都道府県の地図は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、資源エネルギー庁や国土交通省のオープンデータを、列名・単位・文字コードを統一し、テーブルの構成や集計の単位をメタデータとして付けて公開しています。本記事で使った[市町村別逆潮流量テーブル](/datasets/queria/enecho/electric_power/reverse_power_flow_by_municipality)と[市町村別需要電力量テーブル](/datasets/queria/enecho/electric_power/power_demand_by_municipality)から、担当する市区町村の月別の実績を確認できます。

```sql id=by_source
WITH d AS (SELECT pref_code, pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), r AS (SELECT pref_code, municipality_name, SUM(total_mwh) AS rev, SUM(solar_mwh) AS solar, SUM(wind_mwh) AS wind, SUM(hydro_mwh) AS hydro, SUM(thermal_mwh) AS thermal, SUM(biomass_mwh) AS bio, SUM(geothermal_mwh) AS geo, SUM(nuclear_mwh) AS nuc, SUM(storage_battery_mwh) AS batt, SUM(other_mwh) AS oth FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), j AS (SELECT r.rev / d.demand * 100 AS ratio, CASE greatest(r.solar, r.wind, r.hydro, r.thermal, r.bio, r.geo, r.nuc, r.batt, r.oth) WHEN r.hydro THEN '水力' WHEN r.thermal THEN '火力' WHEN r.solar THEN '太陽光' WHEN r.wind THEN '風力' WHEN r.bio THEN 'バイオマス' WHEN r.nuc THEN '原子力' WHEN r.geo THEN '地熱' END AS lead_src FROM d JOIN r USING (pref_code, municipality_name) WHERE d.demand > 0 AND r.rev > d.demand) SELECT lead_src, count(*) AS towns, CAST(round(median(ratio), 1) AS DOUBLE) AS median_ratio FROM j GROUP BY lead_src ORDER BY towns, lead_src
```

```sql id=trend
WITH d AS (SELECT fiscal_year, pref_code, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality GROUP BY 1, 2, 3), r AS (SELECT fiscal_year, pref_code, municipality_name, SUM(total_mwh) AS rev, SUM(solar_mwh) AS solar, SUM(wind_mwh) AS wind, SUM(hydro_mwh) AS hydro, SUM(thermal_mwh) AS thermal, SUM(biomass_mwh) AS bio, SUM(geothermal_mwh) AS geo, SUM(nuclear_mwh) AS nuc FROM enecho.electric_power.reverse_power_flow_by_municipality GROUP BY 1, 2, 3) SELECT d.fiscal_year, count(*) AS total_towns, count(*) FILTER (WHERE r.rev > d.demand) AS over_towns, count(*) FILTER (WHERE r.rev > d.demand AND greatest(r.solar, r.wind, r.hydro, r.bio, r.geo) > greatest(r.thermal, r.nuc)) AS renewable_towns FROM d JOIN r USING (fiscal_year, pref_code, municipality_name) WHERE d.demand > 0 GROUP BY d.fiscal_year ORDER BY d.fiscal_year
```

```sql id=pref_map
WITH d AS (SELECT pref_code, pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), r AS (SELECT pref_code, municipality_name, SUM(total_mwh) AS rev FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), p AS (SELECT d.pref_name, count(*) AS towns, count(*) FILTER (WHERE r.rev > d.demand) AS over_towns FROM d JOIN r USING (pref_code, municipality_name) WHERE d.demand > 0 GROUP BY d.pref_name) SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, p.over_towns, p.towns, p.pref_name FROM nlftp.boundary.prefecture b JOIN p ON b.prefecture_name = p.pref_name ORDER BY p.over_towns DESC, p.pref_name
```

```sql id=monthly
WITH dm AS (SELECT pref_code, municipality_name, month, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), rm AS (SELECT pref_code, municipality_name, month, SUM(total_mwh) AS rev FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), dy AS (SELECT pref_code, municipality_name, SUM(demand) AS demand FROM dm GROUP BY 1, 2), ry AS (SELECT pref_code, municipality_name, SUM(total_mwh) AS rev, SUM(solar_mwh) AS solar, SUM(wind_mwh) AS wind, SUM(hydro_mwh) AS hydro, SUM(thermal_mwh) AS thermal, SUM(biomass_mwh) AS bio, SUM(geothermal_mwh) AS geo, SUM(nuclear_mwh) AS nuc, SUM(storage_battery_mwh) AS batt, SUM(other_mwh) AS oth FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), lead AS (SELECT dy.pref_code, dy.municipality_name, CASE greatest(ry.solar, ry.wind, ry.hydro, ry.thermal, ry.bio, ry.geo, ry.nuc, ry.batt, ry.oth) WHEN ry.hydro THEN '水力' WHEN ry.thermal THEN '火力' WHEN ry.solar THEN '太陽光' WHEN ry.wind THEN '風力' ELSE 'その他' END AS lead_src FROM dy JOIN ry USING (pref_code, municipality_name) WHERE dy.demand > 0 AND ry.rev > dy.demand) SELECT (dm.month + 8) % 12 + 1 AS fy_month, dm.month, CAST(round(SUM(rm.rev) FILTER (WHERE l.lead_src = '太陽光') / SUM(dm.demand) FILTER (WHERE l.lead_src = '太陽光') * 100, 2) AS DOUBLE) AS solar_ratio, CAST(round(SUM(rm.rev) FILTER (WHERE l.lead_src = '風力') / SUM(dm.demand) FILTER (WHERE l.lead_src = '風力') * 100, 2) AS DOUBLE) AS wind_ratio, CAST(round(SUM(rm.rev) FILTER (WHERE l.lead_src = '水力') / SUM(dm.demand) FILTER (WHERE l.lead_src = '水力') * 100, 2) AS DOUBLE) AS hydro_ratio FROM lead l JOIN dm USING (pref_code, municipality_name) JOIN rm ON rm.pref_code = l.pref_code AND rm.municipality_name = l.municipality_name AND rm.month = dm.month GROUP BY dm.month ORDER BY fy_month
```

```sql id=national
WITH d AS (SELECT pref_code, pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), r AS (SELECT pref_code, municipality_name, SUM(total_mwh) AS rev, SUM(solar_mwh) AS solar, SUM(wind_mwh) AS wind, SUM(hydro_mwh) AS hydro, SUM(thermal_mwh) AS thermal, SUM(biomass_mwh) AS bio, SUM(geothermal_mwh) AS geo, SUM(nuclear_mwh) AS nuc, SUM(storage_battery_mwh) AS batt, SUM(other_mwh) AS oth FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), j AS (SELECT d.demand, r.rev, r.rev / d.demand * 100 AS ratio, CASE greatest(r.solar, r.wind, r.hydro, r.thermal, r.bio, r.geo, r.nuc, r.batt, r.oth) WHEN r.hydro THEN '水力' WHEN r.thermal THEN '火力' WHEN r.solar THEN '太陽光' WHEN r.wind THEN '風力' WHEN r.bio THEN 'バイオマス' WHEN r.nuc THEN '原子力' WHEN r.geo THEN '地熱' END AS lead_src FROM d JOIN r USING (pref_code, municipality_name) WHERE d.demand > 0) SELECT count(*) AS total_towns, count(*) FILTER (WHERE ratio > 100) AS over_towns, CAST(round(SUM(demand) / 1000000, 1) AS DOUBLE) AS demand_twh, CAST(round(SUM(rev) / 1000000, 1) AS DOUBLE) AS reverse_twh, CAST(round(SUM(rev) / SUM(demand) * 100, 1) AS DOUBLE) AS national_ratio, count(*) FILTER (WHERE ratio > 100 AND ratio <= 110) AS band_towns, count(*) FILTER (WHERE ratio > 100 AND ratio <= 110 AND lead_src = '火力') AS band_thermal_towns FROM j
```

```sql id=extremes
WITH d AS (SELECT pref_code, pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), r AS (SELECT pref_code, municipality_name, SUM(total_mwh) AS rev, SUM(solar_mwh) AS solar, SUM(wind_mwh) AS wind, SUM(hydro_mwh) AS hydro, SUM(thermal_mwh) AS thermal, SUM(biomass_mwh) AS bio, SUM(geothermal_mwh) AS geo, SUM(nuclear_mwh) AS nuc, SUM(storage_battery_mwh) AS batt, SUM(other_mwh) AS oth FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2) SELECT d.pref_name, d.municipality_name, CAST(round(r.rev / d.demand * 100) AS BIGINT) AS ratio, CASE greatest(r.solar, r.wind, r.hydro, r.thermal, r.bio, r.geo, r.nuc, r.batt, r.oth) WHEN r.hydro THEN '水力' WHEN r.thermal THEN '火力' WHEN r.solar THEN '太陽光' WHEN r.wind THEN '風力' WHEN r.bio THEN 'バイオマス' WHEN r.nuc THEN '原子力' WHEN r.geo THEN '地熱' END AS lead_src FROM d JOIN r USING (pref_code, municipality_name) WHERE d.demand > 0 ORDER BY r.rev / d.demand DESC, d.municipality_name LIMIT 10
```

```sql id=band
WITH d AS (SELECT pref_code, pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), r AS (SELECT pref_code, municipality_name, SUM(total_mwh) AS rev, SUM(solar_mwh) AS solar, SUM(wind_mwh) AS wind, SUM(hydro_mwh) AS hydro, SUM(thermal_mwh) AS thermal, SUM(biomass_mwh) AS bio, SUM(geothermal_mwh) AS geo, SUM(nuclear_mwh) AS nuc, SUM(storage_battery_mwh) AS batt, SUM(other_mwh) AS oth FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), j AS (SELECT d.pref_name, d.municipality_name, r.rev / d.demand * 100 AS ratio, CASE greatest(r.solar, r.wind, r.hydro, r.thermal, r.bio, r.geo, r.nuc, r.batt, r.oth) WHEN r.hydro THEN '水力' WHEN r.thermal THEN '火力' WHEN r.solar THEN '太陽光' WHEN r.wind THEN '風力' WHEN r.bio THEN 'バイオマス' WHEN r.nuc THEN '原子力' WHEN r.geo THEN '地熱' END AS lead_src FROM d JOIN r USING (pref_code, municipality_name) WHERE d.demand > 0) SELECT pref_name, municipality_name, CAST(round(ratio, 1) AS DOUBLE) AS ratio FROM j WHERE ratio > 100 AND ratio <= 110 AND lead_src = '火力' ORDER BY ratio DESC, municipality_name
```

```sql id=coverage
SELECT min(year_month) AS first_month, max(year_month) AS last_month, count(DISTINCT year_month) AS months, min(fiscal_year) AS first_fy, max(fiscal_year) AS last_fy, CAST(count(*) / count(DISTINCT year_month) AS BIGINT) AS municipalities FROM enecho.electric_power.reverse_power_flow_by_municipality
```
