#krushkal akgorithm 
# for minimal spannning tree 
#by the help of find union algorithm 
class unionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
     
    def union(self ,x,y):
        root_x =self.find(x)
        root_y =self.find(y)

        if root_x != root_y:
            if self.rank[root_x]<self.rank[root_y]:
                self.parent[x]=root_y
            elif self.rank[root_x]>self.rank[root_x]:
                self.parent[root_y]=root_x
            else:
                self.parent[root_y]=root_x
                self.parent[root_x]+=1
        else:
            return True

def krushkal(graph):
    num_vertices=len(graph)
    uf=unionFind(num_vertices)
    edges=[]
    for u in range(num_vertices):
        for v,weight in graph[u]:
            edges.append((u,v,weight))
    edges.sort(key=lambda x:x[2])
    minimum_spanning_tree=[]
    for u,v,weight in edges:
        if uf.find(u) !=uf.find(v):
            minimum_spanning_tree.append((u,v,weight))
    return minimum_spanning_tree


graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (7, 11), (2, 8)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}

minimum_spanning_tree = krushkal(graph)
print(minimum_spanning_tree)
