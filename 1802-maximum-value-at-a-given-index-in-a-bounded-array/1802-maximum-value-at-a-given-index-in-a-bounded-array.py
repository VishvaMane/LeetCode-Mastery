class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc(x: int, cnt: int) -> int:
            if x >= cnt:
                return (x + x - cnt + 1) * cnt // 2
            return (x + 1) * x // 2 + (cnt - x)

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            total = calc(mid - 1, index) + calc(mid, n - index)
            if total <= maxSum:
                lo = mid
            else:
                hi = mid - 1
        return lo