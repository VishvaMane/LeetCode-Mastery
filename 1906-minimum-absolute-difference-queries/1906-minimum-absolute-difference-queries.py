from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pref = [[0] * 101 for _ in range(n + 1)]

        for i, x in enumerate(nums, 1):
            pref[i] = pref[i - 1][:]
            pref[i][x] += 1

        ans = []
        for l, r in queries:
            prev = -1
            best = 101
            for v in range(1, 101):
                if pref[r + 1][v] - pref[l][v] > 0:
                    if prev != -1:
                        best = min(best, v - prev)
                        if best == 1:
                            break
                    prev = v
            ans.append(-1 if best == 101 else best)

        return ans