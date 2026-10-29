class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
            
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                
        return find(source) == find(destination)