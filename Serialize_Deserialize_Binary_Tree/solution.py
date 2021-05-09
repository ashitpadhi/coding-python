# Q: Serialize and deserialize Binary Tree
class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Codec:
    def serializes(self, root):
        # convert a Binary tree into 1#2#X#X#3#4#X#X#5
        if (root is None):
            return "X#"
        leftserialized = self.serializes(root.left)
        rightserialized = self.serializes(root.right)
        
        return str(root.val)+"#"+leftserialized+rightserialized
        
        
    def deserialize(self, root):
        # convert 1#2#X#X#3#4#X#X#5 into a Binary tree
        
        def dfs():
            val = next(data)
            if val == "X":
                return None
            node = Treenode(int(val))
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        data = iter(data.split("#"))
        return dfs()