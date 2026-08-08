class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        suf = [-1] * m
        curr = n - 1
        
        for j in range(m - 1, -1, -1):
            while curr >= 0 and word1[curr] != word2[j]:
                curr -= 1
            if curr >= 0:
                suf[j] = curr
                curr -= 1
            else:
                suf[j] = -1
                
        ans = []
        j = 0
        skipped = False
        
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not skipped and (j + 1 == m or suf[j + 1] > i):
                ans.append(i)
                j += 1
                skipped = True
                
        return ans if len(ans) == m else []