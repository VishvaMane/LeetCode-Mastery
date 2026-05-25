class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in queries:
            cnt = 0
            r_sq = r * r
            for xi, yi in points:
                dx, dy = xi - x, yi - y
                if dx*dx + dy*dy <= r_sq:
                    cnt += 1
            ans.append(cnt)
        return ans