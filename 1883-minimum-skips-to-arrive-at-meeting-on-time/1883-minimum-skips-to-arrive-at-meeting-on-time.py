from math import inf

class Solution:
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        target = hoursBefore * speed
        dp = [0] + [inf] * n

        def ceil_to_hour(x):
            return ((x + speed - 1) // speed) * speed

        for i, d in enumerate(dist):
            ndp = [inf] * (n + 1)
            for k in range(i + 1):
                if dp[k] == inf:
                    continue

                if i == n - 1:
                    ndp[k] = min(ndp[k], dp[k] + d)
                else:
                    ndp[k] = min(ndp[k], ceil_to_hour(dp[k] + d))

                if k + 1 <= n:
                    ndp[k + 1] = min(ndp[k + 1], dp[k] + d)

            dp = ndp

        for k in range(n + 1):
            if dp[k] <= target:
                return k
        return -1