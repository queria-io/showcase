---
title: 人口あたりの薬局が最も多かった沖縄県は、2023年度に最も少ない県になった
description: 都道府県別の薬局数を人口10万人あたりに換算し、1975年度と2023年度を比較しました。最多と最少の差は3.76倍から1.64倍に縮み、2つの年度の順位の相関は−0.04です。
publishedAt: 2026-05-29
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療
  - 薬局
  - 人口
  - 出店
datasets:
  - queria/e_stat
sources:
  - title: 衛生行政報告例
    url: https://www.mhlw.go.jp/toukei/list/36-19.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系 項目定義（I 健康・医療）
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/I
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
  - title: 医療施設調査
    url: https://www.mhlw.go.jp/toukei/list/79-1.html
    publisher: 厚生労働省
  - title: 国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 人口推計
    url: https://www.stat.go.jp/data/jinsui/index.html
    publisher: 総務省統計局
agentHint: 人口10万人あたりの薬局数を都道府県別に1975年度から2023年度まで出して、私の県の順位が何年度にどう動いたかと、同じ年度の人口10万人あたりの一般診療所数の順位を並べて。
socialAnnounce: |-
  人口10万人あたりの薬局数は、1975年度は沖縄県が1位、2023年度は沖縄県が47位でした。都道府県の差は3.76倍から1.64倍に縮み、1975年度の順位と2023年度の順位にはほとんど関係がありません。

  薬局の出店計画や、県の医薬品提供体制の検討に。
---

都道府県ごとの人口あたりの薬局数の順位は、1975年度と2023年度で大きく変わっています。2023年度の上位10県のうち、1975年度も上位10に入っていたのは山口県・広島県・香川県の3県だけです。1975年度に人口10万人あたりの薬局が最も多かったのは沖縄県で、2023年度に最も少ないのも沖縄県です。逆に1975年度に最も少なかった青森県は、2023年度には22位まで上がりました。

この記事では、薬局やドラッグストアの出店先を検討する店舗開発の担当者と、県で医薬品の提供体制を担当する職員に向けて、厚生労働省の[衛生行政報告例](https://www.mhlw.go.jp/toukei/list/36-19.html)の薬局数を1975年度から2023年度まで都道府県別に並べます。2023年度に人口あたりの薬局が最も少ない6県（沖縄県・千葉県・埼玉県・奈良県・福井県・神奈川県）は、1975年度にはいずれも26位以内にいて、その後ほかの県に追い越されました。

## 1975年度の順位と2023年度の順位はほとんど関係がない

データは e-Stat の「社会・人口統計体系」の都道府県別の健康・医療データ（`i_pref_health`）から取得しています。使うのは次の項目です。

| コード | 内容                                                | 時点              |
| ------ | --------------------------------------------------- | ----------------- |
| I7102  | 薬局数                                              | 年度末（3月31日） |
| I7103  | 無薬局町村数（薬局が1つも開設されていない町村の数） | 年度末（3月31日） |
| I5102  | 一般診療所数                                        | 10月1日           |
| A1101  | 総人口（`a_pref_population`）                       | 10月1日           |

[項目定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/I)によると、薬局数は医薬品医療機器等法の許可を受けた薬局の数で、病院・診療所の中の調剤所は含みません。店舗販売業の許可だけで営業するドラッグストア（調剤をしない店）は医薬品販売業（`I7101`）に数えられ、薬局数には入りません。同じ年度の総人口で割って人口10万人あたりの薬局数を計算し、1975年度と2023年度の値を都道府県ごとに並べたのが下の図です。灰色の点が1975年度、青の点が2023年度で、2023年度の多い順に並べています。

```chart
{
  "height": 1000,
  "encoding": {
    "y": {
      "field": "area_name",
      "type": "nominal",
      "sort": {"field": "per_100k_2023", "order": "descending"},
      "title": null,
      "axis": {"labelOverlap": "greedy"}
    }
  },
  "layer": [
    {
      "data": {"name": "ranks"},
      "mark": {"type": "rule", "color": "#cbd5e1", "strokeWidth": 2},
      "encoding": {
        "x": {"field": "per_100k_1975", "type": "quantitative", "title": "人口10万人あたりの薬局数"},
        "x2": {"field": "per_100k_2023"}
      }
    },
    {
      "data": {"name": "ranks"},
      "mark": {"type": "point", "filled": true, "size": 60},
      "encoding": {
        "x": {"field": "per_100k_1975", "type": "quantitative"},
        "color": {
          "datum": "1975年度",
          "type": "nominal",
          "title": null,
          "scale": {"domain": ["1975年度", "2023年度"], "range": ["#94a3b8", "#2166ac"]}
        },
        "tooltip": [
          {"field": "area_name", "title": "都道府県"},
          {"field": "per_100k_1975", "title": "1975年度", "format": ".1f"},
          {"field": "rank_1975", "title": "1975年度の順位"}
        ]
      }
    },
    {
      "data": {"name": "ranks"},
      "mark": {"type": "point", "filled": true, "size": 60},
      "encoding": {
        "x": {"field": "per_100k_2023", "type": "quantitative"},
        "color": {
          "datum": "2023年度",
          "type": "nominal",
          "title": null,
          "scale": {"domain": ["1975年度", "2023年度"], "range": ["#94a3b8", "#2166ac"]}
        },
        "tooltip": [
          {"field": "area_name", "title": "都道府県"},
          {"field": "per_100k_2023", "title": "2023年度", "format": ".1f"},
          {"field": "rank_2023", "title": "2023年度の順位"}
        ]
      }
    }
  ]
}
```

1975年度の上位には、沖縄県（40.5）・和歌山県（32.6）・愛知県（30.8）・東京都（30.7）・大阪府（30.6）が並んでいました。2023年度の上位は佐賀県（64.5）・高知県（60.4）・山形県（60.0）・山口県（59.8）・山梨県（59.7）です。1975年度に42位だった山形県は3位に、45位だった宮崎県は10位に上がりました。1975年度に3位だった愛知県は36位に、4位だった東京都は33位に下がっています。

2つの年度の順位の相関係数は−0.04で、1975年度の順位から2023年度の順位はほとんど予測できません。47都道府県の真ん中は24位です。1975年度の上位10都府県のうち3つは2023年度に真ん中より下（25位以下）へ下がり、下位10県のうち8つは真ん中より上（23位以内）に上がっています。人口10万人あたりの薬局数が1975年度より減ったのは、47都道府県のうち沖縄県だけです。

```sql
SELECT * FROM summary
```

## 最多の県と最少の県の差は、3.76倍から1.64倍に縮んだ

同じ48年間に、県の差も縮みました。下の図は、年度ごとの最多の県と最少の県の比（左の軸）と、47都道府県のばらつきの大きさを平均で割った変動係数（右の軸）です。2010年度は東日本大震災の影響で宮城県の値がなく、福島県も一部の市町村を含まないため、この年度だけ46都道府県で計算しています。

```chart
{
  "layer": [
    {
      "data": {"name": "spread"},
      "mark": {"type": "line", "point": true, "color": "#2166ac"},
      "encoding": {
        "x": {"field": "year", "type": "quantitative", "title": "年度", "axis": {"format": "d"}},
        "y": {"field": "max_min_ratio", "type": "quantitative", "title": "最多÷最少（倍）", "axis": {"orient": "left"}, "scale": {"zero": false}},
        "tooltip": [
          {"field": "year", "title": "年度"},
          {"field": "max_min_ratio", "title": "最多÷最少", "format": ".2f"},
          {"field": "top_pref", "title": "最多"},
          {"field": "bottom_pref", "title": "最少"}
        ]
      }
    },
    {
      "data": {"name": "spread"},
      "mark": {"type": "line", "point": true, "color": "#64748b", "strokeDash": [4, 3]},
      "encoding": {
        "x": {"field": "year", "type": "quantitative", "axis": {"format": "d"}},
        "y": {"field": "cv", "type": "quantitative", "title": "変動係数（破線）", "axis": {"orient": "right"}, "scale": {"zero": false}},
        "tooltip": [
          {"field": "year", "title": "年度"},
          {"field": "cv", "title": "変動係数", "format": ".3f"}
        ]
      }
    }
  ],
  "resolve": {"scale": {"y": "independent"}}
}
```

1975年度は最多の沖縄県（40.5）が最少の青森県（10.8）の3.76倍でした。2023年度は最多の佐賀県（64.5）が最少の沖縄県（39.4）の1.64倍です。最多÷最少は1990年代後半や2000年代後半に一時上がっていますが、変動係数は0.271から0.100へほぼ毎年下がっていて、47都道府県全体の差は48年間縮み続けました。この間に47都道府県の薬局数の合計は26,920から62,828へ2.33倍になり、人口10万人あたりでは24.0から50.5になっています。

## 沖縄県の薬局数は1986年度からほとんど増えていない

沖縄県は1988年度まで14年続けて1位で、そこから順位を下げ、2019年度から2023年度までは5年続けて47位です。下の図は、沖縄県と47都道府県の合計の人口10万人あたりの薬局数です（2010年度の合計と沖縄県の順位は、宮城県を除く46都道府県の値です）。

```chart
{
  "data": {"name": "okinawa"},
  "mark": {"type": "line", "point": true},
  "encoding": {
    "x": {"field": "year", "type": "quantitative", "title": "年度", "axis": {"format": "d"}},
    "y": {"field": "per_100k", "type": "quantitative", "title": "人口10万人あたりの薬局数"},
    "color": {"field": "series", "type": "nominal", "title": null},
    "tooltip": [
      {"field": "series"},
      {"field": "year", "title": "年度"},
      {"field": "pharmacies", "title": "薬局数", "format": ","},
      {"field": "per_100k", "title": "人口10万人あたり", "format": ".1f"},
      {"field": "rank", "title": "順位"}
    ]
  }
}
```

沖縄県の薬局数は1975年度の422から1986年度の548まで増えたあと、2023年度の578まで37年で30しか増えていません。1975年度から2023年度までで見ると1.37倍で、47都道府県の合計の2.33倍を大きく下回ります。人口10万人あたりの値は40.5から39.4へわずかに下がり、全国がその間に2倍以上になったため、1位から47位に移りました。

沖縄県には薬局のない町村も多く、2023年度末に薬局が1つもない町村は10あります。全国の138町村のうち、北海道（27）・長野県（13）・奈良県（12）・福島県（11）に次ぐ数です。

```sql
SELECT * FROM no_pharmacy
```

## 人口あたりの薬局数と一般診療所数の相関は、2023年度で0.43

1975年度の沖縄県は、人口あたりの一般診療所が47都道府県で最も少ないのに、薬局は最も多い県でした。一般診療所1施設あたりの薬局の数は1.18で、47都道府県の合計（0.37）の3倍でした。2023年度は0.62で、合計の0.60とほぼ同じになりました。

下の図は、1975年度と2023年度の都道府県ごとの人口10万人あたりの一般診療所数（横軸）と薬局数（縦軸）です。一般診療所数は10月1日、薬局数はその年度末の値です。

```chart
{
  "data": {"name": "clinic"},
  "facet": {"field": "fiscal_year", "type": "nominal", "title": null},
  "columns": 2,
  "spec": {
    "height": 260,
    "mark": {"type": "circle", "size": 60, "opacity": 0.8},
    "encoding": {
      "x": {"field": "clinics_per_100k", "type": "quantitative", "title": "人口10万人あたりの一般診療所数"},
      "y": {"field": "pharmacies_per_100k", "type": "quantitative", "title": "人口10万人あたりの薬局数"},
      "color": {
        "field": "grp",
        "type": "nominal",
        "title": null,
        "scale": {"domain": ["沖縄県", "ほかの46都道府県"], "range": ["#7c3aed", "#94a3b8"]}
      },
      "tooltip": [
        {"field": "area_name", "title": "都道府県"},
        {"field": "clinics_per_100k", "title": "一般診療所", "format": ".1f"},
        {"field": "pharmacies_per_100k", "title": "薬局", "format": ".1f"},
        {"field": "pharmacies_per_clinic", "title": "診療所あたりの薬局", "format": ".2f"}
      ]
    }
  }
}
```

人口あたりの薬局数と一般診療所数の相関係数は、1975年度の0.09から1995年度の0.37まで上がりました。その後は1995〜2012年度が0.33〜0.39で、最も高い2021年度でも0.48、2023年度は0.43です。一般診療所1施設あたりの薬局の数は、47都道府県の合計で0.37から0.60に増えています。診療所の多い県に薬局も多いという関係は1990年代までに表れましたが、関係は弱いままです。東京都は人口あたりの一般診療所が多いのに、薬局は33位です。

## 業務での使い方

- 薬局の店舗開発の担当者が人口あたりの薬局数で出店先を絞るときは、同じ県の一般診療所1施設あたりの薬局数も並べます。2023年度に人口あたりの薬局が少ない6県は2つに分かれます。千葉県（0.68）・埼玉県（0.71）・沖縄県（0.62）は診療所あたりでは47都道府県の合計（0.60）を上回り、診療所そのものが人口に比べて少ない県です。奈良県（0.47）・福井県（0.58）・神奈川県（0.59）は合計を下回り、診療所の数に比べて薬局が少ない県です。このデータには処方箋の枚数も、診療所が院外に処方箋を出す割合もないので、後者の県で薬局を増やす余地があるかは、県内の処方箋の枚数で確認する必要があります
- 県で医薬品の提供体制を担当する職員は、自分の県の順位を1975年度から年度ごとに並べ、順位が下がり始めた年度と、そのとき薬局数が増えていたかを確認します。沖縄県は1986年度から薬局数がほとんど増えないまま順位を下げました。東京都は人口10万人あたりの薬局数が30.7から50.5に増えても、ほかの県の伸びに届かず4位から33位になりました。薬局数は各年度末の許可数で、開設と廃止を差し引いた数です。沖縄県は薬局数がほとんど増えていない県、東京都は増えていても全国より伸びが小さい県で、自分の県がどちらに近いかを判定すると、県内の市区町村ごとの薬局数を確認するときに、薬局が増えていない地域と伸びの小さい地域のどちらを探せばよいかが決まります

```sql
SELECT * FROM clinic WHERE fiscal_year = '2023年度' AND area_name IN ('沖縄県', '千葉県', '埼玉県', '奈良県', '福井県', '神奈川県') ORDER BY pharmacies_per_100k
```

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別データを2026年11月18日時点で集計しています。薬局数と無薬局町村数の元データは厚生労働省の[衛生行政報告例](https://www.mhlw.go.jp/toukei/list/36-19.html)、一般診療所数は厚生労働省の[医療施設調査](https://www.mhlw.go.jp/toukei/list/79-1.html)、総人口は総務省の[国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)と[人口推計](https://www.stat.go.jp/data/jinsui/index.html)です。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の健康・医療テーブル](/datasets/queria/e_stat/ssds/i_pref_health)から、担当する県の薬局数と一般診療所数の推移を年度ごとに取り出せます。

```sql id=ranks
-- 1975年度と2023年度の人口10万人あたり薬局数と順位（47都道府県）
WITH ph AS (SELECT DISTINCT year, area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), pop AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), d AS (SELECT ph.year, ph.area_name, ph.v AS n, pop.v AS pop, ph.v / pop.v * 100000 AS p, RANK() OVER (PARTITION BY ph.year ORDER BY ph.v / pop.v DESC) AS rk FROM ph JOIN pop ON ph.area = pop.area AND ph.year = pop.year) SELECT a.area_name, ROUND(a.p, 1) AS per_100k_1975, a.rk AS rank_1975, ROUND(b.p, 1) AS per_100k_2023, b.rk AS rank_2023 FROM d a JOIN d b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023 ORDER BY b.p DESC
```

```sql id=summary
-- 2つの年度の順位の相関と、順位が大きく動いた県の数（プロットはしない）
WITH ph AS (SELECT DISTINCT year, area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), pop AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), d AS (SELECT ph.year, ph.area_name, ph.v AS n, pop.v AS pop, ph.v / pop.v * 100000 AS p, RANK() OVER (PARTITION BY ph.year ORDER BY ph.v / pop.v DESC) AS rk FROM ph JOIN pop ON ph.area = pop.area AND ph.year = pop.year) SELECT ROUND(CORR(a.rk, b.rk), 2) AS rank_corr_1975_2023, COUNT(*) FILTER (WHERE a.rk <= 10 AND b.rk >= 25) AS top10_1975_now_25th_or_lower, COUNT(*) FILTER (WHERE a.rk >= 38 AND b.rk <= 23) AS bottom10_1975_now_23rd_or_higher, COUNT(*) FILTER (WHERE b.p < a.p) AS prefs_per_100k_decreased, COUNT(*) AS prefs FROM d a JOIN d b ON a.area_name = b.area_name AND a.year = 1975 AND b.year = 2023
```

```sql id=spread
-- 年度ごとの最多÷最少と変動係数
WITH ph AS (SELECT DISTINCT year, area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), pop AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), d AS (SELECT ph.year, ph.area_name, ph.v AS n, pop.v AS pop, ph.v / pop.v * 100000 AS p, RANK() OVER (PARTITION BY ph.year ORDER BY ph.v / pop.v DESC) AS rk FROM ph JOIN pop ON ph.area = pop.area AND ph.year = pop.year) SELECT year, ROUND(MAX(p) / MIN(p), 2) AS max_min_ratio, ROUND(STDDEV_POP(p) / AVG(p), 3) AS cv, ARG_MAX(area_name, p) AS top_pref, ROUND(MAX(p), 1) AS top_per_100k, ARG_MIN(area_name, p) AS bottom_pref, ROUND(MIN(p), 1) AS bottom_per_100k FROM d GROUP BY year ORDER BY year
```

```sql id=okinawa
-- 沖縄県と47都道府県の合計の薬局数と人口10万人あたりの値
WITH ph AS (SELECT DISTINCT year, area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), pop AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), d AS (SELECT ph.year, ph.area_name, ph.v AS n, pop.v AS pop, ph.v / pop.v * 100000 AS p, RANK() OVER (PARTITION BY ph.year ORDER BY ph.v / pop.v DESC) AS rk FROM ph JOIN pop ON ph.area = pop.area AND ph.year = pop.year) SELECT year, '沖縄県' AS series, n AS pharmacies, ROUND(p, 1) AS per_100k, rk AS rank FROM d WHERE area_name = '沖縄県' UNION ALL SELECT year, '47都道府県の合計' AS series, SUM(n), ROUND(SUM(n) / SUM(pop) * 100000, 1), NULL FROM d GROUP BY year ORDER BY series, year
```

```sql id=no_pharmacy
-- 2023年度末に薬局の無い町村の数（多い5道県と全国の合計）
WITH t AS (SELECT DISTINCT area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7103' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT area_name, v AS towns_without_pharmacy, SUM(v) OVER () AS national_total FROM t ORDER BY v DESC, area_name LIMIT 5
```

```sql id=clinic
-- 1975年度と2023年度の人口10万人あたりの一般診療所数・薬局数
WITH ph AS (SELECT DISTINCT year, area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), cl AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), pop AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), d AS (SELECT ph.year, ph.area_name, ph.v AS n, cl.v AS clinics, ph.v / pop.v * 100000 AS p, cl.v / pop.v * 100000 AS c FROM ph JOIN cl ON ph.area = cl.area AND ph.year = cl.year JOIN pop ON ph.area = pop.area AND ph.year = pop.year) SELECT year::VARCHAR || '年度' AS fiscal_year, area_name, ROUND(c, 1) AS clinics_per_100k, ROUND(p, 1) AS pharmacies_per_100k, ROUND(n / clinics, 2) AS pharmacies_per_clinic, CASE WHEN area_name = '沖縄県' THEN '沖縄県' ELSE 'ほかの46都道府県' END AS grp FROM d WHERE year IN (1975, 2023) ORDER BY year, area_name
```

```sql id=clinic_corr
-- 年度ごとの、人口あたり薬局数と一般診療所数の相関と、診療所1施設あたりの薬局数（プロットはしない）
WITH ph AS (SELECT DISTINCT year, area, area_name, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I7102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), cl AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5102' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), pop AS (SELECT DISTINCT year, area, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 1975 AND 2023), d AS (SELECT ph.year, ph.area_name, ph.v AS n, cl.v AS clinics, ph.v / pop.v * 100000 AS p, cl.v / pop.v * 100000 AS c FROM ph JOIN cl ON ph.area = cl.area AND ph.year = cl.year JOIN pop ON ph.area = pop.area AND ph.year = pop.year) SELECT year, ROUND(CORR(p, c), 2) AS corr_pharmacy_clinic, ROUND(SUM(n) / SUM(clinics), 2) AS pharmacies_per_clinic FROM d GROUP BY year ORDER BY year
```
