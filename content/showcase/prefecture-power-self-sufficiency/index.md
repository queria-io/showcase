---
title: 県内需要に対する発電量の割合は、佐賀県が10年で10.6%から251.0%に上がり、29都道府県では下がった
description: 都道府県別の発電実績と電力需要実績から、県内の発電量を県内の需要量で割った割合を2016年度から2025年度まで集計しました。2025年度は福井県の761.6%が最も高く、滋賀県の1.5%が最も低く、10年で割合が下がったのは29都道府県です。
ogDescription: 県内の発電量を県内の需要量で割った割合を2016年度から2025年度まで集計しました。佐賀県は10.6%から251.0%に上がり、29都道府県では下がりました。
publishedAt: 2026-08-15
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 電力
  - エネルギー
  - 資源エネルギー庁
datasets:
  - queria/enecho
sources:
  - title: 電力調査統計
    url: https://www.enecho.meti.go.jp/statistics/electric_power/ep002/
    publisher: 経済産業省 資源エネルギー庁
  - title: 電力調査統計 よくある問い合わせ
    url: https://www.enecho.meti.go.jp/statistics/electric_power/ep002/pdf/faq.pdf
    publisher: 経済産業省 資源エネルギー庁
agentHint: enecho.electric_power.power_generation_by_prefecture と power_demand_by_prefecture を月別のまま突き合わせて、私の県の発電量と需要量の比率が2025年度の月ごとにどう動いたかを出して。太陽光の発電量も月別で並べて
socialAnnounce: |-
  都道府県別の発電実績と電力需要実績を突き合わせ、県内で使う電気をどれだけ県内で作れているかを10年分そろえました。

  地域のエネルギー計画や電源の立地検討に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

県内の電気事業者の発電量を県内の需要量で割った割合は、2025年度に福井県で761.6%、滋賀県で1.5%でした。佐賀県は2016年度の10.6%から2025年度の251.0%に上がり、和歌山県は101.4%から31.2%に下がっています。2016年度と比較して割合が下がったのは47都道府県のうち29で、そのうち28県では県内の発電量が減っていました。

県内でどれだけの電気が発電され、どれだけ使われているかは、自治体が地域のエネルギー計画を立てるときの基礎になる数字です。この記事では、[資源エネルギー庁の電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)から、都道府県別の発電実績（`power_generation_by_prefecture`）と都道府県別需要実績（`power_demand_by_prefecture`）の2つを都道府県・年度ごとに結合します。どちらも都道府県×月を1行として、2016年度から収録されています。県内にある電気事業者の発電所が発電した電力量を、県内の需要電力量で割った値を、以下では「県内でまかなえている割合」と呼びます。この割合が100%を超える県は、県内で使う量より多くを発電しているということです。

## 2025年度は福井県の761.6%が最も高く、滋賀県の1.5%が最も低い

2025年度（2025年4月〜2026年3月）の1年分を合計して、47都道府県を並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "県内でまかなえている割合（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県", "labelOverlap": "greedy"},
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
      "data": {"name": "mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "県内でまかなえている割合（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県", "labelOverlap": "greedy"},
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
      "data": {"name": "bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "県内でまかなえている割合（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県", "labelOverlap": "greedy"},
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

最も高いのは福井県の761.6%で、県内で使う量の7倍以上を発電しています。福島県397.5%、島根県370.5%、徳島県281.7%が続きます。最も低いのは滋賀県の1.5%と埼玉県の1.6%です。100%以上の県は47のうち21ありました。

この割合は、県内の発電量と県内の需要量を比較した値です。電気は送電線で県境を越えて流れるので、その県で発電した電気がその県で使われたことは表しません。発電量は電気事業者（発電事業者や小売電気事業者など）の発電所の分だけで、[一般家庭の屋根の太陽光のように電気事業者でない者の発電設備は含みません](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/pdf/faq.pdf)。需要量も小売電気事業者などが供給した電力量なので、工場が自前の発電設備で発電して自分で使った分は、発電量にも需要量にも含まれません。

首都圏では、東京都は6.0%、埼玉県は1.6%と低い一方で、千葉県は239.5%、神奈川県は144.7%で、県内の需要量を大きく上回る電気が県内で発電されています。大阪府は24.2%です。

首都圏や大阪府以外でも、滋賀県1.5%、奈良県16.0%、群馬県28.1%、和歌山県31.2%、山梨県35.6%は、東京都や大阪府と同じく下位10に入っています。

## 10年で福井県は630.7ポイント上がり、大分県は116.9ポイント下がった

2016年度と2025年度の割合を比較し、上がった10県と下がった10県を並べました。2つの年度だけで比較しているので、後で取り上げる佐賀県の2022年度のように1年だけ大きく変わった年度を比較の起点や終点にすると、差は大きく変わります。

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "fall"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2016年度からの変化（ポイント）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "低下",
          "type": "nominal",
          "scale": {"domain": ["低下", "上昇"], "range": ["#ef4444", "#22c55e"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rise"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2016年度からの変化（ポイント）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上昇",
          "type": "nominal",
          "scale": {"domain": ["低下", "上昇"], "range": ["#ef4444", "#22c55e"]},
          "title": null
        }
      }
    }
  ]
}
```

福井県は630.7ポイント、佐賀県は240.4ポイント、島根県は207.4ポイント上がりました。反対に大分県は116.9ポイント、三重県は73.1ポイント、徳島県は70.9ポイント、和歌山県は70.3ポイント下がっています。

下がった10県には、首都圏の千葉県（50.7ポイント）・神奈川県（38.8ポイント）と大阪府も入っています。

## 佐賀県は原子力、和歌山県は火力の発電量の増減で割合が大きく変わった

大きく上がった佐賀県、大きく下がった和歌山県、10年を通じて低い東京都の3つを、年度ごとに並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "traj"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fy\"]) && isValid(datum[\"saga_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "fy", "type": "quantitative"},
          {"field": "saga_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "fy",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "saga_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "県内でまかなえている割合（%）", "grid": true}
        },
        "color": {
          "datum": "佐賀県",
          "type": "nominal",
          "scale": {"domain": ["佐賀県", "和歌山県", "東京都"], "range": ["#3b82f6", "#ef4444", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "traj"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fy\"]) && isValid(datum[\"wakayama_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "fy", "type": "quantitative"},
          {"field": "wakayama_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "fy",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "wakayama_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "県内でまかなえている割合（%）", "grid": true}
        },
        "color": {
          "datum": "和歌山県",
          "type": "nominal",
          "scale": {"domain": ["佐賀県", "和歌山県", "東京都"], "range": ["#3b82f6", "#ef4444", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "traj"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"fy\"]) && isValid(datum[\"tokyo_pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "fy", "type": "quantitative"},
          {"field": "tokyo_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "fy",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "tokyo_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "県内でまかなえている割合（%）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {"domain": ["佐賀県", "和歌山県", "東京都"], "range": ["#3b82f6", "#ef4444", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

佐賀県は2016年度に10.6%で、同じ年の東京都の11.4%より低い値でした。2018年度には270.2%に上がり、2025年度は251.0%です。同じ期間の県内の原子力発電量は、2016年度の0から2018年度に17,247GWh、2025年度に15,645GWhになっています。割合が上がったのは、県内の原子力発電所が稼働したためです。

佐賀県の割合は年ごとの変動も大きく、2022年度だけ114.9%に下がっています。この年の原子力発電量は6,712GWhで、2018年度以降のほかの年の半分以下です。原子力の発電量は年によって大きく変わるので、県の位置は1年分ではなく複数年の推移で確認する必要があります。

和歌山県は2016年度に101.4%で、県内の需要量をわずかに上回っていました。2019年度に43.6%まで下がり、2022年度に59.1%まで上がったあと再び下がって、2024年度は24.8%、2025年度は31.2%です。10年で3分の1以下になりました。同じ期間に県内の火力発電量は5,414GWhから753GWhへ7分の1以下に減りました。県内の発電量は4,434GWh減っており、その大半は火力の減少（4,661GWh）です。

東京都は10年を通じて低い水準のまま、11.4%から6.0%へゆるやかに下がりました。

## 100%以上の県の数は22から21でほぼ同じだが、中央値は98.6%から80.1%に下がった

県内でまかなえている割合が100%以上の県の数と、47都道府県の中央値を年度ごとに並べました。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "agg"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "fy", "type": "quantitative"},
              {"field": "over100", "type": "quantitative"}
            ],
            "x": {
              "field": "fy",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "over100",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "100%以上の県の数", "grid": true}
            },
            "color": {
              "datum": "100%以上の県の数",
              "type": "nominal",
              "scale": {"domain": ["100%以上の県の数", "47県の中央値（%）"], "range": ["#93c5fd", "#7c3aed"]},
              "title": null
            }
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "agg"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"fy\"]) && isValid(datum[\"median_pct\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#7c3aed",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 36}
          },
          "encoding": {
            "tooltip": [
              {"field": "fy", "type": "quantitative"},
              {"field": "median_pct", "type": "quantitative"}
            ],
            "x": {
              "field": "fy",
              "type": "ordinal",
              "axis": {"title": "年度", "labelAngle": 0, "labelOverlap": "greedy"},
              "sort": null
            },
            "y": {
              "field": "median_pct",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "中央値（%）", "orient": "right"}
            },
            "color": {
              "datum": "47県の中央値（%）",
              "type": "nominal",
              "scale": {"domain": ["100%以上の県の数", "47県の中央値（%）"], "range": ["#93c5fd", "#7c3aed"]},
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

100%以上の県の数は、2016年度の22から2025年度の21へ、1つ減っただけです。10年間を通しても20から23の間に収まっています。2016年度と2025年度で100%をまたいだのは5県で、佐賀県と宮城県が下から上へ、三重県・和歌山県・熊本県が上から下へ移りました。残る42県は、2つの年度で100%の同じ側にいます。

中央値は98.6%から80.1%へ18.5ポイント下がりました。2016年度の中央値は10年で最も高く、2024年度は91.8%だったので、下げ幅はどの年度と比較するかで大きく変わります。2016年度と2025年度を比較すると、割合が下がった県は47のうち29、上がった県は18です。

割合が下がった29県のうち28県では県内の発電量そのものが減り、26県では火力の発電量が減っていました。29県の火力の発電量は合わせて182,129GWh減り、同じ29県の太陽光と風力の増加13,513GWhは、その1割にも届きません。29県のうち24県では需要量も減っています。需要量が減ると割合は上がるので、この24県で割合が下がったのは発電量が減ったためです。家庭の屋根の太陽光は発電量に含まれず、その電気を家庭で使った分は需要量の減少として表れます。

10年のどの年度でも100%の同じ側にいた県は39です。残る8県は、いずれかの年度で100%をまたいでいます。先の5県に加えて、高知県・石川県・鹿児島県は2016年度と2025年度では同じ側にいながら、途中の年度で反対側に移った年があります。

## 業務での使い方

- 地域エネルギー計画や地球温暖化対策実行計画の基礎資料として、自分の県の位置を47都道府県の中で確認する。2016年度からの推移を確認し、割合が大きく変わった年度があれば、発電実績の電源別の列（原子力・火力・太陽光など）でどの電源の発電量が変わったかを確認する
- 自分の県で大きな発電所の再稼働や休廃止が予定されているとき、その発電所の年間発電量の見込みを県の年間需要量で割り、割合がどれだけ変わるかを見積もる。佐賀県の原子力（240.4ポイント上昇）と和歌山県の火力（70.3ポイント低下）が、実際に起きた変化の大きさの例になる

## データの出典

本記事は資源エネルギー庁 [電力調査統計](https://www.enecho.meti.go.jp/statistics/electric_power/ep002/)の統計表 2-(2)「都道府県別発電実績」と 3-(2)「都道府県別需要実績」を、2026年11月14日時点で集計しています。対象は2016年度から2025年度までの47都道府県×月の実績で、数値はすべて年度で合計しています。2025年度の値は、資源エネルギー庁が2026年9月11日に更新した年度分の公表値です。

Queriaは、電力調査統計の都道府県別の発電実績と需要実績を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別発電実績](/datasets/queria/enecho/electric_power/power_generation_by_prefecture)から自分の県の電源別の発電量を確認したり、[都道府県別電力需要実績](/datasets/queria/enecho/electric_power/power_demand_by_prefecture)と結合して直近の月までの割合を集計したりできます。

```sql id=top
WITH r AS (SELECT g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year = 2025 GROUP BY 1), ranked AS (SELECT pref, pct, ROW_NUMBER() OVER (ORDER BY pct DESC, pref) AS rn FROM r) SELECT pref, ROUND(pct, 1) AS pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=mid
WITH r AS (SELECT g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year = 2025 GROUP BY 1), ranked AS (SELECT pref, pct, ROW_NUMBER() OVER (ORDER BY pct DESC, pref) AS rn FROM r) SELECT pref, ROUND(pct, 1) AS pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=bottom
WITH r AS (SELECT g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year = 2025 GROUP BY 1), ranked AS (SELECT pref, pct, ROW_NUMBER() OVER (ORDER BY pct DESC, pref) AS rn FROM r) SELECT pref, ROUND(pct, 1) AS pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=rise
WITH y AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year IN (2016, 2025) GROUP BY 1, 2), c AS (SELECT a.pref, b.pct - a.pct AS diff FROM y a JOIN y b ON a.pref = b.pref AND a.fy = 2016 AND b.fy = 2025), ranked AS (SELECT pref, diff, ROW_NUMBER() OVER (ORDER BY diff DESC, pref) AS rn FROM c) SELECT pref, ROUND(diff, 1) AS diff FROM ranked WHERE rn <= 10 ORDER BY rn DESC
```

```sql id=fall
WITH y AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year IN (2016, 2025) GROUP BY 1, 2), c AS (SELECT a.pref, b.pct - a.pct AS diff FROM y a JOIN y b ON a.pref = b.pref AND a.fy = 2016 AND b.fy = 2025), ranked AS (SELECT pref, diff, ROW_NUMBER() OVER (ORDER BY diff DESC, pref) AS rn FROM c) SELECT pref, ROUND(diff, 1) AS diff FROM ranked WHERE rn > 37 ORDER BY rn DESC
```

```sql id=traj
WITH j AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) AS gen, SUM(d.total_demand_mwh) AS dem, SUM(g.nuclear_mwh) AS nuc, SUM(g.thermal_mwh) AS th FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year <= 2025 AND g.pref_name IN ('佐賀県', '和歌山県', '東京都') GROUP BY 1, 2) SELECT fy, ROUND(MAX(CASE WHEN pref = '佐賀県' THEN gen / dem * 100 END), 1) AS saga_pct, ROUND(MAX(CASE WHEN pref = '和歌山県' THEN gen / dem * 100 END), 1) AS wakayama_pct, ROUND(MAX(CASE WHEN pref = '東京都' THEN gen / dem * 100 END), 1) AS tokyo_pct, ROUND(MAX(CASE WHEN pref = '佐賀県' THEN nuc / 1000 END), 0) AS saga_nuclear_gwh, ROUND(MAX(CASE WHEN pref = '和歌山県' THEN th / 1000 END), 0) AS wakayama_thermal_gwh, ROUND(MAX(CASE WHEN pref = '和歌山県' THEN gen / 1000 END), 0) AS wakayama_gen_gwh FROM j GROUP BY fy ORDER BY fy
```

```sql id=agg
WITH y AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year <= 2025 GROUP BY 1, 2) SELECT fy, CAST(SUM(CASE WHEN pct >= 100 THEN 1 ELSE 0 END) AS DOUBLE) AS over100, ROUND(MEDIAN(pct), 1) AS median_pct FROM y GROUP BY fy ORDER BY fy
```

```sql id=moves
WITH y AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year IN (2016, 2025) GROUP BY 1, 2), c AS (SELECT a.pref, a.pct AS p16, b.pct AS p25 FROM y a JOIN y b ON a.pref = b.pref AND a.fy = 2016 AND b.fy = 2025) SELECT CAST(SUM(CASE WHEN p25 > p16 THEN 1 ELSE 0 END) AS DOUBLE) AS rose, CAST(SUM(CASE WHEN p25 < p16 THEN 1 ELSE 0 END) AS DOUBLE) AS fell, CAST(SUM(CASE WHEN (p16 >= 100) = (p25 >= 100) THEN 1 ELSE 0 END) AS DOUBLE) AS same_side, string_agg(CASE WHEN p16 < 100 AND p25 >= 100 THEN pref END, '・' ORDER BY pref) AS crossed_up, string_agg(CASE WHEN p16 >= 100 AND p25 < 100 THEN pref END, '・' ORDER BY pref) AS crossed_down FROM c
```

```sql id=crossed
WITH y AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) / SUM(d.total_demand_mwh) * 100 AS pct FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year <= 2025 GROUP BY 1, 2), r AS (SELECT pref, MIN(pct) AS mn, MAX(pct) AS mx FROM y GROUP BY pref) SELECT CAST(SUM(CASE WHEN mn >= 100 OR mx < 100 THEN 1 ELSE 0 END) AS DOUBLE) AS same_side_all_years, string_agg(CASE WHEN NOT (mn >= 100 OR mx < 100) THEN pref END, '・' ORDER BY pref) AS crossed_any_year FROM r
```

```sql id=fallen
WITH j AS (SELECT g.fiscal_year AS fy, g.pref_name AS pref, SUM(g.total_mwh) AS gen, SUM(d.total_demand_mwh) AS dem, SUM(g.thermal_mwh) AS th, SUM(g.solar_mwh + g.wind_mwh) AS sw FROM enecho.electric_power.power_generation_by_prefecture g JOIN enecho.electric_power.power_demand_by_prefecture d ON g.pref_code = d.pref_code AND g.year_month = d.year_month WHERE g.fiscal_year IN (2016, 2025) GROUP BY 1, 2), c AS (SELECT a.pref, b.gen / b.dem - a.gen / a.dem AS dpct, b.gen - a.gen AS dgen, b.dem - a.dem AS ddem, b.th - a.th AS dth, b.sw - a.sw AS dsw FROM j a JOIN j b ON a.pref = b.pref AND a.fy = 2016 AND b.fy = 2025) SELECT CAST(COUNT(*) AS DOUBLE) AS prefs, CAST(SUM(CASE WHEN dgen < 0 THEN 1 ELSE 0 END) AS DOUBLE) AS generation_down, CAST(SUM(CASE WHEN dth < 0 THEN 1 ELSE 0 END) AS DOUBLE) AS thermal_down, CAST(SUM(CASE WHEN ddem < 0 THEN 1 ELSE 0 END) AS DOUBLE) AS demand_down, ROUND(SUM(dth) / 1000) AS thermal_change_gwh, ROUND(SUM(dsw) / 1000) AS solar_wind_change_gwh FROM c WHERE dpct < 0
```
