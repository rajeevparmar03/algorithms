#topological algorithm 
#is used for order the vertices of directed graph 
   
def topological_sort(graph):
    visited =set()
    result=[]

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        result.insert(0,vertex)

    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    return result
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

result =topological_sort(graph)
print("sorted vertices ")
print(result)
