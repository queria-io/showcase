---
title: 竹富町では2025年に、住民の6人に1人が町を出ていきました。それでも人口は34人増えています
description: 市区町村別の転出者数を住民基本台帳人口で割り、全国1,719市区町村を比較しました。転出率は山形県大蔵村の1.56%から北海道占冠村の20.82%まで13倍の差があり、中央値は3.33%です。転出率が7%以上の65市区町村でも、人口増減率の絶対値の中央値は1.78%です。
publishedAt: 2026-09-20
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口移動
  - 住民基本台帳
  - 市区町村
datasets:
  - queria/e_stat
sources:
  - title: 住民基本台帳人口移動報告 2025年（令和7年）結果
    url: https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html
    publisher: 総務省統計局
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
agentHint: 自分の県の市区町村について、2025年の転出者数を住民基本台帳人口で割った転出率を高い順に出して。日本人移動者と外国人移動者に分けた内訳と、住民基本台帳の国外からの転入者数も付けて
socialAnnounce: |-
  市区町村別の転出者数を住民基本台帳人口で割り、全国1,719市区町村を比べました。

  沖縄県竹富町では1年で住民の6人に1人が町を出ていきますが、人口は34人増えています。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

人口4,208人の沖縄県竹富町では、2025年の1年間に691人が町を出て、713人が他の市区町村から転入しました。1年間の人口の増減は34人増です。1年間に町を出た人が住民に占める割合（転出率）を全国1,719市区町村で比較すると、中央値は3.33%で、最も低い山形県大蔵村の1.56%と最も高い北海道占冠村の20.82%では13倍の差があります。転出率が7%以上の65市区町村でも、人口増減率の絶対値の中央値は1.78%で、出ていった人数の5分の1ほどしか人口の変化に表れていません。

この記事では、[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html)の市区町村別データと[住民基本台帳人口](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)を結合し、市区町村ごとの転出率を算出しました。移動報告は住民票の異動届にもとづく実績で、推計値ではありません。集計しているのは市区町村をまたぐ移動だけで、同じ市区町村の中での引っ越しと、国外との出入りは含みません。

## 転出率の中央値は3.33%で、市区町村によって13倍の差がある

全国では、2025年に市区町村をまたいで移動した人が5,190,548人います。人口124,330,690人の4.17%で、およそ24人に1人です。市区町村ごとの転出率を1%刻みで集計しました。棒の高さは、その範囲に入る市区町村の数です。

```chart
{
  "layer": [
    {
      "data": {"name": "dist"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [
          {"field": "band", "type": "nominal"},
          {"field": "municipalities", "type": "quantitative"}
        ],
        "x": {
          "field": "band",
          "type": "nominal",
          "axis": {"title": "1年間に町を出た人の割合", "labelAngle": 0},
          "sort": null
        },
        "y": {
          "field": "municipalities",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "市区町村数", "grid": true}
        }
      }
    }
  ]
}
```

最も多いのは3%台の640市区町村で、2%台の571が続きます。中央値は3.33%で、住民のおよそ30人に1人が1年で町を出ています。全国の4.17%は移動者の総数を総人口で割った値で、市区町村ごとの値の中央値とは異なります。9%以上の市区町村は32あります。最も低いのは山形県大蔵村の1.56%、最も高いのは北海道占冠村の20.82%で、13倍の差があります。

## 人口2万人以上で転出率が高いのは、大都市とその周辺、島と観光地、空港や工場のある市町

人口2万人以上の市区町村を、転出率の高い順に20並べました。棒は日本人住民と外国人住民の転出に分けています。移動報告には国籍の区分があり、日本人移動者（`61000`、2010年から）と外国人移動者（`62000`、2020年から）の合計が移動者（`60000`、2018年から）です。分母はどちらも町の総人口なので、2つの棒を合計すると総数の転出率になります。外国人住民の転出率は、外国人住民のうち何割が転出したかを示す値ではありません。東京23区は、移動報告が「特別区部」を1つの団体として集計しているので、区から区への移動はこの数字に含まれません。冒頭の竹富町は人口が2万人未満なので、この図にはありません。

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "top_out"},
      "transform": [
        {"fold": ["jp_rate", "fr_rate"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"jp_rate\": \"日本人住民\", \"fr_rate\": \"外国人住民\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"jp_rate\",\"fr_rate\"], datum.__series)", "as": "__order"}
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
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["日本人住民", "外国人住民"], "range": ["#3b82f6", "#f97316"]},
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

大都市では、東京都特別区部が6.80%、大阪府大阪市が6.89%、愛知県名古屋市が6.25%です。隣接する埼玉県和光市の7.71%と埼玉県蕨市の7.51%はこれより高く、東京都武蔵野市の6.38%も名古屋市より高くなっています。島と観光地では、沖縄県石垣市が7.12%、沖縄県宮古島市が6.32%、広島県江田島市が6.29%です。空港や工場のある市町では、千葉県成田市が7.45%、千葉県富里市が9.87%、千葉県酒々井町が7.45%、群馬県大泉町が6.09%です。

日本人住民と外国人住民の内訳は、市町によって大きく異なります。埼玉県和光市は日本人住民が7.00%、外国人住民が0.71%、石川県輪島市は6.19%と0.12%で、転出した人のほとんどが日本人住民です。千葉県富里市は日本人住民が3.64%、外国人住民が6.23%、愛知県美浜町は2.98%と4.73%で、外国人住民の転出のほうが多くなっています。和光市と美浜町は転出率がどちらも7.71%ですが、転出した人の国籍の構成は大きく異なります。

## 転出率が7%以上の65市区町村でも、人口増減率の絶対値の中央値は1.78%

横軸に転出率、縦軸に人口の増減率（住民基本台帳人口の1年間の増減数を人口で割った値）を取りました。1点が1市区町村です。縦軸は出生・死亡と国外との出入りを含む実際の増減で、横軸の転出とは集計の範囲が異なります。

```chart
{
  "height": 340,
  "layer": [
    {
      "data": {"name": "scatter_rest"},
      "mark": {"type": "point", "opacity": 0.6, "filled": true, "size": 25},
      "encoding": {
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "out_rate", "type": "quantitative"},
          {"field": "change_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "out_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "y": {
          "field": "change_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口の増減率（%）", "grid": true}
        },
        "color": {
          "datum": "転出率7%未満",
          "type": "nominal",
          "scale": {"domain": ["転出率7%未満", "転出率7%以上"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "scatter_high"},
      "mark": {"type": "point", "filled": true, "size": 49},
      "encoding": {
        "tooltip": [
          {"field": "name", "type": "nominal"},
          {"field": "out_rate", "type": "quantitative"},
          {"field": "change_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "out_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "y": {
          "field": "change_rate",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "人口の増減率（%）", "grid": true}
        },
        "color": {
          "datum": "転出率7%以上",
          "type": "nominal",
          "scale": {"domain": ["転出率7%未満", "転出率7%以上"], "range": ["#94a3b8", "#ef4444"]},
          "title": null
        }
      }
    }
  ]
}
```

転出率が7%以上の市区町村は65あり、その転出率の中央値は8.96%、人口増減率の絶対値の中央値は1.78%です。中央値で比較すると、出ていった人数の5分の1ほどしか人口の変化に表れていません。1,719市区町村全体でも、転出率の中央値3.33%に対して、人口増減率の絶対値の中央値は1.46%です。

個別の市区町村では、この差がさらに大きくなります。埼玉県和光市は住民84,890人のうち6,542人が転出しましたが、1年間の人口の増減は27人増です。東京都特別区部は661,232人が転出し、人口は66,171人増えています。沖縄県竹富町は691人が転出して34人増、北海道倶知安町は1,755人が転出して277人増えました。

転出率が高い市区町村の中には、人口が大きく減ったところもあります。転出率7%以上の65市区町村で人口の減少率が最も大きいのは石川県珠洲市で、転出率8.33%に対して人口は8.39%減りました。2024年1月に地震が起きた能登地方の市です。

## 富里市と美浜町では、国外からの転入が国内からの転入より多い

住民基本台帳の集計では、転入者が国内からと国外からに分かれています。同じ20市区町村について、転入の内訳を示します。分母は町の総人口です。

```chart
{
  "height": 500,
  "layer": [
    {
      "data": {"name": "inflow_mix"},
      "transform": [
        {"fold": ["dom_rate", "ovs_rate"], "as": ["__series", "__value"]},
        {
          "calculate": "{\"dom_rate\": \"国内から\", \"ovs_rate\": \"国外から\"}[datum.__series]",
          "as": "__name"
        },
        {"calculate": "indexof([\"dom_rate\",\"ovs_rate\"], datum.__series)", "as": "__order"}
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
          "axis": {"title": "1年間に町へ入ってきた人の割合（%）", "grid": true}
        },
        "color": {
          "field": "__name",
          "type": "nominal",
          "scale": {"domain": ["国内から", "国外から"], "range": ["#3b82f6", "#22c55e"]},
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

埼玉県和光市は国内から7.55%、国外から0.75%で、転入者のほとんどは国内からです。千葉県富里市は国内から5.15%、国外から5.92%で、国外からのほうが多くなっています。愛知県美浜町も国内から2.60%、国外から5.30%です。転出率が高いのに人口が大きく減っていない市町では、国外からの転入が転出の分を補っています。石川県輪島市は国内から1.83%、国外から0.13%で、転入の割合がこの20市区町村の中で最も低くなっています。転出率6.31%に対して転入は合計1.96%で、人口は1年で6.27%減りました。人口の増減には出生・死亡や国外への転出も含まれるので、減少率が転出入の差より大きくなっています。

北海道倶知安町では、国外からの転入がさらに大きな割合を占めます。2025年の1年間に国外から3,411人が転入しており、人口17,120人の19.92%にあたります。国内では転出1,755人に対して転入が1,377人で、378人の転出超過ですが、人口は277人増えています。3,411人は転入だけの人数で、国外への転出や出生・死亡を差し引いていないので、そのまま人口の増加にはなりません。この町では、移動報告の転出超過だけを見ると、人口が増えているのに減っていると判断することになります。

## 2018年から2025年に、富里市の転出率は1.9倍になった

全国と、4つの市町の転出率の推移です。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"hakone\"]) ? 0 : 1",
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
          {"field": "hakone", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "hakone",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "color": {
          "datum": "神奈川県箱根町",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県箱根町", "北海道倶知安町", "千葉県富里市", "埼玉県和光市", "全国"],
            "range": ["#ef4444", "#f97316", "#7c3aed", "#22c55e", "#94a3b8"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kutchan\"]) ? 0 : 1",
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
          {"field": "kutchan", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "kutchan",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "color": {
          "datum": "北海道倶知安町",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県箱根町", "北海道倶知安町", "千葉県富里市", "埼玉県和光市", "全国"],
            "range": ["#ef4444", "#f97316", "#7c3aed", "#22c55e", "#94a3b8"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tomisato\"]) ? 0 : 1",
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
          {"field": "tomisato", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tomisato",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "color": {
          "datum": "千葉県富里市",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県箱根町", "北海道倶知安町", "千葉県富里市", "埼玉県和光市", "全国"],
            "range": ["#ef4444", "#f97316", "#7c3aed", "#22c55e", "#94a3b8"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"wako\"]) ? 0 : 1",
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
          {"field": "wako", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "wako",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "color": {
          "datum": "埼玉県和光市",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県箱根町", "北海道倶知安町", "千葉県富里市", "埼玉県和光市", "全国"],
            "range": ["#ef4444", "#f97316", "#7c3aed", "#22c55e", "#94a3b8"]
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
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"nationwide\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#94a3b8",
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "nationwide", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "nationwide",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1年間に町を出た人の割合（%）", "grid": true}
        },
        "color": {
          "datum": "全国",
          "type": "nominal",
          "scale": {
            "domain": ["神奈川県箱根町", "北海道倶知安町", "千葉県富里市", "埼玉県和光市", "全国"],
            "range": ["#ef4444", "#f97316", "#7c3aed", "#22c55e", "#94a3b8"]
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

神奈川県箱根町は2019年の11.11%から2021年の8.56%まで下がり、2025年に11.11%に戻っています。北海道倶知安町は2022年の8.02%が最も低く、2025年は10.25%で8年間で最も高くなりました。どちらも観光地で、転出率が下がった時期は往来が制限されていた期間と重なります。

千葉県富里市は、2018年の5.13%から2025年の9.87%まで1.9倍になりました。2021年と2024年に一度下がっていますが、8年間を通して見ると水準が上がっています。埼玉県和光市は8%前後で推移し、2025年は7.71%です。全国は2018年の4.20%から2025年の4.17%まで4%台で変わっておらず、市区町村ごとの変化は全国の値には表れません。

## 業務での使い方

転出率は、1本のクエリで自分の自治体の値を算出できます。人口の増減と並べると、住民の入れ替わりの大きさを確認できます。

- 転入者向けの案内の規模の見積もり: 自分の市区町村の国内からの転入者数を人口で割り、全国の中央値3.01%と比較できます。中央値の2倍を超える場合は、転入手続きの窓口と新しい住民向けの案内の量を、人口規模とは別に見積もる必要があります
- 多言語対応の優先度の判断: 日本人移動者（`61000`）と外国人移動者（`62000`）に分けて転出を算出し、住民基本台帳の国外からの転入者数も合わせて確認できます。富里市や倶知安町のように、国外からの転入が人口の数%から2割に達する自治体では、窓口と広報の多言語化の必要性が高くなります
- 住民名簿を使う施策の見直し: 転出率が8%を超える自治体では、1年で住民の12.5人に1人以上が町を出ます。健診の受診勧奨や地域行事の案内を住民名簿から送る場合は、名簿の更新頻度も施策の一部として決める必要があります
- 人口ビジョンの前提の確認: 移動報告の転入超過数だけで社会増減を見ると、倶知安町のように国外からの転入で増減の向きが逆になる自治体があります。住民基本台帳の増減数と並べて、どちらの数字を使って議論しているかを統一する必要があります

## データの出典

本記事は総務省統計局[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html)の市区町村別の転入者数・転出者数と、総務省[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)の人口・人口動態を 2026-09-20 時点で集計しています。移動報告の値は1月から12月までの暦年の合計です。分母の人口は2025年1月1日現在の値、人口の増減数と転入者数の内訳は2026年1月1日現在の表にある直前1年間の値で、移動報告と同じ2025年の1年間にあたります。

Queriaは、総務省のこれらのデータを、地域コードの桁と列名・単位を統一したテーブルにし、テーブルと列の意味をメタデータに記載して公開しています。本記事で使った[市区町村別 人口移動テーブル](/datasets/e_stat/migration/municipality_migration)と[住民基本台帳人口テーブル](/datasets/e_stat/resident_registry/population)から、自分の自治体の転出入を近隣の市区町村と比較したり、国籍や国内・国外の区分ごとに確認したりできます。

```sql id=summary
WITH pop AS (SELECT p.area_code, p.population_total, n.net_change, n.moved_in_domestic AS in_dom FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' UNION ALL SELECT '13100', SUM(p.population_total), SUM(n.net_change), SUM(n.moved_in_domestic) FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' AND p.area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, outflow FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code = '60000'), j AS (SELECT mig.outflow * 100.0 / pop.population_total AS out_rate, pop.in_dom * 100.0 / pop.population_total AS in_rate, pop.net_change * 100.0 / pop.population_total AS change_rate FROM mig JOIN pop ON pop.area_code = mig.area) SELECT COUNT(*) AS municipalities, ROUND(MEDIAN(out_rate), 2) AS median_out_rate, ROUND(MIN(out_rate), 2) AS min_out_rate, ROUND(MAX(out_rate), 2) AS max_out_rate, ROUND(MEDIAN(in_rate), 2) AS median_in_rate, ROUND(MEDIAN(ABS(change_rate)), 2) AS median_abs_change, COUNT(*) FILTER (WHERE out_rate >= 7) AS n_over7, ROUND(MEDIAN(out_rate) FILTER (WHERE out_rate >= 7), 2) AS median_out_rate_over7, ROUND(MEDIAN(ABS(change_rate)) FILTER (WHERE out_rate >= 7), 2) AS median_abs_change_over7 FROM j
```

```sql id=coverage
SELECT nationality_code, nationality, MIN(year) AS first_year, MAX(year) AS last_year FROM e_stat.migration.municipality_migration GROUP BY nationality_code, nationality ORDER BY nationality_code
```

```sql id=national
SELECT m.year, m.outflow AS movers, p.population_total AS population, ROUND(m.outflow * 100.0 / p.population_total, 2) AS out_rate FROM e_stat.migration.municipality_migration m JOIN e_stat.resident_registry.population p ON p.year = m.year AND p.area_level = 'national' AND p.resident_kind = 'total' WHERE m.area_level = 'national' AND m.sex_code = '0' AND m.nationality_code = '60000' AND m.year <= 2025 ORDER BY m.year
```

```sql id=dist
WITH pop AS (SELECT area_code, population_total FROM e_stat.resident_registry.population WHERE year = 2025 AND resident_kind = 'total' AND area_level = 'municipality' UNION ALL SELECT '13100', SUM(population_total) FROM e_stat.resident_registry.population WHERE year = 2025 AND resident_kind = 'total' AND area_level = 'municipality' AND area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, outflow FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code = '60000'), binned AS (SELECT CAST(LEAST(FLOOR(mig.outflow * 100.0 / pop.population_total), 9) AS INTEGER) AS b FROM mig JOIN pop ON pop.area_code = mig.area) SELECT CASE WHEN b >= 9 THEN '9%以上' ELSE b || '%台' END AS band, COUNT(*) AS municipalities FROM binned GROUP BY b ORDER BY b
```

```sql id=examples
WITH pop AS (SELECT p.area_code, p.pref_name, p.population_total, n.net_change, n.moved_in_overseas AS in_ovs, n.births, n.deaths FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' UNION ALL SELECT '13100', '東京都', SUM(p.population_total), SUM(n.net_change), SUM(n.moved_in_overseas), SUM(n.births), SUM(n.deaths) FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' AND p.area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, area_name, inflow, outflow FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code = '60000') SELECT CASE WHEN mig.area_name LIKE pop.pref_name || '%' THEN mig.area_name ELSE pop.pref_name || mig.area_name END AS name, pop.population_total AS population, mig.outflow AS moved_out, mig.inflow AS moved_in, pop.in_ovs AS moved_in_overseas, pop.births, pop.deaths, pop.net_change, ROUND(mig.outflow * 100.0 / pop.population_total, 2) AS out_rate, ROUND(pop.in_ovs * 100.0 / pop.population_total, 2) AS overseas_rate, ROUND(pop.net_change * 100.0 / pop.population_total, 2) AS change_rate FROM mig JOIN pop ON pop.area_code = mig.area WHERE mig.area IN ('47381', '14382', '01400', '11229', '13100', '12233', '06365') ORDER BY out_rate DESC
```

```sql id=top_out
WITH pop AS (SELECT area_code, pref_name, population_total FROM e_stat.resident_registry.population WHERE year = 2025 AND resident_kind = 'total' AND area_level = 'municipality' UNION ALL SELECT '13100', '東京都', SUM(population_total) FROM e_stat.resident_registry.population WHERE year = 2025 AND resident_kind = 'total' AND area_level = 'municipality' AND area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, area_name, SUM(outflow) FILTER (WHERE nationality_code = '61000') AS out_jp, SUM(outflow) FILTER (WHERE nationality_code = '62000') AS out_fr FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code IN ('61000', '62000') GROUP BY area, area_name), j AS (SELECT CASE WHEN mig.area_name LIKE pop.pref_name || '%' THEN mig.area_name ELSE pop.pref_name || mig.area_name END AS name, mig.out_jp * 100.0 / pop.population_total AS jp_rate, mig.out_fr * 100.0 / pop.population_total AS fr_rate FROM mig JOIN pop ON pop.area_code = mig.area WHERE pop.population_total >= 20000), ranked AS (SELECT name, ROUND(jp_rate, 2) AS jp_rate, ROUND(ROUND(jp_rate + fr_rate, 2) - ROUND(jp_rate, 2), 2) AS fr_rate, ROUND(jp_rate + fr_rate, 2) AS out_rate, ROW_NUMBER() OVER (ORDER BY jp_rate + fr_rate DESC, name) AS rn FROM j) SELECT name, jp_rate, fr_rate, out_rate FROM ranked WHERE rn <= 20 ORDER BY rn
```

```sql id=inflow_mix
WITH pop AS (SELECT p.area_code, p.pref_name, p.population_total, n.moved_in_domestic AS in_dom, n.moved_in_overseas AS in_ovs FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' UNION ALL SELECT '13100', '東京都', SUM(p.population_total), SUM(n.moved_in_domestic), SUM(n.moved_in_overseas) FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' AND p.area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, area_name, outflow FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code = '60000'), j AS (SELECT CASE WHEN mig.area_name LIKE pop.pref_name || '%' THEN mig.area_name ELSE pop.pref_name || mig.area_name END AS name, mig.outflow * 100.0 / pop.population_total AS out_rate, pop.in_dom * 100.0 / pop.population_total AS dom_rate, pop.in_ovs * 100.0 / pop.population_total AS ovs_rate FROM mig JOIN pop ON pop.area_code = mig.area WHERE pop.population_total >= 20000), ranked AS (SELECT name, ROUND(dom_rate, 2) AS dom_rate, ROUND(ovs_rate, 2) AS ovs_rate, ROW_NUMBER() OVER (ORDER BY out_rate DESC, name) AS rn FROM j) SELECT name, dom_rate, ovs_rate FROM ranked WHERE rn <= 20 ORDER BY rn
```

```sql id=scatter_high
WITH pop AS (SELECT p.area_code, p.pref_name, p.population_total, n.net_change FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' UNION ALL SELECT '13100', '東京都', SUM(p.population_total), SUM(n.net_change) FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' AND p.area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, area_name, outflow FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code = '60000'), j AS (SELECT CASE WHEN mig.area_name LIKE pop.pref_name || '%' THEN mig.area_name ELSE pop.pref_name || mig.area_name END AS name, mig.outflow * 100.0 / pop.population_total AS out_rate, pop.net_change * 100.0 / pop.population_total AS change_rate FROM mig JOIN pop ON pop.area_code = mig.area) SELECT name, ROUND(out_rate, 2) AS out_rate, ROUND(change_rate, 2) AS change_rate FROM j WHERE out_rate >= 7 ORDER BY out_rate DESC, name
```

```sql id=scatter_rest
WITH pop AS (SELECT p.area_code, p.pref_name, p.population_total, n.net_change FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' UNION ALL SELECT '13100', '東京都', SUM(p.population_total), SUM(n.net_change) FROM e_stat.resident_registry.population p JOIN e_stat.resident_registry.population n ON n.area_code = p.area_code AND n.year = 2026 AND n.resident_kind = 'total' AND n.area_level = 'municipality' WHERE p.year = 2025 AND p.resident_kind = 'total' AND p.area_level = 'municipality' AND p.area_code BETWEEN '13101' AND '13123'), mig AS (SELECT area, area_name, outflow FROM e_stat.migration.municipality_migration WHERE year = 2025 AND area_level = 'municipality' AND sex_code = '0' AND nationality_code = '60000'), j AS (SELECT CASE WHEN mig.area_name LIKE pop.pref_name || '%' THEN mig.area_name ELSE pop.pref_name || mig.area_name END AS name, mig.outflow * 100.0 / pop.population_total AS out_rate, pop.net_change * 100.0 / pop.population_total AS change_rate FROM mig JOIN pop ON pop.area_code = mig.area) SELECT name, ROUND(out_rate, 2) AS out_rate, ROUND(change_rate, 2) AS change_rate FROM j WHERE out_rate < 7 ORDER BY out_rate DESC, name
```

```sql id=trend
WITH pop AS (SELECT COALESCE(area_code, '00000') AS area_code, year, population_total FROM e_stat.resident_registry.population WHERE resident_kind = 'total' AND (area_level = 'municipality' OR area_level = 'national')), mig AS (SELECT COALESCE(area, '00000') AS area, year, outflow FROM e_stat.migration.municipality_migration WHERE sex_code = '0' AND nationality_code = '60000' AND year <= 2025 AND ((area_level = 'municipality' AND area IN ('14382', '01400', '11229', '12233')) OR area_level = 'national')), r AS (SELECT mig.year, mig.area, mig.outflow * 100.0 / pop.population_total AS out_rate FROM mig JOIN pop ON pop.year = mig.year AND pop.area_code = mig.area) SELECT year, ROUND(MAX(out_rate) FILTER (WHERE area = '14382'), 2) AS hakone, ROUND(MAX(out_rate) FILTER (WHERE area = '01400'), 2) AS kutchan, ROUND(MAX(out_rate) FILTER (WHERE area = '12233'), 2) AS tomisato, ROUND(MAX(out_rate) FILTER (WHERE area = '11229'), 2) AS wako, ROUND(MAX(out_rate) FILTER (WHERE area = '00000'), 2) AS nationwide FROM r GROUP BY year ORDER BY year
```
