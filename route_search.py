import route_const

# 駅の隣駅名と距離を保持
__nodes = {}
# コンソールに結果を出力したいとき True
__print_verbose = False
__print_sql = False

# // preperation // 
def __preparation():
    """ 経路算出の準備を行います。 """
    tmp_stations = []
    for node in route_const.nodes:
        name1 = node['name1']
        name2 = node['name2']
        dist  = node['dist']
        if name1 not in __nodes:
            __nodes[name1] = []
        __nodes[name1].append({'to': name2, 'dist': dist})

        if name2 not in __nodes:
            __nodes[name2] = []
        __nodes[name2].append({'to': name1, 'dist': dist})

        tmp_stations.append(name1)
        tmp_stations.append(name2)
    
    return tuple(tmp_stations)

# // routing //
def __routing(start_name):
    """ 経路探索します。

    Keyword Argument:
        start_name -- 経路探索の始端となる駅名
    """
    result = {}

    # 始端駅以外は 99999 として最長の営業キロとする
    initial = {'dist': 99999, 'route': [], 'way': []}
    for name in __gen_stations:
        result[name] = initial.copy()

    # 始端駅は 0 として、最短の営業キロとする
    result[start_name] = {'dist': 0, 'route': [start_name], 'way': []}

    next_set_from = set([start_name])

    return __routing_impl(next_set_from, result)

# // routing implementation (recursive) //
def __routing_impl(set_from, result):
    """ 経路探索の主処理です。再帰呼び出し可能です。

    Keyword Argument:
        node_from -- これから調べる駅名
        result -- ここまでの探索結果が格納されている連想配列
    """
    next_set_from = set()

    for node_from in set_from:
        for node in __nodes[node_from]:
            node_to   = node['to']       # node_from 駅から見た隣駅名
            node_dist = node['dist']     # node_from 駅から node_to 駅までの営業キロ(0.1km単位)

            current  = result[node_from] # 始端駅から node_from 駅までの経路探索結果
            neighbor = result[node_to]   # 始端駅から node_to   駅までの経路探索結果

            target_distance = current['dist'] + node_dist
            overwrite_neighbor = False

            if target_distance == neighbor['dist']:
                # 始端駅から node_from 駅を経由して node_to 駅までの営業キロと、
                # 始端駅から(別経路で) node_to 駅までの営業キロが等しい
                # 　-> どちらの経路を優先するか決める。
                #    （このとき、新在同一の新幹線区間が含まれている方を優先する）
                is_current_subset  = __is_subset_shinkansen(current['route'])
                is_neighbor_subset = __is_subset_shinkansen(neighbor['route'])

                # current の経路にのみ新在同一の新幹線区間があるとき True
                overwrite_neighbor = (is_current_subset and not is_neighbor_subset)

            elif target_distance < neighbor['dist']:
                # 始端駅から node_from 駅を経由して node_to 駅までの営業キロが、
                # 始端駅から(別経路で) node_to 駅までの営業キロより短い
                #   -> node_from 駅経由の方が短いため、True
                overwrite_neighbor = True
            
            if overwrite_neighbor:
                # 始端駅から node_to 駅までの経路は、node_from 駅を経由した方が
                # 営業キロが短いため、neighbor は current の値で上書き
                neighbor['dist']  = target_distance
                neighbor['route'] = current['route'].copy()
                neighbor['way']   = current['way'].copy()
                neighbor['route'].append(node_to)
                if len(__nodes[node_from]) > 2:
                    # node_from 駅から3方向以上に線路があるので
                    # 選択した方向として node_to 駅を way に追加
                    neighbor['way'].append(node_to)
                # 次回の走査対象駅名を追加
                next_set_from.add(node_to)
                
    # next_set_from 駅群について同様に算出するため、この関数を再帰呼び出し
    if len(next_set_from) > 0:
        result = __routing_impl(next_set_from, result)

    return result

# // judge shinkansen route //
def __is_subset_shinkansen(arr_route):
    """ 駅名の配列に、新在同一となる在来線区間が含まれているかを判定します。

    Keyword Argument:
        arr_route -- ここまで通った駅名が格納された配列
    """
    through = set(arr_route)
    for shinkansen_path in route_const.search_shinkansen:
        if shinkansen_path.issubset(through):
            # いずれかの新在同一となる在来線区間が含まれている
            return True
    
    return False

# // search shinkansen-path //
def __search_shinkansen_path(results):
    """ 探索結果の経路群のうち、新在同一となる在来線区間が含まれているものを標準出力に書き出します。

    Keyword Argument:
        results -- 定数クラスに定義されたすべての駅を始端駅とした探索結果が含まれた連想配列
    """
    edges = set()
    for (name, result) in results.items():
        # name: 始端駅, result: (連想配列)
        for (station, detail) in result.items():
            # station: 終端駅, detail: (連想配列)
            dist = detail['dist']
            route = detail['route']
            way = detail['way']

            if dist <= 1000:
                # 営業キロが 100.0 km 以下の場合は、標準出力に書き出さない
                continue

            if __omit_large_area(name, station, dist):
                # 既定距離以上の区間で、かつ東京駅/横浜駅以外である
                continue

            if __is_subset_shinkansen(route):
                # 新在同一となる在来線区間が含まれている
                edge = (name, station)
                if edge not in edges:
                    if __print_verbose:
                        way_str = ' '.join(way)
                        if __print_sql:
                            print(f"insert into result(station_from, via, distance, station_to) values ('{name}', '{way_str}', '{dist}', '{station}');")
                        else:
                            print(f'{name}-{station} ({dist}) / {way_str}')
                    edges.add(edge)
                    continue

def __omit_large_area(station1, station2, dist):
    """ 始端駅/終端駅が「山手線内」「東京都区内」「横浜市内」に該当するかどうかを判定し、
    中心駅でなければ出力除外(True)を返します。

    Keyword Argument:
        station1 -- 始端駅
        station2 -- 終端駅
        dist - 始端駅から終端駅までの営業キロ
    """
    if station1 == "東京" or station1 == "横浜" or station2 == "東京" or station2 == "横浜":
        return False
    
    # 営業キロが 100.0 km 以下
    if dist <= 1000:
        return False
    # 営業キロが 100.1 - 200.0 km
    if 1000 < dist and dist <= 2000:
        # station1/station2 が、東京駅以外の山手線内の駅であるか
        if set([station1]).issubset(route_const.yamanote) or set([station2]).issubset(route_const.yamanote):
            return True
    # 営業キロが 200.1 km 以上
    if 2000 < dist:
        # station1/station2 が、東京駅以外の東京都区内の駅であるか
        if set([station1]).issubset(route_const.tokunai) or set([station2]).issubset(route_const.tokunai):
            return True
        # station1/station2 が、横浜駅以外の横浜市内の駅であるか
        if set([station1]).issubset(route_const.yokohama) or set([station2]).issubset(route_const.yokohama):
            return True

    return False

# // main //
__results = {}
__gen_stations = __preparation()
# 駅名一覧から順に処理
for start in __gen_stations:
    # 出発駅名を指定して、残りの駅までの最短ルートを算出
    __results[start] = __routing(start)
# 新在同一区間が含まれているかを判定
__search_shinkansen_path(__results)
