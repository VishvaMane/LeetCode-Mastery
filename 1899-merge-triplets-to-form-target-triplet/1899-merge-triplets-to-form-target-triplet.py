from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        found_x = found_y = found_z = False

        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a == x:
                    found_x = True
                if b == y:
                    found_y = True
                if c == z:
                    found_z = True

        return found_x and found_y and found_z