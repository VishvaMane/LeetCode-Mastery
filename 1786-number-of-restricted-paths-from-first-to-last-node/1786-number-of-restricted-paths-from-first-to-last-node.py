import heapq
from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        @lru_cache(None)
        def dfs(u: int) -> int:
            if u == n:
                return 1
            ways = 0
            for v, _ in graph[u]:
                if dist[u] > dist[v]:
                    ways = (ways + dfs(v)) % MOD
            return ways
        
        return dfs(1)