class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
            
        L = 0
        req = [0] * 26
        while L < n:
            c = ord(target[L]) - 97
            req[c] += 1
            if req[c] > freq[c]:
                break
            L += 1
            
        for i in range(min(n - 1, L), -1, -1):
            rem = list(freq)
            for j in range(i):
                rem[ord(target[j]) - 97] -= 1
                
            tgt_c = ord(target[i]) - 97
            best_c = -1
            for c in range(tgt_c + 1, 26):
                if rem[c] > 0:
                    best_c = c
                    break
                    
            if best_c != -1:
                rem[best_c] -= 1
                suffix = "".join(chr(c + 97) * rem[c] for c in range(26))
                return target[:i] + chr(best_c + 97) + suffix
                
        return ""