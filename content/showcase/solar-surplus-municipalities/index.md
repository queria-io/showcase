---
title: 地元で使う量より多くの太陽光の電気を送り出している市区町村が、全国に63あります
description: 資源エネルギー庁の市町村別データで、太陽光が系統に送り出した電気を地域の電力需要と比較しました。2024年度に需要を上回ったのは63市区町村で、全国の需要の0.66%のこの地域から、太陽光の電気の8.8%が送り出されています。
publishedAt: 2026-08-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 再生可能エネルギー
  - 太陽光
  - 電力
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
agentHint: reverse_power_flow_by_municipality の風力（wind_mwh）とバイオマス（biomass_mwh）についても、市区町村ごとに power_demand_by_municipality の需要電力量と比べて、2024年度に需要を上回った市区町村を出して
socialAnnounce: |-
  市区町村ごとに、太陽光が系統に送り出した電気と地域の電力需要を並べました。

  2024年度に需要を上回ったのは63市区町村。5月は需要の2.1倍、1月は0.97倍です。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2024年度に、太陽光の設備から系統へ送り出された電気が、その地域に供給された電気を上回った市区町村は63ありました。最も多い岩手県軽米町では、町に供給された電気の4.7倍です。63市区町村に供給された電気は全国の0.66%ですが、系統に流れ込んだ太陽光の電気の8.8%はここから出ています。

自治体で再生可能エネルギーの導入計画を担当する人は、地域の太陽光を設備容量（kW）で把握することが多いですが、容量からは、その設備が送り出している電気が地域で使っている電気に対してどれくらいかは分かりません。資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)には、2022年度から市区町村別の統計表が2つ加わっています。ひとつは市区町村ごとに小売電気事業者が供給した需要電力量、もうひとつは市区町村ごとに発電設備から系統へ流れ出た電力量（逆潮流量）を電源別に分けたものです。どちらも月ごとで、単位はMWh（1,000kWh）なので、一方を他方で割って比率を計算できます。

## 比率が最も高い軽米町では、需要の4.7倍の太陽光の電気を送り出している

この記事では次の2つのテーブルを使います。

| テーブル                             | 収録内容                                                                                                                                 |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `power_demand_by_municipality`       | 市町村別需要電力量。特別高圧・高圧をまとめた列（`extra_high_and_high_demand_mwh`）、低圧（`low_demand_mwh`）、合計（`total_demand_mwh`） |
| `reverse_power_flow_by_municipality` | 市町村別逆潮流量。水力・火力・原子力・風力・地熱・太陽光・バイオマス・蓄電池・その他の電源別（太陽光は `solar_mwh`）                     |

どちらも市区町村×月の1行で、政令指定都市は市単位、東京都の特別区は区単位です。需要電力量の表にある1,746市区町村について、太陽光の逆潮流量（`solar_mwh`）を、同じ市区町村の需要電力量の合計（`total_demand_mwh`）で割った比率を計算します。

逆潮流量は系統に流れ込んだ電気だけを集計していて、屋根の上で発電してその場で使った分は含みません。需要電力量も小売電気事業者が供給した量なので、自家消費は含みません。この比率は、系統を通って出入りした電気どうしの比較です。

2024年度でこの比率を計算し、高いほうから20市区町村を並べたのが次の図です。破線が100%、つまり送り出した太陽光の電気と、その市区町村に供給された電気がちょうど同じ量になる線です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "top"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "area", "type": "nominal"},
          {"field": "muni", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "muni",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": -45},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "太陽光の逆潮流量 ÷ 需要電力量（%）", "grid": true}
        }
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
  ]
}
```

最も高いのは岩手県軽米町の472.2%です。町に供給された電気の4.7倍にあたる量の太陽光の電気が、町内の設備から系統へ流れ出ています。上位20には福島県の富岡町（432.6%）・川内村（366.1%）・浪江町（365.7%）・鮫川村（317.1%）・飯舘村（242.5%）・小野町（193.6%）と、同じ県から6つが入っています。

比率が高い市区町村が、送り出している電気の量も多いとは限りません。上位20の太陽光逆潮流量は群馬県神流町の21,154MWhから岡山県美作市の439,691MWhまで20倍以上の差があります。比率は分母の需要が小さいときにも高くなるので、人口の少ない町村に大きな発電設備が1つできると、比率は大きく上がります。

## 需要の0.66%の地域から、太陽光の8.8%が出ている

2024年度に比率が100%を超えたのは63市区町村です。この63市区町村に供給された電気は全国の0.66%ですが、系統に流れ込んだ太陽光の電気の8.8%はここから出ています。1,746市区町村を合計すると、太陽光の逆潮流量は92.5TWh、需要電力量は831.0TWhで、比率は11.1%です。

収録されているのは2022年度からの3年度分で、100%を超えた市区町村は56（2022年度）・58（2023年度）・63（2024年度）と増えました。50%を超えた市区町村は148・174・183で、全国の比率も9.9%・11.0%・11.1%と上がっています。3年間の変化は大きくありませんが、どの値も毎年上がっています。

同じ比率を都道府県単位で計算しました。

```map
type: map
layers:
  - from: pref
    geojson: geojson
    color: pct
    label: pref
    name: "太陽光 ÷ 需要（%）"
lng: 137
lat: 36.5
zoom: 4
```

高いのは鹿児島県（31.2%）・福島県（30.0%）・宮崎県（29.2%）・茨城県（28.1%）・栃木県（27.6%）です。低いのは東京都（0.7%）・神奈川県（1.9%）・大阪府（2.2%）で、上位と下位では40倍以上の差があります。都市部は需要が大きく、まとまった設置場所も少ないため、この比率が低くなると考えられます。

## 63市区町村の合計は5月・6月に需要の2倍を超え、1月には97.3%に下がる

電気は発電と同時に使われるので、需給の関係は月ごとに確認する必要があります。100%を超えた63市区町村を合計して、月別の比率を全国と並べたのが次の図です。値が10倍以上違うので、縦軸は対数目盛にしています。線の傾きが同じなら、増え方・減り方も同じです。破線は先ほどと同じ100%の線です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "monthly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"seq\"]) && isValid(datum[\"pct_surplus\"]) ? 0 : 1",
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
          {"field": "seq", "type": "quantitative"},
          {"field": "pct_surplus", "type": "quantitative"}
        ],
        "x": {
          "field": "seq",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月（2024年度）", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "pct_surplus",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "太陽光の逆潮流量 ÷ 需要電力量（%）", "grid": true}
        },
        "color": {
          "datum": "需要を上回った63市区町村",
          "type": "nominal",
          "scale": {"domain": ["需要を上回った63市区町村", "全国"], "range": ["#f97316", "#94a3b8"]},
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
          "calculate": "isValid(datum[\"seq\"]) && isValid(datum[\"pct_all\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "seq", "type": "quantitative"},
          {"field": "pct_all", "type": "quantitative"}
        ],
        "x": {
          "field": "seq",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "月（2024年度）", "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        },
        "y": {
          "field": "pct_all",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "太陽光の逆潮流量 ÷ 需要電力量（%）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {"domain": ["需要を上回った63市区町村", "全国"], "range": ["#f97316", "#94a3b8"]},
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
        "y": {"datum": 2, "type": "quantitative"}
      }
    }
  ]
}
```

63市区町村の合計は5月に212.0%、6月に211.8%と需要の2倍を超え、そこから下がって1月には97.3%になります。年度の合計では需要を上回っている地域でも、1月は合計で需要を下回ります。全国の系列も形は同じで、6月の15.9%が最も高く、1月の7.5%が最も低くなります。

この上下は日射の強さだけでは説明できません。63市区町村が送り出した太陽光の電気は5月に829,742MWh、8月に834,936MWhとほとんど同じですが、比率は212.0%から165.0%に下がります。分母の需要が5月の391,419MWhから8月の506,079MWhへ3割ほど増えるためです。冷暖房で需要が増える夏と冬は、発電量が同じでも比率が下がり、冷暖房を使わない5月・6月に、送り出す電気と使う電気の差が最も大きくなります。

## 業務での使い方

- 蓄電池や電気を使う設備の設置場所を検討するときに、年間の比率に加えて月別の変動で候補地を絞り込めます。年間の比率が同じでも、5月・6月に2倍を超えて1月には100%を下回る地域では、発電した電気を時間や季節をずらして使う設備の効果が大きくなります
- 地域新電力や再エネの地産地消の計画で、地域の需要のうちどれだけを地域の太陽光で賄えているかを、推計ではなく公表統計の値で示せます。同じ表から月別の値も計算できるので、冬の不足も示せます
- 2022年度からの3年度分が同じ定義で集計されているので、補助や誘導策を始めた前後で比率がどう変わったかを確認できます

## データの出典

本記事は経済産業省 資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)から、市町村別需要電力量（`power_demand_by_municipality`）と市町村別逆潮流量（`reverse_power_flow_by_municipality`）を2026年8月11日時点で集計しています。収録範囲は2022年度から2024年度までの3年度分で、値はいずれも月ごとのMWhです。都道府県の地図は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、資源エネルギー庁や国土交通省のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[市町村別逆潮流量](/datasets/queria/enecho/electric_power/reverse_power_flow_by_municipality)と[市町村別需要電力量](/datasets/queria/enecho/electric_power/power_demand_by_municipality)は同じ市区町村と月で結合できるので、自分の市区町村の比率を月ごとに計算できます。

```sql id=top
WITH r AS (SELECT pref_name, municipality_name, SUM(solar_mwh) AS solar FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), d AS (SELECT pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), j AS (SELECT d.municipality_name AS muni, d.pref_name || ' ' || d.municipality_name AS area, r.solar AS solar, d.demand AS demand, r.solar / d.demand * 100 AS pct, ROW_NUMBER() OVER (ORDER BY r.solar / d.demand DESC, d.municipality_name) AS rn FROM d JOIN r USING (pref_name, municipality_name) WHERE d.demand > 0) SELECT muni, area, ROUND(pct, 1) AS pct, ROUND(solar) AS solar_mwh, ROUND(demand) AS demand_mwh FROM j WHERE rn <= 20 ORDER BY rn
```

```sql id=share
WITH r AS (SELECT pref_name, municipality_name, SUM(solar_mwh) AS solar FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), d AS (SELECT pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2), j AS (SELECT COALESCE(r.solar, 0) AS solar, d.demand AS demand FROM d LEFT JOIN r USING (pref_name, municipality_name)) SELECT COUNT(*) AS munis, COUNT(*) FILTER (WHERE solar > demand) AS over100, ROUND(SUM(solar) FILTER (WHERE solar > demand) / SUM(solar) * 100, 1) AS solar_share_pct, ROUND(SUM(demand) FILTER (WHERE solar > demand) / SUM(demand) * 100, 2) AS demand_share_pct, ROUND(SUM(solar) / 1000000, 1) AS solar_twh, ROUND(SUM(demand) / 1000000, 1) AS demand_twh FROM j
```

```sql id=yearly
WITH r AS (SELECT fiscal_year, pref_name, municipality_name, SUM(solar_mwh) AS solar FROM enecho.electric_power.reverse_power_flow_by_municipality GROUP BY 1, 2, 3), d AS (SELECT fiscal_year, pref_name, municipality_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality GROUP BY 1, 2, 3), j AS (SELECT d.fiscal_year AS fiscal_year, COALESCE(r.solar, 0) AS solar, d.demand AS demand FROM d LEFT JOIN r USING (fiscal_year, pref_name, municipality_name) WHERE d.demand > 0) SELECT fiscal_year, COUNT(*) FILTER (WHERE solar > demand) AS over100, COUNT(*) FILTER (WHERE solar > demand * 0.5) AS over50, ROUND(SUM(solar) / SUM(demand) * 100, 1) AS national_pct FROM j GROUP BY 1 ORDER BY 1
```

```sql id=pref
WITH r AS (SELECT pref_name, SUM(solar_mwh) AS solar FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1), d AS (SELECT pref_name, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1) SELECT ST_AsGeoJSON(ST_Simplify(p.geometry, 0.01)) AS geojson, p.prefecture_name AS pref, ROUND(r.solar / d.demand * 100, 1) AS pct FROM nlftp.boundary.prefecture p JOIN r ON r.pref_name = p.prefecture_name JOIN d ON d.pref_name = p.prefecture_name ORDER BY p.prefecture_name
```

```sql id=monthly
WITH r AS (SELECT pref_name, municipality_name, month, SUM(solar_mwh) AS solar FROM enecho.electric_power.reverse_power_flow_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), d AS (SELECT pref_name, municipality_name, month, SUM(total_demand_mwh) AS demand FROM enecho.electric_power.power_demand_by_municipality WHERE fiscal_year = 2024 GROUP BY 1, 2, 3), j AS (SELECT d.pref_name AS pref_name, d.municipality_name AS municipality_name, d.month AS month, COALESCE(r.solar, 0) AS solar, d.demand AS demand FROM d LEFT JOIN r USING (pref_name, municipality_name, month)), y AS (SELECT pref_name, municipality_name, TRUE AS surplus FROM j GROUP BY 1, 2 HAVING SUM(solar) > SUM(demand)) SELECT CASE WHEN j.month >= 4 THEN j.month - 3 ELSE j.month + 9 END AS seq, printf('%d月', j.month) AS label, ROUND(SUM(j.solar) FILTER (WHERE y.surplus) / SUM(j.demand) FILTER (WHERE y.surplus) * 100, 1) AS pct_surplus, ROUND(SUM(j.solar) / SUM(j.demand) * 100, 1) AS pct_all, ROUND(SUM(j.solar) FILTER (WHERE y.surplus)) AS solar_surplus_mwh, ROUND(SUM(j.demand) FILTER (WHERE y.surplus)) AS demand_surplus_mwh FROM j LEFT JOIN y USING (pref_name, municipality_name) GROUP BY 1, 2 ORDER BY 1
```
