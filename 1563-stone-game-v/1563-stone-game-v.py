from typing import List
from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dp(i: int, j: int) -> int:
            if i >= j:
                return 0
            res = 0
            left_sum = 0
            total = prefix[j + 1] - prefix[i]  # sum of stoneValue[i:j+1]

            for k in range(i, j):
                left_sum += stoneValue[k]
                right_sum = total - left_sum

                if left_sum < right_sum:
                    res = max(res, left_sum + dp(i, k))
                elif right_sum < left_sum:
                    res = max(res, right_sum + dp(k + 1, j))
                else:  # left_sum == right_sum
                    res = max(res, left_sum + dp(i, k), right_sum + dp(k + 1, j))
            return res

        return dp(0, n - 1)