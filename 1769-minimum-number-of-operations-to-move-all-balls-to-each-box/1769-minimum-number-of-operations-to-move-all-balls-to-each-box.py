class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        ans = [0] * n
        
        balls = 0
        cost = 0
        for i in range(n):
            ans[i] += cost
            if boxes[i] == '1':
                balls += 1
            cost += balls
        
        balls = 0
        cost = 0
        for i in range(n-1, -1, -1):
            ans[i] += cost
            if boxes[i] == '1':
                balls += 1
            cost += balls
        
        return ans