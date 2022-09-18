# python3
from itertools import permutations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def TSP_bracn_and_bound(graph):
    min_weight=INF
    best_path=[]
    min_weight,best_path,path,weight=explore([0],0,graph,0,-1,min_weight,best_path)
    if min_weight==INF:
        return -1,[]
    return min_weight,[ node+1 for node in best_path]


def explore(path,weight,graph,node,parent,min_weight,best_path):
    if weight>min_weight:
        path.pop()
        weight-=graph[parent][node]
        return min_weight,best_path,path,weight
    if len(path)==len(graph):
        weight+=graph[node][path[0]]
        if weight<min_weight:
            min_weight=weight
            best_path=list(path)
        weight-=graph[node][path[0]]
        path.pop()
        weight-=graph[parent][node]
        return min_weight,best_path,path,weight
    for neigbhour in range(len(graph[node])):
        if neigbhour not in path:
            if graph[node][neigbhour] is not INF:
                weight+=graph[node][neigbhour]
                path.append(neigbhour)
                min_weight,best_path,path,weight=explore(path,weight,graph,neigbhour,node,min_weight,best_path)
    if parent!=-1:
        path.pop()
        weight-=graph[parent][node]
    return min_weight,best_path,path,weight

def optimal_path(graph):
    weight,path=TSP_bracn_and_bound(graph)
    if weight==INF:
        return -1,[]
    else:
        return weight,path 


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))


# 4 6
# 1 2 20
# 1 3 42
# 1 4 35
# 2 3 30
# 2 4 34
# 3 4 12

# 4 4
# 1 2 1
# 2 3 4
# 3 4 5
# 4 2 1

# 4 4
# 1 2 1
# 1 3 4
# 1 4 5
# 3 4 1