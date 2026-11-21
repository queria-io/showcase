---
title: 2023年の空き家率は13.8%で、1978年の1.8倍になった
description: 2023年の空き家率は過去最高の13.8%で、1978年の1.8倍です。都道府県別では徳島県の21.3%から埼玉県の9.3%まで2.3倍の差があります。空き家の戸数は東京都の896,500戸が最も多く、2018年から2023年に東京都は10.7%増え、埼玉県・神奈川県は減りました。
publishedAt: 2026-03-05
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 空き家
  - 住宅
  - 都道府県
datasets:
  - queria/e_stat
  - queria/nlftp
sources:
  - title: 社会・人口統計体系
    url: https://www.stat.go.jp/data/ssds/index.html
    publisher: 総務省統計局
  - title: 住宅・土地統計調査
    url: https://www.stat.go.jp/data/jyutaku/index.html
    publisher: 総務省統計局
  - title: 国土数値情報 行政区域データ
    url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html
    publisher: 国土交通省
agentHint: 空き家数（H110202）と居住世帯あり住宅数（H1101）を2018年と2023年で県別に並べて、住んでいる住宅が減った県で空き家がどれだけ増えたか出して
socialAnnounce: |-
  日本の空き家率は13.8%。
  7軒に1軒が空き家です。

  最も高い徳島県は21.3%、最も低い埼玉県は9.3%。
  戸数でみると最多は東京都の896,500戸で、率では44位です。

  2018年から2023年の5年では、東京都で10.7%増える一方、埼玉県と神奈川県では減りました。
---

総務省の[住宅・土地統計調査](https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf)によると、2023年の日本の空き家率（総住宅数に占める空き家の割合）は13.8%で、過去最高でした。住宅の7軒に1軒が空き家です。1978年の7.6%から1.8倍になり、空き家の戸数は3.4倍に増えています。都道府県別では徳島県の21.3%から埼玉県の9.3%まで2.3倍の差があります。空き家の戸数が最も多いのは東京都の896,500戸で、2018年から2023年に10.7%増えました。同じ首都圏の埼玉県と神奈川県では空き家が減っています。

2023年12月には、[空家等対策の推進に関する特別措置法](https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000035.html)の改正法が施行され、放置された空き家を「管理不全空家等」として扱う仕組みが加わりました。e-Stat「[社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)」の都道府県別住宅データを使い、空き家率の長期推移と地域差、空き家の戸数、2018年から2023年の増減を集計しました。

## 空き家率は45年で1.8倍、戸数は3.4倍になった

使ったのは「居住」分野の3つの指標です。いずれも単位は戸で、10月1日現在の値です。

| コード  | 内容               |
| ------- | ------------------ |
| H1100   | 総住宅数           |
| H1101   | 居住世帯あり住宅数 |
| H110202 | 空き家数           |

空き家率は 空き家数（H110202）÷ 総住宅数（H1100）× 100 で計算します。元の住宅・土地統計調査は5年ごとの調査で、この3指標はいずれも1978年から2023年までの10時点が収録されています。この調査でいう空き家には、賃貸用の空き家・売却用の空き家・別荘などの二次的住宅・それらを除く空き家の4区分が含まれます。放置されて問題になるのは主に「賃貸・売却用及び二次的住宅を除く空き家」ですが、この内訳は `h_pref_housing` に収録されていないため、以下の数字はいずれも4区分の合計です。

```sql
SELECT * FROM coverage
```

```chart
{
  "layer": [
    {
      "data": {"name": "vacancy_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"vacancy_rate\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 64, "color": "#f97316"}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "vacancy_rate", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "vacancy_rate",
          "type": "quantitative",
          "scale": {"domain": [0, 16], "zero": false, "nice": false},
          "axis": {"title": "空き家率（%）", "grid": true}
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

1978年に7.6%だった空き家率は、2023年には13.8%で、1.8倍になりました。最も大きく上がったのは1993年の9.8%から1998年の11.5%への期間で、2008年以降は13%台で推移しています。

空き家率は割合なので、分母の総住宅数も増えていると、上がり方は小さく見えます。総住宅数・居住世帯あり住宅数・空き家数の3つを、1978年を100とした指数で並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "stock_index"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tot_idx\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "tot_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tot_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "指数（1978年=100）", "grid": true}
        },
        "color": {
          "datum": "総住宅数",
          "type": "nominal",
          "scale": {
            "domain": ["総住宅数", "居住世帯あり住宅数", "空き家数"],
            "range": ["#94a3b8", "#3b82f6", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "stock_index"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"occ_idx\"]) ? 0 : 1",
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
          {"field": "occ_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "occ_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "指数（1978年=100）", "grid": true}
        },
        "color": {
          "datum": "居住世帯あり住宅数",
          "type": "nominal",
          "scale": {
            "domain": ["総住宅数", "居住世帯あり住宅数", "空き家数"],
            "range": ["#94a3b8", "#3b82f6", "#f97316"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "stock_index"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"vac_idx\"]) ? 0 : 1",
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
          {"field": "year", "type": "quantitative"},
          {"field": "vac_idx", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "vac_idx",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "指数（1978年=100）", "grid": true}
        },
        "color": {
          "datum": "空き家数",
          "type": "nominal",
          "scale": {
            "domain": ["総住宅数", "居住世帯あり住宅数", "空き家数"],
            "range": ["#94a3b8", "#3b82f6", "#f97316"]
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

2023年の指数は、総住宅数が183.5、居住世帯あり住宅数が172.9、空き家数は336.0です。空き家の戸数は1978年の2,679,200戸から2023年の9,001,600戸に増えています。空き家率が1.8倍なのは、分母の総住宅数も45年で1.8倍になったためで、空き家の戸数は3.4倍に増えています。

## 2023年の空き家率は、徳島県の21.3%から埼玉県の9.3%まで2.3倍の差がある

2023年の空き家率を47都道府県で並べました。全国の行は除いています。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "rate_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家率（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "上位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rate_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家率（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "中間",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "rate_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "rate", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "rate",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家率（%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "下位10",
          "type": "nominal",
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#f97316", "#fdba74", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

徳島県（21.3%）と和歌山県（21.2%）が上位2県で、いずれも5軒に1軒が空き家です。鹿児島県（20.5%）、山梨県（20.4%）、高知県（20.3%）、長野県（20.1%）が続きます。上位10県には徳島県・高知県・愛媛県（19.8%）・香川県（18.6%）と四国4県がすべて入っています。

上位10県の残りは山口県（19.4%）と大分県（19.1%）です。最も低いのは埼玉県（9.3%）で、沖縄県（9.4%）、神奈川県（9.8%）、東京都（10.9%）、千葉県（12.3%）と、首都圏の1都3県がすべて下位10県に入ります。最も高い県と低い県の差は2.3倍です。都道府県別の値は標本調査からの推計値なので、徳島県と和歌山県の0.1ポイント差のような隣り合う順位の違いは、このデータでは判定できません。

## 空き家率の高い10県は、四国4県を除くと互いに離れている

都道府県別の空き家率を地図にしました。

```map
type: map
layers:
  - from: vacancy_map
    geojson: geojson
    color: vacancy_rate
    label: pref_name
    name: "空き家率（%）"
lng: 137
lat: 36.5
zoom: 4
```

濃い色の10県は、四国4県が隣り合うほかは、和歌山県・山梨県・長野県・鹿児島県・大分県・山口県と互いに離れています。淡い色の10県は、関東南部の1都3県が隣り合うほかは、愛知県・京都府・滋賀県・福岡県・宮城県・沖縄県と互いに離れています。

## 空き家の戸数が最も多いのは東京都の896,500戸で、空き家率では44位

同じ2023年のデータを、空き家の戸数で並べ直しました。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "count_top"},
      "mark": {"type": "bar", "color": "#f97316"},
      "encoding": {
        "tooltip": [
          {"field": "vacant", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "vacant",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家数（戸）", "grid": true}
        },
        "y": {
          "field": "pref",
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

最も多いのは東京都の896,500戸で、空き家率では44位です。大阪府701,900戸（率34位）、神奈川県467,100戸（率45位）、北海道451,900戸（率25位）が続きます。空き家率が最も低い埼玉県も、戸数では330,400戸で9位です。

空き家率の上位5県の戸数は次のとおりです。

```sql
SELECT * FROM count_rate_leaders
```

空き家率1位の徳島県は83,000戸で戸数では37位、5位の高知県は78,700戸で39位です。3位の鹿児島県だけが184,200戸で14位に入ります。

## 2018年から2023年に、東京都の空き家は10.7%増え、埼玉県・神奈川県は減った

全国の空き家は2018年の8,488,600戸から2023年の9,001,600戸へ、5年で513,000戸増えました。増加率は6.0%ですが、総住宅数も同じ期間に増えているため、空き家率は13.6%から13.8%へ0.2ポイントの上昇です。都道府県別に、この5年の空き家数の増減率を並べました。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "change_up"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "change_pct", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "change_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家数の増減率（2018年→2023年、%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "増加",
          "type": "nominal",
          "scale": {"domain": ["増加", "減少"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "change_down"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "change_pct", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "change_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "空き家数の増減率（2018年→2023年、%）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "減少",
          "type": "nominal",
          "scale": {"domain": ["増加", "減少"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        }
      }
    }
  ]
}
```

図の増減率は標本による推計値どうしの差なので、小さい増減は誤差と区別できません。総務省が公表する[推定値の大きさ別標準誤差率](https://www.stat.go.jp/data/jyutaku/2023/zuhyou/sui_01_chiiki.xlsx)の「都道府県」シート（甲・乙両調査票）を、各県の2018年と2023年の空き家数の大きさに対数補間で当てはめ、両年の誤差を独立として合成し、1.96倍しました。2023年調査の表を2018年の推計にも当てはめた近似です。この方法で計算した増減率の95%の区間は、県によって±2ポイント台（大阪府）から±8ポイント台（鳥取県）まで差があります。

この区間を超えて増減したのは47都道府県のうち34県で、そのうち32県は増加です。減ったのは埼玉県（-4.6%）と神奈川県（-3.6%）の2県だけで、沖縄県（-3.7%）・山梨県（-3.1%）・大阪府（-1.1%）・茨城県（-0.5%）の減少は区間の内側にあります。福島県の増減には、2018年の調査で抽出の対象から外れていた福島第一原発事故の避難地域（[2018年の調査](https://www.stat.go.jp/data/jyutaku/2018/pdf/g_gaiyou.pdf)では大熊町・双葉町の全域と、南相馬市・富岡町・浪江町・葛尾村・飯舘村の一部）が、2023年に対象に戻った分が含まれます。

同じ首都圏でも東京都は10.7%増え、5年で809,900戸から896,500戸になりました。総住宅数の増加率は東京都6.9%、神奈川県5.8%、埼玉県5.0%で、どれも同じくらいです。増加率が最も大きいのは北海道（19.0%）で、大分県（18.2%）、福井県（18.0%）、富山県（16.2%）、秋田県（14.3%）が続きます。空き家率は北海道と福井県が15.6%、富山県が14.7%、秋田県が15.8%で、いずれも47都道府県の中位です。大分県は空き家率19.1%で、空き家率と増加率の両方が上位です。秋田県は総住宅数が1.1%減るなかで空き家が14.3%増えました。

```sql
SELECT * FROM metro_decomposition
```

神奈川県は総住宅数が261,500戸増え、居住世帯あり住宅数は271,500戸増えました。埼玉県も総住宅数の170,400戸に対して居住世帯あり住宅数は181,700戸増えています。増えた住宅の数より多くの世帯が入居し、空き家は減りました。東京都は総住宅数が529,800戸増えたのに対し、居住世帯あり住宅数の増加は429,900戸で、差はおよそ10万戸、そのうち86,600戸が空き家の増加です。千葉県も総住宅数の161,300戸に対して居住世帯あり住宅数は147,100戸で、東京都と同じく空き家は3.0%増えています（増減率は誤差の区間の内側です）。全国では総住宅数の2,639,300戸増に対して、居住世帯あり住宅数の増加は2,048,700戸でした。総住宅数の増加率がほぼ同じ4都県で空き家の増減が分かれたのは、入居した世帯の増加が住宅の増加を上回ったかどうかによるものです。

## まとめ

- 全国の空き家率は1978年の7.6%から2023年の13.8%へ45年で1.8倍。総住宅数も1.8倍になっているので、空き家の戸数は2,679,200戸から9,001,600戸へ3.4倍に増えている
- 2023年の空き家率は徳島県の21.3%から埼玉県の9.3%まで2.3倍の差がある。上位10県には四国4県がすべて入り、下位10県には首都圏の1都3県がすべて入る
- 空き家が最も多いのは東京都の896,500戸で、空き家率では44位。空き家率1位の徳島県は83,000戸で戸数では37位
- 2018年から2023年で全国の空き家は513,000戸増えた。標本誤差を超えて増減した34県のうち32県は増加で、減ったのは埼玉県（-4.6%）と神奈川県（-3.6%）の2県だけ。同じ首都圏の東京都は10.7%増えている。総住宅数の増加率は東京都6.9%・神奈川県5.8%・埼玉県5.0%と近く、空き家の増減を分けたのは居住世帯あり住宅数の増え方

## データの出典

本記事は e-Stat [社会・人口統計体系](https://www.stat.go.jp/data/ssds/index.html)（総務省統計局）の `e_stat.ssds.h_pref_housing` を2026-09-04時点で集計しています。使った分類コードは総住宅数が H1100、居住世帯あり住宅数が H1101、空き家数が H110202 で、いずれも単位は戸、収録は1978年から2023年までの10時点です。元データは総務省統計局の[住宅・土地統計調査](https://www.stat.go.jp/data/jyutaku/index.html)で、5年ごとに10月1日現在で、国勢調査区から抽出した単位区を対象に実施される標本調査です。指標の定義は[項目定義 H 居住](https://www.e-stat.go.jp/koumoku/koumoku_teigi/H)によります。空き家の4区分の名称は[2023年調査の結果](https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf)の名称を使っています。増減の判定に使った標準誤差率は同じ調査の[推定値の大きさ別標準誤差率](https://www.stat.go.jp/data/jyutaku/2023/zuhyou/sui_01_chiiki.xlsx)です。地図の県境は国土交通省の[国土数値情報 行政区域データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)（`nlftp.boundary.prefecture`）で、描画のため `ST_Simplify` で簡略化しています。

Queriaは、官公庁のオープンデータを、列名・単位・文字コードを統一し、カテゴリコードと項目の説明を付けて公開しています。本記事で使った[都道府県別の住宅・空き家テーブル](/datasets/queria/e_stat/ssds/h_pref_housing)から、関心のある地域の空き家率と戸数を1978年から集計できます。

```sql id=coverage
SELECT cat01 AS "分類コード", ANY_VALUE(unit) AS "単位", MIN(year) AS "収録開始", MAX(year) AS "収録最終", COUNT(DISTINCT year) AS "収録年数" FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H1101', 'H110202') AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY cat01 ORDER BY cat01
```

```sql id=vacancy_trend
WITH n AS (SELECT year, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year) SELECT year, ROUND(100.0 * vac / tot, 1) AS vacancy_rate FROM n WHERE tot > 0 ORDER BY year
```

```sql id=stock_index
WITH n AS (SELECT year, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H1101' THEN TRY_CAST(value AS DOUBLE) END) AS occ, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H1101', 'H110202') AND area_name = '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year), b AS (SELECT tot AS t0, occ AS o0, vac AS v0 FROM n WHERE year = 1978) SELECT n.year AS year, ROUND(100.0 * n.tot / b.t0, 1) AS tot_idx, ROUND(100.0 * n.occ / b.o0, 1) AS occ_idx, ROUND(100.0 * n.vac / b.v0, 1) AS vac_idx, CAST(n.tot AS BIGINT) AS total_dwellings, CAST(n.occ AS BIGINT) AS occupied, CAST(n.vac AS BIGINT) AS vacant FROM n CROSS JOIN b ORDER BY n.year
```

```sql id=rate_top
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name AS pref, ROUND(100.0 * vac / tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY vac / tot DESC, area_name) AS rn FROM d WHERE tot > 0) SELECT pref, rate FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=rate_mid
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name AS pref, ROUND(100.0 * vac / tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY vac / tot DESC, area_name) AS rn FROM d WHERE tot > 0) SELECT pref, rate FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=rate_bottom
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name AS pref, ROUND(100.0 * vac / tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY vac / tot DESC, area_name) AS rn FROM d WHERE tot > 0) SELECT pref, rate FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=vacancy_map
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name) SELECT p.prefecture_name AS pref_name, ST_AsGeoJSON(ST_Simplify(p.geometry, 0.01)) AS geojson, ROUND(100.0 * d.vac / d.tot, 1) AS vacancy_rate FROM nlftp.boundary.prefecture p JOIN d ON p.prefecture_name = d.area_name WHERE d.tot > 0
```

```sql id=count_top
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name AS pref, CAST(vac AS BIGINT) AS vacant, ROUND(100.0 * vac / tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY vac DESC, area_name) AS rn, RANK() OVER (ORDER BY vac / tot DESC) AS rate_rank FROM d WHERE tot > 0) SELECT pref, vacant, rate, rate_rank FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=count_rate_leaders
WITH d AS (SELECT area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY area_name), ranked AS (SELECT area_name AS pref, ROUND(100.0 * vac / tot, 1) AS rate, RANK() OVER (ORDER BY vac / tot DESC) AS rate_rank, CAST(vac AS BIGINT) AS vacant, RANK() OVER (ORDER BY vac DESC) AS count_rank FROM d WHERE tot > 0) SELECT pref AS "都道府県", rate AS "空き家率（%）", rate_rank AS "空き家率の順位", vacant AS "空き家数（戸）", count_rank AS "空き家数の順位" FROM ranked WHERE rate_rank <= 5 ORDER BY rate_rank
```

```sql id=change_up
WITH v AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H110202' AND year IN (2018, 2023) AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), t AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS tot FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H1100' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) > 0), t0 AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS tot FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H1100' AND year = 2018 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) > 0), ranked AS (SELECT a.area_name AS pref, ROUND(100.0 * (b.vac - a.vac) / a.vac, 1) AS change_pct, CAST(a.vac AS BIGINT) AS vacant_2018, CAST(b.vac AS BIGINT) AS vacant_2023, ROUND(100.0 * (t.tot - t0.tot) / t0.tot, 1) AS total_change_pct, ROUND(100.0 * b.vac / t.tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY (b.vac - a.vac) / a.vac DESC, a.area_name) AS rn FROM v a JOIN v b ON a.area_name = b.area_name AND a.year = 2018 AND b.year = 2023 JOIN t ON t.area_name = a.area_name JOIN t0 ON t0.area_name = a.area_name WHERE a.vac > 0) SELECT pref, change_pct, vacant_2018, vacant_2023, total_change_pct, rate FROM ranked WHERE change_pct >= 0 ORDER BY rn
```

```sql id=change_down
WITH v AS (SELECT year, area_name, TRY_CAST(value AS DOUBLE) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H110202' AND year IN (2018, 2023) AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) IS NOT NULL), t AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS tot FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H1100' AND year = 2023 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) > 0), t0 AS (SELECT area_name, TRY_CAST(value AS DOUBLE) AS tot FROM e_stat.ssds.h_pref_housing WHERE cat01 = 'H1100' AND year = 2018 AND area_name <> '全国' AND TRY_CAST(value AS DOUBLE) > 0), ranked AS (SELECT a.area_name AS pref, ROUND(100.0 * (b.vac - a.vac) / a.vac, 1) AS change_pct, CAST(a.vac AS BIGINT) AS vacant_2018, CAST(b.vac AS BIGINT) AS vacant_2023, ROUND(100.0 * (t.tot - t0.tot) / t0.tot, 1) AS total_change_pct, ROUND(100.0 * b.vac / t.tot, 1) AS rate, ROW_NUMBER() OVER (ORDER BY (b.vac - a.vac) / a.vac DESC, a.area_name) AS rn FROM v a JOIN v b ON a.area_name = b.area_name AND a.year = 2018 AND b.year = 2023 JOIN t ON t.area_name = a.area_name JOIN t0 ON t0.area_name = a.area_name WHERE a.vac > 0) SELECT pref, change_pct, vacant_2018, vacant_2023, total_change_pct, rate FROM ranked WHERE change_pct < 0 ORDER BY rn
```

```sql id=metro_decomposition
WITH d AS (SELECT year, area_name, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H1101' THEN TRY_CAST(value AS DOUBLE) END) AS occ, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H1101', 'H110202') AND year IN (2018, 2023) AND area_name IN ('全国', '東京都', '神奈川県', '埼玉県', '千葉県') GROUP BY year, area_name) SELECT a.area_name AS "地域", CAST(b.tot - a.tot AS BIGINT) AS "総住宅数の増加（戸）", CAST(b.occ - a.occ AS BIGINT) AS "居住世帯あり住宅数の増加（戸）", CAST(b.vac - a.vac AS BIGINT) AS "空き家数の増加（戸）", ROUND(100.0 * (b.tot - a.tot) / a.tot, 1) AS "総住宅数の増加率（%）", ROUND(100.0 * (b.occ - a.occ) / a.occ, 1) AS "居住世帯あり住宅数の増加率（%）", ROUND(100.0 * (b.vac - a.vac) / a.vac, 1) AS "空き家数の増加率（%）" FROM d a JOIN d b ON a.area_name = b.area_name AND a.year = 2018 AND b.year = 2023 ORDER BY (b.occ - a.occ) / a.occ DESC
```

```sql id=national_recent
WITH n AS (SELECT year, MAX(CASE WHEN cat01 = 'H1100' THEN TRY_CAST(value AS DOUBLE) END) AS tot, MAX(CASE WHEN cat01 = 'H110202' THEN TRY_CAST(value AS DOUBLE) END) AS vac FROM e_stat.ssds.h_pref_housing WHERE cat01 IN ('H1100', 'H110202') AND area_name = '全国' AND year IN (2018, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year) SELECT year, CAST(tot AS BIGINT) AS total_dwellings, CAST(vac AS BIGINT) AS vacant, ROUND(100.0 * vac / tot, 1) AS vacancy_rate FROM n ORDER BY year
```
