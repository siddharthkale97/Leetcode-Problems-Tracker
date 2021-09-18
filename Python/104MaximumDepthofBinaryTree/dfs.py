class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def d(root):
    if root==None:
        return 0
    return 1 + max(d(root.left), d(root.right))

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return d(root)