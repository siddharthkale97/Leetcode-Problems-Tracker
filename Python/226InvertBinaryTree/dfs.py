'''
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        def traversal(node):
            if node!=None:
                #print(node)
                r = node.right
                node.right = node.left
                node.left = r
                
                if node.left!=None:
                    traversal(node.left)
                if node.right!=None:
                    traversal(node.right)
        traversal(root)                    
        return root