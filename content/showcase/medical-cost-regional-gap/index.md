---
title: 75歳以上の1人当たり医療費は、福岡県が新潟県の1.54倍
description: 2022年度の一人当たり医療費は高知県が埼玉県の1.44倍。75歳以上の1人当たり医療費に絞っても福岡県と新潟県で1.54倍の差があり、北海道と福岡県・大阪府など西日本の13府県は、75歳以上（2008〜2023年度）でも年齢調整した協会けんぽの指数（2009〜2023年度）でも毎年全国を上回っています
publishedAt: 2026-03-07
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療費
  - 都道府県
  - 社会保障
datasets:
  - queria/e_stat
sources:
  - title: 令和4(2022)年度 国民医療費の概況
    url: https://www.mhlw.go.jp/toukei/saikin/hw/k-iryohi/22/index.html
    publisher: 厚生労働省
  - title: 後期高齢者医療事業状況報告
    url: https://www.mhlw.go.jp/bunya/iryouhoken/database/seido/kouki_houkoku.html
    publisher: 厚生労働省
  - title: 統計情報（事業年報）
    url: https://www.kyoukaikenpo.or.jp/g7/cat740/
    publisher: 全国健康保険協会
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: 1人当たり後期高齢者医療費(J450320)を2008年度から2023年度まで都道府県別に出して、全国を100とした値の推移を見たい。上位と下位の顔ぶれが入れ替わった年はある？
socialAnnounce: |-
  一人当たり医療費は高知県が埼玉県の1.44倍。75歳以上どうしで比べると、差は福岡県と新潟県の1.54倍に広がります。

  北海道と福岡県・大阪府など西日本の13府県は、75歳以上でも、年齢調整した協会けんぽの指数でも、毎年全国を上回っていました
---

2022年度の一人当たり医療費は、最も高い高知県が47.9万円、最も低い埼玉県が33.2万円で、1.44倍の開きがあります。上位7県はすべて九州・四国・中国の県で、下位には首都圏の県が並びます。

高齢者が多い県ほど医療費は多くかかり、47都道府県で高齢化率と一人当たり医療費の相関係数は0.57です。この記事では、年齢構成の違いの影響を除いた2つの系列、75歳以上の1人当たり医療費と、協会けんぽが年齢構成の違いを除いて出している地域差指数で、都道府県の差が残るかを確認しました。75歳以上の1人当たり医療費は福岡県が新潟県の1.54倍で、全年齢の1.44倍より差が大きくなります。北海道と西日本の13府県は、2つの系列のどちらでも毎年全国を上回っています。

## 75歳以上どうしで比較すると、医療費と高齢化率の相関はなくなる

一人当たり医療費は、[国民医療費](https://www.mhlw.go.jp/toukei/saikin/hw/k-iryohi/22/index.html)を人口で割った値で、年齢構成の違いを調整していません。これに対して75歳以上の1人当たり医療費は、[後期高齢者医療事業状況報告](https://www.mhlw.go.jp/bunya/iryouhoken/database/seido/kouki_houkoku.html)による後期高齢者医療制度の加入者1人当たりの医療費で、対象は75歳以上に限られています。加入者には、65〜74歳で一定の障害があると認定された人も含まれます。

次の図は、両方の医療費を全国を100とした値にして、高齢化率を横軸に並べたものです。

```chart
{
  "layer": [
    {
      "data": {"name": "cost_vs_aging"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "elderly_rate", "type": "quantitative"},
          {"field": "all_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "elderly_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（%、2022年）", "grid": true}
        },
        "y": {
          "field": "all_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "全国=100", "grid": true}
        },
        "color": {
          "datum": "一人当たり医療費（全年齢）",
          "type": "nominal",
          "scale": {"domain": ["一人当たり医療費（全年齢）", "75歳以上の1人当たり医療費"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "cost_vs_aging"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "elderly_rate", "type": "quantitative"},
          {"field": "old_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "elderly_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "高齢化率（%、2022年）", "grid": true}
        },
        "y": {
          "field": "old_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "全国=100", "grid": true}
        },
        "color": {
          "datum": "75歳以上の1人当たり医療費",
          "type": "nominal",
          "scale": {"domain": ["一人当たり医療費（全年齢）", "75歳以上の1人当たり医療費"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

全年齢の医療費（橙）は高齢化率が高い県ほど高くなりますが、75歳以上の医療費（青）は高齢化率と関係なく分布しています。

```sql
SELECT * FROM corr_2022
```

順位が最も大きく入れ替わるのは秋田県と沖縄県です。秋田県は高齢化率が38.6%で全国最高、全年齢の医療費は全国の107.2%ですが、75歳以上に限ると85.0%で全国を下回ります。沖縄県は高齢化率23.4%で東京都に次いで低く、全年齢では93.0%と全国を下回りますが、75歳以上では108.9%です。全年齢の医療費の順位は、医療費が多くかかる年齢の人がどれだけ住んでいるかによって決まっている部分があります。

75歳以上に限っても、都道府県の差は縮まりません。75歳以上の1人当たり医療費は、最も高い福岡県が117.6万円、最も低い新潟県が76.4万円で、1.54倍です。全年齢の1.44倍より広がります。

```sql
SELECT * FROM gap_2022
```

75歳以上の中でも、85歳以上が多い県と75〜84歳が多い県があり、この系列ではその違いは調整されていません。

## 年齢調整した協会けんぽの指数でも、75歳以上の医療費が高い県が高い

75歳以上とは別の人たちでも同じ傾向があるかを、[協会けんぽ](https://www.kyoukaikenpo.or.jp/g7/cat740/)の地域差指数で確認します。協会けんぽは主に中小企業の従業員とその家族が加入する健康保険で、加入者は現役世代とその子どもが中心です。地域差指数は、都道府県ごとの年齢階級別の1人当たり医療費を全国の年齢構成で重み付けし直した値で、全国を1とします。協会けんぽの都道府県は、加入者の住所ではなく勤め先の事業所がある都道府県で分かれます。2022年度は佐賀県の1.116が最も高く、新潟県の0.907が最も低くなっています。

横軸に75歳以上の医療費、縦軸に協会けんぽの地域差指数をとると、都道府県は右上と左下に多く分布し、相関係数は0.76です。

```chart
{
  "layer": [
    {
      "data": {"name": "pref_compare"},
      "mark": {"type": "point", "filled": true, "size": 100},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "old_idx", "type": "quantitative"},
          {"field": "kyokai_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "old_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "75歳以上の1人当たり医療費（全国=100、2022年度）", "grid": true}
        },
        "y": {
          "field": "kyokai_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "協会けんぽの地域差指数（全国=1、2022年度）", "grid": true}
        },
        "color": {"field": "color", "scale": null, "legend": null}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#9ca3af", "strokeWidth": 1, "strokeDash": [2, 3]},
      "encoding": {
        "x": {"datum": 100, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#9ca3af", "strokeWidth": 1, "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 1, "type": "quantitative"}
      }
    }
  ]
}
```

赤は次の節で集計する「両方で毎年全国を上回る」14道府県、青は「両方で毎年下回る」15県です。

## 14道府県は、年齢構成の影響を除いた2つの系列で毎年全国を上回る

1年だけの結果は偶然の可能性もあるので、複数年で確認します。75歳以上の1人当たり医療費は、後期高齢者医療制度で対象が75歳以上になった2008年度以降を使います。協会けんぽの地域差指数とあわせて、使った期間は次のとおりです。この期間に、どちらの系列でも毎年全国を上回った都道府県と、毎年下回った都道府県を集計しました。

```sql
SELECT * FROM coverage
```

```sql
SELECT * FROM group_summary
```

毎年上回った14道府県のうち、北海道を除く13府県はすべて近畿・中国・四国・九州にあります。毎年下回った15県には、九州・四国・中国の県が1つも入っていません。加入者が重ならない2つの制度のどちらでも、この14道府県は全国を上回り、15県は下回っています。

宮崎県は、協会けんぽの指数が15年のうち1年だけ全国と同じ値で、残りの年は両方の系列で全国を下回っているため、どちらにも入っていません。2つの系列で向きが逆になる県もあり、秋田県は75歳以上で16年とも全国を下回る一方、協会けんぽでは15年とも上回ります。沖縄県はその逆です。

47都道府県の値は次の表のとおりです。「全国超えの年数」は、それぞれの期間のうち全国を上回った年の数です。

```sql
SELECT * FROM pref_table
```

## まとめ

- 2022年度の一人当たり医療費は高知県が埼玉県の1.44倍で、高齢化率との相関は0.57です
- 75歳以上の1人当たり医療費に絞ると、高齢化率との相関は-0.05でほぼなくなりますが、差は福岡県と新潟県で1.54倍に広がります
- 年齢構成の違いを除いた協会けんぽの地域差指数と75歳以上の医療費の相関係数は0.76で、どちらも同じ県が高くなっています
- 北海道と近畿・中国・四国・九州の13府県は、75歳以上（2008〜2023年度）でも協会けんぽ（2009〜2023年度）でも毎年全国を上回っています。関東・中部を中心とする15県は毎年下回っています

全年齢の一人当たり医療費で上位9道県（高知県から北海道まで、熊本県と北海道は同額）は、すべて「両方で毎年上回る」14道府県に入っています。高齢者が多い県ほど医療費は多くなりますが、これらの県は、75歳以上の加入者どうしでも、年齢調整した協会けんぽの指数でも全国を上回り、その状態が15年以上続いています。医療費の地域差には、高齢化率の差だけでは説明できない部分があります。

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを2026年9月28日時点で集計しています。元データは厚生労働省の[国民医療費](https://www.mhlw.go.jp/toukei/saikin/hw/k-iryohi/22/index.html)（2022年度まで）と[後期高齢者医療事業状況報告](https://www.mhlw.go.jp/bunya/iryouhoken/database/seido/kouki_houkoku.html)（2023年度まで）、全国健康保険協会の[事業年報](https://www.kyoukaikenpo.or.jp/g7/cat740/)（2023年度まで）で、高齢化率は同じ体系の総人口と65歳以上人口から計算しています。

Queriaは、e-Statの社会・人口統計体系を、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の福祉統計テーブル](/datasets/queria/e_stat/ssds/j_pref_welfare)から、自分の県の75歳以上の1人当たり医療費や協会けんぽの地域差指数を年ごとに確認できます。

```sql id=cost_vs_aging
WITH w AS (SELECT area, area_name, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 IN ('J4004', 'J450320') AND year = 2022), a AS (SELECT area, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1303') / MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1101') * 100 AS elderly_rate FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND year = 2022 GROUP BY area), n AS (SELECT cat01, v AS nv FROM w WHERE area = '00000') SELECT w.area_name, ROUND(a.elderly_rate, 1) AS elderly_rate, ROUND(MAX(w.v / n.nv * 100) FILTER (WHERE w.cat01 = 'J4004'), 1) AS all_idx, ROUND(MAX(w.v / n.nv * 100) FILTER (WHERE w.cat01 = 'J450320'), 1) AS old_idx FROM w JOIN n ON w.cat01 = n.cat01 JOIN a ON w.area = a.area WHERE w.area != '00000' GROUP BY w.area, w.area_name, a.elderly_rate ORDER BY w.area
```

```sql id=corr_2022
WITH w AS (SELECT area, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 IN ('J4004', 'J450320', 'J4206') AND year = 2022 AND area != '00000'), a AS (SELECT area, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1303') / MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1101') * 100 AS elderly_rate FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1303') AND year = 2022 AND area != '00000' GROUP BY area), p AS (SELECT a.area, a.elderly_rate, MAX(w.v) FILTER (WHERE w.cat01 = 'J4004') AS cost_all, MAX(w.v) FILTER (WHERE w.cat01 = 'J450320') AS cost_old, MAX(w.v) FILTER (WHERE w.cat01 = 'J4206') AS kyokai FROM a JOIN w ON a.area = w.area GROUP BY a.area, a.elderly_rate) SELECT '高齢化率 × 一人当たり医療費（全年齢）' AS "組み合わせ", ROUND(CORR(elderly_rate, cost_all), 2) AS "相関係数" FROM p UNION ALL SELECT '高齢化率 × 75歳以上の1人当たり医療費', ROUND(CORR(elderly_rate, cost_old), 2) FROM p UNION ALL SELECT '75歳以上の1人当たり医療費 × 協会けんぽの地域差指数', ROUND(CORR(cost_old, kyokai), 2) FROM p
```

```sql id=gap_2022
WITH w AS (SELECT area_name, cat01, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 IN ('J4004', 'J450320', 'J4206') AND year = 2022 AND area != '00000'), x AS (SELECT cat01, CASE WHEN cat01 = 'J4206' THEN ROUND(1 + v, 3) ELSE v END AS v, area_name FROM w) SELECT CASE cat01 WHEN 'J4004' THEN '一人当たり医療費（全年齢・千円）' WHEN 'J450320' THEN '75歳以上の1人当たり医療費（円）' ELSE '協会けんぽの地域差指数（全国=1）' END AS "指標", arg_max(area_name, v) AS "最も高い", MAX(v) AS "最高値", arg_min(area_name, v) AS "最も低い", MIN(v) AS "最低値", ROUND(MAX(v) / MIN(v), 2) AS "倍率" FROM x GROUP BY cat01 ORDER BY cat01
```

```sql id=pref_compare
WITH o AS (SELECT area, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J450320' AND year BETWEEN 2008 AND 2023), oc AS (SELECT p.area, COUNT(*) FILTER (WHERE p.v > n.v) AS old_above, COUNT(*) FILTER (WHERE p.v < n.v) AS old_below, COUNT(*) AS old_years FROM o p JOIN o n ON n.area = '00000' AND n.year = p.year WHERE p.area != '00000' GROUP BY p.area), k AS (SELECT area, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) > 0) AS k_above, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) < 0) AS k_below, COUNT(*) AS k_years FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J4206' AND area != '00000' AND year BETWEEN 2009 AND 2023 GROUP BY area), c AS (SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J4004') AS cost_all, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J450320') AS cost_old, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J4206') AS k_dev FROM e_stat.ssds.j_pref_welfare WHERE cat01 IN ('J4004', 'J450320', 'J4206') AND year = 2022 GROUP BY area, area_name), t AS (SELECT c.area, c.area_name, c.cost_all, ROUND(c.cost_old / 10000, 1) AS cost_old_man, ROUND(c.cost_old / nat.cost_old * 100, 1) AS old_idx, ROUND(1 + c.k_dev, 3) AS kyokai_idx, oc.old_above, k.k_above, CASE WHEN oc.old_above = oc.old_years AND k.k_above = k.k_years THEN '両方で毎年上回る' WHEN oc.old_below = oc.old_years AND k.k_below = k.k_years THEN '両方で毎年下回る' ELSE 'どちらでもない' END AS grp FROM c JOIN oc ON c.area = oc.area JOIN k ON c.area = k.area CROSS JOIN (SELECT cost_old FROM c WHERE area = '00000') nat) SELECT area_name, cost_all, cost_old_man, old_idx, kyokai_idx, old_above, k_above, grp, CASE grp WHEN '両方で毎年上回る' THEN '#dc2626' WHEN '両方で毎年下回る' THEN '#2563eb' ELSE '#9ca3af' END AS color FROM t ORDER BY area
```

```sql id=coverage
SELECT CASE cat01 WHEN 'J4004' THEN '一人当たり医療費（全年齢）' WHEN 'J450320' THEN '75歳以上の1人当たり医療費' ELSE '協会けんぽの地域差指数' END AS "系列", MIN(year) AS "最初の年度", MAX(year) AS "最後の年度", COUNT(DISTINCT year) AS "年数" FROM e_stat.ssds.j_pref_welfare WHERE area = '00000' AND (cat01 IN ('J4004', 'J4206') OR (cat01 = 'J450320' AND year >= 2008)) GROUP BY cat01 ORDER BY cat01
```

```sql id=pref_table
WITH o AS (SELECT area, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J450320' AND year BETWEEN 2008 AND 2023), oc AS (SELECT p.area, COUNT(*) FILTER (WHERE p.v > n.v) AS old_above, COUNT(*) FILTER (WHERE p.v < n.v) AS old_below, COUNT(*) AS old_years FROM o p JOIN o n ON n.area = '00000' AND n.year = p.year WHERE p.area != '00000' GROUP BY p.area), k AS (SELECT area, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) > 0) AS k_above, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) < 0) AS k_below, COUNT(*) AS k_years FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J4206' AND area != '00000' AND year BETWEEN 2009 AND 2023 GROUP BY area), c AS (SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J4004') AS cost_all, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J450320') AS cost_old, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J4206') AS k_dev FROM e_stat.ssds.j_pref_welfare WHERE cat01 IN ('J4004', 'J450320', 'J4206') AND year = 2022 GROUP BY area, area_name), t AS (SELECT c.area, c.area_name, c.cost_all, ROUND(c.cost_old / 10000, 1) AS cost_old_man, ROUND(c.cost_old / nat.cost_old * 100, 1) AS old_idx, ROUND(1 + c.k_dev, 3) AS kyokai_idx, oc.old_above, oc.old_below, k.k_above, k.k_below, CASE WHEN oc.old_above = oc.old_years AND k.k_above = k.k_years THEN '両方で毎年上回る' WHEN oc.old_below = oc.old_years AND k.k_below = k.k_years THEN '両方で毎年下回る' ELSE 'どちらでもない' END AS grp FROM c JOIN oc ON c.area = oc.area JOIN k ON c.area = k.area CROSS JOIN (SELECT cost_old FROM c WHERE area = '00000') nat) SELECT area_name AS "都道府県", cost_all AS "全年齢の一人当たり医療費（千円）", cost_old_man AS "75歳以上の1人当たり医療費（万円）", kyokai_idx AS "協会けんぽの地域差指数", old_above AS "75歳以上の全国超えの年数（16年中）", old_below AS "75歳以上の全国未満の年数（16年中）", k_above AS "協会けんぽの全国超えの年数（15年中）", k_below AS "協会けんぽの全国未満の年数（15年中）", grp AS "区分" FROM t ORDER BY area
```

```sql id=group_summary
WITH o AS (SELECT area, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J450320' AND year BETWEEN 2008 AND 2023), oc AS (SELECT p.area, COUNT(*) FILTER (WHERE p.v > n.v) AS old_above, COUNT(*) FILTER (WHERE p.v < n.v) AS old_below, COUNT(*) AS old_years FROM o p JOIN o n ON n.area = '00000' AND n.year = p.year WHERE p.area != '00000' GROUP BY p.area), k AS (SELECT area, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) > 0) AS k_above, COUNT(*) FILTER (WHERE TRY_CAST(value AS DOUBLE) < 0) AS k_below, COUNT(*) AS k_years FROM e_stat.ssds.j_pref_welfare WHERE cat01 = 'J4206' AND area != '00000' AND year BETWEEN 2009 AND 2023 GROUP BY area), c AS (SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J4004') AS cost_all, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J450320') AS cost_old, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'J4206') AS k_dev FROM e_stat.ssds.j_pref_welfare WHERE cat01 IN ('J4004', 'J450320', 'J4206') AND year = 2022 GROUP BY area, area_name), t AS (SELECT c.area, c.area_name, c.cost_all, ROUND(c.cost_old / 10000, 1) AS cost_old_man, ROUND(c.cost_old / nat.cost_old * 100, 1) AS old_idx, ROUND(1 + c.k_dev, 3) AS kyokai_idx, oc.old_above, k.k_above, CASE WHEN oc.old_above = oc.old_years AND k.k_above = k.k_years THEN '両方で毎年上回る' WHEN oc.old_below = oc.old_years AND k.k_below = k.k_years THEN '両方で毎年下回る' ELSE 'どちらでもない' END AS grp FROM c JOIN oc ON c.area = oc.area JOIN k ON c.area = k.area CROSS JOIN (SELECT cost_old FROM c WHERE area = '00000') nat) SELECT grp AS "区分", COUNT(*) AS "都道府県数", string_agg(area_name, '・' ORDER BY area) AS "都道府県" FROM t GROUP BY grp ORDER BY MIN(CASE grp WHEN '両方で毎年上回る' THEN 1 WHEN '両方で毎年下回る' THEN 2 ELSE 3 END)
```
