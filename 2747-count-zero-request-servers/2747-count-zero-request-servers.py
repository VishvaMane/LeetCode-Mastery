class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        freq = [0] * (n + 1)
        unique_servers = 0
        left = 0
        right = 0
        m = len(logs)
        ans = [0] * len(queries)
        
        for q_time, q_idx in sorted_queries:
            start_time = q_time - x
            end_time = q_time
            
            while right < m and logs[right][1] <= end_time:
                server_id = logs[right][0]
                if freq[server_id] == 0:
                    unique_servers += 1
                freq[server_id] += 1
                right += 1
                
            while left < right and logs[left][1] < start_time:
                server_id = logs[left][0]
                freq[server_id] -= 1
                if freq[server_id] == 0:
                    unique_servers -= 1
                left += 1
                
            ans[q_idx] = n - unique_servers
            
        return ans