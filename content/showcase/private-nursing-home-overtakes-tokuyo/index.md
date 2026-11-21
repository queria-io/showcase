---
title: 有料老人ホームの定員が特養を上回る県は、10年で14から36に増えた
description: 有料老人ホームと特養の定員を、都道府県別に2014年から2024年まで比較しました。有料老人ホームのほうが多い県は14から36に増え、75歳以上1,000人あたりの有料老人ホームの定員は県によって3.5倍違います。
publishedAt: 2026-10-03
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 有料老人ホーム
  - 特別養護老人ホーム
  - 介護
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 社会福祉施設等調査
    url: https://www.mhlw.go.jp/toukei/saikin/hw/fukushi/24/index.html
    publisher: 厚生労働省
  - title: 介護サービス施設・事業所調査
    url: https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/service24/index.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
agentHint: e_stat.welfare_facility.facility_statistics の有料老人ホームと e_stat.kaigo_service.insurance_facility の介護老人福祉施設の定員を、自分の県と隣接県について2014年から2024年まで並べて出して。75歳以上人口（e_stat.ssds.a_pref_population の A1419）あたりでも比べたい
socialAnnounce: |-
  有料老人ホームと特養の定員を、都道府県別に2014年から2024年まで比べました。

  有料老人ホームの開設エリアの検討や、地域の介護施設の供給を読むときに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

有料老人ホームの定員が特別養護老人ホーム（特養）の定員より多い都道府県は、2014年の14から2024年の36に増えました。全国の有料老人ホームの定員は10年で2.0倍、特養は1.2倍です。75歳以上1,000人あたりの有料老人ホームの定員が最も多いのは沖縄県の76.1人分で、大分県・宮崎県が続き、最も少ない山梨県・福井県の21.7人分とは3.5倍の差があります。東京都は15位でした。

有料老人ホームの開設先を探すときは、その地域の高齢者の数と、すでにある施設の定員を確認します。有料老人ホームと特養の定員を都道府県ごとに2014年から2024年まで並べ、75歳以上の人口と比較しました。

## 有料老人ホームのほうが多い県は、10年で14から36に増えた

有料老人ホームの定員は厚生労働省の[社会福祉施設等調査](https://www.mhlw.go.jp/toukei/saikin/hw/fukushi/24/index.html)、特養の定員は同じく[介護サービス施設・事業所調査](https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/service24/index.html)から取っています。どちらも毎年10月1日現在の値で、別々の調査です。Queria ではそれぞれ次のテーブルに収録しています。

| テーブル                               | 使う区分                                                                                                 | 内容                                  |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `welfare_facility.facility_statistics` | 有料老人ホーム（サービス付き高齢者向け住宅以外）、有料老人ホーム（サービス付き高齢者向け住宅であるもの） | 2つを足して有料老人ホームの定員とする |
| `kaigo_service.insurance_facility`     | 介護老人福祉施設                                                                                         | 定員30人以上の特養の定員              |

どちらも、全施設から届く基本票の定員（`measure = 'capacity'`、`survey_form = '基本票'`）を使っています。有料老人ホームの定員には、介護職員が常駐する介護付きと、外部の介護サービスを使う住宅型の両方が入っていて、このデータでは分けられません。サービス付き高齢者向け住宅は、食事の提供などで有料老人ホームに当たるものだけが含まれます。

特養の定員には、定員29人以下の地域密着型の特養を含みません。地域密着型を加えると特養の定員は増えるので、次の図の県の数は、有料老人ホームと特養の差が小さい県の分だけ多く出ている可能性があります。反対に、有料老人ホームのうちサービス付き高齢者向け住宅であるもの（2024年は全国で222,874人分）を除くと、有料老人ホームが上回る県は2014年の10から2024年の21になります。県の数はどこまでを有料老人ホームに含めるかで変わりますが、どちらの集計でも10年で2倍以上に増えています。

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "cross_count"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "prefs", "type": "quantitative"},
          {"field": "year", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "prefs",
          "type": "quantitative",
          "scale": {"domain": [0, 47], "zero": false, "nice": false},
          "axis": {"title": "有料老人ホームの定員が特養を上回る都道府県の数", "grid": true}
        }
      }
    },
    {
      "data": {"name": "cross_count"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "prefs",
          "type": "quantitative",
          "scale": {"domain": [0, 47], "zero": false, "nice": false},
          "axis": {"title": "有料老人ホームの定員が特養を上回る都道府県の数", "grid": true}
        },
        "text": {"field": "prefs"}
      }
    }
  ]
}
```

有料老人ホームの定員が特養より多い都道府県は、2014年の14から2024年の36へ、10年で一度も減らずに増えました。2024年に新しく加わったのは京都府で、有料老人ホーム12,630人分に対して特養12,558人分と、ほぼ同じ数です。京都府のように差が小さい県は、地域密着型の特養を含めると特養のほうが多くなる可能性があります。

特養のほうが多いまま残っているのは、新潟県・福井県・秋田県・福島県・滋賀県・茨城県・山形県・山梨県・岩手県・長野県・高知県の11県です。高知県は有料老人ホーム4,198人分に対して特養4,209人分で、差は11人分しかありません。

## 75歳以上1,000人あたりの定員は、特養が31.3人分から29.1人分に下がり、有料老人ホームは29.9人分から45.2人分に上がった

施設に入る人の多くは75歳以上なので、総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)から都道府県別の75歳以上人口（`A1419`）を取得し、75歳以上1,000人あたりの定員を計算しました。75歳以上人口は2015年と2020年が国勢調査、それ以外の年は推計人口なので、図の2019年から2020年に段差があります。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"yuryo_per_1000\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "yuryo_per_1000", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "yuryo_per_1000",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "75歳以上1,000人あたりの定員（人分）", "grid": true}
        },
        "color": {
          "datum": "有料老人ホーム",
          "type": "nominal",
          "scale": {"domain": ["有料老人ホーム", "特養"], "range": ["#7c3aed", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokuyo_per_1000\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "tokuyo_per_1000", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokuyo_per_1000",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "75歳以上1,000人あたりの定員（人分）", "grid": true}
        },
        "color": {
          "datum": "特養",
          "type": "nominal",
          "scale": {"domain": ["有料老人ホーム", "特養"], "range": ["#7c3aed", "#94a3b8"]},
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

全国の有料老人ホームの定員は、2014年の475,284人分から2024年の939,033人分へ、10年で2.0倍になりました。特養は498,327人分から604,469人分で1.2倍です。全国の合計では2015年に有料老人ホームが特養を上回りました。

75歳以上の人口はこの10年で1,592万人から2,078万人に増えています。その1,000人あたりで見ると、特養は31.3人分から29.1人分へ下がり、有料老人ホームは29.9人分から45.2人分へ上がりました。都道府県別でも、75歳以上あたりの有料老人ホームの定員は47都道府県すべてで増え、特養は39都道府県で減っています。75歳以上の人口が増えた分に対応する定員は、主に有料老人ホームで増えました。ここでの定員は入居できる人数の上限で、入居している人の数とは異なります。

## 75歳以上あたりの有料老人ホームの定員が多いのは、沖縄県・大分県・宮崎県

都道府県ごとに、2024年の75歳以上1,000人あたりの定員を並べました。紫が有料老人ホーム、灰色が特養で、有料老人ホームの多い順です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank2024"},
      "transform": [
        {"fold": ["yuryo_per_1000", "tokuyo_per_1000"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"yuryo_per_1000\": \"有料老人ホーム\", \"tokuyo_per_1000\": \"特養\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"yuryo_per_1000\",\"tokuyo_per_1000\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "75歳以上1,000人あたりの定員（人分、2024年）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["有料老人ホーム", "特養"], "range": ["#7c3aed", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

有料老人ホームの定員が75歳以上1,000人あたりで最も多いのは沖縄県の76.1人分で、大分県73.8人分、宮崎県72.6人分が続きます。大阪府（66.3人分）と福岡県（65.2人分）が続くので都市部も多い側に入りますが、東京都は45.7人分で15位です。最も少ないのは山梨県と福井県の21.7人分で、沖縄県とは3.5倍の差があります。

特養は、最も多い新潟県の40.4人分から最も少ない大分県の22.8人分まで、差は1.8倍です。大分県は有料老人ホームの定員が特養の3.2倍あり、特養が少ない県で有料老人ホームが多い組み合わせになっています。反対に、75歳以上あたりの特養が最も多い新潟県（40.4人分）と2番目の福島県（40.1人分）は、有料老人ホームが少ないほうから3番目と6番目です。47都道府県で両者の相関係数を取ると-0.42で、特養の多い県ほど有料老人ホームが少ない傾向があります。有料老人ホームの定員の多さは、都市か地方かだけでは決まらず、その県で特養がどれだけ整備されてきたかとも関係していると考えられます。

## 開設エリアを検討するときの使い方

- 候補の県の75歳以上1,000人あたりの有料老人ホーム定員を、2024年の都道府県の中央値（37.6人分）と比較します。中央値を大きく上回る県では、既存の有料老人ホームと入居者を取り合うことを前提に、自社の入居実績から需要を確認する必要があります。下回る県では、特養と合わせた定員が75歳以上1,000人あたり何人分あるかを先に確認します
- 定員がこの10年で急に増えた県は、増加の倍率で分かります。75歳以上あたりの有料老人ホームの定員が最も伸びたのは富山県で、8.5人分から29.1人分へ3.45倍になりました。岐阜県が2.88倍、徳島県が2.67倍で続き、3県とも2014年には75歳以上1,000人あたり15人分に届いていませんでした。3県とも2024年の値は中央値以下ですが、この10年で競合の開設が続いてきた県です
- 介護付きと住宅型の内訳や入居率はこのデータにないので、自社の入居実績や自治体の介護保険事業計画と合わせて判断します

## データの出典

本記事は厚生労働省の[社会福祉施設等調査](https://www.mhlw.go.jp/toukei/saikin/hw/fukushi/24/index.html)・[介護サービス施設・事業所調査](https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/service24/index.html)と、総務省統計局の[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の都道府県別データを、2026-10-03時点で集計しています。施設の定員はいずれも各年10月1日現在の値です。

Queriaは、有料老人ホームと特養の定員を収録した2つの調査と人口統計を、列名・単位を統一し、テーブルと列の説明を付けて公開しています。本記事で使った[社会福祉施設等調査のテーブル](/datasets/e_stat/welfare_facility/facility_statistics)と[介護保険施設のテーブル](/datasets/e_stat/kaigo_service/insurance_facility)から、開設を検討している県の定員の推移を確認したり、市区町村ごとに特養の定員を集計したりできます。

```sql id=caps
-- 都道府県×年の有料老人ホーム・特養の定員と75歳以上人口（2014〜2024年）
WITH yuryo AS (
  SELECT
    survey_year AS yr,
    prefecture_code AS pc,
    SUM(value) AS cap,
    SUM(value) FILTER (WHERE facility_type = '有料老人ホーム（サービス付き高齢者向け住宅以外）') AS cap_ex
  FROM e_stat.welfare_facility.facility_statistics
  WHERE facility_type IN ('有料老人ホーム（サービス付き高齢者向け住宅以外）', '有料老人ホーム（サービス付き高齢者向け住宅であるもの）')
    AND measure = 'capacity' AND operator = '総数' AND survey_form = '基本票'
    -- 2017年までは政令指定都市・中核市の施設が県の行と別建てなので、県コードで足し合わせる
    AND area_kind IN ('prefecture', 'designated_city', 'core_city')
    AND survey_year BETWEEN 2014 AND 2024
  GROUP BY ALL
), tokuyo AS (
  SELECT survey_year AS yr, prefecture_code AS pc, prefecture_name AS pref, SUM(value) AS cap
  FROM e_stat.kaigo_service.insurance_facility
  WHERE facility_type = '介護老人福祉施設' AND measure = 'capacity' AND survey_form = '基本票'
    AND area_kind = 'prefecture' AND survey_year BETWEEN 2014 AND 2024
  GROUP BY ALL
), pop AS (
  SELECT year AS yr, area_name AS pref, TRY_CAST(value AS DOUBLE) AS pop75
  FROM e_stat.ssds.a_pref_population
  WHERE cat01 = 'A1419' AND area_name <> '全国' AND year BETWEEN 2014 AND 2024
)
SELECT t.yr AS year, t.pc AS prefecture_code, t.pref, CAST(y.cap AS DOUBLE) AS yuryo, CAST(y.cap_ex AS DOUBLE) AS yuryo_excl_sakoju, CAST(t.cap AS DOUBLE) AS tokuyo, p.pop75
FROM tokuyo t
JOIN yuryo y ON y.yr = t.yr AND y.pc = t.pc
JOIN pop p ON p.yr = t.yr AND p.pref = t.pref
```

```sql id=cross_count
SELECT
  year,
  COUNT(*) FILTER (WHERE yuryo > tokuyo) AS prefs,
  -- サービス付き高齢者向け住宅である有料老人ホームを除いた場合（プロットはしない）
  COUNT(*) FILTER (WHERE yuryo_excl_sakoju > tokuyo) AS prefs_excl_sakoju,
  COUNT(*) AS all_prefs
FROM caps
GROUP BY year
ORDER BY year
```

```sql id=national
SELECT
  year,
  SUM(yuryo) AS yuryo,
  SUM(yuryo - yuryo_excl_sakoju) AS yuryo_sakoju,
  SUM(tokuyo) AS tokuyo,
  SUM(pop75) AS pop75,
  ROUND(1000 * SUM(yuryo) / SUM(pop75), 1) AS yuryo_per_1000,
  ROUND(1000 * SUM(tokuyo) / SUM(pop75), 1) AS tokuyo_per_1000
FROM caps
GROUP BY year
ORDER BY year
```

```sql id=rank2024
SELECT
  RANK() OVER (ORDER BY ROUND(1000 * yuryo / pop75, 1) DESC) AS yuryo_rank,
  pref,
  yuryo,
  tokuyo,
  ROUND(1000 * yuryo / pop75, 1) AS yuryo_per_1000,
  ROUND(1000 * tokuyo / pop75, 1) AS tokuyo_per_1000,
  ROUND(yuryo / tokuyo, 2) AS yuryo_to_tokuyo
FROM caps
WHERE year = 2024
ORDER BY yuryo / pop75 DESC, prefecture_code
```

```sql id=change_2014_2024
-- 10年間の75歳以上1,000人あたり定員の変化と、2024年の両者の相関（プロットはしない）
SELECT
  COUNT(*) FILTER (WHERE y24 > y14) AS prefs_yuryo_up,
  COUNT(*) FILTER (WHERE t24 < t14) AS prefs_tokuyo_down,
  ROUND(MIN(y24 / y14), 2) AS yuryo_growth_min,
  ROUND(MAX(y24 / y14), 2) AS yuryo_growth_max,
  ROUND(CORR(y24, t24), 2) AS corr_2024,
  ROUND(1000 * MEDIAN(y24), 1) AS yuryo_per_1000_median_2024
FROM (
  SELECT
    pref,
    MAX(yuryo / pop75) FILTER (WHERE year = 2014) AS y14,
    MAX(yuryo / pop75) FILTER (WHERE year = 2024) AS y24,
    MAX(tokuyo / pop75) FILTER (WHERE year = 2014) AS t14,
    MAX(tokuyo / pop75) FILTER (WHERE year = 2024) AS t24
  FROM caps
  GROUP BY pref
) AS w
```

```sql id=growth
-- 75歳以上1,000人あたりの有料老人ホーム定員の10年の伸び（プロットはしない）
SELECT
  pref,
  ROUND(1000 * MAX(yuryo / pop75) FILTER (WHERE year = 2014), 1) AS yuryo_per_1000_2014,
  ROUND(1000 * MAX(yuryo / pop75) FILTER (WHERE year = 2024), 1) AS yuryo_per_1000_2024,
  ROUND(MAX(yuryo / pop75) FILTER (WHERE year = 2024) / MAX(yuryo / pop75) FILTER (WHERE year = 2014), 2) AS growth
FROM caps
GROUP BY pref
ORDER BY growth DESC, pref
```
