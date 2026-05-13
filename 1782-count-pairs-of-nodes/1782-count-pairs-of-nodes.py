class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        deg = [0] * (n + 1)
        shared = [{} for _ in range(n + 1)]

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            shared[u][v] = shared[u].get(v, 0) + 1

        sorted_deg = sorted(deg[1:])
        ans = [0] * len(queries)

        for k, q in enumerate(queries):
            i, j = 0, n - 1
            while i < j:
                if sorted_deg[i] + sorted_deg[j] > q:
                    ans[k] += j - i
                    j -= 1
                else:
                    i += 1

            for u in range(1, n + 1):
                for v, sh in shared[u].items():
                    if deg[u] + deg[v] > q and deg[u] + deg[v] - sh <= q:
                        ans[k] -= 1

        return ans