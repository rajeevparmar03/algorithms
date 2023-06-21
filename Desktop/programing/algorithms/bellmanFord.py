"""bellman ford algoritm 
  time complexity :  O(V*E)
  used to find shortest distance from src """

class Graph:
    def __init__(self,vertices):
        self.graph=[]
        self.v=vertices 
    
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def bellmanFord(self,source):
        dist =[float('inf')]*self.v
        dist[source] =0

        for _ in range(self.v-1):
            for u,v,w in self.graph:
                if dist[u]!=float('inf') and dist[u] + w <dist[v]:
                    dist[v] =dist[u] + w 

        for u,v ,w in self.graph:
            if dist[u]!=float('inf') and dist[u]+w <dist[v]:
                print("it contains a negative cycle ")
                return 
        
        self.printdistances(distanceskd)
    def Printdistances(self ,distances):
        print("distance  between source to vertx") 
        for i in range(self.graph):
            print(f"{i}\t\t{distances[i]}")

        
]kldw
# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellmanFord(0)






       
