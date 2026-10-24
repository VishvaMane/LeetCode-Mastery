class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_days(date: str) -> int:
            m, d = int(date[:2]), int(date[3:])
            return sum(months[:m-1]) + d
        
        start_alice = date_to_days(arriveAlice)
        end_alice = date_to_days(leaveAlice)
        start_bob = date_to_days(arriveBob)
        end_bob = date_to_days(leaveBob)
        
        start = max(start_alice, start_bob)
        end = min(end_alice, end_bob)
        
        return max(0, end - start + 1)