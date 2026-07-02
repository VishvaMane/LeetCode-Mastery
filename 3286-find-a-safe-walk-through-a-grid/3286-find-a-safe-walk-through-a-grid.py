from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        start_cost = grid[0][0]
        if start_cost >= health:
            return False

        dist = [[10**9] * n for _ in range(m)]
        dist[0][0] = start_cost
        dq = deque([(0, 0)])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            x, y = dq.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                nd = dist[x][y] + grid[nx][ny]
                if nd < dist[nx][ny] and nd < health:
                    dist[nx][ny] = nd
                    if grid[nx][ny] == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

        return dist[m - 1][n - 1] < health