from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        vis = [False] * n

        def dfs(i: int):
            vis[i] = True
            x, y = 1, len(g[i])
            for j in g[i]:
                if not vis[j]:
                    a, b = dfs(j)
                    x += a
                    y += b
            return x, y

        ans = 0
        for i in range(n):
            if not vis[i]:
                x, y = dfs(i)
                if x * (x - 1) == y:
                    ans += 1
        return ans