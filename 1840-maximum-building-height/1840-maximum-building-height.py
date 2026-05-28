from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()

        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0]
            )

        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0]
            )

        ans = 0
        for i in range(1, len(restrictions)):
            a, x = restrictions[i - 1]
            b, y = restrictions[i]
            d = b - a
            ans = max(ans, (x + y + d) // 2)

        return ans