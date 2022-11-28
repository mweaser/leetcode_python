# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        q = deque()
        q.append(root)
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                
                if curr.left and curr.right:
                    tmp = curr.left
                    curr.left = curr.right
                    curr.right = tmp
                    q.append(curr.left)
                    q.append(curr.right)

                elif curr.right and not curr.left:
                    q.append(curr.right)
                    curr.left = curr.right
                    curr.right = None        
                
                elif curr.left and not curr.right:
                    q.append(curr.left)
                    curr.right = curr.left
                    curr.left = None

            
                    
               
            
        return root
        