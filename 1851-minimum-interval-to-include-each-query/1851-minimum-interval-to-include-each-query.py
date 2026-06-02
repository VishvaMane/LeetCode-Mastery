from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q = sorted((x, i) for i, x in enumerate(queries))
        ans = [-1] * len(queries)
        heap = []
        j = 0

        for x, idx in q:
            while j < len(intervals) and intervals[j][0] <= x:
                l, r = intervals[j]
                heapq.heappush(heap, (r - l + 1, r))
                j += 1

            while heap and heap[0][1] < x:
                heapq.heappop(heap)

            if heap:
                ans[idx] = heap[0][0]

        return ans