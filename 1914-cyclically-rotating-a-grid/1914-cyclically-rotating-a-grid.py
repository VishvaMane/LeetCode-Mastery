from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [row[:] for row in grid]

        layers = min(m, n) // 2

        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            vals = []

            for c in range(left, right + 1):
                vals.append(grid[top][c])
            for r in range(top + 1, bottom):
                vals.append(grid[r][right])
            for c in range(right, left - 1, -1):
                vals.append(grid[bottom][c])
            for r in range(bottom - 1, top, -1):
                vals.append(grid[r][left])

            shift = k % len(vals)
            rotated = vals[shift:] + vals[:shift]

            idx = 0
            for c in range(left, right + 1):
                res[top][c] = rotated[idx]
                idx += 1
            for r in range(top + 1, bottom):
                res[r][right] = rotated[idx]
                idx += 1
            for c in range(right, left - 1, -1):
                res[bottom][c] = rotated[idx]
                idx += 1
            for r in range(bottom - 1, top, -1):
                res[r][left] = rotated[idx]
                idx += 1

        return res