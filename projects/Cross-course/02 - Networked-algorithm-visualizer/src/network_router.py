"""
Networked Graph Routing & Pathfinding Engine
"""

from typing import Dict, List, Tuple, Optional, Any
import heapq

class CampusNetworkRouter:
    def __init__(self):
        self.graph: Dict[str, List[Tuple[str, float]]] = {}

    def add_link(self, u: str, v: str, latency_ms: float):
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append((v, latency_ms))
        self.graph[v].append((u, latency_ms))

    def find_optimal_route(self, origin: str, destination: str) -> Dict[str, Any]:
        """Executes Dijkstra's algorithm and reconstructs optimal path."""
        distances = {node: float('inf') for node in self.graph}
        prev = {node: None for node in self.graph}
        distances[origin] = 0.0

        pq = [(0.0, origin)]
        visited_order = []

        while pq:
            curr_dist, u = heapq.heappop(pq)
            visited_order.append(u)

            if u == destination:
                break
            if curr_dist > distances[u]:
                continue

            for v, weight in self.graph.get(u, []):
                alt = curr_dist + weight
                if alt < distances[v]:
                    distances[v] = alt
                    prev[v] = u
                    heapq.heappush(pq, (alt, v))

        # Reconstruct path
        path = []
        curr = destination
        while curr:
            path.append(curr)
            curr = prev.get(curr)
        path.reverse()

        return {
            "origin": origin,
            "destination": destination,
            "total_latency_ms": distances[destination],
            "optimal_path": path if path[0] == origin else [],
            "explored_nodes": visited_order
        }
