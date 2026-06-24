class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        M = [[min(i, j) % MOD for j in range(m)] for i in range(m)]

        if n & 1:
            vec = [0] * m
            s = 0
            for v in range(m):
                vec[v] = s
                s = (s + (m - 1 - v)) % MOD
        else:
            vec = [i % MOD for i in range(m)]

        p = (n - 2) // 2

        def mat_mul(A, B):
            C = [[0] * m for _ in range(m)]
            for i in range(m):
                Ci = C[i]
                Ai = A[i]
                for k in range(m):
                    a = Ai[k]
                    if a:
                        Bk = B[k]
                        for j in range(m):
                            Ci[j] = (Ci[j] + a * Bk[j]) % MOD
            return C

        def mat_vec_mul(A, v):
            res = [0] * m
            for i in range(m):
                s = 0
                row = A[i]
                for j in range(m):
                    s = (s + row[j] * v[j]) % MOD
                res[i] = s
            return res

        base = M
        while p:
            if p & 1:
                vec = mat_vec_mul(base, vec)
            p >>= 1
            if p:
                base = mat_mul(base, base)

        return (2 * sum(vec)) % MOD