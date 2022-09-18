#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent,weights):
    if weights[vertex]==float('inf'):
        temporary_weight=tree[vertex].weight
        if len(tree[vertex].children)==0:
            weights[vertex]=temporary_weight
        else:
            for child in tree[vertex].children:
                if child!=parent:
                    for child_w in tree[child].children:
                        if child_w!=vertex:
                            temporary_weight+=dfs(tree,child_w,child,weights)
            temporary_weight_2=0
            for child in tree[vertex].children:
                if child!=parent:
                    temporary_weight_2+=dfs(tree,child,vertex,weights)
            weight=max(temporary_weight,temporary_weight_2)
            weights[vertex]=weight
    return weights[vertex]


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    weights=[float('inf')]*size
    return dfs(tree, 0, -1,weights)


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()

# 5
# 1 5 3 7 5
# 5 4
# 2 3
# 4 2
# 1 2