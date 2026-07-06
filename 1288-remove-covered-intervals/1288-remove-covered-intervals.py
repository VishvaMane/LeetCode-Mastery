from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        prev_end = -1
        
        for _, end in intervals:
            if end > prev_end:
                ans += 1
                prev_end = end
        
        return ans