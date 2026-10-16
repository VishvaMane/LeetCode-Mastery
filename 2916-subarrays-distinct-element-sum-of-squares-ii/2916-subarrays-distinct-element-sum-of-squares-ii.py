class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        def update_bit(bit, idx, val):
            while idx < len(bit):
                bit[idx] = (bit[idx] + val) % MOD
                idx += idx & (-idx)
                
        def query_bit(bit, idx):
            s = 0
            while idx > 0:
                s = (s + bit[idx]) % MOD
                idx -= idx & (-idx)
            return s
            
        def range_add(L, R, val):
            update_bit(bit1, L, val)
            update_bit(bit1, R + 1, -val)
            
            update_bit(bit2, L, val * (L - 1))
            update_bit(bit2, R + 1, -val * R)
            
        def prefix_sum(idx):
            return (idx * query_bit(bit1, idx) - query_bit(bit2, idx)) % MOD
            
        def range_sum(L, R):
            return (prefix_sum(R) - prefix_sum(L - 1)) % MOD

        last_occurrence = [-1] * 100001
        ans = 0
        current_sum = 0
        
        for i in range(n):
            val = nums[i]
            prev_idx = last_occurrence[val]
            last_occurrence[val] = i
            
            L = prev_idx + 2
            R = i + 1
            
            sum_vals = range_sum(L, R)
            
            current_sum = (current_sum + 2 * sum_vals + (i - prev_idx)) % MOD
            ans = (ans + current_sum) % MOD
            
            range_add(L, R, 1)
            
        return ans