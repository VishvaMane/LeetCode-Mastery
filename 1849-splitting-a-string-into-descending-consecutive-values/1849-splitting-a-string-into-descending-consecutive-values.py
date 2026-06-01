class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(i: int, prev: int, parts: int) -> bool:
            if i == n:
                return parts >= 2

            cur = 0
            for j in range(i, n):
                cur = cur * 10 + (ord(s[j]) - ord('0'))

                if prev == -1 or prev - cur == 1:
                    if dfs(j + 1, cur, parts + 1):
                        return True

                if prev != -1 and cur >= prev:
                    break

            return False

        return dfs(0, -1, 0)