---
title: 2025年の国勢調査の人口は、5年前に国が出した将来推計を、47都道府県のうち40で下回った
description: 2020年の国勢調査をもとにした将来推計と2025年の国勢調査を比較しました。全国の人口は見通しより28万9,924人少なく、推計の2020年の人口が国勢調査と一致する1,130市区町村のうち751で見通しを下回りました。
publishedAt: 2026-11-03
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 国勢調査
  - 将来推計人口
  - 人口ビジョン
  - 総合計画
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 令和7年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2025/index.html
    publisher: 総務省統計局
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 国土数値情報 1kmメッシュ別将来推計人口（R6国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html
    publisher: 国土交通省
  - title: 日本の地域別将来推計人口（令和5年推計）
    url: https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp
    publisher: 国立社会保障・人口問題研究所
agentHint: 2020年の国勢調査をもとにした将来推計の2025年の増減率と、2025年国勢調査の実際の増減率の差を、自分の県の市町村ごとに出して。推計の2020年の人口が国勢調査と2%以上違う市町村は除いて、男女比の2020年から2025年への変化も並べて
socialAnnounce: |-
  2025年の国勢調査の人口は、5年前の国の将来推計より全国で28万9,924人少なく、47都道府県のうち40で推計を下回りました。

  人口ビジョンや総合計画の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2025年の国勢調査の全国の人口は、2020年の国勢調査から作られた将来推計の見通しより28万9,924人少なく、47都道府県のうち40道府県で見通しを下回りました。比較できる1,130市区町村のうち751団体、およそ3分の2も見通しを下回っています。7割の団体では見通しとの差が2ポイント以内に収まり、10ポイント以上外れた町もあります。人口5,000人以上で見通しから4ポイント以上外れた団体では、およそ3割で女性100人あたりの男性の数が5年で3以上変わっていました。この変化は、外れた理由が働く人の一時的な転入・転出かどうかを判断する材料になります。

市町村の人口ビジョンや総合計画は、国立社会保障・人口問題研究所（社人研）が国勢調査の人口をもとに出す将来推計を前提にしています。いま使われている推計は2020年の国勢調査から作られたもので、2025年の人口の見通しも含んでいます。2025年の国勢調査の結果が公表されたので、この見通しと実際の人口を全国の市区町村について比較しました。

## 全国の人口は、見通しより28万9,924人少なかった

使うのは2つのデータです。1つは総務省統計局の[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)の人口等基本集計（`census_municipality_2025`）で、2025年10月1日現在の市区町村ごとの人口と、2020年の人口を2025年の市区町村の区域に組み替えた値を持っています。もう1つは国土交通省の[国土数値情報 1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を市区町村ごとに集計した表（`future_population_municipality`）です。この推計は2020年の国勢調査と社人研の[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)にもとづいていて、2020年から2070年まで5年ごとの人口を持っています。ここではその2025年の値を「見通し」と呼びます。

比較するのは2020年から2025年への増減率です。見通しの増減率は推計の2025年の値を推計の2020年の値で割って、実際の増減率は2025年の国勢調査の人口を2020年の人口で割って出しました。2つの差（ポイント）がマイナスなら、実際の人口は見通しより速く減ったことになります。

全国では、見通しの増減率が -2.29% だったのに対し、実際は -2.52% でした。2025年の人口は見通しの1億2,326万2,452人に対して1億2,297万2,528人です。下の図は、都道府県ごとに見通しの増減率（横軸）と実際の増減率（縦軸）を並べたもので、斜めの線より下にある県は見通しより速く減っています。

```chart caption="都道府県別の人口増減率（2020→2025年）。見通しと実際"
{
  "layer": [
    {
      "data": {"values": [{"x": -8.5, "y": -8.5}, {"x": 1.5, "y": 1.5}]},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"x\"]) && isValid(datum[\"y\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 1,
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "x": {
          "field": "x",
          "type": "quantitative",
          "scale": {"domain": [-8.5, 1.5], "zero": false, "nice": false},
          "axis": {"title": "見通しの増減率（%）", "grid": true}
        },
        "y": {
          "field": "y",
          "type": "quantitative",
          "scale": {"domain": [-8.5, 1.5], "zero": false, "nice": false},
          "axis": {"title": "実際の増減率（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "pref"},
      "mark": {"type": "point", "color": "#3b82f6", "opacity": 0.8, "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "projected_rate", "type": "quantitative"},
          {"field": "actual_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "projected_rate",
          "type": "quantitative",
          "scale": {"domain": [-8.5, 1.5], "zero": false, "nice": false},
          "axis": {"title": "見通しの増減率（%）", "grid": true}
        },
        "y": {
          "field": "actual_rate",
          "type": "quantitative",
          "scale": {"domain": [-8.5, 1.5], "zero": false, "nice": false},
          "axis": {"title": "実際の増減率（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_label"},
      "mark": {"type": "text", "align": "left", "dx": 6, "fontSize": 11, "color": "#64748b"},
      "encoding": {
        "x": {
          "field": "projected_rate",
          "type": "quantitative",
          "scale": {"domain": [-8.5, 1.5], "zero": false, "nice": false},
          "axis": {"title": "見通しの増減率（%）", "grid": true}
        },
        "y": {
          "field": "actual_rate",
          "type": "quantitative",
          "scale": {"domain": [-8.5, 1.5], "zero": false, "nice": false},
          "axis": {"title": "実際の増減率（%）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

見通しを最も大きく下回ったのは島根県で、見通しの -4.70% に対して実際は -6.29%、差は -1.60 ポイントでした。青森県（-1.41 ポイント）、岡山県（-1.33 ポイント）が続きます。見通しを上回ったのは7都府県で、最も大きいのは大阪府の +0.94 ポイントです。見通しでは -1.83% だった減少が、実際には -0.89% にとどまりました。沖縄県（+0.31 ポイント）、東京都（+0.27 ポイント）が続きます。

## 市区町村の3分の2は見通しを下回り、7割は差が2ポイント以内

市区町村ごとに同じ比較をします。推計の表は、1kmメッシュの人口を市区町村に割り振って集計した値で、複数の市区町村にまたがるメッシュは均等に分けています。そのため推計の2020年の人口が国勢調査とずれる団体があり、ずれが2%以内に収まるのは、国勢調査と市区町村コードで照合できる1,876団体（政令指定都市は区ごと）のうち1,130団体です。以下はこの1,130団体の比較で、残る746団体は入っていません。政令指定都市の区と東京23区は合わせて191のうち57しか残りません。

```chart caption="見通しと実際の人口増減率の差（2020→2025年、1,130市区町村）"
{
  "layer": [
    {
      "data": {"name": "muni_comparable"},
      "transform": [{"filter": {"field": "gap", "range": [-8, 6]}}],
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "x": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "実際 − 見通し（ポイント）"},
          "bin": {"step": 0.5, "extent": [-8, 6]}
        },
        "y": {
          "aggregate": "count",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 0, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    }
  ]
}
```

1,130団体のうち751団体（66.5%）で、実際の増減率が見通しを下回りました。差の中央値は -0.67 ポイントで、差が ±2 ポイント以内の団体は803（71.1%）、9割の団体は -4.01 から +2.68 ポイントの間に収まります。図の横軸は -8 から +6 ポイントで切っていて、その外側に23団体があります。そのうち見通しから10ポイント以上外れたのは7団体です。

## 大きく下回った側には奥能登の市町、上回った側には大都市の中心部と北海道・青森の町村

人口5,000人以上の団体のうち、見通しを大きく下回った10団体と大きく上回った10団体を並べます。

```chart caption="見通しと実際の人口増減率の差が大きい市区町村（2020年の人口5,000人以上）"
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "extremes_below"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "gap", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "実際 − 見通し（ポイント）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "見通しを下回った",
          "type": "nominal",
          "scale": {"domain": ["見通しを下回った", "見通しを上回った"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "extremes_above"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "gap", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "gap",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "実際 − 見通し（ポイント）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "見通しを上回った",
          "type": "nominal",
          "scale": {"domain": ["見通しを下回った", "見通しを上回った"], "range": ["#ef4444", "#3b82f6"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

最も大きく下回ったのは石川県珠洲市で、見通しは5年で -12.78% でしたが、実際は -34.57% と人口の3分の1を失い、差は -21.79 ポイントです。輪島市も -14.56 ポイント、穴水町は -7.74 ポイント、能登町は -6.30 ポイントで、下回った10団体のうち4つを、能登半島地震の被害を受けた奥能登の市町が占めます。

上回った側の先頭は北海道長万部町で、見通しは -8.94% でしたが実際は +3.84% と人口が増え、差は +12.78 ポイントでした。大阪市浪速区（+11.77 ポイント）や名古屋市東区（+4.71 ポイント）のような大都市の中心部、つくば市（+5.94 ポイント）のほか、青森県六ヶ所村（+6.80 ポイント）、北海道ニセコ町（+5.16 ポイント）が並びます。

## 大きく外れた町では、女性100人あたりの男性の数が大きく変わっていた

国勢調査は、女性100人に対する男性の数（人口性比）も公表しています。上の20団体について、2020年と2025年の値を並べました。

```chart caption="女性100人あたりの男性の数（2020年と2025年）"
{
  "height": 580,
  "layer": [
    {
      "data": {"name": "sex_ratio_segments"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"x\"]) && isValid(datum[\"y\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#cbd5e1",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "x": {
          "field": "x",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性100人あたりの男性の数", "grid": true}
        },
        "y": {"field": "y", "type": "nominal", "axis": {"title": null}, "sort": null},
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "extremes"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "sex_ratio_2020", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "sex_ratio_2020",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性100人あたりの男性の数", "grid": true}
        },
        "y": {"field": "label", "type": "nominal", "axis": {"title": null}, "sort": null},
        "color": {
          "datum": "2020年",
          "type": "nominal",
          "scale": {"domain": ["2020年", "2025年"], "range": ["#94a3b8", "#7c3aed"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "extremes"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "sex_ratio_2025", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "sex_ratio_2025",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性100人あたりの男性の数", "grid": true}
        },
        "y": {"field": "label", "type": "nominal", "axis": {"title": null}, "sort": null},
        "color": {
          "datum": "2025年",
          "type": "nominal",
          "scale": {"domain": ["2020年", "2025年"], "range": ["#94a3b8", "#7c3aed"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

珠洲市は84.8から101.1へ、輪島市は90.8から102.4へ上がりました。人口が大きく減るなかで、女性の減り方が男性より大きかったことになります。長万部町は92.0から124.1へ、六ヶ所村は132.6から153.0へ上がっていて、人口が見通しを上回った分の多くは男性の転入だったと考えられます。逆に、佐賀県玄海町は120.7から108.1へ下がり、見通しを10.14ポイント下回りました。男性が多かった町から男性が減ったことになります。

男女比の大きな変化は、見通しから大きく外れた団体に多く見られます。人口5,000人以上で比較できる897団体のうち、見通しとの差が4ポイント未満の860団体では、男女比が5年で3以上動いたのは39団体（4.5%）でした。見通しを4ポイント以上下回った26団体では7団体（26.9%）、4ポイント以上上回った11団体では4団体（36.4%）です。4ポイント以上外れた37団体を合わせると、男女比が3以上動いたのは11団体です。つくば市（100.4から102.6）や名古屋市東区（92.2から91.4）のように、見通しを大きく上回っても男女比の動きが3未満の団体もあります。

## 人口ビジョンを見直すときの確認方法

- 人口ビジョンを改定する担当者は、2030年以降の推計を使う前に、自分の市町村の見通しとの差が全国の分布のどこにあるかを確認する。9割の団体は -4.01 から +2.68 ポイントの間にあり、比較できる団体の3分の2は見通しを下回っています。自分の市町村が見通しを下回っていれば、見通しの2025年人口と実際の人口の差を、2030年以降の推計値を読み替えるときの起点にできます
- 見通しとの差が大きい場合は、担当者が男女比の2020年から2025年への変化を一緒に見る。男性の割合が急に上がって人口が見通しを上回ったなら、工事や工場の立ち上げで働く人が一時的に住んでいることが考えられ、その増加を2030年以降の見通しにそのまま延ばすと人口を多めに見積もることになります

## データの出典

本記事は、総務省統計局の[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)人口等基本集計と[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)人口等基本集計、国土交通省の[国土数値情報 1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を市区町村別に集計した表を、2026-11-03 時点で集計しています。

Queria は、国勢調査と国土数値情報の将来推計を、どちらも同じ5桁の市区町村コードで結合できる形にし、列の意味や単位の説明を付けて公開しています。本記事で使った[2025年国勢調査の市区町村別人口](/datasets/queria/e_stat/census/census_municipality_2025)と[市区町村別の将来推計人口](/datasets/queria/nlftp/population/future_population_municipality)から、自分の市町村の見通しとの差を確認できます。

```sql id=muni
-- 推計（2020年国勢調査ベース）と2025年国勢調査を市区町村ごとに突き合わせる
-- gap = 実際の増減率 − 見通しの増減率（ポイント）
-- base_diff = 推計の2020年人口と国勢調査の2020年人口のずれ（%）
SELECT
  c.area,
  c.area_name,
  c.area_level,
  c.population_2020 AS pop2020,
  c.population AS pop2025,
  CAST(o.sex_ratio AS DOUBLE) AS sex_ratio_2020,
  CAST(c.sex_ratio AS DOUBLE) AS sex_ratio_2025,
  ROUND((c.population / c.population_2020 - 1) * 100, 2) AS actual_rate,
  ROUND((f.population_2025 / f.population_2020 - 1) * 100, 2) AS projected_rate,
  ROUND(((c.population / c.population_2020) - (f.population_2025 / f.population_2020)) * 100, 2) AS gap,
  ABS(f.population_2020 / c.population_2020 - 1) * 100 AS base_diff
FROM nlftp.population.future_population_municipality f
JOIN e_stat.census.census_municipality_2025 c
  ON c.area = f.city_code AND c.area_level IN ('city', 'ward', 'town_village')
JOIN e_stat.census.census_municipality o ON o.area = c.area
```

```sql id=nation
-- 全国の見通しと実際（プロットはしない）
SELECT
  f.p20 AS projected_2020,
  f.p25 AS projected_2025,
  c.population_2020 AS actual_2020,
  c.population AS actual_2025,
  ROUND((f.p25 / f.p20 - 1) * 100, 2) AS projected_rate,
  ROUND((c.population / c.population_2020 - 1) * 100, 2) AS actual_rate,
  f.p25 - c.population AS shortfall
FROM e_stat.census.census_municipality_2025 c
CROSS JOIN (
  SELECT SUM(population_2020) AS p20, SUM(population_2025) AS p25
  FROM nlftp.population.future_population_municipality
) f
WHERE c.area_level = 'national'
```

```sql id=pref
SELECT
  c.area_name,
  ROUND((c.population / c.population_2020 - 1) * 100, 2) AS actual_rate,
  ROUND((f.p25 / f.p20 - 1) * 100, 2) AS projected_rate,
  ROUND(((c.population / c.population_2020) - (f.p25 / f.p20)) * 100, 2) AS gap,
  RANK() OVER (ORDER BY ((c.population / c.population_2020) - (f.p25 / f.p20))) AS rank_below
FROM e_stat.census.census_municipality_2025 c
JOIN (
  SELECT prefecture_code, SUM(population_2020) AS p20, SUM(population_2025) AS p25
  FROM nlftp.population.future_population_municipality
  GROUP BY prefecture_code
) f ON f.prefecture_code = LEFT(c.area, 2)
WHERE c.area_level = 'prefecture'
ORDER BY gap, c.area_name
```

```sql id=pref_label
-- 図に名前を出す県（見通しを下回った上位3と上回った上位3）
SELECT area_name, projected_rate, actual_rate
FROM pref
WHERE rank_below <= 3 OR rank_below >= 45
ORDER BY rank_below
```

```sql id=pref_summary
-- 見通しを下回った都道府県の数（プロットはしない）
SELECT COUNT(*) FILTER (WHERE gap < 0) AS below, COUNT(*) FILTER (WHERE gap > 0) AS above
FROM pref
```

```sql id=muni_coverage
-- 推計の表の団体数と、比べられる団体の数（プロットはしない）
SELECT
  COUNT(*) AS n_all,
  COUNT(*) FILTER (WHERE base_diff <= 2) AS n_comparable,
  COUNT(*) FILTER (WHERE base_diff > 2) AS n_excluded,
  COUNT(*) FILTER (WHERE area_level = 'ward') AS wards_all,
  COUNT(*) FILTER (WHERE area_level = 'ward' AND base_diff <= 2) AS wards_comparable
FROM muni
```

```sql id=muni_comparable
-- 推計の2020年人口が国勢調査と2%以内の団体
SELECT area, area_name, pop2020, gap FROM muni WHERE base_diff <= 2
```

```sql id=muni_summary
-- 比べられる団体の数・見通しを下回った数・差の分布（プロットはしない）
SELECT
  COUNT(*) AS n,
  COUNT(*) FILTER (WHERE gap < 0) AS below,
  ROUND(100.0 * COUNT(*) FILTER (WHERE gap < 0) / COUNT(*), 1) AS below_pct,
  MEDIAN(gap) AS median_gap,
  COUNT(*) FILTER (WHERE ABS(gap) <= 2) AS within2,
  ROUND(100.0 * COUNT(*) FILTER (WHERE ABS(gap) <= 2) / COUNT(*), 1) AS within2_pct,
  ROUND(QUANTILE_CONT(gap, 0.05), 2) AS p05,
  ROUND(QUANTILE_CONT(gap, 0.95), 2) AS p95,
  COUNT(*) FILTER (WHERE gap < -8 OR gap > 6) AS outside_axis,
  COUNT(*) FILTER (WHERE ABS(gap) >= 10) AS over10
FROM muni_comparable
```

```sql id=extremes
-- 人口5,000人以上で、見通しとの差が大きい順に下回り10・上回り10
WITH m AS (
  SELECT
    *,
    ROW_NUMBER() OVER (ORDER BY gap, area) AS rn_below,
    ROW_NUMBER() OVER (ORDER BY gap DESC, area) AS rn_above
  FROM muni
  WHERE base_diff <= 2 AND pop2020 >= 5000
)
SELECT
  area, area_name, gap, actual_rate, projected_rate, sex_ratio_2020, sex_ratio_2025,
  area_name || CASE WHEN gap < 0 THEN '（' ELSE '（+' END || CAST(gap AS VARCHAR) || '）' AS label,
  CASE WHEN rn_below <= 10 THEN 'below' ELSE 'above' END AS side,
  CASE WHEN rn_below <= 10 THEN rn_below ELSE 20 + 1 - rn_above END AS ord
FROM m
WHERE rn_below <= 10 OR rn_above <= 10
ORDER BY ord
```

```sql id=extremes_below
SELECT area_name, gap FROM extremes WHERE side = 'below' ORDER BY gap, area_name
```

```sql id=extremes_above
SELECT area_name, gap FROM extremes WHERE side = 'above' ORDER BY gap, area_name
```

```sql id=sex_ratio_segments
-- ダンベルの線（1団体3行、NULL で線を切る）
SELECT x, y FROM (
  SELECT ord, 1 AS k, sex_ratio_2020 AS x, label AS y FROM extremes
  UNION ALL SELECT ord, 2, sex_ratio_2025, label FROM extremes
  UNION ALL SELECT ord, 3, NULL, NULL FROM extremes
)
ORDER BY ord, k
```

```sql id=sex_ratio_groups
-- 人口5,000人以上で、見通しとの差の大きさ別に男女比が3以上動いた団体の数（プロットはしない）
SELECT
  CASE WHEN gap <= -4 THEN '4ポイント以上下回った' WHEN gap < 4 THEN '差が4ポイント未満' ELSE '4ポイント以上上回った' END AS grp,
  COUNT(*) AS n,
  COUNT(*) FILTER (WHERE ABS(sex_ratio_2025 - sex_ratio_2020) >= 3) AS shifted,
  ROUND(100.0 * COUNT(*) FILTER (WHERE ABS(sex_ratio_2025 - sex_ratio_2020) >= 3) / COUNT(*), 1) AS shifted_pct
FROM muni
WHERE base_diff <= 2 AND pop2020 >= 5000
GROUP BY grp
ORDER BY grp
```
