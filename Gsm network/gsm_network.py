# python3
def addNodeClause(ith,clauses):
    Red=ith*3
    Blue=Red-1
    Green=Blue-1
    clauses.append([Red,Blue,Green,0])
    clauses.append([Red*-1,Blue*-1,0])
    clauses.append([Green*-1,Blue*-1,0])
    clauses.append([Red*-1,Green*-1,0])

def addEdgeClauses(first,second,clauses):
    _Red=first*3
    _Blue=_Red-1
    _Green=_Blue-1
    Red=second*3
    Blue=Red-1
    Green=Blue-1
    clauses.append([Red*-1,_Red*-1,0])
    clauses.append([Green*-1,_Green*-1,0])
    clauses.append([Blue*-1,_Blue*-1,0])

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
clauses=[]
for i in range(n):
    ith=i+1
    addNodeClause(ith,clauses)
for i in range(len(adj)):
    for j in range(len(adj[i])):
        addEdgeClauses(i+1,adj[i][j]+1,clauses)
print(str(len(clauses))+' '+str(n*3))
for _ in clauses:
    print(' '.join([str(element) for element in _]))
