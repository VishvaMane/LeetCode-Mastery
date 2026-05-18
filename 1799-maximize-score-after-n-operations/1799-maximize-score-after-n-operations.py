import math
import functools

class Solution:
    def maxScore(self, nums):
        L = len(nums)
        gcd_mat = [[0]*L for _ in range(L)]
        for i in range(L):
            for j in range(i+1, L):
                gcd_mat[i][j] = math.gcd(nums[i], nums[j])

        full_mask = (1 << L) - 1

        @functools.lru_cache(None)
        def dp(mask):
            if mask == 0:
                return 0
            used = L - mask.bit_count()
            k = used // 2 + 1
            res = 0
            bits = [i for i in range(L) if (mask >> i) & 1]
            for a_i in range(len(bits)):
                i = bits[a_i]
                for b_i in range(a_i+1, len(bits)):
                    j = bits[b_i]
                    pair_mask = (1 << i) | (1 << j)
                    score = k * gcd_mat[i][j] + dp(mask ^ pair_mask)
                    if score > res:
                        res = score
            return res

        return dp(full_mask)