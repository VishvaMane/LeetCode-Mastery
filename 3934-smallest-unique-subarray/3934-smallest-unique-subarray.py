class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        length = [0]
        link = [-1]
        nxt = [{}]
        cnt = [0]
        last = 0

        for c in nums:
            cur = len(length)
            length.append(length[last] + 1)
            link.append(0)
            nxt.append({})
            cnt.append(1)

            p = last
            while p != -1 and c not in nxt[p]:
                nxt[p][c] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][c]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(length)
                    length.append(length[p] + 1)
                    link.append(link[q])
                    nxt.append(nxt[q].copy())
                    cnt.append(0)
                    while p != -1 and nxt[p].get(c) == q:
                        nxt[p][c] = clone
                        p = link[p]
                    link[q] = link[cur] = clone

            last = cur

        bucket = [0] * (n + 1)
        for l in length:
            bucket[l] += 1
        for i in range(1, n + 1):
            bucket[i] += bucket[i - 1]

        m = len(length)
        order = [0] * m
        for i in range(m - 1, -1, -1):
            l = length[i]
            bucket[l] -= 1
            order[bucket[l]] = i

        for i in range(m - 1, 0, -1):
            v = order[i]
            cnt[link[v]] += cnt[v]

        ans = n
        for v in range(1, m):
            if cnt[v] == 1:
                cand = length[link[v]] + 1
                if cand < ans:
                    ans = cand

        return ans