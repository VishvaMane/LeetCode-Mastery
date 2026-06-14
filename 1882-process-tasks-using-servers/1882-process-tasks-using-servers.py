import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        ans = [0] * m
        
        free = []
        used = []
        
        for i, weight in enumerate(servers):
            heapq.heappush(free, (weight, i, 0))
        
        for i in range(m):
            current_time = i
            execution_time = tasks[i]
            
            while used and used[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(used)
                heapq.heappush(free, (weight, idx, free_time))
            
            if free:
                weight, idx, free_time = heapq.heappop(free)
                ans[i] = idx
                heapq.heappush(used, (current_time + execution_time, weight, idx))
            else:
                free_time, weight, idx = heapq.heappop(used)
                ans[i] = idx
                heapq.heappush(used, (free_time + execution_time, weight, idx))
        
        return ans    