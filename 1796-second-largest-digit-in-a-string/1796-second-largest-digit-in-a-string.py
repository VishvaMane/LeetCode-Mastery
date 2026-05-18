class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1

        for ch in s:
            if ch.isdigit():
                d = int(ch)

                if d > first:
                    second = first
                    first = d
                elif first > d > second:
                    second = d

        return second