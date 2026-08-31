class Solution:
    def nodesBetweenCriticalPoints(self, head: 'ListNode' | None) -> list[int]:
        first_idx = -1
        last_idx = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                last_idx = idx
            
            prev = curr
            curr = curr.next
            idx += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
            
        return [min_dist, last_idx - first_idx]