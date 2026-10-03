# 01_astar_search.py - A* Pathfinding Algorithm

import heapq

def astar_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, cost, current, path = heapq.heappop(pq)
        if current == goal:
            return path, cost
        if current in visited:
            continue
        visited.add(current)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_cost, neighbor, path + [neighbor]))
    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    heuristic = {'A': 3, 'B': 4, 'C': 1, 'D': 0}
    path, cost = astar_search(graph, 'A', 'D', heuristic)
    print("Optimal Path:", path, "with Total Cost:", cost)
