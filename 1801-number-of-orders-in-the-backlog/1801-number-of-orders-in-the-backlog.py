from heapq import heappush, heappop

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        MOD = 10**9 + 7
        buy = []
        sell = []

        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0 and sell and sell[0][0] <= price:
                    sp, sa = heappop(sell)
                    matched = min(amount, sa)
                    amount -= matched
                    sa -= matched
                    if sa > 0:
                        heappush(sell, (sp, sa))
                        break
                if amount > 0:
                    heappush(buy, (-price, amount))
            else:
                while amount > 0 and buy and -buy[0][0] >= price:
                    bp, ba = heappop(buy)
                    bp = -bp
                    matched = min(amount, ba)
                    amount -= matched
                    ba -= matched
                    if ba > 0:
                        heappush(buy, (-bp, ba))
                        break
                if amount > 0:
                    heappush(sell, (price, amount))

        ans = sum(a for _, a in buy) + sum(a for _, a in sell)
        return ans % MOD