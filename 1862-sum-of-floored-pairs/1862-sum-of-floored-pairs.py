from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        pref = [0] * (mx + 1)
        for i in range(1, mx + 1):
            pref[i] = pref[i - 1] + freq[i]

        ans = 0

        for d in range(1, mx + 1):
            if freq[d] == 0:
                continue

            k = 1
            while k * d <= mx:
                left = k * d
                right = min(mx, (k + 1) * d - 1)
                count_in_range = pref[right] - pref[left - 1]
                ans = (ans + freq[d] * k * count_in_range) % MOD
                k += 1

        return ans