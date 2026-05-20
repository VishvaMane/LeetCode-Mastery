class Trie:
    def __init__(self):
        self.children = [None, None]
        self.cnt = 0
    
    def insert(self, x: int) -> None:
        node = self
        for i in range(15, -1, -1):
            bit = (x >> i) & 1
            if not node.children[bit]:
                node.children[bit] = Trie()
            node = node.children[bit]
            node.cnt += 1
    
    def search(self, x: int, limit: int) -> int:
        node = self
        count = 0
        for i in range(15, -1, -1):
            if not node:
                return count
            x_bit = (x >> i) & 1
            limit_bit = (limit >> i) & 1
            
            if limit_bit == 1:
                if node.children[x_bit]:
                    count += node.children[x_bit].cnt
                node = node.children[x_bit ^ 1]
            else:
                node = node.children[x_bit]
        return count

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        ans = 0
        for num in nums:
            ans += trie.search(num, high + 1) - trie.search(num, low)
            trie.insert(num)
        return ans