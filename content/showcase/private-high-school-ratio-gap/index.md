---
title: 私立高校の割合は東京都の55.6％から徳島県の7.7％まで、7.2倍の差がある
description: 国土数値情報の学校データから、都道府県別の私立高校の割合を比較しました。最も高い東京都は55.6％、最も低い徳島県は7.7％です。1人当たり県民所得との相関係数は0.50で、栃木県・富山県・群馬県・徳島県は、所得が中央値より高いのに私立高校の割合が低い県です
publishedAt: 2026-06-29
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 教育
  - 出店
  - 商圏分析
datasets:
  - queria/nlftp
  - queria/e_stat
sources:
  - title: 国土数値情報 学校データ（P29）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P29-v2_0.html
    publisher: 国土交通省
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
agentHint: 私立幼稚園の比率を都道府県別に出して、私立高校比率が高い県と、幼稚園でも私立志向が強い県が一致するか比べて。
socialAnnounce: |-
  国土数値情報の学校データから、都道府県別の私立高校比率を比べました。

  私立比率は地域の進学志向を映し、所得が高いのに公立志向が強い県には公立対策の需要が眠っています。
  学習塾など教育サービスの商圏評価に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

高校のうち私立の割合は、東京都が55.6％で最も高く、徳島県が7.7％で最も低く、7.2倍の差があります。大阪府・京都府・福岡県・神奈川県など大都市のある府県で高く、秋田県・沖縄県・岩手県・群馬県で低くなっています。1人当たり県民所得との相関係数は0.50です。栃木県・富山県・群馬県・徳島県は、所得が47都道府県の中央値より高いのに、私立高校の割合が中央値より低い県です。

学習塾・予備校・通信教育などの教育サービスでは、商圏人口や所得水準に加えて、その地域の家庭が私立と公立のどちらに進学させることが多いかによって、求められる対策が変わります。私立中高に進学する家庭が多い地域では中学受験・高校受験の対策の需要が多く、公立に進学する家庭が多い地域では、公立のトップ校を目指す層や内申点の対策の需要が中心になります。この記事では、高校のうち私立が占める割合を都道府県別に集計し、地域ごとの進学先の傾向を比較しました。

使ったのは、[国土数値情報の学校データ（P29）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P29-v2_0.html)をもとに全国の学校の所在地・学校種別・管理者を収録したテーブル（`school`）です。管理者は国・都道府県・市区町村・民間・その他に分類されています。この記事では管理者が「民間」の学校を私立とし、それ以外の学校はすべて公立として扱います。都道府県は行政区域コード（`admin_code`）の上位2桁で判定しています。

## 私立の割合は、小学校で1.3％、高等学校で28.8％、大学で70.9％

幼稚園から大学まで、教育段階ごとに私立（管理者が民間）の割合を算出しました。比較の対象は幼稚園・小学校・中学校・高等学校・大学の5種別で、高等専門学校や専修学校などは含めていません。

```chart
{
  "layer": [
    {
      "data": {"name": "ladder"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "school_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "school_class",
          "type": "nominal",
          "axis": {"title": "学校種別", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "私立の割合（％）", "grid": true}
        }
      }
    }
  ]
}
```

私立の割合は教育段階によって大きく異なります。幼稚園は66.5％が私立で、義務教育の小学校は1.3％、中学校は7.7％とほとんどが公立です。高等学校は28.8％、大学は70.9％で、教育段階が上がると私立の割合が再び高くなります。

小中学校はほとんどが公立で、大学は大半が私立です。高校は公立と私立の割合の差が最も小さい段階で、その割合が地域によって異なるので、地域ごとの進学先の傾向を比較する指標として使えます。

## 私立高校の割合は東京都の55.6％が最も高く、徳島県の7.7％が最も低い

2021年時点の私立高校の割合を47都道府県で比較しました。上位10・中間・下位10を色分けしています。この割合は学校の数の割合で、生徒数の割合とは一致しません。私立高校の1校あたりの生徒数は、公立より多い場合も少ない場合もあるためです。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "私立高校比率（％）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "私立高校比率（％）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "私立高校比率（％）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

最も高いのは東京都の55.6％で、高校の半分以上が私立です。大阪府（40.3％）・京都府（37.2％）・福岡県（36.7％）・神奈川県（35.0％）と、大都市のある府県が続きます。低いのは徳島県（7.7％）・秋田県（9.4％）・沖縄県（11.9％）・岩手県（16.5％）・群馬県（16.9％）です。東京都と徳島県では7.2倍の差があります。私立高校の割合が高い地域には、中学受験で私立の中高一貫校を目指す家庭が多く、低い地域では公立の進学校を中心にした進路が一般的だと考えられます。

## 私立高校の割合が高いのは三大都市圏と福岡県

同じ割合を地図にしました。色が濃いほど私立高校の割合が高い県です。

```map
type: map
layers:
  - from: map_data
    geojson: geojson
    color: value
    label: pref_name
    name: "私立高校比率（％）"
lng: 137
lat: 36.5
zoom: 4
```

三大都市圏と福岡県の色が濃く、人口の多い都市部で私立高校の割合が高くなっています。私立高校は一定の生徒数が見込める都市部に多く、学校の選択肢が多い地域ほど私立を選ぶ家庭も多いと考えられます。東北・四国・沖縄などは色が薄く、公立高校が進路の中心になっている地域です。出店候補地がどちらに当たるかによって、私立の中高一貫校の受験対策と、公立の進学校や内申点の対策のどちらが求められるかが変わります。

## 栃木県・富山県・群馬県・徳島県は、所得が中央値より高く私立高校の割合が低い

横軸に私立高校の割合、縦軸に2021年度の1人当たり県民所得（`C122101`）を取り、47都道府県を散布図にしました。点線は47都道府県の中央値（私立高校の割合24.7％、1人当たり県民所得2,949千円）です。1人当たり県民所得は県内で生じた所得を人口で割った値で、家計の可処分所得とは異なります。

```chart
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pct", "type": "quantitative"},
          {"field": "income", "type": "quantitative"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "私立高校比率（％）", "grid": true}
        },
        "y": {
          "field": "income",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1人当たり県民所得（千円・2021年度）", "grid": true}
        }
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 24.7, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 2949, "type": "quantitative"}
      }
    }
  ]
}
```

私立高校の割合と1人当たり県民所得の相関係数は0.50で、所得が高い県ほど私立高校の割合も高い傾向が緩やかにあります。中央値で区切った4つの領域ごとに、教育サービスの需要の傾向が異なると考えられます。

右上には、東京都（55.6％・5,761千円）・神奈川県（35.0％・3,199千円）・愛知県（25.2％・3,597千円）など、所得も私立高校の割合も高い大都市圏があります。私立中高一貫校の受験対策の市場が大きく、競合も多い地域です。左上には、栃木県（19.7％・3,307千円）・富山県（18.9％・3,291千円）・群馬県（16.9％・3,187千円）・徳島県（7.7％・3,202千円）など、所得は中央値より高いのに私立高校の割合が低い県があります。家計に余裕があり公立に進学する家庭が多い地域なので、公立のトップ校を目指す層や難関公立高校の対策の需要が見込めると考えられます。右下の福岡県（36.7％・2,733千円）・熊本県（31.6％・2,746千円）・奈良県（30.6％・2,549千円）は、所得が中央値以下でも私立高校の割合が高く、教育費を私立学校に使う家庭が多い市場と考えられます。

## 出店戦略での使い方

- 商圏の進学先の傾向の把握: 候補地の私立高校の割合を確認し、私立中高一貫校の受験対策と、公立の進学校や内申点の対策のどちらを中心にするかを判断できます
- 所得と組み合わせた需要の把握: 所得が高いのに私立高校の割合が低い県（栃木県・富山県・群馬県・徳島県など）では、公立に進学する家庭の中に、難関公立高校の対策の需要がある可能性があります
- 競合の多さの考慮: 私立高校の割合も所得も高い大都市圏は、受験対策の市場が大きく競合も多いので、価格や指導形態で他社との違いを用意する必要があります

## データの出典

本記事は[国土数値情報の学校データ（P29）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P29-v2_0.html)第2.0版（令和3年）を 2026-07-11 時点で取得して集計しています。令和3年より後の学校の統廃合や新設は含まれていません。所得は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)の1人当たり県民所得（`C122101`、2021年度）を使いました。

Queriaは、国土数値情報やe-Statなどの官公庁のオープンデータを、列名・単位・文字コードを統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[全国の学校所在地テーブル](/datasets/queria/nlftp/facility/school)から、自社の出店候補地の高校の公立・私立の構成を確認し、所得の水準と比較できます。

```sql id=ladder
SELECT school_class, ROUND(100.0 * SUM(CASE WHEN administrator = '民間' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct FROM nlftp.facility.school WHERE school_class IN ('幼稚園', '小学校', '中学校', '高等学校', '大学') GROUP BY school_class ORDER BY CASE school_class WHEN '幼稚園' THEN 1 WHEN '小学校' THEN 2 WHEN '中学校' THEN 3 WHEN '高等学校' THEN 4 WHEN '大学' THEN 5 END
```

```sql id=rank_top
WITH agg AS (SELECT substr(s.admin_code, 1, 2) AS pcode, ROUND(100.0 * SUM(CASE WHEN s.administrator = '民間' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct FROM nlftp.facility.school s WHERE s.school_class = '高等学校' GROUP BY 1), ranked AS (SELECT p.prefecture_name AS area_name, a.pct, ROW_NUMBER() OVER (ORDER BY a.pct DESC, p.prefecture_name) AS rn FROM agg a JOIN nlftp.boundary.prefecture p ON a.pcode = p.prefecture_code) SELECT area_name, pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH agg AS (SELECT substr(s.admin_code, 1, 2) AS pcode, ROUND(100.0 * SUM(CASE WHEN s.administrator = '民間' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct FROM nlftp.facility.school s WHERE s.school_class = '高等学校' GROUP BY 1), ranked AS (SELECT p.prefecture_name AS area_name, a.pct, ROW_NUMBER() OVER (ORDER BY a.pct DESC, p.prefecture_name) AS rn FROM agg a JOIN nlftp.boundary.prefecture p ON a.pcode = p.prefecture_code) SELECT area_name, pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH agg AS (SELECT substr(s.admin_code, 1, 2) AS pcode, ROUND(100.0 * SUM(CASE WHEN s.administrator = '民間' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct FROM nlftp.facility.school s WHERE s.school_class = '高等学校' GROUP BY 1), ranked AS (SELECT p.prefecture_name AS area_name, a.pct, ROW_NUMBER() OVER (ORDER BY a.pct DESC, p.prefecture_name) AS rn FROM agg a JOIN nlftp.boundary.prefecture p ON a.pcode = p.prefecture_code) SELECT area_name, pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=map_data
WITH agg AS (SELECT substr(s.admin_code, 1, 2) AS pcode, ROUND(100.0 * SUM(CASE WHEN s.administrator = '民間' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct FROM nlftp.facility.school s WHERE s.school_class = '高等学校' GROUP BY 1) SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, a.pct AS value, ROW_NUMBER() OVER (ORDER BY p.prefecture_name) - 1 AS row_id FROM agg a JOIN nlftp.boundary.prefecture p ON a.pcode = p.prefecture_code
```

```sql id=scatter
WITH agg AS (SELECT substr(s.admin_code, 1, 2) AS pcode, ROUND(100.0 * SUM(CASE WHEN s.administrator = '民間' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct FROM nlftp.facility.school s WHERE s.school_class = '高等学校' GROUP BY 1) SELECT p.prefecture_name AS area_name, a.pct AS pct, TRY_CAST(i.value AS DOUBLE) AS income FROM agg a JOIN nlftp.boundary.prefecture p ON a.pcode = p.prefecture_code JOIN e_stat.ssds.c_pref_economy i ON i.area_name = p.prefecture_name AND i.cat01 = 'C122101' AND i.year = 2021 WHERE TRY_CAST(i.value AS DOUBLE) IS NOT NULL
```
