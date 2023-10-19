def dijkstra(graph, start):
    num_nodes = len(graph)
    shortest_distances = [float('inf')] * num_nodes
    shortest_distances[start] = 0
    unvisited_nodes = set(range(num_nodes))
    
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: shortest_distances[node])
        unvisited_nodes.remove(current_node)
        
        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:
                distance = shortest_distances[current_node] + graph[current_node][neighbor]
                if distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = distance

    return shortest_distances

graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

start_node = 0
result = dijkstra(graph, start_node)
print(result)
