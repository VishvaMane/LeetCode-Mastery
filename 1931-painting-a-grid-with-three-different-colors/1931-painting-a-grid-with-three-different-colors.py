class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        def get_valid_patterns(height):
            patterns = []
            
            def backtrack(idx, current_pattern):
                if idx == height:
                    patterns.append(tuple(current_pattern))
                    return
                
                for color in range(3):
                    if idx == 0 or current_pattern[idx - 1] != color:
                        current_pattern.append(color)
                        backtrack(idx + 1, current_pattern)
                        current_pattern.pop()
            
            backtrack(0, [])
            return patterns
        
        def is_compatible(pattern1, pattern2):
            for i in range(len(pattern1)):
                if pattern1[i] == pattern2[i]:
                    return False
            return True
        
        valid_patterns = get_valid_patterns(m)
        num_patterns = len(valid_patterns)
        
        compatible = [[False] * num_patterns for _ in range(num_patterns)]
        for i in range(num_patterns):
            for j in range(num_patterns):
                compatible[i][j] = is_compatible(valid_patterns[i], valid_patterns[j])
        
        dp = [1] * num_patterns
        
        for col in range(1, n):
            new_dp = [0] * num_patterns
            
            for curr_pattern in range(num_patterns):
                for prev_pattern in range(num_patterns):
                    if compatible[prev_pattern][curr_pattern]:
                        new_dp[curr_pattern] = (
                            new_dp[curr_pattern] + dp[prev_pattern]
                        ) % MOD
            
            dp = new_dp
        
        return sum(dp) % MOD