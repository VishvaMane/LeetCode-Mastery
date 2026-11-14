class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            curr = 0
            for j in range(i, min(n, i + r)):
                curr += nums[j]
                if j - i + 1 >= l and curr > 0:
                    if curr < ans:
                        ans = curr
        return ans if ans != float('inf') else -1