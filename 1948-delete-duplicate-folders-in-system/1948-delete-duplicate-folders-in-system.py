import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = TrieNode()
        for path in paths:
            curr = root
            for folder in path:
                curr = curr.children[folder]
                
        serial_nodes = collections.defaultdict(list)
        
        def serialize(node):
            if not node.children:
                return ()
            
            sub_structure = []
            for name in sorted(node.children.keys()):
                child = node.children[name]
                sub_structure.append((name, serialize(child)))
                
            serial = tuple(sub_structure)
            serial_nodes[serial].append(node)
            return serial
            
        serialize(root)
        
        for nodes in serial_nodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True
                    
        ans = []
        
        def collect(node, path):
            for name, child in node.children.items():
                if not child.deleted:
                    ans.append(path + [name])
                    collect(child, path + [name])
                    
        collect(root, [])
        return ans