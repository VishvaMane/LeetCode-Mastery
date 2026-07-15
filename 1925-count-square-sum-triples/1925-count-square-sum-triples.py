class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        squares = {c * c for c in range(1, n + 1)}
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a * a + b * b in squares:
                    count += 1
        return count