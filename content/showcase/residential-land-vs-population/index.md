---
title: 人口が減った市区町村の9割で宅地は増え、1人あたりの宅地面積は23年で17%広がった
description: 宅地面積と住民基本台帳人口を市区町村別に2000年度から2023年度まで集計しました。人口が減った1,420市区町村のうち1,296で宅地は増え、全国の1人あたりの宅地面積は123.9m²から144.8m²へ約17%広がっています。
publishedAt: 2026-09-07
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 宅地
  - 人口減少
  - 都市計画
datasets:
  - queria/e_stat
sources:
  - title: 令和6年度 固定資産の価格等の概要調書
    url: https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran08_r06_00.html
    publisher: 総務省
  - title: 住民基本台帳に基づく人口、人口動態及び世帯数
    url: https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html
    publisher: 総務省
  - title: 社会・人口統計体系 Ｂ 自然環境（市区町村）
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000020202
    publisher: 総務省統計局
  - title: 社会・人口統計体系 Ａ 人口・世帯（市区町村）
    url: https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000020201
    publisher: 総務省統計局
agentHint: e_stat.ssds.b_municipal_land の B120103（宅地）と e_stat.ssds.a_municipal_population の A2101（住民基本台帳人口）から、自分の市区町村の2000年度以降の宅地面積・人口・1人あたり宅地面積を年度ごとに出して。同じ県の他の市町村とも比べて
socialAnnounce: |-
  固定資産税の課税台帳にもとづく宅地面積と住民基本台帳人口を、市区町村別に並べました。

  人口が減った1,420市区町村のうち1,296で宅地は増えています。
  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2000年度から2023年度に人口が減った1,420市区町村のうち、1,296（91%）では宅地面積が増えていました。全国では、人口が2008年度をピークに減り始めたあとも宅地面積は増え続け、1人あたりの宅地面積は123.9m²から144.8m²へ約17%広がっています。1人あたりの宅地面積が減ったのは、47都道府県のうち東京都だけです。

道路や水道管は宅地の広がりに合わせて整備されるので、宅地の面積と人口の比率が変わると、住民1人あたりで維持する施設の量も変わります。この記事では、市町村が固定資産税を課すために毎年集計している宅地の面積と、住民基本台帳の人口を、同じ市区町村・同じ年度で比較します。使うのは総務省の[固定資産の価格等の概要調書](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran08_r06_00.html)と[住民基本台帳に基づく人口](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)で、どちらも e-Stat の社会・人口統計体系に、[自然環境](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000020202)と[人口・世帯](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000020201)として地域別・年度別で収録されています。

## 全国では、人口が減り始めたあとも宅地は増え続けている

宅地の面積は、社会・人口統計体系の自然環境（`b_pref_land` / `b_municipal_land`）にある「評価総地積」を使います。市町村が固定資産税の課税対象として評価した土地の面積で、地目ごとに次の3つが1975年度から収録されています。

| コード  | 内容               |
| ------- | ------------------ |
| B120101 | 評価総地積（田）   |
| B120102 | 評価総地積（畑）   |
| B120103 | 評価総地積（宅地） |

山林・牧場・原野・その他の4つも同じ体系にありますが、収録は2007年度までです。

宅地（`B120103`）には、住宅の敷地のほか、店舗・工場・事務所などの建物が建っている土地と、その利用に必要な土地が含まれます。国や自治体が持つ公有地・公共用地、学校用地、境内地などは固定資産税がかからないので、この面積には入りません。

人口は同じ体系の人口・世帯（`a_pref_population` / `a_municipal_population`）にある住民基本台帳人口（`A2101`）を使います。住民基本台帳に記録された日本人住民の数で、外国人住民は含みません。全国の推移を、2000年度を100とした指数で重ねました。

```chart
{
  "layer": [
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"land_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 2.5,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "land_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "land_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2000年度＝100", "grid": true}
        },
        "color": {
          "datum": "宅地面積",
          "type": "nominal",
          "scale": {"domain": ["宅地面積", "人口（日本人住民）"], "range": ["#f97316", "#3b82f6"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "national"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"pop_index\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2.5,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "pop_index", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "pop_index",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "2000年度＝100", "grid": true}
        },
        "color": {
          "datum": "人口（日本人住民）",
          "type": "nominal",
          "scale": {"domain": ["宅地面積", "人口（日本人住民）"], "range": ["#f97316", "#3b82f6"]},
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

2本の線は2008年度から離れていきます。人口は2008年度の12,707.6万人をピークに減り始め、2023年度は12,156.2万人で、2000年度の96.3%になりました。宅地面積は同じ期間に15,647.1km²から17,608.2km²へ、2000年度の112.5%まで増えています。人口が減り始めてからの15年間も、宅地面積の増え方はほとんど変わっていません。

人口を日本人住民に限っているので、人口の減り方は外国人住民を含めた場合より大きくなります。外国人住民を含めた総計は、基準日が1月1日に統一された2014年1月1日から2024年1月1日までに355万人減り、日本人住民は487万人減りました。外国人住民を含めても、人口が減って宅地が増えている傾向は変わりません。

1人あたりの宅地面積は、2000年度の123.9m²から2023年度の144.8m²へ、23年で約17%広がりました。宅地に沿って整備された道路や管路の量が変わらなくても、それを維持する住民の数は減っていると考えられます。

## 人口が減った市区町村の91%で、宅地面積は増えている

全国の値は、人口が増えた都市部と減った地方を合計した値です。市区町村ごとに、2000年度から2023年度への人口の変化率（横軸）と宅地面積の変化率（縦軸）を1点ずつ描きました。対象は両方の値が24年分ある1,715市区町村で、東京23区は区ごとの収録が2008年度で終わるので「特別区部」の1件として集計しています。

```chart
{
  "height": 400,
  "layer": [
    {
      "data": {"name": "municipal_shrink"},
      "mark": {"type": "point", "opacity": 0.5, "filled": true, "size": 16},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_pct", "type": "quantitative"},
          {"field": "land_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_pct",
          "type": "quantitative",
          "scale": {"domain": [-62, 65], "zero": false, "nice": false},
          "axis": {"title": "人口の変化率（%）"}
        },
        "y": {
          "field": "land_pct",
          "type": "quantitative",
          "scale": {"domain": [-50, 100], "zero": false, "nice": false},
          "axis": {"title": "宅地面積の変化率（%）", "grid": true}
        },
        "color": {
          "datum": "人口が減り宅地が増えた",
          "type": "nominal",
          "scale": {"domain": ["人口が減り宅地が増えた", "それ以外"], "range": ["#f97316", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "municipal_other"},
      "mark": {"type": "point", "opacity": 0.5, "filled": true, "size": 16},
      "encoding": {
        "tooltip": [
          {"field": "area_name", "type": "nominal"},
          {"field": "pop_pct", "type": "quantitative"},
          {"field": "land_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "pop_pct",
          "type": "quantitative",
          "scale": {"domain": [-62, 65], "zero": false, "nice": false},
          "axis": {"title": "人口の変化率（%）"}
        },
        "y": {
          "field": "land_pct",
          "type": "quantitative",
          "scale": {"domain": [-50, 100], "zero": false, "nice": false},
          "axis": {"title": "宅地面積の変化率（%）", "grid": true}
        },
        "color": {
          "datum": "それ以外",
          "type": "nominal",
          "scale": {"domain": ["人口が減り宅地が増えた", "それ以外"], "range": ["#f97316", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

点の多くは左上にあります。人口が減ったのは1,420市区町村で、そのうち1,296（91%）で宅地面積は増えていました。人口が2割以上減った858市区町村でも、747で宅地は増えています。1人あたりの宅地面積が広がった市区町村は1,641で、全体の96%です。人口が減っても、その分の宅地が減ってはいません。

縦軸は100%までを表示しています。23年で宅地面積が2倍を超えた市区町村が3つあり、その3点は図の外にあります。

宅地面積は固定資産税の課税台帳に基づくので、地目の認定を見直した年に面積がまとまって変わることがあります。市区町村の単年の増減は開発の量と一致するとは限らず、ここで見ている23年の変化にもこうした見直しが含まれます。

## 1人あたりの宅地面積が減ったのは東京都だけで、秋田県は83.1m²広がった

1人あたりの宅地面積が23年でどれだけ増えたかを、都道府県別に並べました。各年度の県内の宅地面積を県の人口で割った値の増加量（m²）です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pref_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1人あたり宅地面積の増加（m²、2000年度→2023年度）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "増加が大きい10県",
          "type": "nominal",
          "scale": {
            "domain": ["増加が大きい10県", "中間", "増加が小さい10県"],
            "range": ["#f97316", "#fdba74", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1人あたり宅地面積の増加（m²、2000年度→2023年度）", "grid": true}
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
          "scale": {
            "domain": ["増加が大きい10県", "中間", "増加が小さい10県"],
            "range": ["#f97316", "#fdba74", "#94a3b8"]
          },
          "title": null
        }
      }
    },
    {
      "data": {"name": "pref_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [
          {"field": "diff", "type": "quantitative"},
          {"field": "pref", "type": "nominal"}
        ],
        "x": {
          "field": "diff",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "1人あたり宅地面積の増加（m²、2000年度→2023年度）", "grid": true}
        },
        "y": {
          "field": "pref",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": "都道府県"},
          "sort": null
        },
        "color": {
          "datum": "増加が小さい10県",
          "type": "nominal",
          "scale": {
            "domain": ["増加が大きい10県", "中間", "増加が小さい10県"],
            "range": ["#f97316", "#fdba74", "#94a3b8"]
          },
          "title": null
        }
      }
    }
  ]
}
```

最も増えたのは秋田県で、197.8m²から280.9m²へ83.1m²広がりました。岩手県が77.7m²、青森県が72.9m²と続きます。上位10県はいずれも人口が11%以上減っていて、人口の減り方が大きい県ほど1人あたりの面積が大きく増えています。増加が小さいのは大都市のある府県で、神奈川県は67.0m²から68.0m²へ1.0m²の増加です。47都道府県で唯一減ったのが東京都で、23年で人口が12.2%増えたため、46.7m²から44.0m²へ2.7m²減りました。

秋田県と東京都の1人あたり宅地面積の差は、2000年度の4.2倍から2023年度には6.4倍に広がっています。

## 宅地が増えた6,926km²と、田畑が減った8,057km²は近い大きさ

評価総地積は地目ごとに分かれているので、同じ台帳の中で、宅地が増えた期間にどの地目が減ったかを確認できます。収録が1975年度からある田・畑と並べました。

```chart
{
  "layer": [
    {
      "data": {"name": "landuse"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"residential_km2\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#f97316",
        "strokeWidth": 2.5,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "residential_km2", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "residential_km2",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "評価総地積（km²）", "grid": true}
        },
        "color": {
          "datum": "宅地",
          "type": "nominal",
          "scale": {"domain": ["宅地", "田", "畑"], "range": ["#f97316", "#3b82f6", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "landuse"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"paddy_km2\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#3b82f6",
        "strokeWidth": 2.5,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "paddy_km2", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "paddy_km2",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "評価総地積（km²）", "grid": true}
        },
        "color": {
          "datum": "田",
          "type": "nominal",
          "scale": {"domain": ["宅地", "田", "畑"], "range": ["#f97316", "#3b82f6", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    },
    {
      "data": {"name": "landuse"},
      "transform": [
        {"window": [{"op": "row_number", "as": "__row"}]},
        {
          "calculate": "isValid(datum[\"year\"]) && isValid(datum[\"field_km2\"]) ? 0 : 1",
          "as": "__gap"
        },
        {"window": [{"op": "sum", "field": "__gap", "as": "__segment"}]},
        {"filter": "datum.__gap == 0"}
      ],
      "mark": {
        "type": "line",
        "color": "#22c55e",
        "strokeWidth": 2.5,
        "invalid": "break-paths-show-domains"
      },
      "encoding": {
        "tooltip": [
          {"field": "year", "type": "quantitative"},
          {"field": "field_km2", "type": "quantitative"}
        ],
        "x": {
          "field": "year",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "年度", "format": "d"}
        },
        "y": {
          "field": "field_km2",
          "type": "quantitative",
          "scale": {"zero": false},
          "axis": {"title": "評価総地積（km²）", "grid": true}
        },
        "color": {
          "datum": "畑",
          "type": "nominal",
          "scale": {"domain": ["宅地", "田", "畑"], "range": ["#f97316", "#3b82f6", "#22c55e"]},
          "title": null
        },
        "order": {"field": "__row", "type": "quantitative"},
        "detail": {"field": "__segment"}
      }
    }
  ]
}
```

宅地は1975年度の10,682km²から2023年度の17,608km²へ1.6倍になりました。1975年度以降、前年度を下回ったのは2010年度の1回だけです。同じ期間に田は30,526km²から25,181km²へ5,345km²、畑は25,881km²から23,169km²へ2,712km²減っています。宅地が増えた6,926km²と、田畑が減った8,057km²は近い大きさです。

3つとも課税対象の土地だけを集計した値なので、減った田畑がそのまま宅地になったとは限りません。田畑が山林や原野として扱われるようになった分や、道路や公園になって非課税になった分も、田畑の減少に含まれます。この図から分かるのは、課税台帳の上で農地が減り、建物の敷地が増えてきたことです。

## 業務での使い方

- 自分の市区町村の宅地面積と人口を年度ごとに並べると、1人あたりの面積がいつから広がり始めたかが分かります。立地適正化計画の見直しで、居住誘導区域の人口密度をどこまで保つかを検討するときの基礎資料になります
- 同じ県内で人口規模の近い市町村と1人あたりの宅地面積を比較すると、上下水道や道路の維持費が住民1人あたりでどれだけ大きくなりやすいかを相対的に把握できます
- 宅地・田・畑の3つを自分の県で並べると、農地から宅地への移り方が全国と比較して速いか遅いかが分かります。開発許可や農地転用の運用を説明する資料になります

## データの出典

本記事は e-Stat の社会・人口統計体系のうち、[自然環境](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000020202)と[人口・世帯](https://www.e-stat.go.jp/stat-search/database?statdisp_id=0000020201)を2026年9月7日時点で集計しています。宅地・田・畑の面積は総務省の[固定資産の価格等の概要調書](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/ichiran08_r06_00.html)、人口は総務省の[住民基本台帳に基づく人口、人口動態及び世帯数](https://www.soumu.go.jp/main_sosiki/jichi_gyousei/daityo/jinkou_jinkoudoutai-setaisuu.html)が元データです。記事の年度表記はこの体系の収録どおりで、実際の時点はいずれも年度の翌年です。面積は翌年1月1日（固定資産税の賦課期日）、人口は2013年度以降が翌年1月1日、2012年度までが翌年3月31日で、2023年度はどちらも2024年1月1日の値です。

Queriaは、社会・人口統計体系の50年分の統計表を、地目や指標のコードで検索できるテーブルにまとめ、単位や項目の説明を付けて公開しています。本記事で使った[市区町村の土地テーブル](/datasets/queria/e_stat/ssds/b_municipal_land)と[市区町村の人口テーブル](/datasets/queria/e_stat/ssds/a_municipal_population)から、担当地域の宅地面積と人口を年度ごとに確認したり、近隣市町村と並べたりできます。

```sql id=coverage
SELECT '評価総地積（田・畑・宅地）の収録年度' AS item, CAST(MIN(year) AS VARCHAR) || '〜' || CAST(MAX(year) AS VARCHAR) AS detail FROM e_stat.ssds.b_pref_land WHERE area_name = '全国' AND cat01 IN ('B120101', 'B120102', 'B120103') AND TRY_CAST(value AS DOUBLE) IS NOT NULL UNION ALL SELECT '評価総地積（山林・牧場・原野・その他）の収録年度' AS item, CAST(MIN(year) AS VARCHAR) || '〜' || CAST(MAX(year) AS VARCHAR) AS detail FROM e_stat.ssds.b_pref_land WHERE area_name = '全国' AND cat01 IN ('B120104', 'B120105', 'B120106', 'B120107') AND TRY_CAST(value AS DOUBLE) IS NOT NULL UNION ALL SELECT '宅地・東京23区を個別に収録した年度' AS item, CAST(MIN(year) AS VARCHAR) || '〜' || CAST(MAX(year) AS VARCHAR) AS detail FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B120103' AND area_name LIKE '東京都 %区' AND area_name NOT LIKE '% % %' AND TRY_CAST(value AS DOUBLE) IS NOT NULL UNION ALL SELECT '宅地・東京都 特別区部の収録年度' AS item, CAST(MIN(year) AS VARCHAR) || '〜' || CAST(MAX(year) AS VARCHAR) AS detail FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B120103' AND area_name = '東京都 特別区部' AND TRY_CAST(value AS DOUBLE) IS NOT NULL UNION ALL SELECT '住民基本台帳・' || resident_kind || 'の収録開始' AS item, CAST(MIN(reference_date) AS VARCHAR) AS detail FROM e_stat.resident_registry.population WHERE area_level = 'national' GROUP BY resident_kind UNION ALL SELECT '住民基本台帳・基準日が1月1日になった最初の時点' AS item, CAST(MIN(reference_date) AS VARCHAR) AS detail FROM e_stat.resident_registry.population WHERE area_level = 'national' AND MONTH(reference_date) = 1 AND DAY(reference_date) = 1 ORDER BY item
```

```sql id=national
WITH l AS (SELECT year, TRY_CAST(value AS DOUBLE) AS land FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B120103' AND area_name = '全国' AND year BETWEEN 2000 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), p AS (SELECT year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2101' AND area_name = '全国' AND year BETWEEN 2000 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL), a AS (SELECT l.year AS year, l.land AS land, p.pop AS pop FROM l JOIN p ON l.year = p.year) SELECT a.year AS year, ROUND(a.land / 1000000.0, 1) AS land_km2, ROUND(a.pop / 10000.0, 1) AS pop_10k, ROUND(a.land / a.pop, 1) AS m2_per_person, ROUND(a.land / b.land * 100, 1) AS land_index, ROUND(a.pop / b.pop * 100, 1) AS pop_index FROM a CROSS JOIN (SELECT land, pop FROM a WHERE year = 2000) b ORDER BY a.year
```

```sql id=municipal_shrink
WITH land AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B120103' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2023 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '東京都 %区'), pop AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2101' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2023 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '東京都 %区'), j AS (SELECT l.area_name AS area_name, l.year AS year, l.v AS land, p.v AS pop FROM land l JOIN pop p ON l.area_name = p.area_name AND l.year = p.year), fp AS (SELECT area_name FROM j GROUP BY 1 HAVING count(*) = 24), c AS (SELECT j.area_name AS area_name, MAX(CASE WHEN j.year = 2000 THEN land END) AS l0, MAX(CASE WHEN j.year = 2023 THEN land END) AS l1, MAX(CASE WHEN j.year = 2000 THEN pop END) AS p0, MAX(CASE WHEN j.year = 2023 THEN pop END) AS p1 FROM j JOIN fp ON j.area_name = fp.area_name GROUP BY 1) SELECT area_name, ROUND((p1 / p0 - 1) * 100, 1) AS pop_pct, ROUND((l1 / l0 - 1) * 100, 1) AS land_pct FROM c WHERE p1 < p0 AND l1 > l0 ORDER BY area_name
```

```sql id=municipal_other
WITH land AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B120103' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2023 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '東京都 %区'), pop AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2101' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2023 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '東京都 %区'), j AS (SELECT l.area_name AS area_name, l.year AS year, l.v AS land, p.v AS pop FROM land l JOIN pop p ON l.area_name = p.area_name AND l.year = p.year), fp AS (SELECT area_name FROM j GROUP BY 1 HAVING count(*) = 24), c AS (SELECT j.area_name AS area_name, MAX(CASE WHEN j.year = 2000 THEN land END) AS l0, MAX(CASE WHEN j.year = 2023 THEN land END) AS l1, MAX(CASE WHEN j.year = 2000 THEN pop END) AS p0, MAX(CASE WHEN j.year = 2023 THEN pop END) AS p1 FROM j JOIN fp ON j.area_name = fp.area_name GROUP BY 1) SELECT area_name, ROUND((p1 / p0 - 1) * 100, 1) AS pop_pct, ROUND((l1 / l0 - 1) * 100, 1) AS land_pct FROM c WHERE NOT (p1 < p0 AND l1 > l0) ORDER BY area_name
```

```sql id=municipal_counts
WITH land AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.b_municipal_land WHERE cat01 = 'B120103' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2023 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '東京都 %区'), pop AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS v FROM e_stat.ssds.a_municipal_population WHERE cat01 = 'A2101' AND TRY_CAST(value AS DOUBLE) IS NOT NULL AND year BETWEEN 2000 AND 2023 AND area_name LIKE '% %' AND area_name NOT LIKE '% % %' AND area_name NOT LIKE '東京都 %区'), j AS (SELECT l.area_name AS area_name, l.year AS year, l.v AS land, p.v AS pop FROM land l JOIN pop p ON l.area_name = p.area_name AND l.year = p.year), fp AS (SELECT area_name FROM j GROUP BY 1 HAVING count(*) = 24), c AS (SELECT j.area_name AS area_name, MAX(CASE WHEN j.year = 2000 THEN land END) AS l0, MAX(CASE WHEN j.year = 2023 THEN land END) AS l1, MAX(CASE WHEN j.year = 2000 THEN pop END) AS p0, MAX(CASE WHEN j.year = 2023 THEN pop END) AS p1 FROM j JOIN fp ON j.area_name = fp.area_name GROUP BY 1) SELECT count(*) AS municipalities, count(*) FILTER (WHERE p1 < p0) AS pop_down, count(*) FILTER (WHERE p1 < p0 AND l1 > l0) AS pop_down_land_up, count(*) FILTER (WHERE p1 / p0 < 0.8) AS pop_down_20pct, count(*) FILTER (WHERE p1 / p0 < 0.8 AND l1 > l0) AS pop_down_20pct_land_up, count(*) FILTER (WHERE l1 / p1 > l0 / p0) AS per_capita_up, count(*) FILTER (WHERE l1 / l0 > 2.0) AS land_doubled FROM c
```

```sql id=pref_top
WITH l AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS land FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B120103' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL), p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2101' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL), j AS (SELECT l.area_name AS pref, l.year AS year, l.land / p.pop AS per_capita, p.pop AS pop FROM l JOIN p ON l.area_name = p.area_name AND l.year = p.year), d AS (SELECT pref, ROUND(MAX(CASE WHEN year = 2000 THEN per_capita END), 1) AS m2_2000, ROUND(MAX(CASE WHEN year = 2023 THEN per_capita END), 1) AS m2_2023, ROUND(MAX(CASE WHEN year = 2023 THEN per_capita END) - MAX(CASE WHEN year = 2000 THEN per_capita END), 1) AS diff, ROUND((MAX(CASE WHEN year = 2023 THEN pop END) / MAX(CASE WHEN year = 2000 THEN pop END) - 1) * 100, 1) AS pop_pct FROM j GROUP BY 1), ranked AS (SELECT pref, m2_2000, m2_2023, diff, pop_pct, ROW_NUMBER() OVER (ORDER BY diff DESC, pref) AS rn FROM d) SELECT pref, m2_2000, m2_2023, diff, pop_pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pref_mid
WITH l AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS land FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B120103' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL), p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2101' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL), j AS (SELECT l.area_name AS pref, l.year AS year, l.land / p.pop AS per_capita, p.pop AS pop FROM l JOIN p ON l.area_name = p.area_name AND l.year = p.year), d AS (SELECT pref, ROUND(MAX(CASE WHEN year = 2000 THEN per_capita END), 1) AS m2_2000, ROUND(MAX(CASE WHEN year = 2023 THEN per_capita END), 1) AS m2_2023, ROUND(MAX(CASE WHEN year = 2023 THEN per_capita END) - MAX(CASE WHEN year = 2000 THEN per_capita END), 1) AS diff, ROUND((MAX(CASE WHEN year = 2023 THEN pop END) / MAX(CASE WHEN year = 2000 THEN pop END) - 1) * 100, 1) AS pop_pct FROM j GROUP BY 1), ranked AS (SELECT pref, m2_2000, m2_2023, diff, pop_pct, ROW_NUMBER() OVER (ORDER BY diff DESC, pref) AS rn FROM d) SELECT pref, m2_2000, m2_2023, diff, pop_pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pref_bottom
WITH l AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS land FROM e_stat.ssds.b_pref_land WHERE cat01 = 'B120103' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL), p AS (SELECT area_name, year, TRY_CAST(value AS DOUBLE) AS pop FROM e_stat.ssds.a_pref_population WHERE cat01 = 'A2101' AND area_name <> '全国' AND year IN (2000, 2023) AND TRY_CAST(value AS DOUBLE) IS NOT NULL), j AS (SELECT l.area_name AS pref, l.year AS year, l.land / p.pop AS per_capita, p.pop AS pop FROM l JOIN p ON l.area_name = p.area_name AND l.year = p.year), d AS (SELECT pref, ROUND(MAX(CASE WHEN year = 2000 THEN per_capita END), 1) AS m2_2000, ROUND(MAX(CASE WHEN year = 2023 THEN per_capita END), 1) AS m2_2023, ROUND(MAX(CASE WHEN year = 2023 THEN per_capita END) - MAX(CASE WHEN year = 2000 THEN per_capita END), 1) AS diff, ROUND((MAX(CASE WHEN year = 2023 THEN pop END) / MAX(CASE WHEN year = 2000 THEN pop END) - 1) * 100, 1) AS pop_pct FROM j GROUP BY 1), ranked AS (SELECT pref, m2_2000, m2_2023, diff, pop_pct, ROW_NUMBER() OVER (ORDER BY diff DESC, pref) AS rn FROM d) SELECT pref, m2_2000, m2_2023, diff, pop_pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=landuse
SELECT year, ROUND(MAX(CASE WHEN cat01 = 'B120103' THEN TRY_CAST(value AS DOUBLE) END) / 1000000.0, 0) AS residential_km2, ROUND(MAX(CASE WHEN cat01 = 'B120101' THEN TRY_CAST(value AS DOUBLE) END) / 1000000.0, 0) AS paddy_km2, ROUND(MAX(CASE WHEN cat01 = 'B120102' THEN TRY_CAST(value AS DOUBLE) END) / 1000000.0, 0) AS field_km2 FROM e_stat.ssds.b_pref_land WHERE area_name = '全国' AND cat01 IN ('B120101', 'B120102', 'B120103') AND year BETWEEN 1975 AND 2023 AND TRY_CAST(value AS DOUBLE) IS NOT NULL GROUP BY year ORDER BY year
```

```sql id=resident_kind
SELECT year, reference_date, MAX(CASE WHEN resident_kind = 'total' THEN population_total END) AS total, MAX(CASE WHEN resident_kind = 'japanese' THEN population_total END) AS japanese, MAX(CASE WHEN resident_kind = 'foreign' THEN population_total END) AS foreign_residents FROM e_stat.resident_registry.population WHERE area_level = 'national' AND year IN (2014, 2024) GROUP BY year, reference_date ORDER BY year
```
