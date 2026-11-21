---
title: 全国333の医療の区域の64.0%で2050年の65歳以上人口が減り、千葉県には+32.4%と−23.7%の区域がある
description: 全国333の二次医療圏で65歳以上の人数を2025年と2050年で比較すると、213区域（64.0%）で減ります。同じ千葉県に+32.4%の区域と−23.7%の区域があります。
ogDescription: 全国333の二次医療圏で65歳以上の人数を2025年と2050年で比較すると、213区域（64.0%）で減ります。
publishedAt: 2026-09-09
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 将来推計人口
  - 医療圏
  - 高齢化
  - 地域分析
datasets:
  - queria/nlftp
sources:
  - title: 国土数値情報 医療圏データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A38.html
    publisher: 国土交通省
  - title: 国土数値情報 1kmメッシュ別将来推計人口（R6国政局推計）
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html
    publisher: 国土交通省
  - title: 令和2年国勢調査
    url: https://www.stat.go.jp/data/kokusei/2020/index.html
    publisher: 総務省統計局
  - title: 日本の地域別将来推計人口（令和5(2023)年推計）
    url: https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp
    publisher: 国立社会保障・人口問題研究所
agentHint: 自分の県の二次医療圏ごとに、2025年と2050年の65歳以上人口と増減率を出して。構成市区町村ごとの内訳と、区域の総人口も一緒に見たい
socialAnnounce: |-
  全国333区域で65歳以上の人数を2050年まで数えました。

  64.0%の区域で減り、同じ千葉県に+32.4%と−23.7%が並びます。病院や介護の投資判断に。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

全国333の二次医療圏のうち213区域（64.0%）で、2050年の65歳以上人口は2025年より少なくなります。増減率は、最も減る石川県の能登北部が−46.1%、最も増える東京都の区中央部が+63.7%です。同じ千葉県の中でも、東葛南部は+32.4%、安房は−23.7%です。区域の人口が小さいほど減る区域が多く、総人口が下から5分の1の区域で65歳以上が増えるのは3.0%だけでした。

病院の建て替えや介護施設の新設は、投じた資金を回収するまでに長い年月がかかります。その間の利用者の数は、施設のある地域に住む高齢者の数で決まります。投資の判断に必要なのは全国の数ではなく、事業を営む範囲の数です。この記事では、都道府県が医療計画で定める区域を単位に、65歳以上の人数が2025年から2050年にかけてどう変わるかを集計します。

## 集計の方法と使うデータ

区域の単位には二次医療圏を使います。一般の入院医療をその中で完結させることを想定して都道府県が定める区域で、複数の市区町村で1つの区域になります。全国に335区域あり、[国土数値情報の医療圏データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A38.html)から、区域の範囲（`nlftp.medical.secondary_medical_area`）と、市区町村と区域の対応表（`nlftp.medical.medical_area_municipality`）を取得できます。区域の分け方は2020年度時点の医療計画に基づいています。

人口は、[国土数値情報の1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を市区町村単位に集計したテーブル（`nlftp.population.future_population_municipality`）を使います。元になっているのは総務省の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)と、国立社会保障・人口問題研究所の「[日本の地域別将来推計人口（令和5年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)」です。

このテーブルには次の列があります。

| 列                                                | 内容                                |
| ------------------------------------------------- | ----------------------------------- |
| `population_2020` 〜 `population_2070`            | 総人口。2020年から2070年まで5年刻み |
| `elderly_ratio_2025`                              | 2025年の65歳以上人口の割合（%）     |
| `elderly_ratio_2050`                              | 2050年の65歳以上人口の割合（%）     |
| `growth_rate_2025_2035` / `growth_rate_2025_2050` | 総人口の増減率（%）                 |

将来推計人口のテーブルは政令指定都市を行政区の単位で持っているので、たとえば千葉市は6行に分かれます。65歳以上の人数の列はないので、`population_2025 * elderly_ratio_2025 / 100` で市区町村ごとに人数を計算し、区域を構成する市区町村について合計します。高齢化率は2025年と2050年の2時点しかないので、人数を比較できるのもこの2時点です。

福島県の13市町村は、将来推計人口のテーブルで `city_code` が `07999` の1行にまとめられていて、市区町村コードで結合できません。この13市町村は相双といわきの2区域に属し、どちらの区域も構成する市町村がすべてこの1行に入っているので、区域ごとの合計を計算できません。集計の対象は、この2区域を除いた333区域です。

## 333区域のうち213区域で、65歳以上人口が減る

区域ごとに2025年と2050年の65歳以上人口を計算し、増減率の順に333区域を並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "dist_dec"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "bin_mid", "type": "quantitative"},
          {"field": "areas", "type": "quantitative"}
        ],
        "x": {
          "field": "bin_mid",
          "type": "ordinal",
          "axis": {
            "title": "65歳以上人口の増減率（2025年→2050年、%）",
            "labelAngle": 0,
            "labelOverlap": "greedy"
          },
          "sort": null
        },
        "y": {
          "field": "areas",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "区域数", "grid": true}
        },
        "color": {
          "datum": "減る区域",
          "type": "nominal",
          "scale": {"domain": ["減る区域", "増える区域"], "range": ["#94a3b8", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "dist_inc"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "bin_mid", "type": "quantitative"},
          {"field": "areas", "type": "quantitative"}
        ],
        "x": {
          "field": "bin_mid",
          "type": "ordinal",
          "axis": {
            "title": "65歳以上人口の増減率（2025年→2050年、%）",
            "labelAngle": 0,
            "labelOverlap": "greedy"
          },
          "sort": null
        },
        "y": {
          "field": "areas",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "区域数", "grid": true}
        },
        "color": {
          "datum": "増える区域",
          "type": "nominal",
          "scale": {"domain": ["減る区域", "増える区域"], "range": ["#94a3b8", "#3b82f6"]},
          "title": null
        }
      }
    }
  ]
}
```

333区域のうち213区域（64.0%）で、2050年の65歳以上人口が2025年を下回ります。増減率の中央値は−8.0%で、最も減る区域は−46.1%（石川県の能登北部）、最も増える区域は+63.7%（東京都の区中央部）でした。区域の間で110ポイント近い差があります。

333区域の合計では、65歳以上人口は+6.5%増えます。減る213区域に住む65歳以上の人は、2025年時点で全体の34.5%だからです。区域の数では3分の2が減りますが、人数では3分の1の人が住む区域です。施設はどれか1つの区域の中にあるので、全国の合計ではなく区域ごとの値で判断する必要があります。

高齢化率（総人口に占める65歳以上の割合）は、333区域のうち332区域で2050年に上がります。下がるのは東京都の島しょ（35.8%→34.9%）だけです。高齢化率はほぼすべての区域で上がりますが、高齢者の人数は3分の2の区域で減ります。

高齢化率は小数第1位までしかないので、そこから計算した人数には丸めによる誤差があります。増減率の絶対値が0.5%未満の9区域は、増えるか減るかを判定できません。また、ここでの人数は65歳以上全体です。このテーブルの年齢の区切りは65歳だけなので、入院や介護の必要度が高い75歳以上や85歳以上の人数は計算できません。

## 総人口が下から5分の1の区域で、65歳以上が増えるのは3.0%

333区域を2025年の総人口で5等分し、それぞれのグループで65歳以上人口が増える区域の割合を計算しました。

```chart
{
  "layer": [
    {
      "data": {"name": "by_size"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "up_pct", "type": "quantitative"},
          {"field": "size_label", "type": "nominal"}
        ],
        "x": {
          "field": "size_label",
          "type": "nominal",
          "axis": {"title": "区域の総人口（2025年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "up_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "65歳以上人口が増える区域の割合（%）", "grid": true}
        }
      }
    },
    {
      "data": {"name": "by_size"},
      "mark": {"type": "text", "align": "center", "dx": 0, "baseline": "bottom", "dy": -4},
      "encoding": {
        "x": {
          "field": "size_label",
          "type": "nominal",
          "axis": {"title": "区域の総人口（2025年）", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "up_pct",
          "type": "quantitative",
          "scale": {"domain": [0, 100], "zero": false, "nice": false},
          "axis": {"title": "65歳以上人口が増える区域の割合（%）", "grid": true}
        },
        "text": {"field": "up_pct"}
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

最も小さいグループ（1.75〜6.95万人）では、67区域のうち65歳以上が増えるのは3.0%の2区域だけです。グループが大きくなるごとに7.5%、17.9%と上がり、最も大きいグループ（56.86〜380.2万人）では90.9%で増えます。増減率の中央値も、最も小さいグループの−30.4%から最も大きいグループの+15.5%まで、人口が大きくなるほど高くなります。

区域の人口規模が分かれば、その区域の高齢者が増えるか減るかをおおよそ判断できます。人口の小さい区域では、高齢者の人数も減ります。区域の総人口はこのテーブルの `population_2025` を合計すれば計算できるので、投資先の候補を並べるときに最初に確認する指標になります。

## 東京都・石川県・千葉県では、県内の区域で増減率が56ポイント以上違う

同じ都道府県の中でも、区域によって増えるか減るかが逆になります。県内で最も増える区域と最も減る区域の差が大きい10県です。

```chart
{
  "height": 440,
  "layer": [
    {
      "data": {"name": "spread_hi"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "chg", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "65歳以上人口の増減率（2025年→2050年、%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "県内で最も増える区域",
          "type": "nominal",
          "scale": {"domain": ["県内で最も増える区域", "県内で最も減る区域"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "spread_hi"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "65歳以上人口の増減率（2025年→2050年、%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "text": {"field": "area_name"}
      }
    },
    {
      "data": {"name": "spread_lo"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "chg", "type": "quantitative"},
          {"field": "pref_name", "type": "nominal"}
        ],
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "65歳以上人口の増減率（2025年→2050年、%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "県内で最も減る区域",
          "type": "nominal",
          "scale": {"domain": ["県内で最も増える区域", "県内で最も減る区域"], "range": ["#3b82f6", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "spread_lo"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "chg",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "65歳以上人口の増減率（2025年→2050年、%）", "grid": true}
        },
        "y": {
          "field": "pref_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "text": {"field": "area_name"}
      }
    }
  ]
}
```

差が最も大きいのは東京都で、区中央部の+63.7%と島しょの−22.3%で86.0ポイント違います。石川県は石川中央（+15.0%）と能登北部（−46.1%）で61.1ポイント、千葉県は東葛南部（+32.4%）と安房（−23.7%）で56.1ポイントです。北海道は21区域のうち、増えるのは札幌だけで、残る20区域は減ります。

この10県はすべて、増える区域と減る区域が同じ県の中にあります。県単位の統計で高齢者が増えるか減るかを判断すると、事業を営む区域によっては逆の結論になります。

## 千葉県では、東京湾岸の区域で2〜3割増え、東部と南部の区域で1〜2割減る

千葉県の9区域です。

| 区域         | 市区町村数 | 総人口（2025年） | 65歳以上（2025年） | 65歳以上（2050年） | 増減率 |
| ------------ | ---------- | ---------------- | ------------------ | ------------------ | ------ |
| 東葛南部     | 6          | 1,813,721        | 424,195            | 561,591            | +32.4% |
| 東葛北部     | 5          | 1,422,559        | 383,325            | 468,970            | +22.3% |
| 千葉         | 6          | 991,173          | 271,165            | 329,266            | +21.4% |
| 印旛         | 9          | 703,793          | 213,905            | 231,739            | +8.3%  |
| 君津         | 4          | 321,012          | 100,650            | 102,607            | +1.9%  |
| 市原         | 1          | 259,260          | 82,704             | 80,814             | −2.3%  |
| 山武長生夷隅 | 17         | 392,364          | 151,617            | 134,655            | −11.2% |
| 香取海匝     | 7          | 243,562          | 93,871             | 74,633             | −20.5% |
| 安房         | 4          | 110,661          | 49,479             | 37,750             | −23.7% |

東京湾に面した東葛南部・東葛北部・千葉の3区域では65歳以上が2割から3割強増え、県の東部と南部の山武長生夷隅・香取海匝・安房の3区域では1割から2割強減ります。

65歳以上の人数を比較できるのは2025年と2050年だけですが、総人口は2070年まで5年ごとの値があります。2020年を100として4区域を並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "chiba_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokatsu_south\"]) ? 0 : 1",
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
          {"field": "tokatsu_south", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokatsu_south",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "総人口（2020年＝100）", "grid": true}
        },
        "color": {
          "datum": "東葛南部",
          "type": "nominal",
          "scale": {
            "domain": ["東葛南部", "千葉", "山武長生夷隅", "安房"],
            "range": ["#3b82f6", "#93c5fd", "#f97316", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "chiba_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"chiba_city\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "chiba_city", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "chiba_city",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "総人口（2020年＝100）", "grid": true}
        },
        "color": {
          "datum": "千葉",
          "type": "nominal",
          "scale": {
            "domain": ["東葛南部", "千葉", "山武長生夷隅", "安房"],
            "range": ["#3b82f6", "#93c5fd", "#f97316", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "chiba_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"sanbu\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "sanbu", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "sanbu",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "総人口（2020年＝100）", "grid": true}
        },
        "color": {
          "datum": "山武長生夷隅",
          "type": "nominal",
          "scale": {
            "domain": ["東葛南部", "千葉", "山武長生夷隅", "安房"],
            "range": ["#3b82f6", "#93c5fd", "#f97316", "#ef4444"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "chiba_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {"calculate": "isValid(datum[\"year\"]) && isValid(datum[\"awa\"]) ? 0 : 1", "as": "__gap"},
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
          {"field": "awa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "awa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "総人口（2020年＝100）", "grid": true}
        },
        "color": {
          "datum": "安房",
          "type": "nominal",
          "scale": {
            "domain": ["東葛南部", "千葉", "山武長生夷隅", "安房"],
            "range": ["#3b82f6", "#93c5fd", "#f97316", "#ef4444"]
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

東葛南部は2030年の101.3が最も高く、2070年でも90.3です。千葉は2020年から下がり続け、2070年に81.9になります。山武長生夷隅は2070年に47.2、安房は45.6で、どちらも50年で人口が半分以下になります。同じ県の中に、50年後に1割減る区域と半分以下になる区域があります。

高齢者の人数が減る区域では、総人口はそれより速く減ります。安房は総人口が2025年から2050年で3割以上減り、65歳以上は23.7%減です。人口に占める高齢者の割合は上がり続けるので、地域の中で医療・介護が必要な人の割合は大きくなり、それを支える働き手の数は減ります。

## 業務での使い方

- 投資判断の単位を統一する: 施設の商圏を市区町村ではなく区域の単位で捉え、回収期間が終わる年の65歳以上人口を最初に確認します。区域の総人口が全国で下から5分の1に入る場合、65歳以上が増える区域は3.0%です
- 県の平均で判断しない: `medical_area_municipality` で自社の施設がある市区町村の区域コードを取得し、その区域の増減率を計算してから、県内のほかの区域と比較します
- 撤退と統合の時期を逆算する: 高齢者の数が減る区域では、総人口はそれより速く減ります。人員の採用や外来の受け入れ先を、需要の大きさに加えて働き手の減り方から検討できます

## データの出典

本記事は[国土数値情報の医療圏データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A38.html)（2020年度版）と[1kmメッシュ別将来推計人口（R6国政局推計）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-mesh1000r6.html)を2026年9月9日時点で集計しています。推計の元になっているのは総務省の[令和2年国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)と、国立社会保障・人口問題研究所の「[日本の地域別将来推計人口（令和5(2023)年推計）](https://www.ipss.go.jp/pp-shicyoson/j/shicyoson23/t-page.asp)」で、2020年の国勢調査より後の出来事は推計に含まれていません。

Queria は、医療圏データと将来推計人口を、列名・単位・コード体系を統一し、各列の意味の説明を付けて公開しています。本記事で使った[市区町村と医療圏の対応表](/datasets/nlftp/medical/medical_area_municipality)と[市区町村別将来推計人口テーブル](/datasets/nlftp/population/future_population_municipality)を市区町村コードで結合すると、自社の施設がある区域の数字を確認したり、候補地の区域を並べて比較したりできます。

```sql id=coverage
SELECT COUNT(*) AS areas_total, SUM(CASE WHEN miss > 0 THEN 1 ELSE 0 END) AS areas_excluded, SUM(CASE WHEN miss = 0 THEN 1 ELSE 0 END) AS areas_used, SUM(miss) AS municipalities_missing, STRING_AGG(CASE WHEN miss > 0 THEN pn || ' ' || an || '（構成' || n_muni || '市町村のうち' || miss || '市町村が市区町村コードで引けない）' END, ' / ' ORDER BY ac) AS excluded_areas FROM (SELECT m.secondary_area_code AS ac, m.secondary_area_name AS an, m.prefecture_name AS pn, COUNT(*) AS n_muni, SUM(CASE WHEN f.city_code IS NULL THEN 1 ELSE 0 END) AS miss FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code GROUP BY 1, 2, 3)
```

```sql id=summary
WITH j AS (SELECT m.secondary_area_code AS ac, m.secondary_area_name AS an, m.prefecture_name AS pn, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, an, pn, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25) AS pop25, SUM(p50) AS pop50, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1, 2, 3) SELECT COUNT(*) AS areas, SUM(CASE WHEN old50 < old25 THEN 1 ELSE 0 END) AS decreasing, ROUND(CAST(SUM(CASE WHEN old50 < old25 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS decreasing_pct, ROUND(MEDIAN(old50 / old25 * 100 - 100), 1) AS median_chg, ROUND(MIN(old50 / old25 * 100 - 100), 1) AS min_chg, ROUND(MAX(old50 / old25 * 100 - 100), 1) AS max_chg, ROUND(SUM(old50) / SUM(old25) * 100 - 100, 1) AS national_chg, ROUND(SUM(CASE WHEN old50 < old25 THEN old25 ELSE 0 END) * 100 / SUM(old25), 1) AS elderly_share_decreasing, SUM(CASE WHEN old50 / pop50 > old25 / pop25 THEN 1 ELSE 0 END) AS ratio_up, SUM(CASE WHEN ABS(old50 / old25 * 100 - 100) < 0.5 THEN 1 ELSE 0 END) AS near_zero_areas FROM a WHERE miss = 0
```

```sql id=dist_dec
WITH j AS (SELECT m.secondary_area_code AS ac, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1) SELECT CAST(FLOOR((old50 / old25 * 100 - 100) / 10) * 10 + 5 AS INTEGER) AS bin_mid, COUNT(*) AS areas FROM a WHERE miss = 0 AND old50 < old25 GROUP BY 1 ORDER BY 1
```

```sql id=dist_inc
WITH j AS (SELECT m.secondary_area_code AS ac, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1) SELECT CAST(FLOOR((old50 / old25 * 100 - 100) / 10) * 10 + 5 AS INTEGER) AS bin_mid, COUNT(*) AS areas FROM a WHERE miss = 0 AND old50 >= old25 GROUP BY 1 ORDER BY 1
```

```sql id=by_size
WITH j AS (SELECT m.secondary_area_code AS ac, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25) AS pop25, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1), q AS (SELECT pop25, old50 / old25 * 100 - 100 AS chg, NTILE(5) OVER (ORDER BY pop25) AS band FROM a WHERE miss = 0) SELECT band, ROUND(MIN(pop25) / 10000, 2) || '〜' || ROUND(MAX(pop25) / 10000, 2) || '万人' AS size_label, COUNT(*) AS areas, ROUND(CAST(SUM(CASE WHEN chg > 0 THEN 1 ELSE 0 END) AS DOUBLE) * 100 / COUNT(*), 1) AS up_pct, ROUND(MEDIAN(chg), 1) AS median_chg FROM q GROUP BY 1 ORDER BY 1
```

```sql id=spread_hi
WITH j AS (SELECT m.secondary_area_code AS ac, m.secondary_area_name AS an, m.prefecture_name AS pn, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, an, pn, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1, 2, 3), c AS (SELECT pn, an, old50 / old25 * 100 - 100 AS chg FROM a WHERE miss = 0), s AS (SELECT pn, MAX(chg) AS hi, MIN(chg) AS lo, COUNT(*) AS areas, SUM(CASE WHEN chg > 0 THEN 1 ELSE 0 END) AS up_areas, SUM(CASE WHEN chg <= 0 THEN 1 ELSE 0 END) AS down_areas, ROW_NUMBER() OVER (ORDER BY MAX(chg) - MIN(chg) DESC, pn) AS rn FROM c GROUP BY 1 HAVING COUNT(*) >= 2) SELECT s.pn AS pref_name, ROUND(s.hi, 1) AS chg, MIN(h.an) AS area_name, s.areas, s.up_areas, s.down_areas FROM s JOIN c h ON h.pn = s.pn AND h.chg = s.hi WHERE s.rn <= 10 GROUP BY s.rn, s.pn, s.hi, s.areas, s.up_areas, s.down_areas ORDER BY s.rn
```

```sql id=spread_lo
WITH j AS (SELECT m.secondary_area_code AS ac, m.secondary_area_name AS an, m.prefecture_name AS pn, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, an, pn, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1, 2, 3), c AS (SELECT pn, an, old50 / old25 * 100 - 100 AS chg FROM a WHERE miss = 0), s AS (SELECT pn, MAX(chg) AS hi, MIN(chg) AS lo, ROW_NUMBER() OVER (ORDER BY MAX(chg) - MIN(chg) DESC, pn) AS rn FROM c GROUP BY 1 HAVING COUNT(*) >= 2) SELECT s.pn AS pref_name, ROUND(s.lo, 1) AS chg, MIN(l.an) AS area_name FROM s JOIN c l ON l.pn = s.pn AND l.chg = s.lo WHERE s.rn <= 10 GROUP BY s.rn, s.pn, s.lo ORDER BY s.rn
```

```sql id=chiba
WITH j AS (SELECT m.secondary_area_name AS an, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code WHERE m.prefecture_code = '12'), a AS (SELECT an, COUNT(*) AS municipalities, SUM(p25) AS pop25, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1) SELECT an AS area_name, municipalities, CAST(ROUND(pop25) AS BIGINT) AS pop_2025, CAST(ROUND(old25) AS BIGINT) AS elderly_2025, CAST(ROUND(old50) AS BIGINT) AS elderly_2050, ROUND(old50 / old25 * 100 - 100, 1) AS chg FROM a ORDER BY chg
```

```sql id=chiba_trend
WITH j AS (SELECT m.secondary_area_name AS an, f.population_2020 AS p2020, f.population_2025 AS p2025, f.population_2030 AS p2030, f.population_2035 AS p2035, f.population_2040 AS p2040, f.population_2045 AS p2045, f.population_2050 AS p2050, f.population_2055 AS p2055, f.population_2060 AS p2060, f.population_2065 AS p2065, f.population_2070 AS p2070 FROM nlftp.medical.medical_area_municipality m JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code WHERE m.prefecture_code = '12' AND m.secondary_area_name IN ('東葛南部', '千葉', '山武長生夷隅', '安房')), g AS (SELECT an, SUM(p2020) AS y2020, SUM(p2025) AS y2025, SUM(p2030) AS y2030, SUM(p2035) AS y2035, SUM(p2040) AS y2040, SUM(p2045) AS y2045, SUM(p2050) AS y2050, SUM(p2055) AS y2055, SUM(p2060) AS y2060, SUM(p2065) AS y2065, SUM(p2070) AS y2070 FROM j GROUP BY 1), u AS (UNPIVOT g ON y2020, y2025, y2030, y2035, y2040, y2045, y2050, y2055, y2060, y2065, y2070 INTO NAME yr VALUE pop), w AS (SELECT an, CAST(REPLACE(yr, 'y', '') AS INTEGER) AS year, pop, FIRST_VALUE(pop) OVER (PARTITION BY an ORDER BY CAST(REPLACE(yr, 'y', '') AS INTEGER)) AS base FROM u) SELECT year, ROUND(MAX(CASE WHEN an = '東葛南部' THEN pop / base * 100 END), 1) AS tokatsu_south, ROUND(MAX(CASE WHEN an = '千葉' THEN pop / base * 100 END), 1) AS chiba_city, ROUND(MAX(CASE WHEN an = '山武長生夷隅' THEN pop / base * 100 END), 1) AS sanbu, ROUND(MAX(CASE WHEN an = '安房' THEN pop / base * 100 END), 1) AS awa FROM w GROUP BY 1 ORDER BY 1
```

```sql id=ratio_down
WITH j AS (SELECT m.secondary_area_code AS ac, m.secondary_area_name AS an, m.prefecture_name AS pn, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, an, pn, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25) AS pop25, SUM(p50) AS pop50, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1, 2, 3) SELECT pn AS pref_name, an AS area_name, ROUND(old25 / pop25 * 100, 1) AS elderly_ratio_2025, ROUND(old50 / pop50 * 100, 1) AS elderly_ratio_2050 FROM a WHERE miss = 0 AND old50 / pop50 <= old25 / pop25 ORDER BY 1, 2
```

```sql id=extremes
WITH j AS (SELECT m.secondary_area_code AS ac, m.secondary_area_name AS an, m.prefecture_name AS pn, f.city_code AS cc, f.population_2025 AS p25, f.population_2050 AS p50, f.elderly_ratio_2025 AS e25, f.elderly_ratio_2050 AS e50 FROM nlftp.medical.medical_area_municipality m LEFT JOIN nlftp.population.future_population_municipality f ON f.city_code = m.admin_code), a AS (SELECT ac, an, pn, SUM(CASE WHEN cc IS NULL THEN 1 ELSE 0 END) AS miss, SUM(p25) AS pop25, SUM(p25 * e25 / 100) AS old25, SUM(p50 * e50 / 100) AS old50 FROM j GROUP BY 1, 2, 3), r AS (SELECT pn, an, CAST(ROUND(pop25) AS BIGINT) AS pop_2025, ROUND(old50 / old25 * 100 - 100, 1) AS chg, RANK() OVER (ORDER BY old50 / old25 DESC) AS rank_top, RANK() OVER (ORDER BY old50 / old25) AS rank_bottom FROM a WHERE miss = 0) SELECT pn AS pref_name, an AS area_name, pop_2025, chg, rank_top, rank_bottom FROM r WHERE rank_top <= 5 OR rank_bottom <= 5 ORDER BY chg DESC
```
