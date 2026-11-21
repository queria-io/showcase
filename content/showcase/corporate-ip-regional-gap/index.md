---
title: 特許を持つ会社の割合が一番高いのは富山県、東京は10位。デザインの登録は新潟県が全国一
description: 全国444万社の登記所在地とgBizINFOの知財情報から、特許・商標・意匠を持つ会社の割合を都道府県別に比較しました。特許を持つ会社の割合は富山県が0.921%で最も高く、東京都は10位です。県の間の差は特許で6.05倍、意匠で10.17倍、商標で2.52倍です。
ogDescription: 特許を持つ会社の割合は富山県が0.921%で最も高く、東京都は10位でした。全国444万社とgBizINFOの知財情報を法人番号で結合して集計しています。
publishedAt: 2026-08-19
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - 知的財産
  - 特許
  - gBizINFO
  - 法人番号
datasets:
  - queria/gbizinfo
  - queria/houjin_bangou
  - queria/nlftp
sources:
  - title: gBizINFO 法人活動情報
    url: https://info.gbiz.go.jp/
    publisher: 経済産業省
  - title: 法人番号公表サイト
    url: https://www.houjin-bangou.nta.go.jp/
    publisher: 国税庁
agentHint: houjin_bangou.main.mart_houjin_bangou の city_name と gbizinfo.main.mart_gbizinfo_patent を使って、自分の県の市区町村別に特許・商標・意匠を持つ会社の数と、会社数に占める割合を出して。2014年から2019年の出願に絞って
socialAnnounce: |-
  全国444万社の登記所在地と、gBizINFOの特許・商標・意匠を突き合わせました。

  特許を持つ会社の割合が最も高いのは富山県で、東京都は10位です。

  Queriaは行政のオープンデータを業務で使える形に整えて公開しています。
---

2014年から2019年に出願して登録された特許を持つ会社は、県内の会社の0.921%を占める富山県が最も多く、東京都は0.652%で10位でした。特許を持つ会社の割合は、最も高い県と最も低い県で6.05倍違います。意匠では10.17倍の差があり、1位は新潟県です。商標を持つ会社の割合の差は2.52倍で、どの県も近い水準です。

[国税庁が公表する法人番号](https://www.houjin-bangou.nta.go.jp/)の全件データには、全国の会社の登記所在地が記録されています。[経済産業省のgBizINFO](https://info.gbiz.go.jp/)は、法人番号ごとに特許・意匠・商標の情報を収録しています。この記事では2つを法人番号で結合し、特許・商標・意匠を持つ会社が県内の会社に占める割合を都道府県別に集計しました。多くの都道府県が出願費用の助成や相談窓口などの知的財産の支援を行っており、その対象になる会社の数を把握する材料になります。

## 全国444万社のうち、商標を持つ会社は1.488%、特許は0.529%、意匠は0.152%

分母は、法人番号のある法人のうち、株式会社・有限会社・合名会社・合資会社・合同会社の会社です。全国で4,439,774社あり、登記された本店の所在地から都道府県が分かります。分子は、gBizINFOに収録された特許・意匠・商標のうち、その会社が権利者になっているものです。

gBizINFOに収録されるのは登録された権利で、出願から登録までには時間がかかります。最近の出願ほど収録が遅れるので、収録がほぼ済んでいる2014年から2019年に出願され、登録された権利を対象にしました。法人番号で結び付く権利だけが収録されるので、個人名義の出願は含みません。

```sql
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), src AS (SELECT corporate_number, rights_type FROM gbizinfo.main.mart_gbizinfo_patent WHERE application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), rd AS (SELECT DISTINCT corporate_number, rights_type FROM src), base AS (SELECT prefecture_name AS pref, COUNT(*) AS firms FROM h GROUP BY prefecture_name), byp AS (SELECT rd.rights_type AS rt, h.prefecture_name AS pref, COUNT(*) AS ip FROM h JOIN rd ON rd.corporate_number = h.corporate_number GROUP BY 1, 2), pc AS (SELECT byp.rt, byp.pref, byp.ip, CAST(byp.ip AS DOUBLE) * 100 / base.firms AS p FROM byp JOIN base ON base.pref = byp.pref) SELECT rt AS '権利の種類', (SELECT SUM(firms) FROM base) AS '対象の会社数', SUM(ip) AS '権利を持つ会社数', ROUND(CAST(SUM(ip) AS DOUBLE) * 100 / (SELECT SUM(firms) FROM base), 3) AS '全国の会社に占める割合(%)', arg_max(pref, p) AS '割合が最も高い県', ROUND(MAX(p), 3) AS '最高(%)', arg_min(pref, p) AS '割合が最も低い県', ROUND(MIN(p), 3) AS '最低(%)', ROUND(MAX(p) / MIN(p), 2) AS '最高と最低の倍率' FROM pc GROUP BY rt ORDER BY SUM(ip) DESC
```

商標を持つ会社は66,050社で、全国の会社の1.488%です。特許は23,466社（0.529%）、意匠は6,763社（0.152%）です。商標を持つ会社は、特許の2.8倍、意匠の9.8倍あります。意匠は、製品の形や模様などのデザインを保護する権利です。

表の右端の列は、県内の会社に占める割合の、最も高い県と最も低い県の比です。商標は2.52倍、特許は6.05倍、意匠は10.17倍です。商標を持つ会社の割合はどの県でも近い水準で、特許と意匠を持つ会社の割合は県によって大きく異なります。

## 特許を持つ会社の割合は、富山県が0.921%で最も高い

県内の会社のうち、2014年から2019年に出願して登録された特許を持つ会社の割合です。青が上位10、薄い青が中間の27、グレーが下位10です。

```chart
{
  "height": 980,
  "layer": [
    {
      "data": {"name": "pat_top"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "特許を持つ会社の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pat_mid"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "特許を持つ会社の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    },
    {
      "data": {"name": "pat_bottom"},
      "mark": {"type": "bar"},
      "encoding": {
        "tooltip": [{"field": "pct", "type": "quantitative"}, {"field": "pref", "type": "nominal"}],
        "x": {
          "field": "pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "特許を持つ会社の割合（%）", "grid": true}
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
          "scale": {"domain": ["上位10", "中間", "下位10"], "range": ["#3b82f6", "#93c5fd", "#94a3b8"]},
          "title": null
        }
      }
    }
  ]
}
```

1位は富山県で0.921%、2位は福井県で0.855%です。滋賀県（0.757%）、大阪府（0.728%）、長野県（0.716%）、愛知県（0.698%）、京都府（0.697%）、石川県（0.690%）、新潟県（0.660%）が続き、東京都は0.652%で10位です。富山県の割合は東京都の約1.4倍です。北陸3県がすべて上位に入り、新潟県と長野県も上位にあります。

割合が低いのは沖縄県（0.152%）、長崎県（0.197%）、北海道（0.200%）、熊本県（0.251%）、千葉県（0.264%）です。富山県と沖縄県では6.05倍の差があります。

会社の所在地は、法人番号に登録された本店の所在地です。地方の工場で生まれた発明でも、本店が東京にある会社の特許は東京都に集計されます。

特許を持つ会社の数で見ると、東京都が最も多くなります。

```sql
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), p AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_patent WHERE rights_type = '特許' AND application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS firms, COUNT(p.corporate_number) AS ip FROM h LEFT JOIN p ON p.corporate_number = h.corporate_number GROUP BY h.prefecture_name) SELECT pref AS '都道府県', ip AS '特許を持つ会社数', ROUND(CAST(ip AS DOUBLE) * 100 / (SELECT SUM(ip) FROM agg), 1) AS '全国に占める割合(%)', firms AS '会社数', ROUND(CAST(firms AS DOUBLE) * 100 / (SELECT SUM(firms) FROM agg), 1) AS '会社数の全国シェア(%)' FROM agg ORDER BY ip DESC LIMIT 5
```

東京都で特許を持つ会社は6,996社で、全国の23,466社の29.8%を占めます。東京都の会社数が全国に占める割合は24.2%なので、特許を持つ会社は会社数の比率より多く東京都に集まっています。支援の対象になる会社の数を見積もるときは社数を、県内でどれだけの会社が特許を持っているかを把握するときは割合を使います。

## 特許の割合が同じ程度の県でも、商標の割合は長野県の1.565%から東京都の2.028%まで分かれる

横軸に特許を持つ会社の割合、縦軸に商標を持つ会社の割合を取り、47都道府県を並べました。点にカーソルを合わせると県名が表示されます。

```chart
{
  "height": 360,
  "layer": [
    {
      "data": {"name": "axes"},
      "mark": {"type": "point", "color": "#7c3aed", "filled": true, "size": 81},
      "encoding": {
        "tooltip": [
          {"field": "pref", "type": "nominal"},
          {"field": "pat_pct", "type": "quantitative"},
          {"field": "tm_pct", "type": "quantitative"}
        ],
        "x": {
          "field": "pat_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "特許を持つ会社の割合（%）", "grid": true}
        },
        "y": {
          "field": "tm_pct",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "商標を持つ会社の割合（%）", "grid": true}
        }
      }
    }
  ]
}
```

商標の割合は0.804%から2.028%の範囲にあります。特許の割合は0.152%から0.921%で、値は小さいものの、県の間の差は商標より大きくなっています。

特許の割合が同じ程度でも、商標の割合は県によって異なります。特許の割合が0.65%から0.72%の長野県・愛知県・京都府・石川県・新潟県・東京都では、商標の割合は長野県の1.565%から東京都の2.028%まで分かれます。特許が0.20%前後の長崎県と北海道では、商標は長崎県が1.179%、北海道が0.832%で、1.4倍違います。

千葉県は特許0.264%（43位）、商標0.804%（47位）で、図の左下の端にあります。埼玉県（特許34位・商標44位）、茨城県（特許31位・商標45位）、神奈川県（特許26位・商標37位）も近くにあり、いずれも商標の順位が特許の順位より低くなっています。

## 意匠を持つ会社の割合は新潟県が0.340%で最も高く、沖縄県の10.17倍

意匠は県の間の差が10.17倍で、3つの権利の中で最も大きいので、地図にしました。色が濃いほど、県内の会社に占める割合が高い県です。

```map
type: map
layers:
  - from: design_map
    geojson: geojson
    color: pct
    label: pref_name
    name: "意匠を持つ会社の割合（%）"
lng: 137
lat: 36.5
zoom: 4
```

1位は新潟県で0.340%、2位が奈良県（0.305%）、3位が富山県（0.304%）です。大阪府（0.285%）、岐阜県（0.246%）、福井県（0.244%）が続き、東京都は0.186%で13位です。新潟県から北陸・近畿・東海にかけての県は色が濃く、北海道（0.057%）・東北・九州は色が薄くなっています。最も低い沖縄県は0.033%で、新潟県との差は10.17倍です。

特許の上位には北陸の県が多く、意匠の上位には新潟県と奈良県が入ります。新潟県は特許では9位で意匠では1位、奈良県は特許では14位で意匠では2位です。特許を持つ会社が多い県と意匠を持つ会社が多い県は、一部は重なり、一部は異なります。

## 業務での使い方

- 自県の順位を3つの権利ごとに確認できます。特許・商標・意匠のうち全国平均を下回っているものを見ると、支援のどの分野に人員を配置するかを検討する材料になります
- 3つの権利で順位が大きく異なる県を確認できます。新潟県は特許9位・意匠1位、京都府は特許7位・意匠16位で、県ごとに割合の高い権利が異なります
- 近隣の県や産業構成の似た県と比較できます。規模が同じ程度の県で割合が大きく違う場合、制度の利用状況に差がある可能性があります
- 市区町村ごとに集計できます。法人番号のデータには市区町村名があるので、同じ方法で県内の市区町村ごとの割合を出せます

## データの出典

本記事は[経済産業省のgBizINFO](https://info.gbiz.go.jp/)が収録する知的財産情報と、[国税庁の法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)の全件データを、2026年8月19日時点で法人番号で結合して集計しています。知的財産情報の元データは特許庁の登録原簿で、対象は2014年から2019年までに出願され登録された特許・意匠・商標です。会社の所在地は法人番号に登録された本店の所在地を使っています。

Queriaは、gBizINFOと国税庁の法人番号のように別々に公表されるオープンデータを、法人番号を結合キーにしたテーブルにし、列名や単位の意味をメタデータに記載して公開しています。本記事で使った[知的財産テーブル](/datasets/queria/gbizinfo/main/mart_gbizinfo_patent)と[法人番号テーブル](/datasets/queria/houjin_bangou/main/mart_houjin_bangou)から、自県の会社を業種や規模で絞り込んだり、市区町村ごとに集計したりできます。

```sql id=pat_top
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), p AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_patent WHERE rights_type = '特許' AND application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS firms, COUNT(p.corporate_number) AS ip FROM h LEFT JOIN p ON p.corporate_number = h.corporate_number GROUP BY h.prefecture_name), ranked AS (SELECT pref, ROUND(CAST(ip AS DOUBLE) * 100 / firms, 3) AS pct, ROW_NUMBER() OVER (ORDER BY CAST(ip AS DOUBLE) / firms DESC, pref) AS rn FROM agg) SELECT pref, pct FROM ranked WHERE rn <= 10 ORDER BY rn
```

```sql id=pat_mid
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), p AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_patent WHERE rights_type = '特許' AND application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS firms, COUNT(p.corporate_number) AS ip FROM h LEFT JOIN p ON p.corporate_number = h.corporate_number GROUP BY h.prefecture_name), ranked AS (SELECT pref, ROUND(CAST(ip AS DOUBLE) * 100 / firms, 3) AS pct, ROW_NUMBER() OVER (ORDER BY CAST(ip AS DOUBLE) / firms DESC, pref) AS rn FROM agg) SELECT pref, pct FROM ranked WHERE rn > 10 AND rn <= 37 ORDER BY rn
```

```sql id=pat_bottom
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), p AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_patent WHERE rights_type = '特許' AND application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS firms, COUNT(p.corporate_number) AS ip FROM h LEFT JOIN p ON p.corporate_number = h.corporate_number GROUP BY h.prefecture_name), ranked AS (SELECT pref, ROUND(CAST(ip AS DOUBLE) * 100 / firms, 3) AS pct, ROW_NUMBER() OVER (ORDER BY CAST(ip AS DOUBLE) / firms DESC, pref) AS rn FROM agg) SELECT pref, pct FROM ranked WHERE rn > 37 ORDER BY rn
```

```sql id=axes
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), rd AS (SELECT DISTINCT corporate_number, rights_type FROM gbizinfo.main.mart_gbizinfo_patent WHERE application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS firms, COUNT(r1.corporate_number) AS pat, COUNT(r2.corporate_number) AS tm FROM h LEFT JOIN rd r1 ON r1.corporate_number = h.corporate_number AND r1.rights_type = '特許' LEFT JOIN rd r2 ON r2.corporate_number = h.corporate_number AND r2.rights_type = '商標' GROUP BY h.prefecture_name) SELECT pref, ROUND(CAST(pat AS DOUBLE) * 100 / firms, 3) AS pat_pct, ROUND(CAST(tm AS DOUBLE) * 100 / firms, 3) AS tm_pct FROM agg ORDER BY pat_pct DESC
```

```sql id=design_map
WITH h AS (SELECT corporate_number, prefecture_name FROM houjin_bangou.main.mart_houjin_bangou WHERE kind IN ('301','302','303','304','305')), d AS (SELECT DISTINCT corporate_number FROM gbizinfo.main.mart_gbizinfo_patent WHERE rights_type = '意匠' AND application_date >= DATE '2014-01-01' AND application_date < DATE '2020-01-01'), agg AS (SELECT h.prefecture_name AS pref, COUNT(*) AS firms, COUNT(d.corporate_number) AS ip FROM h LEFT JOIN d ON d.corporate_number = h.corporate_number GROUP BY h.prefecture_name) SELECT ST_AsGeoJSON(ST_Simplify(b.geometry, 0.01)) AS geojson, ROUND(CAST(a.ip AS DOUBLE) * 100 / a.firms, 3) AS pct, b.prefecture_name AS pref_name FROM nlftp.boundary.prefecture b JOIN agg a ON a.pref = b.prefecture_name
```
