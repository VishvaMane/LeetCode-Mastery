from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrival = [dist[i] / speed[i] for i in range(n)]
        arrival.sort()
        
        for minute in range(n):
            if arrival[minute] <= minute:
                return minute
        return n