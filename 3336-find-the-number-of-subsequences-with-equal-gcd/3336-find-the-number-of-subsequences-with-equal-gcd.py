from math import gcd
from typing import List
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for num in nums:
            ndp = dp.copy()
            for (g1, g2), cnt in dp.items():
                # Add num to seq1
                new_g1 = num if g1 == 0 else gcd(g1, num)
                ndp[(new_g1, g2)] = (ndp[(new_g1, g2)] + cnt) % MOD

                # Add num to seq2
                new_g2 = num if g2 == 0 else gcd(g2, num)
                ndp[(g1, new_g2)] = (ndp[(g1, new_g2)] + cnt) % MOD
            dp = ndp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 != 0 and g1 == g2:
                ans = (ans + cnt) % MOD

        return ans