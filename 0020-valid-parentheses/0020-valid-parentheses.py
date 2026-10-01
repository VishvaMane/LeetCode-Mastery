class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():  
                stack.append(char)
            else:  
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        
        return len(stack) == 0