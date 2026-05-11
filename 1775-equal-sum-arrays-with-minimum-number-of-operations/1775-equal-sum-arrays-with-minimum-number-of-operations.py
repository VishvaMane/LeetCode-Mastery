class Solution:
    def minOperations(self, nums1, nums2):
        s1 = sum(nums1)
        s2 = sum(nums2)

        # make sure s1 <= s2
        if s1 > s2:
            return self.minOperations(nums2, nums1)

        # check if equalization is even possible
        n1, n2 = len(nums1), len(nums2)
        if n1 * 6 < n2 or n2 * 1 > n1 * 6:
            return -1

        # how many changes of size 1,2,3,4,5 can we make?
        # count[i] = number of elements that can contribute i extra to reduce the gap
        count = [0] * 6  # index 0–5 for changes 1–5

        # nums1: can increase; max gain = 6 - x
        for x in nums1:
            count[6 - x] += 1

        # nums2: can decrease; max reduction = x - 1
        for x in nums2:
            count[x - 1] += 1

        # gap to close
        diff = s2 - s1
        ops = 0

        # use largest possible change first (5, then 4, ..., 1)
        for d in range(5, 0, -1):
            if diff <= 0:
                break
            # how many d‑sized changes can we use?
            need = (diff + d - 1) // d  # ceil(diff / d)
            use = min(need, count[d])
            diff -= use * d
            ops += use

        return ops if diff <= 0 else -1