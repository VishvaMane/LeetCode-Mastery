class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        count = [0] * 10
        for d in digits:
            count[d] += 1
            
        ans = 0
        for i in range(100, 1000, 2):
            d1 = i // 100
            d2 = (i // 10) % 10
            d3 = i % 10
            
            count[d1] -= 1
            count[d2] -= 1
            count[d3] -= 1
            
            if count[d1] >= 0 and count[d2] >= 0 and count[d3] >= 0:
                ans += 1
                
            count[d1] += 1
            count[d2] += 1
            count[d3] += 1
            
        return ans