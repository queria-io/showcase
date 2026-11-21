---
title: 住む人が100人未満で1,000人以上が働く1km区画の45.7%は、ベッドタウンとされる市区町村にある
description: 従業者が1,000人以上で夜間人口が100人未満の1kmメッシュを全国で集計しました。市区町村を特定できた451か所のうち206か所（45.7%）は、昼夜間人口比率が100を下回る市区町村の中にあります。
publishedAt: 2026-08-03
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - メッシュ統計
  - 立地
  - 昼夜間人口
datasets:
  - queria/e_stat
  - queria/nlftp
  - queria/soumu
sources:
  - title: 令和2年国勢調査に関する地域メッシュ統計
    url: https://www.stat.go.jp/data/mesh/index.html
    publisher: 総務省統計局
  - title: 平成28年経済センサス-活動調査
    url: https://www.stat.go.jp/data/e-census/2016/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 統計に用いる標準地域コード
    url: https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm
    publisher: 総務省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 従業者が1,000人以上で夜間人口が100人未満の1kmメッシュを、自分の県の市区町村別に数えて。従業者数の合計と事業所数、1事業所あたりの従業者数も出して
socialAnnounce: |-
  働く人は1,000人超、住む人は100人未満。そんな1km四方の区画を全国で数えました。

  その45.7%は、通勤者を送り出す側としてベッドタウン扱いされる市区町村の中にあります。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

従業者が1,000人以上いて、住んでいる人が100人未満の1kmメッシュは全国に521か所あります。市区町村を特定できた451か所のうち206か所（45.7%）は、昼夜間人口比率が100を下回る、通勤者を送り出す側の111市区町村の中にありました。最も多い東京都大田区（昼夜間人口比率96.5）では、11か所のメッシュで合計66,098人が働いています。

出店候補地を市区町村ごとの数字で絞り込むときは、昼夜間人口比率がよく使われます。その市区町村に通勤・通学で入ってくる人と出ていく人を差し引きした指標で、100を超えれば人を集める側、下回れば人を送り出す側です。100を下回る自治体を「ベッドタウン」として候補から外す、という使い方をします。この比率は市区町村全体の平均なので、住む人がほとんどいない区画で数千人が働いていても、周りの住宅地と平均されて数字には表れません。この記事では1kmメッシュの統計を使い、比率が100を下回る自治体の中にある、働く人が集まる区画を集計します。比率が100未満の自治体がすべて大都市の住宅地というわけではありませんが、以下では、この比率で候補地を絞り込むときの呼び方として「ベッドタウン」を使います。

## 昼夜間人口比率が100未満でも、従業者5,000人以上のメッシュを持つ市区町村が139ある

[地域メッシュ統計](https://www.stat.go.jp/data/mesh/index.html)は、日本全国を緯度・経度で区切った1kmの正方形ごとに統計値を集計したもので、市区町村の境界と関係なく地域を比較できます。メッシュを識別するコード（`mesh_code`）は8桁で、上位4桁が約80km四方の第1次メッシュ、次の2桁がそれを64分割した約10km四方、最後の2桁がさらに100分割した約1km四方を表します。上位の桁が同じメッシュは地理的に隣り合うので、コードの前方一致で広い範囲を切り出せます。

使う列は3つです。`nighttime_population` は令和2年（2020年）国勢調査の夜間人口で、そのメッシュに住んでいる人の数です。`employees` と `establishments` は平成28年（2016年）経済センサス‐活動調査の従業者数と事業所数です。住む人と働く人は別の調査なので、調査時点が4年ずれています。従業者数は日本標準産業分類のA〜Rが対象で、S（公務）を含まないので、官公庁が集まる区画では従業者数が小さくなります。

全国で人口または事業所が記録されている1kmメッシュは184,209か所あります。横軸に市区町村の昼夜間人口比率（`A6108`、2020年）、縦軸にその市区町村の中で最も従業者が多い1kmメッシュの従業者数を取り、1,739市区町村を並べました。政令指定都市の昼夜間人口比率は、行政区ごとではなく市全体の値です。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "low"},
      "mark": {"type": "point", "opacity": 0.55, "filled": true, "size": 25},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "ratio", "type": "quantitative"},
          {"field": "max_emp", "type": "quantitative"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "市区町村の昼夜間人口比率", "grid": true}
        },
        "y": {
          "field": "max_emp",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "市区町村内で最大の1kmメッシュ従業者数（人）", "grid": true}
        },
        "color": {
          "datum": "昼夜間人口比率が100未満",
          "type": "nominal",
          "scale": {"domain": ["昼夜間人口比率が100未満", "100以上"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "high"},
      "mark": {"type": "point", "opacity": 0.55, "filled": true, "size": 25},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "ratio", "type": "quantitative"},
          {"field": "max_emp", "type": "quantitative"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "市区町村の昼夜間人口比率", "grid": true}
        },
        "y": {
          "field": "max_emp",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "市区町村内で最大の1kmメッシュ従業者数（人）", "grid": true}
        },
        "color": {
          "datum": "100以上",
          "type": "nominal",
          "scale": {"domain": ["昼夜間人口比率が100未満", "100以上"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

比率が高い自治体ほど大きなメッシュを持つ傾向はありますが、関係は弱く、両対数で描いたこの図の上での相関係数は0.13です。最大メッシュ従業者数の中央値は、比率100未満の自治体で1,365人、100以上の自治体で1,739人で、差は1.3倍ほどです。元の値のまま計算すると相関係数は0.51になりますが、これは比率も従業者数も極端に大きい東京都中央区（232,159人）や千代田区（195,253人）などの数自治体の影響です。

1,739市区町村のうち1,147は比率100未満で、そのうち139市区町村には従業者が5,000人以上の1kmメッシュがあります。図の左側で青い点が縦に広く分布しているのは、これらの市区町村です。

## 働く人だけの区画の上位は、比率が90台の市区町村に集まっている

「従業者が1,000人以上で、夜間人口が100人未満」の1kmメッシュを集計します。1平方キロメートルに1,000人以上が働きに来ていて、住んでいる人はほとんどいない区画です。従業者が1,000人以上のメッシュは全国に12,627か所あり、そのうち521か所（4.1%）が条件に当てはまります。

メッシュにはそれぞれ1つの市区町村コードが割り当てられていて、市区町村の境界をまたぐメッシュもどちらか一方の市区町村に入ります。コードが付いていないメッシュ（海上など）や、行政区の再編で現在のコード一覧にないメッシュは除き、市区町村を特定できた451か所を対象にしました。451か所は238市区町村にあり、そのうち206か所（45.7%）は、昼夜間人口比率が100を下回る111市区町村の中にあります。

比率100未満の市区町村について、該当メッシュの従業者数を合計し、上位15市区町村を並べました。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "bedtown"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "emp", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "emp",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "該当メッシュの従業者数の合計（人）", "grid": true}
        },
        "y": {
          "field": "area_name",
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

最も多いのは東京都大田区で、11か所のメッシュに合計66,098人が働いています。大田区の昼夜間人口比率は96.5で、区全体では通勤者を送り出す側です。千葉県浦安市が3か所で33,026人（比率96.0）、神奈川県横浜市が11か所で30,577人（比率92.5）と続きます。埼玉県狭山市は該当メッシュが1か所だけですが、そこに15,328人が働いていて（比率95.1）、1か所で上位に入っています。

上位15市区町村の昼夜間人口比率は、最も低い船橋市の84.4から福山市の99.8までで、15のうち13が90以上です。通勤者を大きく送り出している自治体ではなく、比率が100をわずかに下回る自治体にこれらの区画があります。比率が100に近い自治体は、人を集める側とも送り出す側とも判断されにくく、候補地の検討で見落としやすいと考えられます。

## 1事業所あたりの従業者数は、同じ大田区の中でも10倍近く違う

上位の区画には、夜間人口が0人のメッシュが並びます。大田区のメッシュ`53392652`は住む人0人に対して31,058人が働いていて、浦安市の`53393750`も0人に対して26,663人です。

働く人だけの区画でも、少数の大きな事業所が占めている区画と、小さな事業所が集まっている区画があります。昼夜間人口比率が100未満の市区町村にある該当メッシュを、従業者数の多い順に10件並べ、事業所数と1事業所あたりの従業者数を求めました。

```sql
WITH c AS (SELECT area_code, pref_name || ' ' || COALESCE(NULLIF(designated_city_name, ''), municipality_name) AS area_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), r AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year = 2020 GROUP BY area_name) SELECT m.mesh_code AS 'メッシュコード', c.area_name AS '市区町村', r.ratio AS '昼夜間人口比率', m.nighttime_population AS '夜間人口(人)', m.employees AS '従業者数(人)', m.establishments AS '事業所数', ROUND(CAST(m.employees AS DOUBLE) / m.establishments, 0) AS '1事業所あたり(人)' FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code JOIN r ON c.area_name = r.area_name WHERE m.employees >= 1000 AND m.nighttime_population < 100 AND r.ratio < 100 ORDER BY m.employees DESC LIMIT 10
```

1事業所あたりの従業者数は、浦安市のメッシュで321人、埼玉県狭山市で189人、千葉県君津市で175人です。大田区の中でも、メッシュ`53392652`は185事業所で1事業所あたり168人、`53392690`は339事業所で17人と、10倍近い差があります。

1事業所あたりの従業者数が多い区画では、働く人の多くが少数の事業所に勤めています。1つの事業所の移転や生産調整で従業者数が大きく変わり、需要の変動も大きくなりやすいと考えられます。1事業所あたりの従業者数が少ない区画では、個々の事業所が入れ替わっても従業者数の合計は急には変わりにくいと考えられます。従業者数だけで候補地を評価すると、この違いは分かりません。

## 該当メッシュが最も多いのは愛知県の43か所で、東京都は18か所

該当メッシュ451か所を都道府県別に集計しました。色が濃いほど該当メッシュが多い都道府県です。

```map
type: map
layers:
  - from: pref_map
    geojson: geojson
    color: n
    label: pref_name
    name: "該当メッシュ数"
lng: 137
lat: 36.5
zoom: 4
```

最も多いのは愛知県の43か所で、千葉県38か所、北海道30か所、兵庫県28か所、神奈川県27か所と続きます。東京都は18か所で8番目で、京都府・奈良県・高知県は0か所でした。件数は面積や総従業者数で割っていない実数なので、県の広さや経済規模の違いを含みます。従業者数に公務が含まれないので、官庁が集まる都府県では件数が小さくなります。

## 候補地の絞り込みでの使い方

- 昼夜間人口比率で自治体を候補から外す前に、その自治体の中の1kmメッシュの最大従業者数も確認します。比率が100未満でも、従業者5,000人以上のメッシュを持つ自治体が139あります
- 従業者数と事業所数を両方取得し、1事業所あたりの従業者数を求めます。従業者数が同じでも、1事業所あたりの従業者数が多い区画と少ない区画では、需要の変動の大きさが違います
- メッシュコードの上位6桁で約10km四方にまとめると、隣り合う複数の区画をまとめて評価できます。市区町村の境界をまたぐ商圏を扱うときに使えます

## データの出典

本記事は総務省統計局の[地域メッシュ統計](https://www.stat.go.jp/data/mesh/index.html)を2026-08-03時点で集計しています。夜間人口は令和2年国勢調査、従業者数と事業所数は[平成28年経済センサス-活動調査](https://www.stat.go.jp/data/e-census/2016/index.html)によるものです。市区町村の昼夜間人口比率は[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)の`A6108`（2020年）、メッシュの市区町村コードから名称への対応は総務省の[統計に用いる標準地域コード](https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm)、地図の境界は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使いました。

Queriaは、国勢調査・経済センサスのメッシュ統計と市区町村統計、標準地域コード、行政区域の境界を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[昼夜間人口メッシュテーブル](/datasets/e_stat/census/daytime_population_mesh_1km)から、自社の候補地がある市区町村のメッシュを従業者数の順に並べたり、[市区町村別人口テーブル](/datasets/e_stat/ssds/a_municipal_population)の昼夜間人口比率と結合したりできます。

```sql id=counts
SELECT COUNT(*) AS all_mesh, SUM(CASE WHEN employees >= 1000 THEN 1 ELSE 0 END) AS emp1000_mesh, SUM(CASE WHEN employees >= 1000 AND nighttime_population < 100 THEN 1 ELSE 0 END) AS work_only_mesh, ROUND(100.0 * SUM(CASE WHEN employees >= 1000 AND nighttime_population < 100 THEN 1 ELSE 0 END) / SUM(CASE WHEN employees >= 1000 THEN 1 ELSE 0 END), 1) AS work_only_pct FROM e_stat.census.daytime_population_mesh_1km
```

```sql id=scope
WITH c AS (SELECT area_code, pref_name || ' ' || COALESCE(NULLIF(designated_city_name, ''), municipality_name) AS area_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), r AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year = 2020 GROUP BY area_name), w AS (SELECT c.area_name, r.ratio FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code JOIN r ON c.area_name = r.area_name WHERE m.employees >= 1000 AND m.nighttime_population < 100) SELECT COUNT(*) AS matched_mesh, SUM(CASE WHEN ratio < 100 THEN 1 ELSE 0 END) AS in_low_ratio, ROUND(100.0 * SUM(CASE WHEN ratio < 100 THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_in_low, COUNT(DISTINCT area_name) AS munis, COUNT(DISTINCT CASE WHEN ratio < 100 THEN area_name END) AS low_munis FROM w
```

```sql id=muni_stat
WITH c AS (SELECT area_code, pref_name || ' ' || COALESCE(NULLIF(designated_city_name, ''), municipality_name) AS area_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), r AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year = 2020 GROUP BY area_name), mx AS (SELECT c.area_name, MAX(m.employees) AS max_emp FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code GROUP BY 1) SELECT COUNT(*) AS munis, SUM(CASE WHEN r.ratio < 100 THEN 1 ELSE 0 END) AS low_ratio_munis, SUM(CASE WHEN r.ratio < 100 AND mx.max_emp >= 5000 THEN 1 ELSE 0 END) AS low_with_big_mesh, ROUND(CORR(r.ratio, mx.max_emp), 2) AS corr_raw, ROUND(CORR(LN(r.ratio), LN(mx.max_emp)), 2) AS corr_log, ROUND(MEDIAN(CASE WHEN r.ratio < 100 THEN mx.max_emp END), 0) AS med_low, ROUND(MEDIAN(CASE WHEN r.ratio >= 100 THEN mx.max_emp END), 0) AS med_high FROM mx JOIN r ON mx.area_name = r.area_name
```

```sql id=low
WITH c AS (SELECT area_code, pref_name || ' ' || COALESCE(NULLIF(designated_city_name, ''), municipality_name) AS area_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), r AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year = 2020 GROUP BY area_name), mx AS (SELECT c.area_name, MAX(m.employees) AS max_emp FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code GROUP BY 1) SELECT mx.area_name, r.ratio, mx.max_emp FROM mx JOIN r ON mx.area_name = r.area_name WHERE r.ratio < 100 ORDER BY mx.max_emp DESC
```

```sql id=high
WITH c AS (SELECT area_code, pref_name || ' ' || COALESCE(NULLIF(designated_city_name, ''), municipality_name) AS area_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), r AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year = 2020 GROUP BY area_name), mx AS (SELECT c.area_name, MAX(m.employees) AS max_emp FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code GROUP BY 1) SELECT mx.area_name, r.ratio, mx.max_emp FROM mx JOIN r ON mx.area_name = r.area_name WHERE r.ratio >= 100 ORDER BY mx.max_emp DESC
```

```sql id=bedtown
WITH c AS (SELECT area_code, pref_name || ' ' || COALESCE(NULLIF(designated_city_name, ''), municipality_name) AS area_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), r AS (SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS ratio FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A6108' AND year = 2020 GROUP BY area_name), agg AS (SELECT c.area_name, r.ratio, CAST(SUM(m.employees) AS BIGINT) AS emp, COUNT(*) AS meshes FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code JOIN r ON c.area_name = r.area_name WHERE m.employees >= 1000 AND m.nighttime_population < 100 AND r.ratio < 100 GROUP BY 1, 2), ranked AS (SELECT area_name, ratio, emp, meshes, ROW_NUMBER() OVER (ORDER BY emp DESC, area_name) AS rn FROM agg) SELECT area_name, ratio, emp, meshes FROM ranked WHERE rn <= 15 ORDER BY rn DESC
```

```sql id=pref_map
WITH c AS (SELECT area_code, pref_name FROM soumu.code.municipality WHERE area_kind IN ('municipality','ward','designated_city')), w AS (SELECT c.pref_name, COUNT(*) AS n FROM e_stat.census.daytime_population_mesh_1km m JOIN c ON m.city_code = c.area_code WHERE m.employees >= 1000 AND m.nighttime_population < 100 GROUP BY 1) SELECT ST_AsGeoJSON(ST_Simplify(p.geometry, 0.01)) AS geojson, COALESCE(w.n, 0) AS n, p.prefecture_name AS pref_name FROM nlftp.boundary.prefecture p LEFT JOIN w ON p.prefecture_name = w.pref_name
```
