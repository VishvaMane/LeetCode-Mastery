class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(map(int, str(n)))
        digit_sum = sum(digits)
        digit_product = 1
        for digit in digits:
            digit_product *= digit
        total = digit_sum + digit_product
        return n % total == 0