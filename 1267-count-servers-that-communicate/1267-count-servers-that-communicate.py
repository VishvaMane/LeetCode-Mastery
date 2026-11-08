class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(col) for col in zip(*grid)]
        
        return sum(
            1
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1)
        )