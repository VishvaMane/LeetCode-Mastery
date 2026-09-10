class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left = 1
        right = 100000
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if 2 * mid * (mid + 1) * (2 * mid + 1) >= neededApples:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans * 8  