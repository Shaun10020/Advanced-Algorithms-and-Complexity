# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.adj[from_].append(to)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def bfs(graph, s, t):
    path=[-1]*len(graph.graph)
    queue=[]
    queue.append(s)
    while queue:
        u=queue.pop(0)
        for x in graph.graph[u]:
            edge=graph.edges[x]
            if (edge.capacity-edge.flow)>0 and path[edge.v]==-1:
                path[edge.v]=x
                if edge.v==t:
                    array=[]
                    while True:
                        array.append(path[edge.v])
                        if edge.u==s:
                            break
                        edge=graph.edges[path[edge.u]]
                    return list(reversed(array))
                queue.append(edge.v)
    return None

def add(graph,path,flow):
    for i in range(len(path)):
        graph.add_flow(path[i],flow)

def min_flow(graph,path):
    flow=float('inf')
    for i in range(len(path)):
        edge=graph.edges[path[i]]
        if (edge.capacity-edge.flow)<flow:
            flow=edge.capacity-edge.flow
    return flow

def max_flow(graph, from_, to):
    flow = 0
    while True:
        path=bfs(graph,from_,to)
        if not path:
            return flow
        minflow=min_flow(graph,path)
        add(graph,path,minflow)
        flow+=minflow

        


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))

# 5 7
# 1 2 2
# 2 5 5
# 1 3 6
# 3 4 2
# 4 5 1
# 3 2 3
# 2 4 1

# 4 5
# 1 2 10000
# 1 3 10000
# 2 3 1
# 3 4 10000
# 2 4 10000

# 2 5
# 1 1 10000
# 1 2 1
# 1 2 4
# 1 2 100
# 2 1 900