import math

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 2
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = math.gcd(g, x)
                l = math.lcm(l, x)
                if p == l * g:
                    if j - i + 1 > ans:
                        ans = j - i + 1
                elif p > 25200:
                    break
        return ans