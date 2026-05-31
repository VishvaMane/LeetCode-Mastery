from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = len(nums)
        for i, x in enumerate(nums):
            if x == target:
                dist = abs(i - start)
                if dist < min_dist:
                    min_dist = dist
        return min_dist