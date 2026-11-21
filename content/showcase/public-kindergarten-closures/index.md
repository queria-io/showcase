---
title: 公立幼稚園は5年で3,101園から2,183園に減り、閉園した公立幼稚園の7割は後継の園が記録されていない
description: 文部科学省の学校コードで2021年5月から2026年5月の園数を比較すると、公立幼稚園は918園（30%）減り、公立の認定こども園は241園の増加にとどまります。公立の幼稚園とこども園が1園もない市区町村は938から984に増えました。
publishedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 幼稚園
  - 認定こども園
  - 子育て
  - 公共施設
datasets:
  - queria/mext
  - queria/soumu
sources:
  - title: 学校コード
    url: https://www.mext.go.jp/b_menu/toukei/mext_01087.html
    publisher: 文部科学省
  - title: 統計に用いる標準地域コード
    url: https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm
    publisher: 総務省統計局
agentHint: 自分の市区町村について、公立の幼稚園と幼保連携型認定こども園の園数を2021年5月と2026年5月で出して、閉園した園の後継コードも見せて
socialAnnounce: |-
  公立幼稚園は2021年5月の3,101園から2026年5月の2,183園へ、5年で30%減りました。

  公立の幼保連携型認定こども園が増えたのは241園です。公立の幼稚園もこども園も1園もない市区町村は、938から984に増えました。
  Queriaは行政のオープンデータを整えて公開しています
---

公立幼稚園は2021年5月の3,101園から2026年5月の2,183園へ、5年で918園（30%）減りました。同じ期間に公立の幼保連携型認定こども園は862園から1,103園へ241園増えただけで、減った園の約4分の1です。私立は幼稚園が553園減り、こども園が1,447園増えたので、私立では幼稚園の減少を上回る数のこども園が増えました。公立では、こども園の増加は幼稚園の減少の約4分の1にとどまります。

市区町村で公立園の再編や統合を計画する担当者は、近隣の自治体が公立園を何園減らしたかを知る必要があります。文部科学省の[学校コード](https://www.mext.go.jp/b_menu/toukei/mext_01087.html)は、全国の幼稚園と幼保連携型認定こども園に付いた学校コード、設置区分、所在地、廃止年月日、廃止後の後継コードを毎年の一覧にまとめています。2021年5月から2026年5月までの6時点の一覧を比較し、所在地の住所を[標準地域コード](https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm)の市区町村名と突き合わせて、市区町村ごとの園数を集計しました。

学校コードに載る認定こども園は幼保連携型だけです。幼稚園型の認定こども園は幼稚園として載り、保育所型は載りません。園の数であり、園児の数ではありません。設置区分は公立と私立の2つに絞り、国立は除いています。2021年の時点だけ基準日が5月27日で、2022年以降は5月1日です。

## 公立幼稚園は5年で30%減り、私立のこども園が1,447園増えた

使ったのは文部科学省の学校コード（`mext.school_codes.schools`）です。1行が1つの学校コードで、学校種（`school_type_code`、A1は幼稚園、A2は幼保連携型認定こども園）、設置区分（`establishment`、公立は `public`、私立は `private`）、設定年月日（`valid_from`）、廃止年月日（`valid_to`）を持ちます。ある時点に開いている園は、設定年月日がその時点以前で、廃止年月日が空かその時点より後の学校コードです。

```chart
{
  "data": { "name": "trend" },
  "mark": { "type": "line", "point": true },
  "encoding": {
    "x": { "field": "year", "type": "ordinal", "title": "年（各年5月時点）" },
    "y": { "field": "n", "type": "quantitative", "title": "園数" },
    "color": { "field": "kind", "type": "nominal", "title": null },
    "tooltip": [{ "field": "kind" }, { "field": "year" }, { "field": "n", "format": "," }]
  }
}
```

| 区分         | 2021年5月 | 2026年5月 | 増減   |
| ------------ | --------- | --------- | ------ |
| 公立幼稚園   | 3,101     | 2,183     | −918   |
| 私立幼稚園   | 6,267     | 5,714     | −553   |
| 公立こども園 | 862       | 1,103     | +241   |
| 私立こども園 | 5,407     | 6,854     | +1,447 |

私立では、幼稚園の減少553園に対してこども園が1,447園増えています。公立は幼稚園の減少918園に対してこども園の増加が241園で、公立の園の総数は3,963園から3,286園に減りました。

## 閉園した公立幼稚園の69%は、後継の学校コードが記録されていない

学校コードには、廃止された学校について引き継ぐ後継の学校コードが記録されます。2021年5月より後に廃止された幼稚園（期間中に新設されて廃止された園を含みます）を、後継の種類で分けました。公立は938園で、前節の純減918園との差は、同じ期間に新設された園の分です。

```chart
{
  "data": { "name": "successor" },
  "mark": "bar",
  "encoding": {
    "y": { "field": "establishment", "type": "nominal", "title": null },
    "x": { "field": "n", "type": "quantitative", "stack": "normalize", "title": "廃止された幼稚園の割合", "axis": { "format": "%" } },
    "color": { "field": "successor", "type": "nominal", "title": null, "sort": ["こども園が引き継ぐ", "幼稚園が引き継ぐ", "後継の記録なし"] },
    "tooltip": [{ "field": "establishment" }, { "field": "successor" }, { "field": "n", "format": "," }]
  }
}
```

公立は938園が廃止され、こども園が引き継いだのは218園（23%）、別の幼稚園が引き継いだのは71園（8%）、後継の記録がないのは649園（69%）です。私立は583園のうち、こども園が引き継いだのが219園（38%）、後継の記録がないのが354園（61%）です。後継の記録が無いことは、引き継ぐ園が無かったことを意味するとは限りません。学校コードの上で、廃止された園と後継の園が結び付けられていない園を数えています。

## 公立の幼稚園もこども園も1園もない市区町村が、938から984に増えた

学校の住所を市区町村名と突き合わせ、2021年5月と2026年5月で、公立の幼稚園とこども園の合計園数が市区町村ごとにどう変わったかを分類しました。市区町村は、政令指定都市を市単位とし、東京23区を区単位とした1,747です。地図では政令指定都市の市の値を区に同じ色で配っています。住所を市区町村名と突き合わせられなかった公立園は、2021年5月で11園（0.3%）です。

```map
type: map
caption: 公立の幼稚園・こども園の園数の変化（2021年5月→2026年5月、市区町村別）
layers:
  - from: muni_map
    area: city
    code: mcode
    color: change
    label: label
    name: 公立園の変化
lng: 137.5
lat: 37.5
zoom: 4.3
```

分類ごとの市区町村数は次のとおりです。

```sql
SELECT change AS 分類, count(*) AS 市区町村数 FROM muni_stat GROUP BY change ORDER BY 2 DESC
```

公立幼稚園を持つ市区町村は670から540に減り、130市区町村が公立幼稚園を全廃しました。そのうち57市区町村は公立のこども園もありません。公立の幼稚園とこども園が合わせて0園になった市区町村は、公立こども園だけを持っていた市区町村を含めて62です。公立の幼稚園もこども園も1園もない市区町村は、2021年5月の938から2026年5月の984に増えました。

## 公立幼稚園の減少率は都道府県で大きく異なる

2021年5月に公立幼稚園が10園以上あった39都道府県で、2026年5月までの公立幼稚園の減少率を比較しました。10園未満の県は、1園の閉園で減少率が大きく動くため除いています。

```chart
{
  "data": { "name": "pref_rank" },
  "mark": "bar",
  "height": 1100,
  "encoding": {
    "y": { "field": "pref", "type": "nominal", "sort": "-x", "title": null },
    "x": { "field": "rate", "type": "quantitative", "title": "公立幼稚園の減少率（%）" },
    "color": { "field": "grp", "type": "nominal", "title": null, "scale": { "domain": ["上位10", "中間", "下位10"], "range": ["#3182bd", "#9ecae1", "#94a3b8"] } },
    "tooltip": [{ "field": "pref" }, { "field": "k21", "title": "2021年5月" }, { "field": "k26", "title": "2026年5月" }, { "field": "rate", "format": ".1f" }]
  }
}
```

減少率が最も高いのは富山県の62.5%（16園から6園）で、新潟県の59.3%（27園から11園）、岩手県の51.6%（31園から15園）、岐阜県の50.8%、福岡県の50.0%が続きます。最も低いのは広島県の11.6%（69園から61園）で、東京都の12.3%、愛知県の17.9%、静岡県の19.8%、山形県の20.0%が下位です。

## 自分の市区町村を、近隣の市区町村と比較する

- 公立園の再編を担当する自治体の職員は、地図とその下の分類で、近隣の市区町村で、公立園が増えたか、減ったか、公立幼稚園が0園になったかを確認できます。市区町村ごとの後継の内訳は、記事の `agentHint` の問いで調べられます
- 公立園の再編計画に、閉園した公立幼稚園の後継（こども園・別の幼稚園・記録なし）の内訳を添えるときは、全国の公立幼稚園で69%が記録なしという数字を比較の基準にできます
- 私立園の経営者は、2021年5月には公立の幼稚園かこども園があり、2026年5月に0園になった62市区町村を、公立園の閉園で受け入れ先が変わった地域として把握できます。園児がどこへ移ったかは、このデータでは分かりません

## データの出典

本記事は文部科学省の[学校コード](https://www.mext.go.jp/b_menu/toukei/mext_01087.html)の2021年5月から2026年5月の一覧を2026-11-21時点で集計しています。市区町村の突き合わせには総務省の[標準地域コード](https://www.soumu.go.jp/toukei_toukatsu/index/seido/9-5.htm)を使いました。

行政データの整備に時間を取られず、地域ごとの園の増減を判断の材料にできます。Queriaは学校コードの列名・単位を揃えて公開しているので、[学校コードのテーブル](/datasets/queria/mext/school_codes/schools)から自分の市区町村の園を確認できます。

```sql id=sch
WITH m AS (
  SELECT COALESCE(municipality_code, area_code) AS mcode,
         pref_name || COALESCE(county_name, '') || municipality_name AS k1,
         pref_name || COALESCE(designated_city_name, '') || municipality_name AS k2
  FROM soumu.code.municipality WHERE area_kind IN ('municipality', 'ward')
), keys AS (
  SELECT mcode, k1 AS k FROM m
  UNION SELECT mcode, k2 FROM m
  UNION SELECT area_code, pref_name || designated_city_name FROM soumu.code.municipality WHERE area_kind = 'designated_city'
)
SELECT s.school_code, s.school_type_code, s.establishment, s.valid_from, s.valid_to, s.successor_school_codes, keys.mcode
FROM mext.school_codes.schools s JOIN keys ON starts_with(regexp_replace(s.address, '^北海道[^市町村郡]{1,4}郡', '北海道'), keys.k)
WHERE s.school_type_code IN ('A1', 'A2') AND s.establishment IN ('public', 'private')
QUALIFY row_number() OVER (PARTITION BY s.school_code ORDER BY length(keys.k) DESC) = 1
```

```sql id=trend
WITH d AS (SELECT unnest([DATE '2021-05-27', DATE '2022-05-01', DATE '2023-05-01', DATE '2024-05-01', DATE '2025-05-01', DATE '2026-05-01']) AS snap)
SELECT year(snap) AS year,
  CASE establishment WHEN 'public' THEN '公立' ELSE '私立' END || CASE school_type_code WHEN 'A1' THEN '幼稚園' ELSE 'こども園' END AS kind,
  count(*) AS n
FROM d JOIN mext.school_codes.schools s ON s.valid_from <= snap AND (s.valid_to IS NULL OR s.valid_to > snap)
WHERE school_type_code IN ('A1', 'A2') AND establishment IN ('public', 'private')
GROUP BY ALL ORDER BY year, kind
```

```sql id=successor
SELECT CASE s.establishment WHEN 'public' THEN '公立' ELSE '私立' END AS establishment,
  CASE WHEN EXISTS (SELECT 1 FROM mext.school_codes.schools b WHERE list_contains(s.successor_school_codes, b.school_code) AND b.school_type_code = 'A2') THEN 'こども園が引き継ぐ'
       WHEN EXISTS (SELECT 1 FROM mext.school_codes.schools b WHERE list_contains(s.successor_school_codes, b.school_code) AND b.school_type_code = 'A1') THEN '幼稚園が引き継ぐ'
       ELSE '後継の記録なし' END AS successor,
  count(*) AS n
FROM mext.school_codes.schools s
WHERE s.school_type_code = 'A1' AND s.establishment IN ('public', 'private') AND s.valid_to > DATE '2021-05-27'
GROUP BY ALL ORDER BY 1, 2
```

```sql id=muni_stat
WITH muni AS (
  SELECT area_code AS mcode, pref_name || COALESCE(designated_city_name, '') || COALESCE(county_name, '') || municipality_name AS label
  FROM soumu.code.municipality WHERE is_municipality AND area_kind IN ('municipality', 'designated_city')
), agg AS (
  SELECT mu.mcode, mu.label,
    count(sch.school_code) FILTER (WHERE sch.establishment = 'public' AND sch.valid_from <= DATE '2021-05-27' AND (sch.valid_to IS NULL OR sch.valid_to > DATE '2021-05-27')) AS pub21,
    count(sch.school_code) FILTER (WHERE sch.establishment = 'public' AND sch.valid_from <= DATE '2026-05-01' AND (sch.valid_to IS NULL OR sch.valid_to > DATE '2026-05-01')) AS pub26,
    count(sch.school_code) FILTER (WHERE sch.establishment = 'public' AND sch.school_type_code = 'A1' AND sch.valid_from <= DATE '2021-05-27' AND (sch.valid_to IS NULL OR sch.valid_to > DATE '2021-05-27')) AS k21,
    count(sch.school_code) FILTER (WHERE sch.establishment = 'public' AND sch.school_type_code = 'A1' AND sch.valid_from <= DATE '2026-05-01' AND (sch.valid_to IS NULL OR sch.valid_to > DATE '2026-05-01')) AS k26
  FROM muni mu LEFT JOIN sch ON sch.mcode = mu.mcode GROUP BY 1, 2
)
SELECT mcode, label || '（公立 ' || pub21 || '園→' || pub26 || '園）' AS label, pub21, pub26, k21, k26,
  CASE WHEN pub21 > 0 AND pub26 = 0 THEN '公立の幼稚園・こども園が0園に'
       WHEN k21 > 0 AND k26 = 0 THEN '公立幼稚園が0園に'
       WHEN pub26 < pub21 THEN '公立園が減った'
       WHEN pub26 > pub21 THEN '公立園が増えた'
       WHEN pub26 = 0 THEN '公立園なし（変化なし）'
       ELSE '園数は変わらない' END AS change
FROM agg
```

```sql id=pref_rank
WITH r AS (
  SELECT m.pref_name AS pref, sum(k21) AS k21, sum(k26) AS k26, 100.0 * (sum(k21) - sum(k26)) / sum(k21) AS rate
  FROM muni_stat x JOIN soumu.code.municipality m ON m.area_code = x.mcode
  GROUP BY 1 HAVING sum(k21) >= 10
), ranked AS (SELECT *, ROW_NUMBER() OVER (ORDER BY rate DESC, pref) AS rn, count(*) OVER () AS cnt FROM r)
SELECT pref, k21, k26, rate,
  CASE WHEN rn <= 10 THEN '上位10' WHEN rn > cnt - 10 THEN '下位10' ELSE '中間' END AS grp
FROM ranked ORDER BY rn
```

```sql id=muni_map
-- 政令指定都市は区の境界で描くため、市の値を区に配る。集計には使わない
SELECT w.area_code AS mcode, s.label, s.pub21, s.pub26, s.k21, s.k26, s.change
FROM muni_stat s JOIN soumu.code.municipality w ON w.municipality_code = s.mcode AND w.area_kind = 'ward'
UNION ALL
SELECT mcode, label, pub21, pub26, k21, k26, change FROM muni_stat WHERE mcode NOT IN (SELECT municipality_code FROM soumu.code.municipality WHERE area_kind = 'ward')
```
