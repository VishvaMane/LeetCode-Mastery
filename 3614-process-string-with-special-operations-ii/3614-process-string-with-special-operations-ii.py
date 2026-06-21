class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        
        sz = 0
        sizes = [0] * n
        
        for i, c in enumerate(s):
            if c == '*':
                if sz > 0:
                    sz -= 1
            elif c == '#':
                sz *= 2
            elif c == '%':
                pass
            else:
                sz += 1
            sizes[i] = sz
        
        if k >= sz:
            return '.'
        
        for i in range(n - 1, -1, -1):
            c = s[i]
            sz = sizes[i]
            
            if c == '*':
                continue
            elif c == '#':
                if k >= sz // 2:
                    k -= sz // 2
            elif c == '%':
                k = sz - 1 - k
            else:
                if k == sz - 1:
                    return c
        
        return '.'