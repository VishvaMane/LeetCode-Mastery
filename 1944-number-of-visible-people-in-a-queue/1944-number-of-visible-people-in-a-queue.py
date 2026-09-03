class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        ans = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
                
            if stack:
                count += 1
                
            ans[i] = count
            stack.append(heights[i])
            
        return ans