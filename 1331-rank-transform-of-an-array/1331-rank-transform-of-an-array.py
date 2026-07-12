from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for a in sorted(arr):
            if a not in rank:
                rank[a] = len(rank) + 1
        return [rank[a] for a in arr]