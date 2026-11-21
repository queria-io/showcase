---
title: 熊本県の大口の電力需要は、2023年末から2年6か月で21.1%増えた
description: 資源エネルギー庁の都道府県別電力需要を12か月移動累計で集計しました。特別高圧の需要は全国で9年に4.8%減った一方、2016年度から2023年度に二桁増えた県が5つあり、熊本県は2023年12月から2026年6月に21.1%増えています。
ogDescription: 資源エネルギー庁の都道府県別電力需要を12か月移動累計で集計し、2016年度から2023年度に特別高圧の需要が二桁増えた5県の推移を比較しました。
publishedAt: 2026-08-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 電力
  - 製造業
  - 企業誘致
datasets:
  - queria/enecho
  - queria/e_stat
sources:
  - title: 電力調査統計
    url: https://www.enecho.meti.go.jp/statistics/electric_power/ep002/
    publisher: 経済産業省 資源エネルギー庁
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省
  - title: 経済構造実態調査
    url: https://www.stat.go.jp/data/kkj/gaiyo.html
    publisher: 総務省・経済産業省
  - title: 工業統計調査
    url: https://www.meti.go.jp/statistics/tyo/kougyo/result-2.html
    publisher: 経済産業省
  - title: 社会・人口統計体系 項目定義
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/C
    publisher: 総務省
  - title: 電気事業制度について
    url: https://www.enecho.meti.go.jp/category/electricity_and_gas/electric/summary/
    publisher: 経済産業省 資源エネルギー庁
agentHint: 三重県と鹿児島県の特別高圧の電力需要を2016年4月から月ごとに出して。12か月移動累計にして、水準が動き出した月も教えて。
socialAnnounce: |-
  資源エネルギー庁の都道府県別電力需要を月ごとに追いました。

  大口の需要が2016年度から2023年度に二桁増えたのは5県で、熊本県は2023年末から2年6か月で21.1%増えました。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

熊本県の特別高圧の電力需要は、直近12か月の合計で2023年12月の2,841GWhから2026年6月の3,441GWhへ、2年6か月で21.1%増えました。特別高圧の需要は全国では2016年度から2025年度に4.8%減っていますが、2016年度から2023年度に二桁増えた県が岩手県・長崎県・三重県・熊本県・鹿児島県の5つあります。製造品出荷額等は47都道府県のうち46で増えた一方、そのうち36では特別高圧の電力需要が減っていました。

資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)には、都道府県別の電力需要実績が2016年4月から2026年6月まで、月ごとに収録されています（`power_demand_by_prefecture`）。小売電気事業者が供給した電力量を、契約の電圧区分で3つに分けたものです。

| 列                      | 区分     |
| ----------------------- | -------- |
| `extra_high_demand_mwh` | 特別高圧 |
| `high_demand_mwh`       | 高圧     |
| `low_demand_mwh`        | 低圧     |

この記事では特別高圧を集計しました。3区分のうち契約の規模が最も大きい区分で、電力の小売自由化も[使用最大電力2,000kW以上の需要家](https://www.enecho.meti.go.jp/category/electricity_and_gas/electric/summary/)から始まり、50kW以上、2016年4月の全面自由化へと対象が広がりました。区分は契約の電圧だけで分けているので、業種の区別はなく、製造業以外の需要家も同じ区分に入っています。電力需要実績は小売電気事業者が供給した分なので、事業所が自家発電で使う電力は含まず、系統から買う量が変わると、使う電力の総量が同じでもこの値は変わります。

## 特別高圧の需要が二桁増えた5県は、増えた時期がそれぞれ違う

月ごとの値をそのまま並べると夏と冬が高くなります。直近12か月を合計すると1年分の季節がすべて入るので、季節による変動を除いた水準の変化が分かります。この12か月移動累計を2017年3月から2026年6月まで並べたのが次の図です。県によって水準が5倍以上違うので、縦軸は対数目盛にしています。線の傾きが同じなら増加率も同じです。

対象は、2016年度から2023年度にかけて特別高圧の需要が二桁増えた岩手県・長崎県・三重県・熊本県・鹿児島県の5県です。

```chart
{
  "height": 320,
  "layer": [
    {
      "data": {"name": "ramp"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"t\"]) && isValid(datum[\"iwate\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#22c55e", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "t", "type": "quantitative"},
          {"field": "iwate", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "iwate",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "特別高圧の電力需要・直近12か月の合計（GWh・対数目盛）", "grid": true}
        },
        "color": {
          "datum": "岩手県",
          "type": "nominal",
          "scale": {
            "domain": ["岩手県", "熊本県", "長崎県", "鹿児島県", "三重県"],
            "range": ["#22c55e", "#ec4899", "#3b82f6", "#f97316", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ramp"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"t\"]) && isValid(datum[\"kumamoto\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#ec4899", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "t", "type": "quantitative"},
          {"field": "kumamoto", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "kumamoto",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "特別高圧の電力需要・直近12か月の合計（GWh・対数目盛）", "grid": true}
        },
        "color": {
          "datum": "熊本県",
          "type": "nominal",
          "scale": {
            "domain": ["岩手県", "熊本県", "長崎県", "鹿児島県", "三重県"],
            "range": ["#22c55e", "#ec4899", "#3b82f6", "#f97316", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ramp"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"t\"]) && isValid(datum[\"nagasaki\"]) ? 0 : 1",
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
          {"field": "nagasaki", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "nagasaki",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "特別高圧の電力需要・直近12か月の合計（GWh・対数目盛）", "grid": true}
        },
        "color": {
          "datum": "長崎県",
          "type": "nominal",
          "scale": {
            "domain": ["岩手県", "熊本県", "長崎県", "鹿児島県", "三重県"],
            "range": ["#22c55e", "#ec4899", "#3b82f6", "#f97316", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ramp"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"t\"]) && isValid(datum[\"kagoshima\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#f97316", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "t", "type": "quantitative"},
          {"field": "kagoshima", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "kagoshima",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "特別高圧の電力需要・直近12か月の合計（GWh・対数目盛）", "grid": true}
        },
        "color": {
          "datum": "鹿児島県",
          "type": "nominal",
          "scale": {
            "domain": ["岩手県", "熊本県", "長崎県", "鹿児島県", "三重県"],
            "range": ["#22c55e", "#ec4899", "#3b82f6", "#f97316", "#7c3aed"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "ramp"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"t\"]) && isValid(datum[\"mie\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {"type": "line", "color": "#7c3aed", "invalid": "break-paths-show-domains"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "t", "type": "quantitative"},
          {"field": "mie", "type": "quantitative"}
        ],
        "x": {
          "field": "t",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "mie",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "特別高圧の電力需要・直近12か月の合計（GWh・対数目盛）", "grid": true}
        },
        "color": {
          "datum": "三重県",
          "type": "nominal",
          "scale": {
            "domain": ["岩手県", "熊本県", "長崎県", "鹿児島県", "三重県"],
            "range": ["#22c55e", "#ec4899", "#3b82f6", "#f97316", "#7c3aed"]
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

5県とも2016年度から2023年度で増えていますが、増えた時期はそれぞれ違います。岩手県は系列の底である2019年7月の1,421GWhから2023年1月の2,405GWhまで、42か月で69.2%増えました。そのあと2024年1月の2,376GWhまで1年ほど横ばいで、2026年6月には2,715GWhへ再び増えています。長崎県は2020年5月の1,403GWhから2025年1月の2,052GWhまで46.3%増え、その後は2026年6月の2,102GWhまで緩やかに増えています。

鹿児島県は最も早く、系列の始まりである2017年3月の1,445GWhから2019年10月の1,589GWhまで上がったあと、2021年2月に1,528GWhまで下がり、2026年3月に系列で最も多い1,663GWhへ戻しました。2026年6月は1,653GWhです。三重県は5県のなかで水準が最も高く、2017年3月の7,628GWhから2022年の9,524GWhまで伸びたあと、2025年7月の9,416GWhからは毎月下がり、2026年6月は9,225GWhです。熊本県は2017年3月の2,472GWhから2018年9月の2,714GWhまでと、2021年2月の2,587GWhから2023年2月の2,882GWhまでの2度伸びたあと、2023年は1年を通じて2,841〜2,882GWhの範囲で推移しました。2024年に入ってから再び増え、2025年7月の3,366GWhから11月の3,308GWhへいったん下がったあと、2026年6月には3,441GWhになりました。2023年12月の2,841GWhと比較すると、2年6か月で21.1%の増加です。

5県それぞれの、直近12か月の合計が最も小さかった月と最も大きかった月、最新の月は次のとおりです。

```sql
SELECT * FROM ramp_points
```

## 全国の特別高圧の需要は、9年で4.8%減った

5県の増加と比較するため、3つの区分それぞれについて、47都道府県の合計を年度ごとに集計しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"extra_high_twh\"]) ? 0 : 1",
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
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "extra_high_twh", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "extra_high_twh",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "電力需要（TWh）", "grid": true}
        },
        "color": {
          "datum": "特別高圧",
          "type": "nominal",
          "scale": {"domain": ["特別高圧", "高圧", "低圧"], "range": ["#3b82f6", "#f97316", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"high_twh\"]) ? 0 : 1",
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
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "high_twh", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "high_twh",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "電力需要（TWh）", "grid": true}
        },
        "color": {
          "datum": "高圧",
          "type": "nominal",
          "scale": {"domain": ["特別高圧", "高圧", "低圧"], "range": ["#3b82f6", "#f97316", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fiscal_year\"]) && isValid(datum[\"low_twh\"]) ? 0 : 1",
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
          {"field": "fiscal_year", "type": "quantitative"},
          {"field": "low_twh", "type": "quantitative"}
        ],
        "x": {
          "field": "fiscal_year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "low_twh",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "電力需要（TWh）", "grid": true}
        },
        "color": {
          "datum": "低圧",
          "type": "nominal",
          "scale": {"domain": ["特別高圧", "高圧", "低圧"], "range": ["#3b82f6", "#f97316", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

特別高圧は2016年度の231.4TWhから2025年度の220.3TWhへ、9年で4.8%減りました。高圧は308.3TWhから291.1TWhへ減り、家庭を含む低圧は2016年度も2025年度も310.8TWhです。低圧だけが増えて他の2区分が減ったのは、収録期間では2019年度から2020年度にかけての一度だけです。特別高圧は229.9TWhから215.0TWhへ、高圧は302.8TWhから291.2TWhへ落ちる一方、低圧は303.4TWhから314.7TWhへ増えています。

特別高圧の全国の需要は、増減を繰り返しながら減っています。収録期間で最も多いのは2018年度の236.3TWh、最も少ないのは2020年度の215.0TWhで、そのあと2021年度に225.4TWhへ戻し、2023年度に217.8TWhまで下がったあと、2025年度は220.3TWhです。全国の需要が減るなかで、5県は同じ期間に需要を増やしました。

## 製造品出荷額等が増えた46都道府県のうち、36で特別高圧の需要は減った

製造業の規模を金額で表した統計に、製造品出荷額等があります。e-Statの[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)に収録された都道府県別の経済データ（`c_pref_economy`）に、製造品出荷額等（`C3401`）として1975年から2023年まで入っています。[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/C)によれば、単位は百万円、対象は従業者4人以上の事業所、集計期間は暦年（1〜12月）です。電力需要のほうは年度（4〜3月）なので、以下の比較は3か月ずれた期間を重ねています。

両方の値がある2016年から2023年について、都道府県ごとの変化率を散布図にしました。横軸が製造品出荷額等、縦軸が特別高圧の電力需要で、どちらも2016年からの変化率です。出荷額の2016年の値は[工業統計調査](https://www.meti.go.jp/statistics/tyo/kougyo/result-2.html)、2023年の値は[経済構造実態調査](https://www.stat.go.jp/data/kkj/gaiyo.html)によるもので、変化率にはこの調査の切り替えの影響も含まれます。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "divergence"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "ship_pct", "type": "quantitative"},
          {"field": "power_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "ship_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "製造品出荷額等の変化率（%）", "grid": true}
        },
        "y": {
          "field": "power_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "特別高圧の電力需要の変化率（%）", "grid": true}
        }
      }
    }
  ]
}
```

点のほとんどは右下にあります。製造品出荷額等は47都道府県のうち46で増えていますが、そのうち36では特別高圧の電力需要が減っています。両方が増えたのは10だけです。図では岐阜県が横軸に重なって見えますが、変化率が0.0%に丸まっているためで、減った36に含まれます。

出荷額の伸びが最も大きいのは大分県の+53.8%と愛媛県の+46.6%ですが、電力はそれぞれ16.4%、17.2%減っています。電力の減少率が最も大きいのは高知県の-37.4%で、高知県の出荷額は+15.2%増えています。電力の増加率が最も大きいのは岩手県の+58.8%で、出荷額の+31.7%を上回りました。最初の図の5県のうち、電力の伸びが出荷額を上回ったのは岩手県と長崎県の2県です。長崎県は出荷額の+6.4%に対して電力が+28.2%でした。

製造品出荷額等は名目の金額で、電力需要は物量です。金額は、生産した量が同じでも単価が変わると変化します。

熊本県の電力需要は、2024年に入ってから3度目の増加が続いています。製造品出荷額等の収録は2023年までなので、2023年末からの2年6か月の増加は、出荷額の統計にはまだ含まれていません。

## データの出典

本記事は経済産業省 資源エネルギー庁の[電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)から都道府県別電力需要実績（`power_demand_by_prefecture`）を、e-Statの[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)から都道府県別経済データ（`c_pref_economy`）の製造品出荷額等（`C3401`）を、2026-10-20時点で集計しています。電力は2016年4月から2026年6月まで、製造品出荷額等は1975年から2023年までが収録範囲です。

Queriaは、資源エネルギー庁やe-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別電力需要実績](/datasets/queria/enecho/electric_power/power_demand_by_prefecture)から自分の県の直近の推移を確認したり、[都道府県別経済データ](/datasets/queria/e_stat/ssds/c_pref_economy)と比較したりできます。

```sql id=divergence
WITH e AS (SELECT pref_name, SUM(CASE WHEN fiscal_year = 2016 THEN extra_high_demand_mwh END) AS eh16, SUM(CASE WHEN fiscal_year = 2023 THEN extra_high_demand_mwh END) AS eh23 FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year IN (2016, 2023) GROUP BY pref_name), s AS (SELECT area_name, MAX(CASE WHEN year = 2016 THEN TRY_CAST(value AS DOUBLE) END) AS s16, MAX(CASE WHEN year = 2023 THEN TRY_CAST(value AS DOUBLE) END) AS s23 FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year IN (2016, 2023) AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT e.pref_name, ROUND((s.s23 / s.s16 - 1) * 100, 1) AS ship_pct, ROUND((e.eh23 / e.eh16 - 1) * 100, 1) AS power_pct FROM e JOIN s ON e.pref_name = s.area_name ORDER BY e.pref_name
```

```sql id=counts
WITH e AS (SELECT pref_name, SUM(CASE WHEN fiscal_year = 2016 THEN extra_high_demand_mwh END) AS eh16, SUM(CASE WHEN fiscal_year = 2023 THEN extra_high_demand_mwh END) AS eh23 FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year IN (2016, 2023) GROUP BY pref_name), s AS (SELECT area_name, MAX(CASE WHEN year = 2016 THEN TRY_CAST(value AS DOUBLE) END) AS s16, MAX(CASE WHEN year = 2023 THEN TRY_CAST(value AS DOUBLE) END) AS s23 FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND year IN (2016, 2023) AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), j AS (SELECT e.pref_name, s.s16, s.s23, e.eh16, e.eh23 FROM e JOIN s ON e.pref_name = s.area_name) SELECT COUNT(*) AS prefs, SUM(CASE WHEN s23 > s16 THEN 1 ELSE 0 END) AS shipment_up, SUM(CASE WHEN s23 > s16 AND eh23 < eh16 THEN 1 ELSE 0 END) AS shipment_up_power_down, SUM(CASE WHEN s23 > s16 AND eh23 > eh16 THEN 1 ELSE 0 END) AS both_up, ROUND(MIN((eh23 / eh16 - 1) * 100), 1) AS power_min, ROUND(MAX((eh23 / eh16 - 1) * 100), 1) AS power_max FROM j
```

```sql id=coverage
SELECT MIN(year) AS first_year, MAX(year) AS last_year, COUNT(DISTINCT year) AS years FROM e_stat.ssds.c_pref_economy WHERE cat01 = 'C3401' AND area_name != '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL
```

```sql id=national
SELECT fiscal_year, ROUND(SUM(extra_high_demand_mwh) / 1000000, 1) AS extra_high_twh, ROUND(SUM(high_demand_mwh) / 1000000, 1) AS high_twh, ROUND(SUM(low_demand_mwh) / 1000000, 1) AS low_twh FROM enecho.electric_power.power_demand_by_prefecture WHERE fiscal_year <= 2025 GROUP BY fiscal_year ORDER BY fiscal_year
```

```sql id=ramp
WITH r AS (SELECT pref_name, year, month, SUM(extra_high_demand_mwh) OVER (PARTITION BY pref_name ORDER BY year_month ROWS BETWEEN 11 PRECEDING AND CURRENT ROW) / 1000 AS eh12, ROW_NUMBER() OVER (PARTITION BY pref_name ORDER BY year_month) AS seq FROM enecho.electric_power.power_demand_by_prefecture WHERE pref_name IN ('岩手県', '熊本県', '長崎県', '鹿児島県', '三重県')) SELECT year + (month - 1) / 12.0 AS t, printf('%d年%d月', year, month) AS label, ROUND(MAX(CASE WHEN pref_name = '岩手県' THEN eh12 END), 0) AS iwate, ROUND(MAX(CASE WHEN pref_name = '熊本県' THEN eh12 END), 0) AS kumamoto, ROUND(MAX(CASE WHEN pref_name = '長崎県' THEN eh12 END), 0) AS nagasaki, ROUND(MAX(CASE WHEN pref_name = '鹿児島県' THEN eh12 END), 0) AS kagoshima, ROUND(MAX(CASE WHEN pref_name = '三重県' THEN eh12 END), 0) AS mie FROM r WHERE seq >= 12 GROUP BY t, label ORDER BY t
```

```sql id=ramp_points
WITH r AS (SELECT pref_name, year_month, year, month, SUM(extra_high_demand_mwh) OVER (PARTITION BY pref_name ORDER BY year_month ROWS BETWEEN 11 PRECEDING AND CURRENT ROW) / 1000 AS eh12, ROW_NUMBER() OVER (PARTITION BY pref_name ORDER BY year_month) AS seq FROM enecho.electric_power.power_demand_by_prefecture WHERE pref_name IN ('岩手県', '熊本県', '長崎県', '鹿児島県', '三重県')), s AS (SELECT *, printf('%d年%d月', year, month) AS label, ROW_NUMBER() OVER (PARTITION BY pref_name ORDER BY eh12, year_month) AS lo, ROW_NUMBER() OVER (PARTITION BY pref_name ORDER BY eh12 DESC, year_month) AS hi, ROW_NUMBER() OVER (PARTITION BY pref_name ORDER BY year_month DESC) AS last FROM r WHERE seq >= 12) SELECT pref_name AS '県', MAX(CASE WHEN lo = 1 THEN label END) AS '最小の月', ROUND(MAX(CASE WHEN lo = 1 THEN eh12 END)) AS '最小(GWh)', MAX(CASE WHEN hi = 1 THEN label END) AS '最大の月', ROUND(MAX(CASE WHEN hi = 1 THEN eh12 END)) AS '最大(GWh)', MAX(CASE WHEN last = 1 THEN label END) AS '最新の月', ROUND(MAX(CASE WHEN last = 1 THEN eh12 END)) AS '最新(GWh)' FROM s GROUP BY pref_name ORDER BY pref_name
```

```sql id=kumamoto
WITH r AS (SELECT year, month, year_month, SUM(extra_high_demand_mwh) OVER (ORDER BY year_month ROWS BETWEEN 11 PRECEDING AND CURRENT ROW) / 1000 AS eh12 FROM enecho.electric_power.power_demand_by_prefecture WHERE pref_name = '熊本県'), b AS (SELECT MIN(eh12) AS lo23, MAX(eh12) AS hi23 FROM r WHERE year = 2023), l AS (SELECT year, month, eh12 FROM r ORDER BY year_month DESC LIMIT 1) SELECT ROUND(b.lo23) AS '2023年の最小(GWh)', ROUND(b.hi23) AS '2023年の最大(GWh)', printf('%d年%d月', l.year, l.month) AS '最新の月', ROUND(l.eh12) AS '最新(GWh)', (l.year - 2023) * 12 + l.month - 12 AS '2023年12月からの月数', ROUND((l.eh12 / b.lo23 - 1) * 100, 1) AS '2023年の最小からの増加(%)' FROM b, l
```
