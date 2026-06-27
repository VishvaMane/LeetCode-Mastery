from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        @lru_cache(None)
        def dfs(players):
            m = len(players)
            pos = {x: i for i, x in enumerate(players)}
            if pos[firstPlayer] + pos[secondPlayer] == m - 1:
                return (1, 1)

            pairs = m // 2
            nxt = set()

            def backtrack(i, cur):
                if i == pairs:
                    if m & 1:
                        cur.append(players[pairs])
                    nxt.add(tuple(sorted(cur)))
                    if m & 1:
                        cur.pop()
                    return

                a = players[i]
                b = players[m - 1 - i]

                if a == firstPlayer or a == secondPlayer:
                    cur.append(a)
                    backtrack(i + 1, cur)
                    cur.pop()
                elif b == firstPlayer or b == secondPlayer:
                    cur.append(b)
                    backtrack(i + 1, cur)
                    cur.pop()
                else:
                    cur.append(a)
                    backtrack(i + 1, cur)
                    cur.pop()
                    cur.append(b)
                    backtrack(i + 1, cur)
                    cur.pop()

            backtrack(0, [])

            mn = 10
            mx = 0
            for state in nxt:
                e, l = dfs(state)
                mn = min(mn, e + 1)
                mx = max(mx, l + 1)
            return (mn, mx)

        return list(dfs(tuple(range(1, n + 1))))