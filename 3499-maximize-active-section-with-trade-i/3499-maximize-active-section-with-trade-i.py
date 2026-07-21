from itertools import groupby, pairwise

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zero_groups = [len(list(g)) for c, g in groupby(s) if c == '0']
        ones = s.count('1')
        if len(zero_groups) < 2:
            return ones
        best = max(a + b for a, b in pairwise(zero_groups))
        return ones + best