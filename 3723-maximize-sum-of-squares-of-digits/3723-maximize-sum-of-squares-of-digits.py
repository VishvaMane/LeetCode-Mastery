class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        q, r = divmod(sum, 9)
        if q == num:
            return "9" * num
            
        return "9" * q + str(r) + "0" * (num - q - 1)