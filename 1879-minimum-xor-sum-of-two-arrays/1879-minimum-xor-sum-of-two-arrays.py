from functools import lru_cache
from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @lru_cache(None)
        def dp(mask: int) -> int:
            i = mask.bit_count()
            if i == n:
                return 0

            ans = float('inf')
            for j in range(n):
                if not (mask >> j) & 1:
                    ans = min(ans, (nums1[i] ^ nums2[j]) + dp(mask | (1 << j)))
            return ans

        return dp(0)