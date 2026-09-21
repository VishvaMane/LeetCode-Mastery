class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        total = [0] * k
        current = [0] * k
        
        for num in nums:
            next_curr = [0] * k
            val = num % k
            next_curr[val] += 1
            
            for r in range(k):
                if current[r] > 0:
                    next_curr[(r * val) % k] += current[r]
                    
            current = next_curr
            for r in range(k):
                total[r] += current[r]
                
        return total