# Q: Finding kth smallest element in BST

class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def kthSmallest(self, root:Treenode, k:int)->int:
        self.k = k
        self.res = None
        
        self.inOrder(None)
        return self.res
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.k -= 1
        if self.k==0:
            self.res = root.val
            return
        self.inOrder(root.right)