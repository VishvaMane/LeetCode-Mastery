class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        curr = 0
        best = -1

        for right, val in enumerate(nums):
            curr += val
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            if curr == target:
                best = max(best, right - left + 1)

        return -1 if best == -1 else len(nums) - best