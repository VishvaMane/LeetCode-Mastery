class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
        next_zero = [-1] * n
        curr = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = i
            next_zero[i] = curr
            
        prev_zero = [-1] * n
        curr = -1
        for i in range(n):
            if s[i] == '0':
                curr = i
            prev_zero[i] = curr

        zeros = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zeros.append((start, i - 1))
            else:
                i += 1

        z_id = [-1] * n
        for idx, (st, en) in enumerate(zeros):
            for j in range(st, en + 1):
                z_id[j] = idx

        Z_len = [en - st + 1 for st, en in zeros]
        N_z = len(zeros)
        
        O_len = []
        for j in range(N_z - 1):
            O_len.append(zeros[j+1][0] - zeros[j][1] - 1)
            
        Z_adj = []
        for j in range(N_z - 1):
            Z_adj.append(Z_len[j] + Z_len[j+1])

        def build_max_st(arr):
            m = len(arr)
            if not m: return []
            max_k = m.bit_length()
            st = [[0] * m for _ in range(max_k)]
            st[0] = list(arr)
            for k in range(1, max_k):
                step = 1 << (k - 1)
                for j in range(m - (1 << k) + 1):
                    st[k][j] = st[k-1][j] if st[k-1][j] > st[k-1][j + step] else st[k-1][j + step]
            return st

        def build_min_st(arr):
            m = len(arr)
            if not m: return []
            max_k = m.bit_length()
            st = [[0] * m for _ in range(max_k)]
            st[0] = list(arr)
            for k in range(1, max_k):
                step = 1 << (k - 1)
                for j in range(m - (1 << k) + 1):
                    st[k][j] = st[k-1][j] if st[k-1][j] < st[k-1][j + step] else st[k-1][j + step]
            return st

        st_Z_len = build_max_st(Z_len)
        st_O_len = build_min_st(O_len)
        st_Z_adj = build_max_st(Z_adj)

        def query_max(st, l, r):
            if l > r: return -1
            k = (r - l + 1).bit_length() - 1
            return st[k][l] if st[k][l] > st[k][r - (1 << k) + 1] else st[k][r - (1 << k) + 1]

        def query_min(st, l, r):
            if l > r: return float('inf')
            k = (r - l + 1).bit_length() - 1
            return st[k][l] if st[k][l] < st[k][r - (1 << k) + 1] else st[k][r - (1 << k) + 1]

        ans = []
        for L, R in queries:
            fz = next_zero[L]
            lz = prev_zero[R]
            
            if fz == -1 or fz > R or fz == lz:
                ans.append(total_ones)
                continue
                
            u = z_id[fz]
            v = z_id[lz]
            
            if u == v:
                ans.append(total_ones)
                continue
                
            b1 = zeros[u][1] - fz + 1
            bk = lz - zeros[v][0] + 1
            
            M_a = query_min(st_O_len, u, v - 1)
            
            M_b = b1 if b1 > bk else bk
            if v - 1 >= u + 1:
                mid_max = query_max(st_Z_len, u + 1, v - 1)
                if mid_max > M_b:
                    M_b = mid_max
                    
            if v == u + 1:
                M_adj = b1 + bk
            else:
                opt1 = b1 + Z_len[u+1]
                opt2 = Z_len[v-1] + bk
                M_adj = opt1 if opt1 > opt2 else opt2
                if v - 2 >= u + 1:
                    mid_adj = query_max(st_Z_adj, u + 1, v - 2)
                    if mid_adj > M_adj:
                        M_adj = mid_adj
                        
            gain = M_adj if M_adj > (M_b - M_a) else (M_b - M_a)
            ans.append(total_ones + gain)
            
        return ans