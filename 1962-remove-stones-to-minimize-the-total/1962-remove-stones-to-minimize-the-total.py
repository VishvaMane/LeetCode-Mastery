import heapq

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            largest -= largest // 2
            heapq.heappush(heap, -largest)

        return -sum(heap)