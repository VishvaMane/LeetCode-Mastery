class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        counts = [0] * 32
        
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    counts[i] += 1
                    
        ans = 0
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if counts[i] > 0:
                    current_num |= (1 << i)
                    counts[i] -= 1
            ans = (ans + current_num * current_num) % MOD
            
        return ans