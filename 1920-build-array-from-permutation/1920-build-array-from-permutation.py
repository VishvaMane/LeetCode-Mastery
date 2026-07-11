from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i] % n] % n)
        for i in range(n):
            nums[i] //= n
        return nums