from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> bool:
            stack = [(r, c)]
            grid2[r][c] = 0
            is_sub = True

            while stack:
                x, y = stack.pop()
                if grid1[x][y] == 0:
                    is_sub = False

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                        grid2[nx][ny] = 0
                        stack.append((nx, ny))

            return is_sub

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    ans += 1

        return ans