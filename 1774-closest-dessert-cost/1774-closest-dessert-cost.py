class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        ans = min(baseCosts)

        def dfs(i, curr):
            nonlocal ans

            if abs(curr - target) < abs(ans - target) or (
                abs(curr - target) == abs(ans - target) and curr < ans
            ):
                ans = curr

            if i == len(toppingCosts) or curr > target and curr - target > abs(ans - target):
                return

            dfs(i + 1, curr)
            dfs(i + 1, curr + toppingCosts[i])
            dfs(i + 1, curr + 2 * toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)

        return ans