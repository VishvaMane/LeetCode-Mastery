class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_perm(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            l, r = i + 1, len(arr) - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        target = list(num)
        for _ in range(k):
            next_perm(target)

        s = list(num)
        ans = 0
        for i in range(len(s)):
            if s[i] == target[i]:
                continue
            j = i + 1
            while s[j] != target[i]:
                j += 1
            while j > i:
                s[j], s[j - 1] = s[j - 1], s[j]
                j -= 1
                ans += 1
        return ans