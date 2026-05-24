class Solution:
    def arraySign(self, nums):
        sign = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                sign = -sign
        return sign