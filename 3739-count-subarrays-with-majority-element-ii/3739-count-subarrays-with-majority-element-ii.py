from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, i, v=1):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [1 if v == target else -1 for v in nums]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + arr[i]
        all_vals = sorted(set(pref))
        idx = {v: i+1 for i, v in enumerate(all_vals)}
        fw = Fenwick(len(all_vals))
        ans = 0
        for p in pref:
            pos = idx[p]
            ans += fw.sum(pos-1)
            fw.add(pos, 1)
        return ans