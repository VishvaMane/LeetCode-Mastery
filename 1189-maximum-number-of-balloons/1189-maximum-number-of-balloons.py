from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        
        # Required counts for "balloon"
        b = cnt['b']
        a = cnt['a']
        l = cnt['l'] // 2
        o = cnt['o'] // 2
        n = cnt['n']
        
        return min(b, a, l, o, n)