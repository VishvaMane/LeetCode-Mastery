from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        ans = float('inf')

        while q:
            node = q.popleft()
            for nei, dist in graph[node]:
                ans = min(ans, dist)
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return ans