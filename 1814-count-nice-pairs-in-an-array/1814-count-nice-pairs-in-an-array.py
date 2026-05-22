def rev(x: int) -> int:
    y = 0
    while x:
        y = y * 10 + x % 10
        x //= 10
    return y

class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        from collections import Counter
        mod = 10**9 + 7
        diffs = Counter(num - rev(num) for num in nums)
        total = 0
        for v in diffs.values():
            total = (total + v * (v - 1) // 2) % mod
        return total