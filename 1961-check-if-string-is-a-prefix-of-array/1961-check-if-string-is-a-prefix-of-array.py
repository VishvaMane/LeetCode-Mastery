class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        i = 0
        for word in words:
            if s[i:i+len(word)] == word:
                i += len(word)
                if i == len(s):
                    return True
            else:
                return False
        return False