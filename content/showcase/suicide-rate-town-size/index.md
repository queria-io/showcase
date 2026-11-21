---
title: 男性の自殺死亡率は、人口1万人未満の市町村で人口20万人以上の市区の1.3〜1.4倍。20〜59歳の女性ではこの差がほとんど無い
description: 2022〜2025年の市区町村別の自殺者数を人口規模で分けて集計しました。男性は20〜39歳・40〜59歳・60歳以上のどれでも人口の少ない市町村ほど高く、人口1万人未満の市町村は人口20万人以上の市区の1.3〜1.4倍です。20〜59歳の女性は、規模による差が人口10万人あたり2.6以内でした
publishedAt: 2026-11-13
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 自殺対策
  - 市区町村
  - 人口規模
datasets:
  - queria/mhlw
  - queria/e_stat
sources:
  - title: 地域における自殺の基礎資料
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000140901.html
    publisher: 厚生労働省
  - title: 令和7年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2025/index.html
    publisher: 総務省統計局
  - title: "Geography of suicide in Japan: spatial patterning and rural-urban differences"
    url: https://doi.org/10.1007/s00127-020-01978-7
    publisher: Social Psychiatry and Psychiatric Epidemiology
agentHint: 2022〜2025年の自殺者数を、20歳代から80歳以上までの10歳刻みで、人口1万人未満の市町村と人口20万人以上の市区に分けて人口10万人あたりで出して。男女別に、小さい市町村の値が大きい市区の何倍かも並べて
socialAnnounce: |-
  2022〜2025年の市区町村別の自殺者数を、市区町村の人口規模で分けました。

  40〜59歳の男性は、人口1万人未満の市町村で人口10万人あたり40.7、人口20万人以上の市区で28.8。
  女性は同じ年代で12.6と12.3で、規模による差がほとんどありませんでした。
---

2022〜2025年の4年分の市区町村別の自殺者数を、市区町村の人口規模と性・年齢で分けて人口あたりの値にすると、男性は20〜39歳・40〜59歳・60歳以上のどの年代でも、人口の少ない市町村ほど高くなりました。人口1万人未満の市町村の値は、人口20万人以上の市区の1.3〜1.4倍です。20〜59歳の女性は、規模による差が人口10万人あたり2.6以内でした。60歳以上の女性は、人口の少ない市町村がやや高くなっています。

市区町村は、地域の実情に合わせた自殺対策計画を作ることになっています。計画で重点を置く対象を決めるときに、自分の市区町村と同じくらいの規模の市区町村でどの性・年代の自殺が多いかを、判断の材料にできます。

2021年に発表された研究（Yoshioka ほか、Social Psychiatry and Psychiatric Epidemiology）は、全国の市区町村を対象に、都市と農村の自殺の多さの違いを性・年齢別に分析しています。男性の40歳未満と40〜59歳で農村ほど高く、40歳未満の女性では農村との関係が見られなかったと報告しています。この記事では、研究より後の2022〜2025年のデータを、市区町村の人口規模で分けて比較しました。

## 40〜59歳の男性は、人口1万人未満の市町村で40.7、人口20万人以上の市区で28.8

自殺者数は厚生労働省の[地域における自殺の基礎資料](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000140901.html)の月別・市区町村別の値で、亡くなった人が住んでいた市区町村（住居地）で集計しています。2022〜2025年の48か月分の合計を、[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)の年齢別人口の4年分で割り、1年あたりの人口10万人あたりの値にしました。20歳未満は自殺者数が少ないので除いています。

人口規模は、国勢調査の年齢別人口（年齢不詳を除く）を合計した市区町村の人口で4つに分けました。政令指定都市と東京都の特別区は区ごとに集計しています。2024年に区を再編した浜松市は、2022〜2023年の区と国勢調査の区が対応しないので、市全体で集計しています。

| 人口規模   | 市区町村数 |
| ---------- | ---------- |
| 1万人未満  | 571        |
| 1〜5万人   | 673        |
| 5〜20万人  | 495        |
| 20万人以上 | 151        |

```chart caption="人口10万人あたりの自殺死亡率（2022〜2025年の1年あたり）"
{
  "data": { "name": "by_size" },
  "mark": "bar",
  "encoding": {
    "x": { "field": "sex_age", "type": "nominal", "sort": { "field": "group_order" }, "title": null, "axis": { "labelAngle": 0 } },
    "xOffset": { "field": "size_class", "sort": { "field": "size_order" } },
    "y": { "field": "rate", "type": "quantitative", "title": "人口10万人あたり" },
    "color": { "field": "size_class", "type": "nominal", "sort": { "field": "size_order" }, "title": "市区町村の人口", "scale": { "range": ["#1e3a8a", "#3b82f6", "#93c5fd", "#94a3b8"] } },
    "tooltip": [
      { "field": "sex_age", "title": "性・年齢" },
      { "field": "size_class", "title": "市区町村の人口" },
      { "field": "rate", "title": "人口10万人あたり" },
      { "field": "suicides", "title": "4年間の自殺者数", "format": "," }
    ]
  }
}
```

男性は3つの年代のすべてで、規模が小さいほど値が高くなります。40〜59歳は規模の小さい順に40.7、35.3、30.4、28.8で、人口1万人未満の市町村は人口20万人以上の市区の1.4倍です。20〜39歳は33.1から24.8、60歳以上は34.5から24.2まで下がります。

20〜59歳の女性は、4つの規模の値が近く、規模の順にも並んでいません。20〜39歳は12.1、11.1、12.7、13.7で、40〜59歳は12.6、11.4、12.6、12.3です。人口1万人未満の市町村の20〜59歳の女性では、人口10万人あたり1ポイントの差は、571市町村を合わせて1年に2〜3人の違いにあたります。60歳以上の女性は12.8、11.1、10.8、10.6と規模の順に下がり、人口1万人未満の市町村は人口20万人以上の市区の1.2倍です。

男性の20〜39歳と40〜59歳で人口の少ない市町村ほど高い点は、先の研究と同じです。研究は60歳以上の男性について、社会経済的な特性で調整すると都市と農村の差が明確でないと報告しています。この記事の値は調整をしていない人口あたりの値です。ただし、60歳以上の男性に占める80歳以上の割合は、人口1万人未満の市町村で25.0%、人口20万人以上の市区で24.0%とほぼ同じで、男性60歳以上の差はこの割合の違いによるものではありません。研究は、女性の40〜59歳と60歳以上で、都市と農村の両端が高いU字形の関係を報告しています。この記事の値では、40〜59歳の両端と中間の差は1ポイント前後で、60歳以上は人口の少ない市町村ほどやや高くなっています。

## 男性は2022年から2025年のどの年も、人口1万人未満の市町村が最も高い

人口の少ない市町村は、1年分だけでは値が大きく変動します。男性の差が特定の年だけのものでないかを確認するため、20歳以上をまとめて年ごとに集計しました。

```chart caption="20歳以上の男性の年ごとの自殺死亡率（人口10万人あたり）"
{
  "data": { "name": "yearly" },
  "transform": [{ "filter": "datum.panel === '男性'" }],
  "mark": { "type": "line", "point": true },
  "encoding": {
    "x": { "field": "year", "type": "ordinal", "title": null, "axis": { "labelAngle": 0 } },
    "y": { "field": "rate", "type": "quantitative", "title": "人口10万人あたり", "scale": { "domain": [0, 40] } },
    "color": { "field": "size_class", "type": "nominal", "sort": { "field": "size_order" }, "title": "市区町村の人口", "scale": { "range": ["#1e3a8a", "#3b82f6", "#93c5fd", "#94a3b8"] } },
    "tooltip": [
      { "field": "size_class", "title": "市区町村の人口" },
      { "field": "year", "title": "年" },
      { "field": "rate", "title": "人口10万人あたり" }
    ]
  }
}
```

```chart caption="20歳以上の女性の年ごとの自殺死亡率（人口10万人あたり）"
{
  "data": { "name": "yearly" },
  "transform": [{ "filter": "datum.panel === '女性'" }],
  "mark": { "type": "line", "point": true },
  "encoding": {
    "x": { "field": "year", "type": "ordinal", "title": null, "axis": { "labelAngle": 0 } },
    "y": { "field": "rate", "type": "quantitative", "title": "人口10万人あたり", "scale": { "domain": [0, 40] } },
    "color": { "field": "size_class", "type": "nominal", "sort": { "field": "size_order" }, "title": "市区町村の人口", "scale": { "range": ["#1e3a8a", "#3b82f6", "#93c5fd", "#94a3b8"] } },
    "tooltip": [
      { "field": "size_class", "title": "市区町村の人口" },
      { "field": "year", "title": "年" },
      { "field": "rate", "title": "人口10万人あたり" }
    ]
  }
}
```

男性は2022年から2025年のどの年も、人口1万人未満の市町村が最も高く、人口20万人以上の市区が最も低くなっています。4つの規模とも値は下がっていて、1万人未満の市町村は38.3から32.9、20万人以上の市区は27.4から24.6になりました。

女性は年によって規模の順位が入れ替わります。人口1万人未満の市町村は2022年と2023年に4つの規模で最も高く、2025年は9.7で2番目に低くなっています。

2026年1月以降の月は暫定値で、確定値の公表時に差し替わるので、集計は確定値が公表されている2025年までです。

## 自殺対策計画の重点対象を決めるときの使い方

- 人口の少ない市町村の計画では、男性への対策の比重を大きな市区より高くする根拠になります。人口1万人未満の市町村の男性の値は、20〜39歳・40〜59歳・60歳以上のどれでも人口20万人以上の市区の1.3〜1.4倍で、20〜59歳の女性には同じ差がありません
- 自分の市区町村の値は、同じ規模の市区町村の合計と比較できます。人口の少ない市町村は1年に数人の違いで値が大きく変わるので、数年分を合計するか、近隣の市町村と合わせて集計する必要があります
- 20〜59歳の女性は規模による差が小さいので、規模の近い市区町村の値より、自分の市区町村の数年分の推移を確認するほうが判断の材料になります

## データの出典

本記事は厚生労働省の[地域における自殺の基礎資料](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000140901.html)の月別・市区町村別の自殺者数（2022〜2025年、確定値）と、総務省の[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)の市区町村別・年齢別人口を、2026-11-13 時点で集計しています。都市と農村の比較の切り口は Yoshioka ほか（2021）の[研究](https://doi.org/10.1007/s00127-020-01978-7)を参考にしています。

Queriaは、厚生労働省の自殺の統計や国勢調査を、列名・単位・地域コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[月別・市区町村別の自殺者数のテーブル](/datasets/queria/mhlw/jisatsu/suicide_municipality_monthly)と[2025年国勢調査の年齢別人口のテーブル](/datasets/queria/e_stat/census/census_municipality_age_2025)から、自分の市区町村と同じ規模の市区町村の値を確認できます。

## 相談窓口

悩みを抱えている方は、厚生労働省の[まもろうよ こころ](https://www.mhlw.go.jp/mamorouyokokoro/)で電話・SNSの相談窓口を探せます。

```sql id=by_size
-- 人口規模 × 性 × 年齢層の自殺死亡率（2022〜2025年の1年あたり、人口10万人あたり）
-- 政令指定都市と東京都の特別区は区ごとに数える。2024年に区を再編した浜松市（22130）は、
-- 2022〜2023年の旧区と国勢調査の新しい区が対応しないので市全体で数える
WITH s AS (
  SELECT city_code, sex,
    CASE WHEN category IN ('20-29歳', '30-39歳') THEN '20〜39歳'
         WHEN category IN ('40-49歳', '50-59歳') THEN '40〜59歳'
         WHEN category IN ('60-69歳', '70-79歳', '80歳以上') THEN '60歳以上' END AS age_group,
    sum(count) AS n
  FROM mhlw.jisatsu.suicide_municipality_monthly
  WHERE location_basis = '住居地' AND attribute = '年齢階級' AND sex IN ('男', '女')
    AND year BETWEEN 2022 AND 2025
    AND ((area_level = '市区町村' AND (substr(city_code, 3, 1) <> '1' OR city_code = '22130'))
      OR (area_level = '区' AND city_code NOT BETWEEN '22131' AND '22140'))
  GROUP BY ALL
),
a AS (
  SELECT * FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'town_village', 'ward') AND age_from IS NOT NULL
    AND NOT (area_level = 'city' AND substr(area, 3, 1) = '1' AND area <> '22130')
    AND NOT (area_level = 'ward' AND area BETWEEN '22131' AND '22140')
),
t AS (SELECT area, sum(population_male + population_female) AS total FROM a GROUP BY 1),
c AS (
  SELECT a.area, x.sex,
    CASE WHEN a.age_to <= 39 THEN '20〜39歳' WHEN a.age_from < 60 THEN '40〜59歳' ELSE '60歳以上' END AS age_group,
    sum(CASE x.sex WHEN '男' THEN a.population_male ELSE a.population_female END) AS pop
  FROM a CROSS JOIN (VALUES ('男'), ('女')) x(sex)
  WHERE a.age_from >= 20
  GROUP BY ALL
),
u AS (
  SELECT c.*, coalesce(s.n, 0) AS n,
    CASE WHEN t.total < 10000 THEN 1 WHEN t.total < 50000 THEN 2 WHEN t.total < 200000 THEN 3 ELSE 4 END AS size_order
  FROM c
  JOIN t USING (area)
  LEFT JOIN s ON s.city_code = c.area AND s.sex = c.sex AND s.age_group = c.age_group
)
SELECT sex || ' ' || age_group AS sex_age, sex, age_group,
  (CASE sex WHEN '男' THEN 0 ELSE 3 END) + (CASE age_group WHEN '20〜39歳' THEN 1 WHEN '40〜59歳' THEN 2 ELSE 3 END) AS group_order,
  CASE size_order WHEN 1 THEN '1万人未満' WHEN 2 THEN '1〜5万人' WHEN 3 THEN '5〜20万人' ELSE '20万人以上' END AS size_class,
  size_order,
  count(*) AS municipalities, sum(n) AS suicides,
  round(sum(n) / 4 / sum(pop) * 100000, 1) AS rate
FROM u
GROUP BY ALL
ORDER BY group_order, size_order
```

```sql id=yearly
-- 人口規模 × 性 × 年の自殺死亡率（20歳以上、人口10万人あたり）
WITH s AS (
  SELECT year, city_code, sex, sum(count) AS n
  FROM mhlw.jisatsu.suicide_municipality_monthly
  WHERE location_basis = '住居地' AND attribute = '年齢階級' AND sex IN ('男', '女')
    AND year BETWEEN 2022 AND 2025
    AND category IN ('20-29歳', '30-39歳', '40-49歳', '50-59歳', '60-69歳', '70-79歳', '80歳以上')
    AND ((area_level = '市区町村' AND (substr(city_code, 3, 1) <> '1' OR city_code = '22130'))
      OR (area_level = '区' AND city_code NOT BETWEEN '22131' AND '22140'))
  GROUP BY ALL
),
a AS (
  SELECT * FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'town_village', 'ward') AND age_from IS NOT NULL
    AND NOT (area_level = 'city' AND substr(area, 3, 1) = '1' AND area <> '22130')
    AND NOT (area_level = 'ward' AND area BETWEEN '22131' AND '22140')
),
t AS (SELECT area, sum(population_male + population_female) AS total FROM a GROUP BY 1),
c AS (
  SELECT a.area, x.sex,
    sum(CASE x.sex WHEN '男' THEN a.population_male ELSE a.population_female END) AS pop
  FROM a CROSS JOIN (VALUES ('男'), ('女')) x(sex)
  WHERE a.age_from >= 20
  GROUP BY ALL
),
u AS (
  SELECT y.year, c.sex, c.pop, coalesce(s.n, 0) AS n,
    CASE WHEN t.total < 10000 THEN 1 WHEN t.total < 50000 THEN 2 WHEN t.total < 200000 THEN 3 ELSE 4 END AS size_order
  FROM c
  JOIN t USING (area)
  CROSS JOIN (VALUES (2022), (2023), (2024), (2025)) y(year)
  LEFT JOIN s ON s.city_code = c.area AND s.sex = c.sex AND s.year = y.year
)
SELECT year, CASE sex WHEN '男' THEN '男性' ELSE '女性' END AS panel,
  CASE size_order WHEN 1 THEN '1万人未満' WHEN 2 THEN '1〜5万人' WHEN 3 THEN '5〜20万人' ELSE '20万人以上' END AS size_class,
  size_order,
  round(sum(n) / sum(pop) * 100000, 1) AS rate
FROM u
GROUP BY ALL
ORDER BY panel, size_order, year
```

```sql id=age80
-- 60歳以上の人口に占める80歳以上の割合（人口規模別）。プロットはしない
WITH a AS (
  SELECT * FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'town_village', 'ward') AND age_from IS NOT NULL
    AND NOT (area_level = 'city' AND substr(area, 3, 1) = '1' AND area <> '22130')
    AND NOT (area_level = 'ward' AND area BETWEEN '22131' AND '22140')
),
t AS (SELECT area, sum(population_male + population_female) AS total FROM a GROUP BY 1)
SELECT CASE WHEN total < 10000 THEN 1 WHEN total < 50000 THEN 2 WHEN total < 200000 THEN 3 ELSE 4 END AS size_order,
  round(100.0 * sum(population_male) FILTER (WHERE age_from >= 80) / sum(population_male) FILTER (WHERE age_from >= 60), 1) AS male_80_share,
  round(100.0 * sum(population_female) FILTER (WHERE age_from >= 80) / sum(population_female) FILTER (WHERE age_from >= 60), 1) AS female_80_share
FROM a JOIN t USING (area)
GROUP BY 1
ORDER BY 1
```
