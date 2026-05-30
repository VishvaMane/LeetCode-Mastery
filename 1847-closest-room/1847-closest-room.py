from bisect import bisect_left, insort
from typing import List

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        qs = [[q[0], q[1], i] for i, q in enumerate(queries)]
        
        rooms.sort(key=lambda x: -x[1])
        qs.sort(key=lambda x: -x[1])
        
        roomIds = []
        i = 0
        
        for preferred, minSize, idx in qs:
            while i < len(rooms) and rooms[i][1] >= minSize:
                insort(roomIds, rooms[i][0])
                i += 1
            
            if not roomIds:
                ans[idx] = -1
                continue
            
            pos = bisect_left(roomIds, preferred)
            candidates = []
            if pos < len(roomIds):
                candidates.append(roomIds[pos])
            if pos > 0:
                candidates.append(roomIds[pos - 1])
            
            best = min(candidates, key=lambda x: (abs(x - preferred), x))
            ans[idx] = best
        
        return ans