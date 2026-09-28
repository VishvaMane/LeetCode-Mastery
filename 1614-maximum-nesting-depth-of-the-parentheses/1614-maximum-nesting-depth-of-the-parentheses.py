class Solution:
    def maxDepth(self, s: str) -> int:
        max_d = 0
        curr = 0
        
        for c in s:
            if c == '(':
                curr += 1
                max_d = max(max_d, curr)
            elif c == ')':
                curr -= 1
        
        return max_d