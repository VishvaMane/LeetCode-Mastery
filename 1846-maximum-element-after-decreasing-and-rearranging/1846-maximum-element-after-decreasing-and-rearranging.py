from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1

        for x in arr[1:]:
            if x >= ans + 1:
                ans += 1

        return ans