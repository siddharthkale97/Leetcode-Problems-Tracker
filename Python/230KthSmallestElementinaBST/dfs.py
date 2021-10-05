'''
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def dfs(node):
            if node!=None:
                if node.left!=None:
                    dfs(node.left)
                nums.append(node.val)
                if node.right!=None:
                    dfs(node.right)
        dfs(root)
        # print(nums)
        return nums[k-1]
'''
Runtime: 73 ms, faster than 21.43% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.2 MB, less than 15.87% of Python3 online submissions for Kth Smallest Element in a BST.
'''