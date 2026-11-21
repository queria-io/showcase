---
title: 横浜市からは60代が出ていき、80歳以上は入ってきます。60代は転出超過で80歳以上は転入超過の市が、政令市20市のうち7市あります
description: 2014〜2025年の転入超過を年齢別に集計すると、横浜市は60代で1万3,683人の転出超過、80歳以上で4,561人の転入超過です。政令市20市の合計でも80歳以上は4万6,693人の転入超過ですが、東京23区は60代も80歳以上も転出超過です。
publishedAt: 2026-10-31
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口移動
  - 高齢者
  - 高齢者住宅
  - 介護
datasets:
  - queria/e_stat
  - queria/soumu
sources:
  - title: 住民基本台帳人口移動報告
    url: https://www.stat.go.jp/data/idou/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
agentHint: 政令市以外の市町村ごとに、75〜79歳・80〜84歳・85〜89歳・90歳以上の転入超過数（日本人移動者）を2014年から2025年まで合計して、80歳以上人口あたりの多い順に都道府県別で出して
socialAnnounce: |-
  2014〜2025年の転入超過を年齢別に数えると、横浜市は60代で1万3,683人の転出超過、80歳以上では4,561人の転入超過でした。東京23区は60代も80歳以上も転出超過です。

  高齢者住宅の立地や介護需要の見通しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

横浜市では、2014年から2025年までの12年間に、60代は転出した人が転入した人を1万3,683人上回り、80歳以上は転入した人が転出した人を4,561人上回りました。政令指定都市20市の合計でも、60代は1万2,543人の転出超過、80歳以上は4万6,693人の転入超過です。60代が転出超過で80歳以上が転入超過の政令市は、20市のうち7市あります。東京23区と、大阪市・京都市・神戸市・北九州市では、80歳以上も転出超過です。

高齢者の引っ越しには、仕事を退いたあとに都市を離れて海や山の近くへ移るものと、体が弱ってから子どもの住む街や施設のある街へ移るものがあるとよく言われます。この記事では、住民票の移動を年齢別に集計し、それぞれの年齢の人がどの市町村に移っているかを確認しました。高齢者向け住宅や介護施設の立地を検討する方に向けた内容です。

## 政令市の合計では、70代で転出超過から転入超過に変わる

使ったのは総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)の市区町村別・年齢5歳階級別の表で、e-Stat の `municipality_migration_age` に収録されています。住民票の異動届にもとづく実績で、1月から12月までの1年間に市区町村をまたいで住所を移した人を、移った時点の年齢で集計しています。年齢は0〜4歳から85〜89歳までの5歳刻みと90歳以上の19区分です。2014年から続いているのは日本人の移動だけなので、すべて日本人移動者（`61000`）の値を使います。

ここでは、転入者数から転出者数を引いた転入超過数を12年分合計し、全国の市区町村を東京23区、政令指定都市20市、それ以外の市町村の3つに分けました。東京23区は原典で1つの単位（特別区部）として扱われ、政令市も市全体で1つの単位なので、23区の中や同じ政令市の中で区をまたいだ引っ越しは集計に含まれません。転入超過は転入した人と転出した人の差で、転入した人数ではありません。

```chart caption="年齢別の転入超過数（日本人移動者、2014〜2025年の合計、50歳以上）"
{
  "layer": [
    {
      "data": {"name": "prof_city"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"age\"]) && isValid(datum[\"net\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [{"field": "age", "type": "nominal"}, {"field": "net", "type": "quantitative"}],
        "x": {
          "field": "age",
          "type": "nominal",
          "axis": {"title": "移った時点の年齢", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "net",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人、12年の合計）", "grid": true}
        },
        "color": {
          "datum": "政令指定都市（20市）",
          "type": "nominal",
          "scale": {
            "domain": ["政令指定都市（20市）", "それ以外の市町村", "東京23区"],
            "range": ["#3b82f6", "#22c55e", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "prof_other"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"age\"]) && isValid(datum[\"net\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [{"field": "age", "type": "nominal"}, {"field": "net", "type": "quantitative"}],
        "x": {
          "field": "age",
          "type": "nominal",
          "axis": {"title": "移った時点の年齢", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "net",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人、12年の合計）", "grid": true}
        },
        "color": {
          "datum": "それ以外の市町村",
          "type": "nominal",
          "scale": {
            "domain": ["政令指定都市（20市）", "それ以外の市町村", "東京23区"],
            "range": ["#3b82f6", "#22c55e", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "prof_tokyo"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"age\"]) && isValid(datum[\"net\"]) ? 0 : 1", "as": "__gap"},
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 49}
      },
      "encoding": {
        "tooltip": [{"field": "age", "type": "nominal"}, {"field": "net", "type": "quantitative"}],
        "x": {
          "field": "age",
          "type": "nominal",
          "axis": {"title": "移った時点の年齢", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "net",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人、12年の合計）", "grid": true}
        },
        "color": {
          "datum": "東京23区",
          "type": "nominal",
          "scale": {
            "domain": ["政令指定都市（20市）", "それ以外の市町村", "東京23区"],
            "range": ["#3b82f6", "#22c55e", "#94a3b8"]
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

政令市以外の市町村では、50代から70代まで転入が転出を上回り、60〜64歳の4万4,646人が最も多くなっています。60代（60〜69歳）の12年間の転入超過は7万8,271人です。70代で転入超過は少なくなり、80歳以上では9,603人の転出超過になります。政令市では、60代は1万2,543人の転出超過ですが、70〜74歳で転入超過になり、80〜84歳の1万7,881人が最も多くなります。

東京23区は、50歳以上のすべての年齢で転出超過です。60代は6万5,739人、80歳以上は3万7,102人の転出超過でした。23区の60代の転出超過は、政令市以外の市町村の60代の転入超過と近い規模です。この表には転出先が記録されていないので、23区を出た人がどの市町村に転入したかは判定できません。

## 60代が転出超過で80歳以上が転入超過の政令市は、横浜市・川崎市・広島市など7市

60代と80歳以上の12年間の転入超過数を、政令市ごとに並べました。

```chart caption="政令指定都市の転入超過数（日本人移動者、2014〜2025年の合計）"
{
  "height": 640,
  "layer": [
    {
      "data": {"name": "cities"},
      "transform": [
        {"fold": ["n6069", "n80"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"n6069\": \"60代（60〜69歳）\", \"n80\": \"80歳以上\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"n6069\",\"n80\"], datum.__series)", "as": "__order"}
      ],
      "mark": {"type": "bar"},
      "encoding": {
        "y": {
          "field": "city",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "x": {
          "field": "__value",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "転入超過数（人、12年の合計）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["60代（60〜69歳）", "80歳以上"], "range": ["#93c5fd", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__order", "type": "quantitative"},
        "yOffset": {"field": "__name", "sort": ["80歳以上", "60代（60〜69歳）"]},
        "tooltip": [
          {"field": "city", "type": "nominal"},
          {"field": "__name", "type": "nominal", "title": "系列"},
          {"field": "__value", "type": "quantitative", "title": "値"}
        ]
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

20市のうち16市で、80歳以上は転入超過です。60代は転出超過で80歳以上は転入超過の市は、さいたま市・横浜市・川崎市・仙台市・広島市・名古屋市・堺市の7市です。横浜市は60代の1万3,683人の転出超過から80歳以上の4,561人の転入超過へ、川崎市は8,042人の転出超過から3,067人の転入超過へ、広島市は2,796人の転出超過から2,801人の転入超過へ変わります。さいたま市も、60代は2,475人の転出超過、80歳以上は5,665人の転入超過です。

7市の人口の違いの影響を除くため、12年間の転入超過数を1年あたりに換算し、その年齢の住民1,000人あたりの人数にしました（住民の数の出典は後の節で説明します）。80歳以上の転入超過が人口あたりで最も多いのはさいたま市で、80歳以上1,000人あたり年に5.05人です。7市で80歳以上の住民が最も多い横浜市は、人口あたりでは1.30人です。

```sql
SELECT name AS "市", r60 AS "60代（1,000人あたり/年）", r80 AS "80歳以上（1,000人あたり/年）" FROM flip_rates ORDER BY r80 DESC, name
```

札幌市は60代でも1万844人の転入超過で、80歳以上はさらに多い1万5,517人です。80歳以上の転入超過は、政令市の中で札幌市が特に多くなっています。80歳以上が転出超過になったのは、京都市・神戸市・大阪市・北九州市の4市でした。

政令市の80歳以上の転入超過4万6,693人のうち、首都圏の5市（さいたま市・横浜市・相模原市・千葉市・川崎市）の合計は2万408人で、43.7%を占めます。同じ12年間に、東京23区の80歳以上は3万7,102人の転出超過です。

## 23区の60代の転出超過と、政令市の80歳以上の転入超過は、2025年に12年間で最も多くなった

東京23区の60代の転出超過、政令市以外の市町村の60代の転入超過、政令市の80歳以上の転入超過の年ごとの推移です。いずれも2014年より2025年のほうが多くなっています。

```chart caption="転入超過数の推移（日本人移動者、2014〜2025年）"
{
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"other_60s\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "other_60s", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "other_60s",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "政令市以外の市町村・60代",
          "type": "nominal",
          "scale": {
            "domain": ["政令市以外の市町村・60代", "政令市・80歳以上", "東京23区・60代"],
            "range": ["#22c55e", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"city_80plus\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "city_80plus", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "city_80plus",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "政令市・80歳以上",
          "type": "nominal",
          "scale": {
            "domain": ["政令市以外の市町村・60代", "政令市・80歳以上", "東京23区・60代"],
            "range": ["#22c55e", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo_60s\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tokyo_60s", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokyo_60s",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "東京23区・60代",
          "type": "nominal",
          "scale": {
            "domain": ["政令市以外の市町村・60代", "政令市・80歳以上", "東京23区・60代"],
            "range": ["#22c55e", "#3b82f6", "#94a3b8"]
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

東京23区の60代の転出超過は、2014年の4,283人から2025年は7,020人になり、12年間で最も多くなりました。政令市以外の市町村の60代の転入超過は、2014年の4,960人から2021年に8,462人まで増え、2025年は8,091人です。政令市の80歳以上の転入超過は、2014年の2,929人から2025年は4,878人で、12年間で最も多い年です。2020年は3,284人で、前年の4,830人から一度減っています。

## 60代の転入超過が人口あたりで最も多い伊東市と熱海市では、80歳以上は転出超過

市町村ごとに、12年間の転入超過数を1年あたりに換算し、その年齢の住民1,000人あたりの人数にしました。住民の数は、e-Stat の社会・人口統計体系の市区町村別人口（`a_municipal_population`）の2020年の国勢調査の値です。60代の人数は60歳以上人口（`A1416`）から70歳以上人口（`A1417`）を引いて算出し、80歳以上は80歳以上人口（`A1418`）を使います。分母は2020年の1時点に固定しているので、12年間の平均の目安です。

下の図は、80歳以上の住民が5,000人以上いる市町村を、横軸に60代、縦軸に80歳以上の転入超過を取って並べたものです。右下にあるのは、60代は転入超過で80歳以上は転出超過の市町村です。

```chart caption="住民1,000人あたりの年間転入超過数（日本人移動者、2014〜2025年の平均、80歳以上人口5,000人以上の市町村）"
{
  "layer": [
    {
      "data": {"name": "scatter"},
      "mark": {"type": "point", "color": "#3b82f6", "opacity": 0.55, "filled": true, "size": 36},
      "encoding": {
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "r60", "type": "quantitative"},
          {"field": "r80", "type": "quantitative"}
        ],
        "x": {
          "field": "r60",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "60代の住民1,000人あたり（人/年）", "grid": true}
        },
        "y": {
          "field": "r80",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "80歳以上の住民1,000人あたり（人/年）", "grid": true}
        }
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

60代の住民が3,000人以上いる市町村で、60代の転入超過が人口あたりで最も多いのは伊東市で、60代1,000人あたり年に19.1人です。2位の熱海市は15.75人です。どちらも80歳以上では転出超過で、伊東市は1,000人あたり年に0.25人、熱海市は0.32人です。12年間の合計では、伊東市の80歳以上は26人、熱海市は23人の転出超過で、転入と転出がほぼ同じです。60代の転入超過が人口あたりで多い上位10市町村のうち、80歳以上が転入超過なのは北杜市・湯河原町・那須町・八重瀬町・南城市の5つで、伊東市・熱海市・館山市・国東市・いすみ市の5つは80歳以上が転出超過です。80歳以上の住民1,000人あたりでは、八重瀬町の年8.73人の転入超過から国東市の年3.84人の転出超過まで分かれます。60代が多く転入する市町村でも、80歳以上の転入が多いとは限りません。

```sql
SELECT name AS "市町村", r60 AS "60代（1,000人あたり/年）", r80 AS "80歳以上（1,000人あたり/年）" FROM resort ORDER BY rn
```

## 高齢者住宅の候補地を選ぶときの使い方

- 有料老人ホームやサービス付き高齢者向け住宅の入居者を見込むときは、候補の市の80歳以上の住民の数に加えて、80歳以上の転入超過を80歳以上の住民1,000人あたりに換算した値を比較できます。80歳以上の住民が2万人以上いる市では、札幌市の年7.79人が最も多い値です。値が高い市では、80歳以上の住民が市の外からの転入で増えています。既存の施設に入居して住民票を移した人もこの値に含まれるので、施設が多い市ほど値が高くなることがあります。候補の市の値が高いときは、その市の既存の施設の数と並べて、入居の需要が満たされていないかを確認する必要があります。政令市は市全体で1つの値なので、区や地区の単位で候補地を選ぶには、この値だけでは判断できません
- 60代が転出超過の市でも、入居者になる80歳以上の転入が少ないとは限りません。横浜市や川崎市のように、80歳以上では転入超過の市があります。伊東市や熱海市のように60代の転入が多い市でも、80歳以上の転入超過はほぼゼロです。60代と80歳以上を分けて確認する必要があります

## データの出典

本記事は総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/index.html)の市区町村別・年齢5歳階級別の転入・転出者数（日本人移動者、2014〜2025年）と、総務省統計局の[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)の市区町村別人口（2020年の国勢調査の値）を、2026-10-31 時点で集計しています。

Queria は、総務省統計局の人口移動の統計を、列名と地域コードを統一したテーブルにし、各列の意味をメタデータに記載して公開しています。本記事で使った[年齢別の人口移動テーブル](/datasets/queria/e_stat/migration/municipality_migration_age)と[市区町村別の人口テーブル](/datasets/queria/e_stat/ssds/a_municipal_population)から、候補地の市町村の80歳以上の転入超過の推移を確認できます。

```sql id=moves
-- 市区町村×年齢（50歳以上）の12年合計。政令市は市全体、東京23区は特別区部（13100）の1行
-- 期間中に町から市になって地域コードが変わった富谷市（2016年）と那珂川市（2018年）は新しいコードにまとめる
WITH g AS (
  SELECT
    CASE area WHEN '04423' THEN '04216' WHEN '40305' THEN '40231' ELSE area END AS area,
    CASE area WHEN '04423' THEN '富谷市' WHEN '40305' THEN '那珂川市' ELSE area_name END AS area_name,
    age_code, age, net_inflow
  FROM e_stat.migration.municipality_migration_age
  WHERE area_level = 'municipality' AND sex_code = '0' AND nationality_code = '61000'
    AND year BETWEEN 2014 AND 2025 AND age_code >= '211'
)
SELECT g.area, g.area_name, g.age_code, g.age,
  CASE WHEN c.area_kind = 'designated_city' THEN 'city'
       WHEN g.area = '13100' THEN 'tokyo'
       ELSE 'other' END AS kind,
  SUM(g.net_inflow) AS net
FROM g
LEFT JOIN soumu.code.municipality c ON c.area_code = g.area
GROUP BY ALL
```

```sql id=prof_city
SELECT age, SUM(net) AS net FROM moves
WHERE kind = 'city'
GROUP BY age_code, age ORDER BY age_code
```

```sql id=prof_other
SELECT age, SUM(net) AS net FROM moves
WHERE kind = 'other'
GROUP BY age_code, age ORDER BY age_code
```

```sql id=prof_tokyo
SELECT age, SUM(net) AS net FROM moves
WHERE kind = 'tokyo'
GROUP BY age_code, age ORDER BY age_code
```

```sql id=summary
-- 本文の60代・80歳以上の合計の裏付け（プロットはしない）
SELECT kind, COUNT(DISTINCT area) AS units,
  SUM(net) FILTER (WHERE age_code IN ('213', '214')) AS n6069,
  SUM(net) FILTER (WHERE age_code IN ('217', '218', '402')) AS n80
FROM moves GROUP BY kind ORDER BY kind
```

```sql id=cities
SELECT area_name AS city,
  SUM(net) FILTER (WHERE age_code IN ('213', '214')) AS n6069,
  SUM(net) FILTER (WHERE age_code IN ('217', '218', '402')) AS n80
FROM moves WHERE kind = 'city'
GROUP BY area_name ORDER BY n80 DESC, city
```

```sql id=concentration
-- 本文の「首都圏5市で43.7%」と「7市」の裏付け（プロットはしない）
SELECT SUM(n80) FILTER (WHERE city IN ('さいたま市', '横浜市', '相模原市', '千葉市', '川崎市')) AS tokyo_area5_n80,
  SUM(n80) AS city_n80,
  ROUND(SUM(n80) FILTER (WHERE city IN ('さいたま市', '横浜市', '相模原市', '千葉市', '川崎市')) * 100.0 / SUM(n80), 1) AS share_pct,
  COUNT(*) FILTER (WHERE n6069 < 0 AND n80 > 0) AS flip_cities
FROM cities
```

```sql id=trend
SELECT g.year,
  SUM(g.net_inflow) FILTER (WHERE g.area = '13100' AND g.age_code IN ('213', '214')) AS tokyo_60s,
  SUM(g.net_inflow) FILTER (WHERE c.area_kind IS DISTINCT FROM 'designated_city' AND g.area <> '13100' AND g.age_code IN ('213', '214')) AS other_60s,
  SUM(g.net_inflow) FILTER (WHERE c.area_kind = 'designated_city' AND g.age_code IN ('217', '218', '402')) AS city_80plus
FROM e_stat.migration.municipality_migration_age g
LEFT JOIN soumu.code.municipality c ON c.area_code = g.area
WHERE g.area_level = 'municipality' AND g.sex_code = '0' AND g.nationality_code = '61000'
  AND g.year BETWEEN 2014 AND 2025
GROUP BY g.year ORDER BY g.year
```

```sql id=rates
-- 12年合計を年あたりにし、2020年国勢調査のその年齢の人口1,000人あたりにした値
WITH p AS (
  SELECT area,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1416')
      - MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1417') AS p6069,
    MAX(TRY_CAST(value AS DOUBLE)) FILTER (WHERE cat01 = 'A1418') AS p80
  FROM e_stat.ssds.a_municipal_population
  WHERE year = 2020 AND cat01 IN ('A1416', 'A1417', 'A1418')
  GROUP BY area
), m AS (
  SELECT area, area_name AS name,
    SUM(net) FILTER (WHERE age_code IN ('213', '214')) AS n6069,
    SUM(net) FILTER (WHERE age_code IN ('217', '218', '402')) AS n80
  FROM moves WHERE kind <> 'tokyo'
  GROUP BY area, area_name
)
SELECT m.area, m.name, m.n6069, m.n80, p.p6069, p.p80,
  ROUND(m.n6069 / 12.0 / p.p6069 * 1000, 2) AS r60,
  ROUND(m.n80 / 12.0 / p.p80 * 1000, 2) AS r80
FROM m JOIN p USING (area)
```

```sql id=flip_rates
-- 60代は転出超過・80歳以上は転入超過の政令市
SELECT r.name, r.p80, r.r60, r.r80
FROM rates r JOIN cities c ON c.city = r.name
WHERE c.n6069 < 0 AND c.n80 > 0
```

```sql id=scatter
SELECT name, r60, r80 FROM rates WHERE p80 >= 5000 ORDER BY area
```

```sql id=resort
-- 60代の住民3,000人以上で、60代の転入超過が人口あたりで多い10市町村
SELECT name, n80, r60, r80, ROW_NUMBER() OVER (ORDER BY r60 DESC, name) AS rn
FROM rates WHERE p6069 >= 3000
QUALIFY rn <= 10
ORDER BY rn
```

```sql id=big80
-- 本文の札幌市の値の裏付け（プロットはしない）。80歳以上の住民2万人以上で80歳以上の転入超過が人口あたりで多い順
SELECT name, r80, RANK() OVER (ORDER BY r80 DESC) AS rnk
FROM rates WHERE p80 >= 20000
QUALIFY rnk <= 5
ORDER BY rnk, name
```
