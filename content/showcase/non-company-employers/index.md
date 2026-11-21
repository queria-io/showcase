---
title: 37の町村では、会社より医療法人や社会福祉法人などで働く人のほうが多い
description: 令和3年経済センサスの従業者を経営組織別に集計しました。1,719市区町村のうち37町村では、従業者が最も多い経営組織が、医療法人や社会福祉法人などの会社以外の法人です。37町村のその従業者の60.0%は医療，福祉で働いています。
ogDescription: 令和3年経済センサスの従業者を経営組織別に集計しました。1,719市区町村のうち37町村では、従業者が最も多い経営組織が会社以外の法人です。
publishedAt: 2026-08-29
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 経済センサス
  - 雇用
  - 経営組織
datasets:
  - queria/e_stat
  - queria/nlftp
  - queria/soumu
sources:
  - title: 令和3年経済センサス‐活動調査
    url: https://www.stat.go.jp/data/e-census/2021/index.html
    publisher: 総務省・経済産業省
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: e_stat.economic_census.establishment_industry で島根県邑南町（area_level が municipality）の従業者数を、産業大分類×経営組織別に出して。会社以外の法人がどの産業に集まっているか確かめて
socialAnnounce: |-
  令和3年経済センサスの従業者を経営組織別に数えました。

  1,719市区町村のうち37町村では、最大の勤め先が会社ではなく医療法人や社会福祉法人などです。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

全国1,719市区町村のうち37の町村では、従業者が最も多い経営組織が会社ではなく、医療法人・社会福祉法人・学校法人などの会社以外の法人です。37町村の会社以外の法人の従業者のうち60.0%は医療，福祉で働いています。全国でも、会社以外の法人は事業所数の9.4%ですが、従業者数では16.0%を占めます。

市町村の雇用対策では、企業の誘致や創業支援が多く行われていて、その対象は会社です。この記事では、[令和3年経済センサス‐活動調査](https://www.stat.go.jp/data/e-census/2021/index.html)の民営事業所の従業者数を経営組織別に集計し、地域で多くの人を雇っているのがどの組織かを確認しました。経営組織は事業所を営んでいる主体の種類で、個人（個人事業主）、会社（株式会社や合同会社など）、会社以外の法人（医療法人・社会福祉法人・学校法人・協同組合・宗教法人など）の3つに分かれます。役場や公立学校のように国と地方公共団体が直接運営する事業所と、公務は含まれません。

## 会社以外の法人は、事業所の9.4%で従業者の16.0%

経営組織は `organization_code` で区分されていて、総数と内訳が同じ列に並びます。

| コード | 経営組織                           |
| ------ | ---------------------------------- |
| 0      | 総数（個人＋会社＋会社以外の法人） |
| 1      | 個人                               |
| 2      | 会社                               |
| 3      | 会社以外の法人                     |
| S1     | （別掲）外国の会社                 |
| S2     | （別掲）法人でない団体             |

S1 と S2 は総数の一部を別に集計した別掲なので、総数に加えると二重に集計することになります。以下の集計はすべて、個人・会社・会社以外の法人の3区分によるものです。

全国の民営事業所は4,870,898か所、そこで働く従業者は55,700,098人です。事業所数では会社が58.7%、個人が31.9%、会社以外の法人が9.4%です。従業者数では、会社以外の法人が16.0%を占めます。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "org_national"},
      "transform": [
        {"fold": ["est_pct", "emp_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"est_pct\": \"事業所の割合\", \"emp_pct\": \"従業者の割合\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"est_pct\",\"emp_pct\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "organization",
          "type": "nominal",
          "axis": {"title": "経営組織", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "全国に占める割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["事業所の割合", "従業者の割合"], "range": ["#93c5fd", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "xOffset": {"field": "__name", "sort": ["事業所の割合", "従業者の割合"]},
        "tooltip": [
          {"field": "organization", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    },
    {
      "data": {"name": "org_national"},
      "transform": [
        {"fold": ["est_pct", "emp_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"est_pct\": \"事業所の割合\", \"emp_pct\": \"従業者の割合\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"est_pct\",\"emp_pct\"], datum.__series)", "as": "__order"},
        {
          "calculate": "datum[{\"est_pct\":\"est_pct\",\"emp_pct\":\"emp_pct\"}[datum.__series]]",
          "as": "__text"
        },
        {"filter": "isValid(datum.__text)"}
      ],
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "organization",
          "type": "nominal",
          "axis": {"title": "経営組織", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "全国に占める割合（%）", "grid": true}
        },
        "xOffset": {"field": "__name", "sort": ["事業所の割合", "従業者の割合"]},
        "text": {"field": "__text"}
      }
    }
  ]
}
```

1事業所あたりの従業者数は、会社以外の法人が19.4人で最も多く、会社の14.9人、個人の2.8人を上回ります。会社以外の法人は、事業所の数は少ないものの、1か所あたりで多くの人を雇っています。この表は、売上（収入）金額等の数値が得られた民営事業所を集計の対象にしているため、事業所に関する集計の民営事業所数とは母数が違います。

## 医療，福祉では従業者の72.4%が会社以外の法人で働いている

産業大分類ごとに、従業者数を経営組織で分けます。産業は大分類16区分に農林漁業を加えた17区分で、重複なく全産業を含む組み合わせです。図は従業者数の多い産業から順に並べています。

```chart
{
  "height": 520,
  "layer": [
    {
      "data": {"name": "industry_mix"},
      "transform": [
        {"fold": ["corp_pct", "npo_pct", "solo_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"corp_pct\": \"会社\", \"npo_pct\": \"会社以外の法人\", \"solo_pct\": \"個人\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"corp_pct\",\"npo_pct\",\"solo_pct\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "industry_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の構成比（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["会社", "会社以外の法人", "個人"], "range": ["#94a3b8", "#7c3aed", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "industry_name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

会社以外の法人の比率が最も高いのは医療，福祉で72.4%、次いで教育，学習支援業が62.1%です。農林漁業の37.6%、複合サービス事業の34.5%が続きます。建設業は0.2%、製造業は0.6%、運輸業，郵便業は0.8%とほとんどが会社で、従業者数が最も多い卸売業，小売業でも2.6%です。医療，福祉と教育，学習支援業では、事業を営むのが医療法人・社会福祉法人・学校法人であることが多いためです。

農林漁業だけは個人の値が入りません。経済センサス‐活動調査が農林漁業の個人経営を調査の対象外としているためで、この図でも農林漁業は会社と会社以外の法人の2区分になっています。

## 都道府県では鹿児島県の25.0%から愛知県の11.5%まで、2.2倍の差がある

会社以外の法人が従業者に占める割合を、都道府県別に地図にしました。色が濃いほど割合が高い県です。

```map
type: map
layers:
  - from: pref_map
    geojson: geojson
    color: z_val
    label: pref_name
    name: "会社以外の法人（%）"
lng: 137
lat: 36.5
zoom: 4
```

最も高いのは鹿児島県の25.0%で、長崎県24.6%、高知県24.3%、島根県23.7%と続きます。最も低いのは愛知県の11.5%、次いで東京都12.1%、静岡県13.3%、大阪府13.9%です。最も高い県と最も低い県の差はおよそ2.2倍です。上位は九州・四国・山陰の県で、下位は大都市圏のある都府県です。

## 37町村では会社以外の法人が、12市区町村では個人が最も多くの人を雇っている

市区町村の単位で集計すると、従業者が最も多い経営組織が会社ではない地域があります。この表に市区町村として入っているのは1,719で、東京23区は「特別区部」として1つにまとめられています。そのうち、従業者数が最も多い経営組織が会社なのは1,670市区町村です。残るうち37町村では会社以外の法人が、12の市区町村では個人が最も多くなっています。

その37はすべて町または村です。会社以外の法人の割合が最も高いのは熊本県球磨村の63.5%で、青森県西目屋村61.1%、高知県大川村58.0%が続きます。この割合が50%を超え、働く人の過半数が会社以外の法人に勤めている町村は9つあります。最も高い球磨村の値は、令和2年7月豪雨で被災した翌年の時点のものです。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "reversal"},
      "transform": [
        {"fold": ["corp_pct", "npo_pct", "solo_pct"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"corp_pct\": \"会社\", \"npo_pct\": \"会社以外の法人\", \"solo_pct\": \"個人\"}[datum.__series]",
          "as": "__name"
        },
        {
          "calculate": "indexof([\"corp_pct\",\"npo_pct\",\"solo_pct\"], datum.__series)",
          "as": "__order"
        }
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "従業者数の構成比（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["会社", "会社以外の法人", "個人"], "range": ["#94a3b8", "#7c3aed", "#f97316"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

37町村のうち28町村は、従業者数が1,000人に満たない小さな地域です。1,000人以上の9町村は、福井県永平寺町の7,638人が最も多く、石川県内灘町6,545人、奈良県三郷町4,190人、島根県邑南町3,636人、和歌山県高野町2,043人と続きます。会社が最大の勤め先ではない町村には、従業者が数千人の町も含まれます。

これらの町村では個人経営の割合も高く、沖縄県伊平屋村が33.3%、長崎県小値賀町と沖縄県粟国村がともに32.8%、奈良県御杖村が32.2%、群馬県南牧村が32.0%と、個人が3割を超える町村があります。会社・会社以外の法人・個人の3つの割合が近く、どれか1つが大半を占めているわけではありません。

## 37町村の会社以外の法人では、従業者の60.0%が医療，福祉で働いている

この37町村の会社以外の法人の従業者を、産業別に分けます。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "reversal_mix"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "pct", "type": "quantitative"},
          {"field": "industry_name", "type": "nominal"}
        ],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社以外の法人の従業者に占める割合（%）", "grid": true}
        },
        "y": {
          "field": "industry_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "reversal_mix"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社以外の法人の従業者に占める割合（%）", "grid": true}
        },
        "y": {
          "field": "industry_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "text": {"field": "pct"}
      }
    }
  ]
}
```

医療，福祉が60.0%を占めます。教育，学習支援業が10.2%、農林漁業が8.9%、サービス業（他に分類されないもの）が8.1%、卸売業，小売業が4.5%と続きます。町村の規模では、病院や介護施設、保育所が地域で最も大きい職場の1つになると考えられます。

誘致や創業支援の対象は会社ですが、この37町村で最も多くの人を雇っているのは会社以外の法人です。これらの町村で雇用を増やしたり維持したりするには、医療法人や社会福祉法人と協議することになります。

## 業務での使い方

- 自分の市区町村について経営組織別の従業者数を集計し、働く人が会社に集中しているのか、会社以外の法人や個人にも分散しているのかを確認する
- 会社以外の法人の比率が高い場合は、産業別の内訳を集計して、対象となる法人の種類（医療、福祉、教育、農林漁業など）を絞る
- 近隣の町村と比較して雇用の構成が似ている地域を探し、人材確保の施策や広域連携の相手を選ぶ材料にする
- 個人経営の比率が高い地域では、事業承継の支援が雇用の維持に直接関係する。会社向けの施策の対象にならない従業者の数を示せる

## データの出典

本記事は総務省・経済産業省[令和3年経済センサス‐活動調査](https://www.stat.go.jp/data/e-census/2021/index.html)の産業横断的集計「売上（収入）金額等」を、2026年8月29日時点で集計しています。数値は2021年6月1日現在で、対象は民営事業所です。都道府県の地図は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)を使っています。

Queriaは、総務省・経済産業省や国土交通省のオープンデータを、列名・単位・地域や産業の階層を統一し、総数と内訳の関係を列の説明に書いて公開しています。本記事で使った[産業別・経営組織別の事業所テーブル](/datasets/queria/e_stat/economic_census/establishment_industry)から、担当する市区町村の経営組織別・産業別の従業者数を集計できます。

```sql id=org_national
SELECT organization, SUM(establishments) AS establishments, SUM(employees) AS employees, ROUND(100 * CAST(SUM(establishments) AS DOUBLE) / (SELECT SUM(establishments) FROM e_stat.economic_census.establishment_industry WHERE area_level = 'national' AND industry_code = 'AR' AND organization_code = '0'), 1) AS est_pct, ROUND(100 * CAST(SUM(employees) AS DOUBLE) / (SELECT SUM(employees) FROM e_stat.economic_census.establishment_industry WHERE area_level = 'national' AND industry_code = 'AR' AND organization_code = '0'), 1) AS emp_pct, ROUND(CAST(SUM(employees) AS DOUBLE) / SUM(establishments), 1) AS per_est FROM e_stat.economic_census.establishment_industry WHERE area_level = 'national' AND industry_code = 'AR' AND organization_code IN ('1', '2', '3') GROUP BY organization ORDER BY SUM(employees)
```

```sql id=industry_mix
SELECT industry_name, SUM(CASE WHEN organization_code = '0' THEN employees END) AS total, ROUND(100 * CAST(SUM(CASE WHEN organization_code = '1' THEN employees END) AS DOUBLE) / SUM(CASE WHEN organization_code = '0' THEN employees END), 1) AS solo_pct, ROUND(100 * CAST(SUM(CASE WHEN organization_code = '2' THEN employees END) AS DOUBLE) / SUM(CASE WHEN organization_code = '0' THEN employees END), 1) AS corp_pct, ROUND(100 * CAST(SUM(CASE WHEN organization_code = '3' THEN employees END) AS DOUBLE) / SUM(CASE WHEN organization_code = '0' THEN employees END), 1) AS npo_pct FROM e_stat.economic_census.establishment_industry WHERE area_level = 'national' AND (industry_level = 2 OR industry_code = 'AB') GROUP BY industry_name ORDER BY total DESC, industry_name
```

```sql id=pref_map
SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, e.npo_pct AS z_val, b.prefecture_name AS pref_name FROM (SELECT area_name, ROUND(100 * CAST(SUM(CASE WHEN organization_code = '3' THEN employees END) AS DOUBLE) / SUM(CASE WHEN organization_code = '0' THEN employees END), 1) AS npo_pct FROM e_stat.economic_census.establishment_industry WHERE area_level = 'prefecture' AND industry_code = 'AR' GROUP BY area_name) e JOIN nlftp.boundary.prefecture b ON b.prefecture_name = e.area_name ORDER BY b.prefecture_name
```

```sql id=reversal
WITH m AS (SELECT area, area_name, CAST(SUM(CASE WHEN organization_code = '0' THEN employees END) AS DOUBLE) AS tot, COALESCE(CAST(SUM(CASE WHEN organization_code = '1' THEN employees END) AS DOUBLE), 0) AS solo, COALESCE(CAST(SUM(CASE WHEN organization_code = '2' THEN employees END) AS DOUBLE), 0) AS corp, COALESCE(CAST(SUM(CASE WHEN organization_code = '3' THEN employees END) AS DOUBLE), 0) AS npo FROM e_stat.economic_census.establishment_industry WHERE area_level = 'municipality' AND industry_code = 'AR' GROUP BY 1, 2), s AS (SELECT COUNT(*) AS n_all, COUNT(*) FILTER (WHERE corp >= npo AND corp >= solo) AS n_corp_top, COUNT(*) FILTER (WHERE NOT (corp >= npo AND corp >= solo) AND solo > npo) AS n_solo_top FROM m) SELECT c.pref_name || ' ' || m.area_name AS name, m.tot AS total, ROUND(100 * m.corp / m.tot, 1) AS corp_pct, ROUND(100 * m.npo / m.tot, 1) AS npo_pct, ROUND(100 * m.solo / m.tot, 1) AS solo_pct, s.n_all, s.n_corp_top, s.n_solo_top FROM m JOIN soumu.code.municipality c ON c.area_code = m.area CROSS JOIN s WHERE m.npo > m.corp AND m.npo >= m.solo ORDER BY npo_pct DESC, name
```

```sql id=reversal_mix
WITH m AS (SELECT area, COALESCE(CAST(SUM(CASE WHEN organization_code = '1' THEN employees END) AS DOUBLE), 0) AS solo, COALESCE(CAST(SUM(CASE WHEN organization_code = '2' THEN employees END) AS DOUBLE), 0) AS corp, COALESCE(CAST(SUM(CASE WHEN organization_code = '3' THEN employees END) AS DOUBLE), 0) AS npo FROM e_stat.economic_census.establishment_industry WHERE area_level = 'municipality' AND industry_code = 'AR' GROUP BY 1), rev AS (SELECT area FROM m WHERE npo > corp AND npo >= solo), mix AS (SELECT industry_name, CAST(SUM(employees) AS DOUBLE) AS emp FROM e_stat.economic_census.establishment_industry WHERE area_level = 'municipality' AND organization_code = '3' AND (industry_level = 2 OR industry_code = 'AB') AND area IN (SELECT area FROM rev) GROUP BY 1) SELECT industry_name, emp, ROUND(100 * emp / (SELECT SUM(emp) FROM mix), 1) AS pct FROM mix WHERE emp IS NOT NULL ORDER BY emp DESC, industry_name
```
