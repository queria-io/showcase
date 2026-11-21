---
title: 中古マンションの㎡単価は、東京都では築20年で築浅の約77%、地方では約53%になる
description: 不動産取引価格情報の2022〜2024年の中古マンション取引を、築年数別・地域別に集計しました。全国の㎡単価は築浅の約100万円から築30年代前半の約25万円まで下がって下げ止まります。築20年の価格維持率は東京都が約77%、その他地方が約53%です。
publishedAt: 2026-06-10
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 不動産
  - 中古マンション
  - 資産性
datasets:
  - queria/reinfolib
sources:
  - title: 不動産情報ライブラリ（不動産取引価格情報）
    url: https://www.reinfolib.mlit.go.jp/
    publisher: 国土交通省
agentHint: 福岡県の中古マンションの築年数別㎡単価カーブを出して。東京都のように下げ止まりが高い位置に来るのか、地方寄りの下がり方かを比べて
socialAnnounce: |-
  中古マンションの取引データを築年数別に分析し、価格の下げ止まりと資産性の地域差を見ました。

  物件購入の見極めや不動産投資の出口戦略に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2022〜2024年の中古マンションの取引では、全国の㎡単価の中央値は築0〜1年の約100万円から、築25年で約43万円、築30年代前半で約25万円まで下がり、そこから下げ止まります。築0〜4年の㎡単価を100とした価格維持率は、築20年で東京都が約77%、主要都市圏が約55%、その他地方が約53%です。築20年の㎡単価は、東京都が約105万円、その他地方が約30万円でした。

中古マンションの購入・売却・投資では、築何年でどれだけ価格が下がり、どこで下げ止まるか、その下がり方が地域でどう違うかを把握しておくと、買う時期や売却時の価格を見積もりやすくなります。この記事では、国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)の不動産取引価格情報から、中古マンションの築年数と㎡単価の関係を集計します。

## 全国の㎡単価は築30年代前半の約25万円で下げ止まる

不動産情報ライブラリの不動産取引価格情報（`mart_trade_prices`）には、物件種別・所在地・面積・取引価格・建築年などが入っています。主な物件種別は次のとおりです。

| 物件種別         | 内容                             |
| ---------------- | -------------------------------- |
| 宅地(土地と建物) | 一戸建て（土地付き）             |
| 宅地(土地)       | 更地・宅地                       |
| 中古マンション等 | 中古マンション・テラスハウスなど |
| 農地             | 田・畑                           |
| 林地             | 山林                             |

中古マンション等（`property_type = '中古マンション等'`）に絞り、取引年（`year`）から建築年（`building_year`、例: `1991年`）を引いて築年数を求めました。建築年が数字で読み取れない行は除いています。市況の変動を築年数の影響と区別するため、取引は直近3年（2022〜2024年）に限り、築年数ごとに㎡単価（取引価格 ÷ 専有面積）の中央値を求めました。対象は築0〜45年で、取引が50件に満たない築年は除いています。

```chart
{
  "layer": [
    {
      "data": {"name": "age_curve"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age\"]) && isValid(datum[\"unit_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "age", "type": "quantitative"},
          {"field": "unit_man", "type": "quantitative"}
        ],
        "x": {
          "field": "age",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "unit_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

築0〜1年の㎡単価は約100万円で、築15年で約65万円（築浅の約3分の2）、築25年で約43万円（半分以下）、築30年代前半で約25万円（約4分の1）まで下がります。築35年以降はおおむね28〜33万円の範囲で、わずかに上がっています。価格が大きく下がるのは築25年ごろまでで、それより古い物件は今後の値下がりが小さいと考えられます。

この集計は、同じ物件を何年も追ったものではなく、築年数の違う物件を同じ時期に並べて比較したものです。築年数の古い物件で取引されているのは、立地の良い都心部などの物件に偏ると考えられ、下げ止まったあとにわずかに上がるのはそのためと考えられます。

## 築20年の㎡単価は、東京都が約105万円、その他地方が約30万円

東京都、主要都市圏（大阪・愛知・神奈川・埼玉・千葉・兵庫・京都・福岡の8府県）、その他地方の3グループに分け、5年ごとの築年帯で㎡単価の中央値を比較しました。この3区分は本記事で設けたもので、統計上の区分ではありません。取引が30件未満の築年帯は除いています。

```chart
{
  "layer": [
    {
      "data": {"name": "region_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_band\"]) && isValid(datum[\"unit_man\"]) ? 0 : 1",
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
          {"field": "age_band", "type": "quantitative"},
          {"field": "unit_man", "type": "quantitative"}
        ],
        "x": {
          "field": "age_band",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "unit_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "主要都市圏", "その他地方"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_metro"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_band\"]) && isValid(datum[\"unit_man\"]) ? 0 : 1",
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
          {"field": "age_band", "type": "quantitative"},
          {"field": "unit_man", "type": "quantitative"}
        ],
        "x": {
          "field": "age_band",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "unit_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "主要都市圏",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "主要都市圏", "その他地方"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_rural"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_band\"]) && isValid(datum[\"unit_man\"]) ? 0 : 1",
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
          {"field": "age_band", "type": "quantitative"},
          {"field": "unit_man", "type": "quantitative"}
        ],
        "x": {
          "field": "age_band",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "unit_man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "㎡単価中央値（万円）", "grid": true}
        },
        "color": {
          "datum": "その他地方",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "主要都市圏", "その他地方"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
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

築0〜4年の㎡単価は東京都が約137万円、主要都市圏が約92万円、その他地方が約57万円で、2倍以上の差があります。この差は築年数が進んでも縮まりません。築20年では東京都が約105万円、主要都市圏が約51万円、その他地方が約30万円です。下げ止まる水準も、東京都が60万円台、地方は15〜17万円前後です。

## 築20年の価格維持率は、東京都が約77%、地方は約5割

各グループの築0〜4年の㎡単価を100として、築年数ごとの価格維持率を求めました。

```chart
{
  "layer": [
    {
      "data": {"name": "region_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_band\"]) && isValid(datum[\"rel\"]) ? 0 : 1",
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
          {"field": "age_band", "type": "quantitative"},
          {"field": "rel", "type": "quantitative"}
        ],
        "x": {
          "field": "age_band",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "rel",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築浅（築0〜4年）を100とした価格水準", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "主要都市圏", "その他地方"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_metro"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_band\"]) && isValid(datum[\"rel\"]) ? 0 : 1",
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
          {"field": "age_band", "type": "quantitative"},
          {"field": "rel", "type": "quantitative"}
        ],
        "x": {
          "field": "age_band",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "rel",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築浅（築0〜4年）を100とした価格水準", "grid": true}
        },
        "color": {
          "datum": "主要都市圏",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "主要都市圏", "その他地方"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "region_rural"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_band\"]) && isValid(datum[\"rel\"]) ? 0 : 1",
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
          {"field": "age_band", "type": "quantitative"},
          {"field": "rel", "type": "quantitative"}
        ],
        "x": {
          "field": "age_band",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築年数（年）", "format": "d"}
        },
        "y": {
          "field": "rel",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "築浅（築0〜4年）を100とした価格水準", "grid": true}
        },
        "color": {
          "datum": "その他地方",
          "type": "nominal",
          "scale": {
            "domain": ["東京都", "主要都市圏", "その他地方"],
            "range": ["#ef4444", "#3b82f6", "#94a3b8"]
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

東京都は築20年で約77%、築30年で約51%です。主要都市圏は築20年で約55%、その他地方は約53%で、築20年で築浅のほぼ半分になります。築30年では主要都市圏が約32%、その他地方が約30%です。同じ築年数で、東京都の価格維持率は地方の1.5倍前後です。

地方では価格が早く下がるので、築年数の古い物件を相対的に安く購入できます。価格の維持を重視するか、購入費用を抑えるかで、選ぶ地域と築年数は変わります。

価格維持率は、ある物件が築20年でこれだけ値下がりするという予測ではありません。専有面積・駅からの距離・管理状態の違いも調整していないので、同じ築年帯の中の価格差はこの集計では分かりません。

## 購入・投資での使い方

- 購入時期の検討: 価格が大きく下がる築25年ごろまでと、下げ止まった築30年以降では、値下がりのリスクが違う。下げ止まったあとの物件は、今後の値下がりが小さい
- 価格の維持か購入費用か: 価格の維持を重視するなら維持率の高い東京都などの都市部、購入費用を抑えるなら水準も維持率も低い地方、と地域を選び分ける
- 投資の売却時の価格: 購入時の築年数から、保有期間中にどれだけ価格が下がるかを見積もり、売却時の想定価格を求める
- 借入・担保評価: 築年数が進むほど担保価値が下がるので、借入可能額や返済期間への影響を事前に見込む

## データの出典

本記事は国土交通省の[不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)が公開する不動産取引価格情報を、2026年7月11日時点で取得して集計しています。対象は2022〜2024年に成約した中古マンション等の取引です。

Queriaは、国土交通省の不動産取引価格情報を、列名・単位・文字コードを統一し、物件種別や列の説明を付けて公開しています。本記事で使った[不動産取引価格テーブル](/datasets/queria/reinfolib/main/mart_trade_prices)から、関心のあるエリアの築年数別の㎡単価を確認したり、物件種別ごとに価格の下がり方を比較したりできます。

```sql id=age_curve
SELECT (year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) AS age, ROUND(MEDIAN(trade_price / NULLIF(area, 0)) / 10000, 1) AS unit_man FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND building_year SIMILAR TO '[0-9]+年' AND year BETWEEN 2022 AND 2024 AND (year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) BETWEEN 0 AND 45 GROUP BY age HAVING COUNT(*) >= 50 ORDER BY age
```

```sql id=region_tokyo
WITH d AS (SELECT (CAST((year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) / 5 AS INT) * 5) AS age_band, trade_price / NULLIF(area, 0) AS unit FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND building_year SIMILAR TO '[0-9]+年' AND year BETWEEN 2022 AND 2024 AND prefecture = '東京都' AND (year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) BETWEEN 0 AND 40), agg AS (SELECT age_band, MEDIAN(unit) AS unit FROM d GROUP BY age_band HAVING COUNT(*) >= 30) SELECT age_band, ROUND(unit / 10000, 1) AS unit_man, ROUND(unit / FIRST_VALUE(unit) OVER (ORDER BY age_band) * 100, 1) AS rel FROM agg ORDER BY age_band
```

```sql id=region_metro
WITH d AS (SELECT (CAST((year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) / 5 AS INT) * 5) AS age_band, trade_price / NULLIF(area, 0) AS unit FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND building_year SIMILAR TO '[0-9]+年' AND year BETWEEN 2022 AND 2024 AND prefecture IN ('大阪府', '愛知県', '神奈川県', '埼玉県', '千葉県', '兵庫県', '京都府', '福岡県') AND (year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) BETWEEN 0 AND 40), agg AS (SELECT age_band, MEDIAN(unit) AS unit FROM d GROUP BY age_band HAVING COUNT(*) >= 30) SELECT age_band, ROUND(unit / 10000, 1) AS unit_man, ROUND(unit / FIRST_VALUE(unit) OVER (ORDER BY age_band) * 100, 1) AS rel FROM agg ORDER BY age_band
```

```sql id=region_rural
WITH d AS (SELECT (CAST((year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) / 5 AS INT) * 5) AS age_band, trade_price / NULLIF(area, 0) AS unit FROM reinfolib.main.mart_trade_prices WHERE property_type = '中古マンション等' AND area > 0 AND trade_price > 0 AND building_year SIMILAR TO '[0-9]+年' AND year BETWEEN 2022 AND 2024 AND prefecture NOT IN ('東京都', '大阪府', '愛知県', '神奈川県', '埼玉県', '千葉県', '兵庫県', '京都府', '福岡県') AND (year - CAST(REGEXP_EXTRACT(building_year, '[0-9]+') AS INT)) BETWEEN 0 AND 40), agg AS (SELECT age_band, MEDIAN(unit) AS unit FROM d GROUP BY age_band HAVING COUNT(*) >= 30) SELECT age_band, ROUND(unit / 10000, 1) AS unit_man, ROUND(unit / FIRST_VALUE(unit) OVER (ORDER BY age_band) * 100, 1) AS rel FROM agg ORDER BY age_band
```
