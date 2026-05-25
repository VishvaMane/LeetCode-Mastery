class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        
        for obstacle in obstacles[1:]:
            if obstacle:
                dp[obstacle - 1] = float('inf')
            
            min_jumps = min(dp) + 1
            
            for lane in range(3):
                if obstacle != lane + 1:
                    dp[lane] = min(dp[lane], min_jumps)
        
        return min(dp)