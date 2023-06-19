#dijkrasta algorithm 
#it is used for shortest path from one point 
import heapq

def dijkstra(graph ,source):
    distances={node: float('inf') for node in graph }
    distances[source]=0
    priority_q=[(0,source)]

    while priority_q:
        current_distance,current_node =heapq.heappop(priority_q)

        if current_distance>distances[current_node]:
            continue


        for neighbor,weight in graph[current_node].items():
            distance=current_distance+ weight

            if distance <distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(priority_q,(distance,neighbor))
    return distances


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 6},
    'D': {'B': 1, 'C': 6}
}
start="A"

result=dijkstra(graph,start)
for row in result:

    print(row)