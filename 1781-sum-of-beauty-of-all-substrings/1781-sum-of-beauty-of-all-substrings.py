from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        ans, n = 0, len(s)
        for i in range(n):
            cnt = [0] * 26
            for j in range(i, n):
                cnt[ord(s[j]) - ord('a')] += 1
                mi, mx = float('inf'), 0
                for v in cnt:
                    if v > 0:
                        mi = min(mi, v)
                        mx = max(mx, v)
                ans += mx - mi
        return ans