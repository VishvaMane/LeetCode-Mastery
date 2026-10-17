class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        arr = [(digit_sum(x), x, i) for i, x in enumerate(nums)]
        arr.sort()

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or arr[i][2] == i:
                continue
            
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1
            
            if cycle_size > 0:
                swaps += cycle_size - 1
                
        return swaps