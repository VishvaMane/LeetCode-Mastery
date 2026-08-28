class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
            
        odd_count = sum(1 for f in freq if f % 2 != 0)
        if odd_count > 1:
            return ""
        if n % 2 == 0 and odd_count != 0:
            return ""
            
        mid_c = ""
        avail_freq = [0] * 26
        for i in range(26):
            if freq[i] % 2 != 0:
                mid_c = chr(i + 97)
            avail_freq[i] = freq[i] // 2
            
        half_n = n // 2
        target_left = target[:half_n]
        
        target_freq = [0] * 26
        for ch in target_left:
            target_freq[ord(ch) - 97] += 1
            
        if target_freq == avail_freq:
            P = target_left + mid_c + target_left[::-1]
            if P > target:
                return P
                
        for i in range(half_n - 1, -1, -1):
            prefix = target_left[:i]
            rem_freq = list(avail_freq)
            valid = True
            for ch in prefix:
                idx = ord(ch) - 97
                rem_freq[idx] -= 1
                if rem_freq[idx] < 0:
                    valid = False
                    break
                    
            if not valid:
                continue
                
            target_char_idx = ord(target_left[i]) - 97
            best_c_idx = -1
            for j in range(target_char_idx + 1, 26):
                if rem_freq[j] > 0:
                    best_c_idx = j
                    break
                    
            if best_c_idx != -1:
                rem_freq[best_c_idx] -= 1
                suffix = "".join(chr(j + 97) * rem_freq[j] for j in range(26))
                half_s = prefix + chr(best_c_idx + 97) + suffix
                return half_s + mid_c + half_s[::-1]
                
        return ""