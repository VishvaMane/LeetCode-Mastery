class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff = [0] * 102
        base = 1950

        for birth, death in logs:
            diff[birth - base] += 1
            diff[death - base] -= 1

        curr = 0
        best = 0
        ans = 1950

        for i in range(101):
            curr += diff[i]
            if curr > best:
                best = curr
                ans = base + i

        return ans