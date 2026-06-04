from collections import deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        count = [[0] * 26 for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                count[i][ord(colors[i]) - ord('a')] = 1
        
        processed = 0
        ans = 0
        
        while queue:
            u = queue.popleft()
            processed += 1
            ans = max(ans, count[u][ord(colors[u]) - ord('a')])
            
            for v in graph[u]:
                for i in range(26):
                    count[v][i] = max(count[v][i], count[u][i] + 
                                     (1 if i == ord(colors[v]) - ord('a') else 0))
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        return ans if processed == n else -1