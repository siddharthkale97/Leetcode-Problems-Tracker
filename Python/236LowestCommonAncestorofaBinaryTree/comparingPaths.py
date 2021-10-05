'''
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
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
        
        path = []

        def dfs(node, target): 
            if node == None:
                return False
            if node.val == target:
                path.append(node)
                return True
            
            path.append(node)
            res1 = dfs(node.left, target)
            if res1 == True:
                return True
            res2 = dfs(node.right, target)
            if res2 == True:
                return True
            path.remove(node)
            return False
        path = []
        dfs(root, p.val)
        patha = list(path)
        
        path = []
        dfs(root, q.val)
        pathb = list(path)
        path = []
        
        prev = root
        j, i = 0, 0
        while( i < len(patha) and j < len(pathb)):
            if patha[i] == pathb[j]:
                prev = patha[i]
            i += 1
            j += 1
        return prev
        