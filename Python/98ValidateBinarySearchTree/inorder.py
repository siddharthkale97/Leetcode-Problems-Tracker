# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, ARRAY):
    if root!=None:
        inorder(root.left, ARRAY)
        ARRAY.append(root.val)
        #print(root.val)
        inorder(root.right, ARRAY)
def ifsorted(l):
    a = float("-inf")
    for i in range(len(l)):
        if l[i]<=a:
            return False
        a = l[i]
    return True
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ARRAY = []
        if root==None:
            return True
        inorder(root, ARRAY)
        #print(ARRAY)
        return ifsorted(ARRAY)