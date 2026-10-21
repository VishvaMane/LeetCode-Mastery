class Solution:
    def minOperations(self, s: str) -> int:
        is_sorted = True
        for i in range(len(s) - 1):
            if s[i] > s[i+1]:
                is_sorted = False
                break
        
        if is_sorted:
            return 0
            
        n = len(s)
        if n == 2:
            return -1
            
        min_c = min(s)
        max_c = max(s)
        
        if s[0] == min_c or s[-1] == max_c:
            return 1
            
        if s[0] == max_c and s[-1] == min_c and s.count(max_c) == 1 and s.count(min_c) == 1:
            return 3
            
        return 2