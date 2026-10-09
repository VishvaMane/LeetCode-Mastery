class Solution:
    def minInsertions(self, s: str) -> int:
        req_right = 0
        insertions = 0
        
        for char in s:
            if char == '(':
                if req_right % 2 != 0:
                    insertions += 1
                    req_right -= 1
                req_right += 2
            else:
                req_right -= 1
                if req_right < 0:
                    insertions += 1
                    req_right = 1
                    
        return insertions + req_right