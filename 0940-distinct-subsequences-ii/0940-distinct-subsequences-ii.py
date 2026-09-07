class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007
        endsIn = [0] * 26
        
        for c in s:
            endsIn[ord(c) - ord('a')] = (sum(endsIn) + 1) % MOD
        
        return sum(endsIn) % MOD