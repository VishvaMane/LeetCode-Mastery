class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        is_asc = True
        is_desc = True
        idx = -1
        
        for i in range(n):
            if nums[i] == 0:
                idx = i
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                is_asc = False
            if nums[(i + 1) % n] != (nums[i] - 1) % n:
                is_desc = False
                
        if is_asc:
            return min(idx, n - idx + 2)
        if is_desc:
            return min((idx + 1) % n + 1, n - idx)
            
        return -1