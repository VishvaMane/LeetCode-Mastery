class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        in_time = [0] * n
        out_time = [0] * n
        depth = [0] * n
        parent = [-1] * n
        
        adj_iter = [iter(adj[i]) for i in range(n)]
        stack = [0]
        timer = 1
        in_time[0] = timer
        timer += 1
        
        while stack:
            u = stack[-1]
            try:
                v = next(adj_iter[u])
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    in_time[v] = timer
                    timer += 1
                    stack.append(v)
            except StopIteration:
                out_time[u] = timer - 1
                stack.pop()
                
        LOG = 17
        up = [[0] * LOG for _ in range(n)]
        for i in range(n):
            up[i][0] = parent[i] if parent[i] != -1 else i
            
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
            
        bit = [0] * (n + 2)
        
        def add(idx, val):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        vals = [1 << (ord(c) - 97) for c in s]
        for i in range(n):
            add(in_time[i], vals[i])
            add(out_time[i] + 1, vals[i])
            
        ans = []
        for q in queries:
            if isinstance(q, str):
                parts = q.split()
            else:
                parts = q
                
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                change = vals[u] ^ new_mask
                vals[u] = new_mask
                add(in_time[u], change)
                add(out_time[u] + 1, change)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                pref_u = query(in_time[u])
                pref_v = query(in_time[v])
                mask = pref_u ^ pref_v ^ vals[lca]
                ans.append(True if (mask == 0 or (mask & (mask - 1)) == 0) else False)
                
        return ans