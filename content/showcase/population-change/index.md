---
title: 人口が増えた256市区町村の122は日本人が減っています
description: 住民基本台帳の市区町村別人口を2014年から2026年まで日本人と外国人に分けて集計しました。2026年1月1日時点で人口が増えていたのは1,898市区町村のうち256で、そのうち122は日本人が減り、外国人の増加が日本人の減少を上回った市区町村です。出生数が死亡数を上回ったのは21で、2014年の261から減りました。
ogDescription: 住民基本台帳の市区町村別人口を2014年から2026年まで日本人と外国人に分けて集計しました。人口が増えた256市区町村のうち、出生数が死亡数を上回ったのは21、日本人が減りながら増えたのは122です。
publishedAt: 2026-02-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口
  - 市区町村
  - 住民基本台帳
datasets:
  - queria/e_stat
sources:
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
agentHint: e_stat.resident_registry.population の2026年で、自分の県の市区町村について resident_kind ごとの net_change を並べて。総人口が増えて日本人が減っている市区町村がいくつあるかも数えて
socialAnnounce: |-
  住民基本台帳の市区町村別人口を、日本人と外国人に分けて2014年から2026年まで並べました。

  人口が増えた256市区町村のうち122は日本人が減っています。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2025年の1年間で人口が増えた市区町村は、1,898のうち256でした。そのうち122は、日本人が減り、外国人の増加が日本人の減少を上回ったことで人口が増えています。出生数が死亡数を上回った市区町村は21です。2014年は、人口が増えた390市区町村のうち、出生数が死亡数を上回ったのが261、日本人が減りながら人口が増えたのが15でした。

全国では、2025年の1年間で人口が563,048人減りました。日本人が916,744人減り、外国人が353,696人増えています。人口が増えた市区町村の数は、2014年の390から2017年の421まで増え、その後は減って2026年は256です。

## 人口が増えた市区町村のうち、出生数が死亡数を上回ったのは2014年の261から2026年は21に減った

使ったのは総務省の[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)で、1行が1つの地域と1つの住民区分の組み合わせです。住民区分（`resident_kind`）には日本人（`japanese`）・外国人（`foreign`）・両者の合計（`total`）の3つがあります。

| 列                 | 内容                                                   |
| ------------------ | ------------------------------------------------------ |
| `population_total` | 時点の人口                                             |
| `natural_change`   | 自然増減（出生数 − 死亡数）                            |
| `social_change`    | 社会増減（転入者数 − 転出者数 ＋ その他増 − その他減） |
| `net_change`       | 増減数（自然増減 ＋ 社会増減）                         |

人口は各年の時点の値、増減はその前の1年間の値です。外国人住民が住民基本台帳に記録されるようになったのは2012年7月なので、外国人と合計のデータは2013年からです。時点は2013年までが3月31日、2014年以降が1月1日なので、時点が統一されている2014年以降を集計しました。集計の単位は市区町村で、政令指定都市は行政区ごと、東京23区は区ごとに集計しています。市区町村の数は市町村合併や区の再編で年ごとに変わり、2026年は1,898です。

人口が増えた市区町村の数と、そのうち出生数が死亡数を上回った数、日本人が減りながら人口が増えた数を重ねました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "composition"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"grew\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "grew", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "時点（年）", "format": "d"}
        },
        "y": {
          "field": "grew",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "color": {
          "datum": "人口が増えた",
          "type": "nominal",
          "scale": {
            "domain": ["人口が増えた", "うち出生数が死亡数を上回った", "うち日本人が減った"],
            "range": ["#64748b", "#22c55e", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "composition"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"grew_with_births\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "grew_with_births", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "時点（年）", "format": "d"}
        },
        "y": {
          "field": "grew_with_births",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "color": {
          "datum": "うち出生数が死亡数を上回った",
          "type": "nominal",
          "scale": {
            "domain": ["人口が増えた", "うち出生数が死亡数を上回った", "うち日本人が減った"],
            "range": ["#64748b", "#22c55e", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "composition"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"grew_as_japanese_fell\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "grew_as_japanese_fell", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "時点（年）", "format": "d"}
        },
        "y": {
          "field": "grew_as_japanese_fell",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        },
        "color": {
          "datum": "うち日本人が減った",
          "type": "nominal",
          "scale": {
            "domain": ["人口が増えた", "うち出生数が死亡数を上回った", "うち日本人が減った"],
            "range": ["#64748b", "#22c55e", "#ef4444"]
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

2014年に人口が増えた390市区町村のうち、出生数が死亡数を上回ったのは261、日本人が減りながら人口が増えたのは15でした。2026年は、増えた256のうち出生数が死亡数を上回ったのが21、日本人が減りながら増えたのが122で、2つの数の大小が逆になっています。

この2つの数の大小は、2022年から2023年の間に逆になりました。2022年は、増えた215のうち日本人が減りながら増えた市区町村が4で、13年間で最も少ない年です。2022年の時点は2022年1月1日なので、増減は2021年の1年間の値で、入国制限が続いていた期間にあたります。

2026年の1,898市区町村のうち、日本人が減ったのは1,757、外国人が増えたのは1,677です。両方が起きた市区町村は1,545で、全体の8割です。122は、そのうち外国人の増加が日本人の減少より大きかった市区町村です。

## 日本人が減りながら人口が増えた122市区町村は、24都道府県にある

122市区町村を合計すると、人口は45,828人増え、日本人は39,540人減り、外国人は85,368人増えています。人口の増加数の中央値は178人で、122のうち52は100人未満、1,000人以上増えたのは10です。半分近くは100人未満の差で増加になっているので、順位ではなく増減の向きを見るための数字です。

増加数の上位12市区町村を、日本人と外国人に分けて並べました。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "jp_fell_top"},
      "transform": [
        {"fold": ["japanese_change", "foreign_change"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"japanese_change\": \"日本人\", \"foreign_change\": \"外国人\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"japanese_change\",\"foreign_change\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "name",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": -45},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "増減数（人）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["日本人", "外国人"], "range": ["#94a3b8", "#2563eb"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["日本人", "外国人"]},
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

増加数が最も大きいのは江戸川区の3,844人で、日本人が995人減り、外国人が4,839人増えています。122のうち日本人の減少と外国人の増加がどちらも最も大きいのは川口市で、日本人が4,561人減り、外国人が5,629人増えて、人口は1,068人増えました。松戸市も日本人が1,697人減り、外国人が3,152人増えて、1,455人増えています。

川口市の内訳を見ると、日本人は転入20,770人、転出20,647人でほぼ同じで、死亡が出生を3,428人上回った分が減少になっています。外国人は転入15,078人、転出7,504人で、転入が転出の2倍です。外国人の社会増減5,202人には、転入と転出の差のほかに、その他増108人とその他減2,480人も含まれているので、社会増減は転入超過と同じ値ではありません。

122市区町村は24都道府県にあります。大阪府の15、東京都の14、埼玉県と愛知県の各11が多く、北海道の7、宮城県の5、長野県の4も含まれます。大都市圏以外でも起きています。

国勢調査をもとに2015年から2020年で同じ条件の市区町村を集計した結果は、[外国人人口の記事](/showcase/foreign-population)にあります。

## 出生数が死亡数を上回った21市区町村のうち、10は大都市の区

人口が増えた256のうち、出生数が死亡数を上回った21市区町村です。

```sql
SELECT pref AS 都道府県, name AS 市区町村, births AS 出生数, deaths AS 死亡数, natural_gain AS 自然増減, social_change AS 社会増減, total_change AS 増減数 FROM birth_gain
```

21市区町村は3つに分かれます。東京都の中央区・港区・千代田区、大阪市の中央区・西区・北区・福島区・天王寺区、川崎市中原区、福岡市博多区の10は大都市の区です。つくば市・長久手市・日進市・和光市・野々市市・菊陽町・川越町の7は大都市に隣接する市町です。残る4は沖縄県の南風原町・豊見城市・中城村・宜野座村です。

自然増減の中央値は86人で、21のうち8つは50人未満です。三重郡川越町の1人のように、出生数と死亡数がほぼ同じ市区町村も含まれます。

社会増減がマイナスなのは島尻郡南風原町の-6人と豊見城市の-96人の2つだけで、残る19は社会増減もプラスです。転出超過を自然増で補って人口が増えている市区町村は、この21のうち2つです。

## 減少率の下位20のうち14でも外国人は増えているが、増加は合計199人

減少率の下位20を並べました。増加率と同じく、1年前の人口が1万人以上の市区町村に絞っています。この条件を外すと下位20のうち18が1万人未満の町村になりますが、最も減少率が大きいのは、条件の有無にかかわらず珠洲市です。

```chart
{
  "height": 380,
  "layer": [
    {
      "data": {"name": "decline_rate_top"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "change_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "", "labelAngle": -45},
          "sort": null
        },
        "y": {
          "field": "change_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "増減率（%）", "grid": true}
        }
      }
    }
  ]
}
```

減少率が最も大きいのは石川県珠洲市の-8.39%で、輪島市の-6.27%、鳳珠郡能登町の-4.02%が続きます。この3市町は2024年1月の令和6年能登半島地震の被災地で、ここに出ているのは地震から2年目にあたる2025年の1年間の増減です。4位以降は福島県双葉郡浪江町の-3.59%から兵庫県美方郡香美町の-2.95%までの範囲にあり、下位20のうち17がこの範囲に入ります。

住民基本台帳は住民登録の数なので、避難していても転出届を出していなければ人口は減らず、避難先へ住民票を移すと減少として集計されます。能登の3市町の値は、住民票の移動を反映したものです。

この20のうち14では、外国人が増えています。20市区町村の外国人の増加は合計199人で、同じ20市区町村の日本人は10,668人減っています。外国人の増加は人口が減っている市区町村でも起きていて、122市区町村との違いは増加の大きさです。

## 増加率の上位20で日本人が減っているのは2だけ

増加率の上位20を並べました。1年前の人口が1万人以上の市区町村に絞っています。

```sql
SELECT pref AS 都道府県, name AS 市区町村, population AS 人口, total_change AS 増減数, change_pct AS 増減率 FROM growth_rate_top
```

愛知県名古屋市中区の3.38%と大阪府三島郡島本町の3.06%が特に高く、3位の東京都中央区は1.93%です。20位は福岡県福岡市東区の1.28%です。

この20のうち、日本人が減っているのは2つだけで、出生数が死亡数を上回ったのは6つです。増加率が高い市区町村と、外国人の増加で人口が増えた122市区町村は、ほとんど重なりません。

同じ表で、名古屋市中区は3,365人増えて人口102,869人、島本町は988人増えて33,235人です。人口が少ない市区町村は数百人の増減で率が大きく変わるので、規模を比較するときは増減数で並べ直す必要があります。

## まとめ

- 2025年の1年間で全国の人口は563,048人減り、日本人が916,744人減って、外国人が353,696人増えました
- 1,898市区町村のうち人口が増えたのは256です。日本人が減った市区町村は1,757、外国人が増えた市区町村は1,677あります
- 人口が増えた256のうち、出生数が死亡数を上回ったのは21です。2014年は390のうち261でした
- 日本人が減りながら人口が増えた市区町村は122です。2014年は15で、入国制限が続いていた2022年は4でした
- 122市区町村は24都道府県にあり、大阪府15・東京都14・埼玉県11・愛知県11が多くなっています
- 減少率の下位20のうち14でも外国人は増えています。20市区町村の外国人の増加は合計199人で、同じ20市区町村の日本人の減少10,668人より大幅に少なくなっています
- 増加率の上位20で日本人が減っているのは2つだけで、122市区町村とはほとんど重なりません

## データの出典

本記事は総務省の[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)の市区町村別データを2026年9月22日時点で集計しています。人口は各年1月1日時点、増減はその前の1年間の値で、外国人を含む集計は2013年から収録されています。

Queriaは、住民基本台帳の人口と人口動態を、市区町村のコードを標準地域コードに統一したテーブルにし、住民区分や時点の切り替わりをメタデータに記載して公開しています。本記事で使った[住民基本台帳人口テーブル](/datasets/queria/e_stat/resident_registry/population)から、自分の自治体の増減を日本人と外国人に分けて確認したり、近隣の市区町村と比較したりできます。

```sql id=coverage
SELECT year, MIN(reference_date) AS reference_date, COUNT(DISTINCT resident_kind) AS resident_kinds, COUNT(DISTINCT area_code) AS areas FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year BETWEEN 2010 AND 2026 GROUP BY year ORDER BY year
```

```sql id=national
SELECT year, resident_kind, population_total, births, deaths, natural_change, social_change, net_change FROM e_stat.resident_registry.population WHERE area_level = 'national' AND year BETWEEN 2014 AND 2026 ORDER BY year, resident_kind
```

```sql id=composition
WITH m AS (SELECT year, area_code, municipality_name, resident_kind, natural_change, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year BETWEEN 2014 AND 2026), leaf AS (SELECT DISTINCT a.year, a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.year = a.year AND b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (year, area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (year, area_code) WHERE m.resident_kind = 'japanese') SELECT t.year AS year, COUNT(*) AS municipalities, SUM(CASE WHEN t.net_change > 0 THEN 1 ELSE 0 END) AS grew, SUM(CASE WHEN t.net_change > 0 AND t.natural_change > 0 THEN 1 ELSE 0 END) AS grew_with_births, SUM(CASE WHEN t.net_change > 0 AND j.net_change < 0 THEN 1 ELSE 0 END) AS grew_as_japanese_fell FROM t JOIN j USING (year, area_code) GROUP BY t.year ORDER BY t.year
```

```sql id=latest_counts
WITH m AS (SELECT area_code, municipality_name, resident_kind, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese'), f AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'foreign') SELECT COUNT(*) AS municipalities, SUM(CASE WHEN t.net_change > 0 THEN 1 ELSE 0 END) AS grew, SUM(CASE WHEN j.net_change < 0 THEN 1 ELSE 0 END) AS japanese_fell, SUM(CASE WHEN f.net_change > 0 THEN 1 ELSE 0 END) AS foreign_rose, SUM(CASE WHEN j.net_change < 0 AND f.net_change > 0 THEN 1 ELSE 0 END) AS japanese_fell_foreign_rose FROM t JOIN j USING (area_code) JOIN f USING (area_code)
```

```sql id=jp_fell_profile
WITH m AS (SELECT area_code, municipality_name, resident_kind, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese'), f AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'foreign') SELECT COUNT(*) AS municipalities, SUM(CASE WHEN t.net_change < 100 THEN 1 ELSE 0 END) AS gain_under_100, SUM(CASE WHEN t.net_change >= 1000 THEN 1 ELSE 0 END) AS gain_over_1000, CAST(MEDIAN(t.net_change) AS BIGINT) AS median_gain, SUM(t.net_change) AS total_gain, SUM(j.net_change) AS japanese_loss, SUM(f.net_change) AS foreign_gain FROM t JOIN j USING (area_code) JOIN f USING (area_code) WHERE t.net_change > 0 AND j.net_change < 0
```

```sql id=jp_fell_top
WITH m AS (SELECT area_code, municipality_name, resident_kind, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese'), f AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'foreign') SELECT t.municipality_name AS name, t.net_change AS total_change, j.net_change AS japanese_change, f.net_change AS foreign_change FROM t JOIN j USING (area_code) JOIN f USING (area_code) WHERE t.net_change > 0 AND j.net_change < 0 ORDER BY t.net_change DESC, t.municipality_name LIMIT 12
```

```sql id=jp_fell_pref
WITH m AS (SELECT area_code, pref_name, municipality_name, resident_kind, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese') SELECT t.pref_name AS pref, COUNT(*) AS municipalities FROM t JOIN j USING (area_code) WHERE t.net_change > 0 AND j.net_change < 0 GROUP BY t.pref_name ORDER BY municipalities DESC, t.pref_name
```

```sql id=kawaguchi
SELECT resident_kind AS kind, moved_in_total AS moved_in, moved_out_total AS moved_out, other_added AS other_in, other_removed AS other_out, social_change AS social_change, births AS births, deaths AS deaths, natural_change AS natural_change, net_change AS net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026 AND municipality_name = '川口市' ORDER BY resident_kind
```

```sql id=birth_gain
WITH m AS (SELECT area_code, pref_name, municipality_name, resident_kind, births, deaths, natural_change, social_change, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total') SELECT t.pref_name AS pref, t.municipality_name AS name, t.births AS births, t.deaths AS deaths, t.natural_change AS natural_gain, t.social_change AS social_change, t.net_change AS total_change FROM t WHERE t.net_change > 0 AND t.natural_change > 0 ORDER BY t.natural_change DESC, t.municipality_name
```

```sql id=growth_rate_top
WITH m AS (SELECT area_code, pref_name, municipality_name, resident_kind, population_total, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total') SELECT t.pref_name AS pref, t.municipality_name AS name, t.population_total AS population, t.net_change AS total_change, ROUND(100.0 * t.net_change / (t.population_total - t.net_change), 2) AS change_pct FROM t WHERE t.population_total - t.net_change >= 10000 ORDER BY change_pct DESC, t.municipality_name LIMIT 20
```

```sql id=decline_rate_top
WITH m AS (SELECT area_code, pref_name, municipality_name, resident_kind, population_total, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total') SELECT t.pref_name || ' ' || t.municipality_name AS label, t.population_total AS population, t.net_change AS total_change, ROUND(100.0 * t.net_change / (t.population_total - t.net_change), 2) AS change_pct FROM t WHERE t.population_total - t.net_change >= 10000 ORDER BY change_pct ASC, t.municipality_name LIMIT 20
```

```sql id=jp_fell_extremes
WITH m AS (SELECT area_code, municipality_name, resident_kind, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese'), f AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'foreign'), g AS (SELECT t.municipality_name AS name, j.net_change AS japanese_change, f.net_change AS foreign_change FROM t JOIN j USING (area_code) JOIN f USING (area_code) WHERE t.net_change > 0 AND j.net_change < 0) SELECT name, japanese_change, foreign_change, RANK() OVER (ORDER BY japanese_change ASC) AS japanese_decline_rank, RANK() OVER (ORDER BY foreign_change DESC) AS foreign_gain_rank FROM g QUALIFY japanese_decline_rank <= 3 OR foreign_gain_rank <= 3 ORDER BY japanese_decline_rank, name
```

```sql id=growth_top_profile
WITH m AS (SELECT area_code, municipality_name, resident_kind, population_total, natural_change, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese'), ranked AS (SELECT t.area_code, ROW_NUMBER() OVER (ORDER BY ROUND(100.0 * t.net_change / (t.population_total - t.net_change), 2) DESC, t.municipality_name) AS rn FROM t WHERE t.population_total - t.net_change >= 10000) SELECT COUNT(*) AS municipalities, SUM(CASE WHEN j.net_change < 0 THEN 1 ELSE 0 END) AS japanese_fell, SUM(CASE WHEN t.natural_change > 0 THEN 1 ELSE 0 END) AS births_over_deaths FROM ranked r JOIN t USING (area_code) JOIN j USING (area_code) WHERE r.rn <= 20
```

```sql id=decline_bottom_profile
WITH m AS (SELECT area_code, municipality_name, resident_kind, population_total, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), j AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'japanese'), f AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'foreign'), ranked AS (SELECT t.area_code, ROW_NUMBER() OVER (ORDER BY ROUND(100.0 * t.net_change / (t.population_total - t.net_change), 2) ASC, t.municipality_name) AS rn FROM t WHERE t.population_total - t.net_change >= 10000) SELECT COUNT(*) AS municipalities, SUM(CASE WHEN f.net_change > 0 THEN 1 ELSE 0 END) AS foreign_rose, SUM(f.net_change) AS foreign_gain, SUM(j.net_change) AS japanese_loss FROM ranked r JOIN j USING (area_code) JOIN f USING (area_code) WHERE r.rn <= 20
```

```sql id=decline_all_sizes
WITH m AS (SELECT area_code, municipality_name, resident_kind, population_total, net_change FROM e_stat.resident_registry.population WHERE area_level = 'municipality' AND year = 2026), leaf AS (SELECT DISTINCT a.area_code FROM m a WHERE a.municipality_name <> '島しょ' AND NOT EXISTS (SELECT 1 FROM m b WHERE b.municipality_name <> a.municipality_name AND starts_with(b.municipality_name, a.municipality_name))), t AS (SELECT m.* FROM m JOIN leaf USING (area_code) WHERE m.resident_kind = 'total'), ranked AS (SELECT t.municipality_name AS name, t.population_total - t.net_change AS previous_population, ROUND(100.0 * t.net_change / (t.population_total - t.net_change), 2) AS change_pct FROM t WHERE t.population_total - t.net_change > 0 ORDER BY change_pct ASC, name LIMIT 20) SELECT COUNT(*) AS municipalities, SUM(CASE WHEN previous_population < 10000 THEN 1 ELSE 0 END) AS under_10000, MIN(change_pct) AS worst_pct, ARG_MIN(name, change_pct) AS worst_name FROM ranked
```
