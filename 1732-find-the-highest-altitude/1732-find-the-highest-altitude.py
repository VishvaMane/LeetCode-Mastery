class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        best = 0

        for g in gain:
            curr += g
            best = max(best, curr)

        return best