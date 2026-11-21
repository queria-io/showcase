---
title: 米は6年で9割近く値上がりしても買う量が変わらず、3割近く高くなった魚は2割減りました
description: 総務省の家計調査で、食品の単価と購入量を2019年と2025年で比較しました。米は単価が86.8%上がっても購入量は1.4%減で、単価が28.2%上がった生鮮魚介は購入量が22.5%減りました。
ogDescription: 家計調査で食品の単価と購入量を2019年と2025年で比較しました。米は86.8%値上がりして購入量1.4%減、生鮮魚介は28.2%値上がりして22.5%減です。
publishedAt: 2026-09-02
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 家計調査
  - 食品
  - 物価
datasets:
  - queria/e_stat
sources:
  - title: 家計調査 家計収支編 二人以上の世帯 品目別支出金額（年次）
    url: https://www.e-stat.go.jp/dbview?sid=0004023605
    publisher: 総務省統計局
  - title: 家計調査 家計収支編 二人以上の世帯 品目別購入数量（年次）
    url: https://www.e-stat.go.jp/dbview?sid=0004023606
    publisher: 総務省統計局
agentHint: e_stat.household.quantity と expenditure を cat01 で結合して、塩干魚介（010220000）の1gあたり支払額と年間購入量を2019年と2025年で県庁所在市別に出して。生鮮魚介（010210000）と減り方を比べて
socialAnnounce: |-
  家計調査の食品116品目の単価と購入量を2019年と2025年で比べました。米は9割近く高くなっても量がほぼ変わらず、魚は3割弱の値上がりで2割減っています。

  売場の品揃えの判断に。Queriaは行政のオープンデータを整えて公開しています。
---

2019年から2025年に、二人以上の世帯が米に払った1kgあたりの金額は86.8%上がりましたが、購入量は1.4%しか減っていません。生鮮魚介は値上がりが28.2%で、購入量は22.5%減りました。値上がり幅がほぼ同じ品目どうしでも、こんぶは21.7%の値上がりで購入量が31.2%減り、バターは21.9%の値上がりで7.7%増えています。値上がり幅の大きい順と、購入量の減り方の大きい順は一致しません。

食品スーパーの商品部で品揃えと価格改定を決めている担当者は、売上の伸びが単価の上昇によるもので、買い上げ点数は減っているという報告を毎月受け取ります。この記事では、値上がりした食品から順に買われなくなっているのかを確認します。

家計が何をどれだけ買ったかは、[総務省統計局の家計調査](https://www.stat.go.jp/data/kakei/)が品目ごとに記録しています。支出金額と購入数量が別々の統計表になっているので、同じ品目コードで結合すると、その食品に1単位あたりいくら払っているかを年ごとに出せます。この記事では、食品116品目について値上がり幅と購入量の変化を並べます。

## 家計調査の支出金額と購入数量を、品目コードで結合する

家計調査の家計収支編には、品目別の支出金額（`expenditure`）と品目別の購入数量（`quantity`）の2つのテーブルがあります。品目コード（`cat01`）が共通なので、両方を結合すると1単位あたりの支払額を求められます。ここでの単価は、世帯が払った金額を買った数量で割った値です。店頭の表示価格とは異なり、銘柄や容量の選び方も含めて世帯が実際に払った額です。

世帯区分（`cat02`）は二人以上の世帯（`03`）を使います。年次の値は12か月の合計で、たとえば米の購入量は1世帯の年間のキログラム数です。購入数量は品目ごとに記録されていて、単位も品目ごとに違います。食料は12の中分類に分かれますが、そのうち菓子類・調理食品・外食には数量の記録がありません。

費目の単位で数量が公表されているのは、食料のうち次の12区分です。加工肉や調味料は品目ごとには数量があるものの、費目の単位では数量が公表されていません。

| コード    | 区分     | 数量の単位 |
| --------- | -------- | ---------- |
| 010110001 | 米       | 1kg        |
| 010120000 | パン     | 1g         |
| 010130000 | 麺類     | 1g         |
| 010140000 | 他の穀類 | 1g         |
| 010210000 | 生鮮魚介 | 1g         |
| 010220000 | 塩干魚介 | 1g         |
| 010310000 | 生鮮肉   | 1g         |
| 010410001 | 牛乳     | 1l         |
| 010430001 | 卵       | 1g         |
| 010510000 | 生鮮野菜 | 1g         |
| 010610000 | 生鮮果物 | 1g         |
| 010710000 | 油脂     | 1g         |

比較の起点は新型コロナ前の2019年です。2020年と2021年は購入量が増えた品目が多く、その2年を起点にすると減り方が実際より大きく出ます。米の購入量も2019年の62.2kgから2020年の64.5kgへ増えています。

## 値上がり幅が最も大きい米と卵は、購入量がほとんど減っていない

12費目それぞれについて、1単位あたりの支払額と購入量が2019年から2025年でどう変わったかを並べました。上にあるほど値上がり幅が大きい費目です。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "category"},
      "transform": [
        {"fold": ["price_pct", "qty_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"price_pct\": \"1単位あたりの支払額\", \"qty_pct\": \"購入量\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"price_pct\",\"qty_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "item",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "2019年からの変化（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["1単位あたりの支払額", "購入量"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["購入量", "1単位あたりの支払額"]},
        "tooltip": [
          {"field": "item", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

値上がり幅が最も大きいのは米で86.8%、次いで卵が58.6%です。購入量はどちらもほとんど変わらず、米は1.4%減、卵は2.7%減です。購入量が最も大きく減ったのは生鮮魚介の22.5%減で、値上がり幅は28.2%と米の3分の1以下です。この数量は家庭で使うために買った分で、外食や惣菜として食べた魚は含みません。油脂も43.2%の値上がりに対して20.5%減、塩干魚介は26.3%の値上がりに対して19.5%減で、値上がり幅の順と減り方の順は一致していません。

購入量が増えている費目もあります。他の穀類が5.2%増、麺類が4.1%増、生鮮肉が4.0%増です。生鮮肉の値上がり幅は12.0%で12区分のうち最も小さい一方、麺類は19.6%、他の穀類は18.9%で、22.5%減った生鮮魚介の28.2%との差はどちらも10ポイント未満です。

二人以上の世帯の平均世帯人員は、この6年で2.97人から2.87人へ3.4%減っています。1世帯あたりの購入量はこの分だけ減りやすくなるので、数%の減少は世帯人員の減少で説明できます。生鮮魚介の22.5%減はその6倍以上で、世帯人員の減少だけでは説明できません。

## 米は2年で単価がほぼ倍になり、購入量は8.1%増えた

値上がり幅が最も大きかった米について、単価と購入量の推移を2015年から並べました。

```chart
{
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "rice"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"yen_per_kg\"]) ? 0 : 1",
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
              {"field": "year", "type": "quantitative"},
              {"field": "yen_per_kg", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年", "format": "d"}
            },
            "y": {
              "field": "yen_per_kg",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "1kgあたりの支払額（円）", "grid": true}
            },
            "color": {
              "datum": "1kgあたりの支払額（円）",
              "type": "nominal",
              "scale": {"domain": ["1kgあたりの支払額（円）", "年間購入量（kg）"], "range": ["#f97316", "#3b82f6"]},
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
          "data": {"name": "rice"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kg\"]) ? 0 : 1",
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
              {"field": "kg", "type": "quantitative"}
            ],
            "x": {
              "field": "year",
              "type": "quantitative",
              "scale": {"zero": false},
              "axis": {"title": "年", "format": "d"}
            },
            "y": {
              "field": "kg",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "年間購入量（kg）", "grid": false, "orient": "right"}
            },
            "color": {
              "datum": "年間購入量（kg）",
              "type": "nominal",
              "scale": {"domain": ["1kgあたりの支払額（円）", "年間購入量（kg）"], "range": ["#f97316", "#3b82f6"]},
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

1kgあたりの支払額は、2023年の360.1円から2024年に451.8円、2025年に697.1円になりました。2年で93.6%上がり、ほぼ倍です。年間購入量は2023年の56.7kgから2025年の61.3kgへ8.1%増えました。値段がほぼ倍になった2年間に、家庭が買った米の量は増えています。

2015年から2023年は、1kgあたりの支払額が330.6円から360.1円へ8.9%上がる間に、購入量は69.5kgから56.7kgへ18.4%減っています。値段が8.9%上がった8年間に量が2割近く減り、値段が倍になった2年間に量が増えたことになります。

## 値上がり幅がほぼ同じ30品目で、購入量は33.0%減から11.6%増まで分かれる

費目より細かい品目の単位で、116品目を値上がり幅と購入量の変化の散布図にしました。この116品目は穀類・魚介類・肉類・乳卵類・野菜海藻・果物・油脂調味料の7分類に属し、数量の記録がある飲料と酒類は含みません。品目分類は2025年改定版で、途中で統合された品目は2019年の値と範囲が一致しないことがあります。このうち、支払額の上昇が17%から23%の範囲にある30品目を色分けしました。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "others"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "item", "type": "nominal"},
          {"field": "price_pct", "type": "quantitative"},
          {"field": "qty_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "price_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1単位あたりの支払額の変化（%）", "grid": true}
        },
        "y": {
          "field": "qty_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "購入量の変化（%）", "grid": true}
        },
        "color": {
          "datum": "その他の86品目",
          "type": "nominal",
          "scale": {"domain": ["その他の86品目", "支払額が17〜23%上がった30品目"], "range": ["#94a3b8", "#ec4899"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "band"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "item", "type": "nominal"},
          {"field": "price_pct", "type": "quantitative"},
          {"field": "qty_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "price_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1単位あたりの支払額の変化（%）", "grid": true}
        },
        "y": {
          "field": "qty_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "購入量の変化（%）", "grid": true}
        },
        "color": {
          "datum": "支払額が17〜23%上がった30品目",
          "type": "nominal",
          "scale": {"domain": ["その他の86品目", "支払額が17〜23%上がった30品目"], "range": ["#94a3b8", "#ec4899"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

色を付けた30品目は、支払額の上昇が17.3%から23.0%の範囲にあります。購入量はさやまめの33.0%減から合いびき肉の11.6%増まで、44.6ポイントの幅に分布しています。30品目のうち8品目は購入量が増えています。

値上がり幅がほぼ同じで、購入量の増減が逆になった組を2つ挙げます。こんぶは21.7%高くなって31.2%減り、バターは21.9%高くなって7.7%増えました。さしみ盛合わせは18.0%高くなって26.8%減り、カップ麺は18.1%高くなって7.6%増えています。いずれも値上がり幅の差は0.2ポイント以下です。

この30品目のうち減り方の大きい10品目は、さやまめ33.0%減、かれい32.6%減、しじみ31.9%減、こんぶ31.2%減、さしみ盛合わせ26.8%減、メロン25.9%減、他の貝22.3%減、ベーコン19.0%減、牛肉17.4%減、食塩16.7%減です。増えた8品目は、だいこん漬・たい・カップ麺・バター・キウイフルーツ・鶏肉・パスタ・合いびき肉です。同じ分類の中でも増減の向きは分かれ、魚介ではかれいが32.6%減の一方でたいは3.4%増、肉類では牛肉が17.4%減の一方で鶏肉は10.3%増、合いびき肉は11.6%増です。116品目全体で購入量が増えたのは23品目です。

## 生鮮魚介の購入量は、52市すべてで減った

購入量の減り方が最も大きかった生鮮魚介について、県庁所在市と政令指定都市の52市を並べました。家計調査の地域区分は全国と52市で、都道府県別の値はありません。市ごとの標本は小さく、1市の値は年によって大きく変わるので、個々の市の順位より、増減の向きを確認してください。

```chart
{
  "height": 1080,
  "layer": [
    {
      "data": {"name": "city_small"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "qty_pct", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "qty_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "生鮮魚介の購入量の変化（%、2019年→2025年）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "減り方が小さい10市",
          "type": "nominal",
          "scale": {
            "domain": ["減り方が小さい10市", "中間", "減り方が大きい10市"],
            "range": ["#94a3b8", "#93c5fd", "#3b82f6"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "city_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "qty_pct", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "qty_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "生鮮魚介の購入量の変化（%、2019年→2025年）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {
            "domain": ["減り方が小さい10市", "中間", "減り方が大きい10市"],
            "range": ["#94a3b8", "#93c5fd", "#3b82f6"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "city_large"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "qty_pct", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "qty_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "生鮮魚介の購入量の変化（%、2019年→2025年）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "減り方が大きい10市",
          "type": "nominal",
          "scale": {
            "domain": ["減り方が小さい10市", "中間", "減り方が大きい10市"],
            "range": ["#94a3b8", "#93c5fd", "#3b82f6"]
          },
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

52市すべてで生鮮魚介の購入量が減っています。減少率は和歌山市の7.5%から仙台市の41.3%までの範囲で、増えた市はありません。全国の22.5%減は、特定の地域の減少によるものではありません。

## 売場と発注の判断にどう使うか

- 棚の面積は、品目ごとの購入量の変化を見て決めます。米や卵のように大きく値上がりしても購入量が減っていない品目があり、値上がり幅だけでは購入量が減る品目を判別できません
- 面積は分類の単位でなく品目の単位で決めます。値上がり幅が同じ範囲の品目でも、購入量は3割減から1割増まで分かれ、同じ魚介・同じ肉類の中でも増減の向きが分かれます
- 担当エリアの市を選んで全国と比較します。生鮮魚介はどの市でも減っていますが、減り方には5倍以上の差があり、全国の値が自エリアにそのまま当てはまるとは限りません

## データの出典

本記事は総務省統計局の家計調査 家計収支編 二人以上の世帯について、[品目別支出金額](https://www.e-stat.go.jp/dbview?sid=0004023605)と[品目別購入数量](https://www.e-stat.go.jp/dbview?sid=0004023606)の年次データを2026年9月2日時点で集計しています。品目分類は2025年改定版で、年次の値は12か月の合計です。地域区分は全国と、47の県庁所在市（東京都は都区部）に川崎市・相模原市・浜松市・堺市・北九州市を加えた52市です。

Queriaは、支出金額と購入数量のように別々に公表される統計表を、品目コードや地域コードを統一し、単位や収録期間をメタデータとして付けて公開しています。本記事で使った[品目別支出金額テーブル](/datasets/queria/e_stat/household/expenditure)と[品目別購入数量テーブル](/datasets/queria/e_stat/household/quantity)を結合すると、担当する品目の単価と購入量を年ごとに確認できます。

```sql id=category
WITH j AS (SELECT q.cat01, q.item_name, q.unit, q.year, q.value AS qty, e.value AS yen FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.area = '00000' AND q.year IN (2019, 2025) AND q.item_level = 3 AND q.cat01 LIKE '010%' AND q.value > 0) SELECT cat01, regexp_replace(item_name, '^[0-9.]+ ', '') AS item, unit, ROUND((MAX(CASE WHEN year = 2025 THEN yen / qty END) / MAX(CASE WHEN year = 2019 THEN yen / qty END) - 1) * 100, 1) AS price_pct, ROUND((MAX(CASE WHEN year = 2025 THEN qty END) / MAX(CASE WHEN year = 2019 THEN qty END) - 1) * 100, 1) AS qty_pct FROM j GROUP BY cat01, item_name, unit HAVING COUNT(*) = 2 ORDER BY price_pct
```

```sql id=quantity_scope
WITH mids AS (SELECT DISTINCT cat01, regexp_replace(item_name, '^[0-9.]+ ', '') AS mid_name FROM e_stat.household.expenditure WHERE cat02 = '03' AND item_parent = '010000000'), q AS (SELECT substr(cat01, 1, 4) || '00000' AS mid_code, COUNT(DISTINCT cat01) AS n FROM e_stat.household.quantity WHERE cat02 = '03' GROUP BY 1) SELECT m.mid_name, COALESCE(q.n, 0) AS quantity_items FROM mids m LEFT JOIN q ON q.mid_code = m.cat01 ORDER BY m.cat01
```

```sql id=household_size
SELECT year, value AS persons FROM e_stat.household.expenditure WHERE cat02 = '03' AND frequency = '年次' AND area = '00000' AND cat01 = '000300000' AND year IN (2019, 2025) ORDER BY year
```

```sql id=rice
SELECT q.year AS year, ROUND(e.value / q.value, 1) AS yen_per_kg, ROUND(q.value, 1) AS kg FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.area = '00000' AND q.cat01 = '010110001' AND q.year BETWEEN 2015 AND 2025 ORDER BY q.year
```

```sql id=band
WITH leaf AS (SELECT DISTINCT cat01 FROM e_stat.household.quantity WHERE cat01 NOT IN (SELECT item_parent FROM e_stat.household.quantity WHERE item_parent IS NOT NULL)), j AS (SELECT q.item_name, q.year, q.value AS qty, e.value AS yen FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.area = '00000' AND q.year IN (2019, 2025) AND q.cat01 LIKE '010%' AND q.cat01 IN (SELECT cat01 FROM leaf) AND q.value > 0), c AS (SELECT regexp_replace(item_name, '^[^ ]+ ', '') AS item, ROUND((MAX(CASE WHEN year = 2025 THEN yen / qty END) / MAX(CASE WHEN year = 2019 THEN yen / qty END) - 1) * 100, 1) AS price_pct, ROUND((MAX(CASE WHEN year = 2025 THEN qty END) / MAX(CASE WHEN year = 2019 THEN qty END) - 1) * 100, 1) AS qty_pct FROM j GROUP BY item_name HAVING COUNT(*) = 2) SELECT item, price_pct, qty_pct FROM c WHERE price_pct BETWEEN 17 AND 23 ORDER BY qty_pct
```

```sql id=others
WITH leaf AS (SELECT DISTINCT cat01 FROM e_stat.household.quantity WHERE cat01 NOT IN (SELECT item_parent FROM e_stat.household.quantity WHERE item_parent IS NOT NULL)), j AS (SELECT q.item_name, q.year, q.value AS qty, e.value AS yen FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.area = '00000' AND q.year IN (2019, 2025) AND q.cat01 LIKE '010%' AND q.cat01 IN (SELECT cat01 FROM leaf) AND q.value > 0), c AS (SELECT regexp_replace(item_name, '^[^ ]+ ', '') AS item, ROUND((MAX(CASE WHEN year = 2025 THEN yen / qty END) / MAX(CASE WHEN year = 2019 THEN yen / qty END) - 1) * 100, 1) AS price_pct, ROUND((MAX(CASE WHEN year = 2025 THEN qty END) / MAX(CASE WHEN year = 2019 THEN qty END) - 1) * 100, 1) AS qty_pct FROM j GROUP BY item_name HAVING COUNT(*) = 2) SELECT item, price_pct, qty_pct FROM c WHERE price_pct NOT BETWEEN 17 AND 23 ORDER BY price_pct
```

```sql id=city_small
WITH j AS (SELECT q.area_name, q.year, q.value AS qty, e.value AS yen FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.year IN (2019, 2025) AND q.cat01 = '010210000' AND q.area <> '00000' AND q.value > 0), c AS (SELECT regexp_replace(area_name, '^[0-9]+ ', '') AS city, ROUND((MAX(CASE WHEN year = 2025 THEN yen / qty END) / MAX(CASE WHEN year = 2019 THEN yen / qty END) - 1) * 100, 1) AS price_pct, ROUND((MAX(CASE WHEN year = 2025 THEN qty END) / MAX(CASE WHEN year = 2019 THEN qty END) - 1) * 100, 1) AS qty_pct FROM j GROUP BY area_name HAVING COUNT(*) = 2), ranked AS (SELECT city, price_pct, qty_pct, ROW_NUMBER() OVER (ORDER BY qty_pct DESC, city) AS rn FROM c) SELECT city, price_pct, qty_pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=city_mid
WITH j AS (SELECT q.area_name, q.year, q.value AS qty, e.value AS yen FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.year IN (2019, 2025) AND q.cat01 = '010210000' AND q.area <> '00000' AND q.value > 0), c AS (SELECT regexp_replace(area_name, '^[0-9]+ ', '') AS city, ROUND((MAX(CASE WHEN year = 2025 THEN yen / qty END) / MAX(CASE WHEN year = 2019 THEN yen / qty END) - 1) * 100, 1) AS price_pct, ROUND((MAX(CASE WHEN year = 2025 THEN qty END) / MAX(CASE WHEN year = 2019 THEN qty END) - 1) * 100, 1) AS qty_pct FROM j GROUP BY area_name HAVING COUNT(*) = 2), ranked AS (SELECT city, price_pct, qty_pct, ROW_NUMBER() OVER (ORDER BY qty_pct DESC, city) AS rn FROM c) SELECT city, price_pct, qty_pct FROM ranked WHERE rn > 10 AND rn <= 42 ORDER BY rn
```

```sql id=city_large
WITH j AS (SELECT q.area_name, q.year, q.value AS qty, e.value AS yen FROM e_stat.household.quantity q JOIN e_stat.household.expenditure e ON e.cat01 = q.cat01 AND e.cat02 = q.cat02 AND e.area = q.area AND e.time = q.time WHERE q.cat02 = '03' AND q.frequency = '年次' AND q.year IN (2019, 2025) AND q.cat01 = '010210000' AND q.area <> '00000' AND q.value > 0), c AS (SELECT regexp_replace(area_name, '^[0-9]+ ', '') AS city, ROUND((MAX(CASE WHEN year = 2025 THEN yen / qty END) / MAX(CASE WHEN year = 2019 THEN yen / qty END) - 1) * 100, 1) AS price_pct, ROUND((MAX(CASE WHEN year = 2025 THEN qty END) / MAX(CASE WHEN year = 2019 THEN qty END) - 1) * 100, 1) AS qty_pct FROM j GROUP BY area_name HAVING COUNT(*) = 2), ranked AS (SELECT city, price_pct, qty_pct, ROW_NUMBER() OVER (ORDER BY qty_pct DESC, city) AS rn FROM c) SELECT city, price_pct, qty_pct FROM ranked WHERE rn > 42 ORDER BY rn
```
