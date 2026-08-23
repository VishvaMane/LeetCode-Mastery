import sys

class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        sys.setrecursionlimit(200000)
        
        n = len(parents)
        adj = [[] for _ in range(n)]
        root = -1
        
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                adj[p].append(i)
                
        node_queries = [[] for _ in range(n)]
        for i, (node, val) in enumerate(queries):
            node_queries[node].append((i, val))
            
        ans = [0] * len(queries)
        trie = [[0, 0, 0]]
        
        def update(val, d):
            curr = 0
            trie[curr][2] += d
            for i in range(17, -1, -1):
                bit = (val >> i) & 1
                if not trie[curr][bit]:
                    trie.append([0, 0, 0])
                    trie[curr][bit] = len(trie) - 1
                curr = trie[curr][bit]
                trie[curr][2] += d

        def query(val):
            curr = 0
            res = 0
            for i in range(17, -1, -1):
                bit = (val >> i) & 1
                target = 1 - bit
                nxt = trie[curr][target]
                if nxt and trie[nxt][2] > 0:
                    res |= (1 << i)
                    curr = nxt
                else:
                    curr = trie[curr][bit]
            return res

        def dfs(u):
            update(u, 1)
            for q_idx, val in node_queries[u]:
                ans[q_idx] = query(val)
            for v in adj[u]:
                dfs(v)
            update(u, -1)
            
        dfs(root)
        
        return ans