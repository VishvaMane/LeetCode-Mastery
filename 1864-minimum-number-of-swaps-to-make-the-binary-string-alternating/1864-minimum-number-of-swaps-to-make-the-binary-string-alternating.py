class Solution:
    def minSwaps(self, s: str) -> int:
        n0 = s.count('0')
        n1 = len(s) - n0
        
        if abs(n0 - n1) > 1:
            return -1
        
        def calc(start_with: int) -> int:
            cnt = 0
            for i, ch in enumerate(s):
                expected = start_with ^ (i & 1)
                if int(ch) != expected:
                    cnt += 1
            return cnt // 2
        
        if n0 == n1:
            return min(calc(0), calc(1))
        elif n0 > n1:
            return calc(0)
        else:
            return calc(1)