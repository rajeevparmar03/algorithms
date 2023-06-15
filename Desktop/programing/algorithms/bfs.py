#breadth first search algorithm 
from collections import  deque
def bfs(graph,start):
    visited=set()
    queue=deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node =queue.popleft()
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start='A'
bfs(graph,start)

