class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD
        cnt = [0] * 26
        ans = 0
        for i in range(n - 1, -1, -1):
            x = ord(s[i]) - ord('a')
            cnt[x] += 1
            smaller = sum(cnt[:x])
            ways = fact[n - 1 - i]
            for c in range(26):
                ways = ways * invfact[cnt[c]] % MOD
            ans = (ans + smaller * ways) % MOD
        return ans