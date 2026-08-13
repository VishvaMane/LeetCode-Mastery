class Solution:
    def canMerge(self, trees: list['TreeNode']) -> 'TreeNode' | None:
        roots = {tree.val: tree for tree in trees}
        leaves = set()
        
        for tree in trees:
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
                
        main_root = None
        for tree in trees:
            if tree.val not in leaves:
                main_root = tree
                break
                
        if not main_root:
            return None
            
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
                
            if not node.left and not node.right and node.val in roots and node.val != main_root.val:
                node.left = roots[node.val].left
                node.right = roots[node.val].right
                del roots[node.val]
                
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
            
        del roots[main_root.val]
        
        if dfs(main_root, float('-inf'), float('inf')) and not roots:
            return main_root
        return None