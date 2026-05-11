class Solution:
    def nearestValidPoint(self, x, y, points):
        ans = -1
        mn = 10**9

        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)

                if d < mn:
                    mn = d
                    ans = i

        return ans