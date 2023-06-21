#floyd warshall algorithm
# used to find all pair shortest path 

def floyd_warshall(graph):
    A=[row[:] for row in graph] 
    n= len(graph) 
    

    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j]=min(A[i][j],A[i][k]+A[k][j])
    return A
inf =float('inf')        
graph =[
    [0,3,inf,7],
    [8,0,2,inf],
    [5,inf,0,1],
    [2,inf,inf,0]
]

result=floyd_warshall(graph)
for row in result:
   print(row)