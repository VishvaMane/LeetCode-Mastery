class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors
        q, r = divmod(primeFactors, 3)
        def modpow(a, b):
            res = 1
            a %= MOD
            while b:
                if b & 1:
                    res = res * a % MOD
                a = a * a % MOD
                b >>= 1
            return res
        if r == 0:
            return modpow(3, q)
        if r == 1:
            return modpow(3, q-1) * 4 % MOD
        return modpow(3, q) * 2 % MOD