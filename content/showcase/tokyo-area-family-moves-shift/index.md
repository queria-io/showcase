---
title: 埼玉・千葉・神奈川の子どもの転入超過は、3年で7,547人から139人に減った
description: 0〜14歳の転入超過を1都3県で集計すると、埼玉・千葉・神奈川の合計は2022年の7,547人から2025年は139人に減り、東京都の多摩は5,086人で12年で最も多くなりました。
publishedAt: 2026-10-17
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 人口移動
  - 子育て
  - 首都圏
  - 住宅
datasets:
  - queria/e_stat
sources:
  - title: 住民基本台帳人口移動報告
    url: https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html
    publisher: 総務省統計局
agentHint: 埼玉・千葉・神奈川の市区町村ごとに、0〜14歳と30〜44歳の転入超過数（日本人移動者）を2014年から2025年まで毎年並べて、2022年から2025年に減った人数の大きい順に出して
socialAnnounce: |-
  埼玉・千葉・神奈川の子どもの転入超過は2022年7,547人から2025年139人に。多摩は5,086人で12年で最多です。

  郊外の市の人口見通しや施設計画の見直しに。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています
---

0〜14歳の子どもについて、埼玉県・千葉県・神奈川県の3県に転入した人数から転出した人数を引くと、2022年は7,547人、2025年は139人でした。3県では、2023年からの3年で、転入する子どもと転出する子どもの数がほぼ同じになりました。同じ2025年に、東京都の多摩・島しょ地域ではこの差が5,086人で、2014年以降で最も大きくなっています。大阪市・名古屋市の周辺では、このような減少はありませんでした。

首都圏では、子育て世帯は住宅が狭くなると東京23区を出て、家賃や住宅価格の安い埼玉・千葉・神奈川へ移ると考えられてきました。郊外の市では、子育て世帯の転入が、人口の見通しや保育所・学校の整備計画の前提になっています。

## 埼玉・千葉・神奈川の子どもの転入超過は、2022年から3年でほぼゼロになった

使うのは総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html)の市区町村別・年齢5歳階級別の表で、e-Stat の `municipality_migration_age` に収録されています。住民票の異動届にもとづく実績で、1月から12月までの1年間に市区町村をまたいで住所を移した人を集計しています。同じ市区町村の中での引っ越しと、国外との出入りは入りません。

ここでは0〜4歳・5〜9歳・10〜14歳の3階級を合計して「子ども」とし、転入者数から転出者数を引いた転入超過数を集計します。子どもは親と一緒に移るので、子どもの転入超過は子育て世帯の移動の方向を表します。2014年から続いているのは日本人の移動だけなので、すべて日本人移動者の値です。東京都は、特別区部（23区）とそれ以外の市町村（多摩と島しょ）に分けました。島しょの町村は人口が少なく、合計への影響は小さいので、以下では多摩と呼びます。

```chart caption="0〜14歳の転入超過数（日本人移動者、1都3県の地域別、2014〜2025年）"
{
  "layer": [
    {
      "data": {"name": "kids_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"three_pref\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ef4444",
        "strokeWidth": 3,
        "strokeDash": [6, 4],
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "three_pref", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "three_pref",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "埼玉・千葉・神奈川の計",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "埼玉県", "千葉県", "神奈川県", "多摩・島しょ", "東京23区"],
            "range": ["#ef4444", "#22c55e", "#f97316", "#7c3aed", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "kids_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"saitama\"]) ? 0 : 1",
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
          {"field": "saitama", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "saitama",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "埼玉県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "埼玉県", "千葉県", "神奈川県", "多摩・島しょ", "東京23区"],
            "range": ["#ef4444", "#22c55e", "#f97316", "#7c3aed", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "kids_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"chiba\"]) ? 0 : 1",
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
          {"field": "chiba", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "chiba",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "千葉県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "埼玉県", "千葉県", "神奈川県", "多摩・島しょ", "東京23区"],
            "range": ["#ef4444", "#22c55e", "#f97316", "#7c3aed", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "kids_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"kanagawa\"]) ? 0 : 1",
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
          {"field": "kanagawa", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "kanagawa",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "神奈川県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "埼玉県", "千葉県", "神奈川県", "多摩・島しょ", "東京23区"],
            "range": ["#ef4444", "#22c55e", "#f97316", "#7c3aed", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "kids_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tama\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tama", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tama",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "多摩・島しょ",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "埼玉県", "千葉県", "神奈川県", "多摩・島しょ", "東京23区"],
            "range": ["#ef4444", "#22c55e", "#f97316", "#7c3aed", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "kids_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ku23\"]) ? 0 : 1",
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
          {"field": "ku23", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "ku23",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "東京23区",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "埼玉県", "千葉県", "神奈川県", "多摩・島しょ", "東京23区"],
            "range": ["#ef4444", "#22c55e", "#f97316", "#7c3aed", "#3b82f6", "#94a3b8"]
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

埼玉県・千葉県・神奈川県の3県を合わせた子どもの転入超過は、2014年の3,491人から増え、コロナ禍の2021年に7,528人、2022年に7,547人となりました。2022年は収録期間の12年で最も多い年です。その後は2023年に5,050人、2024年に2,498人、2025年に139人と、3年続けて大きく減りました。2025年は埼玉県が858人、千葉県が1,506人で、神奈川県は2,225人の転出超過です。

23区では、子どもの転出超過が2021年の16,434人から2025年の7,374人へ半分以下に減り、コロナ禍の前の2019年（7,042人）とほぼ同じ水準に戻りました。多摩だけは反対に、2023年の3,330人から2024年に4,121人、2025年に5,086人と増えています。2023年まではどの年も3県の合計が多摩を上回っていましたが、2024年に逆転し、2025年には3県を合わせても多摩の3%に届きません。コロナ禍の前の2019年と比較すると、23区の子どもの転出超過は7,042人と7,374人でほぼ同じなのに、3県の転入超過は5,553人から139人に減り、多摩は3,441人から5,086人に増えています。23区から転出する子どもの数は変わらず、転入超過が多い地域が3県から多摩に変わりました。この表には転入元と転出先がないので、23区から3県へ移る家族が減ったのか、ほかの地域から3県へ来る家族が減ったのかは区別できません。

```sql
SELECT year AS 年, ku23 AS 東京23区, tama AS 多摩・島しょ, saitama AS 埼玉県, chiba AS 千葉県, kanagawa AS 神奈川県, three_pref AS 埼玉・千葉・神奈川の計 FROM kids_trend
```

## 30〜44歳の転入超過も、2025年は多摩が3県の合計を上回った

子どもと一緒に移る親の年齢として、30〜34歳・35〜39歳・40〜44歳を合計した30〜44歳の転入超過も集計しました。この年齢には子どものいない人も含まれますが、増減の方向は子どもと一致します。

```chart caption="30〜44歳の転入超過数（日本人移動者、2014〜2025年）"
{
  "layer": [
    {
      "data": {"name": "parents_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"three_pref\"]) ? 0 : 1",
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
          {"field": "three_pref", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "three_pref",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "埼玉・千葉・神奈川の計",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "多摩・島しょ", "東京23区"],
            "range": ["#22c55e", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "parents_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tama\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tama", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tama",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "多摩・島しょ",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "多摩・島しょ", "東京23区"],
            "range": ["#22c55e", "#3b82f6", "#94a3b8"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "parents_trend"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"ku23\"]) ? 0 : 1",
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
          {"field": "ku23", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "ku23",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "東京23区",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川の計", "多摩・島しょ", "東京23区"],
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

埼玉・千葉・神奈川の3県の30〜44歳の転入超過は、2021年の18,945人をピークに、2025年は5,747人まで減りました。多摩は2025年に6,941人で、2014年以降で最も多く、2014年以降で初めて3県の合計を上回っています。23区の30〜44歳はコロナ禍の前の2019年にはほぼ差し引きゼロ（60人の転入超過）でしたが、2021年に32,372人の転出超過となり、2025年も10,392人の転出超過が続いています。23区から転出する30〜44歳はコロナ禍の前より多いままで、その転入先として増えているのは多摩です。

## 大阪市・名古屋市の周辺では、子どもの転入超過は減っていない

子どもの数が減っているので、引っ越す子どもも年々少なくなっています。全国の市区町村の0〜14歳の転入者数は2022年の464,572人から2025年は386,120人に、16.9%減りました。この減少だけでは、3県の転入超過が98%減ったことは説明できません。大阪市・名古屋市の周辺と比較しました。

```chart caption="0〜14歳の転入超過数（日本人移動者、大都市の周辺の比較、2014〜2025年）"
{
  "layer": [
    {
      "data": {"name": "metro_compare"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"tokyo_suburbs\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 3,
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 36}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "tokyo_suburbs", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "tokyo_suburbs",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "埼玉・千葉・神奈川",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川", "大阪市以外の大阪府と滋賀・京都・兵庫・奈良", "名古屋市以外の愛知県"],
            "range": ["#22c55e", "#ec4899", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "metro_compare"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"osaka_suburbs\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#ec4899",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "osaka_suburbs", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "osaka_suburbs",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "大阪市以外の大阪府と滋賀・京都・兵庫・奈良",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川", "大阪市以外の大阪府と滋賀・京都・兵庫・奈良", "名古屋市以外の愛知県"],
            "range": ["#22c55e", "#ec4899", "#64748b"]
          },
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "metro_compare"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"nagoya_suburbs\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#64748b",
        "invalid": "break-paths-show-domains",
        "point": {"filled": true, "size": 25}
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "nagoya_suburbs", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年", "format": "d"}
        },
        "y": {
          "field": "nagoya_suburbs",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "転入超過数（人）", "grid": true}
        },
        "color": {
          "datum": "名古屋市以外の愛知県",
          "type": "nominal",
          "scale": {
            "domain": ["埼玉・千葉・神奈川", "大阪市以外の大阪府と滋賀・京都・兵庫・奈良", "名古屋市以外の愛知県"],
            "range": ["#22c55e", "#ec4899", "#64748b"]
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

大阪市以外の大阪府と、滋賀・京都・兵庫・奈良を合わせた子どもの転入超過は、2022年の4,872人に対して2025年は4,446人で、ほぼ横ばいです。名古屋市以外の愛知県は2022年の55人から2025年の353人へ増えています。名古屋市以外の愛知県は2021年まで毎年わずかな転出超過でしたが、2022年以降は減っていません。3つの大都市圏のうち、子どもの転入超過が大きく減ったのは東京の隣の3県だけです。

## 大きく減ったのは、2020〜2022年に子どもの転入超過が多かった市

1都3県の市区町村ごとに、2020〜2022年の3年間と2023〜2025年の3年間で子どもの転入超過の合計を比較しました。1年ごとの値は増減が大きいので、3年分を合計しています。23区は上の図で示したので除いています。政令市は市全体の値です。基準にした2020〜2022年はコロナ禍の時期で、3県の子どもの転入超過が12年で最も多かった期間なので、ここでの減少には、その時期に一時的に増えた分が元に戻った分も含まれます。

```chart caption="0〜14歳の転入超過数の変化（2023〜2025年の合計 − 2020〜2022年の合計、1都3県の市区町村、23区を除く）"
{
  "height": 600,
  "layer": [
    {
      "data": {"name": "muni_increase"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "変化（人）", "grid": true}
        },
        "y": {
          "field": "label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "増えた10市",
          "type": "nominal",
          "scale": {"domain": ["増えた10市", "減った10市"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "muni_decline"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "label", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "変化（人）", "grid": true}
        },
        "y": {
          "field": "label",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": null},
          "sort": null
        },
        "color": {
          "datum": "減った10市",
          "type": "nominal",
          "scale": {"domain": ["増えた10市", "減った10市"], "range": ["#3b82f6", "#ef4444"]},
          "title": null
        }
      }
    }
  ],
  "config": {"legend": {"orient": "bottom"}}
}
```

最も大きく減ったのはさいたま市で、2020〜2022年の4,530人から2023〜2025年は2,322人へ2,208人減りました。横浜市は401人の転入超過から1,544人の転出超過へ、流山市は2,248人から406人へ、藤沢市は1,800人から315人へ、印西市は2,130人から822人へと続きます。5市を合わせた減少は8,788人です。2020〜2022年に3県で子どもの転入超過が多かった上位5市はさいたま市・流山市・印西市・柏市・藤沢市で、このうち柏市を除く4市が、減った人数の上位5市に入っています。

増えた上位10市のうち6つは多摩の市で、最も大きい町田市は2,223人から2,791人へ568人増えました。増えた人数は減った人数よりずっと少なく、10市を合わせても3,326人です。埼玉・千葉・神奈川の150市区町村のうち89で、子どもの転入超過が減っています。

```sql
SELECT label AS 市区町村, before_sum AS "2020〜2022年", after_sum AS "2023〜2025年", diff AS 変化 FROM muni_change_table
```

## 郊外の市の子育て施策の担当者が確認すること

- 2020〜2022年に子どもの転入超過が多かった市ほど、計画を見直す必要があります。さいたま市・流山市・印西市・藤沢市はこの3年間で1,800人以上の転入超過がありましたが、2023〜2025年はさいたま市で約半分、印西市で4割弱、流山市と藤沢市では2割弱に減りました。人口の将来見通しや保育所・学校の整備計画がこの時期の転入超過を前提にしているなら、その前提は変わっています
- 隣接する市と比較して、減少が自分の市だけか、周辺の市にも共通するかを確認します。周辺の市でも減っているなら、市の施策の効果より、首都圏全体の移動の変化によるものと考えられます

## データの出典

本記事は総務省統計局の[住民基本台帳人口移動報告](https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html)の市区町村別・年齢5歳階級別の転入者数・転出者数（日本人移動者、2014〜2025年）を、2026年10月17日時点で集計しています。

Queriaは、住民基本台帳人口移動報告をはじめとする官公庁のオープンデータを、列名・単位・文字コードを統一し、テーブルと列の説明を付けて公開しています。本記事で使った[市区町村別・年齢別の人口移動テーブル](/datasets/queria/e_stat/migration/municipality_migration_age)から、自分の市と周辺の市の子どもや30〜44歳の転入超過を年ごとに確認できます。

```sql id=kids_trend
-- 0〜14歳（0〜4・5〜9・10〜14歳）の転入超過数を1都3県の地域別に年ごとに足す（日本人移動者・男女計・市区町村の粒度）
SELECT year,
  SUM(net_inflow) FILTER (WHERE area = '13100') AS ku23,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) = '13' AND area <> '13100') AS tama,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) = '11') AS saitama,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) = '12') AS chiba,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) = '14') AS kanagawa,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) IN ('11', '12', '14')) AS three_pref
FROM e_stat.migration.municipality_migration_age
WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
  AND age_code IN ('201', '202', '203')
  AND LEFT(area, 2) IN ('11', '12', '13', '14')
  AND year BETWEEN 2014 AND 2025
GROUP BY year
ORDER BY year
```

```sql id=parents_trend
-- 30〜44歳（30〜34・35〜39・40〜44歳）の転入超過数を地域別に年ごとに足す（日本人移動者・男女計）
SELECT year,
  SUM(net_inflow) FILTER (WHERE area = '13100') AS ku23,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) = '13' AND area <> '13100') AS tama,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) IN ('11', '12', '14')) AS three_pref
FROM e_stat.migration.municipality_migration_age
WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
  AND age_code IN ('207', '208', '209')
  AND LEFT(area, 2) IN ('11', '12', '13', '14')
  AND year BETWEEN 2014 AND 2025
GROUP BY year
ORDER BY year
```

```sql id=metro_compare
-- 大都市の周辺の0〜14歳の転入超過数（日本人移動者）。関西は大阪市（27100）以外の大阪府と滋賀・京都・兵庫・奈良、中京は名古屋市（23100）以外の愛知県
SELECT year,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) IN ('11', '12', '14')) AS tokyo_suburbs,
  SUM(net_inflow) FILTER (WHERE (LEFT(area, 2) = '27' AND area <> '27100') OR LEFT(area, 2) IN ('25', '26', '28', '29')) AS osaka_suburbs,
  SUM(net_inflow) FILTER (WHERE LEFT(area, 2) = '23' AND area <> '23100') AS nagoya_suburbs
FROM e_stat.migration.municipality_migration_age
WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
  AND age_code IN ('201', '202', '203')
  AND year BETWEEN 2014 AND 2025
GROUP BY year
ORDER BY year
```

```sql id=kids_moves_total
-- 全国の市区町村の0〜14歳の転入者数（日本人移動者）。子どもの移動そのものの減り方を本文で示すための値で、プロットはしない
SELECT year, SUM(inflow) AS kids_inflow
FROM e_stat.migration.municipality_migration_age
WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
  AND age_code IN ('201', '202', '203')
  AND year BETWEEN 2014 AND 2025
GROUP BY year
ORDER BY year
```

```sql id=muni_change_table
-- 1都3県の市区町村（23区は特別区部として1単位、政令市は市全体）の0〜14歳の転入超過数を2020〜2022年と2023〜2025年の3年合計で比べる。23区は除く
WITH s AS (
  SELECT area, ANY_VALUE(area_name) AS area_name,
    SUM(net_inflow) FILTER (WHERE year BETWEEN 2020 AND 2022) AS before_sum,
    SUM(net_inflow) FILTER (WHERE year BETWEEN 2023 AND 2025) AS after_sum
  FROM e_stat.migration.municipality_migration_age
  WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
    AND age_code IN ('201', '202', '203')
    AND LEFT(area, 2) IN ('11', '12', '13', '14') AND area <> '13100'
  GROUP BY area
)
SELECT CASE LEFT(area, 2) WHEN '11' THEN '埼玉県' WHEN '12' THEN '千葉県' WHEN '13' THEN '東京都' ELSE '神奈川県' END || ' ' || area_name AS label,
  before_sum, after_sum, after_sum - before_sum AS diff
FROM s
ORDER BY diff, area
```

```sql id=muni_decline
-- 3年合計の変化が最も小さい（最も減った）10市。図は上から増えた順に並べるので、減った側は減りの小さい順（rn の大きい順）に渡す
WITH s AS (
  SELECT area, ANY_VALUE(area_name) AS area_name,
    SUM(net_inflow) FILTER (WHERE year BETWEEN 2023 AND 2025) - SUM(net_inflow) FILTER (WHERE year BETWEEN 2020 AND 2022) AS diff
  FROM e_stat.migration.municipality_migration_age
  WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
    AND age_code IN ('201', '202', '203')
    AND LEFT(area, 2) IN ('11', '12', '13', '14') AND area <> '13100'
  GROUP BY area
), r AS (
  SELECT area_name || '（' || CASE LEFT(area, 2) WHEN '11' THEN '埼玉' WHEN '12' THEN '千葉' WHEN '13' THEN '東京' ELSE '神奈川' END || '）' AS label,
    diff, ROW_NUMBER() OVER (ORDER BY diff, area) AS rn
  FROM s
)
SELECT label, diff FROM r WHERE rn <= 10 ORDER BY rn DESC
```

```sql id=muni_increase
-- 3年合計の変化が最も大きい（最も増えた）10市。図の先頭に置き、増えた順（rn の小さい順）に渡す
WITH s AS (
  SELECT area, ANY_VALUE(area_name) AS area_name,
    SUM(net_inflow) FILTER (WHERE year BETWEEN 2023 AND 2025) - SUM(net_inflow) FILTER (WHERE year BETWEEN 2020 AND 2022) AS diff
  FROM e_stat.migration.municipality_migration_age
  WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
    AND age_code IN ('201', '202', '203')
    AND LEFT(area, 2) IN ('11', '12', '13', '14') AND area <> '13100'
  GROUP BY area
), r AS (
  SELECT area_name || '（' || CASE LEFT(area, 2) WHEN '11' THEN '埼玉' WHEN '12' THEN '千葉' WHEN '13' THEN '東京' ELSE '神奈川' END || '）' AS label,
    diff, ROW_NUMBER() OVER (ORDER BY diff DESC, area) AS rn
  FROM s
)
SELECT label, diff FROM r WHERE rn <= 10 ORDER BY rn
```

```sql id=muni_summary
-- 本文の件数・合計の裏付け（プロットはしない）。3県で変化がマイナスの市区町村数、減少上位5市の減少の合計、増加上位10の増加の合計
WITH s AS (
  SELECT area,
    SUM(net_inflow) FILTER (WHERE year BETWEEN 2023 AND 2025) - SUM(net_inflow) FILTER (WHERE year BETWEEN 2020 AND 2022) AS diff
  FROM e_stat.migration.municipality_migration_age
  WHERE area_level = 'municipality' AND nationality_code = '61000' AND sex_code = '0'
    AND age_code IN ('201', '202', '203')
    AND LEFT(area, 2) IN ('11', '12', '13', '14') AND area <> '13100'
  GROUP BY area
), r AS (
  SELECT area, diff,
    ROW_NUMBER() OVER (ORDER BY diff, area) AS rn_down,
    ROW_NUMBER() OVER (ORDER BY diff DESC, area) AS rn_up
  FROM s
)
SELECT
  COUNT(*) FILTER (WHERE LEFT(area, 2) IN ('11', '12', '14')) AS three_pref_units,
  COUNT(*) FILTER (WHERE LEFT(area, 2) IN ('11', '12', '14') AND diff < 0) AS three_pref_decreased,
  SUM(diff) FILTER (WHERE rn_down <= 5) AS top5_decline_sum,
  SUM(diff) FILTER (WHERE rn_up <= 10) AS top10_increase_sum,
  COUNT(*) FILTER (WHERE rn_up <= 10 AND LEFT(area, 2) = '13') AS top10_increase_tokyo
FROM r
```
