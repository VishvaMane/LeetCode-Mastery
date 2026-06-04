class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = [""] * len(words)

        for w in words:
            pos = int(w[-1]) - 1
            ans[pos] = w[:-1]

        return " ".join(ans)