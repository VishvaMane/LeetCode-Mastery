class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_count = [[0] * k for _ in range(4 * n)]
        
        def build(node, start, end):
            if start == end:
                v = nums[start] % k
                tree_prod[node] = v
                tree_count[node][v] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
            l_prod = tree_prod[2 * node]
            r_prod = tree_prod[2 * node + 1]
            tree_prod[node] = (l_prod * r_prod) % k
            
            l_count = tree_count[2 * node]
            r_count = tree_count[2 * node + 1]
            
            for i in range(k):
                tree_count[node][i] = l_count[i]
            for i in range(k):
                if r_count[i]:
                    tree_count[node][(l_prod * i) % k] += r_count[i]
                    
        def update(node, start, end, idx, val):
            if start == end:
                v = val % k
                tree_prod[node] = v
                for i in range(k):
                    tree_count[node][i] = 0
                tree_count[node][v] = 1
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
                
            l_prod = tree_prod[2 * node]
            r_prod = tree_prod[2 * node + 1]
            tree_prod[node] = (l_prod * r_prod) % k
            
            l_count = tree_count[2 * node]
            r_count = tree_count[2 * node + 1]
            
            for i in range(k):
                tree_count[node][i] = l_count[i]
            for i in range(k):
                if r_count[i]:
                    tree_count[node][(l_prod * i) % k] += r_count[i]

        def query(node, start, end, ql, qr):
            if ql <= start and end <= qr:
                return tree_prod[node], tree_count[node]
            mid = (start + end) // 2
            if qr <= mid:
                return query(2 * node, start, mid, ql, qr)
            elif ql > mid:
                return query(2 * node + 1, mid + 1, end, ql, qr)
            else:
                l_prod, l_count = query(2 * node, start, mid, ql, qr)
                r_prod, r_count = query(2 * node + 1, mid + 1, end, ql, qr)
                
                n_prod = (l_prod * r_prod) % k
                n_count = list(l_count)
                for i in range(k):
                    if r_count[i]:
                        n_count[(l_prod * i) % k] += r_count[i]
                return n_prod, n_count

        build(1, 0, n - 1)
        ans = []
        for idx, val, start_idx, x in queries:
            update(1, 0, n - 1, idx, val)
            _, res_count = query(1, 0, n - 1, start_idx, n - 1)
            ans.append(res_count[x])
            
        return ans