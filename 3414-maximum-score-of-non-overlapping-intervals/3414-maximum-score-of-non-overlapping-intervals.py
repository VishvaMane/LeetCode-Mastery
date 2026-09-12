import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
            
        arr.sort(key=lambda x: (x[1], x[0], x[2], x[3]))
        R = [x[1] for x in arr]
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            l, r, w, idx = arr[i-1]
            j = bisect.bisect_left(R, l)
            
            for k in range(1, 5):
                best = dp[i-1][k]
                
                prev_weight, prev_list = dp[j][k-1]
                new_weight = prev_weight - w
                new_list = sorted(prev_list + [idx])
                
                cand = (new_weight, new_list)
                if cand < best:
                    best = cand
                    
                dp[i][k] = best
                
        return dp[n][4][1]