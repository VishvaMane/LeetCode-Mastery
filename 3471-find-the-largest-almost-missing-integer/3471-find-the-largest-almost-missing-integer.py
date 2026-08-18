class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        counts = {}
        for i in range(len(nums) - k + 1):
            for num in set(nums[i:i + k]):
                counts[num] = counts.get(num, 0) + 1
        
        ans = -1
        for num, c in counts.items():
            if c == 1:
                if num > ans:
                    ans = num
                    
        return ans