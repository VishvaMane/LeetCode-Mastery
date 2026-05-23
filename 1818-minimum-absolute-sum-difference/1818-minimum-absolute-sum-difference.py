class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        sorted_nums1 = sorted(nums1)
        n = len(sorted_nums1)
        
        total_diff = sum(abs(a - b) for a, b in zip(nums1, nums2)) % MOD
        
        max_reduction = 0
        
        for num1, num2 in zip(nums1, nums2):
            current_diff = abs(num1 - num2)
            
            idx = bisect_left(sorted_nums1, num2)
            
            if idx < n:
                min_possible_diff = abs(sorted_nums1[idx] - num2)
            else:
                min_possible_diff = float('inf')
            
            if idx > 0:
                min_possible_diff = min(min_possible_diff, abs(sorted_nums1[idx - 1] - num2))
            
            reduction = current_diff - min_possible_diff
            max_reduction = max(max_reduction, reduction)
        
        return (total_diff - max_reduction + MOD) % MOD