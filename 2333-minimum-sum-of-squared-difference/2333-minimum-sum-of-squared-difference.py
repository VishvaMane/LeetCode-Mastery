class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        k = k1 + k2
        
        if sum(diffs) <= k:
            return 0
            
        max_val = max(diffs)
        counts = [0] * (max_val + 1)
        
        for d in diffs:
            counts[d] += 1
            
        for i in range(max_val, 0, -1):
            if counts[i] > 0:
                if k >= counts[i]:
                    counts[i - 1] += counts[i]
                    k -= counts[i]
                    counts[i] = 0
                else:
                    counts[i - 1] += k
                    counts[i] -= k
                    k = 0
                    break
                    
        ans = 0
        for i in range(1, max_val + 1):
            if counts[i] > 0:
                ans += counts[i] * i * i
                
        return ans