from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        dirs = [(-1, 0), (0, -1), (-1, -1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if ways[i][j] == 0:
                    continue

                for di, dj in dirs:
                    x, y = i + di, j + dj
                    if x < 0 or y < 0 or board[x][y] == 'X':
                        continue

                    val = score[i][j]
                    if board[x][y] != 'E':
                        val += int(board[x][y])

                    if val > score[x][y]:
                        score[x][y] = val
                        ways[x][y] = ways[i][j]
                    elif val == score[x][y]:
                        ways[x][y] = (ways[x][y] + ways[i][j]) % MOD

        if ways[0][0] == 0:
            return [0, 0]
        return [score[0][0], ways[0][0]]