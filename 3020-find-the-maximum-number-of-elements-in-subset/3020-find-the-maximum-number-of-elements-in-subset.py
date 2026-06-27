from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = cnt[1] if cnt[1] % 2 == 1 else cnt[1] - 1

        for x in cnt:
            if x == 1:
                continue
            length = 0
            cur = x
            while cur in cnt and cnt[cur] >= 2:
                length += 2
                cur *= cur
            ans = max(ans, length + 1 if cur in cnt else length - 1)

        return max(ans, 1)