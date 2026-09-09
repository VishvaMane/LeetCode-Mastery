class Solution:
    def numberOfWeeks(self, milestones: list[int]) -> int:
        total = sum(milestones)
        max_m = max(milestones)
        rest = total - max_m
        
        if max_m > rest + 1:
            return 2 * rest + 1
        return total