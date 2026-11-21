---
title: 特定健診で血糖の値が糖尿病の目安を超える男性の割合は、70代前半で40代前半の約5倍
description: NDBオープンデータの2023年度の特定健診の検査値分布を集計しました。HbA1c 6.5%以上の男性の割合は40代前半の3.28%から70代前半の16.75%へ約5.1倍に増え、収縮期血圧140以上の男女差は70代前半でほぼなくなります。男性のBMI 25以上は沖縄県が46.90%で最も高い値です。
publishedAt: 2026-07-16
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 健康
  - 医療
  - 特定健診
datasets:
  - queria/mhlw
  - queria/nlftp
sources:
  - title: 第11回NDBオープンデータ
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000177221_00017.html
    publisher: 厚生労働省
  - title: 特定健診・特定保健指導について
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000161103.html
    publisher: 厚生労働省
agentHint: HbA1c 6.5%以上（test_item='HbA1C'）の該当割合を都道府県（prefecture）別に集計して、男性の肥満で沖縄が突出したのと同じ顔ぶれが上位に来るか比べて。fiscal_year=2023で都道府県判別不可は除いて
socialAnnounce: |-
  特定健診3,000万件の検査値分布を数えました。

  肥満は男性の50代前半がピーク。血圧140以上の男女差は70代前半でほぼ消え、HbA1c 6.5%以上は男性で40代前半の約5倍に。
  Queriaは医療のオープンデータを整えて公開しています。
---

2023年度の特定健診で、HbA1c 6.5%以上に該当した男性の割合は、40代前半の3.28%から70代前半の16.75%へ約5.1倍に増えます。収縮期血圧140mmHg以上の割合は、40代前半では男性10.88%・女性5.03%と2倍以上の差がありますが、70代前半では男性30.64%・女性29.82%でほぼ同じです。肥満（BMI 25以上）の男性の割合は50代前半の39.52%が最も高く、70代前半では30.81%に下がります。都道府県別では、男性の肥満の割合は沖縄県の46.90%が最も高く、収縮期血圧140以上の割合は山梨県の23.55%が最も高くなっています。

40〜74歳を対象に毎年行われる[特定健康診査](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000161103.html)（いわゆるメタボ健診）は、日本で最も規模の大きい健康診断の一つです。検査結果はレセプト情報・特定健診等情報データベース（NDB）に集められ、集計結果が「NDBオープンデータ」として公開されています。2026年6月に公開された[第11回NDBオープンデータ](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000177221_00017.html)には、2023年度に実施された特定健診の検査値分布が収録されています。

このデータには、平均値に加えて検査値の分布が収録されています。検査項目ごとに値の階級（例えばBMIなら「25.0以上30.0未満」）別の該当者数が、年齢階級・性別・都道府県の組み合わせで集計されています。本記事では、生活習慣病に関わる3つの指標、肥満（BMI）・血圧（収縮期血圧）・血糖（HbA1c）について、基準以上の人の割合が年齢・性別・地域でどう変わるかを集計します。

## 3つの指標と集計の範囲

使用するのは厚生労働省NDBオープンデータの特定健診 検査値分布（`mhlw.ndb.health_checkup`）です。2023年度分として、BMI・腹囲・血圧・血糖・脂質・肝機能・腎機能・尿検査・眼底検査など25の検査項目が収録されており、それぞれ検査値の階級（`value_class`）× 年齢階級（`age_class`、40〜74歳の5歳刻み7階級）× 性別 × 都道府県別に件数（`count`）を持ちます。都道府県には47都道府県のほか「都道府県判別不可」という区分があり、全国の値には含め、県別の集計では除外します。

本記事で使う3つの指標と、集計する範囲は次のとおりです。基準以上の割合は、該当する階級の件数の合計を、その検査項目の全階級の件数の合計で割った値です。検査項目ごとに実施件数が異なるので、指標ごとに分母は異なります。

| 指標               | 収録されている階級        | 本記事で集計する範囲                   |
| ------------------ | ------------------------- | -------------------------------------- |
| BMI（kg/m²）       | 18.5未満〜40.0以上の7階級 | 25.0以上の4階級（肥満の目安）          |
| 収縮期血圧（mmHg） | 120未満〜180以上の6階級   | 140以上の3階級（高血圧の診断基準水準） |
| HbA1c（%・NGSP値） | 5.6未満〜8.4以上の6階級   | 6.5以上の3階級（糖尿病型の目安）       |

全国の件数と割合です。

```sql
SELECT '肥満（BMI 25以上・男性）' AS 指標, SUM(count) AS 検査件数, ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 1) AS '該当割合（%）' FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '男' UNION ALL SELECT '肥満（BMI 25以上・女性）', SUM(count), ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 1) FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '女' UNION ALL SELECT '収縮期血圧 140mmHg以上（男女計）', SUM(count), ROUND(100.0 * SUM(CASE WHEN value_class IN ('140以上160未満','160以上180未満','180以上') THEN count ELSE 0 END) / SUM(count), 1) FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = '収縮期血圧' UNION ALL SELECT 'HbA1c 6.5%以上（男女計）', SUM(count), ROUND(100.0 * SUM(CASE WHEN value_class IN ('6.5以上8.0未満','8.0以上8.4未満','8.4以上') THEN count ELSE 0 END) / SUM(count), 1) FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'HbA1C'
```

BMIの検査件数は男女合わせて約3,094万件です。受診者全体では、BMI 25以上は男性の36.6%・女性の21.4%、収縮期血圧140mmHg以上は17.8%、HbA1c 6.5%以上は7.3%です。これは40〜74歳の受診者全体の値で、年齢と性別で分けると、指標ごとに異なる傾向があります。

この健診データは服薬中の人も含む1回の測定値の分布なので、そこから計算した割合は医学的な有病率とは異なります。本記事では「基準となる階級以上に該当した受診者の割合」として扱います。

## 血圧と血糖の割合は年齢とともに上がり、肥満の割合は50代前半が最も高い

3つの指標について、基準以上に該当する割合を年齢階級別・男女別に並べました。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "bmi_m"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_class\"]) && isValid(datum[\"pct\"]) ? 0 : 1",
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
          {"field": "age_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "age_class",
          "type": "nominal",
          "axis": {"title": "年齢階級", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "基準以上の割合（%）", "grid": true}
        },
        "color": {
          "datum": "BMI 25以上・男",
          "type": "nominal",
          "scale": {
            "domain": [
              "BMI 25以上・男",
              "BMI 25以上・女",
              "収縮期血圧140以上・男",
              "収縮期血圧140以上・女",
              "HbA1c 6.5以上・男",
              "HbA1c 6.5以上・女"
            ],
            "range": ["#3b82f6", "#93c5fd", "#ef4444", "#fca5a5", "#22c55e", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bmi_f"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_class\"]) && isValid(datum[\"pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#93c5fd",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "age_class",
          "type": "nominal",
          "axis": {"title": "年齢階級", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "基準以上の割合（%）", "grid": true}
        },
        "color": {
          "datum": "BMI 25以上・女",
          "type": "nominal",
          "scale": {
            "domain": [
              "BMI 25以上・男",
              "BMI 25以上・女",
              "収縮期血圧140以上・男",
              "収縮期血圧140以上・女",
              "HbA1c 6.5以上・男",
              "HbA1c 6.5以上・女"
            ],
            "range": ["#3b82f6", "#93c5fd", "#ef4444", "#fca5a5", "#22c55e", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bp_m"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_class\"]) && isValid(datum[\"pct\"]) ? 0 : 1",
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
          {"field": "age_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "age_class",
          "type": "nominal",
          "axis": {"title": "年齢階級", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "基準以上の割合（%）", "grid": true}
        },
        "color": {
          "datum": "収縮期血圧140以上・男",
          "type": "nominal",
          "scale": {
            "domain": [
              "BMI 25以上・男",
              "BMI 25以上・女",
              "収縮期血圧140以上・男",
              "収縮期血圧140以上・女",
              "HbA1c 6.5以上・男",
              "HbA1c 6.5以上・女"
            ],
            "range": ["#3b82f6", "#93c5fd", "#ef4444", "#fca5a5", "#22c55e", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "bp_f"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_class\"]) && isValid(datum[\"pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#fca5a5",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "age_class",
          "type": "nominal",
          "axis": {"title": "年齢階級", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "基準以上の割合（%）", "grid": true}
        },
        "color": {
          "datum": "収縮期血圧140以上・女",
          "type": "nominal",
          "scale": {
            "domain": [
              "BMI 25以上・男",
              "BMI 25以上・女",
              "収縮期血圧140以上・男",
              "収縮期血圧140以上・女",
              "HbA1c 6.5以上・男",
              "HbA1c 6.5以上・女"
            ],
            "range": ["#3b82f6", "#93c5fd", "#ef4444", "#fca5a5", "#22c55e", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "hba1c_m"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_class\"]) && isValid(datum[\"pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "age_class",
          "type": "nominal",
          "axis": {"title": "年齢階級", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "基準以上の割合（%）", "grid": true}
        },
        "color": {
          "datum": "HbA1c 6.5以上・男",
          "type": "nominal",
          "scale": {
            "domain": [
              "BMI 25以上・男",
              "BMI 25以上・女",
              "収縮期血圧140以上・男",
              "収縮期血圧140以上・女",
              "HbA1c 6.5以上・男",
              "HbA1c 6.5以上・女"
            ],
            "range": ["#3b82f6", "#93c5fd", "#ef4444", "#fca5a5", "#22c55e", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "hba1c_f"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_class\"]) && isValid(datum[\"pct\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#86efac",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_class", "type": "nominal"},
          {"field": "pct", "type": "quantitative"}
        ],
        "x": {
          "field": "age_class",
          "type": "nominal",
          "axis": {"title": "年齢階級", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "基準以上の割合（%）", "grid": true}
        },
        "color": {
          "datum": "HbA1c 6.5以上・女",
          "type": "nominal",
          "scale": {
            "domain": [
              "BMI 25以上・男",
              "BMI 25以上・女",
              "収縮期血圧140以上・男",
              "収縮期血圧140以上・女",
              "HbA1c 6.5以上・男",
              "HbA1c 6.5以上・女"
            ],
            "range": ["#3b82f6", "#93c5fd", "#ef4444", "#fca5a5", "#22c55e", "#86efac"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

3つの指標は、年齢による変化の仕方がそれぞれ異なります。

肥満（青系）の割合は、年齢とともに増えてはいません。男性は40代前半の34.83%から50代前半の39.52%まで上がったあと下がり、70代前半では30.81%と40代より低くなります。女性は全年齢で19〜22%の範囲にあり、ほぼ横ばいです。

収縮期血圧（赤系）の割合は男女とも年齢とともに上がり続け、男女差は小さくなります。40代前半では男性10.88%・女性5.03%と2倍以上の差があり、年齢とともに女性の割合が速く上がって、70代前半では男性30.64%・女性29.82%とほぼ同じになります。

血糖（緑系）の割合も年齢とともに上がり続けます。HbA1c 6.5%以上の割合は、男性で40代前半の3.28%から70代前半の16.75%へ約5.1倍、女性では1.20%から9.27%へ約7.7倍に増えます。男女差は小さくなりますが、70代前半でも男性が女性の約1.8倍です。

この図は2023年度の値を年齢階級別に並べたもので、同じ人を追跡した変化ではありません。70代の肥満の割合が40代より低いのは、加齢による体格の変化に加えて、世代ごとの食生活の違いや、健康状態の良い人ほど健診を受け続けやすいことも影響していると考えられます。

## 男性の肥満の割合は、沖縄県が46.90%で最も高い

肥満は男女差が大きいので、割合の高い男性に絞って47都道府県を比較しました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "bmi_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "BMI 25以上の割合（%・男性）", "grid": true}
        },
        "y": {
          "field": "prefecture",
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
      "data": {"name": "bmi_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "BMI 25以上の割合（%・男性）", "grid": true}
        },
        "y": {
          "field": "prefecture",
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
      "data": {"name": "bmi_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "prefecture", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "BMI 25以上の割合（%・男性）", "grid": true}
        },
        "y": {
          "field": "prefecture",
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

最も高いのは沖縄県の46.90%で、受診した男性のほぼ2人に1人がBMI 25以上に該当します。2位の北海道（41.15%）とは5ポイント以上の差があります。以下、青森県（40.27%）、福島県（39.38%）、宮城県（39.22%）と、北海道・東北の県が上位に並びます。

最も低いのは鳥取県の32.72%で、新潟県（32.82%）、京都府・島根県（ともに33.05%）が続きます。沖縄県と鳥取県の差は14ポイント余りです。最も低い県でも男性の3人に1人近くが該当しており、どの県でも割合は高い水準にあります。

## 収縮期血圧140以上の割合は、山梨県が23.55%で最も高く、東京都が14.07%で最も低い

収縮期血圧140mmHg以上の割合（男女計）を地図にしました。色が濃いほど割合が高い県です。

```map
type: map
layers:
  - from: bp_map
    geojson: geojson
    color: value
    label: pref_name
    name: "140mmHg以上の割合（%）"
lng: 137
lat: 36.5
zoom: 4
```

最も高いのは山梨県の23.55%で、山形県（23.10%）、鳥取県（22.53%）、岩手県（22.22%）、秋田県（22.16%）が続きます。東北から甲信、山陰にかけての県の色が濃く、首都圏や大阪府など大都市圏は色が薄くなっています。最も低いのは東京都の14.07%、次いで神奈川県の14.97%で、山梨県と東京都では約1.7倍の差があります。

この割合は県ごとの受診者の年齢構成を調整していません。血圧の割合は年齢とともに大きく上がるので、現役世代の被保険者が多い都市部は低く、受診者の年齢層が高い県は高く出やすくなります。肥満で上位だった沖縄県や北海道は血圧では上位に入らず、内陸・日本海側の県が上位に並ぶので、指標によって上位の県は異なります。

## まとめ

特定健診の検査値分布（BMIの検査件数は男女合計で約3,094万件）を集計した結果は次のとおりです。

- 肥満（BMI 25以上）は男性36.6%・女性21.4%です。男性は50代前半の39.52%が最も高く、70代前半には30.81%まで下がります
- 収縮期血圧140mmHg以上の割合は男女とも年齢とともに上がり、40代前半で2倍以上あった男女差は70代前半でほぼなくなります（男性30.64%・女性29.82%）
- HbA1c 6.5%以上の割合は男性で3.28%から16.75%へ約5.1倍、女性で1.20%から9.27%へ約7.7倍に増え、男女差は小さくなりますが残ります
- 都道府県別に上位の県は指標ごとに異なり、男性の肥満は沖縄県46.90%から鳥取県32.72%まで、収縮期血圧140以上は山梨県23.55%から東京都14.07%まで（約1.7倍）でした

## データの出典

本記事は厚生労働省の[第11回NDBオープンデータ](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000177221_00017.html)に収録された[特定健康診査](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000161103.html)の検査値分布を 2026-07-16 時点で取得して集計しています。対象は2023年度（`fiscal_year = 2023`）に実施された特定健診で、受診者は40〜74歳です。

Queriaは、NDBオープンデータなどの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルや列の意味をメタデータとして付けて公開しています。本記事で使った[特定健診 検査値分布テーブル](/datasets/queria/mhlw/ndb/health_checkup)には腹囲・中性脂肪・肝機能など残りの20あまりの検査項目も収録されており、ほかの指標や地域についても同じ方法で割合を集計できます。

```sql id=bmi_m
SELECT age_class, ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '男' GROUP BY age_class ORDER BY age_class
```

```sql id=bmi_f
SELECT age_class, ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '女' GROUP BY age_class ORDER BY age_class
```

```sql id=bp_m
SELECT age_class, ROUND(100.0 * SUM(CASE WHEN value_class IN ('140以上160未満','160以上180未満','180以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = '収縮期血圧' AND sex = '男' GROUP BY age_class ORDER BY age_class
```

```sql id=bp_f
SELECT age_class, ROUND(100.0 * SUM(CASE WHEN value_class IN ('140以上160未満','160以上180未満','180以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = '収縮期血圧' AND sex = '女' GROUP BY age_class ORDER BY age_class
```

```sql id=hba1c_m
SELECT age_class, ROUND(100.0 * SUM(CASE WHEN value_class IN ('6.5以上8.0未満','8.0以上8.4未満','8.4以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'HbA1C' AND sex = '男' GROUP BY age_class ORDER BY age_class
```

```sql id=hba1c_f
SELECT age_class, ROUND(100.0 * SUM(CASE WHEN value_class IN ('6.5以上8.0未満','8.0以上8.4未満','8.4以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'HbA1C' AND sex = '女' GROUP BY age_class ORDER BY age_class
```

```sql id=bmi_top
WITH ranked AS (SELECT prefecture, ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct, ROW_NUMBER() OVER (ORDER BY SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) * 1.0 / SUM(count) DESC, prefecture) AS rn FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '男' AND prefecture != '都道府県判別不可' GROUP BY prefecture) SELECT prefecture, pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=bmi_mid
WITH ranked AS (SELECT prefecture, ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct, ROW_NUMBER() OVER (ORDER BY SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) * 1.0 / SUM(count) DESC, prefecture) AS rn FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '男' AND prefecture != '都道府県判別不可' GROUP BY prefecture) SELECT prefecture, pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=bmi_bottom
WITH ranked AS (SELECT prefecture, ROUND(100.0 * SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct, ROW_NUMBER() OVER (ORDER BY SUM(CASE WHEN value_class IN ('25.0以上30.0未満','30.0以上35.0未満','35.0以上40.0未満','40.0以上') THEN count ELSE 0 END) * 1.0 / SUM(count) DESC, prefecture) AS rn FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = 'BMI' AND sex = '男' AND prefecture != '都道府県判別不可' GROUP BY prefecture) SELECT prefecture, pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=bp_map
WITH bp AS (SELECT prefecture, ROUND(100.0 * SUM(CASE WHEN value_class IN ('140以上160未満','160以上180未満','180以上') THEN count ELSE 0 END) / SUM(count), 2) AS pct FROM mhlw.ndb.health_checkup WHERE fiscal_year = 2023 AND test_item = '収縮期血圧' AND prefecture != '都道府県判別不可' GROUP BY prefecture) SELECT b.prefecture AS pref_name, ST_AsGeoJSON(p.geometry) AS geojson, b.pct AS value, ROW_NUMBER() OVER (ORDER BY b.prefecture) - 1 AS row_id FROM bp b JOIN nlftp.boundary.prefecture p ON b.prefecture = p.prefecture_name
```
