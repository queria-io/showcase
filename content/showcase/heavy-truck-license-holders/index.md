---
title: 大型免許を持つ75歳未満の人は10年で17%減り、人口が増えた東京都でも19%減りました
description: 大型免許の保有者を都道府県別に2014年末から2024年末まで集計しました。75歳未満の保有者は17.1%減り、15〜74歳の人口の減少率6.2%の約2.8倍です。北海道を除く46都府県で、保有者が人口より速く減っています。
publishedAt: 2026-09-29
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 運転免許
  - 物流
  - 人口推計
datasets:
  - queria/e_stat
sources:
  - title: 運転免許統計
    url: https://www.npa.go.jp/publications/statistics/koutsuu/menkyo.html
    publisher: 警察庁
  - title: 人口推計
    url: https://www.stat.go.jp/data/jinsui/index.html
    publisher: 総務省統計局
agentHint: 大型免許の保有者に占める75歳以上の割合を、都道府県別に2014年から2024年まで出して。割合の上がり方が速い県を並べて
socialAnnounce: |-
  大型免許の保有者数を都道府県別に2014年末から10年分追い、15〜74歳の人口の推移と比べました。

  トラックドライバーの採用計画や育成の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

大型免許を持つ75歳未満の人は、2014年末の4,128,973人から2024年末の3,422,131人へ、10年で17.1%減りました。同じ期間に15〜74歳の人口は6.2%減っており、保有者はその約2.8倍の速さで減っています。15〜74歳の人口が3.4%増えた東京都でも、保有者は19.1%減りました。保有者が人口より速く減っていないのは北海道だけです。

地方の運送会社では、大型トラックのドライバーを大型免許を持っている人から採用する前提で募集することが今も多くあります。この記事では、警察庁の[運転免許統計](https://www.npa.go.jp/publications/statistics/koutsuu/menkyo.html)を都道府県別に10年分集計し、大型免許の保有者の減り方を、同じ期間の人口の減り方と比較しました。

## 大型免許の保有者のうち75歳以上は14.2%で、10年で2.2倍になった

データは e-Stat「社会・人口統計体系」の都道府県別の安全に関するデータ（`k_pref_safety`）にある運転免許保有者数です。大型免許については、次の2つの項目が2014年から2024年まで毎年あります。値は各年の12月31日現在です。

| コード  | 内容                                         |
| ------- | -------------------------------------------- |
| K3501   | 運転免許保有者数（第一種免許 大型）          |
| K350101 | 運転免許保有者数（第一種免許 大型 75歳以上） |

ここでは K3501 から K350101 を引いた人数を「75歳未満」とし、75歳以上と分けて積み上げました。75歳未満には、すでに運転の仕事を離れた65〜74歳の人も含まれます。大型バスなどを運転する第二種の大型免許の保有者は、第二種の項目に集計されるので、ここには含まれません。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"fold": ["under75", "over75"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"under75\": \"75歳未満\", \"over75\": \"75歳以上\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"under75\",\"over75\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "x": {
          "field": "year",
          "type": "ordinal",
          "axis": {"title": "年末", "labelAngle": 0, "labelOverlap": "greedy"},
          "sort": null
        },
        "y": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "大型免許の保有者数（人）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["75歳未満", "75歳以上"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "tooltip": [
          {"field": "year", "type": "ordinal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ]
}
```

大型免許の保有者は、2014年末の4,387,969人から2024年末の3,987,111人へ、9.1%減りました。75歳以上は258,996人から564,980人へ2.2倍になり、保有者全体に占める割合は5.9%から14.2%に上がりました。およそ7人に1人が75歳以上です。

75歳未満の保有者は、4,128,973人から3,422,131人へ、10年で17.1%、70万7千人減っています。この間に75歳以上は305,984人増えたので、75歳になって75歳以上に移った人は少なくともこの人数です。残りの多くても40万人ほどは、新しく大型免許を取得した人が、免許を手放した人の数を下回った分にあたります。

## 46都府県で、大型免許の保有者は15〜74歳の人口より速く減っている

同じ10年の15〜74歳の人口の増減と比較しました。人口は[人口推計](https://www.stat.go.jp/data/jinsui/index.html)の各年10月1日現在の値で、総人口から15歳未満と75歳以上を引いて算出しています。大型免許は普通免許より高い年齢にならないと取得できないので、この人口は免許を取得できる年齢より少し広い範囲です。

```chart
{
  "layer": [
    {
      "data": {"name": "pref"},
      "mark": {"type": "point", "color": "#3b82f6", "opacity": 0.7, "filled": true, "size": 64},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_chg", "type": "quantitative"},
          {"field": "license_chg", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_chg",
          "type": "quantitative",
          "scale": {"domain": [-26, 5], "zero": false, "nice": false},
          "axis": {"title": "15〜74歳人口の増減率 2014→2024（%）", "grid": true}
        },
        "y": {
          "field": "license_chg",
          "type": "quantitative",
          "scale": {"domain": [-26, 5], "zero": false, "nice": false},
          "axis": {"title": "75歳未満の大型免許保有者の増減率（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_hl"},
      "mark": {"type": "point", "color": "#ef4444", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_chg", "type": "quantitative"},
          {"field": "license_chg", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_chg",
          "type": "quantitative",
          "scale": {"domain": [-26, 5], "zero": false, "nice": false},
          "axis": {"title": "15〜74歳人口の増減率 2014→2024（%）", "grid": true}
        },
        "y": {
          "field": "license_chg",
          "type": "quantitative",
          "scale": {"domain": [-26, 5], "zero": false, "nice": false},
          "axis": {"title": "75歳未満の大型免許保有者の増減率（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "pref_hl"},
      "mark": {"type": "text", "baseline": "bottom", "dy": -6},
      "encoding": {
        "x": {
          "field": "pop_chg",
          "type": "quantitative",
          "scale": {"domain": [-26, 5], "zero": false, "nice": false},
          "axis": {"title": "15〜74歳人口の増減率 2014→2024（%）", "grid": true}
        },
        "y": {
          "field": "license_chg",
          "type": "quantitative",
          "scale": {"domain": [-26, 5], "zero": false, "nice": false},
          "axis": {"title": "75歳未満の大型免許保有者の増減率（%）", "grid": true}
        },
        "text": {"field": "area_name"}
      }
    },
    {
      "data": {"values": [{}]},
      "mark": {"type": "rule", "color": "#64748b", "strokeDash": [6, 4]},
      "encoding": {
        "x": {"datum": -26, "type": "quantitative"},
        "x2": {"datum": 5, "type": "quantitative"},
        "y": {"datum": -26, "type": "quantitative"},
        "y2": {"datum": 5, "type": "quantitative"}
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
        "x": {"datum": 4, "type": "quantitative"},
        "y": {"datum": -25, "type": "quantitative"},
        "text": {"value": "この線より下は人口より速く減った都道府県"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

全国では、15〜74歳の人口が10年で6.2%減り、75歳未満の大型免許の保有者は17.1%減りました。保有者の減少率は、人口の減少率の約2.8倍です。

破線は、人口と同じ割合で減った場合の位置です。47都道府県のうち46都府県がこの線より下にあり、保有者が人口より速く減っています。15〜74歳の人口が3.4%増えた東京都でも、75歳未満の保有者は19.1%減りました。人口が2.6%増えた沖縄県でも9.3%減っています。線より上にあるのは北海道だけで、人口が10.8%減ったのに対し、保有者は10.1%減でした。北海道の保有者は2024年末でも15〜74歳の人口1,000人あたり62.0人で、全国の38.4人より多くなっています。

保有者が人口より速く減るのは、大型免許の保有者が高い年代に多く、若い世代で新しく取得する人がその減少分を補っていないためと考えられます。

## 10年で2割以上減った県は11あり、最も減ったのは大分県の23.5%

75歳未満の大型免許の保有者の、10年間の増減率を都道府県別に並べました。棒にカーソルを合わせると、2024年の15〜74歳の人口1,000人あたりの保有者数も表示されます。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "over20"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "license_chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "license_chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "75歳未満の大型免許保有者の増減率 2014→2024（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "2割以上減った11県",
          "type": "nominal",
          "scale": {
            "domain": ["2割以上減った11県", "15〜20%減った28都県", "減少が15%未満の8道府県"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "license_chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "license_chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "75歳未満の大型免許保有者の増減率 2014→2024（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "15〜20%減った28都県",
          "type": "nominal",
          "scale": {
            "domain": ["2割以上減った11県", "15〜20%減った28都県", "減少が15%未満の8道府県"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "under15"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "license_chg", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "license_chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "75歳未満の大型免許保有者の増減率 2014→2024（%）", "grid": true}
        },
        "y": {"field": "area_name", "type": "nominal", "axis": {"title": "都道府県"}, "sort": null},
        "color": {
          "datum": "減少が15%未満の8道府県",
          "type": "nominal",
          "scale": {
            "domain": ["2割以上減った11県", "15〜20%減った28都県", "減少が15%未満の8道府県"],
            "range": ["#ef4444", "#fca5a5", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ]
}
```

最も大きく減ったのは大分県の23.5%で、秋田県が23.3%、山形県が23.2%で続きます。この3県では10年で4分の1近くが減りました。2割以上減ったのは長野県までの11県で、そのうち秋田・山形・島根・富山・福井・新潟・石川の7県は日本海側の県です。減少率が最も小さいのは沖縄県の9.3%で、北海道が10.1%、福岡県と熊本県が13.4%です。保有者が増えた都道府県はありません。

2024年末の75歳未満の保有者を15〜74歳の人口1,000人あたりで見ると、全国は38.4人です。最も多いのは青森県の86.3人で、秋田県が80.0人、岩手県が74.2人、山形県が73.9人です。最も少ないのは東京都の13.8人で、神奈川県が21.3人、大阪府が21.4人です。秋田県と山形県は、人口あたりの保有者数が全国で最も多い県に入り、減少率も全国で最も大きい県に入っています。

## 業務での使い方

- 自社の営業所がある県の、人口あたりの保有者数と減少率を確認できます。保有者が多い県でも、10年で2割を超えて減っていれば、大型免許を持つ人から採用できる人数は年々少なくなります
- 普通免許や中型免許の人を採用して大型免許を取得させる育成の費用を、採用計画に最初から含めることを検討できます。人口が増えている東京都でも保有者は減っているので、都市部でも同じ前提で計画する必要があります

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別データを 2026-09-29 時点で集計しています。大型免許の保有者数は警察庁の[運転免許統計](https://www.npa.go.jp/publications/statistics/koutsuu/menkyo.html)による各年12月31日現在の値、人口は総務省統計局の[人口推計](https://www.stat.go.jp/data/jinsui/index.html)による各年10月1日現在の値です。

Queriaは、運転免許統計や人口推計を含む都道府県別の統計を、列名・単位・地域名を統一したテーブルにし、項目の意味をメタデータに記載して公開しています。本記事で使った[都道府県別の安全に関するテーブル](/datasets/queria/e_stat/ssds/k_pref_safety)と[都道府県別の人口テーブル](/datasets/queria/e_stat/ssds/a_pref_population)から、自社の営業所がある県の数字を確認したり、近隣の県と比較したりできます。

```sql id=national
SELECT year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75, MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS over75, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) AS total, ROUND(100 * MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) / MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END), 1) AS over75_share FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND area_name = '全国' AND year BETWEEN 2014 AND 2024 GROUP BY year ORDER BY year
```

```sql id=japan
WITH lic AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75 FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND year IN (2014, 2024) GROUP BY area_name, year), pop AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN value END) - MAX(CASE WHEN cat01 = 'A1301' THEN value END) - MAX(CASE WHEN cat01 = 'A1419' THEN value END) AS pop15_74 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1301', 'A1419') AND year IN (2014, 2024) GROUP BY area_name, year), chg AS (SELECT a.area_name, a.under75 AS under75_2014, b.under75 AS under75_2024, ROUND(100 * (b.under75 / a.under75 - 1), 1) AS license_chg, ROUND(100 * (pb.pop15_74 / pa.pop15_74 - 1), 1) AS pop_chg, ROUND(1000 * b.under75 / pb.pop15_74, 1) AS per1000 FROM lic a JOIN lic b ON b.area_name = a.area_name AND b.year = 2024 JOIN pop pa ON pa.area_name = a.area_name AND pa.year = 2014 JOIN pop pb ON pb.area_name = a.area_name AND pb.year = 2024 WHERE a.year = 2014) SELECT area_name, license_chg, pop_chg, per1000 FROM chg WHERE area_name = '全国'
```

```sql id=pref
WITH lic AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75 FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND year IN (2014, 2024) GROUP BY area_name, year), pop AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN value END) - MAX(CASE WHEN cat01 = 'A1301' THEN value END) - MAX(CASE WHEN cat01 = 'A1419' THEN value END) AS pop15_74 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1301', 'A1419') AND year IN (2014, 2024) GROUP BY area_name, year), chg AS (SELECT a.area_name, a.under75 AS under75_2014, b.under75 AS under75_2024, ROUND(100 * (b.under75 / a.under75 - 1), 1) AS license_chg, ROUND(100 * (pb.pop15_74 / pa.pop15_74 - 1), 1) AS pop_chg FROM lic a JOIN lic b ON b.area_name = a.area_name AND b.year = 2024 JOIN pop pa ON pa.area_name = a.area_name AND pa.year = 2014 JOIN pop pb ON pb.area_name = a.area_name AND pb.year = 2024 WHERE a.year = 2014) SELECT area_name, license_chg, pop_chg FROM chg WHERE area_name <> '全国' ORDER BY area_name
```

```sql id=pref_hl
WITH lic AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75 FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND year IN (2014, 2024) GROUP BY area_name, year), pop AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN value END) - MAX(CASE WHEN cat01 = 'A1301' THEN value END) - MAX(CASE WHEN cat01 = 'A1419' THEN value END) AS pop15_74 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1301', 'A1419') AND year IN (2014, 2024) GROUP BY area_name, year), chg AS (SELECT a.area_name, a.under75 AS under75_2014, b.under75 AS under75_2024, ROUND(100 * (b.under75 / a.under75 - 1), 1) AS license_chg, ROUND(100 * (pb.pop15_74 / pa.pop15_74 - 1), 1) AS pop_chg FROM lic a JOIN lic b ON b.area_name = a.area_name AND b.year = 2024 JOIN pop pa ON pa.area_name = a.area_name AND pa.year = 2014 JOIN pop pb ON pb.area_name = a.area_name AND pb.year = 2024 WHERE a.year = 2014) SELECT area_name, license_chg, pop_chg FROM chg WHERE area_name IN ('北海道', '東京都', '沖縄県', '大分県') ORDER BY area_name
```

```sql id=over20
WITH lic AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75 FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND year IN (2014, 2024) GROUP BY area_name, year), pop AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN value END) - MAX(CASE WHEN cat01 = 'A1301' THEN value END) - MAX(CASE WHEN cat01 = 'A1419' THEN value END) AS pop15_74 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1301', 'A1419') AND year IN (2014, 2024) GROUP BY area_name, year), chg AS (SELECT a.area_name, a.under75 AS under75_2014, b.under75 AS under75_2024, ROUND(100 * (b.under75 / a.under75 - 1), 1) AS license_chg, ROUND(100 * (pb.pop15_74 / pa.pop15_74 - 1), 1) AS pop_chg, ROUND(1000 * b.under75 / pb.pop15_74, 1) AS per1000 FROM lic a JOIN lic b ON b.area_name = a.area_name AND b.year = 2024 JOIN pop pa ON pa.area_name = a.area_name AND pa.year = 2014 JOIN pop pb ON pb.area_name = a.area_name AND pb.year = 2024 WHERE a.year = 2014) SELECT area_name, license_chg, pop_chg, per1000 FROM chg WHERE area_name <> '全国' AND license_chg <= -20 ORDER BY license_chg, area_name
```

```sql id=mid
WITH lic AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75 FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND year IN (2014, 2024) GROUP BY area_name, year), pop AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN value END) - MAX(CASE WHEN cat01 = 'A1301' THEN value END) - MAX(CASE WHEN cat01 = 'A1419' THEN value END) AS pop15_74 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1301', 'A1419') AND year IN (2014, 2024) GROUP BY area_name, year), chg AS (SELECT a.area_name, a.under75 AS under75_2014, b.under75 AS under75_2024, ROUND(100 * (b.under75 / a.under75 - 1), 1) AS license_chg, ROUND(100 * (pb.pop15_74 / pa.pop15_74 - 1), 1) AS pop_chg, ROUND(1000 * b.under75 / pb.pop15_74, 1) AS per1000 FROM lic a JOIN lic b ON b.area_name = a.area_name AND b.year = 2024 JOIN pop pa ON pa.area_name = a.area_name AND pa.year = 2014 JOIN pop pb ON pb.area_name = a.area_name AND pb.year = 2024 WHERE a.year = 2014) SELECT area_name, license_chg, pop_chg, per1000 FROM chg WHERE area_name <> '全国' AND license_chg > -20 AND license_chg <= -15 ORDER BY license_chg, area_name
```

```sql id=under15
WITH lic AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'K3501' THEN TRY_CAST(value AS DOUBLE) END) - MAX(CASE WHEN cat01 = 'K350101' THEN TRY_CAST(value AS DOUBLE) END) AS under75 FROM e_stat.ssds.k_pref_safety WHERE cat01 IN ('K3501', 'K350101') AND year IN (2014, 2024) GROUP BY area_name, year), pop AS (SELECT area_name, year, MAX(CASE WHEN cat01 = 'A1101' THEN value END) - MAX(CASE WHEN cat01 = 'A1301' THEN value END) - MAX(CASE WHEN cat01 = 'A1419' THEN value END) AS pop15_74 FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1101', 'A1301', 'A1419') AND year IN (2014, 2024) GROUP BY area_name, year), chg AS (SELECT a.area_name, a.under75 AS under75_2014, b.under75 AS under75_2024, ROUND(100 * (b.under75 / a.under75 - 1), 1) AS license_chg, ROUND(100 * (pb.pop15_74 / pa.pop15_74 - 1), 1) AS pop_chg, ROUND(1000 * b.under75 / pb.pop15_74, 1) AS per1000 FROM lic a JOIN lic b ON b.area_name = a.area_name AND b.year = 2024 JOIN pop pa ON pa.area_name = a.area_name AND pa.year = 2014 JOIN pop pb ON pb.area_name = a.area_name AND pb.year = 2024 WHERE a.year = 2014) SELECT area_name, license_chg, pop_chg, per1000 FROM chg WHERE area_name <> '全国' AND license_chg > -15 ORDER BY license_chg, area_name
```
