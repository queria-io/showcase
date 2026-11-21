---
title: 2050年までに高齢者が最も増えるのは横浜市で、23.9万人増
description: 市区町村別の将来推計人口で、2025年から2050年の65歳以上人口の増減を集計しました。増加が最も大きいのは横浜市の23.9万人で、川崎市・福岡市・名古屋市が続きます。2025年の高齢化率が40%以上の273市区町村では、すべてで高齢者が減ります
publishedAt: 2026-06-30
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口
  - 高齢化
  - 出店
  - 商圏分析
datasets:
  - queria/nlftp
  - queria/soumu
sources:
  - title: 国土数値情報 1kmメッシュ別将来推計人口（令和6年国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html
    publisher: 国土交通省
  - title: 日本の地域別将来推計人口（令和5年推計）
    url: https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp
    publisher: 国立社会保障・人口問題研究所
  - title: 統計に用いる標準地域コード
    url: https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm
    publisher: 総務省
agentHint: nlftp.population.future_population_municipality を soumu.code.municipality の municipality_code で市単位に畳んで、2025→2050年の高齢者実数（population×elderly_ratio）の増加分の上位30自治体を出して。そのうち首都圏1都3県の外にある市がいくつあるかも数えて
socialAnnounce: |-
  将来推計人口で、高齢者の実数がどこで伸びるかを読み解きました。

  増分が集中するのは横浜・川崎・福岡・名古屋で、首都圏だけではありません。
  介護・ヘルスケアのエリア戦略に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

将来推計人口で2025年から2050年の65歳以上人口の増減を集計すると、全国では6.4%増え、増加が最も大きい自治体は横浜市の23.9万人でした。川崎市（14.4万人）、福岡市（12.2万人）、名古屋市（11.6万人）が続き、上位15の増加分の44%は首都圏1都3県の外にある7市です。2025年の高齢化率が40%以上の273市区町村では、すべてで2050年までに高齢者の人数が減ります。

介護施設、配食サービス、見守り、シニア向け住宅といった高齢者向けサービスの出店・撤退では、需要がどこにあり、これから増えるかを判断する必要があります。サービスの市場規模は、高齢化率（高齢者が人口に占める割合）より、高齢者の人数で決まります。この記事では、国土数値情報の将来推計人口（市区町村別）を使い、2025年から2050年に高齢者の人数がどの地域で増え、どの地域で減るかを集計します。

## データの概要

使用するのは国土交通省の[国土数値情報「1kmメッシュ別将来推計人口（令和6年国政局推計）」](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を市区町村単位に集計した[将来推計人口（市区町村別）テーブル](/datasets/queria/nlftp/population/future_population_municipality)です。推計値は令和2年国勢調査と国立社会保障・人口問題研究所の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)に基づいており、総人口は2020年から2070年まで5年ごと、高齢化率は2025年と2050年の2時点を収録しています。政令指定都市は、市ではなく行政区の単位で入っています。主な列は次のとおりです。

| 列                                          | 内容                                |
| ------------------------------------------- | ----------------------------------- |
| `population_2025` / `population_2050`       | 2025年・2050年の総人口（人）        |
| `elderly_ratio_2025` / `elderly_ratio_2050` | 65歳以上人口の割合（%）             |
| `growth_rate_2025_2050`                     | 2025年から2050年の総人口増減率（%） |

このテーブルには65歳以上人口の実数が入っていないので、本記事の「高齢者人口」は総人口に高齢化率を掛けて求めています。高齢化率は小数第1位までの値なので、求めた人数には丸めの誤差が含まれ、1人単位の比較には使えません。全国の合計で、総人口と高齢者人口の増減を集計しました。

```sql
SELECT * FROM national
```

全国の総人口は2025年から2050年にかけて15.1%減り、高齢者人口は6.4%増えます。高齢者の増加は地域によって大きく異なります。

## 2050年の高齢者人口は東京都が425.8万人で最も多い

2050年時点の高齢者人口を都道府県別に地図にしました。色が濃いほど高齢者の人数が多い地域です。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: value
    label: pref_name
    name: "高齢者人口<br>2050年（万人）"
lng: 137
lat: 36.5
zoom: 4
```

高齢者人口が最も多いのは東京都で、2050年には425.8万人に達します。神奈川・大阪・埼玉・愛知・千葉といった大都市圏の府県が続きます。高齢化率が高い地方の県は、色が薄く、高齢者の人数は少なくなっています。

## 高齢者人口は東京都で31.6%増え、秋田県で21.4%減る

2025年から2050年の高齢者人口の増減率を都道府県別に並べました。47都道府県を、増減率の上位10・中間・下位10の3つに色分けしています。値は令和2年国勢調査時点の人口構成と移動の傾向をもとにした推計で、大規模な再開発や施設の立地による転入は含まれていません。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者人口の増減率 2025→2050（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者人口の増減率 2025→2050（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者人口の増減率 2025→2050（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

高齢者の人数が最も増えるのは東京都で、2025年比31.6%増です。沖縄県（29.0%増）、神奈川県（22.5%増）、愛知県（18.3%増）が続き、埼玉・千葉・大阪といった大都市圏の府県も上位に入っています。下位には秋田県（21.4%減）、高知県（14.8%減）、山口県（14.2%減）、長崎県（13.9%減）など、すでに高齢化が進んだ地方の県が入っています。これらの県では高齢者の人数も減り、高齢者向けサービスの市場は縮小すると考えられます。

## 高齢化率が高い市区町村ほど、高齢者の人数は減る（相関係数−0.96）

人口1万人以上の1,334市区町村について、横軸に2025年の高齢化率、縦軸に2025年から2050年の高齢者実数の増減率をとって散布図にしました。人口1万人未満の市区町村は、高齢者が数十人増減するだけで増減率が大きく変わるので除いています。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#7c3aed", "opacity": 0.4, "filled": true, "size": 25},
      "encoding": {
        "tooltip": [
          {"field": "ratio25", "type": "quantitative"},
          {"field": "chg", "type": "quantitative"}
        ],
        "x": {
          "field": "ratio25",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率 2025年（%）", "grid": true}
        },
        "y": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢者人口の増減率 2025→2050（%）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 10, "type": "quantitative"},
        "x2": {"datum": 60, "type": "quantitative"},
        "y": {"datum": 0, "type": "quantitative"}
      }
    }
  ]
}
```

相関係数は−0.96で、点はほぼ一直線に並びます。1,334市区町村のうち2025年の高齢化率が40%以上のものは273あり、その273すべてで2050年までに高齢者の人数が減ります。30%未満の446市区町村では、443で高齢者が増えます。高齢化率は、すでにどれだけ高齢化したかを示す指標です。高齢化率の高さを根拠に出店地域を選ぶと、高齢者の人数が減っていく地域を選ぶことになります。

## 高齢者の増加は横浜市の23.9万人が最も多く、上位15の44%は首都圏の外の7市

高齢者人口の増加が大きい自治体を集計しました。このテーブルは政令指定都市を行政区の単位で収録しているので、そのままでは1つの市が複数の区に分かれ、東京23区の各区と同じ単位で比較できません。e-Statの[市区町村マスタ](/datasets/queria/e_stat/code/municipality)の `municipality_code` で行政区を市にまとめてから、2025年から2050年の増加分の上位15を並べました。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "top_inc"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [{"field": "inc", "type": "quantitative"}, {"field": "name", "type": "nominal"}],
        "x": {
          "field": "inc",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "高齢者人口の増加分 2025→2050（万人）", "grid": true}
        },
        "y": {
          "field": "name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    }
  ]
}
```

増分が最も大きいのは横浜市で、25年間で23.9万人の高齢者が増えます。川崎市（14.4万人）、福岡市（12.2万人）、名古屋市（11.6万人）、さいたま市（11.0万人）、札幌市（10.8万人）、大阪市（10.2万人）が続き、東京23区で最大の世田谷区（9.2万人）は8番目です。横浜市の増分は世田谷区の2.6倍にあたります。上位15の増加分は合計143.0万人で、そのうち首都圏1都3県の外にある7市が63.1万人、44%を占めます。福岡市・名古屋市・札幌市・大阪市の4市は、いずれも世田谷区を上回ります。

## データの活用

将来推計人口を高齢者の人数で集計すると、高齢者向けサービスのエリア戦略に次のように使えます。

- 首都圏の外も候補に入れる: 増加分の上位15のうち7市は首都圏1都3県の外にあり、福岡・名古屋・札幌・大阪は東京23区で最大の世田谷区を上回る
- 撤退・縮小の時期を数字で決める: 高齢者の人数が減る県は27あり、最も減る秋田県は21.4%減る。長期の投資回収を見込む事業では、この減少を計画に含める
- 自社サービスの価格帯と比較する: 推計人口を所得や住宅の統計と市区町村コードで結合すると、人数だけでなく支払い能力も含めて商圏を評価できる

## データの出典

本記事は国土交通省の[国土数値情報「1kmメッシュ別将来推計人口（令和6年国政局推計）」](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を市区町村単位に集計した[将来推計人口（市区町村別）](/datasets/queria/nlftp/population/future_population_municipality)を、2026年8月20日時点で集計しています。推計値の基礎は令和2年国勢調査と、国立社会保障・人口問題研究所の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)です。政令指定都市の行政区を市単位にまとめる対応は、総務省の[統計に用いる標準地域コード](https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm)から作った[市区町村マスタ](/datasets/queria/e_stat/code/municipality)を使いました。

Queriaは、国土数値情報の将来推計人口を、列名・単位・文字コードと地域コードの体系を統一し、テーブルと列の説明を付けて公開しています。本記事のように[将来推計人口テーブル](/datasets/queria/nlftp/population/future_population_municipality)と[市区町村マスタ](/datasets/queria/e_stat/code/municipality)を結合して、対象エリアの高齢者人口の増減を集計できます。

```sql id=national
SELECT '総人口' AS "区分", ROUND(SUM(population_2025) / 10000) AS "2025年（万人）", ROUND(SUM(population_2050) / 10000) AS "2050年（万人）", ROUND(SUM(population_2050) / SUM(population_2025) * 100 - 100, 1) AS "増減率（%）" FROM nlftp.population.future_population_municipality UNION ALL SELECT '高齢者人口（65歳以上）', ROUND(SUM(population_2025 * elderly_ratio_2025 / 100.0) / 10000), ROUND(SUM(population_2050 * elderly_ratio_2050 / 100.0) / 10000), ROUND(SUM(population_2050 * elderly_ratio_2050 / 100.0) / SUM(population_2025 * elderly_ratio_2025 / 100.0) * 100 - 100, 1) FROM nlftp.population.future_population_municipality
```

```sql id=map_data
WITH agg AS (SELECT prefecture_code AS pcode, SUM(population_2050 * elderly_ratio_2050 / 100.0) AS s50 FROM nlftp.population.future_population_municipality GROUP BY 1) SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, ROUND(agg.s50 / 10000, 1) AS value, ROW_NUMBER() OVER (ORDER BY p.prefecture_name) - 1 AS row_id FROM agg JOIN nlftp.boundary.prefecture p ON agg.pcode = p.prefecture_code
```

```sql id=rank_top
WITH p AS (SELECT prefecture_code AS c, prefecture_name AS pn, population_2025 * elderly_ratio_2025 / 100.0 AS e25, population_2050 * elderly_ratio_2050 / 100.0 AS e50 FROM nlftp.population.future_population_municipality), agg AS (SELECT c, MAX(pn) AS area_name, SUM(e50) / SUM(e25) * 100 - 100 AS chg FROM p GROUP BY c), ranked AS (SELECT area_name, ROUND(chg, 1) AS chg, ROW_NUMBER() OVER (ORDER BY chg DESC, area_name) AS rn FROM agg) SELECT area_name, chg FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH p AS (SELECT prefecture_code AS c, prefecture_name AS pn, population_2025 * elderly_ratio_2025 / 100.0 AS e25, population_2050 * elderly_ratio_2050 / 100.0 AS e50 FROM nlftp.population.future_population_municipality), agg AS (SELECT c, MAX(pn) AS area_name, SUM(e50) / SUM(e25) * 100 - 100 AS chg FROM p GROUP BY c), ranked AS (SELECT area_name, ROUND(chg, 1) AS chg, ROW_NUMBER() OVER (ORDER BY chg DESC, area_name) AS rn FROM agg) SELECT area_name, chg FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH p AS (SELECT prefecture_code AS c, prefecture_name AS pn, population_2025 * elderly_ratio_2025 / 100.0 AS e25, population_2050 * elderly_ratio_2050 / 100.0 AS e50 FROM nlftp.population.future_population_municipality), agg AS (SELECT c, MAX(pn) AS area_name, SUM(e50) / SUM(e25) * 100 - 100 AS chg FROM p GROUP BY c), ranked AS (SELECT area_name, ROUND(chg, 1) AS chg, ROW_NUMBER() OVER (ORDER BY chg DESC, area_name) AS rn FROM agg) SELECT area_name, chg FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=scatter
SELECT ROUND(elderly_ratio_2025, 1) AS ratio25, ROUND((population_2050 * elderly_ratio_2050) / NULLIF(population_2025 * elderly_ratio_2025, 0) * 100 - 100, 1) AS chg FROM nlftp.population.future_population_municipality WHERE population_2025 >= 10000
```

```sql id=top_inc
WITH base AS (SELECT COALESCE(m.municipality_code, f.city_code) AS mcode, f.population_2050 * f.elderly_ratio_2050 / 100.0 - f.population_2025 * f.elderly_ratio_2025 / 100.0 AS d FROM nlftp.population.future_population_municipality f LEFT JOIN soumu.code.municipality m ON m.area_code = f.city_code), agg AS (SELECT mcode, ROUND(SUM(d) / 10000, 1) AS inc FROM base GROUP BY 1), named AS (SELECT n.pref_name || ' ' || COALESCE(n.municipality_name, n.designated_city_name) AS name, agg.inc FROM agg JOIN soumu.code.municipality n ON n.area_code = agg.mcode AND n.is_municipality), ranked AS (SELECT name, inc, ROW_NUMBER() OVER (ORDER BY inc DESC, name) AS rn FROM named) SELECT name, inc FROM ranked WHERE rn <= 15 ORDER BY rn DESC
```
