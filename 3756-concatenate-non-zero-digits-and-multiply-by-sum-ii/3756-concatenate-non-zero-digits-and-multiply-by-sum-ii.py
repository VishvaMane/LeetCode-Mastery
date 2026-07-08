from typing import List

MOD = 10**9 + 7

def modinv(a):
    return pow(a, MOD-2, MOD)

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        tot = [0] * (n+1)
        remains = [0] * (n+1)
        pow10count = [1] * (n+1)

        curPow = 1
        for i in range(n-1, -1, -1):
            d = ord(s[i]) - 48
            tot[i] = (tot[i+1] + d)
            if d == 0:
                remains[i] = remains[i+1]
                pow10count[i] = pow10count[i+1]
            else:
                remains[i] = (remains[i+1] + d * curPow) % MOD
                curPow = (curPow * 10) % MOD
                pow10count[i] = curPow

        ans = []
        for l, r in queries:
            sum_digits = tot[l] - tot[r+1]
            raw = (remains[l] - remains[r+1]) % MOD
            inv = modinv(pow10count[r+1])
            x = (raw * inv) % MOD
            ans.append((x * (sum_digits % MOD)) % MOD)
        return ans