---
title: 新しく建つ家100戸に対して、取り壊される家は12.5戸
description: 2000年度から2024年度の25年間に取り壊された住宅は、新しく着工された住宅100戸あたり全国で12.5戸でした。都道府県別では福岡県の7.0戸から島根県の33.0戸まで差があります。全国の空き家は2023年に900万戸を超えています。
ogDescription: 2000年度から2024年度に取り壊された住宅は、新しく着工された住宅100戸あたり全国で12.5戸、都道府県別では7.0戸から33.0戸でした。
publishedAt: 2026-08-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 空き家
  - 住宅着工
  - 都道府県格差
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系 Ｈ 居住
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010108
    publisher: 総務省統計局
  - title: 建築動態統計調査
    url: https://www.mlit.go.jp/statistics/details/t-other-2_tk_000214.html
    publisher: 国土交通省
  - title: 住宅・土地統計調査
    url: https://www.stat.go.jp/data/jyutaku/index.html
    publisher: 総務省統計局
agentHint: e_stat.ssds.h_pref_housing の着工新設住宅戸数（H1800）と除却住宅戸数（H1901）を、自分の県について2000年度から2024年度まで年ごとに出して。着工100戸あたりの除却戸数も年ごとに計算して、隣の県と並べて
socialAnnounce: |-
  住宅の着工と取り壊しを都道府県別に25年分並べました。

  新築100戸あたりの取り壊しは全国12.5戸、県により7戸から33戸です。
  空き家対策の計画づくりに使えます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2000年度から2024年度までの25年間に、全国で着工された住宅は2,453.7万戸、取り壊された住宅は307.7万戸でした。新しく建った住宅100戸に対して、取り壊された住宅は12.5戸です。都道府県別では、最も多い島根県が33.0戸、最も少ない福岡県が7.0戸で、4.7倍の差があります。全国の空き家は2023年に900.2万戸になりました。

空き家の数は、住宅が増える速さと減る速さの差で決まります。新設住宅の着工戸数は毎月公表され、景気の指標としてよく使われますが、取り壊された住宅の戸数が取り上げられることは多くありません。この記事では、e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010108)に収められた居住分野のデータを使い、全国と47都道府県について、着工された住宅と取り壊された住宅の戸数を集計します。

## 25年間の累計で、着工100戸に対して取り壊しは12.5戸

e-Stat「社会・人口統計体系」の都道府県別の居住データ（`h_pref_housing`）を使います。住宅の出入りに関わる項目は次の4つです。

| コード | 内容             |
| ------ | ---------------- |
| H1800  | 着工新設住宅戸数 |
| H1900  | 滅失住宅戸数     |
| H1901  | 除却住宅戸数     |
| H1902  | 災害住宅戸数     |

着工新設住宅戸数（`H1800`）は国土交通省の[建築動態統計調査](https://www.mlit.go.jp/statistics/details/t-other-2_tk_000214.html)のうち建築着工統計調査によるもので、新築・増築・改築で住宅の戸が新たにつくられた工事の戸数です。滅失住宅戸数（`H1900`）は同じ調査の建築物滅失統計調査によるもので、老朽化や道路拡幅などで取り壊された除却住宅戸数（`H1901`）と、火災・風水害・地震で失われた災害住宅戸数（`H1902`）の合計です。

以下では、災害を含まない除却住宅戸数（`H1901`）を取り壊しの戸数として扱います。[項目の定義](https://www.e-stat.go.jp/koumoku/koumoku_teigi/H)によれば、除却の届出は建築基準法第15条にもとづくもので、床面積が10平方メートル以内の工事では届け出が要らないので、そうした小さな取り壊しはこの戸数に含まれません。着工・除却とも年度の値で、除却の収録は2000年度から始まります。

```chart
{
  "layer": [
    {
      "data": {"name": "flow"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"starts_man\"]) ? 0 : 1",
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
          {"field": "starts_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "starts_man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "戸数（万戸）", "grid": true}
        },
        "color": {
          "datum": "着工新設住宅戸数",
          "type": "nominal",
          "scale": {"domain": ["着工新設住宅戸数", "除却住宅戸数"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "flow"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"removed_man\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "removed_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "removed_man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "戸数（万戸）", "grid": true}
        },
        "color": {
          "datum": "除却住宅戸数",
          "type": "nominal",
          "scale": {"domain": ["着工新設住宅戸数", "除却住宅戸数"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

2000年度は121.3万戸が着工され、19.3万戸が取り壊されました。2024年度は着工81.6万戸に対して取り壊し10.1万戸です。25年間のどの年度でも、取り壊しは着工を大きく下回っています。

25年間の累計では、着工が2,453.7万戸、取り壊しが307.7万戸でした。新しく建った住宅100戸に対して、取り壊された住宅は12.5戸です。

着工はこの25年で32.7%減り、取り壊しは47.8%減っています。

## 着工が減っても、空き家は2008年の756.8万戸から2023年の900.2万戸へ増えた

空き家の数を1978年から並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "vacancy"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "vacant_man", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "調査年", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "vacant_man",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家数（万戸）", "grid": true}
        }
      }
    }
  ]
}
```

空き家は1978年の267.9万戸から2023年の900.2万戸へ、45年で3.4倍になりました。2000年度以降で着工が最も多かった2006年度と比較すると、2024年度の着工は36.5%少なくなっていますが、その間も空き家は2008年の756.8万戸から2023年の900.2万戸へ増えています。この空き家数は5年ごとの[住宅・土地統計調査](https://www.stat.go.jp/data/jyutaku/index.html)によるもので、そのままでは生活を営めない廃屋は住宅として数えていません。

## 着工100戸あたりの取り壊しは、福岡県の7.0戸から島根県の33.0戸まで4.7倍の差がある

2000年度から2024年度までの累計で、着工100戸あたりの除却戸数を47都道府県について計算しました。上位10県を濃い赤、中間の27都道府県を薄い赤、下位10都府県をグレーで示しています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工100戸あたりの除却戸数（戸）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工100戸あたりの除却戸数（戸）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#ef4444", "#fca5a5", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "ratio", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "着工100戸あたりの除却戸数（戸）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
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

最も多いのは島根県で33.0戸、大分県27.9戸、山形県26.6戸が続きます。最も少ないのは福岡県の7.0戸で、沖縄県8.0戸、大阪府8.7戸が続きます。最も多い県と最も少ない県では4.7倍の差があります。

上位10県は、いずれもこの25年で人口が減っています。下位10都府県は、人口が増えた6都県と、人口が減った佐賀県・石川県・京都府・大阪府の4府県です。

## 空き家率が高い県でも、取り壊しが多いとは限らない

横軸に2023年の空き家率、縦軸に着工100戸あたりの除却戸数を取り、点の色を2000年から2024年の人口の増減で塗り分けました。赤いほど人口が減った県です。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "filled": true, "size": 121},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "vacancy_rate", "type": "quantitative"},
          {"field": "ratio", "type": "quantitative"}
        ],
        "x": {
          "field": "vacancy_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "空き家率（2023年・%）", "grid": true}
        },
        "y": {
          "field": "ratio",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "着工100戸あたりの除却戸数（戸）", "grid": true}
        },
        "color": {
          "field": "pop_change",
          "type": "quantitative",
          "scale": {"scheme": "redyellowblue"}
        }
      }
    }
  ]
}
```

空き家率が高い県ほど取り壊しがやや多い傾向はありますが、ばらつきが大きく、空き家率だけでは取り壊しの多さは決まりません。空き家率が全国で2番目に高い和歌山県（21.2%）の除却は14.8戸で、空き家率が下から11番目の山形県（13.5%）の26.6戸を下回ります。

人口が減った県（赤い点）は、取り壊しが多い側に多くあります。例外もあり、鹿児島県は人口が14.2%減り空き家率も20.5%と高いのに、除却は12.0戸で全国平均を下回ります。人口が17.5%増えた東京都は10.3戸、人口が7.0%減った石川県は9.5戸で、ほぼ同じ水準です。空き家率は2023年10月1日時点の値で、除却戸数は2000年度から2024年度までの累計です。

## 業務での使い方

- 担当する県の位置を、着工100戸あたりの除却戸数で確認する。空き家率が近い県でも取り壊しの水準は異なるので、参考にする他県はこの戸数で選ぶ
- 県単位で除却戸数の年次推移を出し、解体費の補助制度を始めた年度の前後で戸数が変わったかを確認する
- 着工戸数と合わせて、地域で行われている解体工事の規模を見積もる。届出の要らない小規模な取り壊しは含まれないので、実際の戸数はこれ以上になる

## データの出典

本記事は e-Stat の[社会・人口統計体系](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010108)から、居住分野と人口・世帯分野の都道府県別データを2026年8月25日時点で取得して集計しています。着工新設住宅戸数と除却住宅戸数は国土交通省の[建築動態統計調査](https://www.mlit.go.jp/statistics/details/t-other-2_tk_000214.html)、空き家数と総住宅数は総務省の[住宅・土地統計調査](https://www.stat.go.jp/data/jyutaku/index.html)、総人口は国勢調査と人口推計が元データです。着工と除却は年度の値、空き家数と総住宅数は調査年10月1日時点の値です。

Queriaは、社会・人口統計体系の都道府県別データを、列名・単位・文字コードを統一し、都道府県や年度で結合できる形にして、テーブルと列の説明を付けて公開しています。本記事で使った[居住テーブル](/datasets/queria/e_stat/ssds/h_pref_housing)から、担当する県の除却戸数を年ごとに確認したり、[人口・世帯テーブル](/datasets/queria/e_stat/ssds/a_pref_population)と結合して世帯数の推移と並べたりできます。

```sql id=flow
SELECT year, SUM(CASE WHEN cat01 = 'H1800' THEN TRY_CAST(value AS DOUBLE) END) / 10000 AS starts_man, SUM(CASE WHEN cat01 = 'H1901' THEN TRY_CAST(value AS DOUBLE) END) / 10000 AS removed_man FROM e_stat.ssds.h_pref_housing WHERE area_name = '全国' AND cat01 IN ('H1800', 'H1901') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2024 GROUP BY year ORDER BY year
```

```sql id=vacancy
SELECT year, SUM(TRY_CAST(value AS DOUBLE)) / 10000 AS vacant_man FROM e_stat.ssds.h_pref_housing WHERE area_name = '全国' AND cat01 = 'H110202' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=pref_top
WITH agg AS (SELECT area_name, SUM(CASE WHEN cat01 = 'H1800' THEN TRY_CAST(value AS DOUBLE) END) AS starts, SUM(CASE WHEN cat01 = 'H1901' THEN TRY_CAST(value AS DOUBLE) END) AS removed FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND cat01 IN ('H1800', 'H1901') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2024 GROUP BY area_name), ranked AS (SELECT area_name, removed / starts * 100 AS ratio, ROW_NUMBER() OVER (ORDER BY removed / starts * 100 DESC, area_name) AS rn FROM agg) SELECT area_name, ratio FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH agg AS (SELECT area_name, SUM(CASE WHEN cat01 = 'H1800' THEN TRY_CAST(value AS DOUBLE) END) AS starts, SUM(CASE WHEN cat01 = 'H1901' THEN TRY_CAST(value AS DOUBLE) END) AS removed FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND cat01 IN ('H1800', 'H1901') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2024 GROUP BY area_name), ranked AS (SELECT area_name, removed / starts * 100 AS ratio, ROW_NUMBER() OVER (ORDER BY removed / starts * 100 DESC, area_name) AS rn FROM agg) SELECT area_name, ratio FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH agg AS (SELECT area_name, SUM(CASE WHEN cat01 = 'H1800' THEN TRY_CAST(value AS DOUBLE) END) AS starts, SUM(CASE WHEN cat01 = 'H1901' THEN TRY_CAST(value AS DOUBLE) END) AS removed FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND cat01 IN ('H1800', 'H1901') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2024 GROUP BY area_name), ranked AS (SELECT area_name, removed / starts * 100 AS ratio, ROW_NUMBER() OVER (ORDER BY removed / starts * 100 DESC, area_name) AS rn FROM agg) SELECT area_name, ratio FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=scatter
WITH agg AS (SELECT area_name, SUM(CASE WHEN cat01 = 'H1800' THEN TRY_CAST(value AS DOUBLE) END) AS starts, SUM(CASE WHEN cat01 = 'H1901' THEN TRY_CAST(value AS DOUBLE) END) AS removed FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND cat01 IN ('H1800', 'H1901') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2024 GROUP BY area_name), vac AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vacant, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS total FROM e_stat.ssds.h_pref_housing WHERE area_name <> '全国' AND cat01 IN ('H110202', 'H1100') AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), pop AS (SELECT area_name, MAX(CASE WHEN year = 2000 THEN TRY_CAST(value AS DOUBLE) END) AS p2000, MAX(CASE WHEN year = 2024 THEN TRY_CAST(value AS DOUBLE) END) AS p2024 FROM e_stat.ssds.a_pref_population WHERE area_name <> '全国' AND cat01 = 'A1101' AND year IN (2000, 2024) AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT agg.area_name, vac.vacant / vac.total * 100 AS vacancy_rate, agg.removed / agg.starts * 100 AS ratio, (pop.p2024 / pop.p2000 - 1) * 100 AS pop_change FROM agg JOIN vac ON agg.area_name = vac.area_name JOIN pop ON agg.area_name = pop.area_name ORDER BY vacancy_rate
```
