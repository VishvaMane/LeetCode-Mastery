class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        arr = sorted([(num, i) for i, num in enumerate(nums)])
        ans = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1
            
            indices = sorted(arr[k][1] for k in range(i, j))
            for k, idx in enumerate(indices):
                ans[idx] = arr[i + k][0]
                
            i = j
            
        return ans   