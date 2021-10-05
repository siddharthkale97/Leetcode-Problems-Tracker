'''
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = res = root
        
        if p.val>q.val:
            a = p
            p = q
            q = a
        
        cond = True
        while(cond):
            if curr == None:
                cond = False
                break
            if p.val < curr.val < q.val:
                res = curr
                break
            elif p.val == curr.val or q.val == curr.val:
                res = curr
                break
            elif q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val:
                curr = curr.right
        
        return res
'''
Runtime: 76 ms, faster than 78.98% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.2 MB, less than 45.19% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''