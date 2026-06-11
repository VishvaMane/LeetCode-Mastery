from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        s1 = [[0] * (n + 2) for _ in range(m + 1)]
        s2 = [[0] * (n + 2) for _ in range(m + 1)]
        
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s1[i][j] = s1[i - 1][j - 1] + x
                s2[i][j] = s2[i - 1][j + 1] + x
        
        sums = set()
        
        for i, row in enumerate(grid, 1):
            for j, center_value in enumerate(row, 1):
                sums.add(center_value)
                max_radius = min(i - 1, m - i, j - 1, n - j)
                
                for k in range(1, max_radius + 1):
                    a = s1[i + k][j] - s1[i][j - k]
                    b = s1[i][j + k] - s1[i - k][j]
                    c = s2[i][j - k] - s2[i - k][j]
                    d = s2[i + k][j] - s2[i][j + k]
                    
                    rhombus_sum = a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
                    sums.add(rhombus_sum)
        
        sorted_sums = sorted(sums, reverse=True)
        return sorted_sums[:3]