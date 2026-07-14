from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        MOD1, BASE1 = (1 << 61) - 1, 131
        MOD2, BASE2 = (1 << 31) - 1, 137

        def get_hashes(path, length):
            power1 = pow(BASE1, length - 1, MOD1)
            power2 = pow(BASE2, length - 1, MOD2)

            h1 = h2 = 0
            for i in range(length):
                h1 = (h1 * BASE1 + path[i]) % MOD1
                h2 = (h2 * BASE2 + path[i]) % MOD2

            hashes = {(h1, h2)}

            for i in range(length, len(path)):
                h1 = ((h1 - path[i - length] * power1) * BASE1 + path[i]) % MOD1
                h2 = ((h2 - path[i - length] * power2) * BASE2 + path[i]) % MOD2
                hashes.add((h1, h2))

            return hashes

        def search(length: int) -> bool:
            if length == 0:
                return True

            common_hashes = None

            for path in paths:
                if len(path) < length:
                    return False

                current_hashes = get_hashes(path, length)

                if common_hashes is None:
                    common_hashes = current_hashes
                else:
                    common_hashes &= current_hashes
                    if not common_hashes:
                        return False

            return bool(common_hashes)

        left, right = 0, min(len(p) for p in paths)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if search(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans