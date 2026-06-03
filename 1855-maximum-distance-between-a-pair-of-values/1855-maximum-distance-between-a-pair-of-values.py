class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_dist = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # Valid pair, update max distance
                max_dist = max(max_dist, j - i)
                j += 1  # Try to find farther j
            else:
                # nums1[i] > nums2[j], need larger nums2 value
                i += 1  # Move i forward to get smaller nums1[i]
        
        return max_dist