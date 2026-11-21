---
title: 30代後半で子どもを産む女性の割合は、港区・千代田区・中央区が沖縄県より高い
description: 2024年、35〜39歳の女性1,000人あたりの出生数は東京の港区・千代田区・中央区の合計で81.1と、沖縄県の69.0、全国の53.2を上回りました。20代後半は全国より少なく、出産が30代後半以降に寄っています。
publishedAt: 2026-11-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口動態統計
  - 出生
  - 国勢調査
  - 産婦人科
  - 開業
datasets:
  - queria/e_stat
sources:
  - title: 人口動態統計
    url: https://www.mhlw.go.jp/toukei/list/81-1.html
    publisher: 厚生労働省
  - title: 令和7年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2025/index.html
    publisher: 総務省統計局
agentHint: 自分の県の市区町村ごとに、2024年の母の年齢5歳階級別の出生数を2025年国勢調査の日本人女性の人口で割って、35〜39歳と40〜44歳の女性1,000人あたりの出生数を出して。出生数が年300人以上の市区町村に絞って、全国の値と並べて
socialAnnounce: |-
  35〜39歳の女性1,000人あたりの出生数は、港区・千代田区・中央区の合計で81.1。沖縄県の69.0、全国の53.2を上回りました（2024年）。

  産婦人科クリニックの開業地選びに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

2024年に35〜39歳の女性1,000人あたりに生まれた子どもは、東京の港区・千代田区・中央区（以下、都心3区）の合計で81.1人でした。出生の多い県として知られる沖縄県の69.0人、全国の53.2人を上回ります。40〜44歳では都心3区が24.8人で、全国12.4人のちょうど2倍です。25〜29歳は41.3人で、全国の64.4人を大きく下回ります。都心3区では、全国より30代後半以降に出産する人が多くなっています。

この値は、厚生労働省の[人口動態統計](https://www.mhlw.go.jp/toukei/list/81-1.html)の母の年齢別出生数を、総務省統計局の[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)の日本人女性の年齢別人口で割って出しました。産婦人科クリニックの開業地を探すときは、地域の出生数に加えて、どの年齢の女性が出産しているかも判断材料になります。同じ出生数でも、母親が20代中心の地域と30代後半以上が多い地域とでは、妊婦健診で求められる対応や、出生前検査・不妊治療の相談の多さが変わると考えられます。

## 年齢ごとに見ると、都心3区は30代後半から沖縄県を上回る

[母の年齢別出生数のテーブル](/datasets/queria/e_stat/vital_statistics/births_by_mother_age)は、人口動態統計の出生数を、母の住所の市区町村ごとに母の年齢5歳階級別で2015年から2024年まで収録しています。数えているのは日本人の子どもの出生です。年齢の区分は次のとおりです。

| 区分名   | コード（`mother_age_code`） |
| -------- | --------------------------- |
| 14歳以下 | 00190                       |
| 15〜19歳 | 00220                       |
| 20〜24歳 | 00230                       |
| 25〜29歳 | 00240                       |
| 30〜34歳 | 00250                       |
| 35〜39歳 | 00260                       |
| 40〜44歳 | 00280                       |
| 45〜49歳 | 00300                       |
| 50歳以上 | 00310                       |
| 不詳     | 00450                       |

この出生数を、[2025年国勢調査の年齢別人口のテーブル](/datasets/queria/e_stat/census/census_municipality_age_2025)にある日本人女性の同じ年齢の人口で割り、1,000人あたりの値にしました。双子は2人と数えるので、出産した女性の割合よりわずかに大きく出ます。14歳以下は15〜19歳に、50歳以上は45〜49歳に含めています。出生は2024年の1年間、人口は2025年10月1日時点で、1年あまりずれているため、女性が増えている区では値がやや小さめに出ます。国勢調査で年齢が分からない人は、その市区町村の年齢構成に合わせて各年齢に割り振りました。

```chart caption="母の年齢別の、女性1,000人あたりの出生数（2024年）"
{
  "layer": [
    {
      "data": {"name": "curve_all"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_label\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_label", "type": "nominal"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "age_label",
          "type": "nominal",
          "axis": {"title": "母の年齢", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性1,000人あたりの出生数（人）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "沖縄県", "都心3区（港・千代田・中央）"],
            "range": ["#94a3b8", "#f97316", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_okinawa"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_label\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_label", "type": "nominal"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "age_label",
          "type": "nominal",
          "axis": {"title": "母の年齢", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性1,000人あたりの出生数（人）", "grid": true}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "沖縄県", "都心3区（港・千代田・中央）"],
            "range": ["#94a3b8", "#f97316", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "curve_core"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"age_label\"]) && isValid(datum[\"rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [
          {"field": "age_label", "type": "nominal"},
          {"field": "rate", "type": "quantitative"}
        ],
        "x": {
          "field": "age_label",
          "type": "nominal",
          "axis": {"title": "母の年齢", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性1,000人あたりの出生数（人）", "grid": true}
        },
        "color": {
          "datum": "都心3区（港・千代田・中央）",
          "type": "nominal",
          "scale": {
            "domain": ["全国", "沖縄県", "都心3区（港・千代田・中央）"],
            "range": ["#94a3b8", "#f97316", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

都心3区の線は、20代では3本のうち最も低く、30〜34歳で全国（90.0人）を上回り、35〜39歳で沖縄県を追い越します。沖縄県はどの年齢でも全国より高くなっています。都心3区は、20代の値が全国より低く、30代後半と40代前半の値が全国より高くなっています。

2024年に都心3区で生まれた子ども4,640人のうち、母が35歳以上だったのは45.5%です。全国では30.3%、沖縄県では32.5%でした。15〜49歳の各年齢の値を合計すると（5歳階級なので5倍します）、都心3区は1.25で、全国の1.19をわずかに上回り、沖縄県の1.57には届きません。この値は一生のうちに産む子どもの数の目安で、都心3区は全国とほぼ同じですが、出産する年齢の分布は大きく異なります。分母に2025年の国勢調査を使っているので、この値は厚生労働省が公表する合計特殊出生率とは一致しません。

## 出生数300人以上の市区町村で、30代後半の値が最も高いのは港区、40代前半は千代田区

市区町村ごとに同じ値を出し、20代後半と30代後半で並べたのが下の図です。出生数が少ない町村は年ごとの増減で値が大きく振れるので、2024年の出生数が300人以上の600市区町村（政令指定都市は区ごと）に絞っています。

```chart caption="市区町村別の、25〜29歳と35〜39歳の女性1,000人あたりの出生数（2024年、出生数300人以上）"
{
  "layer": [
    {
      "data": {"name": "sc_other"},
      "mark": {"type": "point", "opacity": 0.5, "filled": true, "size": 36},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "r25", "type": "quantitative"},
          {"field": "r35", "type": "quantitative"}
        ],
        "x": {
          "field": "r25",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "25〜29歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "y": {
          "field": "r35",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "35〜39歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "color": {
          "datum": "その他の市区町村",
          "type": "nominal",
          "scale": {
            "domain": ["その他の市区町村", "沖縄県の市町村", "都心3区"],
            "range": ["#94a3b8", "#f97316", "#ef4444"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "sc_okinawa"},
      "mark": {"type": "point", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "r25", "type": "quantitative"},
          {"field": "r35", "type": "quantitative"}
        ],
        "x": {
          "field": "r25",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "25〜29歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "y": {
          "field": "r35",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "35〜39歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "color": {
          "datum": "沖縄県の市町村",
          "type": "nominal",
          "scale": {
            "domain": ["その他の市区町村", "沖縄県の市町村", "都心3区"],
            "range": ["#94a3b8", "#f97316", "#ef4444"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "sc_core"},
      "mark": {"type": "point", "filled": true, "size": 121},
      "encoding": {
        "tooltip": [
          {"field": "label", "type": "nominal"},
          {"field": "r25", "type": "quantitative"},
          {"field": "r35", "type": "quantitative"}
        ],
        "x": {
          "field": "r25",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "25〜29歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "y": {
          "field": "r35",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "35〜39歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "color": {
          "datum": "都心3区",
          "type": "nominal",
          "scale": {
            "domain": ["その他の市区町村", "沖縄県の市町村", "都心3区"],
            "range": ["#94a3b8", "#f97316", "#ef4444"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "sc_core"},
      "mark": {"type": "text", "align": "right", "dx": -6},
      "encoding": {
        "x": {
          "field": "r25",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "25〜29歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "y": {
          "field": "r35",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "35〜39歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "text": {"field": "label"}
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

多くの市区町村は、20代後半の値が高いほど30代後半の値も高い右上がりの帯に並びます。沖縄県の市町村は帯の右上にあり、どちらの年齢でも出産が多い地域です。都心3区は帯から離れた左上にあります。35〜39歳の値は港区が83.5人で600市区町村の中で最も高く、千代田区が79.4人で3番目、中央区が78.6人で5番目です。2番目と4番目は沖縄県の南城市と南風原町でした。港区は国勢調査で年齢が分からない日本人女性が4.6%いるので、2位の南城市との差1.2人は、その人たちの年齢の割り振り方によっては入れ替わりうる差です。都心3区の25〜29歳の値は34.8〜46.6人で、全国の64.4人を下回ります。出生は出産したときの母の住所で数えるので、出産の前に区の外へ引っ越した人の出生は区の数に入らず、転出の多い区ほど値は低めに出ます。

40〜44歳では、都心の区がさらに上位に集まります。

```chart caption="40〜44歳の女性1,000人あたりの出生数の上位15市区町村（2024年、出生数300人以上）"
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "top40"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "r40", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "r40",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "40〜44歳の女性1,000人あたりの出生数（人）", "grid": true}
        },
        "y": {"field": "label", "type": "nominal", "axis": {"title": null}, "sort": null},
        "color": {"field": "color", "scale": null, "legend": null}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

1位は千代田区の28.8人で、全国（12.4人）の2倍を超えます。上位15のうち7つは東京23区（千代田区・渋谷区・港区・中央区・目黒区・品川区・新宿区）で、名古屋市中区、大阪市中央区、さいたま市大宮区といった大都市の中心部も入ります。残りは宮古島市、読谷村、豊見城市、南城市の沖縄県の4市町村と、大分県の日田市です。渋谷区は国勢調査で年齢が分からない日本人女性が9.4%いて、それを年齢構成に合わせて割り振った値です。その人たちに40代前半が実際より多く含まれていれば、渋谷区の値はこれより低くなります。

## 勝どき駅から半径1kmに住む人の年齢構成

市区町村の値を見たあとは、開業候補地の駅の周りにどの年齢の人がどれだけ住んでいるかを確認します。下の地図は、都心3区のうち中央区の都営大江戸線勝どき駅から半径1kmの範囲です。範囲に住む人の数と年齢構成が出ます。地図をクリックすると中心が移るので、自分の候補地の駅に置き換えられます。円は隣の区にもかかるので、その住民も数に入ります。

```map
type: around
lng: 139.777153
lat: 35.658948
radius: 1000
caption: 都営大江戸線 勝どき駅から半径1km
```

## 産婦人科クリニックの開業地選びにどう使うか

- 候補地の市区町村について、母の年齢別の出生数を女性の人口で割り、30代後半と40代前半の値を全国（53.2人、12.4人）と並べる。都心3区のように全国の1.5倍から2倍ある地域では、35歳以上の妊婦の健診や出生前検査の相談に応じる体制を厚くする計画が立てやすくなります
- 出生数だけでなく、母が35歳以上の出生の割合も見る。都心3区では45.5%で、全国の30.3%を大きく上回ります。候補地の出生数にこの割合を掛けると、35歳以上で出産する人の数を見積もれます
- 不妊治療の相談を受ける婦人科を併設するかどうかを考えるときも、候補地の40〜44歳の値が全国の何倍かを材料にできます。40代前半で出産する人が多い地域ほど、その手前で治療を考える人も多いと考えられます
- 市区町村の値で候補の区を絞ったあと、駅の周りに30代・40代の女性がどれだけ住んでいるかを地図で確認する

## データの出典

本記事は厚生労働省の[人口動態統計](https://www.mhlw.go.jp/toukei/list/81-1.html)の市区町村別・母の年齢別出生数（2024年）と、総務省統計局の[令和7年国勢調査](https://www.stat.go.jp/data/kokusei/2025/index.html)の市区町村別・年齢別の日本人女性の人口（2025年10月1日現在）を、2026-11-09 時点で集計しています。

Queriaは、人口動態統計と国勢調査を、列名・単位・地域コードを統一し、テーブルと列の説明をつけて公開しています。本記事で使った[母の年齢別出生数のテーブル](/datasets/queria/e_stat/vital_statistics/births_by_mother_age)と[2025年国勢調査の年齢別人口のテーブル](/datasets/queria/e_stat/census/census_municipality_age_2025)を市区町村コードで結合すると、開業候補地の市区町村の値を同じ方法で出せます。

```sql id=curve
-- 2024年の出生数（人口動態統計）を2025年国勢調査の日本人女性で割り、全国・沖縄県・都心3区の年齢別の値を出す
WITH b AS (
  SELECT area_code AS area, area_name, prefecture_code,
    CASE
      WHEN mother_age_code = '00190' THEN 15
      WHEN mother_age_from >= 45 THEN 45
      ELSE mother_age_from
    END AS age_from,
    sum(births) AS births
  FROM e_stat.vital_statistics.births_by_mother_age
  WHERE year = 2024
    AND area_kind IN ('municipality', 'ward')
    AND mother_age_code <> '00450'
  GROUP BY ALL
), w_total AS (
  SELECT area,
    sum(population_japanese_female) AS total,
    sum(population_japanese_female) FILTER (WHERE age_from IS NOT NULL) AS known
  FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'ward', 'town_village')
  GROUP BY area
), w AS (
  SELECT c.area, c.age_from,
    c.population_japanese_female * t.total / t.known AS women
  FROM e_stat.census.census_municipality_age_2025 c
  JOIN w_total t USING (area)
  WHERE c.area_level IN ('city', 'ward', 'town_village')
    AND c.age_from BETWEEN 15 AND 45
    AND t.known > 0
), areas AS (
  SELECT DISTINCT area, area_name, prefecture_code FROM b
),
rates AS (
SELECT w.area, a.area_name, a.prefecture_code, w.age_from, w.women,
  coalesce(b.births, 0) AS births
FROM w
JOIN areas a USING (area)
LEFT JOIN b USING (area, age_from)
WHERE w.women > 0
),
grouped AS (
  SELECT
    CASE
      WHEN area IN ('13101', '13102', '13103') THEN '都心3区'
      WHEN prefecture_code = '47' THEN '沖縄県'
    END AS grp,
    age_from, births, women
  FROM rates
)
SELECT grp, age_from,
  CAST(age_from AS VARCHAR) || '〜' || CAST(age_from + 4 AS VARCHAR) || '歳' AS age_label,
  sum(births) AS births,
  round(sum(women)) AS women,
  round(1000 * sum(births) / sum(women), 1) AS rate
FROM grouped
WHERE grp IS NOT NULL
GROUP BY grp, age_from
UNION ALL
SELECT '全国' AS grp, age_from,
  CAST(age_from AS VARCHAR) || '〜' || CAST(age_from + 4 AS VARCHAR) || '歳' AS age_label,
  sum(births) AS births,
  round(sum(women)) AS women,
  round(1000 * sum(births) / sum(women), 1) AS rate
FROM rates
GROUP BY age_from
ORDER BY grp, age_from
```

```sql id=curve_all
-- 全国の年齢別の値
SELECT age_from, age_label, rate FROM curve WHERE grp = '全国' ORDER BY age_from
```

```sql id=curve_okinawa
-- 沖縄県の年齢別の値
SELECT age_from, age_label, rate FROM curve WHERE grp = '沖縄県' ORDER BY age_from
```

```sql id=curve_core
-- 都心3区（港区・千代田区・中央区）の年齢別の値
SELECT age_from, age_label, rate FROM curve WHERE grp = '都心3区' ORDER BY age_from
```

```sql id=summary
-- 出生数、母が35歳以上の出生の割合、15〜49歳の値の合計（5倍）を出す（プロットはしない）
SELECT grp,
  sum(births) AS births,
  round(100.0 * sum(births) FILTER (WHERE age_from >= 35) / sum(births), 1) AS share_35_over,
  round(5 * sum(births / women), 2) AS sum_of_rates
FROM curve
GROUP BY grp
ORDER BY grp
```

```sql id=units
-- 市区町村（政令指定都市は区）ごとの25〜29歳・35〜39歳・40〜44歳の値。2024年の出生数300人以上に絞る
WITH b AS (
  SELECT area_code AS area, area_name, prefecture_code,
    CASE
      WHEN mother_age_code = '00190' THEN 15
      WHEN mother_age_from >= 45 THEN 45
      ELSE mother_age_from
    END AS age_from,
    sum(births) AS births
  FROM e_stat.vital_statistics.births_by_mother_age
  WHERE year = 2024
    AND area_kind IN ('municipality', 'ward')
    AND mother_age_code <> '00450'
  GROUP BY ALL
), w_total AS (
  SELECT area,
    sum(population_japanese_female) AS total,
    sum(population_japanese_female) FILTER (WHERE age_from IS NOT NULL) AS known
  FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'ward', 'town_village')
  GROUP BY area
), w AS (
  SELECT c.area, c.age_from,
    c.population_japanese_female * t.total / t.known AS women
  FROM e_stat.census.census_municipality_age_2025 c
  JOIN w_total t USING (area)
  WHERE c.area_level IN ('city', 'ward', 'town_village')
    AND c.age_from BETWEEN 15 AND 45
    AND t.known > 0
), areas AS (
  SELECT DISTINCT area, area_name, prefecture_code FROM b
),
rates AS (
SELECT w.area, a.area_name, a.prefecture_code, w.age_from, w.women,
  coalesce(b.births, 0) AS births
FROM w
JOIN areas a USING (area)
LEFT JOIN b USING (area, age_from)
WHERE w.women > 0
),
names AS (
  SELECT DISTINCT area, area_name AS label
  FROM e_stat.census.census_municipality_age_2025
  WHERE area_level IN ('city', 'ward', 'town_village')
)
SELECT r.area, n.label,
  CASE
    WHEN r.area IN ('13101', '13102', '13103') THEN '都心3区'
    WHEN any_value(r.prefecture_code) = '47' THEN '沖縄県'
    ELSE 'その他'
  END AS grp,
  sum(r.births) AS births,
  round(1000 * sum(r.births) FILTER (WHERE r.age_from = 25) / sum(r.women) FILTER (WHERE r.age_from = 25), 1) AS r25,
  round(1000 * sum(r.births) FILTER (WHERE r.age_from = 35) / sum(r.women) FILTER (WHERE r.age_from = 35), 1) AS r35,
  round(1000 * sum(r.births) FILTER (WHERE r.age_from = 40) / sum(r.women) FILTER (WHERE r.age_from = 40), 1) AS r40
FROM rates r JOIN names n USING (area)
GROUP BY r.area, n.label
HAVING sum(r.births) >= 300
ORDER BY r.area
```

```sql id=sc_other
-- 散布図: 都心3区と沖縄県以外
SELECT label, r25, r35 FROM units WHERE grp = 'その他'
```

```sql id=sc_okinawa
-- 散布図: 沖縄県の市町村
SELECT label, r25, r35 FROM units WHERE grp = '沖縄県'
```

```sql id=sc_core
-- 散布図: 都心3区
SELECT label, r25, r35 FROM units WHERE grp = '都心3区'
```

```sql id=top35
-- 35〜39歳の値の上位10（プロットはしない）
SELECT ROW_NUMBER() OVER (ORDER BY r35 DESC, label) AS rn, label, grp, r35, r25
FROM units
QUALIFY rn <= 10
ORDER BY rn
```

```sql id=top40
-- 40〜44歳の値の上位15
SELECT ROW_NUMBER() OVER (ORDER BY r40 DESC, label) AS rn, label, grp, r40,
  CASE grp WHEN '都心3区' THEN '#ef4444' WHEN '沖縄県' THEN '#f97316' ELSE '#94a3b8' END AS color
FROM units
QUALIFY rn <= 15
ORDER BY rn
```

```sql id=unit_count
-- 散布図と上位の対象になった市区町村の数（プロットはしない）
SELECT count(*) AS units, sum(births) AS births FROM units
```

```sql id=unknown_age
-- 2025年国勢調査で年齢が「不詳」の日本人女性の割合（プロットはしない）
SELECT area_name,
  round(100.0 * sum(population_japanese_female) FILTER (WHERE age_from IS NULL) / sum(population_japanese_female), 1) AS unknown_pct
FROM e_stat.census.census_municipality_age_2025
WHERE area IN ('13101', '13102', '13103', '13113')
GROUP BY area_name
ORDER BY area_name
```
