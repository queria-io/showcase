---
title: 納税者1人あたりの課税対象所得は、港区の1,397万円と南牧村の224万円で6.2倍違う
description: e-Statの市区町村経済データから課税対象所得と納税義務者数を集計しました。2023年度の納税者1人あたり課税対象所得は港区1,397万円から南牧村224万円まで6.2倍の差があり、市区町村の中央値は297.6万円です。総額（市場規模）と組み合わせて出店候補地を評価する方法を示します。
publishedAt: 2026-05-30
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 所得
  - 商圏分析
  - 出店戦略
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 市町村税課税状況等の調
    url: https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09.html
    publisher: 総務省
agentHint: 市区町村別の納税者1人あたり課税対象所得について、2013年度から2023年度への増加率を計算して、購買力の伸びが大きい市区町村と縮んだ市区町村を並べて。
socialAnnounce: |-
  全国1,700超の市区町村の課税対象所得を集計し、1人あたり所得（購買力）と総所得（市場規模）の2軸で分析しました。

  出店候補地の商圏評価やエリアマーケティングに。Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2023年度の納税者1人あたりの課税対象所得は、最も高い東京都港区が1,396.8万円、最も低い群馬県南牧村が223.7万円で、約6.2倍の差がありました。1,741市区町村の中央値は297.6万円です。総額が全国最大の横浜市は1人あたり436.9万円で45位、1人あたりが4位の北海道猿払村は総額が横浜市の700分の1ほどです。出店候補地を評価するときは、1人あたりの所得（購買力）と総額（市場規模）を分けて確認する必要があります。

新規出店やエリアマーケティングで候補地を比較するときは、商圏の人口とあわせて住民の購買力を確認します。同じ人口規模でも、住民の所得水準が違えば、想定できる客単価や取り扱う価格帯が変わります。市区町村ごとの購買力は、住民税の課税状況から得られる課税対象所得で把握できます。この記事では、e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の市区町村別の経済データから、課税対象所得と納税義務者数を使って納税者1人あたりの課税対象所得を計算します。

## データの概要

使うのは e-Stat の「社会・人口統計体系」の市区町村別経済基盤データ（`c_municipal_economy`）です。住民の所得水準に関係する主なカテゴリは次の3つです。

| コード  | 内容                   |
| ------- | ---------------------- |
| C120110 | 課税対象所得           |
| C120120 | 納税義務者数（所得割） |
| C120130 | 納税義務者数（均等割） |

課税対象所得（`C120110`）は市町村民税の課税対象となった所得の総額で、単位は千円です。これを所得割の納税義務者数（`C120120`）で割ると、納税者1人あたりの課税対象所得を計算できます。本記事では万円に換算しています。

分子と分母はどちらも住民税を納めている人だけの集計です。年金収入だけで課税されない世帯や、非課税限度額以下の世帯は含まれないので、1人あたりの値は住民全体の平均所得より高くなります。この差は、高齢化率の高い自治体ほど大きくなります。

集計の対象は、2023年度に課税対象所得と納税義務者数の両方がある1,741団体です。

## 全国の1人あたり課税対象所得は、2023年度も1992年度の381.5万円に戻っていない

全市区町村を合計した1人あたり課税対象所得の推移を、1985年度から並べました。金額は名目値で、物価の変動は調整していません。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"man\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1人あたり課税対象所得（万円）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1985年度の260.5万円から上がり続け、最も高いのは1992年度の381.5万円です。そこから下がり続け、2013年度の320.7万円まで約16%低下しました。2013年度からは10年続けて上がっていますが、2023年度は366.2万円で、1992年度の水準より15.3万円低くなっています。物価の上昇を考えると、実際に買える量の差はこれより大きくなります。

2024年度の1人あたりは393.4万円で、1992年度を初めて上回ります。この増加は分母の減少によるものです。2024年度は所得割の納税義務者数が6,017.7万人から5,715.2万人へ5.0%減り、課税対象所得の総額は220.35兆円から224.82兆円への2.0%増でした。所得割の納税義務者数は、[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/C)で税額控除後に納税義務が残る人と定められています。そのため、2024年度に実施された定額減税で所得割額が0になった人が分母から外れたと考えられます。同じ年の均等割の納税義務者数は6,486.7万人から6,565.0万人へ1.2%増えているので、人口や就業者が減ったわけではありません。2024年度の1人あたりの値は2023年度以前と比較できないので、以下の市区町村の比較には2023年度を使います。

## 1人あたり課税対象所得は、港区の1,396.8万円から南牧村の223.7万円まで6.2倍違う

2023年度の1人あたり課税対象所得の上位15団体と下位10団体です。

```chart
{
  "height": 640,
  "layer": [
    {
      "data": {"name": "rank"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "man", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1人あたり課税対象所得（万円）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "市区町村"}, "sort": null}
      }
    }
  ]
}
```

最も高いのは東京都港区の1,396.8万円で、千代田区（1,121.3万円）、渋谷区（1,073.7万円）と都心の3区が続きます。最も低い群馬県南牧村（223.7万円）と比較すると、約6.2倍の差があります。

4位には北海道猿払村（872.7万円）が入っています。1人あたりの所得は都心の区に近い水準ですが、次の節で示すように総額は小さく、出店先としての条件は東京の都心と異なります。出店の判断では、1人あたりの所得と、商圏としての市場規模を分けて確認する必要があります。

## 総額と1人あたりの2軸で並べると、横浜市・港区・猿払村は別々の位置にある

横軸に課税対象所得の総額（市場全体の所得規模）、縦軸に1人あたり課税対象所得（購買力）をとり、1,741市区町村を散布図にしました。総額は団体によって桁が大きく違うので、横軸は対数軸です。東京23区は区ごとに、政令指定都市は市ごとに数えているので、横軸の順位はこの単位の取り方で変わります。23区を「特別区部」として1つにまとめると28.6兆円で、横浜市の3.4倍です。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter_all"},
      "mark": {"type": "point", "color": "#93c5fd", "opacity": 0.5, "filled": true, "size": 25},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "oku", "type": "quantitative"},
          {"field": "man", "type": "quantitative"}
        ],
        "x": {
          "field": "oku",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "総課税対象所得（億円・対数軸）", "grid": true}
        },
        "y": {
          "field": "man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1人あたり課税対象所得（万円）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scatter_highlight"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "oku", "type": "quantitative"},
          {"field": "man", "type": "quantitative"}
        ],
        "x": {
          "field": "oku",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "総課税対象所得（億円・対数軸）", "grid": true}
        },
        "y": {
          "field": "man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1人あたり課税対象所得（万円）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "scatter_highlight"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "oku",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "総課税対象所得（億円・対数軸）", "grid": true}
        },
        "y": {
          "field": "man",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1人あたり課税対象所得（万円）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

赤い点の4団体は、それぞれ別の位置にあります。横浜市は総額が約8.5兆円（85,051億円）で全国最大です。1人あたりは436.9万円で港区の3分の1以下ですが、1,741団体のうち45位で、市区町村の中央値297.6万円を大きく上回ります。大阪市は総額が4.8兆円規模、1人あたり372.8万円で136位です。全国の合計から計算した366.2万円は人口の多い自治体の影響を強く受けた値で、1団体を1件として並べた中央値297.6万円とは70万円近く違います。大都市は、全国の合計値と比較すると平均程度に見えますが、市区町村の中では上位です。港区は総額が2.1兆円で横浜市の4分の1ですが、1人あたりは1,396.8万円で特に高くなっています。猿払村は1人あたり872.7万円と高く、総額は123.5億円で横浜市の700分の1ほどなので、グラフの左上に1つだけ離れて位置しています。

この2軸を使うと、出店候補地を「市場規模が大きく購買力も高い（右上）」「市場規模は大きいが購買力は都心ほど高くない（右下）」「購買力は高いが市場規模が小さい（左上）」といった象限に分けられます。どの象限を優先するかは、業態や価格帯によって変わります。高価格帯の店舗なら購買力が高い左上と右上のエリアが、来店数を見込むチェーン店なら市場規模が大きい右側のエリアが候補になります。

どちらの軸も住民の居住地で集計した値なので、通勤や観光で訪れる人の消費は含まれません。昼間人口が夜間人口を大きく上回るオフィス街や観光地では、この2軸で評価すると商圏が実際より小さくなります。

## 業務での使い方

このデータは、出店やエリア戦略の最初の絞り込みに使えます。

- 出店候補地の購買力による絞り込み: 1人あたり課税対象所得で候補エリアを絞ります。2023年度の市区町村の中央値は297.6万円、上位1割の境目は363.9万円なので、想定する客単価に応じて基準の値を決めます
- 市場規模と組み合わせた評価: 課税対象所得の総額を市場規模の指標として、購買力との2軸で候補地を象限に分け、業態に合う象限を優先します
- 商圏内の比較: 同じ都市圏や隣接する市区町村の中で1人あたり所得を比較し、近くにあっても購買力が異なるエリアを区別します。比較の基準は全国の合計値ではなく、対象とする団体の中での位置にします

## まとめ

- 全国の1人あたり課税対象所得は、1992年度の381.5万円が最も高く、2013年度の320.7万円まで約16%下がりました。そこから10年続けて上がりましたが、2023年度は366.2万円で、1992年度より15.3万円低い水準です
- 2024年度の1人あたりは393.4万円ですが、所得割の納税義務者数が5.0%減り、総額は2.0%増にとどまっているので、2023年度以前とは比較できません
- 2023年度の市区町村では、港区の1,396.8万円から南牧村の223.7万円まで約6.2倍の差があります
- 市区町村を1団体1件として並べた中央値は297.6万円で、全国の合計から計算した366.2万円とは70万円近く違います。横浜市の436.9万円は市区町村の中で45位です
- 猿払村のように、1人あたりの所得が高くても市場規模が小さいエリアがあるので、2つは分けて確認する必要があります
- 課税対象所得の総額（市場規模）と1人あたり課税対象所得（購買力）の2軸で象限に分けると、業態や価格帯に応じて出店候補地の優先順位を決められます

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の市区町村別経済基盤データ（`c_municipal_economy`）を2026年8月10日時点で集計しています。課税対象所得（`C120110`）と納税義務者数（`C120120`・`C120130`）の元は、総務省の[市町村税課税状況等の調](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran09.html)で、数値はすべて年度の値です。長期の推移は1985年度から2023年度、市区町村の比較は2023年度を対象にしています。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[市区町村別の経済統計テーブル](/datasets/queria/e_stat/ssds/c_municipal_economy)から候補エリアを絞り込んだり、事業所数や人口のデータと結合して商圏を評価したりできます。

```sql id=national_trend
WITH inc AS (SELECT area, ANY_VALUE(area_name) AS area_name, year, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120110' GROUP BY area, year), tax AS (SELECT area, year, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120120' GROUP BY area, year) SELECT i.year, ROUND(SUM(i.v) * 1000 / SUM(t.v) / 10000, 1) AS man FROM inc i JOIN tax t ON i.area = t.area AND i.year = t.year WHERE i.area_name LIKE '% %' AND i.area_name NOT LIKE '% % %' AND i.area_name NOT LIKE '%特別区部%' AND i.v IS NOT NULL AND t.v > 0 AND i.year BETWEEN 1985 AND 2023 GROUP BY i.year ORDER BY i.year
```

```sql id=recent_totals
WITH m AS (SELECT area, ANY_VALUE(area_name) AS area_name, cat01, year, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 IN ('C120110', 'C120120', 'C120130') AND year IN (2023, 2024) GROUP BY area, cat01, year), f AS (SELECT * FROM m WHERE area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '%特別区部%' AND v > 0) SELECT year, ROUND(SUM(CASE WHEN cat01 = 'C120110' THEN v END) / 1000000000, 2) AS income_chou, ROUND(SUM(CASE WHEN cat01 = 'C120120' THEN v END) / 10000, 1) AS payers_income_man, ROUND(SUM(CASE WHEN cat01 = 'C120130' THEN v END) / 10000, 1) AS payers_flat_man, ROUND(SUM(CASE WHEN cat01 = 'C120110' THEN v END) * 1000 / SUM(CASE WHEN cat01 = 'C120120' THEN v END) / 10000, 1) AS man FROM f GROUP BY year ORDER BY year
```

```sql id=rank
WITH inc AS (SELECT area, ANY_VALUE(area_name) AS area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120110' AND year = 2023 GROUP BY area), tax AS (SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120120' AND year = 2023 GROUP BY area), per AS (SELECT i.area_name, ROUND(i.v * 1000 / t.v / 10000, 1) AS man, ROW_NUMBER() OVER (ORDER BY i.v / t.v DESC, i.area_name) AS rn_top, ROW_NUMBER() OVER (ORDER BY i.v / t.v ASC, i.area_name) AS rn_bot FROM inc i JOIN tax t ON i.area = t.area WHERE i.area_name LIKE '% %' AND i.area_name NOT LIKE '% % %' AND i.area_name NOT LIKE '%特別区部%' AND i.v IS NOT NULL AND t.v > 0) SELECT area_name, man FROM per WHERE rn_top <= 15 OR rn_bot <= 10 ORDER BY man DESC
```

```sql id=scatter_all
WITH inc AS (SELECT area, ANY_VALUE(area_name) AS area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120110' AND year = 2023 GROUP BY area), tax AS (SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120120' AND year = 2023 GROUP BY area) SELECT i.area_name, ROUND(i.v / 100000, 1) AS oku, ROUND(i.v * 1000 / t.v / 10000, 1) AS man FROM inc i JOIN tax t ON i.area = t.area WHERE i.area_name LIKE '% %' AND i.area_name NOT LIKE '% % %' AND i.area_name NOT LIKE '%特別区部%' AND i.v IS NOT NULL AND t.v > 0
```

```sql id=distribution
WITH inc AS (SELECT area, ANY_VALUE(area_name) AS area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120110' AND year = 2023 GROUP BY area), tax AS (SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120120' AND year = 2023 GROUP BY area), per AS (SELECT i.area_name, i.v * 1000 / t.v / 10000 AS man FROM inc i JOIN tax t ON i.area = t.area WHERE i.area_name LIKE '% %' AND i.area_name NOT LIKE '% % %' AND i.area_name NOT LIKE '%特別区部%' AND i.v IS NOT NULL AND t.v > 0), r AS (SELECT area_name, man, ROW_NUMBER() OVER (ORDER BY man DESC, area_name) AS rn FROM per) SELECT COUNT(*) AS n, ROUND(MEDIAN(man), 1) AS median_man, ROUND(QUANTILE_CONT(man, 0.90), 1) AS p90_man, MAX(CASE WHEN area_name = '神奈川県 横浜市' THEN rn END) AS rn_yokohama, MAX(CASE WHEN area_name = '大阪府 大阪市' THEN rn END) AS rn_osaka, (SELECT ROUND(MAX(TRY_CAST(value AS DOUBLE)) / 100000, 1) FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120110' AND year = 2023 AND area_name = '東京都 特別区部') AS tokyo23_oku FROM r
```

```sql id=scatter_highlight
WITH inc AS (SELECT area, ANY_VALUE(area_name) AS area_name, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120110' AND year = 2023 GROUP BY area), tax AS (SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS v FROM e_stat.ssds.c_municipal_economy WHERE cat01 = 'C120120' AND year = 2023 GROUP BY area) SELECT SPLIT_PART(i.area_name, ' ', 2) AS label, ROUND(i.v / 100000, 1) AS oku, ROUND(i.v * 1000 / t.v / 10000, 1) AS man FROM inc i JOIN tax t ON i.area = t.area WHERE i.area_name IN ('神奈川県 横浜市', '大阪府 大阪市', '東京都 港区', '北海道 猿払村') ORDER BY oku
```
