class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def preorder(root,l):
    if not root:
        l.append(float("-inf"))
        return
    l.append(root.val)
    preorder(root.left,l)
    preorder(root.right,l)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        l1 = []
        preorder(p,l1)
        l2 = []
        preorder(q,l2)
        if l1==l2:
            return True
        else:
            return False