# python3
# mymap = {}

# for i in nodes:
#     for j in nodes:
#         if i != j:
#             mymap[(i, j)] = 0

# for _ in range(m):
#     u, v = map(int, input().split())
#     mymap[(u, v)] = 1
#     mymap[(v, u)] = 1

# for i in nodes:
#     for j in nodes:
#         if (i, j) in mymap:
#             if mymap[(i, j)] == 0:
#                 for k in range(1, n):
#                     clauses.append([-varnum(k, i), -varnum(k + 1, j)])

def V(i,j,n):
    return (j*n)+i

def eachnode(n,clauses):
    for j in range(n):
        clauses.append([V(i,j,n) for i in range(1,n+1)]+[0])

def eachposition(n,clauses):
    for i in range(1,n+1):
        clauses.append([V(i,j,n) for j in range(n)]+[0])

def nosamenode(n,clauses):
    for k in range(n):
        for i in range(1,n):
            for j in range(i+1,n+1):            
                clauses.append([V(i,k,n)*-1,V(j,k,n)*-1,0])

def nosameposition(n,clauses):
    for k in range(1,n+1):
        for i in range(n-1):
            for j in range(i+1,n):            
                clauses.append([V(k,i,n)*-1,V(k,j,n)*-1,0]  )
    
def noadj(edges,clauses,n):
    map={}
    for i in range(n):
        for j in range(n):
            if i!=j:
                map[(i,j)]=0
    for (u,v) in edges:
        u-=1
        v-=1
        map[(u,v)]=1
        map[(v,u)]=1
    for i in range(n):
        for j in range(n):
            if i!=j:
                if map[(i,j)]==0:
                    for k in range(1,n):
                        clauses.append([V(k,i,n)*-1,V(k+1,j,n)*-1,0])

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
clauses=[]
eachnode(n,clauses)
eachposition(n,clauses)
nosamenode(n,clauses)
nosameposition(n,clauses)
noadj(edges,clauses,n)
print(str(len(clauses))+' '+str(n*n))
for _ in clauses:
    print(' '.join([str(element) for element in _]))


# 5 4
# 1 2
# 2 3
# 3 5
# 4 5