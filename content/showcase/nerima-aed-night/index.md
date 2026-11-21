---
title: 練馬区で夜に使えるAEDは18台で、区民の94.3%はそれが1台も無い町丁目に住む
description: 練馬区が公開するAED設置箇所一覧395台のうち、夜に使えるのは18台です。区の202の町丁目のうち191にはその1台も無く、70万9,750人が住んでいます。
ogDescription: 練馬区が公開するAED設置箇所一覧395台のうち、夜に使えるのは18台でした。
publishedAt: 2026-09-26
updatedAt: 2026-11-21
author:
  name: UD
  url: https://udus.dev
tags:
  - AED
  - オープンデータ
  - 練馬区
datasets:
  - queria/metro_tokyo
  - queria/e_stat
sources:
  - title: AED設置箇所一覧
    url: https://www.city.nerima.tokyo.jp/kusei/tokei/opendata/opendatasite/hokenfukushi/aed.html
    publisher: 練馬区
  - title: 地域・年齢別人口
    url: https://www.city.nerima.tokyo.jp/kusei/tokei/opendata/opendatasite/tokei_kusei/population.html
    publisher: 練馬区
  - title: 令和2年国勢調査 小地域（町丁・字等別）境界データ
    url: https://www.e-stat.go.jp/gis
    publisher: 総務省統計局
  - title: アドレス・ベース・レジストリ
    url: https://www.digital.go.jp/policies/base_registry_address
    publisher: デジタル庁
agentHint: metro_tokyo.ods.aed で org_code ごとに、start_time と end_time が 時:分 の形になっている台数と、そうでない台数を数えて、時刻の欄がどの市区町村でどれだけ記録されているか比べて
socialAnnounce: |-
  練馬区が公開しているAED設置箇所一覧395台を数えました。

  夜に使えるのは18台。区の202の町丁目のうち191にはその1台も無く、そこに70万9,750人、区民の94.3%が住んでいます。
  Queriaは行政のオープンデータを整えて公開しています。
---

[練馬区のAED設置箇所一覧](https://www.city.nerima.tokyo.jp/kusei/tokei/opendata/opendatasite/hokenfukushi/aed.html)に載っている395台のうち、利用できる時刻と備考から夜に使えると判断できるのは18台でした。区の202の町丁目のうち191にはその18台が1台も無く、そこに区民の94.3%にあたる70万9,750人が住んでいます。395台のうち224台は20時より前に使えなくなります。

東京都内では14の市区町村が同じ様式でAEDの設置場所を公開していて、名称と住所のほかに、利用できる開始時刻と終了時刻の欄があります。学校は夜に閉まり、区民館には閉館時刻がありますが、心停止は開館時間の外でも起きます。この記事では時刻の欄を使って、夜に使えるAEDの台数と場所を集計します。

## 395台のうち224台は、20時より前に使えなくなる

開始時刻と終了時刻で分けると、内訳は次のとおりです。

```sql
SELECT band AS '使える時間帯', n AS '台数' FROM band ORDER BY 2 DESC
```

最も多いのは20時より前に終わるもので224台、全体の半分を超えます。20時台か21時台までのものが146台で、ここまでで370台、全体の93.7%です。

22時まで使えるものが10台、開始が0時・終了が24時と記録されているものが13台でした。この13台が、一覧の上で24時間使えるものです。

残る2台は、開始も終了も `-` と書かれているものが1台と、`0.395833333` のような小数が入っているものが1台です。小数は、表計算ソフトが内部で持つ時刻の形のまま書き出された値です。この2台は何時まで使えるかを読み取れないので、時間帯の集計からは除いています（終了時刻の `0.75` を整数の時として読むと1時になり、「20時より前に終わる」に入ってしまうためです）。台数だけを集計する以降の表には、395台の一部として含めています。

```chart
{
  "height": 200,
  "layer": [
    {
      "data": {"name": "band"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "n", "type": "quantitative"}, {"field": "band", "type": "nominal"}],
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "台数", "grid": true}
        },
        "y": {
          "field": "band",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        }
      }
    },
    {
      "data": {"name": "band"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "n",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "台数", "grid": true}
        },
        "y": {
          "field": "band",
          "type": "nominal",
          "scale": {"reverse": true},
          "axis": {"title": ""},
          "sort": null
        },
        "text": {"field": "n"}
      }
    }
  ]
}
```

## 夜に使える18台は、保健相談所・区役所・駐車場・休日の診療所などにある

同じ一覧には、利用可能時間の特記事項を書く欄（備考）があります。備考の内容を集計すると次のとおりです。

```sql
SELECT total AS '台数', with_notes AS '備考の記載あり', always AS 'うち常時利用可能', after_hours AS 'うち時間外', call_guard AS 'うち声掛け', closed_days AS 'うち休館日・改修の記載' FROM notes
```

395台のうち327台に備考があり、その中に時間外の扱いを書いたものがあります。

```sql
SELECT band AS '時刻の欄', note AS '備考欄', n AS '台数' FROM by_column ORDER BY 1, 3 DESC
```

時刻の欄では夜まで使えないのに、備考に時間外の記載があるものが5台あります。区役所の本庁舎3か所と西庁舎、石神井庁舎で、いずれも「完全閉庁日と年末年始を除く※時間外でも、西庁舎1階夜間入口から、警備員に声掛けすると利用可能」（石神井庁舎は地下1階の警備室）と書かれています。

5台の終了時刻は 17:15 が2つ、19:00、21:30、22:00 です。22:00の1台（本庁舎アトリウム）は、前の表で「22時まで」に入れた10台のうちの1台でもあります。

時刻の欄が0時〜24時の13台のうち12台にも備考があります。9台は「屋外設置であるため、常時利用可能（機器整備中は除く）」で、3つの診療所は「平日23時〜8:30／土日祝22時〜8:30は警備員に声掛けすることで使用可能」と、深夜は警備員への声掛けが必要です。

この記事の「夜に使える18台」は、時刻の欄が `0:00`〜`24:00` の13台に、備考に「時間外」「常時利用可能」「声掛け」のいずれかを含む5台を加えた数です。「夜間利用がある場合、最大21:30まで」のように使える時間の上限を書いた備考は、時間外に使えるという意味ではないので含めていません。18台のうち、区役所の5台と診療所の3台は警備員への声掛けが前提で、実際にその時刻に建物へ入れるかどうかはデータからは確認できません。

## 夜に使える18台は、すべて住所から座標を求められた

この一覧には緯度・経度の欄がありますが、395台すべて空欄です。そのため、住所の欄から、デジタル庁が公開している[アドレス・ベース・レジストリ](https://www.digital.go.jp/policies/base_registry_address)を使って座標を求めました。

```sql
SELECT total AS '台数', outside_ward AS 'うち区外', source_latlon AS '一覧に緯度がある', with_geo AS '住所から座標が付いた', block_or_better AS 'うち街区か号まで', night_with_geo AS 'うち夜に使える18台' FROM geo
```

390台に座標が付き、390台すべてで街区（番）か、それより細かい号まで特定できています。座標は区が記録した設置位置ではなく、住所の号か街区の代表点です。

座標が付かなかった5台のうち4台は、住所が練馬区の外にある区の宿泊施設です。岩井少年自然の家（千葉県南房総市）、武石少年自然の家の本館と新館（長野県上田市）、軽井沢少年自然の家（長野県北佐久郡軽井沢町）で、時刻の欄は 8:30〜17:30 です。この4台の備考には「宿泊者がいる場合は24時間利用可能」と書かれていますが、「時間外」「常時利用可能」「声掛け」のどれにも当たらないので、18台には入っていません。残る1台は、住所の番地の前に余分なハイフンが入っています。

夜に使える18台には、すべて座標が付きました。

```sql
SELECT * FROM night_list ORDER BY 3, 1
```

名称で分けると、保健相談所が5か所、休日の診療所が3か所、区立の駐車場と自転車駐車場が4か所、区役所の庁舎が5か所です。残る1つは「しらゆり荘」で、この一覧には施設の種別の欄がないので、どのような施設かは分かりません。

設置位置の欄も集計しました。

```sql
SELECT * FROM outdoor ORDER BY 1, 3 DESC
```

設置位置に「屋外」と書かれているのは5台だけで、5台とも夜に使える18台に含まれます。それ以外の377台には、屋外の記載がありません。

設置位置と備考が一致しない台もあります。区立駐車場の4台は、設置位置が「地下1階駐車場管理室内」などの屋内ですが、備考は「屋外設置であるため、常時利用可能」です。どちらが正しいかは、この一覧からは判断できません。

## 夜に使えるAEDが無い191の町丁目に、区民の94.3%が住んでいる

練馬区は[町丁目ごとの人口も毎月公開しています](https://www.city.nerima.tokyo.jp/kusei/tokei/opendata/opendatasite/tokei_kusei/population.html)。国勢調査の町丁目の境界に18台の座標を重ね、町丁目ごとに集計しました。町丁目の名称は、境界データが「旭丘一丁目」、区の人口データが「旭丘１丁目」と表記が違うので、丁目の直前の文字を算用数字に統一して結合しています。境界側・人口側とも202地区で、すべて一致しました。

```sql
SELECT coverage AS '町丁目', areas AS '地区数', pop AS '人口' FROM coverage ORDER BY 3 DESC
```

202の町丁目のうち、夜に使えるAEDがあるのは11でした。残る191の町丁目には1台もなく、そこに住んでいるのは70万9,750人、区民の94.3%です。

この数字は、AEDが町丁目の区画の中にあるかどうかだけで判定していて、隣の町丁目にある1台は「無い」側に含めています。時刻の欄だけで判断した13台で集計しても、AEDが無い町丁目は同じ191です。備考から加えた5台は、すべて13台がある11の町丁目の中にあります。

人口の多い町丁目から並べると、次のとおりです。

```chart
{
  "height": 300,
  "layer": [
    {
      "data": {"name": "top"},
      "mark": {"type": "bar", "color": "#3b82f6"},
      "encoding": {
        "tooltip": [{"field": "pop", "type": "quantitative"}, {"field": "area", "type": "nominal"}],
        "x": {
          "field": "pop",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（2026年6月1日）", "grid": true}
        },
        "y": {"field": "area", "type": "nominal", "axis": {"title": ""}, "sort": null}
      }
    },
    {
      "data": {"name": "top"},
      "mark": {"type": "text", "align": "left", "dx": 4},
      "encoding": {
        "x": {
          "field": "pop",
          "type": "quantitative",
          "scale": {"zero": true},
          "axis": {"title": "人口（2026年6月1日）", "grid": true}
        },
        "y": {"field": "area", "type": "nominal", "axis": {"title": ""}, "sort": null},
        "text": {"field": "pop"}
      }
    }
  ]
}
```

最も人口が多いのは光が丘3丁目の8,685人で、関町南4丁目、田柄4丁目と続きます。町丁目は広さがそれぞれ違うので、この順位はAEDから最も遠い地域の順位ではありません。人口が7千人を超える町丁目が4つあり、そのどれにも夜に使えるAEDは1台もありません。

## まとめ

- 練馬区のAED設置箇所一覧395台のうち、夜に使えるのは18台です。内訳は保健相談所5、休日の診療所3、区立の駐車場と自転車駐車場4、区役所の庁舎5、しらゆり荘1です
- 18台が1台も無い町丁目は202のうち191で、そこに70万9,750人、区民の94.3%が住んでいます
- 395台のうち224台は20時より前に、146台は20時台か21時台までに使えなくなります
- 設置位置に屋外と書かれているのは5台で、5台とも夜に使える18台に含まれます
- 18台のうち、区役所の5台と診療所の3台は、警備員への声掛けが前提です

## データの出典

本記事は、東京都オープンデータカタログサイトで公開されている練馬区の[AED設置箇所一覧](/datasets/queria/metro_tokyo/ods/aed)と[地域・年齢別人口](/datasets/queria/metro_tokyo/ods/population)、[国勢調査の小地域境界データ](/datasets/queria/e_stat/boundary/small_area)（令和2年）を、2026年9月26日時点で取得して集計しています。人口は2026年6月1日現在のものです。

Queriaは、自治体が公開したCSVを、施設の名称・住所・時刻などの列に整理し、住所から求めた座標を別の列として付けて、人口や境界のデータと結合できる形で公開しています。[AEDのテーブル](/datasets/queria/metro_tokyo/ods/aed)には東京都内の14の市区町村のデータが入っているので、担当している市区町村に置き換えて同じ集計ができます。時刻の書き方は自治体ごとに違い（開始と終了をどちらも `0:00` と記録したもの、秒まで記録したもの、日をまたぐものなど）、13台という数は他の自治体の数字とそのままは比較できません。

```sql id=band
SELECT CASE WHEN start_time IS NULL OR end_time IS NULL OR NOT regexp_matches(start_time, '^[0-9]{1,2}:[0-9]{2}$') OR NOT regexp_matches(end_time, '^[0-9]{1,2}:[0-9]{2}$') THEN '時刻として読み取れない' WHEN start_time = '0:00' AND end_time = '24:00' THEN '0時から24時まで' WHEN end_time = '22:00' THEN '22時まで' WHEN try_cast(split_part(end_time, ':', 1) AS INT) BETWEEN 20 AND 21 THEN '20時台か21時台まで' ELSE '20時より前に終わる' END AS band, count(*) AS n FROM metro_tokyo.ods.aed WHERE org_code = 't131202' GROUP BY 1 ORDER BY n DESC
```

```sql id=by_column
SELECT CASE WHEN start_time = '0:00' AND end_time = '24:00' THEN '時刻の欄が0時〜24時' ELSE '時刻の欄はそれ以外' END AS band, CASE WHEN available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%' THEN '備考に時間外の記載あり' ELSE '備考に記載なし' END AS note, count(*) AS n FROM metro_tokyo.ods.aed WHERE org_code = 't131202' GROUP BY 1, 2 ORDER BY 1, 3 DESC
```

```sql id=notes
SELECT count(*) AS total, count(*) FILTER (WHERE available_notes IS NOT NULL AND available_notes <> '') AS with_notes, count(*) FILTER (WHERE available_notes LIKE '%常時利用可能%') AS always, count(*) FILTER (WHERE available_notes LIKE '%時間外%') AS after_hours, count(*) FILTER (WHERE available_notes LIKE '%声掛け%') AS call_guard, count(*) FILTER (WHERE available_notes LIKE '%休館%' OR available_notes LIKE '%閉館%' OR available_notes LIKE '%改修%') AS closed_days FROM metro_tokyo.ods.aed WHERE org_code = 't131202'
```

```sql id=orgs
SELECT count(DISTINCT org_code) AS municipalities, count(*) AS rows FROM metro_tokyo.ods.aed
```

```sql id=geo
SELECT count(*) AS total, count(*) FILTER (WHERE address NOT LIKE '%練馬区%') AS outside_ward, count(lat) AS source_latlon, count(geo_lat) AS with_geo, count(*) FILTER (WHERE geo_level IN ('residential_detail', 'residential_block')) AS block_or_better, count(*) FILTER (WHERE ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%') AND geo_lat IS NOT NULL) AS night_with_geo FROM metro_tokyo.ods.aed WHERE org_code = 't131202'
```

```sql id=areas
SELECT (SELECT count(*) FROM e_stat.boundary.small_area WHERE city_name = '練馬区') AS boundary_areas, (SELECT count(DISTINCT area_name) FROM metro_tokyo.ods.population WHERE organization_name = '練馬区' AND survey_date = '2026-06-01') AS population_areas
```

```sql id=coverage
WITH area AS (SELECT regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(area_name, '一丁目$', '1丁目'), '二丁目$', '2丁目'), '三丁目$', '3丁目'), '四丁目$', '4丁目'), '五丁目$', '5丁目'), '六丁目$', '6丁目'), '七丁目$', '7丁目'), '八丁目$', '8丁目'), '九丁目$', '9丁目') AS k, geometry FROM e_stat.boundary.small_area WHERE city_name = '練馬区'), pop AS (SELECT translate(area_name, '０１２３４５６７８９', '0123456789') AS k, total_population AS pop FROM metro_tokyo.ods.population WHERE organization_name = '練馬区' AND survey_date = '2026-06-01'), aed AS (SELECT geo_lat, geo_lon FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND geo_lat IS NOT NULL AND ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%')), j AS (SELECT p.k, p.pop, count(aed.geo_lat) AS n FROM area a JOIN pop p ON p.k = a.k LEFT JOIN aed ON ST_Contains(a.geometry, ST_Point(aed.geo_lon, aed.geo_lat)) GROUP BY p.k, p.pop) SELECT CASE WHEN n = 0 THEN '夜に使えるAEDが無い' ELSE '夜に使えるAEDがある' END AS coverage, count(*) AS areas, sum(pop) AS pop FROM j GROUP BY 1 ORDER BY pop DESC
```

```sql id=top
WITH area AS (SELECT regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(area_name, '一丁目$', '1丁目'), '二丁目$', '2丁目'), '三丁目$', '3丁目'), '四丁目$', '4丁目'), '五丁目$', '5丁目'), '六丁目$', '6丁目'), '七丁目$', '7丁目'), '八丁目$', '8丁目'), '九丁目$', '9丁目') AS k, geometry FROM e_stat.boundary.small_area WHERE city_name = '練馬区'), pop AS (SELECT translate(area_name, '０１２３４５６７８９', '0123456789') AS k, total_population AS pop FROM metro_tokyo.ods.population WHERE organization_name = '練馬区' AND survey_date = '2026-06-01'), aed AS (SELECT geo_lat, geo_lon FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND geo_lat IS NOT NULL AND ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%')) SELECT p.k AS area, p.pop FROM area a JOIN pop p ON p.k = a.k LEFT JOIN aed ON ST_Contains(a.geometry, ST_Point(aed.geo_lon, aed.geo_lat)) GROUP BY p.k, p.pop HAVING count(aed.geo_lat) = 0 ORDER BY p.pop DESC LIMIT 10
```

```sql id=night_list
SELECT name AS '名称', install_position AS '設置位置', CASE WHEN start_time = '0:00' AND end_time = '24:00' THEN '時刻の欄' ELSE '備考欄' END AS '夜に使えると分かる欄' FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%') ORDER BY 3, 1
```

```sql id=outdoor
SELECT CASE WHEN ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%') THEN '夜に使える18台' ELSE 'それ以外の377台' END AS '区分', CASE WHEN install_position LIKE '%屋外%' THEN '敷地内の屋外' WHEN install_position IS NULL OR install_position = '' THEN '記載なし' ELSE '屋外の記載なし' END AS '設置位置の欄', count(*) AS '台数' FROM metro_tokyo.ods.aed WHERE org_code = 't131202' GROUP BY 1, 2 ORDER BY 1, 3 DESC
```

```sql id=night13
WITH area AS (SELECT regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(area_name, '一丁目$', '1丁目'), '二丁目$', '2丁目'), '三丁目$', '3丁目'), '四丁目$', '4丁目'), '五丁目$', '5丁目'), '六丁目$', '6丁目'), '七丁目$', '7丁目'), '八丁目$', '8丁目'), '九丁目$', '9丁目') AS k, geometry FROM e_stat.boundary.small_area WHERE city_name = '練馬区'), pop AS (SELECT translate(area_name, '０１２３４５６７８９', '0123456789') AS k, total_population AS pop FROM metro_tokyo.ods.population WHERE organization_name = '練馬区' AND survey_date = '2026-06-01'), aed AS (SELECT geo_lat, geo_lon FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND geo_lat IS NOT NULL AND (start_time = '0:00' AND end_time = '24:00')), j AS (SELECT p.k, p.pop, count(aed.geo_lat) AS n FROM area a JOIN pop p ON p.k = a.k LEFT JOIN aed ON ST_Contains(a.geometry, ST_Point(aed.geo_lon, aed.geo_lat)) GROUP BY p.k, p.pop) SELECT CASE WHEN n = 0 THEN '夜に使えるAEDが無い' ELSE '夜に使えるAEDがある' END AS coverage, count(*) AS areas, sum(pop) AS pop FROM j GROUP BY 1 ORDER BY pop DESC
```

```sql id=hall_end
SELECT name, start_time, end_time FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND NOT (start_time = '0:00' AND end_time = '24:00') AND ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%') ORDER BY end_time, name
```

```sql id=provisos
SELECT count(*) AS night, count(*) FILTER (WHERE available_notes LIKE '%機器整備中%') AS maintenance, count(*) FILTER (WHERE available_notes LIKE '%完全閉庁日%') AS office_closed, count(*) FILTER (WHERE available_notes LIKE '%年末年始%') AS new_year, count(*) FILTER (WHERE available_notes IS NULL OR available_notes = '') AS no_notes, count(*) FILTER (WHERE available_notes LIKE '%休館%' OR available_notes LIKE '%閉館%' OR available_notes LIKE '%改修%') AS closed_days FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%')
```

```sql id=no_geo
SELECT name, address, start_time, end_time, available_notes, ((start_time = '0:00' AND end_time = '24:00') OR available_notes LIKE '%時間外%' OR available_notes LIKE '%常時利用可能%' OR available_notes LIKE '%声掛け%') AS night FROM metro_tokyo.ods.aed WHERE org_code = 't131202' AND geo_lat IS NULL ORDER BY name
```
