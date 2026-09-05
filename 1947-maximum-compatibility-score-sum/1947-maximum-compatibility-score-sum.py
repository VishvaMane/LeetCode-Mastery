from functools import cache

class Solution:
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        m, n = len(students), len(students[0])
        
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(s == t for s, t in zip(students[i], mentors[j]))
                
        @cache
        def dfs(i: int, mask: int) -> int:
            if i == m:
                return 0
            ans = 0
            for j in range(m):
                if not (mask & (1 << j)):
                    ans = max(ans, score[i][j] + dfs(i + 1, mask | (1 << j)))
            return ans
            
        return dfs(0, 0)