class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        
        for char in s:
            if char == '(':
                stack.append([])
            elif char == ')':
                reversed_chunk = stack.pop()[::-1]
                stack[-1].extend(reversed_chunk)
            else:
                stack[-1].append(char)
                
        return "".join(stack[0])