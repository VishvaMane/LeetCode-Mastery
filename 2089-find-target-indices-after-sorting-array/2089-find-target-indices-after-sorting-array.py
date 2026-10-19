class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_than = sum(1 for n in nums if n < target)
        equal_to = sum(1 for n in nums if n == target)
        return list(range(less_than, less_than + equal_to))