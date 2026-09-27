class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        radius = [0] * n
        center = 0
        right = 0
        
        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                radius[i] = min(right - i, radius[mirror])
            
            while i - 1 - radius[i] >= 0 and i + 1 + radius[i] < n and s[i - 1 - radius[i]] == s[i + 1 + radius[i]]:
                radius[i] += 1
            
            if i + radius[i] > right:
                center = i
                right = i + radius[i]
                
        left = [0] * n
        left[0] = 1
        c = 0
        for i in range(1, n):
            while c + radius[c] < i:
                c += 1
            left[i] = max(left[i - 1], 2 * (i - c) + 1)
            
        right_arr = [0] * n
        right_arr[n - 1] = 1
        c = n - 1
        for i in range(n - 2, -1, -1):
            while c - radius[c] > i:
                c -= 1
            right_arr[i] = max(right_arr[i + 1], 2 * (c - i) + 1)
            
        ans = 0
        for i in range(n - 1):
            if left[i] * right_arr[i + 1] > ans:
                ans = left[i] * right_arr[i + 1]
                
        return ans