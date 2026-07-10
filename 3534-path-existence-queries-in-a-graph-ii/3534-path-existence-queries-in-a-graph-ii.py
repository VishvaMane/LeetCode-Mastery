from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        U = sorted(list(set(nums)))
        N_U = len(U)
        val_to_idx = {v: i for i, v in enumerate(U)}
        
        comp = [0] * N_U
        c = 0
        for i in range(1, N_U):
            if U[i] - U[i-1] > maxDiff:
                c += 1
            comp[i] = c
            
        # Initialize binary lifting table
        up = [[0] * 18 for _ in range(N_U)]
        
        right = 0
        for i in range(N_U):
            while right + 1 < N_U and U[right + 1] <= U[i] + maxDiff:
                right += 1
            up[i][0] = right
            
        for k in range(1, 18):
            for i in range(N_U):
                up[i][k] = up[up[i][k-1]][k-1]
                
        ans = []
        for u, v in queries:
            # Same exact node = 0 distance
            if u == v:
                ans.append(0)
                continue
                
            A, B = nums[u], nums[v]
            
            # Different nodes but same value = 1 step
            if A == B:
                ans.append(1)
                continue
                
            if A > B:
                A, B = B, A
                
            start = val_to_idx[A]
            end = val_to_idx[B]
            
            # Check if they are in the same reachable component
            if comp[start] != comp[end]:
                ans.append(-1)
                continue
                
            target = B - maxDiff
            if U[start] >= target:
                ans.append(1)
                continue
                
            steps = 0
            curr = start
            
            # Binary lifting to find the minimum jumps to reach >= target
            for k in range(17, -1, -1):
                nxt = up[curr][k]
                if U[nxt] < target:
                    curr = nxt
                    steps += (1 << k)
                    
            ans.append(steps + 2)
            
        return ans