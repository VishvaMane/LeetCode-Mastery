class Solution:
    def maxSumMinProduct(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        stack = []
        max_prod = 0
        for i in range(n+1):
            cur = nums[i] if i < n else 0
            while stack and nums[stack[-1]] > cur:
                mid = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                total = prefix[right+1] - prefix[left]
                prod = nums[mid] * total
                if prod > max_prod:
                    max_prod = prod
            stack.append(i)
        return max_prod % MOD
        