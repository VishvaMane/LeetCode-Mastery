class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        parent = list(range(row * col + 2))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        top = row * col
        bottom = row * col + 1
        grid = [[0] * col for _ in range(row)]
        
        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1
            idx = r * col + c
            
            if r == 0:
                union(idx, top)
            if r == row - 1:
                union(idx, bottom)
                
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union(idx, nr * col + nc)
                    
            if find(top) == find(bottom):
                return i
                
        return 0