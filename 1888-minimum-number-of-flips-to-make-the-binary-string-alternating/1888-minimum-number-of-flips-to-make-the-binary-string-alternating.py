class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        ans = n
        m1 = m2 = 0

        for i, ch in enumerate(t):
            exp1 = '0' if i % 2 == 0 else '1'
            exp2 = '1' if i % 2 == 0 else '0'

            if ch != exp1:
                m1 += 1
            if ch != exp2:
                m2 += 1

            if i >= n:
                j = i - n
                old = t[j]
                old_exp1 = '0' if j % 2 == 0 else '1'
                old_exp2 = '1' if j % 2 == 0 else '0'

                if old != old_exp1:
                    m1 -= 1
                if old != old_exp2:
                    m2 -= 1

            if i >= n - 1:
                ans = min(ans, m1, m2)

        return ans