class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def to_minutes(t: str) -> int:
            return int(t[:2]) * 60 + int(t[3:])

        start = to_minutes(loginTime)
        end = to_minutes(logoutTime)

        if end < start:
            end += 24 * 60

        start = ((start + 14) // 15) * 15
        end = (end // 15) * 15

        return max(0, (end - start) // 15)