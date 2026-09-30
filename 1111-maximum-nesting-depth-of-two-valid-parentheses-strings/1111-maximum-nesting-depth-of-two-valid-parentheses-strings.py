class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign based on current depth, then increase
                result.append(depth & 1)
                depth += 1
            else:  # char == ')'
                # Decrease depth first, then assign
                depth -= 1
                result.append(depth & 1)
        
        return result