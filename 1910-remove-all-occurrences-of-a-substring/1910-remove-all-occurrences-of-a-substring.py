class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        stack = []

        for ch in s:
            stack.append(ch)
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                del stack[-part_len:]

        return ''.join(stack)