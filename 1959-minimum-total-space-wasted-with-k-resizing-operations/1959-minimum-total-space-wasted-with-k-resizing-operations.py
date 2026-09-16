from functools import cache

class Solution:
    def minSpaceWastedKResizing(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        @cache
        def dp(i: int, k_rem: int) -> int:
            if i == n:
                return 0
            if k_rem < 0:
                return float('inf')
            
            ans = float('inf')
            max_val = 0
            sum_val = 0
            
            for j in range(i, n):
                if nums[j] > max_val:
                    max_val = nums[j]
                sum_val += nums[j]
                
                waste = max_val * (j - i + 1) - sum_val
                ans = min(ans, waste + dp(j + 1, k_rem - 1))
                
            return ans
            
        return dp(0, k)