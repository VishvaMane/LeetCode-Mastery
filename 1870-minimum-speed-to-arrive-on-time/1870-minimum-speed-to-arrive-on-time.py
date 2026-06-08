import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        
        def time_needed(speed: int) -> float:
            total = 0
            for i in range(len(dist) - 1):
                total += math.ceil(dist[i] / speed)
            total += dist[-1] / speed
            return total
        
        left, right = 1, 10**7
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if time_needed(mid) <= hour:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans