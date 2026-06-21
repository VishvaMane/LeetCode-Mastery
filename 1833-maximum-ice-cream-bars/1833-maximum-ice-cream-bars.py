from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        
        for c in costs:
            freq[c] += 1
        
        count = 0
        for cost in range(1, max_cost + 1):
            while freq[cost] > 0 and coins >= cost:
                coins -= cost
                count += 1
                freq[cost] -= 1
        
        return count