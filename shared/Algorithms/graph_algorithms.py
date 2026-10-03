"""
Core Graph Algorithms Library
BFS, DFS, Dijkstra shortest path, and topological sort.
"""

from typing import Dict, List, Tuple, Set, Optional
import heapq
from collections import deque

class Graph:
    def __init__(self, directed: bool = False):
        self.adj: Dict[str, List[Tuple[str, float]]] = {}
        self.directed = directed

    def add_edge(self, u: str, v: str, weight: float = 1.0):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def bfs(self, start: str) -> List[str]:
        """Breadth-First Search traversal."""
        visited: Set[str] = set()
        queue = deque([start])
        visited.add(start)
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)
            for neighbor, _ in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

    def dfs(self, start: str) -> List[str]:
        """Depth-First Search traversal."""
        visited: Set[str] = set()
        traversal = []

        def _dfs_visit(node: str):
            visited.add(node)
            traversal.append(node)
            for neighbor, _ in self.adj.get(node, []):
                if neighbor not in visited:
                    _dfs_visit(neighbor)

        _dfs_visit(start)
        return traversal

    def dijkstra(self, start: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
        """Dijkstra's Single-Source Shortest Path using min-heap."""
        distances: Dict[str, float] = {node: float('inf') for node in self.adj}
        predecessors: Dict[str, Optional[str]] = {node: None for node in self.adj}
        distances[start] = 0.0

        pq: List[Tuple[float, str]] = [(0.0, start)]

        while pq:
            curr_dist, u = heapq.heappop(pq)
            if curr_dist > distances[u]:
                continue

            for v, weight in self.adj.get(u, []):
                new_dist = curr_dist + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    heapq.heappush(pq, (new_dist, v))

        return distances, predecessors
