from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        vals = []

        for u, v, c in edges:
            g[u].append((v, c))
            indeg[v] += 1
            vals.append(c)

        topo = []
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def can(x: int) -> bool:
            INF = 10**30
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, c in g[u]:
                    if c < x:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    nd = dist[u] + c
                    if nd < dist[v]:
                        dist[v] = nd

            return dist[n - 1] <= k

        if not vals:
            return -1

        lo, hi = 0, max(vals)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans