import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        heapq.heapify(available)
        used_free = []
        busy = []
        handled = [0] * k

        for i in range(len(arrival)):
            arr = arrival[i]
            l = load[i]
            p = i % k

            if p == 0 and used_free:
                available.extend(used_free)
                used_free.clear()
                heapq.heapify(available)

            while busy and busy[0][0] <= arr:
                _, server_id = heapq.heappop(busy)
                if server_id >= p:
                    heapq.heappush(available, server_id)
                else:
                    heapq.heappush(used_free, server_id)

            while available and available[0] < p:
                heapq.heappush(used_free, heapq.heappop(available))

            if available:
                server_id = heapq.heappop(available)
            elif used_free:
                server_id = heapq.heappop(used_free)
            else:
                continue

            handled[server_id] += 1
            heapq.heappush(busy, (arr + l, server_id))

        max_handled = max(handled)
        return [i for i, count in enumerate(handled) if count == max_handled]