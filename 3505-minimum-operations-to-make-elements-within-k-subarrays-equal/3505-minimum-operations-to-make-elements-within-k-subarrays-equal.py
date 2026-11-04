import collections
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Max-heap for the lower half of the sliding window
        L = [] 
        # Min-heap for the upper half of the sliding window
        R = [] 
        
        # Dictionaries for lazy deletion
        delayed_L = collections.defaultdict(int)
        delayed_R = collections.defaultdict(int)
        
        sum_L = 0
        sum_R = 0
        size_L = 0
        size_R = 0
        
        def prune_L():
            while L and delayed_L[-L[0]] > 0:
                val = -L[0]
                delayed_L[val] -= 1
                if delayed_L[val] == 0:
                    del delayed_L[val]
                heapq.heappop(L)

        def prune_R():
            while R and delayed_R[R[0]] > 0:
                val = R[0]
                delayed_R[val] -= 1
                if delayed_R[val] == 0:
                    del delayed_R[val]
                heapq.heappop(R)

        def insert(val):
            nonlocal sum_L, sum_R, size_L, size_R
            prune_L()
            if L and val <= -L[0]:
                heapq.heappush(L, -val)
                sum_L += val
                size_L += 1
            else:
                heapq.heappush(R, val)
                sum_R += val
                size_R += 1

        def remove(val):
            nonlocal sum_L, sum_R, size_L, size_R
            prune_L()
            if L and val <= -L[0]:
                delayed_L[val] += 1
                sum_L -= val
                size_L -= 1
            else:
                delayed_R[val] += 1
                sum_R -= val
                size_R -= 1

        def balance():
            nonlocal sum_L, sum_R, size_L, size_R
            target_L = (size_L + size_R + 1) // 2
            
            while size_L < target_L:
                prune_R()
                val = heapq.heappop(R)
                sum_R -= val
                size_R -= 1
                
                heapq.heappush(L, -val)
                sum_L += val
                size_L += 1
                
            while size_L > target_L:
                prune_L()
                val = -heapq.heappop(L)
                sum_L -= val
                size_L -= 1
                
                heapq.heappush(R, val)
                sum_R += val
                size_R += 1

        def get_cost():
            prune_L()
            median = -L[0]
            # Since elements in L are <= median and elements in R are >= median
            # The cost is just the summation of absolute differences
            return (size_L * median - sum_L) + (sum_R - size_R * median)

        C = []
        for i in range(x - 1):
            insert(nums[i])
            balance()
            
        for i in range(x - 1, n):
            insert(nums[i])
            balance()
            C.append(get_cost())
            remove(nums[i - x + 1])
            

        dp = [0] * (n + 1)
        for j in range(1, k + 1):
            new_dp = [float('inf')] * (n + 1)
            for i in range(j * x, n + 1):
                ans = new_dp[i - 1]
                cand = dp[i - x] + C[i - x]
                if cand < ans:
                    ans = cand
                new_dp[i] = ans
            dp = new_dp
            
        return int(dp[n])