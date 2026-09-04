class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        res = list(num)
        mutating = False
        
        for i in range(len(res)):
            d = int(res[i])
            if change[d] > d:
                res[i] = str(change[d])
                mutating = True
            elif change[d] < d:
                if mutating:
                    break
                    
        return "".join(res)