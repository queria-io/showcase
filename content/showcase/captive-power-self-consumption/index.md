---
title: 山口県では、工場が自分で作って使う電気が、電力会社の販売量の7割にあたる
description: 資源エネルギー庁の電力調査統計から、自家用発電所が2025年度に発電した電力量を都道府県別に集計しました。自家消費された電力量は全国では小売電気事業者の販売量の7.5%ですが、山口県では69.8%です。秋田県の自家用発電所は発電量の62.9%が風力で、72.6%を外へ送っています。
ogDescription: 自家用発電所が2025年度に自家消費した電力量は、山口県では小売電気事業者の販売量の69.8%、全国では7.5%でした。
publishedAt: 2026-09-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 電力
  - 自家発電
  - 企業立地
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
agentHint: enecho.electric_power.captive_power_generation_by_prefecture から、自分の県の自家用発電所の発電量を原動力別・月別に出して。自家消費電力量と送電電力量の内訳も月ごとに比べて
socialAnnounce: |-
  資源エネルギー庁の電力調査統計から、自家用発電所の実績を都道府県別に集計しました。

  自家消費された電力量は、山口県では小売電気事業者の販売量の69.8%にあたります。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2025年度に工場などの自家用発電所が発電し、そのまま自分で使った電力量は、全国で61,060GWhでした。小売電気事業者が販売した電力量の7.5%にあたります。この割合は県によって大きく異なり、山口県では69.8%、東京都では0.7%です。秋田県の自家用発電所は発電量の62.9%が風力で、発電量の72.6%を敷地の外へ送っています。

企業誘致の資料で電力を説明するときは、電力会社が県内で販売した電力量の統計を使うのが一般的です。工場が自分の敷地で発電してそのまま使う電気は、電力会社との売買がないので、この統計には含まれません。この記事では、その電力量を都道府県別に集計しました。

## 自家用発電所が発電した電気の64.3%は、発電した事業者が自分で使っている

使ったのは、経済産業省 資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)にある「自家用発電所等実績」です。自家用発電所は、電気を売る事業のためではなく、自らの需要のために発電する設備です。工場の屋根に載せた小規模な太陽光の自家消費や、家庭の設備は含みません。

このテーブルには、都道府県・月・原動力ごとに、発電した電力量とその行き先が記録されています。発電した電気は3つに分かれます。

| 区分               | 意味                                                 |
| ------------------ | ---------------------------------------------------- |
| 自家消費電力量     | 発電した事業者が自分で使った分                       |
| 所内及び損失電力量 | 発電所そのものの運転に使った分と送る途中で失われた分 |
| 送電電力量         | 発電所の外へ送った分                                 |

2025年度（2025年4月〜2026年3月）の全国の合計は94,949GWhでした。このうち61,060GWhが自家消費、7,825GWhが所内及び損失、26,064GWhが送電です。発電した電気の64.3%は、発電した事業者が自分で使っています。

同じ年度に小売電気事業者が全国で供給した電力需要量は817,450GWhです。自家消費された61,060GWhはこの量に含まれないので、両者を合計しても重複しません。全国では、小売販売量の7.5%にあたる電気が、電力会社を通らずに発電され、使われていました。

## 山口県では小売販売量の69.8%、東京都では0.7%

自家消費された電力量が、その県で小売電気事業者が販売した電力量の何%にあたるかを地図にしました。色が濃いほど、電力会社を通らない電気の比重が大きい県です。

```map
type: map
layers:
  - from: map
    geojson: geojson
    color: pct
    label: pref_name
    name: "小売販売量に対する割合（%）"
lng: 137
lat: 36.5
zoom: 4
```

色の濃い県は臨海部に多くあります。割合の高い順に並べると、県ごとの差は次のとおりです。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "自家消費量／小売販売量（%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "自家消費量／小売販売量（%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "自家消費量／小売販売量（%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは山口県の69.8%です。県内で小売電気事業者が販売した電力量の7割にあたる電気を、工場などが自分で発電して使っています。岡山県が40.1%、広島県が30.5%、和歌山県が23.7%で続きます。いずれも臨海部に大規模な工場が集まる県です。

最も低いのは沖縄県と奈良県の0.4%で、石川県が0.5%、東京都が0.7%です。上位と下位では100倍以上の差があるので、全国の7.5%という値は、どの県の状況も表していません。

企業誘致の資料に「県内の電力需要」として電力会社の販売量を載せると、東京都ではほぼ県内の電気の使用量を表しますが、山口県では自家消費の分が大きく抜け落ちます。

## 火力中心の山口県は発電量の18.7%を、風力中心の秋田県は72.6%を外へ送っている

自家用発電所の統計には、原動力別の内訳もあります。2025年度の全国の内訳は次のとおりです。

```sql
SELECT CASE WHEN power_source_group = '火力' THEN '火力（計）' WHEN power_source_group = '新エネルギー' AND power_source_name = '計' THEN '新エネルギー（計）' ELSE power_source_name END AS '電源', ROUND(SUM(generation_mwh) / 1000) AS '発電量(GWh)', ROUND(SUM(generation_mwh) / (SELECT SUM(generation_mwh) FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計') * 100, 1) AS '構成比(%)' FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND ((power_source_group = '火力' AND power_source_name = '計') OR (power_source_group = '新エネルギー' AND power_source_name IN ('計', '太陽光', '風力', '地熱', 'バイオマス')) OR power_source_group = '水力') GROUP BY 1 ORDER BY 2 DESC
```

全国では火力が82,223GWhで86.6%を占めます。新エネルギーの計は18,988GWhで20.0%です。この表は計と内訳を同じ列に並べているので、構成比を合計すると100%を超えます。また、バイオマスの8,076GWhは新エネルギーの計と火力の計の両方に含まれています。以下では、重複しない太陽光・風力・地熱の3つを合わせた割合を「太陽光・風力・地熱の割合」と呼びます。全国では10,911GWhで、合計の11.5%です。

電源の構成は、発電した電気の行き先と関係しています。横軸に太陽光・風力・地熱の割合、縦軸に発電量のうち外へ送った割合を取り、都道府県を並べました。円の大きさは発電量です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "mix"},
      "mark": {"type": "point", "color": "#3b82f6", "opacity": 0.65, "filled": true, "size": 36},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "vre_pct", "type": "quantitative"},
          {"field": "tx_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "vre_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "太陽光・風力・地熱の割合（%）", "grid": true}
        },
        "y": {
          "field": "tx_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "発電量のうち外へ送った割合（%）", "grid": true}
        },
        "size": {
          "field": "bubble",
          "type": "quantitative",
          "legend": null,
          "scale": {"range": [16, 900]}
        }
      }
    }
  ]
}
```

都道府県は、左下と右上の2つのグループに分かれます。

左下にあるのは山口県です。発電量は9,500.8GWhで全国最大で、そのうち87.6%が石炭を燃料とする火力です。太陽光・風力・地熱は2.9%です。外へ送るのは18.7%で、残りは自分で使います。岡山県（太陽光・風力・地熱2.2%、外へ送る割合23.5%）と愛知県（3.2%、20.8%）も同じ位置にあります。これらの県の設備は、工場が自分の使う熱と電気をまかなうために置いたものなので、発電した電気の大半を敷地の中で使っています。

右上にあるのは秋田県です。発電量は502.3GWhで山口県の19分の1ですが、太陽光・風力・地熱が70.9%を占め、そのうち風力が62.9%です。発電量の72.6%を外へ送っています。外へ送る割合が最も高いのは高知県の83.6%で、熊本県が76.1%、山形県が75.2%で続きます。これらの県の自家用発電所は、発電した電気の大半を敷地の外へ送っています。

企業誘致では、2つのグループは別の情報を示します。左下の県には、電気を大量に使う産業がすでに集まっていて、その電気を自分で発電する設備があります。右上の県では、自家用として登録された再生可能エネルギーの設備が、系統に電気を供給しています。

## 茨城県では、送電量の68.4%が特定供給の相手方に送られている

外へ送られた電気は、送電先によって、電気事業者への送電、特定供給の相手方への送電、その他の事業者への送電の3つに分かれます。特定供給は、生産工程・資本関係・人的関係などで密接な関係にある相手方へ電気を供給することです。同じ構内や隣の敷地にある別の会社へ、電力会社を通さずに電気を送る場合がこれにあたります。

全国では、送電された26,064GWhのうち21,025GWhが電気事業者へ、4,899GWhが特定供給の相手方へ送られています。送電量の多い15県について内訳を示します。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "dest"},
      "transform": [
        {"fold": ["util_gwh", "spec_gwh", "other_gwh"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"util_gwh\": \"電気事業者へ\", \"spec_gwh\": \"特定供給の相手方へ\", \"other_gwh\": \"その他の事業者へ\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"util_gwh\",\"spec_gwh\",\"other_gwh\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "送電電力量（GWh）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {
            "domain": ["電気事業者へ", "特定供給の相手方へ", "その他の事業者へ"],
            "range": ["#3b82f6", "#22c55e", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

送電量が最も多いのは広島県の2,578.2GWhで、そのうち2,578.1GWhが電気事業者向けです。特定供給はありません。2位の茨城県は2,222.3GWhのうち1,519.6GWhが特定供給で、送電量の68.4%を占めます。山口県は1,780.9GWhのうち870.1GWh、愛知県は1,673.4GWhのうち849.3GWhが特定供給です。この3県で、全国の特定供給4,899GWhの66%を占めます。

岡山県は1,921.8GWhを送電していますが、特定供給は13.0GWhです。送電量が同じ程度でも、電気事業者に送るか特定供給の相手方に送るかは県によって異なります。

特定供給が多い県では、同じ敷地の中にある複数の企業が電気を融通し合っています。産業用地の問い合わせに答えるとき、系統から電気を買う以外の調達方法がその土地にあるかを判断する材料になります。

## 企業誘致の資料での使い方

- 自県の「電力需要」に、自家消費されている電力量を並べて示せます。山口県のように、電力会社の販売量だけでは県内で使われている電気の量を説明できない県があります
- 誘致する産業を検討するとき、自家用発電所の電源構成を参考にできます。火力が中心の県には熱と電気を大量に使う産業がすでにあり、太陽光・風力が中心の県には発電事業が立地しています
- 特定供給の量が多い県には、構内で電気を融通し合う企業がすでにあります。特定供給の相手方は資本関係などで密接な関係にある事業者に限られるので、グループ会社や取引先と一緒に進出する問い合わせで、その方法を取れる地区かどうかを判断する材料になります
- 月ごとのデータがあるので、季節による変動や大きな設備の増減を追えます。県全体の水準がいつ変わったかを確認できます

## データの出典

本記事は経済産業省 資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)のうち、統計表5「自家用発電所等実績」と統計表3-(2)「都道府県別電力需要実績」を2026年9月5日時点で集計しています。自家用発電所の都道府県別のデータは2024年4月から2026年3月までで、本記事はこのうち2025年度（2025年4月〜2026年3月）の12か月を対象にしています。電力量の単位はいずれもMWhで、本文と図では1,000で割ったGWhで表示しています。都道府県の地図は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、原典で月ごと・原動力ごとのExcelに分かれている自家用発電所の実績を、都道府県コードと年月を列にした1つのテーブルにまとめ、合計・内訳・再掲の区別をメタデータに記載して公開しています。本記事で使った[自家用発電所の実績テーブル](/datasets/queria/enecho/electric_power/captive_power_generation_by_prefecture)と[都道府県別電力需要テーブル](/datasets/queria/enecho/electric_power/power_demand_by_prefecture)から、自分の県の数字を月単位で確認したり、原動力別の内訳を追ったりできます。

```sql id=national
WITH c AS (SELECT SUM(generation_mwh) AS gen, SUM(self_consumption_mwh) AS self_used, SUM(station_use_and_loss_mwh) AS loss, SUM(transmission_total_mwh) AS tx, SUM(transmission_to_utilities_mwh) AS to_util, SUM(transmission_to_specified_supply_mwh) AS to_spec FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計'), d AS (SELECT SUM(total_demand_mwh) AS dem FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year = 2025) SELECT ROUND(c.gen / 1000) AS gen_gwh, ROUND(c.self_used / 1000) AS self_gwh, ROUND(c.loss / 1000) AS loss_gwh, ROUND(c.tx / 1000) AS tx_gwh, ROUND(c.to_util / 1000) AS to_util_gwh, ROUND(c.to_spec / 1000) AS to_spec_gwh, ROUND(d.dem / 1000) AS demand_gwh, ROUND(c.self_used / d.dem * 100, 1) AS self_pct_of_demand, ROUND(c.self_used / c.gen * 100, 1) AS self_share, ROUND(c.tx / c.gen * 100, 1) AS tx_share FROM c, d
```

```sql id=coverage
SELECT MIN(year_month) AS first_month, MAX(year_month) AS last_month, COUNT(DISTINCT pref_name) AS prefs, COUNT(*) AS rows_total FROM enecho.electric_power.captive_power_generation_by_prefecture
```

```sql id=map
WITH c AS (SELECT pref_name, SUM(self_consumption_mwh) AS self_used FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計' GROUP BY 1), d AS (SELECT pref_name, SUM(total_demand_mwh) AS dem FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year = 2025 GROUP BY 1) SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, ROUND(c.self_used / d.dem * 100, 1) AS pct, b.prefecture_name AS pref_name FROM nlftp.boundary.prefecture b JOIN c ON b.prefecture_name = c.pref_name JOIN d ON d.pref_name = c.pref_name
```

```sql id=rank_top
WITH c AS (SELECT pref_name, SUM(self_consumption_mwh) AS self_used FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計' GROUP BY 1), d AS (SELECT pref_name, SUM(total_demand_mwh) AS dem FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year = 2025 GROUP BY 1), ranked AS (SELECT c.pref_name AS pref_name, ROUND(c.self_used / d.dem * 100, 1) AS pct, ROW_NUMBER() OVER (ORDER BY c.self_used / d.dem DESC, c.pref_name) AS rn FROM c JOIN d ON c.pref_name = d.pref_name) SELECT pref_name, pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH c AS (SELECT pref_name, SUM(self_consumption_mwh) AS self_used FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計' GROUP BY 1), d AS (SELECT pref_name, SUM(total_demand_mwh) AS dem FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year = 2025 GROUP BY 1), ranked AS (SELECT c.pref_name AS pref_name, ROUND(c.self_used / d.dem * 100, 1) AS pct, ROW_NUMBER() OVER (ORDER BY c.self_used / d.dem DESC, c.pref_name) AS rn FROM c JOIN d ON c.pref_name = d.pref_name) SELECT pref_name, pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH c AS (SELECT pref_name, SUM(self_consumption_mwh) AS self_used FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計' GROUP BY 1), d AS (SELECT pref_name, SUM(total_demand_mwh) AS dem FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year = 2025 GROUP BY 1), ranked AS (SELECT c.pref_name AS pref_name, ROUND(c.self_used / d.dem * 100, 1) AS pct, ROW_NUMBER() OVER (ORDER BY c.self_used / d.dem DESC, c.pref_name) AS rn FROM c JOIN d ON c.pref_name = d.pref_name) SELECT pref_name, pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=mix
WITH b AS (SELECT pref_name, SUM(CASE WHEN power_source_group = '合計' THEN generation_mwh ELSE 0 END) AS tot, SUM(CASE WHEN power_source_group = '合計' THEN transmission_total_mwh ELSE 0 END) AS tx, SUM(CASE WHEN power_source_group = '新エネルギー' AND power_source_name IN ('太陽光', '風力', '地熱') THEN generation_mwh ELSE 0 END) AS vre, SUM(CASE WHEN power_source_group = '火力（燃料別）' AND power_source_name = '石炭' THEN generation_mwh ELSE 0 END) AS coal, SUM(CASE WHEN power_source_group = '新エネルギー' AND power_source_name = '風力' THEN generation_mwh ELSE 0 END) AS wind FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 GROUP BY 1) SELECT pref_name, ROUND(vre / NULLIF(tot, 0) * 100, 1) AS vre_pct, ROUND(tx / NULLIF(tot, 0) * 100, 1) AS tx_pct, ROUND(coal / NULLIF(tot, 0) * 100, 1) AS coal_pct, ROUND(wind / NULLIF(tot, 0) * 100, 1) AS wind_pct, ROUND(tot / 1000, 1) AS gen_gwh, ROUND(SQRT(tot / 1000) / 5 + 5, 1) AS bubble FROM b ORDER BY vre_pct DESC
```

```sql id=dest
WITH t AS (SELECT pref_name, SUM(transmission_to_utilities_mwh) / 1000 AS util, SUM(transmission_to_specified_supply_mwh) / 1000 AS spec, SUM(transmission_to_other_operators_mwh) / 1000 AS other, SUM(transmission_total_mwh) / 1000 AS tot FROM enecho.electric_power.captive_power_generation_by_prefecture WHERE fiscal_year = 2025 AND power_source_group = '合計' GROUP BY 1), r AS (SELECT pref_name, util, spec, other, tot, ROW_NUMBER() OVER (ORDER BY tot DESC, pref_name) AS rn FROM t) SELECT pref_name, ROUND(util, 1) AS util_gwh, ROUND(spec, 1) AS spec_gwh, ROUND(other, 1) AS other_gwh, ROUND(tot, 1) AS tot_gwh, ROUND(spec / NULLIF(tot, 0) * 100, 1) AS spec_share FROM r WHERE rn <= 15 ORDER BY rn
```
