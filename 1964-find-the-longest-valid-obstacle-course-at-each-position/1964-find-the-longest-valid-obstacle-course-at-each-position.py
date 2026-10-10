import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        lis = []
        ans = []
        
        for x in obstacles:
            idx = bisect.bisect_right(lis, x)
            
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
                
            ans.append(idx + 1)
            
        return ans