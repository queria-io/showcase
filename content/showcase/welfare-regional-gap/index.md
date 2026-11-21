---
title: 生活保護の保護率、半世紀で九州7県はすべて下がり大都市圏の7都府県はすべて上がった
description: 都道府県別の生活保護の保護率を1975年度と2023年度で比較すると、九州の7県はすべて下がり、東京・大阪など大都市圏の7都府県はすべて上がった。3.1倍あった両者の差は1.05倍まで縮んでいる
publishedAt: 2026-03-01
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 生活保護
  - 社会保障
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 被保護者調査
    url: https://www.mhlw.go.jp/toukei/list/74-16b.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 都道府県別の生活保護の保護率（J1105÷A1101）を1975〜2023年度で出して、1995年度から2023年度までの上がり幅が大きい順に並べて。大都市圏の7都府県と九州の7県はどこに入る？
socialAnnounce: |-
  1975年度、生活保護の保護率は九州の7県が2.69%、東京・大阪など大都市圏の7都府県が0.87%でした。

  2023年度は1.91%と1.81%。
  九州の7県はすべて下がり、7都府県はすべて上がりました。
---

生活保護を受けている人の割合がいちばん高いのは大阪府で、2023年度は住民の3.04%です。ところが1975年度の大阪府は1.22%で、47都道府県の22位でした。当時の1位は3.79%の福岡県で、九州の県が上位に並んでいました。

1975年度と2023年度を比較すると、東京都・神奈川県・千葉県・埼玉県・愛知県・大阪府・兵庫県の大都市圏の7都府県はすべて保護率が上がり、九州の7県はすべて下がりました。1975年度に3.1倍あった両者の差は、2023年度には1.05倍になっています。

## 九州の7県と大都市圏の7都府県の差は、3.1倍から1.05倍に縮まった

保護率は、生活保護を受けている人（被保護実人員）を総人口で割った割合です。被保護実人員は年度の1か月平均で、保護を一時停止されている人を含みます。下の図の区分ごとの値は、区分に入る都道府県の人数の合計を人口の合計で割ったものなので、人口の多い東京都・神奈川県・大阪府の増減の影響が大きくなります。

```chart
{
  "layer": [
    {
      "data": {"name": "group_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kyushu\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "kyushu", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "kyushu",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "保護率（%）", "grid": true}
        },
        "color": {
          "datum": "九州の7県",
          "type": "nominal",
          "scale": {
            "domain": ["九州の7県", "大都市圏の7都府県", "その他の33道府県", "全国"],
            "range": ["#3b82f6", "#f97316", "#94a3b8", "#475569"]
          },
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
        "invalid": "break-paths-show-domains"
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
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "metro",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "保護率（%）", "grid": true}
        },
        "color": {
          "datum": "大都市圏の7都府県",
          "type": "nominal",
          "scale": {
            "domain": ["九州の7県", "大都市圏の7都府県", "その他の33道府県", "全国"],
            "range": ["#3b82f6", "#f97316", "#94a3b8", "#475569"]
          },
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"other\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "other", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "other",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "保護率（%）", "grid": true}
        },
        "color": {
          "datum": "その他の33道府県",
          "type": "nominal",
          "scale": {
            "domain": ["九州の7県", "大都市圏の7都府県", "その他の33道府県", "全国"],
            "range": ["#3b82f6", "#f97316", "#94a3b8", "#475569"]
          },
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"national\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#475569",
        "strokeWidth": 2,
        "strokeDash": [2, 3],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "national", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "national",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "保護率（%）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {
            "domain": ["九州の7県", "大都市圏の7都府県", "その他の33道府県", "全国"],
            "range": ["#3b82f6", "#f97316", "#94a3b8", "#475569"]
          },
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

1975年度の保護率は九州の7県が2.69%、大都市圏の7都府県が0.87%で、3.1倍の差がありました。九州の7県は1975年度から1990年代後半にかけて下がりました。大都市圏の7都府県は1983〜84年度の0.99%まで上がったあと、1992年度の0.61%まで下がりました。それぞれの底からはどちらも2014年度ごろまで上がり、以降は緩やかに下がっています。九州の7県は2023年度の1.91%でも1975年度の水準に届かず、大都市圏の7都府県は1.81%と1975年度の2倍を超えました。差は約0.1ポイントです。九州の7県が下がったのは1975年度と比較した場合で、最も低かった1990年代後半と比較すると上がっています。

```sql
SELECT * FROM group_gap
```

## 14都府県を1つずつ見ても、大都市圏の7都府県はすべて上がり、九州の7県はすべて下がった

1975年度から2023年度の保護率の倍率を47都道府県で並べると、上から8つのうち7つが大都市圏の7都府県です。残る1つは静岡県で、1975年度は0.42%で47位でした。

```chart
{
  "layer": [
    {
      "data": {"name": "change_by_pref"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "保護率の倍率（2023年度÷1975年度）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#475569", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 1, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

橙が大都市圏の7都府県、青が九州の7県です。7都府県の倍率は兵庫県の1.82倍から大阪府の2.5倍までで、1倍を下回ったところはありません。九州の7県はすべて1倍を下回りますが、最も高い大分県は0.99倍（1.70%→1.68%）でほぼ横ばいです。佐賀県は1.70%から0.92%へ下がって0.54倍と、47都道府県で最も小さい倍率です。それ以外の33道府県は、上がった20と下がった13に分かれます。

```sql
SELECT * FROM group_summary
```

順位で見ると、千葉県は42位から18位へ、埼玉県は43位から24位へ、東京都は26位から9位へ上がりました。福岡県は1位から5位になっています。保護率が1位の都道府県は、1996年度まで22年続けて福岡県でした。その後は北海道に移り、2004年度に初めて大阪府が1位になって、2006年度からは大阪府が続いています。

```sql
SELECT * FROM top1_runs
```

保護率は保護を受けている人の割合で、生活に困っている人の割合そのものではありません。要件を満たしながら申請していない人は数に入らないので、県の間の差や順位の入れ替わりには、困窮の広がりとあわせて申請や運用の違いも含まれます。都道府県の値は、県内の指定都市・中核市で保護を受けている人を含みます。

```sql
SELECT * FROM pref_table
```

## まとめ

- 1975年度の保護率は九州の7県が2.69%、大都市圏の7都府県が0.87%で3.1倍の差があったが、2023年度は1.91%と1.81%で1.05倍になった
- 1975年度から2023年度に、東京都・神奈川県・千葉県・埼玉県・愛知県・大阪府・兵庫県はすべて1.82倍以上に上がり、九州の7県はすべて下がった
- 保護率1位は1996年度まで22年続けて福岡県で、2006年度からは大阪府が続いている。大阪府は1975年度には22位だった

自分の県の保護率がこの半世紀で上がったか下がったかは、上の表の倍率と順位で確認できます。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年9月30日時点で集計しています。被保護実人員の元データは厚生労働省の[被保護者調査](https://www.mhlw.go.jp/toukei/list/74-16b.html)で、定義は[項目定義 J 福祉・社会保障](https://www.e-stat.go.jp/koumoku/koumoku_teigi/J)によります。総人口は同じ体系の10月1日現在の値です。

Queriaは、e-Statの社会・人口統計体系を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の福祉統計テーブル](/datasets/queria/e_stat/ssds/j_pref_welfare)から、自分の県の保護率を1975年度から年度ごとに集計できます。

```sql id=group_trend
WITH base AS ( SELECT w.year, CASE WHEN w.area_name = '全国' THEN 'national' WHEN w.area_name IN ('東京都', '神奈川県', '千葉県', '埼玉県', '愛知県', '大阪府', '兵庫県') THEN 'metro' WHEN w.area_name IN ('福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県') THEN 'kyushu' ELSE 'other' END AS grp, CAST(w.value AS DOUBLE) AS persons, CAST(p.value AS DOUBLE) AS pop FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1105' AND w.year BETWEEN 1975 AND 2023 ) SELECT year, ROUND(SUM(persons) FILTER (WHERE grp = 'kyushu') / SUM(pop) FILTER (WHERE grp = 'kyushu') * 100, 2) AS kyushu, ROUND(SUM(persons) FILTER (WHERE grp = 'metro') / SUM(pop) FILTER (WHERE grp = 'metro') * 100, 2) AS metro, ROUND(SUM(persons) FILTER (WHERE grp = 'other') / SUM(pop) FILTER (WHERE grp = 'other') * 100, 2) AS other, ROUND(SUM(persons) FILTER (WHERE grp = 'national') / SUM(pop) FILTER (WHERE grp = 'national') * 100, 2) AS national FROM base GROUP BY year ORDER BY year
```

```sql id=group_gap
WITH base AS ( SELECT w.year, CASE WHEN w.area_name IN ('東京都', '神奈川県', '千葉県', '埼玉県', '愛知県', '大阪府', '兵庫県') THEN 'metro' WHEN w.area_name IN ('福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県') THEN 'kyushu' END AS grp, CAST(w.value AS DOUBLE) AS persons, CAST(p.value AS DOUBLE) AS pop FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1105' AND w.year IN (1975, 2023) ), g AS ( SELECT year, SUM(persons) FILTER (WHERE grp = 'kyushu') / SUM(pop) FILTER (WHERE grp = 'kyushu') * 100 AS k, SUM(persons) FILTER (WHERE grp = 'metro') / SUM(pop) FILTER (WHERE grp = 'metro') * 100 AS m FROM base GROUP BY year ) SELECT year AS 年度, ROUND(k, 2) AS "九州の7県（%）", ROUND(m, 2) AS "大都市圏の7都府県（%）", ROUND(k - m, 2) AS "差（ポイント）", ROUND(k / m, 2) AS "九州÷大都市圏" FROM g ORDER BY year
```

```sql id=top1_runs
WITH rate AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1105' AND w.area_name != '全国' AND w.year BETWEEN 1975 AND 2023 ), top AS ( SELECT year, area_name FROM rate QUALIFY RANK() OVER (PARTITION BY year ORDER BY rate DESC) = 1 ) SELECT area_name AS "保護率1位の都道府県", MIN(year) AS 最初の年度, MAX(year) AS 最後の年度, COUNT(*) AS 年数 FROM top GROUP BY area_name ORDER BY MIN(year)
```

```sql id=change_by_pref
WITH rate AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1105' AND w.area_name != '全国' AND w.year IN (1975, 2023) ), ranked AS ( SELECT *, RANK() OVER (PARTITION BY year ORDER BY rate DESC) AS rnk FROM rate ), wide AS ( SELECT a.area_name, a.rate AS r75, a.rnk AS k75, b.rate AS r23, b.rnk AS k23 FROM ranked a JOIN ranked b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023 ), grouped AS ( SELECT *, CASE WHEN area_name IN ('東京都', '神奈川県', '千葉県', '埼玉県', '愛知県', '大阪府', '兵庫県') THEN '大都市圏の7都府県' WHEN area_name IN ('福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県') THEN '九州の7県' ELSE 'その他の33道府県' END AS grp FROM wide ) SELECT area_name, ROUND(r23 / r75, 2) AS ratio, CASE WHEN grp = '大都市圏の7都府県' THEN '#f97316' WHEN grp = '九州の7県' THEN '#3b82f6' ELSE '#cbd5e1' END AS color FROM grouped ORDER BY r23 / r75 DESC, area_name
```

```sql id=group_summary
WITH rate AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1105' AND w.area_name != '全国' AND w.year IN (1975, 2023) ), ranked AS ( SELECT *, RANK() OVER (PARTITION BY year ORDER BY rate DESC) AS rnk FROM rate ), wide AS ( SELECT a.area_name, a.rate AS r75, a.rnk AS k75, b.rate AS r23, b.rnk AS k23 FROM ranked a JOIN ranked b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023 ), grouped AS ( SELECT *, CASE WHEN area_name IN ('東京都', '神奈川県', '千葉県', '埼玉県', '愛知県', '大阪府', '兵庫県') THEN '大都市圏の7都府県' WHEN area_name IN ('福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県') THEN '九州の7県' ELSE 'その他の33道府県' END AS grp FROM wide ) SELECT grp AS 区分, COUNT(*) AS 都道府県数, SUM(CASE WHEN r23 > r75 THEN 1 ELSE 0 END) AS 上がった, SUM(CASE WHEN r23 < r75 THEN 1 ELSE 0 END) AS 下がった, ROUND(MIN(r23 / r75), 2) AS 倍率の最小, ROUND(MAX(r23 / r75), 2) AS 倍率の最大 FROM grouped GROUP BY grp ORDER BY MIN(r23 / r75) DESC
```

```sql id=pref_table
WITH rate AS ( SELECT w.year, w.area_name, CAST(w.value AS DOUBLE) / CAST(p.value AS DOUBLE) * 100 AS rate FROM e_stat.ssds.j_pref_welfare w JOIN e_stat.ssds.a_pref_population p ON p.area_name = w.area_name AND p.year = w.year AND p.cat01 = 'A1101' WHERE w.cat01 = 'J1105' AND w.area_name != '全国' AND w.year IN (1975, 2023) ), ranked AS ( SELECT *, RANK() OVER (PARTITION BY year ORDER BY rate DESC) AS rnk FROM rate ), wide AS ( SELECT a.area_name, a.rate AS r75, a.rnk AS k75, b.rate AS r23, b.rnk AS k23 FROM ranked a JOIN ranked b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023 ), grouped AS ( SELECT *, CASE WHEN area_name IN ('東京都', '神奈川県', '千葉県', '埼玉県', '愛知県', '大阪府', '兵庫県') THEN '大都市圏の7都府県' WHEN area_name IN ('福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県') THEN '九州の7県' ELSE 'その他の33道府県' END AS grp FROM wide ) SELECT area_name AS 都道府県, ROUND(r75, 2) AS "1975年度（%）", k75 AS "1975年度の順位", ROUND(r23, 2) AS "2023年度（%）", k23 AS "2023年度の順位", ROUND(r23 / r75, 2) AS 倍率, grp AS 区分 FROM grouped ORDER BY r23 / r75 DESC, area_name
```
