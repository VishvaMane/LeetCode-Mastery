class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        chars = list(s)
        
        tree_max = [1] * (4 * n)
        tree_pref = [1] * (4 * n)
        tree_suff = [1] * (4 * n)
        
        def merge(node, l, mid, r):
            left = 2 * node
            right = 2 * node + 1
            left_len = mid - l + 1
            right_len = r - mid
            
            if chars[mid] == chars[mid + 1]:
                tree_max[node] = max(tree_max[left], tree_max[right], tree_suff[left] + tree_pref[right])
                tree_pref[node] = tree_pref[left] + tree_pref[right] if tree_pref[left] == left_len else tree_pref[left]
                tree_suff[node] = tree_suff[right] + tree_suff[left] if tree_suff[right] == right_len else tree_suff[right]
            else:
                tree_max[node] = max(tree_max[left], tree_max[right])
                tree_pref[node] = tree_pref[left]
                tree_suff[node] = tree_suff[right]
        
        def build(node, l, r):
            if l == r:
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, l, mid, r)
            
        def update(node, l, r, idx):
            if l == r:
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx)
            else:
                update(2 * node + 1, mid + 1, r, idx)
            merge(node, l, mid, r)
            
        build(1, 0, n - 1)
        
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            chars[idx] = queryCharacters[i]
            update(1, 0, n - 1, idx)
            ans.append(tree_max[1])
            
        return ans