import collections

class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        mapping = collections.defaultdict(int)
        for start, end, color in segments:
            mapping[start] += color
            mapping[end] -= color
            
        res = []
        prev = None
        current_sum = 0
        
        for pos in sorted(mapping.keys()):
            if prev is not None and current_sum > 0:
                res.append([prev, pos, current_sum])
            current_sum += mapping[pos]
            prev = pos
            
        return res