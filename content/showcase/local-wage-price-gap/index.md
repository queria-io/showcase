---
title: 東京との給与の差のうち、物価の差で埋まるのは2割
description: 東京都を100とすると、道府県の年間給与は63〜91、物価は92〜99でした。給与の差のうち物価の差で埋まるのは中央値で2割で、物価で割り戻しても業種によって9〜30ポイントの差が残ります
publishedAt: 2026-10-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 賃金
  - 物価
  - 採用
  - 地域比較
datasets:
  - queria/e_stat
sources:
  - title: 賃金構造基本統計調査
    url: https://www.mhlw.go.jp/toukei/list/chinginkouzou.html
    publisher: 厚生労働省
  - title: 小売物価統計調査（構造編）
    url: https://www.stat.go.jp/data/kouri/kouzou/index.html
    publisher: 総務省統計局
agentHint: 宮城県・広島県・福岡県について、医療・福祉と情報通信の年間給与（所定内給与×12＋年間賞与）を2020〜2024年調査で毎年出して。東京都と比べた比率と、消費者物価地域差指数で割り戻した比率も並べて
socialAnnounce: |-
  東京を100とすると、道府県の年間給与は63〜91、物価は92〜99でした。
  給与の差のうち物価の差で埋まるのは中央値で2割です。

  UIJターン採用の年収設計に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

東京都を100としたとき、東京都以外の46道府県の年間給与は62.8から90.6まで差があり、物価は92.0から98.6の範囲に収まっています。給与の差のうち物価の差と同じ大きさの分は、中央値で20.4%です。給与の差の8割は、物価の差では説明できません。物価で割り戻した給与で東京都を上回る県はなく、同じ業種どうしで比較しても、物価で割り戻した後の差は業種によって8.6ポイントから30.3ポイントあります。

地方の企業が東京で働く人をUIJターンで採用するとき、提示できる年収は東京より低くなることが多く、候補者には「地方は物価が安いので、生活水準は変わらない」と説明されることがあります。給与と物価を都道府県ごとに並べ、この説明が数字に合うかを確認しました。

## 給与は東京の6〜9割、物価は東京の9割強

給与は厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)の都道府県別の値を使います。ここでいう年間給与は、6月分の所定内給与額を12倍し、前年1年間の賞与その他特別給与額を足したものです。所定内給与には残業代などの超過労働給与が入らないので、実際の年収より少し低い値になります。対象はフルタイムで働く一般労働者で、パートなどの短時間労働者は入りません。企業規模は10人以上で、働いている事業所の所在地で都道府県を分けています。

物価は総務省の[小売物価統計調査（構造編）](https://www.stat.go.jp/data/kouri/kouzou/index.html)の消費者物価地域差指数で、e-Stat「社会・人口統計体系」の都道府県別経済基盤データ（`c_pref_economy`）に収録されています。全国平均を100として、同じ品目を全国共通の割合で買ったときの価格の差を表します。2013年以降の系列は費目別に12のカテゴリがあります。

| コード | 内容           |
| ------ | -------------- |
| C5701  | 総合           |
| C5702  | 家賃を除く総合 |
| C5703  | 食料           |
| C5704  | 住居           |
| C5705  | 光熱・水道     |
| C5706  | 家具・家事用品 |
| C5707  | 被服及び履物   |
| C5708  | 保健医療       |
| C5709  | 交通・通信     |
| C5710  | 教育           |
| C5711  | 教養娯楽       |
| C5712  | 諸雑費         |

ここでは家賃を含む総合（`C5701`）を使います。指数は全国共通の支出の割合で品目の値段を重み付けしたものなので、地域差の大きい住居費も、支出全体に占める住居費の割合の分しか指数に反映されません。住まいの広さや車を持つかどうかといった暮らし方の違いも入りません。

給与は2020〜2024年調査、物価は2020〜2024年の5年平均を計算し、どちらも東京都を100とする指数にしました。下の図の点線は、物価が安いのと同じ割合だけ給与が低い場合の線です。点がこの線の上にあれば物価で割り戻した給与が東京都より高く、下にあれば低いことになります。

```chart caption="都道府県別の年間給与と物価（東京都=100、2020〜2024年の平均）"
{
  "layer": [
    {
      "data": {"values": [{"x": 90, "y": 90}, {"x": 100, "y": 100}]},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"x\"]) && isValid(datum[\"y\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "x": {
          "field": "x",
          "type": "quantitative",
          "scale": {"domain": [90, 101], "zero": false, "nice": false},
          "axis": {"title": "物価（東京都=100）", "grid": true}
        },
        "y": {
          "field": "y",
          "type": "quantitative",
          "scale": {"domain": [60, 102], "zero": false, "nice": false},
          "axis": {"title": "年間給与（東京都=100）", "grid": true}
        },
        "color": {
          "datum": "物価の差と同じだけ給与が低い線",
          "type": "nominal",
          "scale": {"domain": ["物価の差と同じだけ給与が低い線", "都道府県"], "range": ["#94a3b8", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pref_total"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "price_idx", "type": "quantitative"},
          {"field": "wage_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "price_idx",
          "type": "quantitative",
          "scale": {"domain": [90, 101], "zero": false, "nice": false},
          "axis": {"title": "物価（東京都=100）", "grid": true}
        },
        "y": {
          "field": "wage_idx",
          "type": "quantitative",
          "scale": {"domain": [60, 102], "zero": false, "nice": false},
          "axis": {"title": "年間給与（東京都=100）", "grid": true}
        },
        "color": {
          "datum": "都道府県",
          "type": "nominal",
          "scale": {"domain": ["物価の差と同じだけ給与が低い線", "都道府県"], "range": ["#94a3b8", "#3b82f6"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

産業計の給与は、年齢・業種・企業規模の構成が違う働き手の平均どうしの比較で、同じ仕事に就いたときの給与の差ではありません。東京都の年間給与は5年平均で567.5万円です。東京都以外で最も高い神奈川県が90.6、最も低い青森県が62.8で、中央値は74.5です。物価は最も安い宮崎県が92.0、最も高い神奈川県が98.6で、中央値は94.5です。すべての道府県が点線より大きく下にあります。

給与の差のうち、物価の差と同じ大きさの分がどれだけを占めるかを県ごとに計算すると、中央値は20.4%でした。最も大きい愛知県でも43.7%で、46道府県のうち40で3割に届きません。青森県なら給与の差は37.2ポイント、物価の差は6.0ポイントです。給与が東京都の7割に届かない14県では、この割合はどこも23.4%以下です。給与が低い県ほど物価も安いという関係は弱く、46道府県の給与と物価の指数の相関係数は0.28です。

給与の指数を物価の指数で割ると、物価の差を差し引いた給与の水準になります。青森県は62.8が66.9になり、東京都との差は37.2ポイントから33.1ポイントに縮むだけです。割り戻した後の値は、46道府県で沖縄県の66.8から大阪府の92.1までで、東京都に届く県はありません。

```sql
SELECT * FROM pref_total
```

## 同じ業種どうしで比較しても、物価で割り戻した給与の中央値は東京都の80.3

東京都には金融や情報通信のような給与の高い業種が集まっているので、産業計の差には業種の構成の違いが含まれます。業種別のテーブル（`prefecture_industry_wage`）を使い、同じ業種の中で東京都と比較しました。業種は日本標準産業分類の大分類で、鉱業は標本が少なく欠ける県があるため除いた15業種です。都道府県×業種の値は標本調査からの推計で、組み合わせによっては年ごとに大きく変わるので、ここでも5年平均を使っています。

46道府県×15業種の690通りで見ると、東京都の同じ業種と比較した年間給与の中央値は75.8で、産業計の74.5とほとんど変わりません。物価で割り戻しても中央値は80.3です。業種を統一しても、差の大きさは産業計と同じ程度です。同じ業種でも東京都には本社や大企業が多く、ここで比較しているのは、その県のその業種で働く人の平均どうしです。

業種ごとに46道府県の中央値を計算すると、物価で割り戻した後に残る差は業種によって3倍以上違います。

```chart caption="業種別の年間給与（東京都=100、46道府県の中央値、2020〜2024年の平均）"
{
  "height": 520,
  "layer": [
    {
      "data": {"name": "industry_gap"},
      "transform": [
        {"fold": ["wage_idx", "adjusted_idx"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"wage_idx\": \"給与\", \"adjusted_idx\": \"物価で割り戻した給与\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"wage_idx\",\"adjusted_idx\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "industry_label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"domain": [50, 100], "zero": false, "nice": false},
          "axis": {"title": "東京都=100", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["給与", "物価で割り戻した給与"], "range": ["#93c5fd", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["物価で割り戻した給与", "給与"]},
        "tooltip": [
          {"field": "industry_label", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

物価で割り戻した後の差が最も大きいのは不動産業・物品賃貸業で、給与は66.4、割り戻して69.7です。卸売業・小売業が73.4、金融業・保険業が74.4で続きます。差が最も小さいのは医療・福祉で、給与は85.8、割り戻して91.4です。電気・ガス・熱供給・水道業の91.0、情報通信業の87.4がこれに次ぎます。物価で割り戻した後に残る差は、不動産業・物品賃貸業の30.3ポイントに対して医療・福祉は8.6ポイントです。

690通りのうち、物価で割り戻すと東京都の同じ業種と同じかそれを上回るのは次の9通りだけです。このうち神奈川県の2つは、割り戻す前から東京都を上回っています。次の図で100.0と表示される愛知県の生活関連サービス・娯楽は、丸める前の値が100をわずかに下回るため、この9通りには入りません。

```sql id=cell_above display
-- 物価の差で割り戻すと東京都と同じか上回る組み合わせ
WITH wage AS (
  SELECT industry_code, industry, area_name,
    AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_industry_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0'
    AND area_name <> '全国' AND industry_code <> 'C'
  GROUP BY industry_code, industry, area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.industry_code, w.industry, w.area_name,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER (PARTITION BY w.industry_code) AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER (PARTITION BY w.industry_code) AS price_idx
  FROM wage w JOIN price p USING (area_name)
)
SELECT area_name AS 都道府県, CASE industry_code
    WHEN 'D' THEN '建設' WHEN 'E' THEN '製造' WHEN 'F' THEN '電気・ガス・水道'
    WHEN 'G' THEN '情報通信' WHEN 'H' THEN '運輸・郵便' WHEN 'I' THEN '卸売・小売'
    WHEN 'J' THEN '金融・保険' WHEN 'K' THEN '不動産・物品賃貸' WHEN 'L' THEN '学術研究・専門サービス'
    WHEN 'M' THEN '宿泊・飲食' WHEN 'N' THEN '生活関連サービス・娯楽' WHEN 'O' THEN '教育・学習支援'
    WHEN 'P' THEN '医療・福祉' WHEN 'Q' THEN '複合サービス' WHEN 'R' THEN 'その他のサービス'
  END AS 業種,
  ROUND(wage_idx, 1) AS 給与_東京100,
  ROUND(price_idx, 1) AS 物価_東京100,
  ROUND(100 * wage_idx / price_idx, 1) AS 物価で割り戻した給与_東京100
FROM idx
WHERE area_name <> '東京都' AND 100 * wage_idx / price_idx >= 100
ORDER BY 100 * wage_idx / price_idx DESC, area_name
```

## 同じ県の中でも、業種によって東京都との差は中央値で23.7ポイント違う

採用の現場で必要なのは、自社の所在県と業種の組み合わせでの値です。下の図は、46道府県×15業種のすべてについて、物価で割り戻した年間給与を東京都の同じ業種を100として並べたものです。行は産業計の同じ指数が高い県ほど上にあります。

```chart caption="物価で割り戻した年間給与（東京都の同じ業種=100、2020〜2024年の平均）"
{
  "height": 1080,
  "layer": [
    {
      "data": {"name": "heat"},
      "mark": {"type": "rect"},
      "encoding": {
        "tooltip": [
          {"field": "industry_label", "type": "nominal"},
          {"field": "area_name", "type": "nominal"},
          {"field": "adjusted_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "industry_label",
          "type": "nominal",
          "axis": {"title": null, "labelAngle": -45, "orient": "top"},
          "sort": null
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "field": "adjusted_idx",
          "type": "quantitative",
          "scale": {"range": ["#ef4444", "#fef3c7", "#ffffff", "#3b82f6"]}
        }
      }
    },
    {
      "data": {"name": "heat"},
      "transform": [
        {"calculate": "\"\" + format(datum[\"adjusted_idx\"], \".1f\") + \"\"", "as": "__label"}
      ],
      "mark": {"type": "text", "fontSize": 12},
      "encoding": {
        "x": {
          "field": "industry_label",
          "type": "nominal",
          "axis": {"title": null, "labelAngle": -45, "orient": "top"},
          "sort": null
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "text": {"field": "__label"}
      }
    }
  ]
}
```

赤いほど東京都との差が大きい組み合わせで、青い組み合わせは東京都を上回ります。最も差が大きいのは高知県の不動産業・物品賃貸業で56.8でした。同じ県の中でも業種によって値は大きく異なり、最も高い業種と最も低い業種の差は46道府県の中央値で23.7ポイント、40の道府県で20ポイント以上あります。自社の業種の差は、県全体の平均からは見積もれません。

## 採用の現場での使い方

- 候補者に年収を提示するとき、東京との差を物価の安さだけで説明しないようにします。物価の差で埋まるのは給与の差の2割程度なので、残りは住まいの広さや通勤時間のような、物価指数に入らない条件で示す必要があります
- 自社の所在県と業種の組み合わせで、東京の同じ業種との差の目安を持っておきます。不動産業・物品賃貸業、卸売業・小売業、金融業・保険業は差が大きく、医療・福祉、電気・ガス・熱供給・水道業、情報通信業は小さい業種です

## データの出典

本記事は厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)の都道府県別の一般労働者の賃金（2020〜2024年調査）と、総務省の[小売物価統計調査（構造編）](https://www.stat.go.jp/data/kouri/kouzou/index.html)の消費者物価地域差指数（2020〜2024年）を、2026年10月13日時点で集計しています。

Queriaは、賃金構造基本統計調査や社会・人口統計体系をはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の賃金テーブル](/datasets/queria/e_stat/wage_structure/prefecture_wage)、[都道府県・業種別の賃金テーブル](/datasets/queria/e_stat/wage_structure/prefecture_industry_wage)、[都道府県別の経済基盤データ](/datasets/queria/e_stat/ssds/c_pref_economy)から、自社の県と業種で東京都との差を確認できます。

```sql id=pref_total
-- 都道府県別の年間給与（産業計・男女計の所定内給与×12＋年間賞与）と消費者物価地域差指数（総合）を、2020〜2024年の5年平均にして東京都=100で表す
WITH wage AS (
  SELECT area_name, AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0' AND area_name <> '全国'
  GROUP BY area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.area_name, w.annual,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER () AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER () AS price_idx
  FROM wage w JOIN price p USING (area_name)
)
SELECT area_name,
  ROUND(annual / 10, 1) AS annual_man_yen,
  ROUND(wage_idx, 1) AS wage_idx,
  ROUND(price_idx, 1) AS price_idx,
  ROUND(100 * wage_idx / price_idx, 1) AS adjusted_idx,
  CASE WHEN area_name <> '東京都' THEN ROUND(100 * (100 - price_idx) / (100 - wage_idx), 1) END AS covered_pct
FROM idx
ORDER BY wage_idx DESC, area_name
```

```sql id=pref_summary
-- 東京都を除く46道府県の要約（プロットはしない）。covered_pct は東京都との給与の差のうち、物価の差と同じ大きさの分が占める割合
WITH wage AS (
  SELECT area_name, AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0' AND area_name <> '全国'
  GROUP BY area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.area_name, w.annual,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER () AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER () AS price_idx
  FROM wage w JOIN price p USING (area_name)
), t AS (
  SELECT area_name, annual, wage_idx, price_idx,
    100 * wage_idx / price_idx AS adjusted_idx,
    100 * (100 - price_idx) / (100 - wage_idx) AS covered_pct
  FROM idx WHERE area_name <> '東京都'
)
SELECT
  ROUND((SELECT annual FROM idx WHERE area_name = '東京都') / 10, 1) AS tokyo_man_yen,
  ROUND(MIN(wage_idx), 1) AS min_wage_idx,
  ARG_MIN(area_name, wage_idx) AS min_wage_pref,
  ROUND(MAX(wage_idx), 1) AS max_wage_idx,
  ARG_MAX(area_name, wage_idx) AS max_wage_pref,
  ROUND(MIN(price_idx), 1) AS min_price_idx,
  ARG_MIN(area_name, price_idx) AS min_price_pref,
  ROUND(MAX(price_idx), 1) AS max_price_idx,
  ROUND(MEDIAN(wage_idx), 1) AS median_wage_idx,
  ROUND(MEDIAN(price_idx), 1) AS median_price_idx,
  ROUND(MEDIAN(covered_pct), 1) AS median_covered_pct,
  ROUND(MAX(covered_pct), 1) AS max_covered_pct,
  ARG_MAX(area_name, covered_pct) AS max_covered_pref,
  COUNT(*) FILTER (WHERE covered_pct < 30) AS n_covered_under_30,
  COUNT(*) FILTER (WHERE wage_idx < 70) AS n_wage_under_70,
  ROUND(MAX(covered_pct) FILTER (WHERE wage_idx < 70), 1) AS max_covered_wage_under_70,
  ROUND(MIN(adjusted_idx), 1) AS min_adjusted_idx,
  ROUND(MAX(adjusted_idx), 1) AS max_adjusted_idx,
  ROUND(CORR(wage_idx, price_idx), 2) AS corr_wage_price,
  COUNT(*) AS n_pref
FROM t
```

```sql id=industry_gap
-- 業種別に、東京都を100とした年間給与の指数と、物価の差で割り戻した指数を出し、46道府県の中央値をとる（2020〜2024年の5年平均）
WITH wage AS (
  SELECT industry_code, industry, area_name,
    AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_industry_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0'
    AND area_name <> '全国' AND industry_code <> 'C'
  GROUP BY industry_code, industry, area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.industry_code, w.industry, w.area_name,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER (PARTITION BY w.industry_code) AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER (PARTITION BY w.industry_code) AS price_idx
  FROM wage w JOIN price p USING (area_name)
)
SELECT
  CASE industry_code
    WHEN 'D' THEN '建設' WHEN 'E' THEN '製造' WHEN 'F' THEN '電気・ガス・水道'
    WHEN 'G' THEN '情報通信' WHEN 'H' THEN '運輸・郵便' WHEN 'I' THEN '卸売・小売'
    WHEN 'J' THEN '金融・保険' WHEN 'K' THEN '不動産・物品賃貸' WHEN 'L' THEN '学術研究・専門サービス'
    WHEN 'M' THEN '宿泊・飲食' WHEN 'N' THEN '生活関連サービス・娯楽' WHEN 'O' THEN '教育・学習支援'
    WHEN 'P' THEN '医療・福祉' WHEN 'Q' THEN '複合サービス' WHEN 'R' THEN 'その他のサービス'
  END AS industry_label,
  industry,
  ROUND(MEDIAN(wage_idx), 1) AS wage_idx,
  ROUND(MEDIAN(100 * wage_idx / price_idx), 1) AS adjusted_idx
FROM idx
WHERE area_name <> '東京都'
GROUP BY industry_code, industry
ORDER BY adjusted_idx, industry_code
```

```sql id=cell_summary
-- 46道府県×15業種の690通りの要約（プロットはしない）。鉱業は標本が少なく欠けるセルがあるので除く
WITH wage AS (
  SELECT industry_code, industry, area_name,
    AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_industry_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0'
    AND area_name <> '全国' AND industry_code <> 'C'
  GROUP BY industry_code, industry, area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.industry_code, w.industry, w.area_name,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER (PARTITION BY w.industry_code) AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER (PARTITION BY w.industry_code) AS price_idx
  FROM wage w JOIN price p USING (area_name)
)
SELECT
  COUNT(*) AS n_cells,
  ROUND(MEDIAN(wage_idx), 1) AS median_wage_idx,
  ROUND(MEDIAN(100 * wage_idx / price_idx), 1) AS median_adjusted_idx,
  COUNT(*) FILTER (WHERE wage_idx >= 100) AS n_wage_above_tokyo,
  COUNT(*) FILTER (WHERE 100 * wage_idx / price_idx >= 100) AS n_adjusted_above_tokyo
FROM idx
WHERE area_name <> '東京都'
```

```sql id=pref_industry_spread
-- 同じ県の中で、物価で割り戻した年間給与（東京都の同じ業種=100）が業種によってどれだけ開くか（プロットはしない）
WITH wage AS (
  SELECT industry_code, industry, area_name,
    AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_industry_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0'
    AND area_name <> '全国' AND industry_code <> 'C'
  GROUP BY industry_code, industry, area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.industry_code, w.industry, w.area_name,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER (PARTITION BY w.industry_code) AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER (PARTITION BY w.industry_code) AS price_idx
  FROM wage w JOIN price p USING (area_name)
), cell AS (
  SELECT i.area_name, 100 * i.wage_idx / i.price_idx AS adjusted_idx
  FROM idx i
  WHERE i.area_name <> '東京都'
), rng AS (
  SELECT area_name, MAX(adjusted_idx) - MIN(adjusted_idx) AS spread
  FROM cell
  GROUP BY area_name
)
SELECT COUNT(*) AS n_pref,
  COUNT(*) FILTER (WHERE spread >= 20) AS n_spread_20_or_more,
  ROUND(MEDIAN(spread), 1) AS median_spread
FROM rng
```

```sql id=heat
-- 都道府県×業種の、物価の差で割り戻した年間給与（東京都=100）。行は産業計の同じ指数が高い順に上から並べる
WITH wage AS (
  SELECT industry_code, industry, area_name,
    AVG(scheduled_earnings * 12 + annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_industry_wage
  WHERE year BETWEEN 2020 AND 2024 AND sex_code = '0'
    AND area_name <> '全国' AND industry_code <> 'C'
  GROUP BY industry_code, industry, area_name
), price AS (
  SELECT area_name, AVG(TRY_CAST(value AS DOUBLE)) AS price
  FROM e_stat.ssds.c_pref_economy
  WHERE cat01 = 'C5701' AND year BETWEEN 2020 AND 2024
    AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND area_name <> '全国'
  GROUP BY area_name
), idx AS (
  SELECT w.industry_code, w.industry, w.area_name,
    100 * w.annual / MAX(CASE WHEN w.area_name = '東京都' THEN w.annual END) OVER (PARTITION BY w.industry_code) AS wage_idx,
    100 * p.price / MAX(CASE WHEN w.area_name = '東京都' THEN p.price END) OVER (PARTITION BY w.industry_code) AS price_idx
  FROM wage w JOIN price p USING (area_name)
), total AS (
  SELECT w.area_name,
    AVG(w.scheduled_earnings * 12 + w.annual_special_earnings) AS annual
  FROM e_stat.wage_structure.prefecture_wage w
  WHERE w.year BETWEEN 2020 AND 2024 AND w.sex_code = '0' AND w.area_name <> '全国'
  GROUP BY w.area_name
), total_idx AS (
  SELECT t.area_name,
    (t.annual / MAX(CASE WHEN t.area_name = '東京都' THEN t.annual END) OVER ())
      / (p.price / MAX(CASE WHEN t.area_name = '東京都' THEN p.price END) OVER ()) AS total_adj
  FROM total t JOIN price p USING (area_name)
)
SELECT i.area_name, CASE industry_code
    WHEN 'D' THEN '建設' WHEN 'E' THEN '製造' WHEN 'F' THEN '電気・ガス・水道'
    WHEN 'G' THEN '情報通信' WHEN 'H' THEN '運輸・郵便' WHEN 'I' THEN '卸売・小売'
    WHEN 'J' THEN '金融・保険' WHEN 'K' THEN '不動産・物品賃貸' WHEN 'L' THEN '学術研究・専門サービス'
    WHEN 'M' THEN '宿泊・飲食' WHEN 'N' THEN '生活関連サービス・娯楽' WHEN 'O' THEN '教育・学習支援'
    WHEN 'P' THEN '医療・福祉' WHEN 'Q' THEN '複合サービス' WHEN 'R' THEN 'その他のサービス'
  END AS industry_label,
  ROUND(100 * i.wage_idx / i.price_idx, 1) AS adjusted_idx
FROM idx i JOIN total_idx t USING (area_name)
WHERE i.area_name <> '東京都'
ORDER BY t.total_adj, i.area_name, i.industry_code
```
