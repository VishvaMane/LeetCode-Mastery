from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = defaultdict(int)
        for r, c in reservedSeats:
            rows[r] |= (1 << c)
            
        ans = (n - len(rows)) * 2
        
        for mask in rows.values():
            if (mask & 60) == 0 and (mask & 960) == 0:
                ans += 2
            elif (mask & 60) == 0 or (mask & 960) == 0 or (mask & 240) == 0:
                ans += 1
                
        return ans