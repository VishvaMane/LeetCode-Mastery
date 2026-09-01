import collections

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        
        start_r = start_c = -1
        litter_idx = {}
        k = 0
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_r, start_c = i, j
                elif classroom[i][j] == 'L':
                    litter_idx[(i, j)] = k
                    k += 1
                    
        if k == 0:
            return 0
            
        target_mask = (1 << k) - 1
        visited = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        visited[start_r][start_c][0] = energy
        
        q = collections.deque([(0, start_r, start_c, 0, energy)])
        
        while q:
            moves, r, c, mask, e = q.popleft()
            
            if e == 0:
                continue
                
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    nmask = mask
                    
                    if classroom[nr][nc] == 'R':
                        ne = energy
                    elif classroom[nr][nc] == 'L':
                        nmask |= (1 << litter_idx[(nr, nc)])
                        
                    if nmask == target_mask:
                        return moves + 1
                        
                    if ne > visited[nr][nc][nmask]:
                        visited[nr][nc][nmask] = ne
                        q.append((moves + 1, nr, nc, nmask, ne))
                        
        return -1