---
title: 5年間に記録された地震約130万回のうち、人が揺れを感じたのは0.76%の9,902回
description: 気象庁の震源カタログから2019〜2023年の約130万件を集計しました。有感地震は9,902回で全体の0.76%、震度6弱以上は7回です。マグニチュード5以上の地震は太平洋側の沖合に集中し、震源は西へ行くほど深くなります。
ogDescription: 気象庁の震源カタログから2019〜2023年の約130万件を集計しました。有感地震は9,902回で全体の0.76%、震度6弱以上は7回です。
publishedAt: 2026-07-02
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 地震
  - 防災
  - BCP
  - 気象庁
datasets:
  - queria/jma
sources:
  - title: 地震月報(カタログ編)
    url: https://www.data.jma.go.jp/eqev/data/bulletin/index.html
    publisher: 気象庁
  - title: 震度データベース検索
    url: https://www.data.jma.go.jp/eqdb/data/shindo/index.html
    publisher: 気象庁
agentHint: 日本周辺のマグニチュード5以上の地震を、震源の深さ帯（0–30km・30–70kmなど）別に年ごとに集計して。浅い地震が集中した年があるか見て
socialAnnounce: |-
  気象庁の震源カタログ約130万件から、地震の起きる場所・深さ・規模の分布を可視化しました。

  拠点の地震リスク評価やBCPの基礎資料に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2019〜2023年の5年間に気象庁の震源カタログに記録された地震は1,298,456件で、そのうち人が揺れを感じた有感地震は9,902回、全体の0.76%でした。有感地震は1日あたり平均5回以上起きています。震度4以上は231回、震度6弱以上は7回です。日本周辺のマグニチュード5以上の地震552件は太平洋側の沖合に集中していて、震源は西へ行くほど深くなります。

この記事では、気象庁が公開する[震源カタログ（地震月報カタログ編）](https://www.data.jma.go.jp/eqev/data/bulletin/index.html)を使い、2019〜2023年の地震を場所・深さ・規模で集計しました。使用するテーブルは `jma.main.mart_jma_hypocenters` で、地震1回ごとに発生時刻・緯度経度・深さ・マグニチュード・最大震度が記録されています。事業継続計画（BCP）や拠点の分散を検討するときに、ハザードマップが示す将来の想定と合わせて、実際に観測された地震の分布を確認するための材料になります。

## 記録された地震のうち、人が揺れを感じたのは0.76%

5年間の記録総数と、そのうち有感地震（最大震度が観測された地震）の件数と比率です。最大震度が記録されていない地震は、有感地震に含めていません。

```sql
SELECT count(*) AS 記録総数, count(*) FILTER(WHERE max_intensity_code IS NOT NULL AND max_intensity_code <> '') AS 有感地震数, ROUND(count(*) FILTER(WHERE max_intensity_code IS NOT NULL AND max_intensity_code <> '') * 100.0 / count(*), 2) AS 有感率パーセント FROM jma.main.mart_jma_hypocenters
```

約130万件の記録の大半は、観測網では捉えられても人には感じられない微小な地震です。有感地震は9,902回で、全体の0.76%です。5年間で約9,900回なので、1日あたり平均5回以上、日本のどこかで人が揺れを感じています。

有感地震を最大震度別に並べました。最大震度は、その地震で全国のいずれかの観測点が記録した最も強い震度で、特定の地点の揺れではありません。

```chart
{
  "layer": [
    {
      "data": {"name": "intensity"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [{"field": "label", "type": "nominal"}, {"field": "n", "type": "quantitative"}],
        "x": {
          "field": "label",
          "type": "nominal",
          "axis": {"title": "最大震度", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"type": "log"},
          "stack": null,
          "axis": {"title": "地震の回数（対数目盛）", "grid": true}
        }
      }
    }
  ]
}
```

有感地震で最も多いのは震度1の6,497回で、震度が上がるほど回数は急激に減ります（縦軸は対数目盛）。震度4以上は5年間で231回、震度6弱以上は7回でした。マグニチュードや震度が1段階上がるごとに、地震の回数はおおむね一桁減ります。

震度6弱以上の7回を個別に並べます。震源地の名称は原データでは英語表記なので、この7件だけ日本語にしています。

```sql
SELECT strftime(origin_time, '%Y-%m-%d') AS 発生日, CASE region WHEN 'E OFF FUKUSHIMA PREF' THEN '福島県沖' WHEN 'W OFF YAMAGATA PREF' THEN '山形県沖' WHEN 'NOTO PENINSULA REGION' THEN '能登地方' WHEN 'NORTHERN ARIAKEKAI REG' THEN '有明海' WHEN 'ISHIKARI DEPRESSION' THEN '石狩地方' ELSE region END AS 震源地, ROUND(magnitude, 1) AS マグニチュード, ROUND(depth_km) AS 深さkm, max_intensity AS 最大震度 FROM jma.main.mart_jma_hypocenters WHERE max_intensity_code IN ('C', 'D') ORDER BY origin_time
```

福島県沖では2021年と2022年に続けてマグニチュード7を超える地震が起き、どちらも最大震度6強を記録しています。能登地方では2022年と2023年に強い揺れが繰り返し起きており、この時期にこの地域で地震活動が活発になっていました。強い揺れは特定の時期と地域に集中して起きるので、年間の平均回数だけではこの偏りを把握できません。

## マグニチュード5以上の地震は、太平洋側の沖合に集中している

マグニチュード5以上の地震の震源を地図にしました。気象庁の震源カタログは海外の大地震も収録しているので、日本周辺（緯度24〜46度・経度122〜149度）に絞っています。この範囲でマグニチュード5以上の地震は552件で、色は震源の深さを表します。

```map
type: map
layers:
  - from: quakemap
    lng: lon
    lat: lat
    color: depth
    label: mag
lng: 140
lat: 37
zoom: 3.6
```

震源は太平洋側の沖合に帯状に集中しています。とくに東北から関東の東方沖に多くの点があり、日本の地震活動の中心になっています。太平洋沖の震源は浅く（青）、内陸や日本海側に向かうほど深く（赤）なります。太平洋プレートが日本列島の下に沈み込んでいるため、震源は西へ行くほど深くなります。

## マグニチュード3以上の地震は、深さ30〜70kmが最も多い

震源の深さは被害の出方に関係します。同じ規模でも、浅い地震は地表の揺れが大きくなりやすく、断層が地表に現れることもあります。日本周辺のマグニチュード3以上の地震を深さ帯別に集計しました。

```chart
{
  "layer": [
    {
      "data": {"name": "depthband"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "band", "type": "nominal"}, {"field": "n", "type": "quantitative"}],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "震源の深さ", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "地震の回数", "grid": true}
        }
      }
    }
  ]
}
```

最も多いのは深さ30〜70kmの帯で11,270回、次いで地表に近い0〜30kmが8,487回です。150km以上の深い地震も3,487回あります。マグニチュード5以上に限っても、震源が500kmより深い地震が記録されています。地下数百kmで起きる深発地震は、震源から離れた場所が大きく揺れる「異常震域」を生むことがあるので、震源からの距離だけでは揺れの大きさを判断できません。

## 有感地震は年間1,500〜2,400回で、2021年が最も多い

有感地震の回数の年ごとの推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "annual"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"y\"]) && isValid(datum[\"felt\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "y", "type": "quantitative"},
          {"field": "felt", "type": "quantitative"}
        ],
        "x": {
          "field": "y",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "felt",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "有感地震の回数", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

有感地震の回数は年間およそ1,500〜2,400回で推移しており、2021年の2,423回が最も多くなっています。大きな地震が起きた年やその翌年は、余震が加わって回数が増える傾向があります。ある年の地震が多いか少ないかは、単年の回数ではなく複数年の水準と比較して判断する必要があります。

## まとめ

- 2019〜2023年に記録された地震約130万件のうち、有感地震は9,902回で0.76%。震度が上がるほど回数は一桁ずつ減り、震度6弱以上は7回
- マグニチュード5以上の地震は太平洋側の沖合に帯状に集中し、震源は西へ行くほど深くなる
- 震源の深さは地表付近から500km超まで分布し、深発地震では震源から離れた場所が大きく揺れることがある

## データの出典

本記事は気象庁の[地震月報（カタログ編）](https://www.data.jma.go.jp/eqev/data/bulletin/index.html)をもとにした `jma.main.mart_jma_hypocenters` を、2026-07-11 時点で取得して集計しています。対象期間は2019年から2023年までの5年間で、この期間に収録された震源は1,298,456件です。

Queriaは、気象庁の震源カタログの列名・単位・文字コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[震源カタログのテーブル](/datasets/queria/jma/main/mart_jma_hypocenters)を緯度経度で絞り込むと、自社の拠点の周辺で過去に起きた地震を確認できます。

```sql id=intensity
SELECT max_intensity AS label, count(*) AS n FROM jma.main.mart_jma_hypocenters WHERE max_intensity_code IS NOT NULL AND max_intensity_code <> '' GROUP BY max_intensity, max_intensity_code ORDER BY max_intensity_code
```

```sql id=quakemap
SELECT latitude AS lat, longitude AS lon, ROUND(magnitude, 1) AS mag, ROUND(depth_km) AS depth, (magnitude - 4) * 2.5 AS size FROM jma.main.mart_jma_hypocenters WHERE magnitude >= 5 AND latitude BETWEEN 24 AND 46 AND longitude BETWEEN 122 AND 149 ORDER BY magnitude
```

```sql id=depthband
SELECT CASE WHEN depth_km < 30 THEN '0–30km' WHEN depth_km < 70 THEN '30–70km' WHEN depth_km < 150 THEN '70–150km' ELSE '150km以上' END AS band, count(*) AS n FROM jma.main.mart_jma_hypocenters WHERE depth_km IS NOT NULL AND magnitude >= 3 AND latitude BETWEEN 24 AND 46 AND longitude BETWEEN 122 AND 149 GROUP BY 1 ORDER BY min(depth_km)
```

```sql id=annual
SELECT year(origin_time) AS y, count(*) AS felt FROM jma.main.mart_jma_hypocenters WHERE max_intensity_code IS NOT NULL AND max_intensity_code <> '' GROUP BY 1 ORDER BY 1
```
