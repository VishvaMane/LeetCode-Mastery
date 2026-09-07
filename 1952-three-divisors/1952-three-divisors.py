class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors += 1 if i * i == n else 2
            if divisors > 3:
                return False
        return divisors == 3