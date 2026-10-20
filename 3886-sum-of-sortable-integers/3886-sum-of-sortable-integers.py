class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        is_drop = [nums[i] > nums[i+1] for i in range(n - 1)]
        pref = [0] * n
        for i in range(n - 1):
            pref[i+1] = pref[i] + is_drop[i]
            
        def check(k):
            for i in range(n // k):
                s = i * k
                e = s + k
                internal_drops = pref[e-1] - pref[s]
                if internal_drops > 1:
                    return False
                wrap_drop = 1 if nums[e-1] > nums[s] else 0
                total_drops = internal_drops + wrap_drop
                if total_drops > 1:
                    return False
                
                if total_drops == 0 or (total_drops == 1 and wrap_drop == 1):
                    if nums[s:e] != sorted_nums[s:e]:
                        return False
                else:
                    drop_idx = is_drop.index(True, s, e-1)
                    if nums[drop_idx+1:e] + nums[s:drop_idx+1] != sorted_nums[s:e]:
                        return False
            return True

        ans = 0
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                if check(k):
                    ans += k
                k2 = n // k
                if k2 != k:
                    if check(k2):
                        ans += k2
        return ans