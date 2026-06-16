class Solution:
    def twoEggDrop(self, n: int) -> int:
        m = 0
        total = 0
        while total < n:
            m += 1
            total += m
        return m