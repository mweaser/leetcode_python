# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return
        
        res = []
        q = deque([root])
        
        while q:
            c = []
            for _ in range(len(q)):
                n = q.popleft()
                res.append(n.val)
                
                if n.left:
                    q.append(n.left)
                    
                if n.right:
                    q.append(n.right)
        
        res.sort()
        return res[k-1]
                
        
        