class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for L in range(2 * d, n + 1, d):
                divs[L].append(d)

        sub_cost = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n // 2 + 1)]
        cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L
                min_c = float('inf')
                for d in divs[L]:
                    c = sub_cost[d][i + d][j - d]
                    for r in range(d):
                        if s[i + r] != s[j - d + r]:
                            c += 1
                    sub_cost[d][i][j] = c
                    if c < min_c:
                        min_c = c
                cost[i][j] = min_c

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for p in range(1, k + 1):
            new_dp = [float('inf')] * (n + 1)
            for j in range(2 * p, n + 1):
                best = float('inf')
                for i in range(2 * (p - 1), j - 1):
                    val = dp[i] + cost[i][j]
                    if val < best:
                        best = val
                new_dp[j] = best
            dp = new_dp

        return dp[n]