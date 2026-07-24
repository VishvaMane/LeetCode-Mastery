class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = 2048
        a = [0.0] * n
        for v in set(nums):
            a[v] = 1.0

        h = 1
        while h < n:
            for i in range(0, n, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h <<= 1

        for i in range(n):
            a[i] = a[i] ** 3

        h = 1
        while h < n:
            for i in range(0, n, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h <<= 1

        ans = 0
        for v in a:
            if round(v / n) > 0:
                ans += 1
        return ans