'''
102. Binary Tree Level Order Traversal -

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
'''
'''
Approach -
Add the root to queue along with its level (1)
Add left and right to queue if exisits with level + 1
Create a res list(list), reusing queue here
add elements according to their heights
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [] 
        level = []
        queue.append((root,1)) # add the root and level/height
        level.append((root.val,1)) # add the value to a temp array with height
        while (queue):
            element = queue.pop(0) # get the first element
            root = element[0]
            height = element[1]
            if root.left != None:
                queue.append((root.left,height+1)) # increment height
                level.append((root.left.val,height+1))
            if root.right != None:
                queue.append((root.right,height+1))
                level.append((root.right.val,height+1))
        queue = [[] for i in range(level[len(level) - 1][1])] # create the res list
        for x in level:
            root = x[0]
            height = x[1]
            queue[height-1].append(root) # append to appropriate height
        return queue
'''
Runtime: 32 ms, faster than 82.40% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.8 MB, less than 25.69% of Python3 online submissions for Binary Tree Level Order Traversal.
Time - O(n), Space - O(n^2)
'''