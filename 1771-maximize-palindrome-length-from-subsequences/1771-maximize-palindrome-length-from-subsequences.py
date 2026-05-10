class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n1, n2 = len(word1), len(word2)
        n = n1 + n2

        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < n1 and j >= n1:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return ans