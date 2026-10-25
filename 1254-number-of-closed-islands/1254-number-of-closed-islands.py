class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            q = [(r, c)]
            grid[r][c] = 1
            while q:
                i, j = q.pop()
                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y))
        
        for i in range(m):
            if grid[i][0] == 0: dfs(i, 0)
            if grid[i][n-1] == 0: dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == 0: dfs(0, j)
            if grid[m-1][j] == 0: dfs(m-1, j)
            
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
                    
        return count