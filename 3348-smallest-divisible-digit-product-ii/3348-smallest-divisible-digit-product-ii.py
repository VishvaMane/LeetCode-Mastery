class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        req2 = req3 = req5 = req7 = 0
        while temp % 2 == 0:
            req2 += 1
            temp //= 2
        while temp % 3 == 0:
            req3 += 1
            temp //= 3
        while temp % 5 == 0:
            req5 += 1
            temp //= 5
        while temp % 7 == 0:
            req7 += 1
            temp //= 7
        if temp > 1:
            return "-1"
            
        dp = [[0] * 35 for _ in range(55)]
        for i in range(55):
            for j in range(35):
                if i == 0 and j == 0:
                    continue
                res = float('inf')
                if i > 0: res = min(res, 1 + dp[max(0, i-1)][j])
                if j > 0: res = min(res, 1 + dp[i][max(0, j-1)])
                if i > 0: res = min(res, 1 + dp[max(0, i-2)][j])
                if i > 0 or j > 0: res = min(res, 1 + dp[max(0, i-1)][max(0, j-1)])
                if i > 0: res = min(res, 1 + dp[max(0, i-3)][j])
                if j > 0: res = min(res, 1 + dp[i][max(0, j-2)])
                dp[i][j] = res

        c2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        c3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        c5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        c7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        def build_greedy(length, r2, r3, r5, r7):
            res = []
            for _ in range(length):
                for d in range(1, 10):
                    nr2 = max(0, r2 - c2[d])
                    nr3 = max(0, r3 - c3[d])
                    nr5 = max(0, r5 - c5[d])
                    nr7 = max(0, r7 - c7[d])
                    if dp[nr2][nr3] + nr5 + nr7 <= length - 1 - len(res):
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        L = len(num)
        p2 = [0] * (L + 1)
        p3 = [0] * (L + 1)
        p5 = [0] * (L + 1)
        p7 = [0] * (L + 1)
        
        first_zero = num.find('0')
        start_i = L - 1 if first_zero == -1 else first_zero

        for i in range(start_i + 1):
            if i < L and num[i] != '0':
                d = int(num[i])
                p2[i+1] = p2[i] + c2[d]
                p3[i+1] = p3[i] + c3[d]
                p5[i+1] = p5[i] + c5[d]
                p7[i+1] = p7[i] + c7[d]

        if first_zero == -1:
            if p2[L] >= req2 and p3[L] >= req3 and p5[L] >= req5 and p7[L] >= req7:
                return num

        for i in range(start_i, -1, -1):
            rem2 = max(0, req2 - p2[i])
            rem3 = max(0, req3 - p3[i])
            rem5 = max(0, req5 - p5[i])
            rem7 = max(0, req7 - p7[i])
            
            min_d = int(num[i]) + 1
            for d in range(max(1, min_d), 10):
                nr2 = max(0, rem2 - c2[d])
                nr3 = max(0, rem3 - c3[d])
                nr5 = max(0, rem5 - c5[d])
                nr7 = max(0, rem7 - c7[d])
                
                if dp[nr2][nr3] + nr5 + nr7 <= L - 1 - i:
                    return num[:i] + str(d) + build_greedy(L - 1 - i, nr2, nr3, nr5, nr7)

        req_len = dp[req2][req3] + req5 + req7
        target_length = max(L + 1, req_len)
        return build_greedy(target_length, req2, req3, req5, req7)