# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return
        
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            current_level = []
            levels = len(queue)
            
            for i in range(levels):
                curr = queue.popleft()
                current_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(current_level)
            
        return res
            
        
        