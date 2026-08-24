import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        n = len(times)
        events = sorted([(times[i][0], times[i][1], i) for i in range(n)])
        
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)
        
        occupied_chairs = []
        
        for arrival, leaving, friend_id in events:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)
                
            chair = heapq.heappop(available_chairs)
            
            if friend_id == targetFriend:
                return chair
                
            heapq.heappush(occupied_chairs, (leaving, chair))
            
        return -1