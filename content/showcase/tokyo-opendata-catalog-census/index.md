---
title: 東京都オープンデータカタログでCSVを含むデータセットは64.2%、更新頻度の書き方は136通り
description: 東京都オープンデータカタログの9,646データセット・82,998ファイルのメタデータを集計しました。過半数は区市町村が公開しており、CSVを含むデータセットは64.2%、更新頻度の書き方は136通りに分かれています。
publishedAt: 2026-07-18
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - オープンデータ
  - 東京都
  - メタデータ
datasets:
  - queria/metro_tokyo
sources:
  - title: 東京都オープンデータカタログサイト
    url: https://portal.data.metro.tokyo.lg.jp/
    publisher: 東京都
  - title: 東京都オープンデータ推進庁内ガイドライン
    url: https://portal.data.metro.tokyo.lg.jp/guideline/
    publisher: 東京都
agentHint: 組織(organization_title)別に、CSVを含むデータセットの割合をresourcesのformatから出して、機械判読しやすい形式で公開が進んでいる組織を比べて
socialAnnounce: |-
  東京都オープンデータカタログの9,646データセット・82,998ファイルのメタデータを数えました。

  CSVを含むのは64.2%。更新頻度の書き方は136通りに分かれ、「年1回」の意味だけで28通りありました。
  Queriaは行政のオープンデータを整えて公開しています。
---

東京都オープンデータカタログには、2026年7月時点で9,646のデータセットと82,998のファイルがあります。データセットの過半数（5,534件）は都の局ではなく区市町村などが公開しています。ファイルの約8割はCSVですが、CSVを含むデータセットは64.2%でした。更新頻度の欄の書き方は136通りあり、「1年に1回程度」の意味の書き方だけで28通りあります。

東京都は2017年から[東京都オープンデータカタログサイト](https://portal.data.metro.tokyo.lg.jp/)を運営しています。都の各局に加えて、区市町村のデータも同じカタログで公開されています。誰がどれだけ公開しているか、どの分野が多いか、機械判読できる形式でどれくらい提供されているかは、カタログのメタデータを集計すると確認できます。この記事では、カタログのメタデータを集計の対象にします。

## カタログには9,646のデータセットと82,998のファイルがある

データセット（テーマごとのまとまり）とリソース（実際に配布されるファイル）は別の単位で、1つのデータセットが複数のファイルを持ちます。

```sql
SELECT 'データセット数' AS 項目, COUNT(*) AS 件数 FROM metro_tokyo.catalog.datasets UNION ALL SELECT 'リソース（ファイル）数', COUNT(*) FROM metro_tokyo.catalog.resources UNION ALL SELECT '公開組織数', COUNT(DISTINCT organization_title) FROM metro_tokyo.catalog.datasets UNION ALL SELECT '東京都の局（組織数）', COUNT(DISTINCT organization_title) FROM metro_tokyo.catalog.datasets WHERE organization_title LIKE '東京都%' UNION ALL SELECT '東京都の局（データセット数）', COUNT(*) FROM metro_tokyo.catalog.datasets WHERE organization_title LIKE '東京都%' UNION ALL SELECT '区市町村など（組織数）', COUNT(DISTINCT organization_title) FROM metro_tokyo.catalog.datasets WHERE organization_title NOT LIKE '東京都%' UNION ALL SELECT '区市町村など（データセット数）', COUNT(*) FROM metro_tokyo.catalog.datasets WHERE organization_title NOT LIKE '東京都%' UNION ALL SELECT 'CC BYで公開', COUNT(*) FROM metro_tokyo.catalog.datasets WHERE license_title = 'クリエイティブ・コモンズ 表示（CC BY）'
```

9,646のデータセットに82,998のファイルがあり、95の組織が公開しています。そのうち31が東京都の局、64が区市町村などです。ライセンスは9,643件がクリエイティブ・コモンズ表示（CC BY）なので、利用条件をデータセットごとに確認する必要はほとんどありません。

データセットがカタログに登録された年ごとの件数です。`metadata_created` はデータセットがカタログに登録された日時で、データが作成された日や最後に更新された日とは異なります。カタログの運用が始まった2017〜2018年は年の途中からの登録なので、1年分がそろう2019年から2025年を対象にしています。

```chart
{
  "layer": [
    {
      "data": {"name": "yearly"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"n\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49, "color": "#3b82f6"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "n", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "登録年", "format": "d"}
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "登録データセット数（件）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

登録数は、2019年の419件から2020年に247件に減り、2021年に1,173件に増えています。東京都がデジタルサービス局を設置した2021年4月と同じ時期です。2022年（885件）にいったん減り、2024年の2,965件が最も多く、2025年も2,239件でした。

2019年から2025年までの登録数の合計は8,989件で、全9,646件の大半がこの7年間に登録されています。

## データセットの過半数は、都の局ではなく区市町村が公開している

データセットを公開している組織の上位20です。組織名が「東京都」で始まるものを都の局、それ以外を区市町村などとして色を分けています。

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "org_pref"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "n", "type": "quantitative"},
          {"field": "organization_title", "type": "nominal"}
        ],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "データセット数（件）", "grid": true}
        },
        "y": {
          "field": "organization_title",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "datum": "東京都の局",
          "type": "nominal",
          "scale": {"domain": ["東京都の局", "区市町村など"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "org_city"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "n", "type": "quantitative"},
          {"field": "organization_title", "type": "nominal"}
        ],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "データセット数（件）", "grid": true}
        },
        "y": {
          "field": "organization_title",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "color": {
          "datum": "区市町村など",
          "type": "nominal",
          "scale": {"domain": ["東京都の局", "区市町村など"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        }
      }
    }
  ]
}
```

最も多いのは東京都総務局の2,172件です。総務局には統計部門があり、統計表を1表ずつデータセットとして登録しているので、件数が多くなります。

2位は調布市の1,487件で、都の福祉局（340件）や保健医療局（257件）を大きく上回り、区市町村の中で特に多くなっています。3位の狛江市（399件）も人口規模に比べて多く、大田区（278件）、港区（268件）、江戸川区（266件）などの特別区が続きます。データセットの件数は自治体の規模より、どこまで細かい単位で登録するかという運用の方針で大きく変わると考えられます。

カタログ全体では、区市町村など64組織の5,534件が、都の局31組織の4,112件を上回っています。東京都のカタログですが、データセットの過半数は区市町村などが公開したものです。

## 分野では「行財政」が3,848件で最も多い

カタログでは、各データセットに分野が付けられています。1つのデータセットが複数の分野に属することがあるので、分野ごとにデータセットを重複なく集計しました。分野ごとの件数を足しても、総数にはなりません。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "field"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "n", "type": "quantitative"},
          {"field": "field_name", "type": "nominal"}
        ],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "データセット数（件）", "grid": true}
        },
        "y": {
          "field": "field_name",
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

分野は15あり、「行財政」が3,848件で特に多くなっています。予算・決算・統計・人事など、行政運営に関わるデータです。「くらし・住まい」（1,146件）、「子供・若者・教育」（827件）、「インフラ・まちづくり」（807件）が続きます。

少ないのは「交通」（79件）、「デジタル・最新技術」（95件）、「スポーツ」（116件）です。交通が少ないのは、鉄道やバスの運行データは事業者が公開することが多く、自治体のカタログには載りにくいためと考えられます。

## ファイルの約8割はCSVだが、CSVを含むデータセットは64.2%

オープンデータでは、機械判読できる形式で公開されているかがよく議論されます。国の[オープンデータ基本指針](https://www.digital.go.jp/resources/open_data)も、構造化しやすいデータはCSVなど機械判読に適した形式で公開することを原則としています。カタログのリソースには形式が記録されているので、形式ごとに集計しました。形式の欄が空のリソースは除いています。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "fmt"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "n", "type": "quantitative"}, {"field": "fmt", "type": "nominal"}],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "リソース数（件）", "grid": true}
        },
        "y": {
          "field": "fmt",
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

ファイル単位では、CSVが65,584件で全体の約8割です。XLSX（6,418件）、PDF（3,423件）、XLS（3,349件）が続き、PDFは4%程度です。

1つのデータセットが数百のファイルを持つことがあるので、ファイル単位の割合は、ファイル数の多いデータセットの影響を強く受けます。ファイル数の多い順に並べると、上位は統計調査の報告書です。

```sql
SELECT d.title AS データセット, d.organization_title AS 提供組織, COUNT(*) AS ファイル数 FROM metro_tokyo.catalog.resources r JOIN metro_tokyo.catalog.datasets d ON d.package_id = r.package_id GROUP BY 1, 2 ORDER BY ファイル数 DESC LIMIT 5
```

最も多いデータセットは596ファイルを持っています。集計表を1表ずつCSVで公開しているためで、このようなデータセットがファイル単位の割合を大きく動かします。

そこで、データセット単位でも集計しました。リソースが登録されていない4件を除く9,642のデータセットを、CSVを含むもの、Excelだけのもの、どちらも含まないものに分類しています。

```chart
{
  "height": 180,
  "layer": [
    {
      "data": {"name": "ds_fmt"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "n", "type": "quantitative"},
          {"field": "category", "type": "nominal"}
        ],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "データセット数（件）", "grid": true}
        },
        "y": {
          "field": "category",
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

CSVを含むデータセットは6,192件で64.2%です。ファイル単位の約8割より大きく下がります。Excelだけのものが2,288件（23.7%）、CSVもExcelも含まないものが1,162件（12.0%）で、合わせて3分の1強は、機械判読しやすい表形式のファイルがありません。利用者がどのテーマのデータでも表形式で取得できるかを評価するには、データセット単位の割合のほうが適していると考えられます。形式の欄は登録時に記入された値なので、CSVと記録されていても、セル結合や複数段の見出しを含む表の場合があります。

## 更新頻度の欄の書き方は136通りあり、「1年に1回程度」だけで28通りある

カタログには更新頻度の欄があります。都の[オープンデータ推進庁内ガイドライン](https://portal.data.metro.tokyo.lg.jp/guideline/)は、利用者が更新の時期を事前に把握できるよう、更新の周期を明示するよう求めています。この欄の書き方を集計しました。

書き方は136通りでした。このうち「1年に1回程度の更新」を意味する書き方は28通りあり、合わせて2,211件のデータセットが該当します。「年」を含み、「月」「週」「日」「数」「行わない」と、2以上の数字や「半」を含まない書き方を抜き出しているので、「2年に1回」や「半年ごと」は含みませんが、この条件から漏れた書き方もある可能性があります。

```sql
SELECT '更新頻度の表記の種類' AS 項目, COUNT(DISTINCT update_frequency) AS 件数 FROM metro_tokyo.catalog.datasets WHERE update_frequency IS NOT NULL AND update_frequency <> '' UNION ALL SELECT '「年1回」を意味する表記の種類', COUNT(DISTINCT update_frequency) FROM metro_tokyo.catalog.datasets WHERE update_frequency LIKE '%年%' AND update_frequency NOT LIKE '%月%' AND update_frequency NOT LIKE '%週%' AND update_frequency NOT LIKE '%日%' AND update_frequency NOT LIKE '%数%' AND update_frequency NOT LIKE '%行わない%' AND NOT regexp_matches(update_frequency, '[2-9２-９二三四五六七八九半]') UNION ALL SELECT '「年1回」に該当するデータセット数', COUNT(*) FROM metro_tokyo.catalog.datasets WHERE update_frequency LIKE '%年%' AND update_frequency NOT LIKE '%月%' AND update_frequency NOT LIKE '%週%' AND update_frequency NOT LIKE '%日%' AND update_frequency NOT LIKE '%数%' AND update_frequency NOT LIKE '%行わない%' AND NOT regexp_matches(update_frequency, '[2-9２-９二三四五六七八九半]')
```

件数の多い12通りです。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "freq"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [{"field": "n", "type": "quantitative"}, {"field": "label", "type": "nominal"}],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "データセット数（件）", "grid": true}
        },
        "y": {
          "field": "label",
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

「1年ごと」（922件）、「年１回」（672件）、「年1回」（171件）、「１年ごと」（125件）のように、同じ意味の書き方が全角・半角や語順の違いで分かれています。「1回/年」「毎年」「年次」も同じ意味です。9番目に多い `随時\n１年に１回程度`（17件）は、改行を表すエスケープ文字がそのまま値に残っています。

これはカタログの仕組みによるものと考えられます。東京都のカタログは CKAN というソフトウェアで運用されていて、CKAN の標準スキーマには更新頻度の項目がありません。そのため、運用者は「extras」という自由記述の追加項目に更新頻度を書いています。[CKANの公式ドキュメント](https://docs.ckan.org/en/2.11/extensions/adding-custom-fields.html)には、extras はキーも値も文字列しか持てず、入力の検証や選択肢の限定もできないと書かれています。値の候補を限定する仕組みがないので、書き方は登録者ごとに異なります。

更新頻度でデータセットを絞り込むには、この欄をそのまま条件に使えないので、書き方の違いを正規化してから集計する必要があります。

## まとめ

- 9,646データセット・82,998ファイルの過半数は、都の局ではなく区市町村などが公開している。件数の順位は自治体の規模より、どこまで細かく登録するかという運用の方針で決まっている
- ファイル単位ではCSVが約8割だが、CSVを含むデータセットは64.2%。どちらの単位で集計するかで、機械判読できる割合が大きく変わる
- 更新頻度の欄の書き方は136通りあり、「1年に1回程度」の意味だけで28通りある。カタログのソフトウェアが自由記述しか受け付けないことが原因と考えられる

## データの出典

本記事は[東京都オープンデータカタログサイト](https://portal.data.metro.tokyo.lg.jp/)のメタデータを、2026年7月18日時点で取得して集計しています。集計したのはカタログに登録された情報で、データファイルの中身は集計していません。

Queria は、東京都オープンデータカタログのメタデータを、列名・単位・文字コードを統一し、各列の意味の説明を付けて公開しています。本記事で使った[データセット一覧テーブル](/datasets/queria/metro_tokyo/catalog/datasets)や[リソース一覧テーブル](/datasets/queria/metro_tokyo/catalog/resources)から、特定の区市町村が公開しているデータセットを一覧にしたり、探している分野にどの形式のファイルがあるかを確認したりできます。

```sql id=yearly
SELECT YEAR(metadata_created) AS year, COUNT(*) AS n FROM metro_tokyo.catalog.datasets WHERE YEAR(metadata_created) BETWEEN 2019 AND 2025 GROUP BY 1 ORDER BY 1
```

```sql id=org_all
WITH ranked AS (SELECT organization_title, COUNT(*) AS n, ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, organization_title) AS rn FROM metro_tokyo.catalog.datasets GROUP BY 1) SELECT organization_title, n FROM ranked WHERE rn <= 20 ORDER BY rn
```

```sql id=org_pref
WITH ranked AS (SELECT organization_title, COUNT(*) AS n, ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, organization_title) AS rn FROM metro_tokyo.catalog.datasets GROUP BY 1) SELECT organization_title, n FROM ranked WHERE rn <= 20 AND organization_title LIKE '東京都%' ORDER BY rn
```

```sql id=org_city
WITH ranked AS (SELECT organization_title, COUNT(*) AS n, ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, organization_title) AS rn FROM metro_tokyo.catalog.datasets GROUP BY 1) SELECT organization_title, n FROM ranked WHERE rn <= 20 AND organization_title NOT LIKE '東京都%' ORDER BY rn
```

```sql id=field
SELECT g.title AS field_name, COUNT(DISTINCT dg.package_id) AS n FROM metro_tokyo.catalog.dataset_groups dg JOIN metro_tokyo.catalog.groups g ON g.group_code = dg.group_code GROUP BY 1 ORDER BY n DESC
```

```sql id=fmt
WITH f AS (SELECT UPPER(format) AS fmt, COUNT(*) AS n FROM metro_tokyo.catalog.resources WHERE format IS NOT NULL AND format <> '' GROUP BY 1), r AS (SELECT fmt, n, ROW_NUMBER() OVER (ORDER BY n DESC, fmt) AS rn FROM f) SELECT fmt, n FROM r WHERE rn <= 12 ORDER BY n DESC
```

```sql id=ds_fmt
WITH d AS (SELECT package_id, BOOL_OR(UPPER(format) = 'CSV') AS has_csv, BOOL_OR(UPPER(format) IN ('XLS', 'XLSX')) AS has_excel FROM metro_tokyo.catalog.resources GROUP BY package_id) SELECT CASE WHEN has_csv THEN 'CSVを含む' WHEN has_excel THEN 'Excelのみ（CSVなし）' ELSE 'CSVもExcelも含まない' END AS category, COUNT(*) AS n FROM d GROUP BY 1 ORDER BY n DESC
```

```sql id=freq
WITH y AS (SELECT update_frequency AS label, COUNT(*) AS n FROM metro_tokyo.catalog.datasets WHERE update_frequency LIKE '%年%' AND update_frequency NOT LIKE '%月%' AND update_frequency NOT LIKE '%週%' AND update_frequency NOT LIKE '%日%' AND update_frequency NOT LIKE '%数%' AND update_frequency NOT LIKE '%行わない%' AND NOT regexp_matches(update_frequency, '[2-9２-９二三四五六七八九半]') GROUP BY 1), r AS (SELECT label, n, ROW_NUMBER() OVER (ORDER BY n DESC, label) AS rn FROM y) SELECT label, n FROM r WHERE rn <= 12 ORDER BY n DESC
```
