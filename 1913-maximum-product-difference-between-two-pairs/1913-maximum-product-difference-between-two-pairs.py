from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = float('inf')

        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x

            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return max1 * max2 - min1 * min2