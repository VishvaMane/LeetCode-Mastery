from typing import List
from collections import defaultdict

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)

        children = defaultdict(list)
        for i, p in enumerate(prevRoom):
            if p != -1:
                children[p].append(i)

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        size = [1] * n
        ways = [1] * n

        post_order = []
        stack = [(0, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                post_order.append(node)
                continue
            stack.append((node, True))
            for c in children[node]:
                stack.append((c, False))

        for node in post_order:
            total_children_size = 0
            ways_node = 1
            for c in children[node]:
                total_children_size += size[c]
                ways_node = ways_node * ways[c] % MOD
                ways_node = ways_node * inv_fact[size[c]] % MOD
            ways_node = ways_node * fact[total_children_size] % MOD

            size[node] = total_children_size + 1
            ways[node] = ways_node

        return ways[0] % MOD


if __name__ == "__main__":
    sol = Solution()
    print(sol.waysToBuildRooms([-1, 0, 1]))         # Expected: 1
    print(sol.waysToBuildRooms([-1, 0, 0, 1, 2]))    # Expected: 6