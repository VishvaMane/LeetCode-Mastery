class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        dest_right = [-1] * (m * n)
        dest_down = [-1] * (m * n)
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                idx = r * n + c
                if grid[r][c] == 0:
                    dest_right[idx] = idx
                    dest_down[idx] = idx
                else:
                    if r + 1 < m:
                        dest_right[idx] = dest_down[(r + 1) * n + c]
                    if c + 1 < n:
                        dest_down[idx] = dest_right[r * n + c + 1]
                        
        ways = [0] * (m * n)
        ways[0] = 1
        
        for r in range(m):
            for c in range(n):
                idx = r * n + c
                w = ways[idx]
                if w == 0 or grid[r][c] == 1:
                    continue
                    
                if c + 1 < n:
                    nxt = dest_right[idx + 1]
                    if nxt != -1:
                        ways[nxt] = (ways[nxt] + w) % MOD
                        
                if r + 1 < m:
                    nxt = dest_down[idx + n]
                    if nxt != -1:
                        ways[nxt] = (ways[nxt] + w) % MOD
                        
        return ways[-1]