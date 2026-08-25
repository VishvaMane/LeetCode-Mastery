from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = set(nums)
        m = 1
        while True:
            val = m * k
            if val not in present:
                return val
            m += 1