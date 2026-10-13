class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted(x * x for x in nums)
        half = len(nums) // 2
        return sum(squares[half:]) - sum(squares[:half])