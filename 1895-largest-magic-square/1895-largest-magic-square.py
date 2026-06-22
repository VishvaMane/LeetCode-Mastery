from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def row_sum(r, l, rr):
            return row_ps[r][rr + 1] - row_ps[r][l]

        def col_sum(c, t, b):
            return col_ps[b + 1][c] - col_ps[t][c]

        def main_diag(r, c, k):
            return diag1[r + k][c + k] - diag1[r][c]

        def anti_diag(r, c, k):
            return diag2[r + k][c] - diag2[r][c + k]

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = row_sum(r, c, c + k - 1)

                    ok = True
                    for i in range(k):
                        if row_sum(r + i, c, c + k - 1) != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    for j in range(k):
                        if col_sum(c + j, r, r + k - 1) != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    if main_diag(r, c, k) != target:
                        continue
                    if anti_diag(r, c, k) != target:
                        continue

                    return k

        return 1