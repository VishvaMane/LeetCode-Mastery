class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1
        res = 0
        mask = 0
        
        for char in word:
            mask ^= 1 << (ord(char) - ord('a'))
            res += count[mask]
            for i in range(10):
                res += count[mask ^ (1 << i)]
            count[mask] += 1
            
        return res