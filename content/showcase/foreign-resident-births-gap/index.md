---
title: 外国人が同じ数だけ住む町でも、1年に生まれる子どもの数は8倍違う
description: 住民基本台帳で外国人住民の人口・世帯数・出生数を市区町村別に追いました。2026年時点で、外国人が4,000人規模住む町でも1年間の出生数は6人から52人まで開いています。
publishedAt: 2026-09-04
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 外国人住民
  - 住民基本台帳
  - 出生
datasets:
  - queria/e_stat
  - queria/soumu
sources:
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
  - title: 在留資格から探す
    url: https://www.moj.go.jp/isa/applications/status/index.html
    publisher: 出入国在留管理庁
agentHint: 外国人住民の1世帯あたりの人数と1,000人あたり出生数を、自分の都道府県の市区町村について2014年から2026年まで出して。単身が増えているのか世帯が増えているのかを比べて
socialAnnounce: |-
  住民基本台帳の市区町村別データから、外国人住民の人口・世帯数・出生数を2014年以降で追いました。

  保育や学校の需要見積もり、住まいの計画に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

外国人住民が3,000人から5,000人いる市区町村で、2026年の集計で直前1年間に外国人住民として登録された新生児の数を比較すると、群馬県館林市は外国人住民4,456人に対して52人、北海道倶知安町は4,279人に対して6人で、8倍以上の差がありました。外国人住民1,000人あたりの年間出生数は、都道府県別でも群馬県の8.3人から青森県の1.6人まで約5倍の差があり、この差は2014年から12年間縮まっていません。

外国人住民が増えている自治体では、保育所の枠や日本語指導の体制を増やすのか、単身者向けの住まいや生活相談の窓口を増やすのかを、年度ごとに決める必要があります。どちらが必要かは、増えた人数だけでは判断できません。この記事では、総務省の[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)を使い、外国人住民の人口に加えて、世帯数と、その地域で生まれた子どもの数を集計します。

## 全国で増えた203万人は、ほとんどが1人だけの世帯

このデータは、毎年1月1日時点の人口と世帯数、およびその直前1年間の出生・死亡・転入・転出を、全国・都道府県・市区町村の単位で収めています。住民区分（`resident_kind`）は3つに分かれます。

| 区分     | 内容       |
| -------- | ---------- |
| total    | 総計       |
| japanese | 日本人住民 |
| foreign  | 外国人住民 |

ここでは外国人住民（`foreign`）だけを使います。外国人住民が住民基本台帳の対象になったのは2012年7月で、日本人と分けて集計できるのは2013年以降です。調査期日が1月1日に統一され、出生数が1月から12月までの1年間を表すようになるのは2014年からです。全国の外国人住民の人口と世帯数を年ごとに集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "pop",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": null, "grid": true}
        },
        "color": {
          "datum": "人口（人）",
          "type": "nominal",
          "scale": {"domain": ["人口（人）", "世帯数（世帯）"], "range": ["#3b82f6", "#f97316"]},
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
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"hh\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "hh", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "hh",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": null, "grid": true}
        },
        "color": {
          "datum": "世帯数（世帯）",
          "type": "nominal",
          "scale": {"domain": ["人口（人）", "世帯数（世帯）"], "range": ["#3b82f6", "#f97316"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

外国人住民は2014年の2,003,379人から2026年の4,031,159人へ、およそ2.0倍になりました。途中の2021年と2022年は人口も世帯数も前年を下回っていて、12年通しての倍率はこの落ち込みを挟んだ値です。同じ期間に世帯数は1,000,252世帯から2,615,996世帯へ、およそ2.6倍です。世帯数は人口より速く増えています。増えた人口2,027,780人を増えた世帯数1,615,744世帯で割ると1.26人で、この12年で増えた住民の多くは1人で世帯を構えていたことになります。1世帯あたりの人数は2.00人から1.54人に下がりました。

この世帯数は、外国人住民だけで構成される世帯を数えたものです。日本人と同居する世帯は日本人住民の区分に入るため、日本人と結婚して暮らす人が多い地域では、1世帯あたりの人数がその分だけ大きく出ます。

## 外国人住民1,000人あたりの出生数は、群馬県の8.3人から青森県の1.6人まで約5倍違う

出生数（`births`）は、前年の1月から12月までに住民票へ記載された出生者の数です。外国人住民の区分では、外国人として住民登録された新生児が含まれます。人口規模の違う県を比較するため、外国人住民1,000人あたりの年間出生数を求めました。分母は全年齢・男女あわせた外国人住民の数なので、この値には20代・30代の住民の割合の違いも含まれます。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "外国人住民1,000人あたりの年間出生数（人）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "外国人住民1,000人あたりの年間出生数（人）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "外国人住民1,000人あたりの年間出生数（人）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も多いのは群馬県で、外国人住民1,000人あたり8.3人です。島根県7.8人、埼玉県7.5人、千葉県7.2人、愛知県7.1人が続きます。最も少ないのは青森県の1.6人で、高知県2.0人、岩手県と鹿児島県が2.3人、新潟県2.4人と続きます。最も多い県と最も少ない県では約5倍の差があります。上位10県のうち島根県を除く9県は、北関東・首都圏・東海の県です。島根県は外国人住民11,437人・出生数89人で、上位10県のなかでどちらも最も少なく、出生数が18人減ると10位の栃木県を下回ります。

## 上位10県と下位10県の差は、12年間で2.1倍から2.6倍に広がった

2026年に1,000人あたりの出生数が多い上位10県と少ない下位10県について、2014年までさかのぼって集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "top_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人住民1,000人あたりの年間出生数（人）", "grid": true}
        },
        "color": {
          "datum": "上位10県",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "下位10県"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bottom_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人住民1,000人あたりの年間出生数（人）", "grid": true}
        },
        "color": {
          "datum": "下位10県",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "下位10県"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

上位10県は2014年に1,000人あたり8.01人、2026年に6.98人です。下位10県は3.90人から2.69人でした。期間中の最高は上位が2017年の8.99人、下位が2015年の4.30人で、どちらも2026年はそれを下回っています。12年を通じて、上位10県は毎年、下位10県の2倍を超えています。2014年は2.1倍、2026年は2.6倍です。

下位10県の外国人住民は、この12年で76,085人から194,856人へ2.6倍に増えました。一方で、年間の出生数は297人から525人です。上位10県は同じ期間に808,928人から1,636,948人へ2.0倍に増え、出生数は6,476人から11,428人になりました。外国人住民は下位10県のほうが速く増えていますが、出生数はそれほど増えていません。

## 外国人住民が4,000人規模の町でも、1年に生まれる子どもの数は6人から52人まで8倍違う

県の平均には、県内の市区町村の差は表れません。外国人住民が3,000人から5,000人いる104市区町村に絞り、1世帯あたりの人数と出生数の関係を集計しました。市区町村の集計では、政令指定都市を1団体として数え、行政区を二重に数えないように標準地域コードで絞っています。

```chart
{
  "layer": [
    {
      "data": {"name": "band"},
      "mark": {"type": "point", "color": "#ec4899", "opacity": 0.7, "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "per_hh", "type": "quantitative"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "per_hh",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人住民の1世帯あたり人数（人）", "grid": true}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "外国人住民1,000人あたりの年間出生数（人）", "grid": true}
        }
      }
    }
  ]
}
```

1世帯あたりの人数が大きい市区町村ほど、出生数も多くなる傾向があります。1世帯あたり1.4人未満の13市区町村では、外国人住民1,000人あたりの出生数は平均3.6人。1.7人以上の21市区町村では平均7.0人で、およそ2倍です。1世帯あたりが1.55人から1.65人の34市区町村だけでも、1,000人あたりの出生数は武蔵野市の2.3人から大府市の10.0人まで差があり、出生数は世帯の人数だけでは決まりません。

最も出生数が多いのは群馬県館林市で、外国人住民4,456人に対して1年間に52人が生まれています。最も少ないのは北海道倶知安町で、4,279人に対して6人でした。1世帯あたりの人数は館林市が1.72人、倶知安町が1.08人です。

[在留資格](https://www.moj.go.jp/isa/applications/status/index.html)によって家族を呼び寄せられるかどうかが違うことが、この差の背景にあると考えられます。技能実習や特定技能1号では原則として家族の帯同ができず、定住者や永住者ではできます。技能実習や特定技能1号の住民が多い地域では単身の住民が多くなり、定住者や永住者が多い地域では家族で暮らす住民が多くなると考えられます。このデータには在留資格の列がないので、地域ごとの在留資格の内訳はこの集計では確認していません。

## 業務での使い方

- 自分の自治体について、人口・世帯数・出生数を並べる。人口の伸びに対して世帯数の伸びが大きければ、増えているのは単身の住民で、保育所や小学校の需要はすぐには動きません
- 1世帯あたりの人数が近い自治体を全国から検索し、その自治体で数年後に出生数がどう変わったかを確認する。自分の自治体がこれからどちらに向かうかの目安になります
- 転入者数（`moved_in_total`）・転出者数（`moved_out_total`）も集計する。単身の住民が多い地域は転入と転出が多く、総数が横ばいでも毎年多くの住民が入れ替わっていることがあります

## データの出典

本記事は総務省「[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)」の全国・都道府県・市区町村別データを、2026年9月4日時点で集計しています。人口と世帯数は各年1月1日現在、出生数は前年1月から12月までの1年間の値です。

Queriaは、年次ごとに分かれて公表されている住民基本台帳の集計を、列名・単位・地域コードを統一した1つのテーブルにして公開しています。本記事で使った[住民基本台帳人口テーブル](/datasets/queria/e_stat/resident_registry/population)から、自分の自治体の人口・世帯数・出生数を年ごとに確認したり、近隣の自治体と比較したりできます。

```sql id=national
SELECT year, population_total AS pop, households AS hh, ROUND(population_total::DOUBLE / households, 3) AS per_hh, births, ROUND(births * 1000.0 / population_total, 2) AS birth_rate FROM e_stat.resident_registry.population WHERE area_level = 'national' AND resident_kind = 'foreign' AND year >= 2014 AND year <= 2026 ORDER BY year
```

```sql id=pref_top
WITH ranked AS (SELECT pref_name, population_total AS pop, births, ROUND(births * 1000.0 / population_total, 1) AS rate, ROW_NUMBER() OVER (ORDER BY births * 1000.0 / population_total DESC, pref_name) AS rn FROM e_stat.resident_registry.population WHERE year = 2026 AND resident_kind = 'foreign' AND area_level = 'prefecture') SELECT pref_name, pop, births, rate FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH ranked AS (SELECT pref_name, population_total AS pop, births, ROUND(births * 1000.0 / population_total, 1) AS rate, ROW_NUMBER() OVER (ORDER BY births * 1000.0 / population_total DESC, pref_name) AS rn FROM e_stat.resident_registry.population WHERE year = 2026 AND resident_kind = 'foreign' AND area_level = 'prefecture') SELECT pref_name, pop, births, rate FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH ranked AS (SELECT pref_name, population_total AS pop, births, ROUND(births * 1000.0 / population_total, 1) AS rate, ROW_NUMBER() OVER (ORDER BY births * 1000.0 / population_total DESC, pref_name) AS rn FROM e_stat.resident_registry.population WHERE year = 2026 AND resident_kind = 'foreign' AND area_level = 'prefecture') SELECT pref_name, pop, births, rate FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=top_trend
WITH r AS (SELECT pref_name, ROW_NUMBER() OVER (ORDER BY births * 1000.0 / population_total DESC, pref_name) AS rn FROM e_stat.resident_registry.population WHERE year = 2026 AND resident_kind = 'foreign' AND area_level = 'prefecture') SELECT p.year, SUM(p.population_total) AS pop, SUM(p.births) AS births, ROUND(SUM(p.births) * 1000.0 / SUM(p.population_total), 2) AS rate FROM e_stat.resident_registry.population p JOIN r ON r.pref_name = p.pref_name WHERE r.rn <= 10 AND p.area_level = 'prefecture' AND p.resident_kind = 'foreign' AND p.year >= 2014 AND p.year <= 2026 GROUP BY p.year ORDER BY p.year
```

```sql id=bottom_trend
WITH r AS (SELECT pref_name, ROW_NUMBER() OVER (ORDER BY births * 1000.0 / population_total DESC, pref_name) AS rn FROM e_stat.resident_registry.population WHERE year = 2026 AND resident_kind = 'foreign' AND area_level = 'prefecture') SELECT p.year, SUM(p.population_total) AS pop, SUM(p.births) AS births, ROUND(SUM(p.births) * 1000.0 / SUM(p.population_total), 2) AS rate FROM e_stat.resident_registry.population p JOIN r ON r.pref_name = p.pref_name WHERE r.rn > 37 AND p.area_level = 'prefecture' AND p.resident_kind = 'foreign' AND p.year >= 2014 AND p.year <= 2026 GROUP BY p.year ORDER BY p.year
```

```sql id=band
SELECT p.municipality_name AS name, m.pref_name, p.population_total AS pop, p.households AS hh, p.births, ROUND(p.population_total::DOUBLE / p.households, 2) AS per_hh, ROUND(p.births * 1000.0 / p.population_total, 1) AS rate FROM e_stat.resident_registry.population p JOIN soumu.code.municipality m ON m.area_code = p.area_code AND m.is_municipality WHERE p.year = 2026 AND p.resident_kind = 'foreign' AND p.area_level = 'municipality' AND p.population_total BETWEEN 3000 AND 5000 ORDER BY rate DESC, name
```
