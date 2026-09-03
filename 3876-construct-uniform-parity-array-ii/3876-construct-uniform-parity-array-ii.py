class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')
        
        for num in nums1:
            if num % 2 == 0:
                if num < min_even:
                    min_even = num
            else:
                if num < min_odd:
                    min_odd = num
                    
        if min_odd == float('inf') or min_even == float('inf'):
            return True
            
        return min_odd < min_even