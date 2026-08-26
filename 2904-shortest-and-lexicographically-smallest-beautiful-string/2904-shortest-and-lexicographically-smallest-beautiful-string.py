class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, char in enumerate(s) if char == '1']
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        ans = ""
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start:end + 1]
            
            if len(sub) < min_len:
                min_len = len(sub)
                ans = sub
            elif len(sub) == min_len:
                if sub < ans:
                    ans = sub
                    
        return ans