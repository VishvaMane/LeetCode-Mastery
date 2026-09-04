class Solution:
    def getLucky(self, s: str, k: int) -> int:
        val = "".join(str(ord(c) - 96) for c in s)
        
        for _ in range(k):
            val = str(sum(int(d) for d in val))
            
        return int(val)