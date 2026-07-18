from typing import List
import math

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        f = [[math.inf] * n for _ in range(maxTime + 1)]
        f[0][0] = passingFees[0]
        for i in range(1, maxTime + 1):
            for x, y, t in edges:
                if t <= i:
                    if f[i - t][y] != math.inf:
                        f[i][x] = min(f[i][x], f[i - t][y] + passingFees[x])
                    if f[i - t][x] != math.inf:
                        f[i][y] = min(f[i][y], f[i - t][x] + passingFees[y])
        ans = min(f[i][n - 1] for i in range(maxTime + 1))
        return ans if ans < math.inf else -1