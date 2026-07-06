from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = 0

        for x in nums:
            prev_even = even
            prev_odd = odd

            even = max(prev_even, prev_odd + x)
            odd = max(prev_odd, prev_even - x)

        return even