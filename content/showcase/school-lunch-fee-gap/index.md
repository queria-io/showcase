---
title: 小学校の給食費が0円の市が、全国81市のうち11。2019年までは最も高い市でも安い市の1.5倍でした
description: 公立小学校の給食費を市別に2015年から2025年まで並べました。2019年まで最大1.5倍だった81市の差は、2025年には0円の市が11、最高は年68,405円に開いています。
ogDescription: 公立小学校の給食費を市別に2015年から2025年まで並べました。2019年まで最大1.5倍だった81市の差は、2025年には0円の市が11、最高は年68,405円です。
publishedAt: 2026-09-21
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 学校給食
  - 小売物価統計
  - 自治体財政
datasets:
  - queria/e_stat
sources:
  - title: 小売物価統計調査
    url: https://www.stat.go.jp/data/kouri/index.html
    publisher: 総務省統計局
  - title: 地方財政状況調査
    url: https://www.e-stat.go.jp/stat-search/files?toukei=00200251
    publisher: 総務省
agentHint: 学校給食(中学校)の品目コード02183で、2015年から2025年までの市別の年額を出して。2025年に0円になった市が2019年にいくら払っていたかも並べて
socialAnnounce: |-
  公立小学校の給食費を、市別に2015年から2025年まで並べました。

  2019年まで81市の差は最大1.5倍でしたが、2025年は0円の市が11、最高は年68,405円です。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2025年に公立小学校の給食費が0円の市は、全国81市のうち11市でした。最も高いのは長岡市の年68,405円です。2019年までは最も高い市と最も安い市の差は1.5倍以内で、0円の市はありませんでした。中央値は2015年の年46,310円から2025年の年48,071円への3.8%増で、ほとんど変わっていません。

公立小学校の給食費は、食材費にあたる分を保護者が負担し、額は市が決めます。2026年度からは国による[学校給食費の抜本的な負担軽減](https://www.mext.go.jp/a_menu/sports/syokuiku/kyu-lighten.html)が始まりました。この記事では、総務省統計局の[小売物価統計調査](https://www.stat.go.jp/data/kouri/index.html)が市ごとに調べている給食費の年額を、2015年から2025年まで並べます。保護者が実際に支払った額なので、市が独自に負担をなくした場合は0円として記録されます。

## 中央値はほとんど変わらず、最高値は上がり、最低値は0円になった

使うのは、小売物価統計調査（動向編）の調査品目の年平均価格です。学校給食は次の2品目が入っています。

| コード | 品目名           |
| ------ | ---------------- |
| 2182   | 学校給食(小学校) |
| 2183   | 学校給食(中学校) |

まず学校給食(小学校)（`02182`）を使います。調査対象は都道府県庁所在市と人口15万以上の市で、2015年以降は81市です。値は年額で、年額は2015年分から入っています。次の図は、各年の最高値・中央値・最低値です。

```chart
{
  "layer": [
    {
      "data": {"name": "spread"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"max_fee\"]) ? 0 : 1",
          "as": "__gap"
        },
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
          {"field": "max_fee", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "max_fee",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "color": {
          "datum": "最高値",
          "type": "nominal",
          "scale": {"domain": ["最高値", "中央値", "最低値"], "range": ["#ef4444", "#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "spread"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"med_fee\"]) ? 0 : 1",
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
          {"field": "med_fee", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "med_fee",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "color": {
          "datum": "中央値",
          "type": "nominal",
          "scale": {"domain": ["最高値", "中央値", "最低値"], "range": ["#ef4444", "#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "spread"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"min_fee\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "min_fee", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "min_fee",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "color": {
          "datum": "最低値",
          "type": "nominal",
          "scale": {"domain": ["最高値", "中央値", "最低値"], "range": ["#ef4444", "#3b82f6", "#94a3b8"]},
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

2015年から2019年までの5年間は、最高値はどの年も長野市で年55,764円から57,817円、最低値は年38,573円から40,581円でした。最高値と最低値の差は、最も大きい2019年でも1.5倍です。中央値は年46,310円から47,447円の間で、ほとんど変わっていません。

2020年は全体が下がり、中央値が年45,058円、最低値は大阪市の年11,417円です。この年は一斉休校で給食が提供されない期間があったので、年額がその分低くなったと考えられます。

2021年以降は、最低値は2021年に0円になり、その後も0円です。最高値は2022年の長野市58,786円の後、2023年からは長岡市になり、2025年は年68,405円でした。中央値は2025年が年48,071円で、2015年の46,310円から3.8%の増加です。中央値の市の負担はほぼ変わらず、最高値と最低値の差が広がっています。

## 0円になった11市の2019年の給食費は、年42,240円から52,695円

2025年に給食費が0円の11市について、2019年と2023年の額を並べます。

```sql
SELECT regexp_replace(p25.area_name, '【.*$', '') AS '市', CAST(ROUND(p19.value) AS BIGINT) AS '2019年（円）', CAST(ROUND(p23.value) AS BIGINT) AS '2023年（円）', CAST(ROUND(p25.value) AS BIGINT) AS '2025年（円）' FROM e_stat.retail_price.item_price p25 JOIN e_stat.retail_price.item_price p19 ON p19.area = p25.area AND p19.cat02 = p25.cat02 AND p19.year = 2019 JOIN e_stat.retail_price.item_price p23 ON p23.area = p25.area AND p23.cat02 = p25.cat02 AND p23.year = 2023 WHERE p25.cat02 = '02182' AND p25.year = 2025 AND p25.value = 0 ORDER BY p19.value DESC
```

11市の2019年の額は、日立市の年42,240円から郡山市の年52,695円までです。同じ年の81市の中央値は47,300円なので、0円になった市が、もともと負担の軽い市だったわけではありません。

この統計は年の平均をとるので、年の途中で負担がなくなった市の値は、支払った月と支払わなかった月の平均になります。2023年の青森市の年6,045円、日立市の年8,640円、和歌山市の年8,560円がこれにあたり、いずれも2025年には0円です。

## 2025年は、上位10市がすべて年57,000円を超え、15市が年1万円未満

2025年の年額で81市を並べます。上の10本の濃い青が上位10市です。下の11行は0円なので、棒がなく市の名前だけが並びます。

```chart
{
  "height": 1830,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "value", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市"},
          "sort": null
        },
        "color": {
          "datum": "上位10市",
          "type": "nominal",
          "scale": {
            "domain": ["上位10市", "負担のある60市", "0円の11市"],
            "range": ["#3b82f6", "#93c5fd", "#22c55e"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "value", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市"},
          "sort": null
        },
        "color": {
          "datum": "負担のある60市",
          "type": "nominal",
          "scale": {
            "domain": ["上位10市", "負担のある60市", "0円の11市"],
            "range": ["#3b82f6", "#93c5fd", "#22c55e"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_free"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "value", "type": "quantitative"},
          {"field": "city", "type": "nominal"}
        ],
        "x": {
          "field": "value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市"},
          "sort": null
        },
        "color": {
          "datum": "0円の11市",
          "type": "nominal",
          "scale": {
            "domain": ["上位10市", "負担のある60市", "0円の11市"],
            "range": ["#3b82f6", "#93c5fd", "#22c55e"]
          },
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは長岡市の年68,405円で、新潟市の年62,252円が続きます。10位の徳島市でも年57,578円で、上位10市はいずれも年57,000円を超えます。2019年に最も高かった長野市の57,817円と同じ水準です。

0円の市の上には、額の小さい市が6市あります。枚方市の年3,800円、八王子市の年4,209円、水戸市の年5,913円、八戸市の年5,915円、前橋市の年11,760円、福岡市の年24,150円です。年の途中で負担が変わった市は、このように中間の値になります。

2025年の81市は、0円が11市、年1万円未満が4市、年4万円台と5万円台が60市で、残る6市は年1万円台から3万円台と年6万円台です。年4万円台から5万円台の60市から離れて、0円と1万円未満の市が15市あります。2019年までは最も安い市でも年38,573円でした。

## 0円の市は、2024年と2025年のどちらも中学校のほうが多い

同じテーブルには学校給食(中学校)（`02183`）も入っています。対象の市は2021年以降が81市で、それより前は77市から80市です。小学校と中学校で、0円の市の数を並べます。

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "grade"},
      "transform": [
        {"fold": ["elem_free", "jhs_free"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"elem_free\": \"小学校\", \"jhs_free\": \"中学校\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"elem_free\",\"jhs_free\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "0円になった市の数", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["小学校", "中学校"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["小学校", "中学校"]},
        "tooltip": [
          {"field": "year", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

0円の市は2021年から2023年まで1市で、2024年に小学校4市・中学校6市、2025年に小学校11市・中学校13市に増えました。2024年と2025年はどちらも中学校のほうが多く、2025年には、小学校は負担があり中学校だけ0円の市が3つあります。大分市（小学校は年57,995円）、伊丹市（年46,464円）、水戸市（年5,913円）です。

給食費は中学校のほうが高く、2025年の中央値は小学校が年48,071円、中学校が年55,470円です。負担の大きい中学校から先に無償にした市があります。大分市の小学校の年57,995円は81市で9番目に高い額ですが、中学校は0円です。

## 0円の市の財政力指数は0.55から1.48まで分かれ、負担のある市の範囲とほぼ重なる

給食費をなくすかどうかには、市の財源も関係します。総務省の[地方財政状況調査](https://www.e-stat.go.jp/stat-search/files?toukei=00200251)には市区町村ごとの財政力指数が入っているので、2024年度決算の値と2025年の給食費を並べます。財政力指数は基準財政収入額を基準財政需要額で割った値の3か年平均で、1を超えると地方交付税を受けない水準です。小売物価統計の「特別区部」は東京23区をまとめた1つの地域で、区ごとの財政力指数と対応しないので、この図はそれを除いた80市で、0円の市は10市です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "fci_paid"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "city", "type": "nominal"},
          {"field": "fci", "type": "quantitative"},
          {"field": "fee", "type": "quantitative"}
        ],
        "x": {
          "field": "fci",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "財政力指数（2024年度決算）", "grid": true}
        },
        "y": {
          "field": "fee",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "color": {
          "datum": "負担のある70市",
          "type": "nominal",
          "scale": {"domain": ["負担のある70市", "0円の10市"], "range": ["#3b82f6", "#22c55e"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "fci_free"},
      "mark": {"type": "point", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "city", "type": "nominal"},
          {"field": "fci", "type": "quantitative"},
          {"field": "fee", "type": "quantitative"}
        ],
        "x": {
          "field": "fci",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "財政力指数（2024年度決算）", "grid": true}
        },
        "y": {
          "field": "fee",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "給食費の年額（円）", "grid": true}
        },
        "color": {
          "datum": "0円の10市",
          "type": "nominal",
          "scale": {"domain": ["負担のある70市", "0円の10市"], "range": ["#3b82f6", "#22c55e"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

0円の10市の財政力指数は、青森市の0.55から浦安市の1.48まで分かれています。中央値は0.875で、負担のある70市の0.76より高い値です。負担のある70市のうち65市は、最も低い青森市の0.55を上回っています。負担のある市の指数は0.48から1.08まで分布していて、0円の市の範囲とほぼ重なります。給食費をなくすかどうかは、財政力の高さだけでは決まっていないと考えられます。

## 業務での使い方

- 自分の市の年額を81市の中で比較し、水準と順位を1つの表で確認できます。議会や保護者への説明で、近隣の市と比較した位置を示す根拠になります
- 0円にした市が直前に徴収していた1人あたりの年額が分かるので、自分の市の児童数を掛けると、負担をなくすのに必要な予算の規模を見積もれます
- 小学校と中学校のどちらを先に無償にした市が多いかが分かるので、段階的に進める場合の順序を、実際に進めた市の例で確認できます

## データの出典

本記事は総務省統計局の[小売物価統計調査（動向編）](https://www.stat.go.jp/data/kouri/index.html)の調査品目の年平均価格と、総務省の[地方財政状況調査](https://www.e-stat.go.jp/stat-search/files?toukei=00200251)を2026年9月21日時点で集計しています。給食費は2015年から2025年の年額、財政力指数は2024年度決算の値です。対象は都道府県庁所在市と人口15万以上の市で、2015年以降は81市です。

Queria は、小売物価統計と地方財政状況調査の市のコードを標準地域コードに統一し、品目コードと品目名、単位や収録年の注意点の説明を付けて公開しています。本記事で使った[品目別価格テーブル](/datasets/queria/e_stat/retail_price/item_price)と[財政力テーブル](/datasets/queria/e_stat/local_finance/fiscal_capacity)から、自分の市の11年分を近隣の市と並べたり、給食以外の品目で同じ比較をしたりできます。

```sql id=spread
SELECT year, ROUND(MAX(value)) AS max_fee, ARG_MAX(regexp_replace(area_name, '【.*$', ''), value) AS max_city, ROUND(MEDIAN(value)) AS med_fee, ROUND(MIN(value)) AS min_fee, ARG_MIN(regexp_replace(area_name, '【.*$', ''), value) AS min_city, COUNT(*) AS n_city FROM e_stat.retail_price.item_price WHERE cat02 = '02182' AND year BETWEEN 2015 AND 2025 AND value IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=rank_top
WITH ranked AS (SELECT regexp_replace(area_name, '【.*$', '') AS city, value, ROW_NUMBER() OVER (ORDER BY value DESC, area_name) AS rn FROM e_stat.retail_price.item_price WHERE cat02 = '02182' AND year = 2025 AND value IS NOT NULL) SELECT city, value FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH ranked AS (SELECT regexp_replace(area_name, '【.*$', '') AS city, value, ROW_NUMBER() OVER (ORDER BY value DESC, area_name) AS rn FROM e_stat.retail_price.item_price WHERE cat02 = '02182' AND year = 2025 AND value IS NOT NULL) SELECT city, value FROM ranked WHERE rn > 10 AND rn <= 70 ORDER BY rn
```

```sql id=rank_free
WITH ranked AS (SELECT regexp_replace(area_name, '【.*$', '') AS city, value, ROW_NUMBER() OVER (ORDER BY value DESC, area_name) AS rn FROM e_stat.retail_price.item_price WHERE cat02 = '02182' AND year = 2025 AND value IS NOT NULL) SELECT city, value FROM ranked WHERE rn > 70 ORDER BY rn
```

```sql id=grade
SELECT year, COUNT(*) FILTER (WHERE cat02 = '02182' AND value = 0) AS elem_free, COUNT(*) FILTER (WHERE cat02 = '02183' AND value = 0) AS jhs_free, COUNT(*) FILTER (WHERE cat02 = '02182') AS elem_n, COUNT(*) FILTER (WHERE cat02 = '02183') AS jhs_n, ROUND(MEDIAN(value) FILTER (WHERE cat02 = '02182')) AS elem_med, ROUND(MEDIAN(value) FILTER (WHERE cat02 = '02183')) AS jhs_med FROM e_stat.retail_price.item_price WHERE cat02 IN ('02182', '02183') AND year BETWEEN 2015 AND 2025 AND value IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=jhs_only
SELECT regexp_replace(j.area_name, '【.*$', '') AS city, j.value AS jhs_fee, e.value AS elem_fee FROM e_stat.retail_price.item_price j JOIN e_stat.retail_price.item_price e ON e.area = j.area AND e.year = j.year AND e.cat02 = '02182' WHERE j.cat02 = '02183' AND j.year = 2025 AND j.value = 0 AND e.value > 0 ORDER BY e.value DESC
```

```sql id=fci_free
WITH j AS (SELECT regexp_replace(p.area_name, '【.*$', '') AS city, p.value AS fee, f.fiscal_capacity_index AS fci FROM e_stat.retail_price.item_price p JOIN e_stat.local_finance.fiscal_capacity f ON f.area_code = p.area AND f.fiscal_year = 2024 WHERE p.cat02 = '02182' AND p.year = 2025 AND p.value IS NOT NULL) SELECT city, fee, fci FROM j WHERE fee = 0 ORDER BY fci
```

```sql id=fci_paid
WITH j AS (SELECT regexp_replace(p.area_name, '【.*$', '') AS city, p.value AS fee, f.fiscal_capacity_index AS fci FROM e_stat.retail_price.item_price p JOIN e_stat.local_finance.fiscal_capacity f ON f.area_code = p.area AND f.fiscal_year = 2024 WHERE p.cat02 = '02182' AND p.year = 2025 AND p.value IS NOT NULL) SELECT city, fee, fci FROM j WHERE fee > 0 ORDER BY fci
```
