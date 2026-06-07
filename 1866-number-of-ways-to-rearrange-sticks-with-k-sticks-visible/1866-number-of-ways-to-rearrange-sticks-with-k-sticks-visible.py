class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (k + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            new_dp = [0] * (k + 1)
            for j in range(1, min(i, k) + 1):
                new_dp[j] = (dp[j-1] + (i-1) * dp[j]) % MOD
            dp = new_dp
        
        return dp[k]