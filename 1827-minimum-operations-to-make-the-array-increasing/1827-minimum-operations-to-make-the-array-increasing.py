class Solution:
    def minOperations(self, nums):
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ops += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return ops