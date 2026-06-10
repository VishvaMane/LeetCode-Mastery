class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        prefix = stones.copy()
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
        
        dp = [float('-inf')] * n
        dp[n - 2] = prefix[-1]
        
        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], prefix[i + 1] - dp[i + 1])
        
        return dp[0]    