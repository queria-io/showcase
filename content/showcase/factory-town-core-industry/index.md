---
title: 工場の街で主力の業種が崩れても伸びても、ほかの業種で働く人は同じだけ減っていました
description: 工業統計の市区町村別データを2008年と2020年で比較しました。主力業種の従業者が半減した街も3割増えた街も、ほかの業種の減り方は中央値で4.8〜6.7%とほぼ同じでした。
ogDescription: 工業統計で761市町村を2008年と2020年で比較しました。主力業種が半減した街も3割増えた街も、ほかの業種で働く人の減り方は同じでした。
publishedAt: 2026-09-15
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 製造業
  - 工業統計
  - 産業構造
datasets:
  - queria/e_stat
sources:
  - title: 工業統計調査
    url: https://www.meti.go.jp/statistics/tyo/kougyo/index.html
    publisher: 経済産業省
  - title: 工業統計調査（政府統計の総合窓口）
    url: https://www.e-stat.go.jp/statistics/00550010
    publisher: 経済産業省
  - title: 日本標準産業分類
    url: https://www.soumu.go.jp/toukei_toukatsu/index/seido/sangyo/index.htm
    publisher: 総務省
agentHint: e_stat.manufacture.municipality_industry から、自分の市区町村の産業中分類別の従業者数と事業所数を2008年と2020年で並べて、どの業種が増えて減ったか出して。同じ主力業種を持つほかの市町村も一覧にして
socialAnnounce: |-
  工業統計で製造業の街761市町村を2008年と2020年で比べました。

  主力業種の従業者が半減した街も3割増えた街も、ほかの業種で働く人の減り方は同じでした。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

工業統計調査で、製造業の業種別の内訳がある市町村を2008年と2020年で比較しました。最も従業者の多い業種（主力業種）の従業者が半減した街のグループも、3割増えた街のグループも、ほかの業種の従業者は中央値で4.8〜6.7%減っており、減り方はほぼ同じでした。主力業種が減った街で、ほかの業種が連鎖して減ることも、減った分の人を雇うことも、このデータには表れていません。

製造業の事業所が集まる街では、働く人の何割かが1つの業種で働いています。その業種の大きな工場が縮小したとき、取引先が連鎖して減るのか、別の業種が人を雇うのかで、産業振興の担当者が取る対策は変わります。[工業統計調査](https://www.meti.go.jp/statistics/tyo/kougyo/index.html)は、市区町村ごとの製造業の従業者数を[日本標準産業分類](https://www.soumu.go.jp/toukei_toukatsu/index/seido/sangyo/index.htm)の中分類24区分に分けて記録しているので、2008年と2020年を並べると、主力業種が減った街と増えた街で、同じ街のほかの業種がどう変わったかを比較できます。

## 業種別の内訳が2008年と2020年の両方にあるのは761市町村

e-Stat「工業統計調査」の市区町村別・産業中分類別統計（`e_stat.manufacture.municipality_industry`）を使います。1つの地域につき製造業計（`industry_code` = `00`）と中分類24区分が縦に並びます。従業者数には秘匿による欠測がなく、内訳を持つ地域では24区分の和が製造業計にちょうど一致します（2008年の766地域・2020年の772地域すべてで一致し、ずれは0件です）。対象は従業者4人以上の事業所で、ある業種の従業者が0人のときは、その業種に従業者4人以上の事業所がないことを表します。

産業中分類の内訳が公表されるのは市区町村と政令指定都市の行政区だけで、都道府県の行は製造業計しか持ちません。2008年と2020年の両方で内訳を持つのは761市町村です。産業別の内訳が公表されていない小規模な市町村と、内訳が行政区ごとにしか無い政令指定都市・東京23区はここに入りません。761市町村の従業者数は2008年が5,880,574人、2020年が5,596,635人で、それぞれ全国の70.3%と72.5%にあたります。

製造業の街の多くは、1つの業種に従業者が偏っています。各市町村で2020年に従業者数が最も多い業種を「主力業種」と呼ぶと、それが街の製造業従業者の3割未満にとどまるのは434市町村です。3割から5割が226市町村、5割から7割が77市町村あり、7割以上を1業種が占める街も24市町村あります。5割以上を1業種が占める街は101で、761市町村の13%、およそ8つに1つです。

以下では、各市町村の従業者数を、2008年時点の主力業種と、それ以外の業種の2つに分けます。産業中分類のコードと名称は2008年から2020年まで同じ産業を指しているので、2つの年の同じ区分どうしを比較できます。

## 主力業種が半減した街も3割増えた街も、ほかの業種の減り方は同じだった

街を主力業種の変化率の順に並べて5等分し、グループごとの中央値を求めました。主力業種とそれ以外がどちらも2008年に500人以上いた647市町村が対象です。

```chart
{
  "height": 320,
  "layer": [
    {
      "data": {"name": "quintile"},
      "transform": [
        {"fold": ["core_med", "rest_med"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"core_med\": \"主力業種\", \"rest_med\": \"それ以外の業種\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"core_med\",\"rest_med\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "qt",
          "type": "ordinal",
          "axis": {
            "title": "主力業種の変化率で5等分したグループ（1が最も減少）",
            "labelAngle": 0,
            "labelOverlap": "greedy"
          },
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の変化率の中央値（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["主力業種", "それ以外の業種"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["主力業種", "それ以外の業種"]},
        "tooltip": [
          {"field": "qt", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

赤い棒（主力業種）は左から51.0%減、21.3%減、8.6%減、7.5%増、29.7%増で、80.7ポイントの幅があります。赤い棒の差はグループの分け方から生じるものなので、比較するのは青い棒（それ以外の業種）です。青い棒は左から4.8%減、6.3%減、5.7%減、5.8%減、6.7%減で、5つのグループの差は1.9ポイントです。ばらつきもほぼ同じで、それ以外の業種の変化率は、どのグループも第1四分位が15.5%減から16.9%減、第3四分位が1.3%増から9.9%増の間にあります。

## 2008年から2020年に従業者が増えたのは24業種のうち6業種だけ

主力業種の変化率の幅が大きいのは、業種ごとの増減が大きく異なるためです。761市町村を合計して、業種別に2008年から2020年の従業者数の変化を集計しました。

```chart
{
  "height": 700,
  "layer": [
    {
      "data": {"name": "ind_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "industry_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の変化率（%、2008年→2020年）", "grid": true}
        },
        "y": {
          "field": "industry_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "datum": "減少",
          "type": "nominal",
          "scale": {"domain": ["減少", "増加"], "range": ["#ef4444", "#22c55e"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "ind_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "industry_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の変化率（%、2008年→2020年）", "grid": true}
        },
        "y": {
          "field": "industry_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "datum": "増加",
          "type": "nominal",
          "scale": {"domain": ["減少", "増加"], "range": ["#ef4444", "#22c55e"]},
          "title": null
        }
      }
    }
  ]
}
```

24区分のうち増えたのは6業種だけです。最も伸びたのは化学工業で254,086人から287,237人へ13.0%増、次いで石油製品・石炭製品製造業が11.0%増、輸送用機械器具製造業が770,447人から810,117人へ5.1%増でした。残る18業種は減っています。最も減ったのは情報通信機械器具製造業で、176,659人から95,500人へ45.9%減りました。繊維工業が28.7%減、なめし革・同製品・毛皮製造業が26.5%減と続きます。

同じ製造業の中に、この12年間で従業者が1割増えた業種と半分近くまで減った業種があります。街の製造業の従業者がどう変わったかは、どの業種を主力にしていたかで大きく異なります。

## 主力業種で街を分けると、主力業種の変化率の幅は61.3ポイント、ほかの業種は15.9ポイント

街を2008年時点の主力業種で分け、街が8つ以上ある16業種について、主力業種とそれ以外の変化率を並べました。

```chart
{
  "height": 640,
  "layer": [
    {
      "data": {"name": "core_rest"},
      "transform": [
        {"fold": ["core_pct", "rest_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"core_pct\": \"主力業種\", \"rest_pct\": \"それ以外の業種\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"core_pct\",\"rest_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "top_ind",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "2008年の主力業種"},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の変化率（%、2008年→2020年）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["主力業種", "それ以外の業種"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["それ以外の業種", "主力業種"]},
        "tooltip": [
          {"field": "top_ind", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

赤い棒の値は大きく異なります。情報通信機械器具製造業を主力とする22市町村では、その業種の従業者が56,443人から28,348人へ49.8%減りました。業務用機械器具製造業の17市町村では35.7%減、電子部品・デバイス・電子回路製造業の80市町村では27.3%減です。反対に化学工業の30市町村では11.5%増、輸送用機械器具製造業の87市町村では5.1%増えています。赤い棒の幅は61.3ポイントです。

青い棒の値の差は小さくなっています。主力業種が半分近くまで減った情報通信機械器具製造業の街で、それ以外の業種は2.6%減にとどまりました。主力が11.5%伸びた化学工業の街でも、それ以外は0.0%です。16業種を通した青い棒の幅は、最も減った印刷・同関連業の街の13.5%減から、最も増えた繊維工業の街の2.4%増まで、15.9ポイントしかありません。

青い棒の並びは赤い棒の並びと対応していません。主力業種が最も減った情報通信機械器具製造業の街ではそれ以外が2.6%減、主力業種がほぼ横ばいだった食料品製造業の街ではそれ以外が8.5%減で、順序はむしろ逆です。主力業種の増減に合わせて、同じ街のほかの業種の従業者が連鎖して減ったり、主力業種で減った分の人を雇って増えたりした傾向は見られません。集計しているのは製造業の事業所だけなので、物流や小売など製造業以外の産業への影響はこの結果には含まれません。

## 主力業種の従業者が大きく減った8市では、ほかの業種は20.0%増えた市も41.9%減った市もある

2008年に主力業種が製造業従業者の5割以上を占めてその業種に2,000人以上が働き、それ以外の業種にも500人以上がいた街のうち、主力業種の従業者が最も多く減った8市を集計しました。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "examples"},
      "transform": [
        {"fold": ["core_pct", "rest_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"core_pct\": \"主力業種\", \"rest_pct\": \"それ以外の業種\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"core_pct\",\"rest_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "nm",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の変化率（%、2008年→2020年）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["主力業種", "それ以外の業種"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["それ以外の業種", "主力業種"]},
        "tooltip": [
          {"field": "nm", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

秋田県にかほ市は、2008年に電子部品・デバイス・電子回路製造業が製造業従業者の63.7%にあたる3,826人を占めていました。2020年にはこれが610人まで減っています。同じ街のそれ以外の業種は2,180人から2,616人へ20.0%増えましたが、増えたのは436人で、主力業種で減った3,216人より少ない人数です。千葉県茂原市も同じ形で、主力の電子部品・デバイス・電子回路製造業が6,264人から1,598人へ減る一方、それ以外は3,429人から3,767人へ9.9%増えました。

東京都武蔵野市と栃木県矢板市では、主力業種の従業者が0人になっています。2008年には、武蔵野市では輸送用機械器具製造業に4,690人、矢板市では情報通信機械器具製造業に2,803人が働いていました。武蔵野市ではそれ以外の業種も573人から333人へ41.9%減り、矢板市では2,541人から2,249人へ11.5%減にとどまっています。

一方、愛知県刈谷市の主力である輸送用機械器具製造業は37,244人から32,564人への12.6%減で、それ以外は15,577人から17,200人へ10.4%増えました。愛知県碧南市はそれ以外が24.3%増です。街ごとに見ると、それ以外の業種は増えた街も減った街もあり、その増減は主力業種が何割減ったかとは対応していません。

## 業務での使い方

- 担当する市町村の主力業種を特定し、その業種が761市町村の合計で増えたか減ったかを確認する。その街の製造業の従業者が増えるか減るかは、主力業種の761市町村の合計での増減でおおむね決まります
- 主力業種が縮小している街で、既存のほかの業種が主力業種で減った人を雇うことを、計画の前提にしない。2008年から2020年までの間、それ以外の業種は中央値で4.8〜6.7%減っており、主力の減少を埋める動きは見られません
- 2020年時点で主力業種が5割を超える101市町村に当てはまる街では、その業種の増減を雇用見通しの前提として扱う。3割未満の街より、雇用の増減の幅が大きくなります。この調査は2020年確報で終わっているので、それ以降の動きは別の統計で確認します
- 既存企業の支援対象を、主力業種の取引先という想定だけで絞り込まない。主力業種が縮小した街でほかの業種が連鎖して減った傾向は、このデータには表れていません

## データの出典

本記事は e-Stat の[工業統計調査](https://www.e-stat.go.jp/statistics/00550010)（経済産業省）に収録された市区町村別・産業中分類別統計（`e_stat.manufacture.municipality_industry`）を2026年9月15日時点で取得して集計しています。従業者数は調査期日時点の人数で、2014年までは調査年の12月31日現在、2017年以降は調査年の6月1日現在です。この調査は2020年確報を最後に行われていません。

Queriaは、年ごとに書式の変わる工業統計調査の統計表を、列名・単位・地域コードを統一し、産業分類の改定や調査期日の変更をテーブルの説明に書いて公開しています。本記事で使った[市区町村別・産業中分類別の工業統計テーブル](/datasets/queria/e_stat/manufacture/municipality_industry)から、担当する市町村の業種構成を確認したり、同じ主力業種を持つほかの市町村を検索したりできます。

```sql id=coverage
WITH b AS (SELECT survey_year, area, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), nat AS (SELECT survey_year, SUM(employees) AS nat_emp FROM e_stat.manufacture.municipality_industry WHERE area_level = 'prefecture' AND industry_level = 1 AND survey_year IN (2008, 2020) GROUP BY survey_year), pn AS (SELECT survey_year, count(DISTINCT area) AS towns, SUM(employees) AS panel_emp FROM b WHERE area IN (SELECT area FROM pan) GROUP BY survey_year) SELECT pn.survey_year AS year, pn.towns, pn.panel_emp, nat.nat_emp, ROUND(pn.panel_emp * 100.0 / nat.nat_emp, 1) AS coverage_pct FROM pn JOIN nat USING (survey_year) ORDER BY year
```

```sql id=ind_down
WITH b AS (SELECT survey_year, area, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), agg AS (SELECT industry_name, SUM(CASE WHEN survey_year = 2008 THEN employees ELSE 0 END) AS e08, SUM(CASE WHEN survey_year = 2020 THEN employees ELSE 0 END) AS e20 FROM b WHERE area IN (SELECT area FROM pan) GROUP BY industry_name), r AS (SELECT industry_name, e08, e20, ROUND(e20 * 100.0 / e08 - 100, 1) AS pct, ROW_NUMBER() OVER (ORDER BY e20 * 1.0 / e08 DESC, industry_name) AS rn FROM agg) SELECT industry_name, e08, e20, pct FROM r WHERE e20 < e08 ORDER BY rn DESC
```

```sql id=ind_up
WITH b AS (SELECT survey_year, area, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), agg AS (SELECT industry_name, SUM(CASE WHEN survey_year = 2008 THEN employees ELSE 0 END) AS e08, SUM(CASE WHEN survey_year = 2020 THEN employees ELSE 0 END) AS e20 FROM b WHERE area IN (SELECT area FROM pan) GROUP BY industry_name), r AS (SELECT industry_name, e08, e20, ROUND(e20 * 100.0 / e08 - 100, 1) AS pct, ROW_NUMBER() OVER (ORDER BY e20 * 1.0 / e08 DESC, industry_name) AS rn FROM agg) SELECT industry_name, e08, e20, pct FROM r WHERE e20 >= e08 ORDER BY rn DESC
```

```sql id=concentration
WITH b AS (SELECT survey_year, area, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), tot AS (SELECT area, SUM(employees) AS tot FROM b WHERE survey_year = 2020 AND area IN (SELECT area FROM pan) GROUP BY area), top AS (SELECT area, industry_name, employees * 100.0 / tot AS sh FROM (SELECT b.area, b.industry_name, b.employees, tot.tot, ROW_NUMBER() OVER (PARTITION BY b.area ORDER BY b.employees DESC, b.industry_name) AS rn FROM b JOIN tot USING (area) WHERE b.survey_year = 2020) WHERE rn = 1) SELECT CASE WHEN sh >= 70 THEN '70%以上' WHEN sh >= 50 THEN '50〜70%' WHEN sh >= 30 THEN '30〜50%' ELSE '30%未満' END AS band, count(*) AS towns FROM top GROUP BY band ORDER BY band
```

```sql id=sum_identity
WITH d AS (SELECT survey_year, area, SUM(CASE WHEN industry_level = 2 THEN employees ELSE 0 END) AS parts, SUM(CASE WHEN industry_level = 1 THEN employees ELSE 0 END) AS total FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' GROUP BY survey_year, area HAVING count(*) FILTER (WHERE industry_level = 2) > 0) SELECT survey_year AS year, count(*) AS areas, SUM(CASE WHEN parts = total THEN 1 ELSE 0 END) AS matching, SUM(CASE WHEN parts <> total THEN 1 ELSE 0 END) AS mismatching FROM d GROUP BY survey_year ORDER BY year
```

```sql id=core_rest
WITH b AS (SELECT survey_year, area, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), top08 AS (SELECT area, industry_name AS top_ind FROM (SELECT area, industry_name, ROW_NUMBER() OVER (PARTITION BY area ORDER BY employees DESC, industry_name) AS rn FROM b WHERE survey_year = 2008 AND area IN (SELECT area FROM pan)) WHERE rn = 1), sp AS (SELECT b.survey_year, b.area, t.top_ind, SUM(CASE WHEN b.industry_name = t.top_ind THEN b.employees ELSE 0 END) AS core, SUM(CASE WHEN b.industry_name = t.top_ind THEN 0 ELSE b.employees END) AS rest FROM b JOIN top08 t USING (area) GROUP BY 1, 2, 3), p AS (SELECT a.top_ind, a.core AS c08, z.core AS c20, a.rest AS r08, z.rest AS r20 FROM (SELECT * FROM sp WHERE survey_year = 2008) a JOIN (SELECT * FROM sp WHERE survey_year = 2020) z USING (area)), g AS (SELECT top_ind, count(*) AS towns, SUM(c08) AS core_08, SUM(c20) AS core_20, SUM(r08) AS rest_08, SUM(r20) AS rest_20, ROUND(SUM(c20) * 100.0 / SUM(c08) - 100, 1) + 0 AS core_pct, ROUND(SUM(r20) * 100.0 / SUM(r08) - 100, 1) + 0 AS rest_pct, ROW_NUMBER() OVER (ORDER BY SUM(c20) * 1.0 / SUM(c08) DESC, top_ind) AS rn FROM p GROUP BY top_ind HAVING count(*) >= 8) SELECT top_ind, towns, core_08, core_20, rest_08, rest_20, core_pct, rest_pct FROM g ORDER BY rn DESC
```

```sql id=quintile
WITH b AS (SELECT survey_year, area, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), top08 AS (SELECT area, industry_name AS top_ind FROM (SELECT area, industry_name, ROW_NUMBER() OVER (PARTITION BY area ORDER BY employees DESC, industry_name) AS rn FROM b WHERE survey_year = 2008 AND area IN (SELECT area FROM pan)) WHERE rn = 1), sp AS (SELECT b.survey_year, b.area, SUM(CASE WHEN b.industry_name = t.top_ind THEN b.employees ELSE 0 END) AS core, SUM(CASE WHEN b.industry_name = t.top_ind THEN 0 ELSE b.employees END) AS rest FROM b JOIN top08 t USING (area) GROUP BY 1, 2), p AS (SELECT a.core AS c08, z.core AS c20, a.rest AS r08, z.rest AS r20 FROM (SELECT * FROM sp WHERE survey_year = 2008) a JOIN (SELECT * FROM sp WHERE survey_year = 2020) z USING (area) WHERE a.core >= 500 AND a.rest >= 500), q AS (SELECT c20 * 100.0 / c08 - 100 AS cpct, r20 * 100.0 / r08 - 100 AS rpct, NTILE(5) OVER (ORDER BY c20 * 1.0 / c08, c08) AS qt FROM p) SELECT qt, count(*) AS towns, ROUND(MEDIAN(cpct), 1) AS core_med, ROUND(MEDIAN(rpct), 1) AS rest_med, ROUND(QUANTILE_CONT(rpct, 0.25), 1) AS rest_p25, ROUND(QUANTILE_CONT(rpct, 0.75), 1) AS rest_p75 FROM q GROUP BY qt ORDER BY qt
```

```sql id=examples
WITH b AS (SELECT survey_year, area, area_name, industry_name, employees FROM e_stat.manufacture.municipality_industry WHERE survey_year IN (2008, 2020) AND area_level = 'municipality' AND industry_level = 2), pan AS (SELECT area FROM b GROUP BY area HAVING count(DISTINCT survey_year) = 2), tot08 AS (SELECT area, SUM(employees) AS tot FROM b WHERE survey_year = 2008 AND area IN (SELECT area FROM pan) GROUP BY area), top08 AS (SELECT area, industry_name AS top_ind, employees * 100.0 / tot AS sh FROM (SELECT b.area, b.industry_name, b.employees, tot08.tot, ROW_NUMBER() OVER (PARTITION BY b.area ORDER BY b.employees DESC, b.industry_name) AS rn FROM b JOIN tot08 USING (area) WHERE b.survey_year = 2008) WHERE rn = 1), sp AS (SELECT b.survey_year, b.area, MAX(b.area_name) AS nm, SUM(CASE WHEN b.industry_name = t.top_ind THEN b.employees ELSE 0 END) AS core, SUM(CASE WHEN b.industry_name = t.top_ind THEN 0 ELSE b.employees END) AS rest FROM b JOIN top08 t USING (area) GROUP BY 1, 2), e AS (SELECT z.nm, t.top_ind, ROUND(t.sh, 1) AS sh08, a.core AS c08, z.core AS c20, a.rest AS r08, z.rest AS r20, ROW_NUMBER() OVER (ORDER BY z.core - a.core, z.nm) AS rn FROM top08 t JOIN (SELECT * FROM sp WHERE survey_year = 2008) a USING (area) JOIN (SELECT * FROM sp WHERE survey_year = 2020) z USING (area) WHERE t.sh >= 50 AND a.core >= 2000 AND a.rest >= 500) SELECT nm, top_ind, sh08, c08, c20, r08, r20, ROUND(c20 * 100.0 / c08 - 100, 1) AS core_pct, ROUND(r20 * 100.0 / r08 - 100, 1) AS rest_pct FROM e WHERE rn <= 8 ORDER BY rn DESC
```
