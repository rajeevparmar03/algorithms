#union field algorithm
"""it is used to find cycle in graph"""
class unionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank =[0]*n

    def find(self ,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x != root_y:
            if self.rank[root_x]<self.rank[root_y]:
                self.parent[root_x]=root_y
            elif self.rank[root_x]>self.rank[root_y]:
                self.parent[root_y]=root_x
            else:
                self.parent[root_y]=root_x
                self.rank[root_x]+=1

        else:
            return True
    
def has_cycle(graph):
    num_vertices =len(graph)
    uf =unionFind(num_vertices)
    for u in range(num_vertices):
        for v in graph[u]:
            if uf.union(u,v):
                return True
    return False
    

graph= {
     0: [1, 2],
     1: [2],
     2: [3, 4],
     3: [],
     4: [0]
        }
    
iscycle =has_cycle(graph)
print(iscycle)
               
