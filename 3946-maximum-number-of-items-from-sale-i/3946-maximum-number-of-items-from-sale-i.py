class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        div_cnt = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f]:
                for m in range(f, max_f + 1, f):
                    div_cnt[f] += freq[m]

        min_p = min(p for _, p in items)
        dp = [0] * (budget + 1)

        for f, p in items:
            if p > budget:
                continue
            v = div_cnt[f]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + v > dp[b]:
                    dp[b] = dp[b - p] + v

        return max(dp[b] + (budget - b) // min_p for b in range(budget + 1))