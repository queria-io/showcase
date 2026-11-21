---
title: 公共工事の見積もりに使う職人の日当は、14年で東北・北陸が関西を追い越した。大阪府はいま青森県より低い
description: 国が公共工事の見積もりに使う職人28職種の日当を合計すると、大阪府は2012年の10位から2026年は33位に下がり、宮城県など4県が東京都を上回りました
publishedAt: 2026-11-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 建設業
  - 公共工事
  - 賃金
  - 地域格差
datasets:
  - queria/mlit
  - queria/e_stat
sources:
  - title: 公共事業労務費調査・公共工事設計労務単価について
    url: https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000217.html
    publisher: 国土交通省
  - title: 建設総合統計
    url: https://www.mlit.go.jp/toukeijouhou/chojou/gai_sougou.htm
    publisher: 国土交通省
  - title: 賃金構造基本統計調査
    url: https://www.mhlw.go.jp/toukei/list/chinginkouzou.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 普通作業員・とび工・鉄筋工・型わく工の4職種について、2012年4月と2026年3月の単価を大阪府・兵庫県・京都府・宮城県・石川県・東京都で並べて、それぞれの上昇率と東京都との比を出して。
socialAnnounce: |
  公共工事の職人28職種の日当を比べると、大阪府は2012年の10位から2026年は33位へ下がり、宮城県など4県は東京都より上です。
  関西の建設会社の賃金設定に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

公共工事の見積もりに使う職人28職種の日当を合計した額は、2012年は東京都が1位、大阪府が10位で、東北と北陸の県は21位以下でした。2026年3月からの単価では、宮城県・石川県・富山県・福島県の4県が東京都を上回り、大阪府は33位で、青森県（16位）より下になっています。

国や自治体が公共工事の予定価格を見積もるときは、国土交通省と農林水産省が毎年決める[公共工事設計労務単価](https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000217.html)を使います。都道府県ごと・職種ごとに決まる職人1日あたりの賃金で、両省が10月に公共工事の現場で払われた賃金を賃金台帳から調査し、その結果から決めます。単価は所定労働時間内の8時間分で、残業代や、会社が負担する法定福利費は含みません。

この記事は、関西や中国地方で公共工事を請け負い、職人を自社で雇っている建設会社の経営者に向けて書いています。自社の県の単価がほかの県と比較してどう動いてきたかは、職人の賃金を決めるときの材料になります。

## 地方の平均では、東北が2013年、北陸が2015年に近畿を上回った

使うのは、国土交通省の公共工事設計労務単価を収録したテーブル（`mlit.construction.design_labor_unit_price`）です。2012年4月から2026年3月まで15回分の改定について、47都道府県と51職種の単価を持ちます。単価が設定されていない職種と県の組には行がありません。

県ごとに設定される職種が違うので、15回すべてで47都道府県に単価がある28職種だけを使い、その単価を1日分ずつ合計した額で県を比較します。28職種は下の表のとおりです。土木工事の職種が中心で、大工や内装工のように一部の県で単価が設定されていない建築の職種は入りません。

```sql
SELECT trades AS "比べる28職種", n AS "職種の数", n_all AS "収録している職種の数" FROM occ_list
```

地方ごとに、28職種の合計額が東京都の何倍かを県ごとに出して平均し、改定のたびに並べました。横軸は単価の適用が始まった年です。2014年から2016年は2月、2017年以降は3月に適用が始まっています。この単価の地方区分では、北陸は新潟県・富山県・石川県で、福井県は近畿に入ります。図には5つの地方を描き、破線は東京都と同じ水準です。

岩手県・宮城県・福島県の単価は、2012年から2022年まで、国の公表資料で被災地向けとして括弧書きにされた値です。2023年以降はこの区別がありません。2021年と2022年は、前の年より下がる単価を前の年のまま据え置く特別措置がとられています。

```chart
{
  "layer": [
    {
      "data": {"name": "region_lines"},
      "transform": [
        {"fold": ["tohoku", "hokuriku", "kyushu", "kinki", "chugoku"], "as": ["key", "ratio"]},
        {"calculate": "{'tohoku': '東北', 'hokuriku': '北陸', 'kyushu': '九州', 'kinki': '近畿', 'chugoku': '中国'}[datum.key]", "as": "region"}
      ],
      "mark": {"type": "line", "point": {"filled": true, "size": 30}},
      "encoding": {
        "x": {"field": "y", "type": "quantitative", "title": "単価の適用が始まった年", "axis": {"format": "d"}, "scale": {"zero": false}},
        "y": {"field": "ratio", "type": "quantitative", "title": "28職種の単価の合計（東京都＝1）", "scale": {"zero": false}},
        "color": {"field": "region", "type": "nominal", "title": null, "scale": {"domain": ["東北", "北陸", "九州", "近畿", "中国"], "range": ["#ef4444", "#f97316", "#86efac", "#3b82f6", "#93c5fd"]}, "legend": {"orient": "bottom"}},
        "tooltip": [{"field": "region", "title": "地方"}, {"field": "y", "title": "年"}, {"field": "ratio", "title": "東京都との比"}]
      }
    },
    {
      "data": {"values": [{"v": 1}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [4, 4]},
      "encoding": {"y": {"field": "v", "type": "quantitative"}}
    }
  ]
}
```

2012年に近畿より平均が高かったのは関東と中部だけでした。東北は2013年、北陸は2015年、図に描いていない北海道は2017年、九州は2018年に近畿を上回りました。九州は2023年から2025年に再び近畿をわずかに下回り、2026年にまた上回っています。2026年に近畿より平均が低い地方は中国だけです。

## 県ごとの順位では、大阪府は10位から33位に下がった

下の図は、28職種の合計額が東京都の何倍かを、2012年4月（灰色）と2026年3月（色付き）で並べたものです。2026年3月の値が大きい県ほど上にあります。赤は東北と北陸の県、青は近畿の府県です。

```chart
{
  "height": 1100,
  "layer": [
    {
      "data": {"name": "pref_change"},
      "encoding": {"y": {"field": "prefecture_name", "type": "nominal", "title": null, "sort": {"field": "ratio_2026", "order": "descending"}}},
      "layer": [
        {"mark": {"type": "rule", "color": "#cbd5e1", "strokeWidth": 3}, "encoding": {"x": {"field": "ratio_2012", "type": "quantitative", "title": "28職種の単価の合計（東京都＝1）", "scale": {"zero": false}}, "x2": {"field": "ratio_2026"}}},
        {"mark": {"type": "point", "filled": true, "size": 60, "color": "#94a3b8"}, "encoding": {"x": {"field": "ratio_2012", "type": "quantitative"}, "tooltip": [{"field": "prefecture_name", "title": "都道府県"}, {"field": "ratio_2012", "title": "2012年4月（東京都＝1）"}]}},
        {"mark": {"type": "point", "filled": true, "size": 90}, "encoding": {"x": {"field": "ratio_2026", "type": "quantitative"}, "color": {"field": "color", "type": "nominal", "scale": null}, "tooltip": [{"field": "prefecture_name", "title": "都道府県"}, {"field": "ratio_2026", "title": "2026年3月（東京都＝1）"}]}}
      ]
    },
    {
      "data": {"values": [{"v": 1}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [4, 4]},
      "encoding": {"x": {"field": "v", "type": "quantitative"}}
    }
  ]
}
```

東北6県と北陸3県は、2012年は東京都の0.857〜0.918倍で、21位から40位に並んでいました。2026年はこの9県すべてが18位以内に入り、宮城県は東京都の1.043倍で1位です。近畿の7府県は、2012年は10〜20位でしたが、2026年は32〜43位です。大阪府の順位は改定のたびに15位、17位、22位と下がり、2018年から2022年は33位か34位でした。2025年は24位まで戻り、2026年は再び33位です。

金額では、28職種を1日ずつ合計した額は2026年3月で東京都が95万2,600円、宮城県が99万3,400円、青森県が93万2,900円、大阪府が88万4,500円です。14年の上昇率は東北6県がいずれも110%を超え、近畿の7府県は81.6〜84.3%で、全国で上昇率が低い順の1位から7位を占めます。

```sql
SELECT prefecture_name AS "都道府県", basket_2012 AS "2012年4月（円）", basket_2026 AS "2026年3月（円）", rise_pct AS "上昇率（%）", rank_2012 AS "2012年の順位", rank_2026 AS "2026年の順位" FROM pref_change WHERE prefecture_name IN ('東京都', '宮城県', '石川県', '青森県', '大阪府', '兵庫県', '京都府') ORDER BY basket_2026 DESC
```

東京都を上回る県は2015年まで0で、2016年に宮城県が初めて上回りました。最も多かったのは2022年の9県です。被災地向けの区別がなくなった2023年以降も、東京都を上回る県は4〜8あり、宮城県は毎年その中に入っています。

```sql
SELECT y AS "適用開始の年", n_above_tokyo AS "東京都を上回る県の数", tokyo_rank AS "東京都の順位", osaka_rank AS "大阪府の順位" FROM above_tokyo
```

## 職人の単価は、46道府県すべてで一般の給与より東京都との差が小さい

職人の単価を、ほかの仕事を含めた一般の給与と並べます。e-Stat「[社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)」の都道府県別労働データ（`f_pref_labor`）にある所定内給与額（男）（`F620217`）は、厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)による男性の一般労働者の月額で、全産業の値です。同じテーブルには女性の値（`F620218`）や、残業代を含む「きまって支給する現金給与額」（`F620215`・`F620216`）もあります。

下の図は、横軸に2024年6月の所定内給与額（男）、縦軸に28職種の単価の合計を、どちらも東京都との比で置いたものです。単価は、2024年度の調査をもとに2025年3月から適用された値を使い、調査した年を統一しています。

```chart
{
  "data": {"name": "wage_vs_price"},
  "layer": [
    {"mark": {"type": "point", "filled": true, "size": 70, "opacity": 0.8}, "encoding": {"x": {"field": "wage_ratio", "type": "quantitative", "title": "男性の所定内給与額 2024年（東京都＝1）", "scale": {"zero": false}}, "y": {"field": "price_ratio", "type": "quantitative", "title": "28職種の単価の合計 2025年3月（東京都＝1）", "scale": {"zero": false}}, "color": {"field": "color", "type": "nominal", "scale": null}, "tooltip": [{"field": "prefecture_name", "title": "都道府県"}, {"field": "wage_ratio", "title": "一般の給与（東京都＝1）"}, {"field": "price_ratio", "title": "職人の単価（東京都＝1）"}]}},
    {"mark": {"type": "text", "dy": -9, "fontSize": 11, "color": "#334155"}, "encoding": {"x": {"field": "wage_ratio", "type": "quantitative"}, "y": {"field": "price_ratio", "type": "quantitative"}, "text": {"field": "label"}}}
  ]
}
```

東京都を除く46道府県の一般の給与は、東京都の0.651〜0.880倍に分布しています。職人の単価は0.857〜1.033倍の範囲にあり、46道府県すべてで、単価の東京都との比が給与の比を上回っています。47都道府県で見た2つの比の相関は0.28で、給与が高い県ほど単価も高いという関係は弱いものです。

単価の比から給与の比を引いた差が最も小さいのは大阪府（0.069）で、神奈川県（0.107）が続きます。大阪府は一般の給与では東京都の0.867倍で、東京都・神奈川県に次ぐ3位ですが、職人の単価では24位です。青森県は、一般の給与が東京都の0.658倍で45位なのに、職人の単価は0.979倍で12位です。秋田県（給与44位・単価9位）と宮城県（給与19位・単価1位）も、給与より単価の順位が高い県です。

```sql
SELECT corr_ratio AS "2つの比の相関", wage_min AS "給与の比の最小", wage_max AS "給与の比の最大", price_min AS "単価の比の最小", price_max AS "単価の比の最大", n_price_above_wage AS "単価の比が上回る道府県", small_gap_prefs AS "差が0.12未満の府県" FROM wage_summary
```

```sql
SELECT prefecture_name AS "都道府県", wage AS "所定内給与額（男・千円）", wage_rank AS "給与の順位", price_rank AS "単価の順位" FROM wage_vs_price WHERE highlight ORDER BY wage_rank
```

## 単価の上昇率と工事の出来高の増減率の相関は-0.12

国土交通省の[建設総合統計](https://www.mlit.go.jp/toukeijouhou/chojou/gai_sougou.htm)による都道府県別の建設工事出来高（`e_stat.construction.prefecture_monthly`）を使い、2012年と2025年の1年分の出来高の増減率と、28職種の単価の合計の上昇率（2012年4月→2026年3月）を県ごとに並べました。出来高は建築・土木、民間・公共を合わせた工事費を工事の進み具合に応じて月ごとに割り振った額で、物価の上昇分を含みます。

```chart
{
  "data": {"name": "output_vs_price"},
  "layer": [
    {"mark": {"type": "point", "filled": true, "size": 70, "opacity": 0.8}, "encoding": {"x": {"field": "out_chg", "type": "quantitative", "title": "建設工事出来高の増減率 2012→2025年（%）", "scale": {"zero": false}}, "y": {"field": "price_chg", "type": "quantitative", "title": "28職種の単価の合計の上昇率 2012→2026年（%）", "scale": {"zero": false}}, "color": {"field": "color", "type": "nominal", "scale": null}, "tooltip": [{"field": "prefecture_name", "title": "都道府県"}, {"field": "out_chg", "title": "出来高の増減（%）"}, {"field": "price_chg", "title": "単価の上昇（%）"}]}},
    {"mark": {"type": "text", "dy": -9, "fontSize": 11, "color": "#334155"}, "encoding": {"x": {"field": "out_chg", "type": "quantitative"}, "y": {"field": "price_chg", "type": "quantitative"}, "text": {"field": "label"}}}
  ]
}
```

2つの増減率の相関は-0.12で、工事が増えた県ほど単価が上がったという関係はありません。この比較は2時点の増減率どうしなので、途中の年の増減は含みません。出来高が2012年より減ったのは宮城県（-17.9%）・青森県（-11.2%）・新潟県（-5.0%）・岩手県（-2.4%）・和歌山県（-1.2%）の5県で、和歌山県を除く4県は単価の上昇率が106%以上です。出来高が2倍になった滋賀県（+100.6%）の単価の上昇率は83.2%で、全国で6番目に低い値です。

```sql
SELECT corr_out_price AS "出来高と単価の増減率の相関", n_pref AS "都道府県の数", output_down AS "出来高が減った県" FROM output_corr
```

## 業務での使い方

- 自社の県と隣の県の単価を、職種ごとに14年分並べる。28職種の合計で近畿の府県が順位を下げていても、自社の職種で同じことが起きているかは職種ごとに確認する必要があります。とび工や鉄筋工のように、自社の職人が多い職種から確認します
- 職人の賃金を決めるときに、自社の県の単価を目安にする。単価は県内の公共工事の現場で払われた賃金をもとに決まるので、同じ県で同じ職種の職人がどれくらい受け取っているかの目安になります。近畿の単価の伸びが小さかったのは、近畿の公共工事の現場で払われた賃金の伸びが小さかったためです。14年で何%上がったかを、東京都や隣の県と並べて確認します

## データの出典

本記事は、国土交通省・農林水産省の[公共工事設計労務単価](https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000217.html)、国土交通省の[建設総合統計](https://www.mlit.go.jp/toukeijouhou/chojou/gai_sougou.htm)、e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別労働データ（元データは厚生労働省の[賃金構造基本統計調査](https://www.mhlw.go.jp/toukei/list/chinginkouzou.html)）を、2026年11月11日時点で集計しています。単価は2012年4月から2026年3月までの15回分、出来高は2012年と2025年の暦年の合計、給与は2024年の値です。

Queriaは、国土交通省やe-Statの統計を、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[公共工事設計労務単価のテーブル](/datasets/queria/mlit/construction/design_labor_unit_price)から、47都道府県・15回分の単価を並べて、自社の県と職種の単価が14年でどう動いたかを確認できます。

```sql id=basket
-- 15回すべてで47都道府県に単価がある職種だけを使い、県ごとに単価を足す
WITH occ AS (
  SELECT occupation_code
  FROM mlit.construction.design_labor_unit_price
  WHERE applied_from <= DATE '2026-03-01'
  GROUP BY occupation_code
  HAVING count(DISTINCT prefecture_code || CAST(applied_from AS VARCHAR)) = 47 * 15
), b AS (
  SELECT applied_from, region, prefecture_code, prefecture_name, sum(unit_price) AS basket, count(*) AS n_trades
  FROM mlit.construction.design_labor_unit_price
  WHERE occupation_code IN (SELECT occupation_code FROM occ) AND applied_from <= DATE '2026-03-01'
  GROUP BY applied_from, region, prefecture_code, prefecture_name
)
SELECT b.applied_from, year(b.applied_from) AS y, b.region, b.prefecture_code, b.prefecture_name, b.basket, b.n_trades,
  round(b.basket / t.basket, 3) AS ratio,
  rank() OVER (PARTITION BY b.applied_from ORDER BY b.basket DESC) AS rnk
FROM b JOIN b AS t ON t.prefecture_name = '東京都' AND t.applied_from = b.applied_from
```

```sql id=occ_list
-- 比べる28職種の一覧（プロットはしない）
SELECT string_agg(occupation, '、' ORDER BY occupation_code) AS trades, count(*) AS n,
  (SELECT count(DISTINCT occupation_code) FROM mlit.construction.design_labor_unit_price WHERE applied_from <= DATE '2026-03-01') AS n_all
FROM (
  SELECT occupation_code, any_value(occupation) AS occupation
  FROM mlit.construction.design_labor_unit_price
  WHERE applied_from <= DATE '2026-03-01'
  GROUP BY occupation_code
  HAVING count(DISTINCT prefecture_code || CAST(applied_from AS VARCHAR)) = 47 * 15
)
```

```sql id=pref_change
SELECT a.prefecture_code, a.prefecture_name, a.region,
  CASE WHEN a.region IN ('東北', '北陸') THEN '#ef4444' WHEN a.region = '近畿' THEN '#3b82f6' ELSE '#64748b' END AS color,
  a.ratio AS ratio_2012, c.ratio AS ratio_2026, a.rnk AS rank_2012, c.rnk AS rank_2026,
  a.basket AS basket_2012, c.basket AS basket_2026,
  round(100 * (c.basket / a.basket - 1), 1) AS rise_pct
FROM basket a
JOIN basket c ON c.prefecture_code = a.prefecture_code AND c.applied_from = DATE '2026-03-01'
WHERE a.applied_from = DATE '2012-04-01'
ORDER BY c.ratio, a.prefecture_name
```

```sql id=region_trend
SELECT y, region, round(avg(ratio), 3) AS ratio, count(*) AS n_pref
FROM basket
GROUP BY y, region
ORDER BY (SELECT avg(b2.ratio) FROM basket b2 WHERE b2.region = basket.region AND b2.applied_from = DATE '2026-03-01'), y
```

```sql id=region_lines
-- 地方ごとの平均を年ごとに1行へ並べる
SELECT y,
  max(ratio) FILTER (WHERE region = '東北') AS tohoku,
  max(ratio) FILTER (WHERE region = '北陸') AS hokuriku,
  max(ratio) FILTER (WHERE region = '近畿') AS kinki,
  max(ratio) FILTER (WHERE region = '中国') AS chugoku,
  max(ratio) FILTER (WHERE region = '四国') AS shikoku,
  max(ratio) FILTER (WHERE region = '九州') AS kyushu,
  max(ratio) FILTER (WHERE region = '北海道') AS hokkaido,
  max(ratio) FILTER (WHERE region = '沖縄') AS okinawa,
  max(ratio) FILTER (WHERE region = '中部') AS chubu,
  max(ratio) FILTER (WHERE region = '関東') AS kanto
FROM region_trend
GROUP BY y
ORDER BY y
```

```sql id=above_tokyo
SELECT applied_from, y,
  count(*) FILTER (WHERE ratio > 1) AS n_above_tokyo,
  max(rnk) FILTER (WHERE prefecture_name = '東京都') AS tokyo_rank,
  max(rnk) FILTER (WHERE prefecture_name = '大阪府') AS osaka_rank
FROM basket
GROUP BY applied_from, y
ORDER BY applied_from
```

```sql id=wage_vs_price
WITH w AS (
  SELECT area_name, TRY_CAST(value AS DOUBLE) AS wage
  FROM e_stat.ssds.f_pref_labor
  WHERE cat01 = 'F620217' AND year = 2024 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL
)
SELECT b.prefecture_name, w.wage, round(w.wage / t.wage, 3) AS wage_ratio, b.ratio AS price_ratio,
  rank() OVER (ORDER BY w.wage DESC) AS wage_rank, b.rnk AS price_rank,
  b.prefecture_name IN ('東京都', '神奈川県', '大阪府', '宮城県', '秋田県', '青森県') AS highlight,
  CASE WHEN b.prefecture_name IN ('東京都', '神奈川県', '大阪府', '宮城県', '秋田県', '青森県') THEN b.prefecture_name ELSE '' END AS label,
  CASE WHEN b.region IN ('東北', '北陸') THEN '#ef4444' WHEN b.region = '近畿' THEN '#3b82f6' ELSE '#94a3b8' END AS color
FROM basket b
JOIN w ON w.area_name = b.prefecture_name
JOIN w AS t ON t.area_name = '東京都'
WHERE b.applied_from = DATE '2025-03-01'
ORDER BY wage_ratio DESC
```

```sql id=output_vs_price
WITH o AS (
  SELECT prefecture_code,
    sum(output) FILTER (WHERE year = 2012) AS out_2012,
    sum(output) FILTER (WHERE year = 2025) AS out_2025
  FROM e_stat.construction.prefecture_monthly
  WHERE year IN (2012, 2025)
  GROUP BY prefecture_code
)
SELECT p.prefecture_name, o.out_2012, o.out_2025,
  round(100 * (o.out_2025 / o.out_2012 - 1), 1) AS out_chg,
  p.rise_pct AS price_chg,
  CASE WHEN p.prefecture_name IN ('宮城県', '青森県', '滋賀県', '大阪府', '石川県', '東京都') THEN p.prefecture_name ELSE '' END AS label,
  p.color
FROM pref_change p JOIN o ON o.prefecture_code = p.prefecture_code
ORDER BY out_chg
```

```sql id=output_corr
-- 出来高と単価の増減率の相関（プロットはしない）
SELECT round(corr(out_chg, price_chg), 2) AS corr_out_price, count(*) AS n_pref,
  string_agg(prefecture_name || '（' || out_chg || '%）', '、' ORDER BY out_chg) FILTER (WHERE out_chg < 0) AS output_down
FROM output_vs_price
```

```sql id=wage_summary
-- 一般の給与と職人の単価の東京都との比をまとめる（プロットはしない）
SELECT round(corr(wage_ratio, price_ratio), 2) AS corr_ratio,
  min(wage_ratio) FILTER (WHERE prefecture_name <> '東京都') AS wage_min, max(wage_ratio) FILTER (WHERE prefecture_name <> '東京都') AS wage_max,
  min(price_ratio) FILTER (WHERE prefecture_name <> '東京都') AS price_min, max(price_ratio) FILTER (WHERE prefecture_name <> '東京都') AS price_max,
  count(*) FILTER (WHERE price_ratio > wage_ratio) AS n_price_above_wage,
  arg_min(prefecture_name, price_ratio - wage_ratio) FILTER (WHERE prefecture_name <> '東京都') AS smallest_gap_pref,
  round(min(price_ratio - wage_ratio) FILTER (WHERE prefecture_name <> '東京都'), 3) AS smallest_gap,
  string_agg(prefecture_name || '（' || round(price_ratio - wage_ratio, 3) || '）', '、' ORDER BY price_ratio - wage_ratio) FILTER (WHERE price_ratio - wage_ratio < 0.12 AND prefecture_name <> '東京都') AS small_gap_prefs
FROM wage_vs_price
```
