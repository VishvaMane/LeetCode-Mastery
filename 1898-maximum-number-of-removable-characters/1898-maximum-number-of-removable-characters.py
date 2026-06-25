from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)

        def can(k: int) -> bool:
            removed = [False] * n
            for i in range(k):
                removed[removable[i]] = True

            j = 0
            for i, ch in enumerate(s):
                if removed[i]:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
                    if j == len(p):
                        return True
            return j == len(p)

        lo, hi = 0, len(removable)
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans