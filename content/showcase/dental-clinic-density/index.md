---
title: 高齢化率がほぼ同じ徳島県と島根県で、人口あたりの歯科診療所の数は1.5倍違う
description: 2023年の人口10万人あたり歯科診療所数は、東京都の75.3が最も多く、福井県・島根県の38.6の約2倍です。高齢化率が0.5ポイントしか違わない徳島県と島根県でも59.1と38.6で1.5倍の差があり、高齢化率では診療所の多さを説明できません。
publishedAt: 2026-05-25
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 医療
  - 歯科
  - 人口
  - 開業
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 医療施設調査
    url: https://www.mhlw.go.jp/toukei/list/79-1.html
    publisher: 厚生労働省
  - title: 令和4年（2022年）医師・歯科医師・薬剤師統計
    url: https://www.mhlw.go.jp/toukei/saikin/hw/ishi/22/index.html
    publisher: 厚生労働省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 2022年の人口10万人あたり歯科医師数（I6200）を都道府県別に出して。2023年の歯科診療所数の密度ランキングと同じ顔ぶれが上位・下位に並ぶか比べて
socialAnnounce: |-
  都道府県と市区町村の歯科診療所数を、人口10万人あたりの密度に揃えて可視化しました。

  開業候補地の評価や既存医院の競合環境の把握に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2023年の人口10万人あたりの歯科診療所数は、東京都の75.3が最も多く、最も少ない福井県と島根県の38.6の約2倍です。この差は高齢化率では説明できません。高齢化率が0.5ポイントしか違わない徳島県（35.4%）と島根県（34.9%）で、人口10万人あたりの歯科診療所数は59.1と38.6で、1.5倍の差があります。

歯科医院の新規開業や継承を検討するとき、候補地の需要の指標としてよく使われるのが高齢化率です。高齢者ほど通院の頻度が高いので、高齢化の進んだ地域には診療所も多いと考えられがちですが、高齢化率で候補地を絞ると、地域にある診療所の多さを見誤ります。この記事では、e-Stat「社会・人口統計体系」の医療施設データから、都道府県と市区町村ごとの歯科診療所数を人口で割り、その分布を確認します。

## 全国の歯科診療所は2016年の68,940施設が最多で、2023年は66,818施設

使うのは、e-Stat「社会・人口統計体系」の都道府県別データ（`i_pref_health`）です。医療提供体制に関する複数のカテゴリが収録されており、今回は主に次の2つを使います。

| コード | 内容                           |
| ------ | ------------------------------ |
| I5103  | 歯科診療所数（年次、1975年〜） |
| I6200  | 歯科医師数（1975年〜）         |

歯科診療所数（`I5103`）のもとは厚生労働省「医療施設調査」、歯科医師数（`I6200`）のもとは同省「[医師・歯科医師・薬剤師統計](https://www.mhlw.go.jp/toukei/saikin/hw/ishi/22/index.html)」です。歯科医師数は1982年までは毎年、それ以降は西暦偶数年だけの調査なので、2つの系列は年が一致しない年があります。

全国の歯科診療所数と歯科医師数の推移です。

```chart
{
  "layer": [
    {
      "data": {"name": "trend_clinics"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"clinics\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "clinics", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "clinics",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "施設・人数", "grid": true}
        },
        "color": {
          "datum": "歯科診療所数",
          "type": "nominal",
          "scale": {"domain": ["歯科診療所数", "歯科医師数"], "range": ["#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend_dentists"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"dentists\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 16}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "dentists", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "dentists",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "施設・人数", "grid": true}
        },
        "color": {
          "datum": "歯科医師数",
          "type": "nominal",
          "scale": {"domain": ["歯科診療所数", "歯科医師数"], "range": ["#3b82f6", "#ec4899"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

歯科診療所数は1975年の32,565施設から増え続け、2016年の68,940施設を最多に減少に転じています。2023年は66,818施設で、前年から937施設減りました。1975年以降で最大の年間減少数です（2番目は2020年の626施設減）。歯科医師数は2020年の107,443人が最多で、2022年は105,267人に減りました。

施設数の伸びが止まる一方で歯科医師数は増えてきたので、1施設あたりの歯科医師数は1975年の1.34人から2022年の1.55人へ増えています。全国の診療所の数が増える時期はすでに終わっており、開業の候補地選びは、診療所の少ない地域を探す作業になっています。

## 人口10万人あたりの歯科診療所数は、東京都の75.3が最多で、福井県・島根県の38.6が最少

2023年の都道府県別の歯科診療所数を人口（`A1101` 総人口）で割り、47都道府県を上位10・中間27・下位10に分けて並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
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
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
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
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
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

最も多いのは東京都の75.3で、大阪府61.7、福岡県59.6と大都市圏が続きますが、4位以降には徳島県（59.1）、和歌山県（57.3）、長崎県（54.3）のような人口規模の小さい県も入ります。最も少ないのは福井県と島根県の38.6で、東京都との差は約2倍です。歯科診療所の多さは、大都市か地方かだけでは説明できません。

この指標は施設の数で、診療できる患者の数ではありません。密度が高い県で、住民1人あたりの診療枠も多いとは限りません。

## 密度の高い県は、大都市圏に加えて徳島県・和歌山県・長崎県など西日本にもある

同じ人口10万人あたり歯科診療所数を、都道府県の境界（`nlftp.boundary.prefecture`）に塗って地図にしました。

```map
type: map
layers:
  - from: pref_map
    geojson: geojson
    color: value
    label: pref_name
    name: "10万人あたり診療所数"
lng: 137
lat: 36.5
zoom: 4
```

色が濃いのは、東京都・大阪府・福岡県のような大都市圏と、徳島県や和歌山県、長崎県といった西日本の県です。北陸（富山42.8・石川42.6・福井38.6）と青森県40.6・島根県38.6・沖縄県40.9・滋賀県39.9は色が薄く、隣り合う県でも密度が異なります。

## 高齢化率が高い県ほど歯科診療所が多いという関係はない

横軸に65歳以上人口の割合（`A1303` ÷ `A1101`）、縦軸に人口10万人あたり歯科診療所数をとりました。

```chart
{
  "layer": [
    {
      "data": {"name": "elderly_scatter"},
      "mark": {"type": "point", "color": "#3b82f6", "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "pref_name", "type": "nominal"},
          {"field": "elderly_pct", "type": "quantitative"},
          {"field": "per_100k", "type": "quantitative"}
        ],
        "x": {
          "field": "elderly_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "65歳以上人口比率（%）", "grid": true}
        },
        "y": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
        }
      }
    },
    {
      "data": {"name": "elderly_scatter"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "elderly_pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "65歳以上人口比率（%）", "grid": true}
        },
        "y": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
        },
        "text": {"field": "pref_name"}
      }
    }
  ]
}
```

高齢化率と歯科診療所の密度のあいだに、強い正の相関はありません。高齢化率が比較的低い東京都（22.8%）・神奈川県（25.9%）・大阪府（27.7%）は密度が75.3・53.1・61.7と高く、高齢化率の高い秋田県（39.1%）・青森県（35.2%）・島根県（34.9%）は44.2・40.6・38.6と低くなっています。

高齢化率がほぼ同じ県どうしでも、密度には大きな差があります。冒頭の徳島県（35.4%）と島根県（34.9%）の59.1対38.6は、高齢化率の差が0.5ポイント以内の県の組み合わせの中で、密度の差が最も大きい例です。次いで徳島県と青森県（35.2%）の59.1対40.6、山梨県（31.8%）と福井県（31.6%）の52.5対38.6が続きます。

## 人口5万人以上の市で最も密度が低いのは南魚沼市の25.0、最も高いのは千代田区の510.0

市区町村別データ（`i_municipal_health`、`a_municipal_population`）から、住民基本台帳人口（`A2101`）が5万人以上の市区町村に絞り、2023年の人口10万人あたり歯科診療所数を出しました。診療所の商圏が成り立つ規模の市区町村に絞ることで、開業の判断に使えるリストになります。

ここでの分母は日本人住民に限った住民基本台帳人口で、都道府県の集計で使った総人口（`A1101`、外国人住民を含む）とは範囲が違います。外国人住民の多い都心区や工業都市では分母が小さくなり、密度が高めに出るので、都道府県の数値とは比較せず、市区町村どうしで比較してください。

密度が低い10市区町村です。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "muni_low"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市区町村"},
          "sort": null
        }
      }
    }
  ]
}
```

新潟県南魚沼市が25.0と最も低く、石川県白山市（28.0）、福井県坂井市（28.7）、沖縄県うるま市（28.8）、静岡県袋井市（29.0）と続きます。いずれも人口5万人以上の市で、商圏の規模はあるのに診療所が少ないので、開業候補地を最初に絞り込むときの対象になります。この集計は市区町村をまたいだ通院を含まないので、隣の市に診療所が集まっている場合は、密度が低くても需要が満たされていないとは限りません。

密度が高い10市区町村です。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "muni_high"},
      "mark": {"type": "bar", "color": "#ef4444"},
      "encoding": {
        "tooltip": [
          {"field": "per_100k", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "per_100k",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口10万人あたり歯科診療所数", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "市区町村"},
          "sort": null
        }
      }
    }
  ]
}
```

東京都千代田区が510.0で最も高く、中央区（271.5）・港区（242.0）・大阪市中央区（241.4）・渋谷区（197.6）が続きます。いずれも住民の数に対して昼間人口（オフィスで働く人や訪れる人）が多いので、住民の数だけを分母にすると密度が高く出ます。名古屋市中区（179.1）や神戸市中央区（137.3）も含め、上位10件はすべて三大都市圏と政令市の中心部です。このランキングには政令市の市全体の行と、その行政区の行がどちらも含まれており、「大阪市 中央区」は行政区の値です。

## このデータをどう業務に活かすか

- 候補地の絞り込み: 候補エリアを最初に絞り込む段階で、市区町村どうしで比較したときに密度が下位になる市区町村を抽出する。都道府県の数値は分母の定義が違うので基準に使わない
- 競合環境の把握: 既存の医院は、自院のある市区町村と近隣の市区町村の密度の差を確認し、競合の多さや新しい医院が開業する可能性を評価する
- 需要の指標との区別: この記事で見たとおり、候補地の高齢化率は診療所の密度をほとんど説明しません。需要の指標として使うときは、診療所の多さとは別の指標として扱う

ここでの数字は候補地を最初に絞り込むための参考値です。実際の判断では、徒歩や自動車で到達できる診療圏の分析、競合医院の専門分野、対象とする患者層の構成などと組み合わせてください。

## まとめ

- 歯科診療所の密度は高齢化率では説明できません。高齢化率が0.5ポイントしか違わない徳島県（35.4%）と島根県（34.9%）で、人口10万人あたりの診療所数は59.1と38.6で、1.5倍の差があります
- 都道府県別の密度は、最も高い東京都の75.3から最も低い福井県・島根県の38.6まで、約2倍の差があります
- 人口5万人以上の市区町村にも密度の低い市があり、商圏分析と組み合わせると開業候補地の絞り込みに使えます
- 全国の歯科診療所は2016年の68,940施設が最多で、2023年は66,818施設です。前年からの937施設減は1975年以降で最大の年間減少数です
- 歯科医師は2020年の107,443人が最多で、2022年は105,267人です

## データの出典

本記事は総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)を e-Stat から取得し、2026年8月8日時点のデータで集計しています。歯科診療所数（`I5103`）のもとは厚生労働省の[医療施設調査](https://www.mhlw.go.jp/toukei/list/79-1.html)、歯科医師数（`I6200`）のもとは[医師・歯科医師・薬剤師統計](https://www.mhlw.go.jp/toukei/saikin/hw/ishi/22/index.html)です。地域別の値は歯科診療所数が2023年、歯科医師数が2022年で、地図の境界線には国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、e-Statの医療施設データなどの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[都道府県別の医療施設テーブル](/datasets/queria/e_stat/ssds/i_pref_health)から、自院や候補地のある地域の歯科診療所数を取得できます。

```sql id=trend_clinics
SELECT year, MAX(TRY_CAST(value AS DOUBLE)) AS clinics FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5103' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2023 GROUP BY year ORDER BY year
```

```sql id=trend_dentists
SELECT year, MAX(TRY_CAST(value AS DOUBLE)) AS dentists FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I6200' AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2022 GROUP BY year ORDER BY year
```

```sql id=pref_top
WITH clinics AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5103' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT c.area_name, ROUND(c.val / p.val * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY c.val / p.val DESC, c.area_name) AS rn FROM clinics c JOIN pop p ON c.area = p.area ) SELECT area_name, per_100k FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH clinics AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5103' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT c.area_name, ROUND(c.val / p.val * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY c.val / p.val DESC, c.area_name) AS rn FROM clinics c JOIN pop p ON c.area = p.area ) SELECT area_name, per_100k FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH clinics AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5103' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), ranked AS ( SELECT c.area_name, ROUND(c.val / p.val * 100000, 1) AS per_100k, ROW_NUMBER() OVER (ORDER BY c.val / p.val DESC, c.area_name) AS rn FROM clinics c JOIN pop p ON c.area = p.area ) SELECT area_name, per_100k FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=pref_map
WITH clinics AS ( SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5103' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name ), pop AS ( SELECT area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name ), rates AS ( SELECT c.area_name, ROUND(c.val / p.val * 100000, 1) AS per_100k FROM clinics c JOIN pop p ON c.area_name = p.area_name ) SELECT r.area_name AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, r.per_100k AS value, ROW_NUMBER() OVER (ORDER BY r.area_name) - 1 AS row_id FROM rates r JOIN nlftp.boundary.prefecture p ON r.area_name = p.prefecture_name
```

```sql id=elderly_scatter
WITH clinics AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_pref_health WHERE cat01 = 'I5103' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ), elderly AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1303' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area ) SELECT c.area_name AS pref_name, ROUND(c.val / p.val * 100000, 1) AS per_100k, ROUND(e.val / p.val * 100, 1) AS elderly_pct FROM clinics c JOIN pop p ON c.area = p.area JOIN elderly e ON c.area = e.area
```

```sql id=muni_low
WITH clinics AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_municipal_health WHERE cat01 = 'I5103' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND TRY_CAST(value AS DOUBLE) >= 50000 GROUP BY area ) SELECT area_name, per_100k FROM ( SELECT c.area_name, ROUND(c.val / p.val * 100000, 1) AS per_100k FROM clinics c JOIN pop p ON c.area = p.area ORDER BY per_100k ASC, area_name LIMIT 10 ) ORDER BY per_100k DESC, area_name
```

```sql id=muni_high
WITH clinics AS ( SELECT area, area_name, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.i_municipal_health WHERE cat01 = 'I5103' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area, area_name ), pop AS ( SELECT area, MAX(TRY_CAST(value AS DOUBLE)) AS val FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2101' AND year = 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND TRY_CAST(value AS DOUBLE) >= 50000 GROUP BY area ) SELECT c.area_name, ROUND(c.val / p.val * 100000, 1) AS per_100k FROM clinics c JOIN pop p ON c.area = p.area ORDER BY per_100k DESC, c.area_name LIMIT 10
```
