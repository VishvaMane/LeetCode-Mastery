from math import gcd

class Solution:
    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = []
        mx = 0
        
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))
        
        prefixGcd.sort()
        
        left, right = 0, n - 1
        total = 0
        
        while left < right:
            total += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total