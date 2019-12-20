search_shinkansen = [
    set(['熊谷', '籠原', '倉賀野', '高崎']), # 熊谷～高崎
    set(['大宮', '宮原', '行田', '熊谷']),   # 大宮～熊谷
    set(['宇都宮', '岡本', '西那須野', '那須塩原']),   # 宇都宮～那須塩原
    set(['小山', '小金井', '雀宮', '宇都宮']),    # 小山～宇都宮
    set(['大宮', '土呂', '間々田', '小山']),      # 大宮～小山
    set(['大宮', 'さいたま新都心', '浦和', '蕨',  # 上野～大宮
         '川口', '東十条', '鶯谷', '上野']),
    set(['上野', '御徒町', '神田', '東京']),      # 東京～上野
    set(['東京', '有楽町', '田町', '品川']),      # 品川～東京
    set(['品川', '大井町', '蒲田', '鶴見', '新子安',   # 小田原～品川
         '横浜', '保土ヶ谷', '戸塚', '藤沢', '辻堂',
         '平塚', '鴨宮', '小田原']),
    set(['小田原', '早川', '湯河原', '熱海']),         # 熱海～小田原
]

yamanote = set([
    '東京', '有楽町', '新橋', '浜松町', '田町', '品川', '大崎',
    '五反田', '目黒', '恵比寿', '渋谷', '原宿', '代々木', '新宿',
    '新大久保', '高田馬場', '目白', '池袋', '大塚', '巣鴨',
    '駒込', '田端', '西日暮里', '日暮里', '鶯谷', '上野',
    '御徒町', '秋葉原', '神田', '御茶ノ水', '水道橋', '飯田橋',
    '市ヶ谷', '四ツ谷', '信濃町', '千駄ヶ谷',
])

tokunai = set([
    '東京', '有楽町', '新橋', '浜松町', '田町', '品川', '大崎',
    '五反田', '目黒', '恵比寿', '渋谷', '原宿', '代々木', '新宿',
    '新大久保', '高田馬場', '目白', '池袋', '大塚', '巣鴨',
    '駒込', '田端', '西日暮里', '日暮里', '鶯谷', '上野',
    '御徒町', '秋葉原', '神田', '御茶ノ水', '水道橋', '飯田橋',
    '市ヶ谷', '四ツ谷', '信濃町', '千駄ヶ谷',
    '大井町', '大森', '蒲田', '大久保', '東中野', '中野', 
    '高円寺', '阿佐ヶ谷', '荻窪', '西荻窪', '西大井',
    '板橋', '十条', '赤羽', '北赤羽', '浮間舟渡', '上中里',
    '王子', '東十条', '尾久', '三河島', '南千住', '北千住',
    '綾瀬', '亀有', '金町', '浅草橋', '両国', '錦糸町',
    '亀戸', '平井', '新小岩', '小岩', '新日本橋', '馬喰町',
    '八丁堀', '越中島', '潮見', '新木場', '葛西臨海公園',
])

yokohama = set([
    '矢向', '尻手', '川崎', '八丁畷', '川崎新町', '小田栄',
    '浜川崎', '昭和', '扇町', '武蔵白石', '大川', '安善',
    '浅野', '新芝浦', '海芝浦', '弁天橋', '武蔵小野', '国道',
    '鶴見', '羽沢横浜国大', '新子安', '東神奈川', '大口',
    '菊名', '新横浜', '小机', '鴨居', '中山', '十日市場',
    '長津田', '横浜', '桜木町', '関内', '石川町', '山手',
    '根岸', '磯子', '新杉田', '洋光台', '港南台', '本郷台',
    '保土ヶ谷', '東戸塚', '戸塚',
])

nodes = (
    {'name1': '品川', 'name2': '大崎', 'dist': 20},
    {'name1': '大崎', 'name2': '五反田', 'dist': 9},
    {'name1': '五反田', 'name2': '目黒', 'dist': 12},
    {'name1': '目黒', 'name2': '恵比寿', 'dist': 15},
    {'name1': '恵比寿', 'name2': '渋谷', 'dist': 16},
    {'name1': '渋谷', 'name2': '原宿', 'dist': 12},
    {'name1': '原宿', 'name2': '代々木', 'dist': 15},
    {'name1': '代々木', 'name2': '新宿', 'dist': 7},
    {'name1': '新宿', 'name2': '新大久保', 'dist': 13},
    {'name1': '新大久保', 'name2': '高田馬場', 'dist': 14},
    {'name1': '高田馬場', 'name2': '目白', 'dist': 9},
    {'name1': '目白', 'name2': '池袋', 'dist': 12},
    {'name1': '池袋', 'name2': '大塚', 'dist': 18},
    {'name1': '大塚', 'name2': '巣鴨', 'dist': 11},
    {'name1': '巣鴨', 'name2': '駒込', 'dist': 7},
    {'name1': '駒込', 'name2': '田端', 'dist': 16},
    {'name1': '田端', 'name2': '西日暮里', 'dist': 8},
    {'name1': '西日暮里', 'name2': '日暮里', 'dist': 5},
    {'name1': '日暮里', 'name2': '鶯谷', 'dist': 11},
    {'name1': '鶯谷', 'name2': '上野', 'dist': 11},
    {'name1': '上野', 'name2': '御徒町', 'dist': 6},
    {'name1': '御徒町', 'name2': '秋葉原', 'dist': 10},
    {'name1': '秋葉原', 'name2': '神田', 'dist': 7},
    {'name1': '神田', 'name2': '東京', 'dist': 13},
    {'name1': '東京', 'name2': '有楽町', 'dist': 8},
    {'name1': '有楽町', 'name2': '新橋', 'dist': 11},
    {'name1': '新橋', 'name2': '浜松町', 'dist': 12},
    {'name1': '浜松町', 'name2': '田町', 'dist': 15},
    {'name1': '田町', 'name2': '品川', 'dist': 22},
    {'name1': '品川', 'name2': '大井町', 'dist': 24},
    {'name1': '大井町', 'name2': '大森', 'dist': 22},
    {'name1': '大森', 'name2': '蒲田', 'dist': 30},
    {'name1': '品川', 'name2': '西大井', 'dist': 36},
    {'name1': '池袋', 'name2': '板橋', 'dist': 18},
    {'name1': '板橋', 'name2': '十条', 'dist': 17},
    {'name1': '十条', 'name2': '赤羽', 'dist': 20},
    {'name1': '赤羽', 'name2': '北赤羽', 'dist': 15},
    {'name1': '北赤羽', 'name2': '浮間舟渡', 'dist': 16},
    {'name1': '田端', 'name2': '上中里', 'dist': 17},
    {'name1': '上中里', 'name2': '王子', 'dist': 11},
    {'name1': '王子', 'name2': '東十条', 'dist': 15},
    {'name1': '東十条', 'name2': '赤羽', 'dist': 18},
    {'name1': '日暮里', 'name2': '尾久', 'dist': 26},
    {'name1': '尾久', 'name2': '赤羽', 'dist': 50},
    {'name1': '東京', 'name2': '八丁堀', 'dist': 12},
    {'name1': '八丁堀', 'name2': '越中島', 'dist': 16},
    {'name1': '越中島', 'name2': '潮見', 'dist': 26},
    {'name1': '潮見', 'name2': '新木場', 'dist': 20},
    {'name1': '新木場', 'name2': '葛西臨海公園', 'dist': 32},
    {'name1': '東京', 'name2': '新日本橋', 'dist': 12},
    {'name1': '新日本橋', 'name2': '馬喰町', 'dist': 11},
    {'name1': '馬喰町', 'name2': '錦糸町', 'dist': 25},
    {'name1': '小岩', 'name2': '新小岩', 'dist': 28},
    {'name1': '新小岩', 'name2': '平井', 'dist': 18},
    {'name1': '平井', 'name2': '亀戸', 'dist': 19},
    {'name1': '亀戸', 'name2': '錦糸町', 'dist': 15},
    {'name1': '錦糸町', 'name2': '両国', 'dist': 15},
    {'name1': '両国', 'name2': '浅草橋', 'dist': 8},
    {'name1': '浅草橋', 'name2': '秋葉原', 'dist': 11},
    {'name1': '秋葉原', 'name2': '御茶ノ水', 'dist': 9},
    {'name1': '神田', 'name2': '御茶ノ水', 'dist': 13},
    {'name1': '御茶ノ水', 'name2': '水道橋', 'dist': 8},
    {'name1': '水道橋', 'name2': '飯田橋', 'dist': 9},
    {'name1': '飯田橋', 'name2': '市ヶ谷', 'dist': 15},
    {'name1': '市ヶ谷', 'name2': '四ツ谷', 'dist': 8},
    {'name1': '四ツ谷', 'name2': '信濃町', 'dist': 13},
    {'name1': '信濃町', 'name2': '千駄ヶ谷', 'dist': 7},
    {'name1': '千駄ヶ谷', 'name2': '代々木', 'dist': 10},
    {'name1': '新宿', 'name2': '大久保', 'dist': 14},
    {'name1': '大久保', 'name2': '東中野', 'dist': 11},
    {'name1': '東中野', 'name2': '中野', 'dist': 19},
    {'name1': '中野', 'name2': '高円寺', 'dist': 14},
    {'name1': '高円寺', 'name2': '阿佐ヶ谷', 'dist': 12},
    {'name1': '阿佐ヶ谷', 'name2': '荻窪', 'dist': 14},
    {'name1': '荻窪', 'name2': '西荻窪', 'dist': 19},
    {'name1': '日暮里', 'name2': '三河島', 'dist': 12},
    {'name1': '三河島', 'name2': '南千住', 'dist': 22},
    {'name1': '南千住', 'name2': '北千住', 'dist': 18},
    {'name1': '北千住', 'name2': '綾瀬', 'dist': 25},
    {'name1': '綾瀬', 'name2': '亀有', 'dist': 22},
    {'name1': '亀有', 'name2': '金町', 'dist': 19},
    {'name1': '蒲田', 'name2': '川崎', 'dist': 38},
    {'name1': '川崎', 'name2': '鶴見', 'dist': 35},
    {'name1': '鶴見', 'name2': '新子安', 'dist': 31},
    {'name1': '新子安', 'name2': '東神奈川', 'dist': 22},
    {'name1': '東神奈川', 'name2': '横浜', 'dist': 18},
    {'name1': '横浜', 'name2': '桜木町', 'dist': 20},
    {'name1': '桜木町', 'name2': '関内', 'dist': 10},
    {'name1': '関内', 'name2': '石川町', 'dist': 8},
    {'name1': '石川町', 'name2': '山手', 'dist': 12},
    {'name1': '山手', 'name2': '根岸', 'dist': 21},
    {'name1': '根岸', 'name2': '磯子', 'dist': 24},
    {'name1': '磯子', 'name2': '新杉田', 'dist': 16},
    {'name1': '新杉田', 'name2': '洋光台', 'dist': 30},
    {'name1': '洋光台', 'name2': '港南台', 'dist': 19},
    {'name1': '港南台', 'name2': '本郷台', 'dist': 25},
    {'name1': '本郷台', 'name2': '大船', 'dist': 36},
    {'name1': '西大井', 'name2': '武蔵小杉', 'dist': 64},
    {'name1': '武蔵小杉', 'name2': '新川崎', 'dist': 27},
    {'name1': '新川崎', 'name2': '鶴見', 'dist': 51},
    {'name1': '横浜', 'name2': '保土ヶ谷', 'dist': 30},
    {'name1': '保土ヶ谷', 'name2': '東戸塚', 'dist': 49},
    {'name1': '東戸塚', 'name2': '戸塚', 'dist': 42},
    {'name1': '戸塚', 'name2': '大船', 'dist': 56},
    {'name1': '大船', 'name2': '藤沢', 'dist': 46},
    {'name1': '藤沢', 'name2': '辻堂', 'dist': 37},
    {'name1': '辻堂', 'name2': '茅ヶ崎', 'dist': 38},
    {'name1': '茅ヶ崎', 'name2': '平塚', 'dist': 52},
    {'name1': '平塚', 'name2': '大磯', 'dist': 40},
    {'name1': '大磯', 'name2': '二宮', 'dist': 53},
    {'name1': '二宮', 'name2': '国府津', 'dist': 46},
    {'name1': '国府津', 'name2': '鴨宮', 'dist': 31},
    {'name1': '鴨宮', 'name2': '小田原', 'dist': 31},
    {'name1': '小田原', 'name2': '早川', 'dist': 21},
    {'name1': '早川', 'name2': '根府川', 'dist': 44},
    {'name1': '根府川', 'name2': '真鶴', 'dist': 54},
    {'name1': '真鶴', 'name2': '湯河原', 'dist': 33},
    {'name1': '湯河原', 'name2': '熱海', 'dist': 55},
    {'name1': '熱海', 'name2': '来宮', 'dist': 12},
    {'name1': '来宮', 'name2': '伊豆多賀', 'dist': 48},
    {'name1': '伊豆多賀', 'name2': '網代', 'dist': 27},
    {'name1': '網代', 'name2': '宇佐美', 'dist': 43},
    {'name1': '宇佐美', 'name2': '伊東', 'dist': 39},
    {'name1': '大船', 'name2': '北鎌倉', 'dist': 23},
    {'name1': '北鎌倉', 'name2': '鎌倉', 'dist': 22},
    {'name1': '鎌倉', 'name2': '逗子', 'dist': 39},
    {'name1': '逗子', 'name2': '東逗子', 'dist': 20},
    {'name1': '東逗子', 'name2': '田浦', 'dist': 34},
    {'name1': '田浦', 'name2': '横須賀', 'dist': 21},
    {'name1': '横須賀', 'name2': '衣笠', 'dist': 34},
    {'name1': '衣笠', 'name2': '久里浜', 'dist': 46},
    {'name1': '鶴見', 'name2': '国道', 'dist': 9},
    {'name1': '国道', 'name2': '鶴見小野', 'dist': 6},
    {'name1': '鶴見小野', 'name2': '弁天橋', 'dist': 9},
    {'name1': '弁天橋', 'name2': '浅野', 'dist': 6},
    {'name1': '浅野', 'name2': '安善', 'dist': 5},
    {'name1': '安善', 'name2': '武蔵白石', 'dist': 6},
    {'name1': '武蔵白石', 'name2': '浜川崎', 'dist': 16},
    {'name1': '浜川崎', 'name2': '昭和', 'dist': 7},
    {'name1': '昭和', 'name2': '扇町', 'dist': 6},
    {'name1': '浅野', 'name2': '新芝浦', 'dist': 9},
    {'name1': '新芝浦', 'name2': '海芝浦', 'dist': 8},
    {'name1': '安善', 'name2': '大川', 'dist': 16},
    {'name1': '浜川崎', 'name2': '小田栄', 'dist': 14},
    {'name1': '小田栄', 'name2': '川崎新町', 'dist': 7},
    {'name1': '川崎新町', 'name2': '八丁畷', 'dist': 9},
    {'name1': '八丁畷', 'name2': '尻手', 'dist': 11},
    {'name1': '川崎', 'name2': '尻手', 'dist': 17},
    {'name1': '尻手', 'name2': '矢向', 'dist': 9},
    {'name1': '矢向', 'name2': '鹿島田', 'dist': 15},
    {'name1': '鹿島田', 'name2': '平間', 'dist': 12},
    {'name1': '平間', 'name2': '向河原', 'dist': 13},
    {'name1': '向河原', 'name2': '武蔵小杉', 'dist': 9},
    {'name1': '武蔵小杉', 'name2': '武蔵中原', 'dist': 17},
    {'name1': '武蔵中原', 'name2': '武蔵新城', 'dist': 13},
    {'name1': '武蔵新城', 'name2': '武蔵溝ノ口', 'dist': 22},
    {'name1': '武蔵溝ノ口', 'name2': '津田山', 'dist': 12},
    {'name1': '津田山', 'name2': '久地', 'dist': 10},
    {'name1': '久地', 'name2': '宿河原', 'dist': 13},
    {'name1': '宿河原', 'name2': '登戸', 'dist': 11},
    {'name1': '登戸', 'name2': '中野島', 'dist': 22},
    {'name1': '中野島', 'name2': '稲田堤', 'dist': 13},
    {'name1': '稲田堤', 'name2': '矢野口', 'dist': 16},
    {'name1': '矢野口', 'name2': '稲城長沼', 'dist': 17},
    {'name1': '稲城長沼', 'name2': '南多摩', 'dist': 14},
    {'name1': '南多摩', 'name2': '府中本町', 'dist': 24},
    {'name1': '府中本町', 'name2': '分倍河原', 'dist': 9},
    {'name1': '分倍河原', 'name2': '西府', 'dist': 12},
    {'name1': '西府', 'name2': '谷保', 'dist': 16},
    {'name1': '谷保', 'name2': '矢川', 'dist': 14},
    {'name1': '矢川', 'name2': '西国立', 'dist': 13},
    {'name1': '西国立', 'name2': '立川', 'dist': 12},
    {'name1': '東神奈川', 'name2': '大口', 'dist': 22},
    {'name1': '大口', 'name2': '菊名', 'dist': 26},
    {'name1': '菊名', 'name2': '新横浜', 'dist': 13},
    {'name1': '新横浜', 'name2': '小机', 'dist': 17},
    {'name1': '小机', 'name2': '鴨居', 'dist': 31},
    {'name1': '鴨居', 'name2': '中山', 'dist': 26},
    {'name1': '中山', 'name2': '十日市場', 'dist': 24},
    {'name1': '十日市場', 'name2': '長津田', 'dist': 20},
    {'name1': '長津田', 'name2': '成瀬', 'dist': 23},
    {'name1': '成瀬', 'name2': '町田', 'dist': 27},
    {'name1': '町田', 'name2': '古淵', 'dist': 28},
    {'name1': '古淵', 'name2': '淵野辺', 'dist': 27},
    {'name1': '淵野辺', 'name2': '矢部', 'dist': 8},
    {'name1': '矢部', 'name2': '相模原', 'dist': 18},
    {'name1': '相模原', 'name2': '橋本', 'dist': 28},
    {'name1': '橋本', 'name2': '相原', 'dist': 19},
    {'name1': '相原', 'name2': '八王子みなみ野', 'dist': 29},
    {'name1': '八王子みなみ野', 'name2': '片倉', 'dist': 14},
    {'name1': '片倉', 'name2': '八王子', 'dist': 26},
    {'name1': '茅ヶ崎', 'name2': '北茅ヶ崎', 'dist': 13},
    {'name1': '北茅ヶ崎', 'name2': '香川', 'dist': 21},
    {'name1': '香川', 'name2': '寒川', 'dist': 17},
    {'name1': '寒川', 'name2': '宮山', 'dist': 21},
    {'name1': '宮山', 'name2': '倉見', 'dist': 14},
    {'name1': '倉見', 'name2': '門沢橋', 'dist': 14},
    {'name1': '門沢橋', 'name2': '社家', 'dist': 16},
    {'name1': '社家', 'name2': '厚木', 'dist': 26},
    {'name1': '厚木', 'name2': '海老名', 'dist': 17},
    {'name1': '海老名', 'name2': '入谷', 'dist': 30},
    {'name1': '入谷', 'name2': '相武台下', 'dist': 17},
    {'name1': '相武台下', 'name2': '下溝', 'dist': 29},
    {'name1': '下溝', 'name2': '原当麻', 'dist': 13},
    {'name1': '原当麻', 'name2': '番田', 'dist': 21},
    {'name1': '番田', 'name2': '上溝', 'dist': 15},
    {'name1': '上溝', 'name2': '南橋本', 'dist': 29},
    {'name1': '南橋本', 'name2': '橋本', 'dist': 20},
    {'name1': '葛西臨海公園', 'name2': '舞浜', 'dist': 21},
    {'name1': '舞浜', 'name2': '新浦安', 'dist': 34},
    {'name1': '新浦安', 'name2': '市川塩浜', 'dist': 21},
    {'name1': '市川塩浜', 'name2': '二俣新町', 'dist': 44},
    {'name1': '二俣新町', 'name2': '南船橋', 'dist': 34},
    {'name1': '南船橋', 'name2': '新習志野', 'dist': 23},
    {'name1': '新習志野', 'name2': '海浜幕張', 'dist': 34},
    {'name1': '海浜幕張', 'name2': '検見川浜', 'dist': 20},
    {'name1': '検見川浜', 'name2': '稲毛海岸', 'dist': 16},
    {'name1': '稲毛海岸', 'name2': '千葉みなと', 'dist': 37},
    {'name1': '千葉みなと', 'name2': '蘇我', 'dist': 40},
    {'name1': '市川塩浜', 'name2': '西船橋', 'dist': 59},
    {'name1': '南船橋', 'name2': '西船橋', 'dist': 54},
    {'name1': '小岩', 'name2': '市川', 'dist': 26},
    {'name1': '市川', 'name2': '本八幡', 'dist': 20},
    {'name1': '本八幡', 'name2': '下総中山', 'dist': 16},
    {'name1': '下総中山', 'name2': '西船橋', 'dist': 16},
    {'name1': '西船橋', 'name2': '船橋', 'dist': 26},
    {'name1': '船橋', 'name2': '東船橋', 'dist': 18},
    {'name1': '東船橋', 'name2': '津田沼', 'dist': 17},
    {'name1': '津田沼', 'name2': '幕張本郷', 'dist': 29},
    {'name1': '幕張本郷', 'name2': '幕張', 'dist': 20},
    {'name1': '幕張', 'name2': '新検見川', 'dist': 16},
    {'name1': '新検見川', 'name2': '稲毛', 'dist': 27},
    {'name1': '稲毛', 'name2': '西千葉', 'dist': 19},
    {'name1': '西千葉', 'name2': '千葉', 'dist': 14},
    {'name1': '千葉', 'name2': '本千葉', 'dist': 14},
    {'name1': '本千葉', 'name2': '蘇我', 'dist': 24},
    {'name1': '蘇我', 'name2': '鎌取', 'dist': 50},
    {'name1': '鎌取', 'name2': '誉田', 'dist': 38},
    {'name1': '誉田', 'name2': '土気', 'dist': 55},
    {'name1': '土気', 'name2': '大網', 'dist': 48},
    {'name1': '大網', 'name2': '永田', 'dist': 24},
    {'name1': '永田', 'name2': '本納', 'dist': 24},
    {'name1': '本納', 'name2': '新茂原', 'dist': 37},
    {'name1': '新茂原', 'name2': '茂原', 'dist': 29},
    {'name1': '茂原', 'name2': '八積', 'dist': 46},
    {'name1': '八積', 'name2': '上総一ノ宮', 'dist': 41},
    {'name1': '上総一ノ宮', 'name2': '東浪見', 'dist': 32},
    {'name1': '東浪見', 'name2': '太東', 'dist': 31},
    {'name1': '太東', 'name2': '長者町', 'dist': 28},
    {'name1': '長者町', 'name2': '三門', 'dist': 16},
    {'name1': '三門', 'name2': '大原', 'dist': 35},
    {'name1': '大原', 'name2': '浪花', 'dist': 33},
    {'name1': '浪花', 'name2': '御宿', 'dist': 49},
    {'name1': '御宿', 'name2': '勝浦', 'dist': 55},
    {'name1': '勝浦', 'name2': '鵜原', 'dist': 36},
    {'name1': '鵜原', 'name2': '上総興津', 'dist': 27},
    {'name1': '上総興津', 'name2': '行川アイランド', 'dist': 33},
    {'name1': '行川アイランド', 'name2': '安房小湊', 'dist': 38},
    {'name1': '安房小湊', 'name2': '安房天津', 'dist': 34},
    {'name1': '安房天津', 'name2': '安房鴨川', 'dist': 56},
    {'name1': '蘇我', 'name2': '浜野', 'dist': 34},
    {'name1': '浜野', 'name2': '八幡宿', 'dist': 22},
    {'name1': '八幡宿', 'name2': '五井', 'dist': 37},
    {'name1': '五井', 'name2': '姉ヶ崎', 'dist': 58},
    {'name1': '姉ヶ崎', 'name2': '長浦', 'dist': 54},
    {'name1': '長浦', 'name2': '袖ヶ浦', 'dist': 39},
    {'name1': '袖ヶ浦', 'name2': '巌根', 'dist': 31},
    {'name1': '巌根', 'name2': '木更津', 'dist': 38},
    {'name1': '木更津', 'name2': '君津', 'dist': 70},
    {'name1': '君津', 'name2': '青堀', 'dist': 37},
    {'name1': '青堀', 'name2': '大貫', 'dist': 46},
    {'name1': '大貫', 'name2': '佐貫町', 'dist': 41},
    {'name1': '佐貫町', 'name2': '上総湊', 'dist': 44},
    {'name1': '上総湊', 'name2': '竹岡', 'dist': 51},
    {'name1': '竹岡', 'name2': '浜金谷', 'dist': 38},
    {'name1': '浜金谷', 'name2': '保田', 'dist': 35},
    {'name1': '保田', 'name2': '安房勝山', 'dist': 33},
    {'name1': '安房勝山', 'name2': '岩井', 'dist': 29},
    {'name1': '岩井', 'name2': '富浦', 'dist': 61},
    {'name1': '富浦', 'name2': '那古船形', 'dist': 23},
    {'name1': '那古船形', 'name2': '館山', 'dist': 38},
    {'name1': '館山', 'name2': '九重', 'dist': 58},
    {'name1': '九重', 'name2': '千倉', 'dist': 49},
    {'name1': '千倉', 'name2': '千歳', 'dist': 20},
    {'name1': '千歳', 'name2': '南三原', 'dist': 36},
    {'name1': '南三原', 'name2': '和田浦', 'dist': 46},
    {'name1': '和田浦', 'name2': '江見', 'dist': 46},
    {'name1': '江見', 'name2': '太海', 'dist': 46},
    {'name1': '太海', 'name2': '安房鴨川', 'dist': 34},
    {'name1': '木更津', 'name2': '祇園', 'dist': 29},
    {'name1': '祇園', 'name2': '上総清川', 'dist': 17},
    {'name1': '上総清川', 'name2': '東清川', 'dist': 21},
    {'name1': '東清川', 'name2': '横田', 'dist': 35},
    {'name1': '横田', 'name2': '東横田', 'dist': 17},
    {'name1': '東横田', 'name2': '馬来田', 'dist': 34},
    {'name1': '馬来田', 'name2': '下郡', 'dist': 14},
    {'name1': '下郡', 'name2': '小櫃', 'dist': 33},
    {'name1': '小櫃', 'name2': '俵田', 'dist': 20},
    {'name1': '俵田', 'name2': '久留里', 'dist': 29},
    {'name1': '久留里', 'name2': '平山', 'dist': 34},
    {'name1': '平山', 'name2': '上総松丘', 'dist': 28},
    {'name1': '上総松丘', 'name2': '上総亀山', 'dist': 43},
    {'name1': '大網', 'name2': '福俵', 'dist': 36},
    {'name1': '福俵', 'name2': '東金', 'dist': 28},
    {'name1': '東金', 'name2': '求名', 'dist': 42},
    {'name1': '求名', 'name2': '成東', 'dist': 46},
    {'name1': '千葉', 'name2': '東千葉', 'dist': 9},
    {'name1': '東千葉', 'name2': '都賀', 'dist': 33},
    {'name1': '都賀', 'name2': '四街道', 'dist': 35},
    {'name1': '四街道', 'name2': '物井', 'dist': 42},
    {'name1': '物井', 'name2': '佐倉', 'dist': 42},
    {'name1': '佐倉', 'name2': '南酒々井', 'dist': 40},
    {'name1': '南酒々井', 'name2': '榎戸', 'dist': 29},
    {'name1': '榎戸', 'name2': '八街', 'dist': 37},
    {'name1': '八街', 'name2': '日向', 'dist': 58},
    {'name1': '日向', 'name2': '成東', 'dist': 52},
    {'name1': '成東', 'name2': '松尾', 'dist': 56},
    {'name1': '松尾', 'name2': '横芝', 'dist': 43},
    {'name1': '横芝', 'name2': '飯倉', 'dist': 38},
    {'name1': '飯倉', 'name2': '八日市場', 'dist': 31},
    {'name1': '八日市場', 'name2': '干潟', 'dist': 51},
    {'name1': '干潟', 'name2': '旭', 'dist': 48},
    {'name1': '旭', 'name2': '飯岡', 'dist': 27},
    {'name1': '飯岡', 'name2': '倉橋', 'dist': 29},
    {'name1': '倉橋', 'name2': '猿田', 'dist': 26},
    {'name1': '猿田', 'name2': '松岸', 'dist': 55},
    {'name1': '松岸', 'name2': '銚子', 'dist': 32},
    {'name1': '佐倉', 'name2': '酒々井', 'dist': 42},
    {'name1': '酒々井', 'name2': '成田', 'dist': 64},
    {'name1': '成田', 'name2': '空港第２ビル', 'dist': 98},
    {'name1': '空港第２ビル', 'name2': '成田空港', 'dist': 10},
    {'name1': '成田', 'name2': '久住', 'dist': 69},
    {'name1': '久住', 'name2': '滑河', 'dist': 55},
    {'name1': '滑河', 'name2': '下総神崎', 'dist': 61},
    {'name1': '下総神崎', 'name2': '大戸', 'dist': 45},
    {'name1': '大戸', 'name2': '佐原', 'dist': 39},
    {'name1': '佐原', 'name2': '香取', 'dist': 36},
    {'name1': '香取', 'name2': '水郷', 'dist': 39},
    {'name1': '水郷', 'name2': '小見川', 'dist': 52},
    {'name1': '小見川', 'name2': '笹川', 'dist': 50},
    {'name1': '笹川', 'name2': '下総橘', 'dist': 52},
    {'name1': '下総橘', 'name2': '下総豊里', 'dist': 33},
    {'name1': '下総豊里', 'name2': '椎柴', 'dist': 48},
    {'name1': '椎柴', 'name2': '松岸', 'dist': 44},
    {'name1': '香取', 'name2': '十二橋', 'dist': 33},
    {'name1': '十二橋', 'name2': '潮来', 'dist': 24},
    {'name1': '潮来', 'name2': '延方', 'dist': 57},
    {'name1': '延方', 'name2': '鹿島神宮', 'dist': 42},
    {'name1': '鹿島神宮', 'name2': '鹿島サッカースタジアム', 'dist': 35},
    {'name1': '成田', 'name2': '下総松崎', 'dist': 56},
    {'name1': '下総松崎', 'name2': '安食', 'dist': 41},
    {'name1': '安食', 'name2': '小林', 'dist': 49},
    {'name1': '小林', 'name2': '木下', 'dist': 43},
    {'name1': '木下', 'name2': '布佐', 'dist': 19},
    {'name1': '布佐', 'name2': '新木', 'dist': 32},
    {'name1': '新木', 'name2': '湖北', 'dist': 26},
    {'name1': '湖北', 'name2': '東我孫子', 'dist': 29},
    {'name1': '東我孫子', 'name2': '我孫子', 'dist': 34},
    {'name1': '金町', 'name2': '松戸', 'dist': 39},
    {'name1': '松戸', 'name2': '北松戸', 'dist': 21},
    {'name1': '北松戸', 'name2': '馬橋', 'dist': 13},
    {'name1': '馬橋', 'name2': '新松戸', 'dist': 16},
    {'name1': '新松戸', 'name2': '北小金', 'dist': 13},
    {'name1': '北小金', 'name2': '南柏', 'dist': 25},
    {'name1': '南柏', 'name2': '柏', 'dist': 24},
    {'name1': '柏', 'name2': '北柏', 'dist': 23},
    {'name1': '北柏', 'name2': '我孫子', 'dist': 21},
    {'name1': '我孫子', 'name2': '天王台', 'dist': 27},
    {'name1': '天王台', 'name2': '取手', 'dist': 34},
    {'name1': '取手', 'name2': '藤代', 'dist': 60},
    {'name1': '藤代', 'name2': '佐貫', 'dist': 21},
    {'name1': '佐貫', 'name2': '牛久', 'dist': 51},
    {'name1': '牛久', 'name2': 'ひたち野うしく', 'dist': 39},
    {'name1': 'ひたち野うしく', 'name2': '荒川沖', 'dist': 27},
    {'name1': '荒川沖', 'name2': '土浦', 'dist': 66},
    {'name1': '土浦', 'name2': '神立', 'dist': 61},
    {'name1': '神立', 'name2': '高浜', 'dist': 65},
    {'name1': '高浜', 'name2': '石岡', 'dist': 36},
    {'name1': '石岡', 'name2': '羽鳥', 'dist': 65},
    {'name1': '羽鳥', 'name2': '岩間', 'dist': 54},
    {'name1': '岩間', 'name2': '友部', 'dist': 69},
    {'name1': '友部', 'name2': '内原', 'dist': 47},
    {'name1': '内原', 'name2': '赤塚', 'dist': 58},
    {'name1': '赤塚', 'name2': '水戸', 'dist': 60},
    {'name1': '赤羽', 'name2': '川口', 'dist': 26},
    {'name1': '川口', 'name2': '西川口', 'dist': 20},
    {'name1': '西川口', 'name2': '蕨', 'dist': 19},
    {'name1': '蕨', 'name2': '南浦和', 'dist': 28},
    {'name1': '南浦和', 'name2': '浦和', 'dist': 17},
    {'name1': '浦和', 'name2': '北浦和', 'dist': 18},
    {'name1': '北浦和', 'name2': '与野', 'dist': 16},
    {'name1': '与野', 'name2': 'さいたま新都心', 'dist': 11},
    {'name1': 'さいたま新都心', 'name2': '大宮', 'dist': 16},
    {'name1': '大宮', 'name2': '土呂', 'dist': 30},
    {'name1': '土呂', 'name2': '東大宮', 'dist': 21},
    {'name1': '東大宮', 'name2': '蓮田', 'dist': 38},
    {'name1': '蓮田', 'name2': '白岡', 'dist': 43},
    {'name1': '白岡', 'name2': '新白岡', 'dist': 24},
    {'name1': '新白岡', 'name2': '久喜', 'dist': 30},
    {'name1': '久喜', 'name2': '東鷲宮', 'dist': 27},
    {'name1': '東鷲宮', 'name2': '栗橋', 'dist': 56},
    {'name1': '栗橋', 'name2': '古河', 'dist': 75},
    {'name1': '古河', 'name2': '野木', 'dist': 47},
    {'name1': '野木', 'name2': '間々田', 'dist': 39},
    {'name1': '間々田', 'name2': '小山', 'dist': 73},
    {'name1': '小山', 'name2': '小金井', 'dist': 75},
    {'name1': '小金井', 'name2': '自治医大', 'dist': 26},
    {'name1': '自治医大', 'name2': '石橋', 'dist': 47},
    {'name1': '石橋', 'name2': '雀宮', 'dist': 74},
    {'name1': '雀宮', 'name2': '宇都宮', 'dist': 77},
    {'name1': '浮間舟渡', 'name2': '戸田公園', 'dist': 24},
    {'name1': '戸田公園', 'name2': '戸田', 'dist': 13},
    {'name1': '戸田', 'name2': '北戸田', 'dist': 14},
    {'name1': '北戸田', 'name2': '武蔵浦和', 'dist': 24},
    {'name1': '武蔵浦和', 'name2': '中浦和', 'dist': 12},
    {'name1': '中浦和', 'name2': '南与野', 'dist': 17},
    {'name1': '南与野', 'name2': '与野本町', 'dist': 16},
    {'name1': '与野本町', 'name2': '北与野', 'dist': 11},
    {'name1': '北与野', 'name2': '大宮', 'dist': 18},
    {'name1': '大宮', 'name2': '日進', 'dist': 37},
    {'name1': '日進', 'name2': '西大宮', 'dist': 26},
    {'name1': '西大宮', 'name2': '指扇', 'dist': 14},
    {'name1': '指扇', 'name2': '南古谷', 'dist': 47},
    {'name1': '南古谷', 'name2': '川越', 'dist': 37},
    {'name1': '川越', 'name2': '西川越', 'dist': 26},
    {'name1': '西川越', 'name2': '的場', 'dist': 22},
    {'name1': '的場', 'name2': '笠幡', 'dist': 29},
    {'name1': '笠幡', 'name2': '武蔵高萩', 'dist': 32},
    {'name1': '武蔵高萩', 'name2': '高麗川', 'dist': 36},
    {'name1': '大宮', 'name2': '宮原', 'dist': 40},
    {'name1': '宮原', 'name2': '上尾', 'dist': 42},
    {'name1': '上尾', 'name2': '北上尾', 'dist': 17},
    {'name1': '北上尾', 'name2': '桶川', 'dist': 19},
    {'name1': '桶川', 'name2': '北本', 'dist': 46},
    {'name1': '北本', 'name2': '鴻巣', 'dist': 36},
    {'name1': '鴻巣', 'name2': '北鴻巣', 'dist': 43},
    {'name1': '北鴻巣', 'name2': '吹上', 'dist': 30},
    {'name1': '吹上', 'name2': '行田', 'dist': 23},
    {'name1': '行田', 'name2': '熊谷', 'dist': 48},
    {'name1': '熊谷', 'name2': '籠原', 'dist': 66},
    {'name1': '籠原', 'name2': '深谷', 'dist': 48},
    {'name1': '深谷', 'name2': '岡部', 'dist': 43},
    {'name1': '岡部', 'name2': '本庄', 'dist': 56},
    {'name1': '本庄', 'name2': '神保原', 'dist': 40},
    {'name1': '神保原', 'name2': '新町', 'dist': 45},
    {'name1': '新町', 'name2': '倉賀野', 'dist': 61},
    {'name1': '倉賀野', 'name2': '高崎', 'dist': 44},
    {'name1': '高崎', 'name2': '高崎問屋町', 'dist': 28},
    {'name1': '高崎問屋町', 'name2': '井野', 'dist': 12},
    {'name1': '井野', 'name2': '新前橋', 'dist': 33},
    {'name1': '新前橋', 'name2': '群馬総社', 'dist': 48},
    {'name1': '群馬総社', 'name2': '八木原', 'dist': 56},
    {'name1': '八木原', 'name2': '渋川', 'dist': 34},
    {'name1': '西荻窪', 'name2': '吉祥寺', 'dist': 19},
    {'name1': '吉祥寺', 'name2': '三鷹', 'dist': 16},
    {'name1': '三鷹', 'name2': '武蔵境', 'dist': 16},
    {'name1': '武蔵境', 'name2': '東小金井', 'dist': 17},
    {'name1': '東小金井', 'name2': '武蔵小金井', 'dist': 17},
    {'name1': '武蔵小金井', 'name2': '国分寺', 'dist': 23},
    {'name1': '国分寺', 'name2': '西国分寺', 'dist': 14},
    {'name1': '西国分寺', 'name2': '国立', 'dist': 17},
    {'name1': '国立', 'name2': '立川', 'dist': 30},
    {'name1': '立川', 'name2': '日野', 'dist': 33},
    {'name1': '日野', 'name2': '豊田', 'dist': 23},
    {'name1': '豊田', 'name2': '八王子', 'dist': 43},
    {'name1': '八王子', 'name2': '西八王子', 'dist': 24},
    {'name1': '西八王子', 'name2': '高尾', 'dist': 33},
    {'name1': '高尾', 'name2': '相模湖', 'dist': 95},
    {'name1': '相模湖', 'name2': '藤野', 'dist': 37},
    {'name1': '藤野', 'name2': '上野原', 'dist': 35},
    {'name1': '上野原', 'name2': '四方津', 'dist': 42},
    {'name1': '四方津', 'name2': '梁川', 'dist': 36},
    {'name1': '梁川', 'name2': '鳥沢', 'dist': 36},
    {'name1': '鳥沢', 'name2': '猿橋', 'dist': 41},
    {'name1': '猿橋', 'name2': '大月', 'dist': 25},
    {'name1': '立川', 'name2': '西立川', 'dist': 19},
    {'name1': '西立川', 'name2': '東中神', 'dist': 8},
    {'name1': '東中神', 'name2': '中神', 'dist': 9},
    {'name1': '中神', 'name2': '昭島', 'dist': 14},
    {'name1': '昭島', 'name2': '拝島', 'dist': 19},
    {'name1': '拝島', 'name2': '牛浜', 'dist': 17},
    {'name1': '牛浜', 'name2': '福生', 'dist': 10},
    {'name1': '福生', 'name2': '羽村', 'dist': 21},
    {'name1': '羽村', 'name2': '小作', 'dist': 24},
    {'name1': '小作', 'name2': '河辺', 'dist': 18},
    {'name1': '河辺', 'name2': '東青梅', 'dist': 13},
    {'name1': '東青梅', 'name2': '青梅', 'dist': 13},
    {'name1': '青梅', 'name2': '宮ノ平', 'dist': 21},
    {'name1': '宮ノ平', 'name2': '日向和田', 'dist': 8},
    {'name1': '日向和田', 'name2': '石神前', 'dist': 10},
    {'name1': '石神前', 'name2': '二俣尾', 'dist': 12},
    {'name1': '二俣尾', 'name2': '軍畑', 'dist': 9},
    {'name1': '軍畑', 'name2': '沢井', 'dist': 14},
    {'name1': '沢井', 'name2': '御嶽', 'dist': 13},
    {'name1': '御嶽', 'name2': '川井', 'dist': 28},
    {'name1': '川井', 'name2': '古里', 'dist': 16},
    {'name1': '古里', 'name2': '鳩ノ巣', 'dist': 22},
    {'name1': '鳩ノ巣', 'name2': '白丸', 'dist': 14},
    {'name1': '白丸', 'name2': '奥多摩', 'dist': 20},
    {'name1': '拝島', 'name2': '熊川', 'dist': 11},
    {'name1': '熊川', 'name2': '東秋留', 'dist': 24},
    {'name1': '東秋留', 'name2': '秋川', 'dist': 22},
    {'name1': '秋川', 'name2': '武蔵引田', 'dist': 15},
    {'name1': '武蔵引田', 'name2': '武蔵増戸', 'dist': 13},
    {'name1': '武蔵増戸', 'name2': '武蔵五日市', 'dist': 26},
    {'name1': '西船橋', 'name2': '船橋法典', 'dist': 29},
    {'name1': '船橋法典', 'name2': '市川大野', 'dist': 30},
    {'name1': '市川大野', 'name2': '東松戸', 'dist': 19},
    {'name1': '東松戸', 'name2': '新八柱', 'dist': 24},
    {'name1': '新八柱', 'name2': '新松戸', 'dist': 41},
    {'name1': '新松戸', 'name2': '南流山', 'dist': 21},
    {'name1': '南流山', 'name2': '三郷', 'dist': 20},
    {'name1': '三郷', 'name2': '新三郷', 'dist': 21},
    {'name1': '新三郷', 'name2': '吉川美南', 'dist': 15},
    {'name1': '吉川美南', 'name2': '吉川', 'dist': 16},
    {'name1': '吉川', 'name2': '越谷レイクタウン', 'dist': 19},
    {'name1': '越谷レイクタウン', 'name2': '南越谷', 'dist': 28},
    {'name1': '南越谷', 'name2': '東川口', 'dist': 43},
    {'name1': '東川口', 'name2': '東浦和', 'dist': 38},
    {'name1': '東浦和', 'name2': '南浦和', 'dist': 37},
    {'name1': '南浦和', 'name2': '武蔵浦和', 'dist': 19},
    {'name1': '武蔵浦和', 'name2': '西浦和', 'dist': 20},
    {'name1': '西浦和', 'name2': '北朝霞', 'dist': 50},
    {'name1': '北朝霞', 'name2': '新座', 'dist': 31},
    {'name1': '新座', 'name2': '東所沢', 'dist': 40},
    {'name1': '東所沢', 'name2': '新秋津', 'dist': 27},
    {'name1': '新秋津', 'name2': '新小平', 'dist': 56},
    {'name1': '新小平', 'name2': '西国分寺', 'dist': 35},
    {'name1': '西国分寺', 'name2': '北府中', 'dist': 22},
    {'name1': '北府中', 'name2': '府中本町', 'dist': 17},
    {'name1': '友部', 'name2': '宍戸', 'dist': 17},
    {'name1': '宍戸', 'name2': '笠間', 'dist': 52},
    {'name1': '笠間', 'name2': '稲田', 'dist': 32},
    {'name1': '稲田', 'name2': '福原', 'dist': 31},
    {'name1': '福原', 'name2': '羽黒', 'dist': 42},
    {'name1': '羽黒', 'name2': '岩瀬', 'dist': 32},
    {'name1': '岩瀬', 'name2': '大和', 'dist': 37},
    {'name1': '大和', 'name2': '新治', 'dist': 36},
    {'name1': '新治', 'name2': '下館', 'dist': 61},
    {'name1': '下館', 'name2': '玉戸', 'dist': 37},
    {'name1': '玉戸', 'name2': '川島', 'dist': 21},
    {'name1': '川島', 'name2': '東結城', 'dist': 21},
    {'name1': '東結城', 'name2': '結城', 'dist': 17},
    {'name1': '結城', 'name2': '小田林', 'dist': 17},
    {'name1': '小田林', 'name2': '小山', 'dist': 49},
    {'name1': '小山', 'name2': '思川', 'dist': 54},
    {'name1': '思川', 'name2': '栃木', 'dist': 54},
    {'name1': '栃木', 'name2': '大平下', 'dist': 44},
    {'name1': '大平下', 'name2': '岩舟', 'dist': 41},
    {'name1': '岩舟', 'name2': '佐野', 'dist': 73},
    {'name1': '佐野', 'name2': '富田', 'dist': 45},
    {'name1': '富田', 'name2': '足利', 'dist': 71},
    {'name1': '足利', 'name2': '山前', 'dist': 45},
    {'name1': '山前', 'name2': '小俣', 'dist': 46},
    {'name1': '小俣', 'name2': '桐生', 'dist': 56},
    {'name1': '桐生', 'name2': '岩宿', 'dist': 40},
    {'name1': '岩宿', 'name2': '国定', 'dist': 64},
    {'name1': '国定', 'name2': '伊勢崎', 'dist': 58},
    {'name1': '伊勢崎', 'name2': '駒形', 'dist': 58},
    {'name1': '駒形', 'name2': '前橋大島', 'dist': 32},
    {'name1': '前橋大島', 'name2': '前橋', 'dist': 38},
    {'name1': '前橋', 'name2': '新前橋', 'dist': 25},
    {'name1': '八王子', 'name2': '北八王子', 'dist': 34},
    {'name1': '北八王子', 'name2': '小宮', 'dist': 22},
    {'name1': '小宮', 'name2': '拝島', 'dist': 53},
    {'name1': '拝島', 'name2': '東福生', 'dist': 31},
    {'name1': '東福生', 'name2': '箱根ヶ崎', 'dist': 33},
    {'name1': '箱根ヶ崎', 'name2': '金子', 'dist': 53},
    {'name1': '金子', 'name2': '東飯能', 'dist': 56},
    {'name1': '東飯能', 'name2': '高麗川', 'dist': 60},
    {'name1': '高麗川', 'name2': '毛呂', 'dist': 64},
    {'name1': '毛呂', 'name2': '越生', 'dist': 30},
    {'name1': '越生', 'name2': '明覚', 'dist': 57},
    {'name1': '明覚', 'name2': '小川町', 'dist': 88},
    {'name1': '小川町', 'name2': '竹沢', 'dist': 38},
    {'name1': '竹沢', 'name2': '折原', 'dist': 44},
    {'name1': '折原', 'name2': '寄居', 'dist': 40},
    {'name1': '寄居', 'name2': '用土', 'dist': 49},
    {'name1': '用土', 'name2': '松久', 'dist': 30},
    {'name1': '松久', 'name2': '児玉', 'dist': 53},
    {'name1': '児玉', 'name2': '丹荘', 'dist': 45},
    {'name1': '丹荘', 'name2': '群馬藤岡', 'dist': 52},
    {'name1': '群馬藤岡', 'name2': '北藤岡', 'dist': 40},
    {'name1': '北藤岡', 'name2': '倉賀野', 'dist': 40},
    {'name1': '宇都宮', 'name2': '岡本', 'dist': 62},
    {'name1': '岡本', 'name2': '宝積寺', 'dist': 55},
    {'name1': '宝積寺', 'name2': '氏家', 'dist': 59},
    {'name1': '氏家', 'name2': '蒲須坂', 'dist': 45},
    {'name1': '蒲須坂', 'name2': '片岡', 'dist': 39},
    {'name1': '片岡', 'name2': '矢板', 'dist': 63},
    {'name1': '矢板', 'name2': '野崎', 'dist': 48},
    {'name1': '野崎', 'name2': '西那須野', 'dist': 52},
    {'name1': '西那須野', 'name2': '那須塩原', 'dist': 60},
    {'name1': '那須塩原', 'name2': '黒磯', 'dist': 55},
    {'name1': '宇都宮', 'name2': '鶴田', 'dist': 53},
    {'name1': '鶴田', 'name2': '鹿沼', 'dist': 104},
    {'name1': '鹿沼', 'name2': '文挟', 'dist': 89},
    {'name1': '文挟', 'name2': '下野大沢', 'dist': 64},
    {'name1': '下野大沢', 'name2': '今市', 'dist': 63},
    {'name1': '今市', 'name2': '日光', 'dist': 73},
    {'name1': '宝積寺', 'name2': '下野花岡', 'dist': 43},
    {'name1': '下野花岡', 'name2': '仁井田', 'dist': 22},
    {'name1': '仁井田', 'name2': '鴻野山', 'dist': 26},
    {'name1': '鴻野山', 'name2': '大金', 'dist': 49},
    {'name1': '大金', 'name2': '小塙', 'dist': 28},
    {'name1': '小塙', 'name2': '滝', 'dist': 25},
    {'name1': '滝', 'name2': '烏山', 'dist': 31},
    {'name1': '水戸', 'name2': '勝田', 'dist': 58},
    {'name1': '勝田', 'name2': '佐和', 'dist': 42},
    {'name1': '佐和', 'name2': '東海', 'dist': 47},
    {'name1': '東海', 'name2': '大甕', 'dist': 74},
    {'name1': '大甕', 'name2': '常陸多賀', 'dist': 46},
    {'name1': '常陸多賀', 'name2': '日立', 'dist': 49},
    {'name1': '日立', 'name2': '小木津', 'dist': 55},
    {'name1': '小木津', 'name2': '十王', 'dist': 42},
    {'name1': '十王', 'name2': '高萩', 'dist': 59},
    {'name1': '高萩', 'name2': '南中郷', 'dist': 45},
    {'name1': '南中郷', 'name2': '磯原', 'dist': 46},
    {'name1': '磯原', 'name2': '大津港', 'dist': 71},
    {'name1': '大津港', 'name2': '勿来', 'dist': 45},
    {'name1': '勿来', 'name2': '植田', 'dist': 46},
    {'name1': '植田', 'name2': '泉', 'dist': 72},
    {'name1': '泉', 'name2': '湯本', 'dist': 65},
    {'name1': '湯本', 'name2': '内郷', 'dist': 35},
    {'name1': '内郷', 'name2': 'いわき', 'dist': 44},
    {'name1': '大月', 'name2': '初狩', 'dist': 61},
    {'name1': '初狩', 'name2': '笹子', 'dist': 65},
    {'name1': '笹子', 'name2': '甲斐大和', 'dist': 61},
    {'name1': '甲斐大和', 'name2': '勝沼ぶどう郷', 'dist': 60},
    {'name1': '勝沼ぶどう郷', 'name2': '塩山', 'dist': 44},
    {'name1': '塩山', 'name2': '東山梨', 'dist': 32},
    {'name1': '東山梨', 'name2': '山梨市', 'dist': 21},
    {'name1': '山梨市', 'name2': '春日居町', 'dist': 28},
    {'name1': '春日居町', 'name2': '石和温泉', 'dist': 28},
    {'name1': '石和温泉', 'name2': '酒折', 'dist': 34},
    {'name1': '酒折', 'name2': '甲府', 'dist': 29},
    {'name1': '甲府', 'name2': '竜王', 'dist': 45},
    {'name1': '竜王', 'name2': '塩崎', 'dist': 41},
    {'name1': '塩崎', 'name2': '韮崎', 'dist': 43},
    {'name1': '高崎', 'name2': '北高崎', 'dist': 24},
    {'name1': '北高崎', 'name2': '群馬八幡', 'dist': 40},
    {'name1': '群馬八幡', 'name2': '安中', 'dist': 42},
    {'name1': '安中', 'name2': '磯部', 'dist': 70},
    {'name1': '磯部', 'name2': '松井田', 'dist': 51},
    {'name1': '松井田', 'name2': '西松井田', 'dist': 12},
    {'name1': '西松井田', 'name2': '横川', 'dist': 58},
    {'name1': '渋川', 'name2': '敷島', 'dist': 64},
    {'name1': '敷島', 'name2': '津久田', 'dist': 30},
    {'name1': '津久田', 'name2': '岩本', 'dist': 58},
    {'name1': '岩本', 'name2': '沼田', 'dist': 51},
    {'name1': '沼田', 'name2': '後閑', 'dist': 52},
    {'name1': '後閑', 'name2': '上牧', 'dist': 71},
    {'name1': '上牧', 'name2': '水上', 'dist': 54},
    {'name1': '水戸', 'name2': '常陸青柳', 'dist': 21},
    {'name1': '常陸青柳', 'name2': '常陸津田', 'dist': 24},
    {'name1': '常陸津田', 'name2': '後台', 'dist': 27},
    {'name1': '後台', 'name2': '下菅谷', 'dist': 14},
    {'name1': '下菅谷', 'name2': '中菅谷', 'dist': 13},
    {'name1': '中菅谷', 'name2': '上菅谷', 'dist': 12},
    {'name1': '上菅谷', 'name2': '常陸鴻巣', 'dist': 36},
    {'name1': '常陸鴻巣', 'name2': '瓜連', 'dist': 37},
    {'name1': '瓜連', 'name2': '静', 'dist': 15},
    {'name1': '静', 'name2': '常陸大宮', 'dist': 58},
    {'name1': '常陸大宮', 'name2': '玉川村', 'dist': 60},
    {'name1': '玉川村', 'name2': '野上原', 'dist': 41},
    {'name1': '野上原', 'name2': '山方宿', 'dist': 29},
    {'name1': '山方宿', 'name2': '中舟生', 'dist': 30},
    {'name1': '中舟生', 'name2': '下小川', 'dist': 31},
    {'name1': '下小川', 'name2': '西金', 'dist': 37},
    {'name1': '西金', 'name2': '上小川', 'dist': 35},
    {'name1': '上小川', 'name2': '袋田', 'dist': 50},
    {'name1': '袋田', 'name2': '常陸大子', 'dist': 42},
    {'name1': '上菅谷', 'name2': '南酒出', 'dist': 28},
    {'name1': '南酒出', 'name2': '額田', 'dist': 12},
    {'name1': '額田', 'name2': '河合', 'dist': 34},
    {'name1': '河合', 'name2': '谷河原', 'dist': 16},
    {'name1': '谷河原', 'name2': '常陸太田', 'dist': 15},
    {'name1': '韮崎', 'name2': '新府', 'dist': 42},
    {'name1': '新府', 'name2': '穴山', 'dist': 35},
    {'name1': '穴山', 'name2': '日野春', 'dist': 54},
    {'name1': '日野春', 'name2': '長坂', 'dist': 62},
    {'name1': '長坂', 'name2': '小淵沢', 'dist': 74},
    {'name1': '小淵沢', 'name2': '信濃境', 'dist': 45},
    {'name1': '信濃境', 'name2': '富士見', 'dist': 47},
    {'name1': '富士見', 'name2': 'すずらんの里', 'dist': 32},
    {'name1': 'すずらんの里', 'name2': '青柳', 'dist': 19},
    {'name1': '青柳', 'name2': '茅野', 'dist': 72},
    {'name1': '茅野', 'name2': '上諏訪', 'dist': 67},
    {'name1': '上諏訪', 'name2': '下諏訪', 'dist': 44},
    {'name1': '下諏訪', 'name2': '岡谷', 'dist': 41},
    {'name1': '岡谷', 'name2': '川岸', 'dist': 35},
    {'name1': '川岸', 'name2': '辰野', 'dist': 60},
    {'name1': '辰野', 'name2': '信濃川島', 'dist': 43},
    {'name1': '信濃川島', 'name2': '小野', 'dist': 40},
    {'name1': '小野', 'name2': '塩尻', 'dist': 99},
    {'name1': '岡谷', 'name2': 'みどり湖', 'dist': 78},
    {'name1': 'みどり湖', 'name2': '塩尻', 'dist': 39},
    {'name1': '塩尻', 'name2': '広丘', 'dist': 38},
    {'name1': '広丘', 'name2': '村井', 'dist': 30},
    {'name1': '村井', 'name2': '平田', 'dist': 20},
    {'name1': '平田', 'name2': '南松本', 'dist': 21},
    {'name1': '南松本', 'name2': '松本', 'dist': 24},
    {'name1': '小淵沢', 'name2': '甲斐小泉', 'dist': 78},
    {'name1': '甲斐小泉', 'name2': '甲斐大泉', 'dist': 56},
    {'name1': '甲斐大泉', 'name2': '清里', 'dist': 59},
    {'name1': '清里', 'name2': '野辺山', 'dist': 64},
    {'name1': '渋川', 'name2': '金島', 'dist': 55},
    {'name1': '金島', 'name2': '祖母島', 'dist': 22},
    {'name1': '祖母島', 'name2': '小野上', 'dist': 42},
    {'name1': '小野上', 'name2': '小野上温泉', 'dist': 18},
    {'name1': '小野上温泉', 'name2': '市城', 'dist': 27},
    {'name1': '市城', 'name2': '中之条', 'dist': 34},
    {'name1': '中之条', 'name2': '群馬原町', 'dist': 31},
    {'name1': '群馬原町', 'name2': '郷原', 'dist': 34},
    {'name1': '郷原', 'name2': '矢倉', 'dist': 17},
    {'name1': '矢倉', 'name2': '岩島', 'dist': 25},
    {'name1': '岩島', 'name2': '川原湯温泉', 'dist': 65},
    {'name1': '川原湯温泉', 'name2': '長野原草津口', 'dist': 50},
    {'name1': '長野原草津口', 'name2': '群馬大津', 'dist': 22},
    {'name1': '群馬大津', 'name2': '羽根尾', 'dist': 22},
    {'name1': '羽根尾', 'name2': '袋倉', 'dist': 29},
    {'name1': '袋倉', 'name2': '万座・鹿沢口', 'dist': 29},
    {'name1': '万座・鹿沢口', 'name2': '大前', 'dist': 31},
    {'name1': '鶴見', 'name2': '羽沢横浜国大', 'dist': 88},
)