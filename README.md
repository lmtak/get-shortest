東京近郊区間・相互駅間検証
====

JR東日本の東京近郊区間内の駅相互において、最短距離を計算し、
それらの各区間に新在同一できる新幹線区間が含まれているかを判定する。

## Description

乗車券の出発駅と到着駅をJR東日本の東京近郊区間に所属する駅で指定すると、
距離に関わらず有効日数1日、途中下車不可の乗車券が発券される。
しかし、経路を指定して東京近郊区間に含まれない新幹線区間を含めることで、
経路から算出された距離に応じた有効日数が設定され、100.1kmを超えれば
途中下車が可能となる。

このような経路を指定した乗車券は、みどりの窓口係員に事細かに伝えることで
発券させることもできる。係員の手を煩わせることなく、駅の指定席券売機で
発券可能な区間を一覧にして出力するスクリプトである。

## Demo

以下、出力の一例を示す。

> 東京-熱海 (1046) / 有楽町 大井町 鶴見 新子安 横浜 保土ヶ谷 藤沢 平塚
> 蒲田-勝田 (1413) / 田町 神田 秋葉原 御徒町 三河島 北小金 天王台 内原 勝田
> 本庄-西八王子 (1060) / 北与野 西浦和 国立 日野 西八王子
> 松本-日光 (3607) / みどり湖 下諏訪 長坂 豊田 国立 新小平 中浦和 土呂 小金井 鶴田

書式: 出発駅-到着駅(距離(**0.1km単位**)) / 経路上の分岐において選択した分岐先駅を列挙

## Requirement
Python3

## Usage
```
python3 route_search.py > specify-output-file.txt
```
## Install

route_search.py と route_const.py を同じディレクトリに配置する。

## Licence

MIT

## Author

[lmtak](https://github.com/lmtak)
