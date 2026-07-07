class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0
        for ch in str(n):
            if ch != '0':
                d = ord(ch) - ord('0')
                x = x * 10 + d
                s += d
        return x * s