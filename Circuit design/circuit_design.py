# python3
import sys
import threading


sys.setrecursionlimit(10**9)
threading.stack_size(2**27)

class Graph:
    def __init__(self,n):
        self.graph={}
        for i in range(1,n+1):
            self.graph[i]=set()
            self.graph[-i]=set()

    def addEdge(self,u,v):
        self.graph[u].add(v)

    def addClauses(self,clauses):
        for clause in clauses:
            u=clause[0]
            if len(clause)==2:
                v=clause[1]
                self.addEdge(-u,v)
                self.addEdge(-v,u)
            else:
                self.addEdge(-u,u)


def DFS(graph):
    visited=[None]*len(graph.graph)
    stack=[]
    for node in graph.graph:
        if visited[literal_to_index(node)]==None:
            array=Explore_DFS(graph,node,visited,[])
            stack+=array
    return stack

def Explore_DFS(graph,node,visited,post_order):
    visited[literal_to_index(node)]=1
    for neigbhour in graph.graph[node]:
        if visited[literal_to_index(neigbhour)]==None:
            post_order=Explore_DFS(graph,neigbhour,visited,post_order)
    post_order.append(node)
    return post_order

def Explore(graph,node,visited,pre_order):
    visited[literal_to_index(node)]=1
    pre_order.append(node)
    for neigbhour in graph.graph[node]:
        if visited[literal_to_index(neigbhour)]==None:
            pre_order=Explore_DFS(graph,neigbhour,visited,pre_order)
    return pre_order

def transpose_graph(graph):
    transpose=Graph(len(graph.graph))
    for node in graph.graph:
        for neighbour in graph.graph[node]:
            transpose.addEdge(neighbour,node)
    return transpose
        
def literal_to_index(literal):
    if literal<0:
        return abs(literal)*2-1
    else:
        return literal*2-2

def SCC(graph):
    stack=DFS(graph)
    transpose=transpose_graph(graph)
    visited=[None]*len(graph.graph)
    array=[None]*len(graph.graph)
    count=0
    while stack:
        node=stack.pop()
        if visited[literal_to_index(node)]==None:
            scc=Explore(transpose,node,visited,[])
            for literal in scc:
                array[literal_to_index(literal)]=count
            count+=1
    return array

def findcontradiction(array):
    count=0
    while count<len(array):
        if array[count]==array[count+1]:
            return True
        count+=2
    return False

def assign(array):
    count=0
    iteration=1
    assign=[]
    while count<len(array):
        if array[count]>array[count+1]:
            assign.append(iteration)
        else:
            assign.append(-iteration)
        count+=2
        iteration+=1
    return assign

def solver(graph):
    array=SCC(graph)
    if findcontradiction(array):
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        array=assign(array)
        print(' '.join([str(element) for element in array]))

def main():
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split())) for i in range(m)]
    graph=Graph(n)
    graph.addClauses(clauses)
    solver(graph)

threading.Thread(target=main).start()
