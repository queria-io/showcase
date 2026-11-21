---
title: 職場のけがの発生頻度は10年で31%上がり、47都道府県のうち43で上昇した
description: 職場のけがの発生頻度を表す度数率は2013年の1.58が最も低く、3年平均では10年で31%上がり、47都道府県のうち43で上昇しました。重さを表す強度率は同じ10年で13%下がっています。
publishedAt: 2026-06-02
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 労働
  - 安全
  - 都道府県
datasets:
  - queria/e_stat
sources:
  - title: 労働災害動向調査
    url: https://www.mhlw.go.jp/toukei/list/44-23.html
    publisher: 厚生労働省
  - title: 社会・人口統計体系 Ｆ 労働
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000010106
    publisher: 総務省統計局
  - title: 令和５年労働災害動向調査（事業所調査（事業所規模100人以上）及び総合工事業調査）の概況
    url: https://www.mhlw.go.jp/toukei/itiran/roudou/saigai/23/
    publisher: 厚生労働省
  - title: 項目定義 Ｆ 労働
    url: https://www.e-stat.go.jp/koumoku/koumoku_teigi/F
    publisher: 総務省統計局
agentHint: 度数率(F8101)と強度率(F8102)を都道府県別に2011年から2023年まで出して、両方が同時に下がった年が多い県を数えて
socialAnnounce: |-
  職場のけがの発生頻度は2013年で下げ止まり、10年で3割増えました。47都道府県のうち43で上がっています。

  ただし重さを表す強度率は下がっていて、強度率から計算した死傷者1人あたりの労働損失日数は64.7日から42.9日に。増えたのは休みの短い災害のほうでした。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

働いた時間あたりのけがの発生頻度（度数率）は、2011〜2013年の平均から2021〜2023年の平均までの10年で31%上がり、47都道府県のうち43で上昇しました。同じ10年で、災害の重さを表す強度率は13%下がり、強度率から計算した死傷者1人あたりの労働損失日数は64.7日から42.9日になりました。増えたのは、休んだ日数の短い災害です。

厚生労働省の[労働災害動向調査](https://www.mhlw.go.jp/toukei/list/44-23.html)が測っている度数率は、1975年の6.75から2013年の1.58まで下がり、4分の1以下になりました。2013年以降は上がり、2023年は2.14です。

## 度数率はけがの頻度を、強度率はけがの重さを表す

[労働安全衛生法](https://laws.e-gov.go.jp/document?lawid=347AC0000000057)に基づいて実施される労働災害動向調査は、発生の頻度と災害の重さを別々の指標で公表しています。

| コード | 指標名         | 計算方法                               |
| ------ | -------------- | -------------------------------------- |
| F8101  | 労働災害度数率 | 死傷者数 ÷ 延べ実労働時間数 × 100万    |
| F8102  | 労働災害強度率 | 労働損失日数 ÷ 延べ実労働時間数 × 1000 |

分母はどちらも延べ実労働時間数なので、強度率を度数率で割ると、死傷者1人あたりの労働損失日数（強度率 ÷ 度数率 × 1000）を計算できます。労働損失日数は[項目定義 Ｆ 労働](https://www.e-stat.go.jp/koumoku/koumoku_teigi/F)の基準で決まり、死亡と永久全労働不能が7,500日、身体障害等級に応じた永久一部労働不能が50〜5,500日、休業だけで復帰した場合は暦日の休業日数に300/365を掛けた日数です。死亡が1件あると7,500日が加わるので、強度率は重い災害があったかどうかで大きく変わります。

## 度数率は2013年の1.58が最も低く、2023年は2.14に上がった

```chart
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"freq_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25, "color": "#ef4444"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "freq_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "freq_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "度数率（死傷者数/100万時間）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": 2013, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0)"}},
        "y2": {"value": {"expr": "height * (1 - 1)"}}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {
        "type": "text",
        "lineBreak": "\n",
        "align": "right",
        "fontSize": 11,
        "color": "#64748b"
      },
      "encoding": {
        "x": {"datum": 2013, "type": "quantitative"},
        "y": {"value": {"expr": "height * (1 - 0.93)"}},
        "text": {"value": "2013年 1.58（49年で最低）"}
      }
    }
  ]
}
```

1975年から2023年までの49年分があり、最も低いのは2013年の1.58です。2023年の2.14はその1.35倍です。

公表されているのは、常用労働者30人以上の事業所から無作為に抽出した標本のうち、事業所規模100人以上の事業所を集計した値です。小規模な事業所や一人親方は含まれません。

調査の対象の産業は途中で増えています。項目定義の注意事項によると、2008年に医療・福祉、2011年に農業、2018年に漁業が加わり、厚生労働省は追加の前後で時系列を比較するときの注意を示しています。2018年より後は対象の産業は変わっておらず、その後も度数率は1.83から2.14へ上がっています。

## 10年で度数率は31%上がり、強度率は13%下がった

度数率と強度率を、2011〜2013年の平均を100として並べます。

```chart
{
  "layer": [
    {
      "data": {"name": "index_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"freq_index\"]) ? 0 : 1",
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
          {"field": "freq_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "freq_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011〜2013年平均 = 100", "grid": true}
        },
        "color": {
          "datum": "度数率（発生の頻度）",
          "type": "nominal",
          "scale": {"domain": ["度数率（発生の頻度）", "強度率（災害の重さ）"], "range": ["#ef4444", "#7c3aed"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "index_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"severity_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#7c3aed",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "severity_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "severity_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2011〜2013年平均 = 100", "grid": true}
        },
        "color": {
          "datum": "強度率（災害の重さ）",
          "type": "nominal",
          "scale": {"domain": ["度数率（発生の頻度）", "強度率（災害の重さ）"], "range": ["#ef4444", "#7c3aed"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#94a3b8", "strokeDash": [2, 3]},
      "encoding": {
        "x": {"value": {"expr": "width * 0"}},
        "x2": {"value": {"expr": "width * 1"}},
        "y": {"datum": 100, "type": "quantitative"}
      }
    }
  ]
}
```

度数率は2018年に114.6に上がってから110を下回らず、2023年は134です。強度率は2018年から2023年まで87で、100に戻っていません。3年平均で比較すると、度数率は31%増、強度率は13%減です。

強度率を度数率で割って求めた死傷者1人あたりの労働損失日数は、2011〜2013年の平均が64.7日、2021〜2023年の平均が42.9日で、34%減りました。けが1件あたりの重さは軽くなっています。

この日数は概算です。強度率は小数第2位までしか公表されていないので、0.01の違いで指数は約10ポイント、1人あたりの日数は約5日変わります。2015年だけ指数が68に下がるのは強度率が0.07だったためで、2010年以降のほかの年は0.09から0.11の範囲にあります。

## 度数率は47都道府県のうち43で上がり、中央値は34.7%増

47都道府県のそれぞれについて、2011〜2013年の平均と2021〜2023年の平均を比較しました。同じテーブルにある「全国」の行は除いています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_change_down"},
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
          "axis": {"title": "度数率の変化率（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下がった県",
          "type": "nominal",
          "scale": {"domain": ["下がった県", "上がった県"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_change_up"},
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
          "axis": {"title": "度数率の変化率（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上がった県",
          "type": "nominal",
          "scale": {"domain": ["下がった県", "上がった県"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        }
      }
    }
  ]
}
```

上がったのは47都道府県のうち43で、変化率の中央値は34.7%です。下がったのは鳥取県（-26.2%）・徳島県（-23.2%）・和歌山県（-13.3%）・山口県（-3.6%）の4県だけでした。最も上がったのは長崎県で112.9%です。

同じ10年の強度率は、上がったのが23県、下がったのが24県で、中央値は-2.7%です。けがの頻度はほとんどの県で上がり、重さは県によって上下が分かれています。

この調査は標本調査で、度数率の標準誤差率が産業別・事業所規模別に9〜10%以内になるように抽出されています。都道府県ごとの精度は設定されていないので、県ごとの値の小さな違いは誤差の範囲です。43県が同じ方向に動いたことは、抽出のばらつきの影響を受けにくい結果です。

2011年から2016年までの調査は、東日本大震災の被災地域や避難指示区域を含む市区町村の事業所を対象から除いています。そのため、岩手県・宮城県・福島県の2011〜2013年の値は、ほかの県と同じ範囲の事業所の集計ではありません。

## 度数率の水準は、最も高い沖縄県と最も低い山口県で3.7倍違う

2021〜2023年の平均の度数率は、最も高い沖縄県が3.98、最も低い山口県が1.07で、3.7倍の差があります。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rank_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "freq_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "freq_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "度数率（死傷者数/100万時間）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "上位10（度数率が高い）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（度数率が高い）", "中間27", "下位10（度数率が低い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "freq_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "freq_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "度数率（死傷者数/100万時間）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "中間27",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（度数率が高い）", "中間27", "下位10（度数率が低い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "rank_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "freq_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "freq_rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "度数率（死傷者数/100万時間）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "下位10（度数率が低い）",
          "type": "nominal",
          "scale": {
            "domain": ["上位10（度数率が高い）", "中間27", "下位10（度数率が低い）"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ]
}
```

上位10県のうち、長崎県・鹿児島県・香川県・山形県の4県は、10年前には全国平均の1.60を下回っていました。下位10県のうち7県も10年前より上がっています。

度数率は、その県で働いた時間で重み付けした産業ごとの発生率の平均です。産業の構成が違えば値も変わるので、県の順位は安全管理の優劣を表しません。自社と産業の構成が近い県を選んで比較する使い方になります。

## 業務での使い方

- 自社の度数率・強度率を、全国の水準（2021〜2023年平均で度数率2.10、強度率0.09）と比較する
- 自社の数値が横ばいの場合に、全国が10年で31%上がっていることと合わせて評価する
- 度数率と強度率のどちらが変化したかで対策を分ける。頻度だけが上がっている場合は、重篤化の防止より、けがの発生そのものを減らす施策を先に行う

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)（総務省統計局）の `e_stat.ssds.f_pref_labor` を2026年9月10日時点で集計しています。使った分類コードは労働災害度数率が F8101、労働災害強度率が F8102 で、どちらも単位のない率です。1975年から2023年までの49年分について、全国と47都道府県の48区分の値が入っています。元データは厚生労働省の[労働災害動向調査](https://www.mhlw.go.jp/toukei/list/44-23.html)で、常用労働者30人以上の事業所と、製造業のうち特定の産業に属する10〜29人の事業所から、産業・事業所規模別に層化して無作為抽出した約32,000事業所を対象とする標本調査です。公表値は[事業所規模100人以上の集計](https://www.mhlw.go.jp/toukei/itiran/roudou/saigai/23/)で、集計期間は1月から12月の1年間です。指標の定義と対象産業の変更は[項目定義 Ｆ 労働](https://www.e-stat.go.jp/koumoku/koumoku_teigi/F)によります。

Queria は、社会・人口統計体系のデータを、列名・単位・文字コードを統一し、分類コードや各列の意味の説明を付けて公開しています。本記事で使った[都道府県別の労働テーブル](/datasets/queria/e_stat/ssds/f_pref_labor)から、自社のある県や同業種が集まる県の度数率と強度率を確認できます。

```sql id=trend
SELECT year, MAX(CASE WHEN cat01 = 'F8101' THEN TRY_CAST(value AS DOUBLE) END) AS freq_rate, MAX(CASE WHEN cat01 = 'F8102' THEN TRY_CAST(value AS DOUBLE) END) AS severity_rate FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F8101', 'F8102') AND area_name = '全国' AND year <= 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=coverage
SELECT MIN(year) AS min_year, MAX(year) AS max_year, COUNT(DISTINCT year) AS years, COUNT(DISTINCT area_name) AS areas FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F8101' AND year <= 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL
```

```sql id=index_trend
WITH n AS (SELECT year, MAX(CASE WHEN cat01 = 'F8101' THEN TRY_CAST(value AS DOUBLE) END) AS freq_rate, MAX(CASE WHEN cat01 = 'F8102' THEN TRY_CAST(value AS DOUBLE) END) AS severity_rate FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F8101', 'F8102') AND area_name = '全国' AND year <= 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year), b AS (SELECT AVG(freq_rate) AS f0, AVG(severity_rate) AS s0 FROM n WHERE year BETWEEN 2011 AND 2013) SELECT n.year, ROUND(n.freq_rate / b.f0 * 100, 1) AS freq_index, ROUND(n.severity_rate / b.s0 * 100, 1) AS severity_index FROM n, b WHERE n.year >= 2000 ORDER BY n.year
```

```sql id=national_change
WITH n AS (SELECT year, MAX(CASE WHEN cat01 = 'F8101' THEN TRY_CAST(value AS DOUBLE) END) AS freq_rate, MAX(CASE WHEN cat01 = 'F8102' THEN TRY_CAST(value AS DOUBLE) END) AS severity_rate FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F8101', 'F8102') AND area_name = '全国' AND year <= 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year), a AS (SELECT AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN freq_rate END) AS f_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN freq_rate END) AS f_new, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN severity_rate END) AS s_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN severity_rate END) AS s_new FROM n) SELECT '度数率' AS metric, ROUND(f_old, 3) AS avg_2011_2013, ROUND(f_new, 3) AS avg_2021_2023, ROUND((f_new / f_old - 1) * 100, 1) AS pct_change FROM a UNION ALL SELECT '強度率', ROUND(s_old, 4), ROUND(s_new, 4), ROUND((s_new / s_old - 1) * 100, 1) FROM a UNION ALL SELECT '死傷者1人あたりの労働損失日数（日）', ROUND(s_old / f_old * 1000, 1), ROUND(s_new / f_new * 1000, 1), ROUND(((s_new / f_new) / (s_old / f_old) - 1) * 100, 1) FROM a
```

```sql id=pref_change_down
WITH a AS (SELECT area_name, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN TRY_CAST(value AS DOUBLE) END) AS v_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN TRY_CAST(value AS DOUBLE) END) AS v_new FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F8101' AND area_name <> '全国' AND year BETWEEN 2011 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), r AS (SELECT area_name, (v_new / v_old - 1) * 100 AS pct, ROW_NUMBER() OVER (ORDER BY (v_new / v_old - 1) * 100 DESC, area_name) AS rn FROM a) SELECT area_name, ROUND(pct, 1) AS pct FROM r WHERE pct < 0 ORDER BY rn DESC
```

```sql id=pref_change_up
WITH a AS (SELECT area_name, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN TRY_CAST(value AS DOUBLE) END) AS v_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN TRY_CAST(value AS DOUBLE) END) AS v_new FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F8101' AND area_name <> '全国' AND year BETWEEN 2011 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), r AS (SELECT area_name, (v_new / v_old - 1) * 100 AS pct, ROW_NUMBER() OVER (ORDER BY (v_new / v_old - 1) * 100 DESC, area_name) AS rn FROM a) SELECT area_name, ROUND(pct, 1) AS pct FROM r WHERE pct >= 0 ORDER BY rn DESC
```

```sql id=pref_change_summary
WITH a AS (SELECT cat01, area_name, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN TRY_CAST(value AS DOUBLE) END) AS v_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN TRY_CAST(value AS DOUBLE) END) AS v_new FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F8101', 'F8102') AND area_name <> '全国' AND year BETWEEN 2011 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY cat01, area_name) SELECT CASE cat01 WHEN 'F8101' THEN '度数率' ELSE '強度率' END AS metric, COUNT(*) AS prefectures, SUM(CASE WHEN v_new > v_old THEN 1 ELSE 0 END) AS increased, SUM(CASE WHEN v_new < v_old THEN 1 ELSE 0 END) AS decreased, ROUND(MEDIAN((v_new / v_old - 1) * 100), 1) AS median_pct FROM a GROUP BY cat01 ORDER BY cat01
```

```sql id=rank_top
WITH a AS (SELECT area_name, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN TRY_CAST(value AS DOUBLE) END) AS v_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN TRY_CAST(value AS DOUBLE) END) AS v_new FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F8101' AND area_name <> '全国' AND year BETWEEN 2011 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name, v_old, v_new, ROW_NUMBER() OVER (ORDER BY v_new DESC, area_name) AS rn FROM a) SELECT area_name, ROUND(v_new, 2) AS freq_rate, ROUND(v_old, 2) AS freq_rate_2011_2013 FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rank_mid
WITH a AS (SELECT area_name, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN TRY_CAST(value AS DOUBLE) END) AS v_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN TRY_CAST(value AS DOUBLE) END) AS v_new FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F8101' AND area_name <> '全国' AND year BETWEEN 2011 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name, v_old, v_new, ROW_NUMBER() OVER (ORDER BY v_new DESC, area_name) AS rn FROM a) SELECT area_name, ROUND(v_new, 2) AS freq_rate, ROUND(v_old, 2) AS freq_rate_2011_2013 FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rank_bottom
WITH a AS (SELECT area_name, AVG(CASE WHEN year BETWEEN 2011 AND 2013 THEN TRY_CAST(value AS DOUBLE) END) AS v_old, AVG(CASE WHEN year BETWEEN 2021 AND 2023 THEN TRY_CAST(value AS DOUBLE) END) AS v_new FROM e_stat.ssds.f_pref_labor WHERE cat01 = 'F8101' AND area_name <> '全国' AND year BETWEEN 2011 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name, v_old, v_new, ROW_NUMBER() OVER (ORDER BY v_new DESC, area_name) AS rn FROM a) SELECT area_name, ROUND(v_new, 2) AS freq_rate, ROUND(v_old, 2) AS freq_rate_2011_2013 FROM ranked WHERE rn > 37 ORDER BY rn
```
