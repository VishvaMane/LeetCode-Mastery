class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        for j in range(1, n):
            dp[j] = {v ^ grid[0][j] for v in dp[j-1]}
            
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            new_dp[0] = {v ^ grid[i][0] for v in dp[0]}
            for j in range(1, n):
                new_dp[j] = {v ^ grid[i][j] for v in (dp[j] | new_dp[j-1])}
            dp = new_dp
            
        return min(dp[-1])