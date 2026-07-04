from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                removed += 1
                if removed > 1:
                    return False

                if i == 1 or nums[i] > nums[i - 2]:
                    prev = nums[i]
                # else: keep prev as is, effectively removing nums[i]
            else:
                prev = nums[i]

        return True