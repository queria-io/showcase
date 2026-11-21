---
title: 従業員101〜300人の会社の23.2%は、女性の管理職が1人もいない
description: 厚生労働省の女性の活躍推進企業データベースで、従業員101〜300人の1万1239社を集計しました。女性管理職がゼロの会社は23.2%で、業種別では2.1%から67.6%まで差があり、女性従業員が6割以上の会社でも10.9%がゼロでした。
ogDescription: 厚生労働省のデータベースで従業員101〜300人の1万1239社を集計しました。女性管理職がゼロの会社は23.2%で、業種別では2.1%から67.6%まで差があります。
publishedAt: 2026-08-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 女性活躍
  - 厚生労働省
  - 人事
datasets:
  - queria/positive_ryouritsu
  - queria/gbizinfo
sources:
  - title: 女性の活躍推進企業データベース オープンデータ
    url: https://positive-ryouritsu.mhlw.go.jp/positivedb/opendata/
    publisher: 厚生労働省
  - title: 改正女性活躍推進法の概要
    url: https://www.mhlw.go.jp/content/001668255.pdf
    publisher: 厚生労働省
  - title: gBizINFO（Gビズインフォ）
    url: https://info.gbiz.go.jp/
    publisher: 経済産業省
agentHint: 従業員101〜300人の会社を業種(industry)別に数えて、女性管理職比率(women_in_management_pct)が0%の会社の割合と、係長級(women_in_kakaricho_pct)が0%の会社の割合を並べて出して
socialAnnounce: |-
  厚生労働省のデータベースで従業員101〜300人の1万1239社を数えました。

  女性の管理職がゼロの会社は23.2%。業種で2.1%〜67.6%と開きます。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

従業員101〜300人で女性管理職の割合を公表している11,239社のうち、2,609社（23.2%）は女性の管理職が1人もいません。業種別では医療、福祉の2.1%から輸送用機械器具製造業の67.6%まで差があります。従業員の60%以上が女性の会社でも10.9%、係長級の30%以上が女性の会社でも9.2%が、女性管理職ゼロでした。

[改正女性活躍推進法](https://www.mhlw.go.jp/content/001668255.pdf)が2026年4月に施行され、従業員101人以上の企業は管理職に占める女性の割合を公表することになりました。公表する企業にとっては、同じ規模・同じ業種の会社と比較して自社の数字が高いか低いかが問題になります。

使ったのは[厚生労働省の女性の活躍推進企業データベース](https://positive-ryouritsu.mhlw.go.jp/positivedb/opendata/)です。企業自身が登録した数字が1社1行で入っていて、管理職・係長級に占める女性の割合、男女の賃金の差異、育児休業の取得率などを含みます。管理職の割合は、各社が課長相当職以上を対象に算出して公表した値です。

## 女性管理職ゼロの会社は、規模が小さいほど多い

管理職の女性の割合の公表値が0%の会社を、規模ごとに集計しました。対象は公表が義務づけられている101人以上の会社です。100人以下は努力義務なので、登録企業は自主的に取り組む会社に偏ります。101〜300人の会社で管理職の割合が必須項目になったのは今年からで、それ以前は選択項目の一つでした。最終更新が今年4月より前の5,238社ではゼロが20.2%、今年4月以降に更新した6,001社では25.9%で、公表する項目を選べた時期のほうが低くなっています。

グラフの棒は「女性管理職ゼロの会社の割合」、折れ線は「女性管理職比率の中央値」です。

```chart
{
  "height": 320,
  "layer": [
    {
      "layer": [
        {
          "data": {"name": "by_size"},
          "mark": {"type": "bar"},
          "encoding": {
            "tooltip": [
              {"field": "zero_pct", "type": "quantitative"},
              {"field": "size_band", "type": "nominal"}
            ],
            "x": {
              "field": "size_band",
              "type": "nominal",
              "axis": {"title": "従業員規模", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "zero_pct",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "ゼロの会社の割合（%）", "grid": true}
            },
            "color": {
              "datum": "女性管理職ゼロの会社の割合",
              "type": "nominal",
              "scale": {
                "domain": ["女性管理職ゼロの会社の割合", "女性管理職比率の中央値"],
                "range": ["#7c3aed", "#f97316"]
              },
              "title": null
            }
          }
        },
        {
          "data": {"name": "by_size"},
          "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
          "encoding": {
            "x": {
              "field": "size_band",
              "type": "nominal",
              "axis": {"title": "従業員規模", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "zero_pct",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "ゼロの会社の割合（%）", "grid": true}
            },
            "text": {"field": "zero_pct"}
          }
        }
      ]
    },
    {
      "layer": [
        {
          "data": {"name": "by_size"},
          "transform": [
            {"window": [{"op": "row_number", "as": "__row"}]},
            {
              "calculate": "isValid(datum[\"size_band\"]) && isValid(datum[\"median_pct\"]) ? 0 : 1",
              "as": "__gap"
            },
            {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
            {"filter": "datum.__gap == 0"}
          ],
          "mark": {
            "type": "line",
            "color": "#f97316",
            "invalid": "break-paths-show-domains",
            "point": {"filled": true, "size": 49}
          },
          "encoding": {
            "tooltip": [
              {"field": "size_band", "type": "nominal"},
              {"field": "median_pct", "type": "quantitative"}
            ],
            "x": {
              "field": "size_band",
              "type": "nominal",
              "axis": {"title": "従業員規模", "labelAngle": 0},
              "sort": null
            },
            "y": {
              "field": "median_pct",
              "type": "quantitative",
              "scale": {"zero": true},
              "axis": {"title": "中央値（%）", "orient": "right"}
            },
            "color": {
              "datum": "女性管理職比率の中央値",
              "type": "nominal",
              "scale": {
                "domain": ["女性管理職ゼロの会社の割合", "女性管理職比率の中央値"],
                "range": ["#7c3aed", "#f97316"]
              },
              "title": null
            },
            "order": {"field": "__row", "type": "quantitative"},
            "detail": {"field": "__segment"}
          }
        }
      ]
    }
  ],
  "resolve": {"scale": {"y": "independent"}},
  "config": {"legend": {"orient": "bottom"}}
}
```

101〜300人の会社は11,239社が公表していて、そのうち2,609社（23.2%）が女性管理職ゼロです。おおよそ4社に1社です。この割合は規模が大きくなるほど下がり、301〜500人で15.5%、501〜1000人で10.6%、1001〜5000人で4.6%、5001人以上では1.1%です。

折れ線で示した中央値は、反対に101〜300人が12.1%で最も高くなっています。301〜500人は10.5%、501〜1000人は10.0%、1001〜5000人は9.1%、5001人以上は9.7%で、いずれも101〜300人を下回ります。中央値で比較すると小さい会社のほうが女性管理職の割合は高い一方、ゼロの会社は小さい会社に多くあります。101〜300人の会社は、女性の登用が進んだ会社と、女性の管理職がいない会社に分かれています。

## 女性管理職ゼロの会社の割合は、業種によって2.1%から67.6%まで差がある

101〜300人の会社を業種別に分け、ゼロの会社の割合を集計しました。公表社数が少ないと1社の増減で割合が大きく変わるので、公表社数が100社以上の18業種に絞っています。図の区分名は長いものを略記しています。

```chart
{
  "height": 600,
  "layer": [
    {
      "data": {"name": "by_industry"},
      "mark": {"type": "bar", "color": "#7c3aed"},
      "encoding": {
        "tooltip": [
          {"field": "zero_pct", "type": "quantitative"},
          {"field": "industry", "type": "nominal"}
        ],
        "x": {
          "field": "zero_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性管理職ゼロの会社の割合（%）", "grid": true}
        },
        "y": {
          "field": "industry",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "by_industry"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "zero_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性管理職ゼロの会社の割合（%）", "grid": true}
        },
        "y": {
          "field": "industry",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "text": {"field": "zero_pct"}
      }
    }
  ]
}
```

業種による差は、規模による差より大きくなっています。最も高い輸送用機械器具製造業は142社中67.6%で、3社に2社が女性管理職ゼロです。鉄鋼業、非鉄金属・金属製品製造業が50.6%、運輸業、郵便業が598社で45.8%と続きます。最も低い医療、福祉は1,985社中2.1%で、金融業、保険業が6.5%、化学工業が6.9%、教育、学習支援業が9.0%、情報通信業が680社で10.0%です。最も高い業種と低い業種で32倍の差があります。同じ従業員101〜300人の会社でも、輸送用機械器具製造業ではゼロの会社が多数で、医療、福祉ではごく少数です。

## 女性従業員が60%以上の会社でも、10.9%は女性管理職がゼロ

ゼロの割合が高い業種に製造業と運輸業が並び、低い業種に医療、福祉が並ぶのは、働いている女性の数が業種によって違うためとも考えられます。これを確認するため、[gBizINFO](https://info.gbiz.go.jp/)の女性従業員比率を使いました。gBizINFOは、政府が持つ法人情報を法人番号で名寄せして公開しているサービスです。

法人番号で照合して両方の数字がある会社は、101〜300人の会社のうち5,057社です。以下はこの5,057社の集計です。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "by_female_ratio"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "zero_pct", "type": "quantitative"},
          {"field": "band", "type": "nominal"}
        ],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "従業員に占める女性の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "zero_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性管理職ゼロの会社の割合（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "by_female_ratio"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "従業員に占める女性の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "zero_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性管理職ゼロの会社の割合（%）", "grid": true}
        },
        "text": {"field": "zero_pct"}
      }
    }
  ]
}
```

女性従業員が少ない会社ほど、ゼロの会社の割合は高くなります。女性が20%未満の1,095社では41.1%、20〜40%で26.5%、40〜60%で17.3%です。

従業員の60%以上が女性の1,668社でも、182社（10.9%）は管理職に女性が1人もいません。女性従業員の割合が高いとゼロの会社は少なくなりますが、女性従業員の割合だけではゼロの会社があることを説明できません。

## 係長級の30%以上が女性の会社でも、9.2%は女性管理職がゼロ

このデータベースには、管理職の1つ下の係長級に占める女性の割合も収録されています。係長級の公表は任意で、101〜300人の会社では管理職とあわせて3,936社が公表しています。

```chart
{
  "height": 280,
  "layer": [
    {
      "data": {"name": "by_kakaricho"},
      "mark": {"type": "bar", "color": "#22c55e"},
      "encoding": {
        "tooltip": [
          {"field": "zero_pct", "type": "quantitative"},
          {"field": "band", "type": "nominal"}
        ],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "係長級に占める女性の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "zero_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性管理職ゼロの会社の割合（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "by_kakaricho"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "係長級に占める女性の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "zero_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "女性管理職ゼロの会社の割合（%）", "grid": true}
        },
        "text": {"field": "zero_pct"}
      }
    }
  ]
}
```

係長級にも女性がいない557社では、69.5%が管理職もゼロです。係長級の女性が0%超10%未満だと43.7%、10〜30%で29.6%に下がります。

係長級の30%以上が女性の1,667社でも、154社（9.2%）は女性の管理職がゼロです。この154社では、管理職の候補になる女性がいないことは理由になりません。

## 自社の数字の位置を確認する手順

公表義務が始まった今年は、自社の数字を同じ業種・規模の会社と比較して説明する必要があります。ここまでの分布は、次の手順で使えます。

1. 自社の業種を見て、その業種でゼロの会社がどれくらいあるかを確認します
2. その業種の中で、自社が0%の会社に入るかどうかを確認します
3. 0%側なら、従業員に占める女性の割合を確認します。60%以上いてゼロであれば、採用ではなく登用の側に理由があると考えられます
4. 係長級の数字も並べます。係長級の3割が女性で管理職がゼロであれば、候補者がいないことは理由になりません

## データの出典

本記事は[厚生労働省の女性の活躍推進企業データベース](https://positive-ryouritsu.mhlw.go.jp/positivedb/opendata/)のオープンデータを2026年8月9日時点で集計しています。従業員に占める女性の割合は[gBizINFO](https://info.gbiz.go.jp/)の企業情報を法人番号で照合したもので、公表値はいずれも各社が自ら登録し、更新した日付も会社ごとに異なります。

Queriaは、企業が公表した指標を1社1行のテーブルにし、法人番号で他の行政データと結合できる形で、列の説明を付けて公開しています。本記事で使った[女性活躍推進企業テーブル](/datasets/queria/positive_ryouritsu/josei_katsuyaku/company)から自社と同じ業種・規模の会社を抽出したり、[gBizINFOの企業テーブル](/datasets/queria/gbizinfo/main/mart_gbizinfo_company)と結合して従業員構成も含めて比較したりできます。

```sql id=by_size
SELECT company_size AS size_band, COUNT(*) AS n, SUM(CASE WHEN women_in_management_pct = 0 THEN 1 ELSE 0 END) AS zero_n, ROUND(CAST(SUM(CASE WHEN women_in_management_pct = 0 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS zero_pct, ROUND(QUANTILE_CONT(women_in_management_pct, 0.5), 1) AS median_pct FROM positive_ryouritsu.josei_katsuyaku.company WHERE women_in_management_pct IS NOT NULL AND company_size IN ('101～300人', '301～500人', '501～1000人', '1001～5000人', '5001人以上') GROUP BY company_size ORDER BY CASE company_size WHEN '101～300人' THEN 1 WHEN '301～500人' THEN 2 WHEN '501～1000人' THEN 3 WHEN '1001～5000人' THEN 4 ELSE 5 END
```

```sql id=by_mandate
SELECT CASE WHEN last_updated >= DATE '2026-04-01' THEN '2026年4月以降に更新' ELSE 'それ以前' END AS b, COUNT(*) AS n, ROUND(CAST(SUM(CASE WHEN women_in_management_pct = 0 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS zero_pct FROM positive_ryouritsu.josei_katsuyaku.company WHERE company_size = '101～300人' AND women_in_management_pct IS NOT NULL GROUP BY 1 ORDER BY b
```

```sql id=by_industry
SELECT CASE industry WHEN '電子部品・デバイス・電子回路・電気機械器具・情報通信機械器具製造業' THEN '電子部品・電気機械器具製造業' ELSE industry END AS industry, COUNT(*) AS n, ROUND(CAST(SUM(CASE WHEN women_in_management_pct = 0 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS zero_pct FROM positive_ryouritsu.josei_katsuyaku.company WHERE company_size = '101～300人' AND women_in_management_pct IS NOT NULL GROUP BY 1 HAVING COUNT(*) >= 100 ORDER BY zero_pct DESC, industry
```

```sql id=by_female_ratio
SELECT CASE WHEN g.female_ratio < 20 THEN '20%未満' WHEN g.female_ratio < 40 THEN '20〜40%' WHEN g.female_ratio < 60 THEN '40〜60%' ELSE '60%以上' END AS band, COUNT(*) AS n, SUM(CASE WHEN c.women_in_management_pct = 0 THEN 1 ELSE 0 END) AS zero_n, ROUND(CAST(SUM(CASE WHEN c.women_in_management_pct = 0 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS zero_pct FROM positive_ryouritsu.josei_katsuyaku.company c JOIN gbizinfo.main.mart_gbizinfo_company g ON c.corporate_number = g.corporate_number WHERE c.company_size = '101～300人' AND c.women_in_management_pct IS NOT NULL AND g.female_ratio IS NOT NULL GROUP BY 1 ORDER BY MIN(g.female_ratio)
```

```sql id=by_kakaricho
SELECT CASE WHEN women_in_kakaricho_pct = 0 THEN '0%' WHEN women_in_kakaricho_pct < 10 THEN '0%超10%未満' WHEN women_in_kakaricho_pct < 30 THEN '10〜30%' ELSE '30%以上' END AS band, COUNT(*) AS n, SUM(CASE WHEN women_in_management_pct = 0 THEN 1 ELSE 0 END) AS zero_n, ROUND(CAST(SUM(CASE WHEN women_in_management_pct = 0 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS zero_pct FROM positive_ryouritsu.josei_katsuyaku.company WHERE company_size = '101～300人' AND women_in_management_pct IS NOT NULL AND women_in_kakaricho_pct IS NOT NULL GROUP BY 1 ORDER BY MIN(women_in_kakaricho_pct)
```
