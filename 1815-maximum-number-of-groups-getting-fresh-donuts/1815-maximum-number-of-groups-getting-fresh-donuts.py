class Solution:
    def maxHappyGroups(self, batchSize: int, groups) -> int:
        mod0 = 0
        cnt = [0] * batchSize

        for g in groups:
            r = g % batchSize
            if r == 0:
                mod0 += 1
            else:
                cnt[r] += 1

        for i in range(1, (batchSize + 1) // 2):
            pairs = min(cnt[i], cnt[batchSize - i])
            mod0 += pairs
            cnt[i] -= pairs
            cnt[batchSize - i] -= pairs

        memo = {}

        def dfs(cnt, rem):
            key = tuple(cnt[1:]) + (rem,)
            if key in memo:
                return memo[key]

            best = 0
            for r in range(1, batchSize):
                if cnt[r] == 0:
                    continue
                cnt[r] -= 1
                new_rem = (rem + r) % batchSize
                happy = 1 if rem == 0 else 0
                best = max(best, happy + dfs(cnt, new_rem))
                cnt[r] += 1
            memo[key] = best
            return best

        return mod0 + dfs(cnt, 0)