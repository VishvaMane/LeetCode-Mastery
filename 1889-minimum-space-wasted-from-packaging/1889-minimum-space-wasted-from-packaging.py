from bisect import bisect_right
from itertools import accumulate

class Solution:
    def minWastedSpace(self, packages, boxes):
        MOD = 10**9 + 7
        packages.sort()
        pref = [0] + list(accumulate(packages))
        total = pref[-1]
        n = len(packages)

        ans = float('inf')

        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue

            waste = 0
            prev = 0
            for b in supplier:
                idx = bisect_right(packages, b)
                if idx > prev:
                    waste += (idx - prev) * b - (pref[idx] - pref[prev])
                    prev = idx
                if prev == n:
                    break

            ans = min(ans, waste)

        return -1 if ans == float('inf') else ans % MOD