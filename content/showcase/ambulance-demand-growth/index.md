---
title: 救急出動の人口あたりの差は、大都市圏とほかの道府県で1.55倍から1.12倍に縮んだ
description: 人口1万人あたりの救急出動は、1976年に大都市圏7都府県がほかの40道府県の1.55倍だった。2023年は1.12倍で、1976年に出動が少なかった都道府県ほど大きく伸びている。
publishedAt: 2026-03-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 救急
  - 高齢化
  - 安全
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
  - title: 社会・人口統計体系 項目定義（K 安全）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/K
    publisher: 総務省統計局
  - title: 救急救助の現況
    url: https://www.fdma.go.jp/publication/rescue/
    publisher: 総務省消防庁
agentHint: 救急出動件数（K1210）を人口1万人あたりにして、1976年から2023年の伸びが大きい順に都道府県を並べ、2000年以降だけで見ても同じ県が上位に来るか確かめて
socialAnnounce: |-
  救急車の出動は、1975年の154万件から2023年の764万件へ5倍になりました。

  人口あたりで見ると、1976年は大都市圏7都府県がほかの40道府県の1.55倍。
  2023年は1.12倍です。伸びたのは大都市圏の外のほうでした。
---

2023年、全国の救急車は764万回出動しました。1975年の154万回の5.0倍です。この間に人口は1.11倍にしか増えていないので、人口1万人あたりの出動は137.4件から614.3件へ、4.5倍になっています。

1970年代は、人口あたりの出動が多いのは大都市圏でした。1976年の人口1万人あたりの出動は、東京都・神奈川県・大阪府・愛知県・埼玉県・千葉県・兵庫県の7都府県が、ほかの40道府県の1.55倍でした。2023年は1.12倍です。1976年から2023年に大きく伸びたのは、7都府県の外のほうでした。出動件数には病院から別の病院への転院搬送も入るので、住民が救急車を呼んだ回数とは一致しません。

## 全国の出動件数は1975年の5倍

使ったのは e-Stat「社会・人口統計体系」の都道府県別の安全データ（`k_pref_safety`）にある救急出動件数（`K1210`）と、人口データ（`a_pref_population`）の総人口（`A1101`）・65歳以上人口（`A1303`）です。

| コード | 内容         | 時点              |
| ------ | ------------ | ----------------- |
| K1210  | 救急出動件数 | 1月〜12月の暦年計 |
| A1101  | 総人口       | 10月1日現在       |
| A1303  | 65歳以上人口 | 10月1日現在       |

救急出動件数は消防庁の[救急救助の現況](https://www.fdma.go.jp/publication/rescue/)を出典とする、救急自動車が出動した件数です。`time_name` は「2023年度」のような年度の形ですが、[項目定義（K 安全）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/K)の時点は暦年計なので、この記事では「年」で書きます。急病や交通事故のほか、病院から別の病院へ患者を運ぶ転院搬送も1件として集計されています。

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"calls\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "area",
        "color": "rgba(239,68,68,0.15)",
        "invalid": "break-paths-show-domains",
        "opacity": 1
      },
      "encoding": {
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "calls",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "救急出動件数（件）", "grid": true}
        },
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"calls\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "calls", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "calls",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "救急出動件数（件）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

2019年に664万件に達したあと、2020年は593万件に減り、2022年に723万件、2023年に764万件と、2年続けて過去最多を更新しました。

```sql
SELECT calls_1975 AS 出動件数_1975年, calls_2023 AS 出動件数_2023年, calls_ratio AS 出動件数の倍率, pop_ratio AS 総人口の倍率, per10k_1975 AS 人口1万人あたり_1975年, per10k_2023 AS 人口1万人あたり_2023年, aged_share_1975 AS 高齢化率_1975年, aged_share_2023 AS 高齢化率_2023年 FROM national
```

## 大都市圏とほかの道府県の差は、1.55倍から1.12倍に縮んだ

下の図は、人口1万人あたりの出動件数を、大都市圏の7都府県とほかの40道府県に分けて年ごとに出したものです。7都府県は2020年の総人口の上位7都府県で（8位は北海道）、出動件数の合計を人口の合計で割っています。ほかの40道府県には京都府や福岡県、宮城県のように大都市を抱える府県も入ります。1975年は山梨県の出動件数が収録されていないので、都道府県どうしの比較は47都道府県がそろう1976年から始めます。

```sql
SELECT year AS 年, prefectures AS 出動件数がある都道府県の数, missing AS 欠けている都道府県 FROM pref_coverage
```

```sql
SELECT * FROM metro_def
```

```chart
{
  "layer": [
    {
      "data": {"name": "group_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"metro\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "metro", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "metro",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1万人あたりの救急出動（件）", "grid": true}
        },
        "color": {
          "datum": "大都市圏7都府県",
          "type": "nominal",
          "scale": {"domain": ["大都市圏7都府県", "ほかの40道府県"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "group_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"others\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "others", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "others",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1万人あたりの救急出動（件）", "grid": true}
        },
        "color": {
          "datum": "ほかの40道府県",
          "type": "nominal",
          "scale": {"domain": ["大都市圏7都府県", "ほかの40道府県"], "range": ["#f97316", "#3b82f6"]},
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

1976年から2023年に、7都府県は178.5件から650.8件へ3.65倍、40道府県は115.5件から581.8件へ5.04倍になりました。差は一定のペースで縮んだのではなく、2つの時期に分かれています。1976年の1.55倍から1983年の1.32倍までと、2003年の1.31倍から2011年の1.17倍までです。その間の1983〜2003年は1.31〜1.36倍の間にとどまり、2011年以降は1.11〜1.18倍の間で動いています。

7都府県という区切りを使わない見方でも同じ向きです。47都道府県を人口1万人あたりの出動で並べ、多いほうから10の平均を少ないほうから10の平均で割った値は、1976年の1.90倍から2023年の1.32倍になりました。

```sql
SELECT year AS 年, metro AS 大都市圏7都府県, others AS ほかの40道府県, metro_to_others AS 大都市圏の倍率, top10_to_bottom10 AS 上位10と下位10の平均の比, max_to_min AS 最多と最少の比 FROM group_trend WHERE year IN (1976, 1983, 1993, 2003, 2011, 2019, 2023) ORDER BY year
```

## 1976年に出動が少なかった都道府県ほど、大きく伸びた

次の図は、横軸に1976年の人口1万人あたりの出動件数、縦軸に2023年までの伸び（2023年の値を1976年の値で割った倍率）をとったものです。

```chart
{
  "layer": [
    {
      "data": {"name": "pg_metro"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "per10k_1976", "type": "quantitative"},
          {"field": "growth", "type": "quantitative"}
        ],
        "x": {
          "field": "per10k_1976",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年の人口1万人あたりの救急出動（件）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年→2023年の倍率", "grid": true}
        },
        "color": {
          "datum": "大都市圏7都府県",
          "type": "nominal",
          "scale": {"domain": ["大都市圏7都府県", "ほかの40道府県"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pg_metro"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "per10k_1976",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年の人口1万人あたりの救急出動（件）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年→2023年の倍率", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    },
    {
      "data": {"name": "pg_others"},
      "mark": {"type": "point", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "per10k_1976", "type": "quantitative"},
          {"field": "growth", "type": "quantitative"}
        ],
        "x": {
          "field": "per10k_1976",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年の人口1万人あたりの救急出動（件）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年→2023年の倍率", "grid": true}
        },
        "color": {
          "datum": "ほかの40道府県",
          "type": "nominal",
          "scale": {"domain": ["大都市圏7都府県", "ほかの40道府県"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pg_others"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "per10k_1976",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年の人口1万人あたりの救急出動（件）", "grid": true}
        },
        "y": {
          "field": "growth",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1976年→2023年の倍率", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

伸びがいちばん大きかったのは鹿児島県の7.21倍で、熊本県6.86倍、宮城県6.57倍と続きます。いちばん小さかったのは東京都の3.06倍で、神奈川県3.37倍、山梨県3.50倍と続きます。1976年に1万人あたり89.1件だった鹿児島県は2023年に642.2件で、東京都の656.0件とほぼ並びました。47都道府県で見ると、1976年の値と伸びの相関は −0.84 です。

```sql
SELECT area_name AS 都道府県, '大都市圏' AS 区分, per10k_1976 AS 人口1万人あたり_1976年, per10k_2023 AS 人口1万人あたり_2023年, growth AS 倍率, aged_share_change AS 高齢化率の上昇幅 FROM pg_metro UNION ALL SELECT area_name, 'ほかの道府県', per10k_1976, per10k_2023, growth, aged_share_change FROM pg_others ORDER BY 倍率 DESC
```

## 高齢化が速く進んだ都道府県ほど伸びたわけではない

全国の高齢化率（総人口に占める65歳以上の割合）は1975年の7.9%から2023年の29.1%になりました。都道府県ごとに見ると、1976年から2023年の高齢化率の上昇幅と、出動の伸びの相関は0.25にとどまります。高齢化率の上昇幅が29.9ポイントで最も大きかった秋田県の伸びは5.49倍で、47都道府県のうち大きいほうから13番目です。

2023年の断面でも、高齢化率が高い県ほど人口あたりの出動が多いという関係はありません。下の図の相関は −0.30 で、高齢化率が最も高い秋田県（39.1%）は1万人あたり529.7件、最も多い大阪府（27.7%）は787.5件です。

```chart
{
  "layer": [
    {
      "data": {"name": "elderly_2023"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "aged_share", "type": "quantitative"},
          {"field": "per10k", "type": "quantitative"}
        ],
        "x": {
          "field": "aged_share",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（%、2023年）", "grid": true}
        },
        "y": {
          "field": "per10k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1万人あたりの救急出動（件、2023年）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "elderly_2023"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "aged_share",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（%、2023年）", "grid": true}
        },
        "y": {
          "field": "per10k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口1万人あたりの救急出動（件、2023年）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

```sql
SELECT prefectures AS 都道府県数, corr_growth_start AS 伸びと1976年の値の相関, corr_growth_aging AS 伸びと高齢化率の上昇幅の相関, corr_level_aged_1976 AS 出動と高齢化率の相関_1976年, corr_level_aged_2023 AS 出動と高齢化率の相関_2023年 FROM pref_corr
```

この相関は県どうしを比較した値なので、全国で出動が増えた原因に高齢化が含まれるかどうかは判定できません。分かるのは、県と県の差の縮まり方を、高齢化の速さの違いでは説明できないということです。

## 人口が減った道府県でも、出動は増え続けている

2000年から2023年に総人口が減ったのは39道府県で、その39道府県すべてで救急出動件数が増えました。増え方は山口県の1.56倍から三重県の2.12倍までです。

```sql
SELECT pop_declined AS 人口が減った道府県, pop_declined_calls_rose AS うち出動件数が増えた道府県, min_area AS 倍率が最小の道府県, min_calls_ratio AS 出動件数の倍率_最小, max_area AS 倍率が最大の道府県, max_calls_ratio AS 出動件数の倍率_最大 FROM pop_decline
```

1970年代には「救急車がよく出るのは大都市」と言えましたが、2023年の人口1万人あたりの出動は、7都府県とほかの40道府県で1割ほどしか違いません。人口の減る県で救急体制を見直すときも、人口が減るぶん出動も減るという前提は、この23年間のどの道府県にも当てはまっていません。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年10月6日時点で集計しています。救急出動件数の元データは総務省消防庁の[救急救助の現況](https://www.fdma.go.jp/publication/rescue/)で、定義と時点は[項目定義（K 安全）](https://www.e-stat.go.jp/koumoku/koumoku_teigi/K)にあります。

Queriaは、e-Statをはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の安全統計テーブル](/datasets/queria/e_stat/ssds/k_pref_safety)から、自分の県の救急出動を1975年から並べたり、救急自動車数で割って1台あたりの出動を計算したりできます。

```sql id=trend
SELECT year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 ORDER BY year
```

```sql id=national
-- 1975年と2023年の全国値（プロットはしない）
WITH k AS ( SELECT year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name = '全国' AND year IN (1975, 2023) ), p AS ( SELECT year, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name = '全国' AND year IN (1975, 2023) GROUP BY year ), j AS ( SELECT k.year, k.calls, p.pop, p.pop65 FROM k JOIN p USING (year) ) SELECT a.calls AS calls_1975, b.calls AS calls_2023, ROUND(b.calls / a.calls, 2) AS calls_ratio, a.pop AS pop_1975, b.pop AS pop_2023, ROUND(b.pop / a.pop, 2) AS pop_ratio, ROUND(a.calls / a.pop * 10000, 1) AS per10k_1975, ROUND(b.calls / b.pop * 10000, 1) AS per10k_2023, ROUND(a.pop65 / a.pop * 100, 1) AS aged_share_1975, ROUND(b.pop65 / b.pop * 100, 1) AS aged_share_2023 FROM j a JOIN j b ON a.year = 1975 AND b.year = 2023
```

```sql id=group_trend
-- 大都市圏7都府県（2020年の総人口の上位7都府県）とほかの40道府県の人口1万人あたり出動件数
WITH c AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1976 AND 2023 ), p AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), j AS ( SELECT c.area_name, c.year, c.calls, p.pop, c.calls / p.pop * 10000 AS per10k, c.area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM c JOIN p USING (area_name, year) ), r AS ( SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY per10k DESC, area_name) AS rank_desc, ROW_NUMBER() OVER (PARTITION BY year ORDER BY per10k, area_name) AS rank_asc FROM j ) SELECT year, COUNT(*) AS prefectures, ROUND(SUM(calls) FILTER (WHERE metro) / SUM(pop) FILTER (WHERE metro) * 10000, 1) AS metro, ROUND(SUM(calls) FILTER (WHERE NOT metro) / SUM(pop) FILTER (WHERE NOT metro) * 10000, 1) AS others, ROUND((SUM(calls) FILTER (WHERE metro) / SUM(pop) FILTER (WHERE metro)) / (SUM(calls) FILTER (WHERE NOT metro) / SUM(pop) FILTER (WHERE NOT metro)), 2) AS metro_to_others, ROUND(AVG(per10k) FILTER (WHERE rank_desc <= 10) / AVG(per10k) FILTER (WHERE rank_asc <= 10), 2) AS top10_to_bottom10, ROUND(MAX(per10k) / MIN(per10k), 2) AS max_to_min FROM r GROUP BY year ORDER BY year
```

```sql id=pg_metro
WITH c AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name <> '全国' AND year IN (1976, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name <> '全国' AND year IN (1976, 2023) GROUP BY area_name, year ), j AS ( SELECT c.area_name, c.year, c.calls / p.pop * 10000 AS per10k, p.pop65 / p.pop * 100 AS aged_share FROM c JOIN p USING (area_name, year) ), w AS ( SELECT area_name, MAX(per10k) FILTER (WHERE year = 1976) AS per10k_1976, MAX(per10k) FILTER (WHERE year = 2023) AS per10k_2023, MAX(aged_share) FILTER (WHERE year = 1976) AS aged_1976, MAX(aged_share) FILTER (WHERE year = 2023) AS aged_2023, area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM j GROUP BY area_name ) SELECT area_name, ROUND(per10k_1976, 1) AS per10k_1976, ROUND(per10k_2023, 1) AS per10k_2023, ROUND(per10k_2023 / per10k_1976, 2) AS growth, ROUND(aged_2023 - aged_1976, 1) AS aged_share_change FROM w WHERE metro ORDER BY growth
```

```sql id=pg_others
WITH c AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name <> '全国' AND year IN (1976, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name <> '全国' AND year IN (1976, 2023) GROUP BY area_name, year ), j AS ( SELECT c.area_name, c.year, c.calls / p.pop * 10000 AS per10k, p.pop65 / p.pop * 100 AS aged_share FROM c JOIN p USING (area_name, year) ), w AS ( SELECT area_name, MAX(per10k) FILTER (WHERE year = 1976) AS per10k_1976, MAX(per10k) FILTER (WHERE year = 2023) AS per10k_2023, MAX(aged_share) FILTER (WHERE year = 1976) AS aged_1976, MAX(aged_share) FILTER (WHERE year = 2023) AS aged_2023, area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM j GROUP BY area_name ) SELECT area_name, ROUND(per10k_1976, 1) AS per10k_1976, ROUND(per10k_2023, 1) AS per10k_2023, ROUND(per10k_2023 / per10k_1976, 2) AS growth, ROUND(aged_2023 - aged_1976, 1) AS aged_share_change FROM w WHERE NOT metro ORDER BY growth
```

```sql id=pref_corr
-- 都道府県どうしの相関（プロットはしない）
WITH c AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name <> '全国' AND year IN (1976, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND area_name <> '全国' AND year IN (1976, 2023) GROUP BY area_name, year ), j AS ( SELECT c.area_name, c.year, c.calls / p.pop * 10000 AS per10k, p.pop65 / p.pop * 100 AS aged_share FROM c JOIN p USING (area_name, year) ), w AS ( SELECT area_name, MAX(per10k) FILTER (WHERE year = 1976) AS per10k_1976, MAX(per10k) FILTER (WHERE year = 2023) AS per10k_2023, MAX(aged_share) FILTER (WHERE year = 1976) AS aged_1976, MAX(aged_share) FILTER (WHERE year = 2023) AS aged_2023, area_name IN ('東京都', '神奈川県', '大阪府', '愛知県', '埼玉県', '千葉県', '兵庫県') AS metro FROM j GROUP BY area_name ) SELECT COUNT(*) AS prefectures, ROUND(CORR(per10k_2023 / per10k_1976, per10k_1976), 2) AS corr_growth_start, ROUND(CORR(per10k_2023 / per10k_1976, aged_2023 - aged_1976), 2) AS corr_growth_aging, ROUND(CORR(per10k_1976, aged_1976), 2) AS corr_level_aged_1976, ROUND(CORR(per10k_2023, aged_2023), 2) AS corr_level_aged_2023, COUNT(*) FILTER (WHERE per10k_2023 / per10k_1976 >= 5) AS growth_5x_or_more, COUNT(*) FILTER (WHERE metro AND per10k_2023 / per10k_1976 >= 5) AS metro_5x_or_more FROM w
```

```sql id=elderly_2023
WITH c AS ( SELECT area_name, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, MAX(CASE WHEN cat01 = 'A1101' THEN TRY_CAST(value AS DOUBLE) END) AS pop, MAX(CASE WHEN cat01 = 'A1303' THEN TRY_CAST(value AS DOUBLE) END) AS pop65 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND year = 2023 AND area_name <> '全国' GROUP BY area_name ) SELECT c.area_name, ROUND(c.calls / p.pop * 10000, 1) AS per10k, ROUND(p.pop65 / p.pop * 100, 1) AS aged_share FROM c JOIN p USING (area_name) ORDER BY per10k DESC
```

```sql id=pop_decline
-- 2000年から2023年に総人口が減った道府県の出動件数（プロットはしない）
WITH c AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS calls FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), p AS ( SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND year IN (2000, 2023) ), w AS ( SELECT c.area_name, MAX(c.calls) FILTER (WHERE c.year = 2000) AS calls_2000, MAX(c.calls) FILTER (WHERE c.year = 2023) AS calls_2023, MAX(p.pop) FILTER (WHERE p.year = 2000) AS pop_2000, MAX(p.pop) FILTER (WHERE p.year = 2023) AS pop_2023 FROM c JOIN p USING (area_name, year) GROUP BY c.area_name ) SELECT COUNT(*) FILTER (WHERE pop_2023 < pop_2000) AS pop_declined, COUNT(*) FILTER (WHERE pop_2023 < pop_2000 AND calls_2023 > calls_2000) AS pop_declined_calls_rose, ARG_MIN(area_name, calls_2023 / calls_2000) FILTER (WHERE pop_2023 < pop_2000) AS min_area, ROUND(MIN(calls_2023 / calls_2000) FILTER (WHERE pop_2023 < pop_2000), 2) AS min_calls_ratio, ROUND(MAX(calls_2023 / calls_2000) FILTER (WHERE pop_2023 < pop_2000), 2) AS max_calls_ratio, ARG_MAX(area_name, calls_2023 / calls_2000) FILTER (WHERE pop_2023 < pop_2000) AS max_area FROM w
```

```sql id=metro_def
-- 2020年の総人口の上位8都道府県（プロットはしない）
SELECT RANK() OVER (ORDER BY TRY_CAST(value AS DOUBLE) DESC) AS 人口の順位, area_name AS 都道府県, ROUND(TRY_CAST(value AS DOUBLE) / 10000, 0) AS 総人口_万人 FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 AND area_name <> '全国' ORDER BY TRY_CAST(value AS DOUBLE) DESC LIMIT 8
```

```sql id=pref_coverage
-- 1975年と1976年の都道府県別の収録状況（プロットはしない）
WITH c AS ( SELECT year, area_name FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K1210' AND area_name <> '全国' AND year IN (1975, 1976) AND TRY_CAST(value AS DOUBLE) IS NOT NULL ), a AS ( SELECT DISTINCT area_name FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 AND area_name <> '全国' ), y AS ( SELECT DISTINCT year FROM c ) SELECT y.year, (SELECT COUNT(*) FROM c WHERE c.year = y.year) AS prefectures, COALESCE((SELECT STRING_AGG(a.area_name, '・' ORDER BY a.area_name) FROM a WHERE a.area_name NOT IN (SELECT area_name FROM c WHERE c.year = y.year)), 'なし') AS missing FROM y ORDER BY y.year
```
