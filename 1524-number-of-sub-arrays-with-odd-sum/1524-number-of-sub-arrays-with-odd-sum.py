class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        curr = 0
        ans = 0
        
        for num in arr:
            curr ^= num & 1
            if curr:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
                
        return ans % MOD