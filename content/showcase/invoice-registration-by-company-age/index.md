---
title: 2024〜2025年に設立された株式会社のインボイス登録率は54%で、2021年から2023年9月に設立された会社の約71%を下回る
description: 法人番号と適格請求書発行事業者の登録を突き合わせると、2024〜2025年設立の株式会社の登録率は54%、2026年1〜3月設立の株式会社は42.5%です。県別では福井県65%から大阪府49%まで開きます。
ogDescription: 2021年から2023年9月に設立された株式会社の登録率は約71%、2024〜2025年設立は54%です。
publishedAt: 2026-11-23
author:
  name: UD
  url: https://udus.dev
tags:
  - インボイス制度
  - 適格請求書発行事業者
  - 法人番号
  - 経理
datasets:
  - queria/invoice_issuers
  - queria/houjin_bangou
sources:
  - title: 適格請求書発行事業者公表サイト
    url: https://www.invoice-kohyo.nta.go.jp/download/
    publisher: 国税庁
  - title: 国税庁法人番号公表サイト
    url: https://www.houjin-bangou.nta.go.jp/download/
    publisher: 国税庁
agentHint: 手元の取引先の法人番号一覧を invoice_issuers.main.issuers と突き合わせて、登録番号のない会社を都道府県別・設立年別に出して。
socialAnnounce: |-
  法人番号とインボイスの登録を突き合わせました。

  2024〜2025年に設立された株式会社の登録率は54%、2021年から2023年9月の設立は約71%。2024年以降の設立では低下が続きます。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2024〜2025年に設立された株式会社のうち、適格請求書発行事業者（インボイスの登録事業者）になっているのは54.0%で、残りの46.0%は登録していません。2021年1月から2023年9月までに設立された株式会社の登録率は69.5%から72.1%で推移しており、2026年1〜3月に設立された株式会社では42.5%まで下がります。登録率は法人の数の割合で、取引額の割合ではありません。

ここでの登録率は、国税庁の法人番号公表サイトに載る現存の法人（登記が閉鎖された法人を除く）のうち、適格請求書発行事業者公表サイトの登録が2026年10月30日の時点で有効な法人の割合です。設立年月は法人番号の指定日で数えています。個人事業者は含みません。

設立から日が浅い会社は、登録するまでに経過した期間が短いため、登録率が低く出ると考えられます。この影響は、下の2024〜2025年と2021年から2023年9月の比較にも含まれます。

## 2023年10月以降に設立された株式会社ほど、登録率が下がる

登録率を設立四半期ごとに集計すると、2021年1月から2023年9月までに設立された株式会社は69.5%から72.1%の範囲でほぼ横ばいです。2023年10月以降に設立された会社から低下が始まり、2024年1月は64.6%、2025年1月は50.1%、2026年1月は42.5%です。合同会社も同じ向きで、2021年に42%から44%だった登録率は2026年1月に23.6%になっています。

```chart caption="設立四半期別の登録率（2026年10月30日時点）"
{
  "data": { "name": "cohort" },
  "mark": { "type": "line", "point": true },
  "encoding": {
    "x": { "field": "quarter", "type": "ordinal", "title": "設立四半期（開始月）", "axis": { "labelAngle": -45 } },
    "y": { "field": "rate", "type": "quantitative", "title": "登録率（%）", "scale": { "domain": [0, 80] } },
    "color": { "field": "kind_name", "type": "nominal", "title": null },
    "tooltip": [{ "field": "quarter" }, { "field": "kind_name" }, { "field": "corps", "format": "," }, { "field": "rate", "format": ".1f" }]
  }
}
```

使っているデータは2つです。法人番号公表サイトの全件データ（`mart_houjin_bangou`）は、法人の種類（株式会社・合同会社など）と、設立年月に使う法人番号の指定日を持ちます。適格請求書発行事業者公表サイトの全件データ（`issuers`）は、1行が1つの登録番号で、法人の登録番号は「T + 法人番号」です。法人番号で2つを結合し、登録が失効・取消になっていない法人を登録済みとしています。

図は2026年3月までに設立された会社を対象にしています。

```sql id=cohort
WITH inv AS (SELECT DISTINCT corporate_number FROM invoice_issuers.main.issuers WHERE is_registered AND registration_date <= DATE '2026-10-30') SELECT strftime(date_trunc('quarter', h.assignment_date), '%Y-%m') AS quarter, CASE h.kind WHEN '301' THEN '株式会社' ELSE '合同会社' END AS kind_name, COUNT(*) AS corps, ROUND(100.0 * AVG((i.corporate_number IS NOT NULL)::int), 1) AS rate FROM houjin_bangou.main.mart_houjin_bangou h LEFT JOIN inv i ON i.corporate_number = h.corporate_number WHERE h.process NOT IN ('71', '81') AND h.kind IN ('301', '305') AND h.assignment_date BETWEEN DATE '2021-01-01' AND DATE '2026-03-31' GROUP BY ALL ORDER BY 2, 1
```

## 登録していない株式会社は、2024〜2025年設立だけで9万社ある

株式会社を設立時期で4つに分けると、次のとおりです。制度開始前の群は設立が古い会社を含むため、登録率は65.4%と、2021年から2023年9月までに設立された会社（約71%）より低くなっています。

```sql
SELECT * FROM split
```

2024〜2025年設立の株式会社は19万7,621社あり、このうち登録していないのは9万879社で、46.0%です。制度開始前に設立された会社の未登録は76万5,646社で、母数は221万社です。

```sql id=split
WITH inv AS (SELECT DISTINCT corporate_number FROM invoice_issuers.main.issuers WHERE is_registered AND registration_date <= DATE '2026-10-30') SELECT CASE WHEN h.assignment_date < DATE '2023-10-01' THEN '制度開始前（〜2023年9月）' WHEN h.assignment_date < DATE '2024-01-01' THEN '2023年10〜12月' WHEN h.assignment_date < DATE '2026-01-01' THEN '2024〜2025年' ELSE '2026年1〜3月' END AS period, COUNT(*) AS corps, COUNT(i.corporate_number) AS registered, COUNT(*) - COUNT(i.corporate_number) AS unregistered, ROUND(100.0 * COUNT(i.corporate_number) / COUNT(*), 1) AS rate FROM houjin_bangou.main.mart_houjin_bangou h LEFT JOIN inv i ON i.corporate_number = h.corporate_number WHERE h.process NOT IN ('71', '81') AND h.kind = '301' AND h.assignment_date <= DATE '2026-03-31' GROUP BY ALL ORDER BY MIN(h.assignment_date)
```

## 法人の種類では、株式会社の63%に対して、有限会社は40%、合同会社は34%

設立時期を区別せずに法人の種類別に集計すると、株式会社の登録率が最も高く63.4%です。有限会社は39.9%、合同会社は34.4%で、合資会社と合名会社は10%台です。取引先に合同会社や合資会社が多い場合は、登録番号のない会社の割合が、株式会社中心の場合より高くなります。

```chart caption="法人の種類別の登録率（現存する株式会社・有限会社・合同会社・合資会社・合名会社）"
{
  "data": { "name": "kinds" },
  "mark": "bar",
  "encoding": {
    "y": { "field": "kind_name", "type": "nominal", "sort": "-x", "title": null },
    "x": { "field": "rate", "type": "quantitative", "title": "登録率（%）" },
    "tooltip": [{ "field": "kind_name" }, { "field": "corps", "format": "," }, { "field": "registered", "format": "," }, { "field": "rate", "format": ".1f" }]
  }
}
```

```sql id=kinds
WITH inv AS (SELECT DISTINCT corporate_number FROM invoice_issuers.main.issuers WHERE is_registered AND registration_date <= DATE '2026-10-30') SELECT CASE h.kind WHEN '301' THEN '株式会社' WHEN '302' THEN '有限会社' WHEN '305' THEN '合同会社' WHEN '303' THEN '合名会社' WHEN '304' THEN '合資会社' END AS kind_name, COUNT(*) AS corps, COUNT(i.corporate_number) AS registered, ROUND(100.0 * COUNT(i.corporate_number) / COUNT(*), 1) AS rate FROM houjin_bangou.main.mart_houjin_bangou h LEFT JOIN inv i ON i.corporate_number = h.corporate_number WHERE h.process NOT IN ('71', '81') AND h.kind IN ('301', '302', '303', '304', '305') GROUP BY h.kind ORDER BY corps DESC
```

## 2024〜2025年設立の株式会社の登録率は、福井県の65%から大阪府の49%まで開く

次の図は、2024〜2025年に設立された株式会社について、本店所在地の都道府県別に登録率を並べたものです。1位の福井県は65.3%（711社）で、47位の大阪府は49.3%（2万3,660社）です。東京都は50.4%で、設立数が最も多い6万549社の約半数が未登録です。登録率が低い下位10都府県には、東京都・大阪府・神奈川県・千葉県・兵庫県・京都府が入っています。地方の県は母数が少なく、福井県の711社、鳥取県の370社のように数百社の県もあります。

```chart caption="2024〜2025年設立の株式会社の登録率（本店所在地の都道府県別）"
{
  "data": { "name": "pref_rank" },
  "mark": "bar",
  "height": 1100,
  "encoding": {
    "y": { "field": "pref", "type": "nominal", "sort": "-x", "title": null },
    "x": { "field": "rate", "type": "quantitative", "title": "登録率（%）" },
    "color": { "field": "grp", "type": "nominal", "title": null, "scale": { "domain": ["上位10", "中間", "下位10"], "range": ["#3182bd", "#9ecae1", "#94a3b8"] } },
    "tooltip": [{ "field": "pref" }, { "field": "corps", "format": "," }, { "field": "rate", "format": ".1f" }]
  }
}
```

```sql id=pref_rank
WITH inv AS (SELECT DISTINCT corporate_number FROM invoice_issuers.main.issuers WHERE is_registered AND registration_date <= DATE '2026-10-30'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS corps, COUNT(i.corporate_number) AS registered FROM houjin_bangou.main.mart_houjin_bangou h LEFT JOIN inv i ON i.corporate_number = h.corporate_number WHERE h.process NOT IN ('71', '81') AND h.kind = '301' AND h.assignment_date BETWEEN DATE '2024-01-01' AND DATE '2025-12-31' AND h.prefecture_name IS NOT NULL GROUP BY h.prefecture_name), ranked AS (SELECT pref, corps, ROUND(100.0 * registered / corps, 1) AS rate, ROW_NUMBER() OVER (ORDER BY registered * 1.0 / corps DESC, pref) AS rn FROM agg) SELECT pref, corps, rate, CASE WHEN rn <= 10 THEN '上位10' WHEN rn > 37 THEN '下位10' ELSE '中間' END AS grp FROM ranked ORDER BY rn
```

## 取引先台帳の確認に使う

- 新規取引先を台帳に登録するときに、法人番号から登録番号の有無を引き、設立が2024年以降の会社は登録番号の確認を優先します。2024年1〜3月設立の株式会社の登録率は64.6%、2025年1〜3月設立は50.1%、2026年1〜3月設立は42.5%と下がるため、設立四半期ごとに確認の件数を見積もれます
- 2024〜2025年に設立された取引先の半数以上が東京都・大阪府・神奈川県にある場合は、同じ設立時期の全国値54%より未登録の割合が高いと見込んで、請求書の受領後に登録番号を確認する件数を見積もります
- 合同会社と合資会社の取引先が多い場合は、登録率が34%と11%にとどまるため、請求書を受け取るたびに登録番号の記載を確認する運用にします

## データの出典

本記事は国税庁の[適格請求書発行事業者公表サイト](https://www.invoice-kohyo.nta.go.jp/download/)の全件データ（2026年10月30日時点）と、[法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/download/)の全件データを法人番号で結合して集計しています。

請求書の登録番号の有無を取引先ごとに確認する作業には、登録の状態と法人の基本情報を同じ法人番号で結び付けたデータが必要です。Queriaはこの2つのデータを列名・日付・コードを揃えて公開しています。[適格請求書発行事業者のテーブル](/datasets/queria/invoice_issuers/main/issuers)と[法人番号のテーブル](/datasets/queria/houjin_bangou/main/mart_houjin_bangou)から、自社の取引先と同じ条件の登録率を確かめられます。

```sql id=base
WITH inv AS (SELECT DISTINCT corporate_number FROM invoice_issuers.main.issuers WHERE is_registered AND registration_date <= DATE '2026-10-30') SELECT COUNT(*) AS corps, ROUND(100.0 * COUNT(i.corporate_number) / COUNT(*), 1) AS rate FROM houjin_bangou.main.mart_houjin_bangou h LEFT JOIN inv i ON i.corporate_number = h.corporate_number WHERE h.process NOT IN ('71', '81') AND h.kind = '301' AND h.assignment_date BETWEEN DATE '2021-01-01' AND DATE '2023-09-30'
```

```sql id=asof
SELECT MAX(file_date) AS file_date FROM invoice_issuers.main.issuers
```
