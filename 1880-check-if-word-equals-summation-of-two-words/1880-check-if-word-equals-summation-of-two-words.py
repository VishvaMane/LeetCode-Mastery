class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(word: str) -> int:
            num = 0
            for ch in word:
                num = num * 10 + (ord(ch) - ord('a'))
            return num
        
        return value(firstWord) + value(secondWord) == value(targetWord)