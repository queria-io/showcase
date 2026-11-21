---
title: 女性の有業率が男性の水準からの予想を45年ずっと上回る県は11、下回る道県は10ある
description: 就業構造基本調査の45年分で、都道府県の女性の有業率を集計しました。2022年は東京都の59.0%が最も高く、奈良県の47.3%が最も低い値です。女性の有業率は男性の有業率と0.802の相関があり、男性の水準から予想される値を11回の調査すべてで上回ったのは11県、すべてで下回ったのは10道県です。
publishedAt: 2026-03-08
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 労働
  - 女性就業
  - 地域格差
datasets:
  - queria/e_stat
sources:
  - title: 令和4年就業構造基本調査
    url: https://www.stat.go.jp/data/shugyou/2022/index.html
    publisher: 総務省統計局
  - title: 人口推計 2022年10月1日現在
    url: https://www.stat.go.jp/data/jinsui/2022np/index.html
    publisher: 総務省統計局
  - title: 社会・人口統計体系
    url: https://www.e-stat.go.jp/regional-statistics/ssdsview
    publisher: 総務省統計局
agentHint: e_stat.ssds.f_municipal_labor で2000年から2020年までの市区町村別の女性の就業者比率を出して。分子は就業者数（女）F110202、分母は労働力人口（女）F110102 と非労働力人口（女）F110802 の合計。これは国勢調査ベースなので有業率とは数え方が違う点に注意して。同じ分母で男性の比率も出し、各年で女性を男性に回帰した残差を市区町村ごとに求めて、石川県と高知県の市町村が都道府県と同じようにプラス側に居続けているか、県内でもばらつくのかを調べて
socialAnnounce: |-
  女性の有業率は、その地域の男性の有業率とよく連動します。

  その予想を45年ずっと上回る県が11、ずっと下回る道県が10。半分近くは同じ側から動いていません。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

[総務省の就業構造基本調査](https://www.stat.go.jp/data/shugyou/2022/index.html)で2022年の女性の有業率を47都道府県で比較すると、最も高いのは東京都の59.0%、最も低いのは奈良県の47.3%でした。女性の有業率は男性の有業率と0.802の相関があり、男性の水準から予想される値との差で並べ直すと、東京都は12位に下がり、沖縄県・高知県・石川県が上位に来ます。1977年からの11回の調査すべてで予想を上回ったのは11県、すべてで下回ったのは10道県です。

働く女性の割合は地方のほうが高い、共働きが多い北陸で高い、といった説明がよくされます。この記事では、男性の有業率と年齢構成を考慮したうえで、都道府県の差を比較します。

## 全国の男女差は45年で35.0ポイントから15.9ポイントへ

有業率は、15歳以上人口に占める有業者の割合です。有業者は、ふだん収入を得る仕事をしている人を指します。調査期間中の実際の就業で判定する[国勢調査](https://www.stat.go.jp/data/kokusei/2020/index.html)や[労働力調査](https://www.stat.go.jp/data/roudou/index.html)の「就業率」とは集計方法が違うので、水準をそのまま並べることはできません。就業構造基本調査は分子（有業者数）と分母（15歳以上人口）の両方を同じ調査で集めているので、有業者数を15歳以上人口で割って求めます。

このデータは [e-Stat「社会・人口統計体系」](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別労働データ（`f_pref_labor`）から取得しています。就業構造基本調査に由来する指標は、男女別に次の4つが収録されています。単位はいずれも千人です。

| コード  | 内容                                       |
| ------- | ------------------------------------------ |
| F120101 | 15歳以上人口（男）（就業構造基本調査結果） |
| F120102 | 15歳以上人口（女）（就業構造基本調査結果） |
| F120201 | 有業者数（男）                             |
| F120202 | 有業者数（女）                             |

収録は1977年から2022年までの11回分で、1982年以降は5年ごとの調査です。全国の推移は次のとおりです。

```chart
{
  "layer": [
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"female_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "female_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "female_rate",
          "type": "quantitative",
          "scale": {"domain": [40, 85], "zero": false, "nice": false},
          "axis": {"title": "有業率（%）", "grid": true}
        },
        "color": {
          "datum": "女性",
          "type": "nominal",
          "scale": {"domain": ["女性", "男性"], "range": ["#ec4899", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"male_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "male_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "male_rate",
          "type": "quantitative",
          "scale": {"domain": [40, 85], "zero": false, "nice": false},
          "axis": {"title": "有業率（%）", "grid": true}
        },
        "color": {
          "datum": "男性",
          "type": "nominal",
          "scale": {"domain": ["女性", "男性"], "range": ["#ec4899", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

女性の有業率は1977年の45.3%から2022年の53.2%へ7.9ポイント上がりました。途中で、1992年の51.0%から2002年の47.9%へ3.1ポイント下がったあと、2022年に11回の調査で最も高い値まで戻しています。男性は80.3%から69.1%へ11.2ポイント下がりました。男女差は35.0ポイントから15.9ポイントに縮み、2回目の1979年以降は毎回、前回の調査より小さくなっています。

差が19.1ポイント縮んだうち、11.2ポイントは男性側の低下です。有業率の分母は15歳以上人口全体で、この45年に全国の15歳以上人口に占める65歳以上の割合は11.1%から32.8%へ上がりました。男性の低下にはこの影響が含まれるので、差の縮小を「女性が働くようになった分」だけで説明することはできません。

## 2022年は東京都が59.0%で最も高く、奈良県が47.3%で最も低い

```chart
{
  "height": 780,
  "layer": [
    {
      "data": {"name": "f_rank"},
      "mark": {"type": "bar", "color": "#ec4899"},
      "encoding": {
        "tooltip": [
          {"field": "female_rate", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "female_rate",
          "type": "quantitative",
          "scale": {"domain": [45, 61], "zero": false, "nice": false},
          "axis": {"title": "女性の有業率（%）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

1位の東京都59.0%は、2位の福井県56.5%を2.5ポイント引き離しています。3位は滋賀県55.1%、4位は石川県と長野県の54.9%、6位が沖縄県の54.6%です。最下位の奈良県47.3%に次いで低いのは秋田県47.9%、山口県48.7%で、1位と最下位の差は11.7ポイントです。

上位には都市と地方の両方が入っています。1位の東京都に加えて愛知県が7位、神奈川県が9位に入る一方、福井県2位・滋賀県3位・石川県4位・長野県4位・沖縄県6位も上位10位内です。大阪府は21位、兵庫県は39位で、大都市のある府県が上位に入るとは限りません。北陸でも富山県は17位、山陰は鳥取県15位・島根県27位で、福井県・石川県ほどではありません。都市か地方かでは並びを説明できません。就業構造基本調査は標本調査で、値は0.1ポイント単位に丸めてあります。0.1〜0.2ポイントの差でついた順位には意味がないと考えてください。

## 水準は年齢構成とも、男性の有業率とも連動する

女性と男性の有業率を都道府県ごとに並べ、点の色に65歳以上の割合を当てます。この割合は有業率の分母に合わせて15歳以上人口を分母に取っており、総人口を分母にする一般的な高齢化率より高く出ます。同じ社会・人口統計体系の人口データ（`a_pref_population`）から、15〜64歳人口の `A1302` と65歳以上人口の `A1303`（どちらも単位は人、1975年から2024年まで収録）を使って求めました。縦軸・横軸の有業率は就業構造基本調査の標本推計、色の年齢構成は[人口推計](https://www.stat.go.jp/data/jinsui/2022np/index.html)に基づく値で、出典が異なります。

```chart
{
  "layer": [
    {
      "data": {"name": "fit_line"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"male_rate\"]) && isValid(datum[\"fitted_female_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeWidth": 2,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "x": {
          "field": "male_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "男性の有業率（%）", "grid": true}
        },
        "y": {
          "field": "fitted_female_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性の有業率（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "fm_scatter"},
      "mark": {"type": "point", "filled": true, "size": 121},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "male_rate", "type": "quantitative"},
          {"field": "female_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "male_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "男性の有業率（%）", "grid": true}
        },
        "y": {
          "field": "female_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "女性の有業率（%）", "grid": true}
        },
        "color": {
          "field": "senior_share",
          "type": "quantitative",
          "scale": {
            "range": [
              "rgb(12,51,131)",
              "rgb(10,136,186)",
              "rgb(242,211,56)",
              "rgb(242,143,56)",
              "rgb(217,30,30)"
            ]
          }
        }
      }
    }
  ],
  "config": {"legend": {"disable": true}}
}
```

図の直線は47都道府県に当てはめた回帰直線です。点は右上ほど青く、左下ほど赤くなります。女性の有業率と65歳以上の割合の相関は −0.645、男性では −0.732 で、高齢者の多い地域ほど男女とも有業率は低くなります。65歳以上の割合が最も低いのは東京都の25.6%、最も高いのは秋田県の42.6%です。

有業率は年齢構成だけでは決まりません。有業率が最も低い奈良県は65歳以上の割合が36.5%と、高いほうから23番目でほぼ真ん中です。長野県は36.8%で19番目に高いにもかかわらず、水準は4位に入っています。

```sql
SELECT corr_female_male AS 女性と男性の有業率, r2_female_male AS その決定係数, corr_female_senior AS 女性有業率と65歳以上割合, corr_male_senior AS 男性有業率と65歳以上割合, corr_residual_senior AS 予想との差と65歳以上割合 FROM correlation
```

## 予想との差で並べ直すと、東京都は12位に下がる

散布図の直線から各都道府県までの縦の差を求めます。プラスなら、その地域の男性の有業率から予想される値より、女性の有業率が高いということです。

```chart
{
  "height": 780,
  "layer": [
    {
      "data": {"name": "residual_rank"},
      "mark": {"type": "bar", "color": "#8b5cf6"},
      "encoding": {
        "tooltip": [
          {"field": "residual", "type": "quantitative"},
          {"field": "area_name", "type": "nominal"}
        ],
        "x": {
          "field": "residual",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "男性の水準から予想される値との差（ポイント）", "grid": true}
        },
        "y": {
          "field": "area_name",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        }
      }
    }
  ]
}
```

上位は沖縄県の+2.6ポイント、高知県の+2.5ポイント、石川県の+2.2ポイント、京都府と鳥取県の+1.9ポイントです。下位は秋田県の−3.0ポイント、福島県の−2.3ポイント、北海道の−2.2ポイントです。京都府と鳥取県のように同じ値で並ぶ組もあります。

有業率の順位とは上位の都道府県が入れ替わります。高知県は女性の有業率そのものは51.7%で31位ですが、男性が63.8%と46位まで低い地域なので、そのなかでは女性が相対的に多く働いていることになります。逆に東京都は水準1位でも、この差では+1.0ポイントの12位です。男性の有業率も74.6%で全国1位なので、女性の有業率の高さの多くは、男性も含めた東京都全体の有業率の高さで説明できます。

この差と65歳以上の割合の相関は −0.098 で、年齢構成の影響はほとんど残りません。この差は47都道府県に当てはめた1本の直線からの距離なので、対象を市区町村や別の年に変えれば直線も値も変わります。

## 11回の調査すべてで予想を上回ったのは11県、すべてで下回ったのは10道県

同じ計算を1977年から2022年までの11回の調査それぞれに当てはめます。直線は各回の47都道府県から引き直しているので、その回のなかでの位置を表します。

11回すべてでプラスだったのは11県（石川県・福井県・長野県・岐阜県・静岡県・山形県・鳥取県・熊本県・佐賀県・宮崎県・高知県）、11回すべてマイナスだったのは10道県（北海道・宮城県・茨城県・埼玉県・千葉県・神奈川県・奈良県・和歌山県・兵庫県・山口県）です。残る26都府県は途中で符号が変わっています。47のうち21、半分近くの地域は45年間ずっと同じ側にいます。

この2つのグループにも、直線に近い県があります。グループのなかで直線に最も近づいたのは、11県では岐阜県の+0.2ポイント、10道県では山口県の−0.3ポイントです。グループの外にも、同じくらいの差の県があります。11回のうち10回プラスで、外れた1回が−0.1ポイントだった県が山梨県・島根県・徳島県と3つ。逆にプラスが1回だけで、その1回が+0.2ポイントだった大阪府と+0.3ポイントだった秋田県もあります。元データの単位は千人で、有業率は0.1ポイント単位に丸めてあり、そのうえ標本調査なので、この程度の差の県は、グループに入ることも外れることもあると考えてください。21という数は増えることも減ることもあります。

```chart
{
  "layer": [
    {
      "data": {"name": "residual_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ishikawa\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#0ea5e9",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "ishikawa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "ishikawa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "予想との差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "石川県",
          "type": "nominal",
          "scale": {
            "domain": ["石川県", "高知県", "沖縄県", "東京都", "秋田県"],
            "range": ["#0ea5e9", "#10b981", "#ec4899", "#f59e0b", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "residual_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kochi\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#10b981",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "kochi", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "kochi",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "予想との差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "高知県",
          "type": "nominal",
          "scale": {
            "domain": ["石川県", "高知県", "沖縄県", "東京都", "秋田県"],
            "range": ["#0ea5e9", "#10b981", "#ec4899", "#f59e0b", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "residual_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"okinawa\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "okinawa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "okinawa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "予想との差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "沖縄県",
          "type": "nominal",
          "scale": {
            "domain": ["石川県", "高知県", "沖縄県", "東京都", "秋田県"],
            "range": ["#0ea5e9", "#10b981", "#ec4899", "#f59e0b", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "residual_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f59e0b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tokyo", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "tokyo",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "予想との差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "東京都",
          "type": "nominal",
          "scale": {
            "domain": ["石川県", "高知県", "沖縄県", "東京都", "秋田県"],
            "range": ["#0ea5e9", "#10b981", "#ec4899", "#f59e0b", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "residual_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"akita\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "akita", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "調査年", "format": "d"}
        },
        "y": {
          "field": "akita",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "予想との差（ポイント）", "grid": true}
        },
        "color": {
          "datum": "秋田県",
          "type": "nominal",
          "scale": {
            "domain": ["石川県", "高知県", "沖縄県", "東京都", "秋田県"],
            "range": ["#0ea5e9", "#10b981", "#ec4899", "#f59e0b", "#64748b"]
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

直線から最も遠いのは高知県と石川県です。45年で最も直線に近づいた回でも、高知県は+2.5ポイント、石川県は+2.2ポイントの幅がありました。石川県はその最小が2022年で、1977年の+6.1ポイントから縮んでいます。高知県は2007年と2022年がともに+2.5ポイントです。どちらも途中で差が広がった回があり、石川県は3回、高知県は4回です。

符号が変わった26都府県には、大きく動いた県も、ほぼ一方に寄ったままの県もあります。沖縄県は1977年に−6.8ポイントと予想を大きく下回っていましたが、2002年の+0.3ポイントで初めてプラスに転じ、2022年は+2.6ポイントで全国最大になりました。東京都も1977年の−7.2ポイントから水準を上げ、2012年の+0.4ポイントでプラスに入りました。同じ26都府県でも秋田県はプラスが1992年の+0.3ポイント1回だけで、残る10回はマイナスです。この+0.3が消えれば、秋田県は11回すべてマイナスの側に移ります。沖縄県が転じた2002年の+0.3、東京都が転じた2012年の+0.4も同じ幅なので、符号が変わった年は前後する可能性があります。

11県と10道県の違いは、女性の有業率に表れています。2022年の平均を取ると、男性の有業率は11県が67.9%、10道県が67.6%でほとんど同じです。それに対して女性の有業率は53.8%と50.9%で2.9ポイント違います。予想との差は女性の有業率から男性の水準に基づく予想を引いた値なので、男性の有業率が同じくらいなら、差は女性の有業率の違いになります。65歳以上の割合は11県のほうが高く（36.8%対34.3%）、11県の女性の有業率が高いのは若い人が多いためではありません。

2022年に予想との差が大きかった沖縄県・高知県・石川県も、経緯は違います。石川県と高知県は45年間ずっとその側にあり、沖縄県は途中で入れ替わった側です。自分の地域がどちらなのかは、一つの調査年の順位ではなく、符号が続いているかどうかで分かります。下の表の「プラスだった調査回数」がその列です。

```sql
SELECT area_name AS 都道府県, female_rate AS 女性の有業率, female_rank AS 女性の順位, male_rate AS 男性の有業率, male_rank AS 男性の順位, senior_share AS 高齢者割合15歳以上人口比, residual AS 予想との差, residual_rank AS 予想との差の順位, positive_surveys AS プラスだった調査回数 FROM rank_table
```

## まとめ

- 女性と男性の有業率の相関は0.802で、都道府県ごとのばらつきの64%は男性の有業率で説明できます
- 男性の水準から予想される値との差で並べ直すと、東京都は1位から12位に下がります
- 11回の調査すべてでプラスだったのは11県、すべてマイナスだったのは10道県で、47のうち21は45年間ずっと同じ側にいます。残る26都府県は途中で符号が変わっていて、沖縄県は2002年、東京都は2012年がその境目でした
- 全国では男女差が45年で35.0ポイントから15.9ポイントに縮みましたが、その19.1ポイントのうち11.2ポイントは男性の有業率の低下によるものです
- 11県と10道県の違いは、男性の有業率や年齢構成では説明できません。2022年の平均は男性が67.9%と67.6%でほぼ同じ、65歳以上の割合はむしろ11県のほうが高い36.8%です

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.e-stat.go.jp/regional-statistics/ssdsview)の都道府県別労働データ（`f_pref_labor`）と人口データ（`a_pref_population`）を 2026-09-09 時点で集計しています。有業率の元データは総務省統計局の[就業構造基本調査](https://www.stat.go.jp/data/shugyou/2022/index.html)で、最新の調査は2022年10月1日現在（表の時間軸は「2022年度」表記）です。

Queriaは、社会・人口統計体系などの官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[都道府県別の労働データのテーブル](/datasets/queria/e_stat/ssds/f_pref_labor)から、自分の地域の有業率を調査年ごとに確認できます。

```sql id=national_trend
WITH rate AS (SELECT year, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE area_name = '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY year) SELECT year, ROUND(f, 1) AS female_rate, ROUND(m, 1) AS male_rate, ROUND(m - f, 1) AS gap_pt FROM rate ORDER BY year
```

```sql id=senior_trend
SELECT year, ROUND(MAX(CASE WHEN cat01 = 'A1303' THEN value END) / (MAX(CASE WHEN cat01 = 'A1303' THEN value END) + MAX(CASE WHEN cat01 = 'A1302' THEN value END)) * 100, 1) AS senior_share FROM e_stat.ssds.a_pref_population WHERE area_name = '全国' AND cat01 IN ('A1302', 'A1303') AND year IN (1977, 1979, 1982, 1987, 1992, 1997, 2002, 2007, 2012, 2017, 2022) AND value IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=f_rank
WITH rate AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name) SELECT area_name, ROUND(f, 1) AS female_rate FROM rate ORDER BY female_rate DESC, area_name
```

```sql id=fm_scatter
WITH rate AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name), age AS (SELECT area_name, MAX(CASE WHEN cat01 = 'A1303' THEN value END) / (MAX(CASE WHEN cat01 = 'A1303' THEN value END) + MAX(CASE WHEN cat01 = 'A1302' THEN value END)) * 100 AS senior FROM e_stat.ssds.a_pref_population WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('A1302', 'A1303') AND value IS NOT NULL GROUP BY area_name) SELECT r.area_name, ROUND(r.m, 1) AS male_rate, ROUND(r.f, 1) AS female_rate, ROUND(a.senior, 1) AS senior_share FROM rate r JOIN age a ON a.area_name = r.area_name ORDER BY r.area_name
```

```sql id=fit_line
WITH rate AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name), fit AS (SELECT REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate), ends AS (SELECT MIN(m) AS m FROM rate UNION ALL SELECT MAX(m) AS m FROM rate) SELECT ROUND(ends.m, 1) AS male_rate, ROUND(fit.s * ends.m + fit.i, 1) AS fitted_female_rate FROM ends, fit ORDER BY male_rate
```

```sql id=residual_rank
WITH rate AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name), fit AS (SELECT REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate) SELECT area_name, ROUND(f - (fit.s * m + fit.i), 1) AS residual FROM rate, fit ORDER BY residual DESC, area_name
```

```sql id=correlation
WITH rate AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name), age AS (SELECT area_name, MAX(CASE WHEN cat01 = 'A1303' THEN value END) / (MAX(CASE WHEN cat01 = 'A1303' THEN value END) + MAX(CASE WHEN cat01 = 'A1302' THEN value END)) * 100 AS senior FROM e_stat.ssds.a_pref_population WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('A1302', 'A1303') AND value IS NOT NULL GROUP BY area_name), fit AS (SELECT REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate) SELECT ROUND(CORR(r.f, r.m), 3) AS corr_female_male, ROUND(REGR_R2(r.f, r.m), 3) AS r2_female_male, ROUND(CORR(r.f, a.senior), 3) AS corr_female_senior, ROUND(CORR(r.m, a.senior), 3) AS corr_male_senior, ROUND(CORR(r.f - (fit.s * r.m + fit.i), a.senior), 3) AS corr_residual_senior FROM rate r JOIN age a ON a.area_name = r.area_name, fit
```

```sql id=rank_table
WITH rate AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name), age AS (SELECT area_name, MAX(CASE WHEN cat01 = 'A1303' THEN value END) / (MAX(CASE WHEN cat01 = 'A1303' THEN value END) + MAX(CASE WHEN cat01 = 'A1302' THEN value END)) * 100 AS senior FROM e_stat.ssds.a_pref_population WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('A1302', 'A1303') AND value IS NOT NULL GROUP BY area_name), fit AS (SELECT REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate), rate_all AS (SELECT year, area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY year, area_name), fit_all AS (SELECT year, REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate_all GROUP BY year), signs AS (SELECT r.area_name, COUNT(*) AS surveys, COUNT(*) FILTER (WHERE r.f - (fa.s * r.m + fa.i) > 0) AS positive_surveys, ROUND(MIN(r.f - (fa.s * r.m + fa.i)), 1) AS min_residual, ROUND(MAX(r.f - (fa.s * r.m + fa.i)), 1) AS max_residual FROM rate_all r JOIN fit_all fa ON fa.year = r.year GROUP BY r.area_name), j AS (SELECT r.area_name, ROUND(r.f, 1) AS female_rate, ROUND(r.m, 1) AS male_rate, ROUND(a.senior, 1) AS senior_share, ROUND(r.f - (fit.s * r.m + fit.i), 1) AS residual FROM rate r JOIN age a ON a.area_name = r.area_name, fit) SELECT j.area_name, j.female_rate, RANK() OVER (ORDER BY j.female_rate DESC) AS female_rank, j.male_rate, RANK() OVER (ORDER BY j.male_rate DESC) AS male_rank, j.senior_share, RANK() OVER (ORDER BY j.senior_share DESC) AS senior_rank, j.residual, RANK() OVER (ORDER BY j.residual DESC) AS residual_rank, signs.positive_surveys, signs.surveys FROM j JOIN signs ON signs.area_name = j.area_name ORDER BY female_rank, j.area_name
```

```sql id=residual_trend
WITH rate AS (SELECT year, area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY year, area_name), fit AS (SELECT year, REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate GROUP BY year), res AS (SELECT r.year, r.area_name, r.f - (fit.s * r.m + fit.i) AS res FROM rate r JOIN fit ON fit.year = r.year) SELECT year, ROUND(MAX(CASE WHEN area_name = '石川県' THEN res END), 1) AS ishikawa, ROUND(MAX(CASE WHEN area_name = '高知県' THEN res END), 1) AS kochi, ROUND(MAX(CASE WHEN area_name = '沖縄県' THEN res END), 1) AS okinawa, ROUND(MAX(CASE WHEN area_name = '東京都' THEN res END), 1) AS tokyo, ROUND(MAX(CASE WHEN area_name = '秋田県' THEN res END), 1) AS akita FROM res GROUP BY year ORDER BY year
```

```sql id=residual_signs
WITH rate_all AS (SELECT year, area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY year, area_name), fit_all AS (SELECT year, REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate_all GROUP BY year), signs AS (SELECT r.area_name, COUNT(*) AS surveys, COUNT(*) FILTER (WHERE r.f - (fa.s * r.m + fa.i) > 0) AS positive_surveys, ROUND(MIN(r.f - (fa.s * r.m + fa.i)), 1) AS min_residual, ROUND(MAX(r.f - (fa.s * r.m + fa.i)), 1) AS max_residual FROM rate_all r JOIN fit_all fa ON fa.year = r.year GROUP BY r.area_name) SELECT area_name, surveys, positive_surveys, min_residual, max_residual FROM signs ORDER BY positive_surveys DESC, min_residual DESC, area_name
```

```sql id=group_profile
WITH rate_all AS (SELECT year, area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY year, area_name), fit_all AS (SELECT year, REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate_all GROUP BY year), signs AS (SELECT r.area_name, COUNT(*) AS surveys, COUNT(*) FILTER (WHERE r.f - (fa.s * r.m + fa.i) > 0) AS positive_surveys, ROUND(MIN(r.f - (fa.s * r.m + fa.i)), 1) AS min_residual, ROUND(MAX(r.f - (fa.s * r.m + fa.i)), 1) AS max_residual FROM rate_all r JOIN fit_all fa ON fa.year = r.year GROUP BY r.area_name), r22 AS (SELECT area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY area_name), a22 AS (SELECT area_name, MAX(CASE WHEN cat01 = 'A1303' THEN value END) / (MAX(CASE WHEN cat01 = 'A1303' THEN value END) + MAX(CASE WHEN cat01 = 'A1302' THEN value END)) * 100 AS senior FROM e_stat.ssds.a_pref_population WHERE year = 2022 AND area_name <> '全国' AND cat01 IN ('A1302', 'A1303') AND value IS NOT NULL GROUP BY area_name), g AS (SELECT s.area_name, CASE WHEN s.positive_surveys = s.surveys THEN 'always_positive' WHEN s.positive_surveys = 0 THEN 'always_negative' ELSE 'changed_sign' END AS sign_group, s.min_residual, s.max_residual, r22.f, r22.m, a22.senior FROM signs s JOIN r22 ON r22.area_name = s.area_name JOIN a22 ON a22.area_name = s.area_name) SELECT sign_group, COUNT(*) AS prefectures, CASE WHEN sign_group = 'always_positive' THEN MIN(min_residual) WHEN sign_group = 'always_negative' THEN MAX(max_residual) END AS closest_to_zero, ROUND(AVG(f), 1) AS avg_female_rate, ROUND(AVG(m), 1) AS avg_male_rate, ROUND(AVG(senior), 1) AS avg_senior_share FROM g GROUP BY sign_group ORDER BY prefectures DESC
```

```sql id=sign_groups
WITH rate_all AS (SELECT year, area_name, MAX(CASE WHEN cat01 = 'F120202' THEN value END) / MAX(CASE WHEN cat01 = 'F120102' THEN value END) * 100 AS f, MAX(CASE WHEN cat01 = 'F120201' THEN value END) / MAX(CASE WHEN cat01 = 'F120101' THEN value END) * 100 AS m FROM e_stat.ssds.f_pref_labor WHERE area_name <> '全国' AND cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY year, area_name), fit_all AS (SELECT year, REGR_SLOPE(f, m) AS s, REGR_INTERCEPT(f, m) AS i FROM rate_all GROUP BY year), signs AS (SELECT r.area_name, COUNT(*) AS surveys, COUNT(*) FILTER (WHERE r.f - (fa.s * r.m + fa.i) > 0) AS positive_surveys, ROUND(MIN(r.f - (fa.s * r.m + fa.i)), 1) AS min_residual, ROUND(MAX(r.f - (fa.s * r.m + fa.i)), 1) AS max_residual FROM rate_all r JOIN fit_all fa ON fa.year = r.year GROUP BY r.area_name) SELECT CASE WHEN positive_surveys = surveys THEN 'always_positive' WHEN positive_surveys = 0 THEN 'always_negative' ELSE 'changed_sign' END AS sign_group, COUNT(*) AS prefectures, STRING_AGG(area_name, ' / ' ORDER BY area_name) AS pref_names FROM signs GROUP BY 1 ORDER BY prefectures DESC
```

```sql id=age_coverage
SELECT cat01, MIN(item_name) AS item, MIN(year) AS min_year, MAX(year) AS max_year, COUNT(DISTINCT year) AS n_years, MIN(unit) AS unit FROM e_stat.ssds.a_pref_population WHERE cat01 IN ('A1302', 'A1303') AND value IS NOT NULL GROUP BY cat01 ORDER BY cat01
```

```sql id=coverage
SELECT cat01, MIN(item_name) AS item, MIN(year) AS min_year, MAX(year) AS max_year, COUNT(DISTINCT year) AS n_surveys, MIN(unit) AS unit, MAX(time_name) AS latest_time_name FROM e_stat.ssds.f_pref_labor WHERE cat01 IN ('F120101', 'F120102', 'F120201', 'F120202') AND value IS NOT NULL GROUP BY cat01 ORDER BY cat01
```
