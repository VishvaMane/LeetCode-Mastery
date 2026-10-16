class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        max_val = (1 << p) - 1
        exp = (1 << (p - 1)) - 1
        
        return (pow(max_val - 1, exp, MOD) * (max_val % MOD)) % MOD