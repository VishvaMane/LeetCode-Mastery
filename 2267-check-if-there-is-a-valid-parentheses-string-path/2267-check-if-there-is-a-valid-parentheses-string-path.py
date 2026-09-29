class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                change = 1 if grid[i][j] == '(' else -1
                max_drops = (m - 1 - i) + (n - 1 - j)
                
                if i > 0:
                    for val in dp[i-1][j]:
                        new_val = val + change
                        if 0 <= new_val <= max_drops:
                            dp[i][j].add(new_val)
                if j > 0:
                    for val in dp[i][j-1]:
                        new_val = val + change
                        if 0 <= new_val <= max_drops:
                            dp[i][j].add(new_val)
                            
        return 0 in dp[m-1][n-1]