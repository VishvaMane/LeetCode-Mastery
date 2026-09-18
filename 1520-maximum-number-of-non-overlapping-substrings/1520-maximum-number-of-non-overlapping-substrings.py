class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: s.find(c) for c in set(s)}
        last = {c: s.rfind(c) for c in set(s)}
        
        intervals = []
        for c in set(s):
            b = first[c]
            e = last[c]
            i = b
            valid = True
            
            while i <= e:
                if first[s[i]] < b:
                    valid = False
                    break
                e = max(e, last[s[i]])
                i += 1
                
            if valid:
                intervals.append((e, b))
                
        intervals.sort()
        
        ans = []
        prev_end = -1
        
        for e, b in intervals:
            if b > prev_end:
                ans.append(s[b:e+1])
                prev_end = e
                
        return ans