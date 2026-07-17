class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        cnt1 = num[:half].count('?')
        cnt2 = num[half:].count('?')
        s1 = sum(int(c) for c in num[:half] if c != '?')
        s2 = sum(int(c) for c in num[half:] if c != '?')
        
        if (cnt1 + cnt2) % 2 == 1:
            return True  # Alice wins
        
        return s1 - s2 != 9 * (cnt2 - cnt1) // 2