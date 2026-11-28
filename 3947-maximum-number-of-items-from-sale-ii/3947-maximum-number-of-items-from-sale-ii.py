class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_p = float('inf')

        for f, p in items:
            freq[f] += 1
            if p < min_p:
                min_p = p

        div_cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                total = 0
                for m in range(f, n + 1, f):
                    total += freq[m]
                div_cnt[f] = total - 1

        candidates = []
        limit_p = 2 * min_p
        for f, p in items:
            if p < limit_p and div_cnt[f] > 0:
                candidates.append((p, div_cnt[f]))

        candidates.sort()

        k = 0
        curr_cost = 0
        ans = budget // min_p

        for p, cnt in candidates:
            rem = budget - curr_cost
            if rem < p:
                break
            take = min(cnt, rem // p)
            curr_cost += take * p
            k += take
            ans = max(ans, 2 * k + (budget - curr_cost) // min_p)
            if take < cnt:
                break

        return ans