class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26
        stack = [(0, 0, -1)]

        while stack:
            u, state, prev = stack.pop()
            c = ord(s[u]) - 97
            if state == 0:
                old = last_seen[c]
                if old != -1:
                    new_parent[u] = old
                last_seen[c] = u
                stack.append((u, 1, old))
                for v in adj[u]:
                    stack.append((v, 0, -1))
            else:
                last_seen[c] = prev

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        order = [0]
        for u in order:
            order.extend(new_adj[u])

        ans = [1] * n
        for u in reversed(order):
            if u != 0:
                ans[new_parent[u]] += ans[u]

        return ans