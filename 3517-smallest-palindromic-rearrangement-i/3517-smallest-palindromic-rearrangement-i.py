class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        left = []
        mid = ""

        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + ord('a'))
            left.append(chr(i + ord('a')) * (freq[i] // 2))

        left = "".join(left)
        return left + mid + left[::-1]