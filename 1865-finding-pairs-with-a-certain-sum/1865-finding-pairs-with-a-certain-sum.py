from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.freq[old] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for x in self.nums1:
            ans += self.freq[tot - x]
        return ans