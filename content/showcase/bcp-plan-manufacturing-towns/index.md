---
title: 事業継続力強化計画の認定は、第2次産業の割合が高い市区町村ほど多く、徳島県は沖縄県の11倍
description: 国の認定を受けた事業継続力強化計画を法人番号と突き合わせ、会社1万社あたりの認定数を県・市区町村別に集計しました。1位の徳島県は47位の沖縄県の11倍で、第2次産業の割合が30%以上の市区町村は15%未満の3.3倍です。過去の災害被害額とは対応しませんでした。
ogDescription: 国の認定を受けた事業継続力強化計画を法人番号と突き合わせ、会社1万社あたりの認定数を県・市区町村別に集計しました。徳島県は沖縄県の11倍です。
publishedAt: 2026-08-23
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 事業継続力強化計画
  - 中小企業
  - 防災
  - gBizINFO
datasets:
  - queria/gbizinfo
  - queria/houjin_bangou
  - queria/e_stat
  - queria/soumu
sources:
  - title: 事業継続力強化計画
    url: https://www.chusho.meti.go.jp/keiei/antei/bousai/keizokuryoku.html
    publisher: 中小企業庁
  - title: gBizINFO
    url: https://info.gbiz.go.jp/
    publisher: 経済産業省
  - title: 国税庁法人番号公表サイト
    url: https://www.houjin-bangou.nta.go.jp/
    publisher: 国税庁
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/statistics/00200502
    publisher: 総務省統計局
agentHint: gbizinfo.main.mart_gbizinfo_certification の title が '事業継続力強化計画認定' の法人を houjin_bangou.main.mart_houjin_bangou と法人番号で突き合わせて、自分の県の市区町村別に会社1万社あたりの認定数を出して。認定数と会社数の実数も一緒に見せて
socialAnnounce: |-
  災害に備える計画をつくった会社を、法人番号と突き合わせて県別に数えました。

  会社1万社あたりで徳島県は沖縄県の11倍。過去の被害額とは対応せず、ものづくりの街ほど多い結果でした。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

事業継続力強化計画の認定を受けた会社は、全国で会社1万社あたり72.6社です。都道府県別では1位の徳島県が404.8社で、47位の沖縄県（35.3社）の約11倍でした。この差は過去の災害被害額とは対応せず、第2次産業で働く人の割合と対応しています。第2次産業の割合が30%以上の市区町村では1万社あたり127.6社で、15%未満の市区町村（38.2社）の3.3倍です。

[事業継続力強化計画](https://www.chusho.meti.go.jp/keiei/antei/bousai/keizokuryoku.html)は、中小企業庁が所管する認定制度です。中小企業が自然災害のリスクを見積もり、設備・人員・連絡体制をどう守るかを計画にまとめて申請すると、経済産業大臣の認定を受けられます。認定を受けた会社は[gBizINFO](https://info.gbiz.go.jp/)に法人番号つきで公開されます。この記事では、その記録を[国税庁の法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)のデータと突き合わせ、会社1万社あたりの認定数を都道府県別・市区町村別に集計しました。この数字は、国の認定を受けた会社の数です。認定を取らずに自社で事業継続計画をつくっている会社は含みません。

想定している読者は、取引先に防災投資や事業継続の相談を持ちかける、地方銀行や信用金庫の法人営業担当者です。自分の営業エリアの認定密度を全国と比較すると、まだ認定を受けていない取引先がどれくらい残っているかを把握できます。

## 認定・届出情報のうち、事業継続力強化計画は2番目に多い33,598件

gBizINFOの認定・届出情報テーブル（`mart_gbizinfo_certification`）は、各省庁の認定・登録・届出を法人番号つきで1件1行に収めています。制度名は`title`列に入っていて、件数の多いものは次のとおりです。

| 制度名                         | 件数   |
| ------------------------------ | ------ |
| 競争参加資格                   | 70,852 |
| 事業継続力強化計画認定         | 33,598 |
| 認定経営革新等支援機関         | 5,896  |
| 経営力向上計画認定             | 3,735  |
| ＤＸ認定制度                   | 3,055  |
| 適格機関投資家等特例業務届出者 | 2,128  |
| 金融商品取引業者登録           | 1,953  |
| ユースエール認定               | 1,926  |

この記事で使うのは事業継続力強化計画認定の33,598件です。法人番号でまとめると32,629社になり、そのうち法人番号公表サイトに会社（株式会社・有限会社・合名会社・合資会社・合同会社）として載っているのは32,244社でした。同じ範囲で集計した会社の総数は4,440,382社なので、全国では会社1万社あたり72.6社が認定を受けています。

収録されているのは2023年2月から2026年6月までに認定された分で、制度が始まってからの累計ではありません。以下の数字は、いま有効な認定の密度を表します。

## 1位の徳島県は、47位の沖縄県の11倍

都道府県別に、会社1万社あたりの認定数を並べました。分子はその県に本店を置く会社のうち認定を受けている会社の数、分母は同じ県の会社の総数です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10県",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "中間", "下位10県"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "中間", "下位10県"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "prefecture_name", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        },
        "y": {
          "field": "prefecture_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10県",
          "type": "nominal",
          "scale": {"domain": ["上位10県", "中間", "下位10県"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

1位は徳島県の404.8社で、2位の高知県（178.9社）の2倍以上です。以下、富山県176.8社、福井県156.8社、香川県154.4社、静岡県153.7社と続きます。最も少ないのは沖縄県の35.3社で、その上が東京都の36.9社、神奈川県48.0社、島根県52.0社、鹿児島県53.6社です。1位と47位の差は約11倍で、全国の中央値は89.9社でした。

下位には東京都・神奈川県・大阪府・京都府・福岡県・北海道と、大都市のある都道府県が並びます。分母は法人番号公表サイトに登記が残っている会社なので、実際には事業を行っていない会社も含みます。持株会社や事業実体の少ない法人が多い都市部では、そのぶん密度が低く出ます。

## 過去の災害被害額が大きい県ほど認定が多い、という関係はない

上位には徳島県・高知県・静岡県・三重県・香川県が並びます。実際に大きな被害を受けてきた県で認定が多いかどうかを確認します。

e-Statの[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)には、都道府県別の災害被害額（`K5112`）が1985年度から2023年度までの39年分、百万円単位で収録されています。この合計を2020年の総人口（`A1101`）で割った「住民1人あたりの累積被害額」を横軸に、認定密度を縦軸に取りました。被害額は物価を調整せずに各年度の金額を合計したもので、分母の人口も2020年の1時点なので、県の間の桁の違いを比較するための目安です。被害額は県によって3桁近く開くので、横軸は対数目盛にしています。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "damage"},
      "mark": {"type": "point", "color": "#f97316", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "dmg_per_capita", "type": "quantitative"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "dmg_per_capita",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1985〜2023年度の累積災害被害額（1人あたり・円、対数目盛）", "grid": true}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "damage"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "dmg_per_capita",
          "type": "quantitative",
          "scale": {"type": "log"},
          "axis": {"title": "1985〜2023年度の累積災害被害額（1人あたり・円、対数目盛）", "grid": true}
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ]
}
```

点は横に広がり、右上がりにはなりません。累積被害額が最も大きい宮城県は認定密度で30位（81.8社）、2位の兵庫県は34位（69.0社）、4位の熊本県は37位（62.5社）、6位の福島県は35位（67.8社）で、いずれも全国の中位から下位です。被害額の上位10県のうち、認定密度でも上位10に入るのは高知県（2位・178.9社）だけでした。

徳島県は、累積被害額では21位です。過去の被害額の大きさでは、認定を受けた会社の多さはほとんど説明できません。

## 第2次産業の割合が30%以上の市区町村は、15%未満の3.3倍

市区町村ごとに、認定密度を産業の構成と並べました。

2020年の国勢調査から、その市区町村に住む就業者数（`F1102`）と、そのうち第2次産業で働く人の数（`F2211`）を取り、第2次産業の割合を出しました。第2次産業には製造業のほか建設業や鉱業が含まれます。この割合で、両方のデータがある1,740市区町村を5つのグループに分け、グループごとに認定数の合計を会社数の合計で割りました。政令指定都市の行政区は市の単位にまとめています。

```chart
{
  "height": 260,
  "layer": [
    {
      "data": {"name": "industry_band"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "band", "type": "nominal"}
        ],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "第2次産業で働く人の割合（2020年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "industry_band"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "第2次産業で働く人の割合（2020年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        },
        "text": {"field": "rate"}
      }
    }
  ]
}
```

第2次産業の割合が高いグループほど、認定密度も高くなります。15%未満のグループは1万社あたり38.2社、15〜20%が58.0社、20〜25%が85.0社、25〜30%が112.1社、30%以上が127.6社です。最も高いグループは最も低いグループの3.3倍です。

個別の市区町村でも確認しました。会社が1,000社以上ある市区町村に絞り、認定密度の高い順に15件を並べています。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "city_top"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "会社1万社あたりの認定数（社）", "grid": true}
        },
        "y": {
          "field": "label",
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

1位は徳島県阿南市の496.5社で、全国平均72.6社の約7倍です。以下、徳島県吉野川市470.2社、静岡県牧之原市454.5社、千葉県富津市372.0社、香川県観音寺市371.9社と続きます。15件のうち4件が徳島県の市で、残りには群馬県大泉町、埼玉県深谷市、新潟県燕市、石川県能美市など、特定の産業の工場が集まる地方都市が多く入っています。

大企業が自社の供給網を守るために、部品や加工を請け負う取引先に事業継続の備えを求める動きがあります。こうした要請を受けやすい会社ほど計画の認定を受けているとすれば、被害の実績より産業構成のほうが認定密度と対応する理由になります。また、認定の申請は商工会議所や自治体の支援を受けて進むことが多く、徳島県の複数の市が上位に入っていることから、県内で地域ぐるみの推進があったと考えられます。

## 業務での使い方

- 自分の営業エリアの市区町村を同じ式で集計し、全国の中央値（1万社あたり89.9社）と比較する。中央値を下回っていれば、認定を受けていない取引先がそれだけ多く残っている
- 取引先の法人番号でgBizINFOの認定情報を検索し、認定の有無と認定日を確認する。認定日から時間が経っている取引先には、計画の見直しを提案できる
- 第2次産業の割合が高いのに認定密度が低い市区町村を探す。供給網からの要請が来やすいのに認定が進んでいない地域では、防災・減災の設備投資の相談が生まれやすいと考えられる

## データの出典

本記事は経済産業省の[gBizINFO](https://info.gbiz.go.jp/)の認定・届出情報、[国税庁法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)の基本3情報、e-Statの[社会・人口統計体系](https://www.e-stat.go.jp/statistics/00200502)を2026年8月23日時点で取得して集計しています。認定は2023年2月から2026年6月まで、災害被害額は1985年度から2023年度まで、第2次産業就業者数は2020年の国勢調査の値です。

Queriaは、省庁ごとに別々に公表されるこれらのオープンデータを、列名・単位・文字コードを統一し、法人番号や地域コードで結合できる形で公開しています。本記事で使った[認定・届出情報テーブル](/datasets/queria/gbizinfo/main/mart_gbizinfo_certification)で担当エリアの認定先を名前で確認したり、[法人番号テーブル](/datasets/queria/houjin_bangou/main/mart_houjin_bangou)と結合して市区町村ごとの会社数を集計したりできます。

```sql id=cert_kinds
SELECT title, COUNT(*) AS records FROM gbizinfo.main.mart_gbizinfo_certification GROUP BY title ORDER BY records DESC, title LIMIT 8
```

```sql id=cert_period
SELECT MIN(certification_date) AS first_date, MAX(certification_date) AS last_date, COUNT(*) AS records FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'
```

```sql id=national
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定') SELECT (SELECT COUNT(*) FROM cert) AS cert_companies, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified, ROUND(CAST(COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS DOUBLE) * 10000 / COUNT(*), 1) AS rate FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND prefecture_name IS NOT NULL
```

```sql id=pref_top
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'), agg AS (SELECT prefecture_name, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND prefecture_name IS NOT NULL GROUP BY prefecture_name), ranked AS (SELECT prefecture_name, ROUND(CAST(certified AS DOUBLE) * 10000 / corps, 1) AS rate, ROW_NUMBER() OVER (ORDER BY CAST(certified AS DOUBLE) * 10000 / corps DESC, prefecture_name) AS rn FROM agg) SELECT prefecture_name, rate FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'), agg AS (SELECT prefecture_name, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND prefecture_name IS NOT NULL GROUP BY prefecture_name), ranked AS (SELECT prefecture_name, ROUND(CAST(certified AS DOUBLE) * 10000 / corps, 1) AS rate, ROW_NUMBER() OVER (ORDER BY CAST(certified AS DOUBLE) * 10000 / corps DESC, prefecture_name) AS rn FROM agg) SELECT prefecture_name, rate FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'), agg AS (SELECT prefecture_name, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND prefecture_name IS NOT NULL GROUP BY prefecture_name), ranked AS (SELECT prefecture_name, ROUND(CAST(certified AS DOUBLE) * 10000 / corps, 1) AS rate, ROW_NUMBER() OVER (ORDER BY CAST(certified AS DOUBLE) * 10000 / corps DESC, prefecture_name) AS rn FROM agg) SELECT prefecture_name, rate FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=damage_coverage
SELECT MIN(year) AS first_year, MAX(year) AS last_year, COUNT(DISTINCT year) AS years, MIN(unit) AS unit FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K5112' AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL
```

```sql id=damage
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'), agg AS (SELECT prefecture_name, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND prefecture_name IS NOT NULL GROUP BY prefecture_name), dmg AS (SELECT area_name, SUM(TRY_CAST(value AS DOUBLE)) AS dmg_myen FROM e_stat.ssds.k_pref_safety WHERE cat01 = 'K5112' AND area_name <> '全国' AND year BETWEEN 1985 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), pop AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS people FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A1101' AND year = 2020 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL) SELECT a.prefecture_name, ROUND(d.dmg_myen * 1000000 / p.people) AS dmg_per_capita, ROUND(CAST(a.certified AS DOUBLE) * 10000 / a.corps, 1) AS rate, CASE WHEN a.prefecture_name IN ('徳島県', '高知県', '静岡県', '宮城県', '兵庫県', '岩手県', '熊本県', '東京都', '沖縄県') THEN a.prefecture_name ELSE '' END AS label FROM agg a JOIN dmg d ON d.area_name = a.prefecture_name JOIN pop p ON p.area_name = a.prefecture_name ORDER BY a.prefecture_name
```

```sql id=industry_band
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'), raw AS (SELECT substr(lg_code, 1, 5) AS ac, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND lg_code IS NOT NULL GROUP BY ac), folded AS (SELECT c.municipality_code AS area, SUM(raw.corps) AS corps, SUM(raw.certified) AS certified FROM raw JOIN soumu.code.municipality c ON c.area_code = raw.ac WHERE c.municipality_code IS NOT NULL GROUP BY c.municipality_code), sec AS (SELECT area, MAX(value) FILTER (WHERE cat01 = 'F2211') AS second_ind, MAX(value) FILTER (WHERE cat01 = 'F1102') AS workers FROM e_stat.ssds.f_municipal_labor WHERE year = 2020 AND cat01 IN ('F2211', 'F1102') GROUP BY area), j AS (SELECT folded.corps, folded.certified, sec.second_ind * 100.0 / sec.workers AS share FROM folded JOIN sec ON sec.area = folded.area WHERE sec.workers > 0) SELECT CASE WHEN share < 15 THEN '15%未満' WHEN share < 20 THEN '15〜20%' WHEN share < 25 THEN '20〜25%' WHEN share < 30 THEN '25〜30%' ELSE '30%以上' END AS band, CASE WHEN share < 15 THEN 1 WHEN share < 20 THEN 2 WHEN share < 25 THEN 3 WHEN share < 30 THEN 4 ELSE 5 END AS ord, COUNT(*) AS municipalities, ROUND(CAST(SUM(certified) AS DOUBLE) * 10000 / SUM(corps), 1) AS rate FROM j GROUP BY band, ord ORDER BY ord
```

```sql id=city_top
WITH cert AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_certification WHERE title = '事業継続力強化計画認定'), raw AS (SELECT substr(lg_code, 1, 5) AS ac, COUNT(*) AS corps, COUNT(*) FILTER (WHERE corporate_number IN (SELECT corporate_number FROM cert)) AS certified FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301', '302', '303', '304', '305') AND lg_code IS NOT NULL GROUP BY ac), folded AS (SELECT c.municipality_code AS area, SUM(raw.corps) AS corps, SUM(raw.certified) AS certified FROM raw JOIN soumu.code.municipality c ON c.area_code = raw.ac WHERE c.municipality_code IS NOT NULL GROUP BY c.municipality_code), named AS (SELECT n.pref_name || ' ' || COALESCE(n.municipality_name, n.designated_city_name) AS label, folded.corps, folded.certified, CAST(folded.certified AS DOUBLE) * 10000 / folded.corps AS rate FROM folded JOIN soumu.code.municipality n ON n.area_code = folded.area AND n.is_municipality WHERE folded.corps >= 1000), ranked AS (SELECT label, ROUND(rate, 1) AS rate, ROW_NUMBER() OVER (ORDER BY rate DESC, label) AS rn FROM named) SELECT label, rate FROM ranked WHERE rn <= 15 ORDER BY rn
```
