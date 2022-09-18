# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

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

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        graph = []
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    graph.append((i+2, n+j+2, 1))
        for i in range(n+m):
            if i < n:
                graph.append((1, i+2, 1))
            else:
                graph.append(( i+2,n+m+2, 1))
        self.graph=self.graph_init(n+m+2,graph)
        paths=self.max_flow(self.graph,0,len(self.graph.graph)-1)
        for path in paths:
            first_edge=self.graph.edges[path[0]]
            second_edge=self.graph.edges[path[-1]]
            applicant=first_edge.v-1
            job=second_edge.u-n-1
            matching[applicant]=job
        return matching

    def graph_init(self,count,array):
        vertex_count=count
        edge_count =len(array) 
        graph = FlowGraph(vertex_count)
        for _ in range(edge_count):
            u, v, capacity = array[_]
            graph.add_edge(u - 1, v - 1, capacity)
        return graph


    def bfs(self,graph, s, t):
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

    def bfs_reversed(self,graph, s, t):
        path=[-1]*len(graph.graph)
        queue=[]
        queue.append(s)
        while queue:
            u=queue.pop(0)
            for x in graph.graph[u]:
                edge=graph.edges[x]
                if (edge.capacity-edge.flow)==0 and path[edge.v]==-1:
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

    def add(self,graph,path,flow):
        for i in range(len(path)):
            graph.add_flow(path[i],flow)

    def max_flow(self,graph, from_, to):
        while True:
            path=self.bfs(graph,from_,to)
            if not path:
                break
            self.add(graph,path,1)
        paths=[]
        while True:
            path=self.bfs_reversed(graph,from_,to)
            if not path:
                return paths
            self.add(graph,path,1)
            paths.append(path)


    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()


# 3 4
# 1 1 0 1
# 0 1 0 0
# 0 0 0 0

# 2 2
# 1 1
# 1 0
