class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        ans = 0
        curr = 0
        for rung in rungs:
            ans += (rung - curr - 1) // dist
            curr = rung
        return ans