---
title: 災害ボランティアをした住民の割合は、東日本大震災の岩手・宮城で11.1%、熊本地震の熊本で8.4%
description: 社会生活基本調査の5回分（2001〜2021年）で、災害に関係したボランティア活動をした人の割合を都道府県別に並べました。2011年の岩手県・宮城県は11.1%、2016年の熊本県は8.4%で、ほかの3回は最も高い県でも4.0%です。ボランティア活動全体では、島根県など6県が5回とも上位10に入っています。
publishedAt: 2026-06-11
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - ボランティア
  - 災害
  - 社会生活基本調査
  - 地域
datasets:
  - queria/e_stat
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/1.html
    publisher: 総務省統計局
  - title: 令和3年社会生活基本調査 調査の概要
    url: https://www.stat.go.jp/data/shakai/2021/gaiyou.html
    publisher: 総務省統計局
  - title: 令和3年社会生活基本調査 生活行動に関する結果 結果の概要
    url: https://www.stat.go.jp/data/shakai/2021/pdf/gaiyoua.pdf
    publisher: 総務省統計局
  - title: 平成23年社会生活基本調査 生活行動に関する結果（報道資料）
    url: https://www.stat.go.jp/data/shakai/2011/pdf/houdou.pdf
    publisher: 総務省統計局
  - title: 平成23年（2011年）東北地方太平洋沖地震
    url: https://www.data.jma.go.jp/eqev/data/2011_03_11_tohoku/index.html
    publisher: 気象庁
  - title: 平成28年（2016年）熊本地震
    url: https://www.data.jma.go.jp/eqev/data/2016_04_14_kumamoto/index.html
    publisher: 気象庁
agentHint: 高齢者を対象とした活動（G6419）の行動者率を2001〜2021年の5回分、都道府県別に出して。5回とも上位10に入る県が、ボランティア活動の総数（G6417）と同じ顔ぶれになるかを比べて
socialAnnounce: |-
  災害に関係したボランティアをした人の割合は、2011年の岩手県・宮城県で11.1%、2016年の熊本県で8.4%。ほかの3回は、最も高い県でも4.0%でした。

  災害ボランティアセンターの備えに。
---

総務省の[社会生活基本調査](https://www.stat.go.jp/data/shakai/2021/gaiyou.html)を5回分（2001〜2021年）並べると、災害に関係したボランティア活動をした人の割合は、東日本大震災の年の岩手県・宮城県で11.1%、熊本地震の年の熊本県で8.4%でした。ほかの3回（2001・2006・2021年）は、最も高い県でも2.5〜4.0%です。ボランティア活動全体では、島根県など6県が5回とも上位10に、京都府など6道府県が5回とも下位10に入っています。

社会福祉協議会のボランティアセンターや自治体の防災担当者は、大きな災害のあとに県内の住民のどれだけが炊き出しや物資の送付などの活動をするかを、災害ボランティアセンターの体制を計画するときの参考にできます。

## 社会生活基本調査の「行動者率」を使う

社会生活基本調査は5年ごとに10月20日現在で行われ、その前の1年間（2021年調査なら2020年10月20日〜2021年10月19日）に自由時間でどんな活動をしたかを尋ねています（[令和3年調査 結果の概要](https://www.stat.go.jp/data/shakai/2021/pdf/gaiyoua.pdf)）。過去1年間に1回でもその活動をした10歳以上の人の割合を「行動者率」と呼びます。都道府県別の値は、e-Stat[「社会・人口統計体系」](https://www.stat.go.jp/data/ssds/1.html)の都道府県別文化・スポーツ統計（`g_pref_culture`）に2001年から2021年までの5回分が入っています。

| コード              | 内容                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| G6417               | ボランティア活動の行動者率（総数）                                                                     |
| G6418〜G6425、G6427 | 分野別（健康・医療、高齢者、障害者、子供、スポーツ・文化、まちづくり、安全な生活、自然・環境、その他） |
| G6426               | 災害に関係した活動の行動者率                                                                           |
| G6428               | 国際協力に関係した活動の行動者率（2006年から）                                                         |

この記事では、災害に関係した活動（`G6426`）を「災害ボランティア」と呼びます。調査の定義では、被災地での炊き出しのほか、災害を受けた人に食べものや着るものを送ることも含みます。都道府県の値は標本調査からの推計なので、値の近い都道府県どうしの順位には誤差が含まれます。

## 岩手・宮城・熊本は8〜11%、ほかの回の最高は4%以下

調査の回ごとに、災害ボランティアの行動者率が最も高かった県（青）と、最も高い値の県を除いた都道府県の中央値（灰）を並べます。

```chart
{
  "height": 260,
  "data": {"name": "peak"},
  "encoding": {"y": {"field": "survey", "type": "ordinal", "title": null}},
  "layer": [
    {"mark": {"type": "rule", "color": "#cbd5e1", "strokeWidth": 3}, "encoding": {"x": {"field": "median_others", "type": "quantitative", "title": "災害に関係した活動の行動者率（%）"}, "x2": {"field": "top_rate"}}},
    {"mark": {"type": "point", "filled": true, "size": 90, "color": "#94a3b8"}, "encoding": {"x": {"field": "median_others", "type": "quantitative"}, "tooltip": [{"field": "survey", "title": "調査"}, {"field": "median_others", "title": "最も高い県を除いた中央値（%）"}]}},
    {"mark": {"type": "point", "filled": true, "size": 90, "color": "#3b82f6"}, "encoding": {"x": {"field": "top_rate", "type": "quantitative"}, "tooltip": [{"field": "survey", "title": "調査"}, {"field": "top_pref", "title": "最も高い県"}, {"field": "top_rate", "title": "行動者率（%）"}, {"field": "top_to_median", "title": "中央値の何倍か"}]}},
    {"mark": {"type": "text", "align": "left", "dx": 8, "fontSize": 11, "color": "#3b82f6"}, "encoding": {"x": {"field": "top_rate", "type": "quantitative"}, "text": {"field": "top_label"}}}
  ]
}
```

```sql
SELECT * FROM peak
```

2011年は宮城県と岩手県がともに11.1%で、その年の[東北地方太平洋沖地震](https://www.data.jma.go.jp/eqev/data/2011_03_11_tohoku/index.html)（2011年3月）は調査の対象期間（2010年10月20日〜2011年10月19日）に入っています。2016年は熊本県が8.4%で、2番目の福岡県（2.6%）の3倍を超えました。同じ年の4月に[熊本地震](https://www.data.jma.go.jp/eqev/data/2016_04_14_kumamoto/index.html)が起きています。この2回を除く3回（2001・2006・2021年）では、最も高い県でも4.0%（2001年の高知県）でした。2001年の高知県（4.0%）は中央値の3.08倍、2006年の長野県（3.1%）は2.95倍で、1つの県が中央値を大きく上回ることは2011年と2016年以外にもあります。2011年と2016年がほかの回と違うのは、値が8%を超えていることです。2011年調査は、岩手県・宮城県・福島県の一部地域を除いて行われました（[平成23年調査の報道資料](https://www.stat.go.jp/data/shakai/2011/pdf/houdou.pdf)の「調査の範囲」）。この3県の値は、除かれた地域の住民を含みません。

47都道府県すべての値を、調査の回ごとに色の濃さで示します。色が濃いのは2011年の列と2016年の熊本県です。2011年は岩手県・宮城県に続いて山形県（6.9%）と福島県（6.5%）が高く、ほかの都道府県もほかの回より高くなっています。

```chart
{
  "height": 900,
  "data": {"name": "by_pref"},
  "mark": "rect",
  "encoding": {
    "x": {"field": "survey", "type": "ordinal", "title": null, "axis": {"orient": "top"}},
    "y": {"field": "area_name", "type": "nominal", "title": null, "sort": {"field": "area"}},
    "color": {"field": "rate", "type": "quantitative", "scale": {"scheme": "blues"}, "title": "行動者率（%）"},
    "tooltip": [{"field": "area_name", "title": "都道府県"}, {"field": "survey", "title": "調査"}, {"field": "rate", "title": "行動者率（%）"}]
  }
}
```

## 岩手・宮城・熊本は5年後の調査で2%台まで下がる

被災した県の値を5回分たどります。

```chart
{
  "data": {"name": "affected"},
  "mark": {"type": "line", "point": true},
  "encoding": {
    "x": {"field": "year", "type": "ordinal", "title": "調査年"},
    "y": {"field": "rate", "type": "quantitative", "title": "災害に関係した活動の行動者率（%）"},
    "color": {"field": "area_name", "type": "nominal", "title": null, "scale": {"domain": ["岩手県", "宮城県", "福島県", "熊本県", "全国"], "range": ["#3b82f6", "#22c55e", "#f97316", "#ef4444", "#64748b"]}},
    "tooltip": [{"field": "area_name", "title": "都道府県"}, {"field": "year", "title": "調査年"}, {"field": "rate", "title": "行動者率（%）"}]
  }
}
```

岩手県（11.1%）と宮城県（11.1%）は、5年後の2016年にそれぞれ2.4%と2.0%に下がりました。熊本県も2016年の8.4%から2021年は2.5%です。どれも全国（2016年1.5%、2021年0.8%）よりは高いものの、地震のあった年の3分の1以下です。熊本県の2021年の2.5%はこの回の47都道府県で最も高く、最も高い県を除いた中央値の3.33倍でした。福島県は2011年の6.5%から2016年は1.3%でした。

## 全国に広がったのは2011年だけ

2011年は、被災した県の外でも値が上がりました。全国の行動者率は2006年の1.2%から2011年に3.8%へ上がり、2016年には1.5%に戻っています。

```sql
SELECT * FROM rise
```

2006年から2011年にかけて47都道府県のうち46で上がり（上がらなかったのは宮崎県）、2011年から2016年にかけて46で下がりました（下がらなかったのは熊本県）。都道府県の中央値は1.1%（2006年）、3.2%（2011年）、1.3%（2016年）です。熊本地震のあった2016年は、熊本県を除いた46都道府県の中央値が1.25%で、2006年の中央値（1.1%）に近い水準です。2011年の全国的な上昇には、被災地へ食べものや着るものを送る活動が含まれていると考えられます。

## ボランティア全体では、6県が5回とも上位10、6道府県が5回とも下位10

災害ボランティアの順位は回ごとに入れ替わり、ボランティア活動の総数（`G6417`）の順位はほとんど変わりません。隣り合う調査どうしで、47都道府県の順位の相関係数を比較します（1に近いほど順位が同じ）。

```chart
{
  "data": {"name": "rank_corr"},
  "mark": "bar",
  "encoding": {
    "x": {"field": "surveys", "type": "ordinal", "title": null},
    "xOffset": {"field": "activity"},
    "y": {"field": "rank_corr", "type": "quantitative", "title": "順位の相関係数", "scale": {"domain": [0, 1]}},
    "color": {"field": "activity", "type": "nominal", "title": null, "scale": {"domain": ["ボランティア活動（総数）", "災害に関係した活動"], "range": ["#22c55e", "#3b82f6"]}},
    "tooltip": [{"field": "activity", "title": "活動"}, {"field": "surveys", "title": "調査"}, {"field": "rank_corr", "title": "順位の相関係数"}]
  }
}
```

総数の順位の相関は0.87〜0.91で、災害ボランティアは0.05〜0.57でした。総数でも、中ほどの都道府県は値が近く標本の誤差もあるので、回ごとに順位が大きく動くことがあります。5回の調査すべてで上位10に入った都道府県と、すべてで下位10に入った都道府県は次のとおりです（同じ値の都道府県は同じ順位として集計しています）。

```sql
SELECT * FROM stable
```

島根県・佐賀県・滋賀県・鳥取県・鹿児島県・長野県は5回とも上位10に、京都府・愛知県・北海道・埼玉県・大阪府・青森県は5回とも下位10に入りました。

全国の総数の行動者率は2006〜2016年の26%台から2021年に17.8%へ下がっています（下の表）。2021年調査の対象期間は2回の緊急事態宣言を含み、総務省は自由時間の生活行動が感染症の影響で変わったと説明しています（[結果の概要](https://www.stat.go.jp/data/shakai/2021/pdf/gaiyoua.pdf)）。2021年の値は、平常時の水準として読まないでください。

```sql
SELECT * FROM national
```

## 業務での使い方

- 災害ボランティアセンターの体制計画: 2011年の岩手県・宮城県と2016年の熊本県では、県内の10歳以上の住民の8〜11%が、その1年に炊き出しや物資の送付などの災害に関係した活動をしました。全国の値は2011年を除くと0.8〜1.5%です。センターに申し出る人の数ではなく、物資を送っただけの人や被災した住民自身も含む割合なので、被災した年に県内の住民のうち何らかの支援をする人の割合の上限の目安として使えます

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/1.html) の都道府県別文化・スポーツ統計を2026年11月12日時点で集計しています。元データは総務省の社会生活基本調査（2001・2006・2011・2016・2021年）で、調査の期日と対象期間は[令和3年調査の概要](https://www.stat.go.jp/data/shakai/2021/gaiyou.html)と[平成23年調査の報道資料](https://www.stat.go.jp/data/shakai/2011/pdf/houdou.pdf)によります。

Queria は社会生活基本調査を含む官公庁のデータを、列名・単位を統一し、カテゴリコードの説明を付けて公開しています。本記事で使った[文化・スポーツ統計テーブル](/datasets/queria/e_stat/ssds/g_pref_culture)には2001年から2021年までの5回分が入っているので、自分の都道府県の行動者率を分野ごと・調査の回ごとに確認できます。

```sql id=peak
WITH d AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6426' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021), r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY v DESC, area_name) AS rn, MAX(v) OVER (PARTITION BY year) AS top_v FROM d) SELECT CAST(year AS VARCHAR) || '年' AS survey, MAX(CASE WHEN rn = 1 THEN area_name END) AS top_pref, MAX(CASE WHEN rn = 1 THEN v END) AS top_rate, MAX(CASE WHEN rn = 2 THEN area_name END) AS second_pref, MAX(CASE WHEN rn = 2 THEN v END) AS second_rate, MAX(CASE WHEN rn = 1 THEN area_name END) || CASE WHEN MAX(CASE WHEN rn = 2 THEN v END) = MAX(CASE WHEN rn = 1 THEN v END) THEN '・' || MAX(CASE WHEN rn = 2 THEN area_name END) ELSE '' END AS top_label, MEDIAN(v) FILTER (WHERE v < top_v) AS median_others, ROUND(MAX(CASE WHEN rn = 1 THEN v END) / MEDIAN(v) FILTER (WHERE v < top_v), 2) AS top_to_median, COUNT(*) AS prefs FROM r GROUP BY year ORDER BY year
```

```sql id=by_pref
SELECT area, area_name, CAST(year AS VARCHAR) || '年' AS survey, TRY_CAST(value AS DOUBLE) AS rate FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6426' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021 ORDER BY area, year
```

```sql id=affected
SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS rate FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6426' AND area_name IN ('岩手県', '宮城県', '福島県', '熊本県', '全国') AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021 ORDER BY area_name, year
```

```sql id=rise
WITH d AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6426' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year IN (2006, 2011, 2016)), w AS (SELECT area_name, MAX(v) FILTER (WHERE year = 2006) AS v06, MAX(v) FILTER (WHERE year = 2011) AS v11, MAX(v) FILTER (WHERE year = 2016) AS v16 FROM d GROUP BY area_name) SELECT COUNT(*) AS prefs, COUNT(*) FILTER (WHERE v11 > v06) AS up_2006_to_2011, STRING_AGG(area_name, '、') FILTER (WHERE v11 <= v06) AS not_up_2006_to_2011, COUNT(*) FILTER (WHERE v16 < v11) AS down_2011_to_2016, STRING_AGG(area_name, '、') FILTER (WHERE v16 >= v11) AS not_down_2011_to_2016, MEDIAN(v06) AS median_2006, MEDIAN(v11) AS median_2011, MEDIAN(v16) AS median_2016, MIN(v11) AS min_2011, MAX(v06) AS max_2006 FROM w
```

```sql id=rank_corr
WITH d AS (SELECT cat01, area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G6417', 'G6426') AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021), r AS (SELECT cat01, area_name, year, RANK() OVER (PARTITION BY cat01, year ORDER BY v DESC) + (COUNT(*) OVER (PARTITION BY cat01, year, v) - 1) / 2.0 AS rk FROM d) SELECT CASE a.cat01 WHEN 'G6417' THEN 'ボランティア活動（総数）' ELSE '災害に関係した活動' END AS activity, CAST(a.year AS VARCHAR) || '→' || CAST(b.year AS VARCHAR) || '年' AS surveys, ROUND(CORR(a.rk, b.rk), 2) AS rank_corr, COUNT(*) AS prefs FROM r a JOIN r b ON a.cat01 = b.cat01 AND a.area_name = b.area_name AND b.year = a.year + 5 GROUP BY a.cat01, a.year, b.year ORDER BY a.cat01, a.year
```

```sql id=stable
WITH d AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.g_pref_culture WHERE cat01 = 'G6417' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021), r AS (SELECT area_name, year, v, RANK() OVER (PARTITION BY year ORDER BY v DESC) AS rk_high, RANK() OVER (PARTITION BY year ORDER BY v ASC) AS rk_low FROM d), c AS (SELECT area_name, COUNT(*) FILTER (WHERE rk_high <= 10) AS top10_surveys, COUNT(*) FILTER (WHERE rk_low <= 10) AS bottom10_surveys, MAX(v) FILTER (WHERE year = 2001) AS rate_2001, MAX(v) FILTER (WHERE year = 2021) AS rate_2021 FROM r GROUP BY area_name) SELECT CASE WHEN top10_surveys = 5 THEN '5回とも上位10' ELSE '5回とも下位10' END AS grp, area_name, rate_2001, rate_2021 FROM c WHERE top10_surveys = 5 OR bottom10_surveys = 5 ORDER BY grp, rate_2021 DESC, area_name
```

```sql id=national
SELECT CAST(year AS VARCHAR) || '年' AS survey, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G6417') AS total_rate, MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'G6426') AS disaster_rate FROM e_stat.ssds.g_pref_culture WHERE cat01 IN ('G6417', 'G6426') AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year <= 2021 GROUP BY year ORDER BY year
```
