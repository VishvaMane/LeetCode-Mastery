class Solution:
    def maxValue(self, n: str, x: int) -> str:
        is_negative = n[0] == '-'
        
        for i, c in enumerate(n):
            if c == '-':
                continue
            digit = int(c)
            if (not is_negative and digit < x) or (is_negative and digit > x):
                return n[:i] + str(x) + n[i:]
        
        return n + str(x)