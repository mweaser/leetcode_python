# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            curr_level = []
            
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            res.append(curr_level)
        
        return len(res)
        
        