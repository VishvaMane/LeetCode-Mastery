from collections import Counter
from math import inf

class Solution:
    def minChanges(self, nums, k):
        MAXX = 1 << 10
        n = len(nums)

        groups = [Counter() for _ in range(k)]
        sizes = [0] * k

        for i, x in enumerate(nums):
            groups[i % k][x] += 1
            sizes[i % k] += 1

        dp = [inf] * MAXX
        dp[0] = 0

        for g in range(k):
            ndp = [min(dp) + sizes[g]] * MAXX

            for xor_prev in range(MAXX):
                if dp[xor_prev] == inf:
                    continue
                base = dp[xor_prev] + sizes[g]
                for val, freq in groups[g].items():
                    ndp[xor_prev ^ val] = min(ndp[xor_prev ^ val], base - freq)

            dp = ndp

        return dp[0]