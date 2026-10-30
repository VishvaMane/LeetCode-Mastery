import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
            
        adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w, labels[v]))
            
        min_c = [k + 1] * n
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        pq = [(0, 0, 1)]
        heappop = heapq.heappop
        heappush = heapq.heappush
        
        target = n - 1
        
        while pq:
            d, u, c = heappop(pq)
            
            if d > dist[u][c]:
                continue
                
            if u == target:
                return d
                
            if c >= min_c[u]:
                continue
            min_c[u] = c
            
            label_u = labels[u]
            
            for v, w, label_v in adj[u]:
                nc = c + 1 if label_v == label_u else 1
                if nc <= k:
                    nd = d + w
                    if nd < dist[v][nc]:
                        dist[v][nc] = nd
                        heappush(pq, (nd, v, nc))
                        
        return -1