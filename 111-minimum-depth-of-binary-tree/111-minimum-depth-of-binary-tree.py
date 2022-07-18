# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        minimumDepth = 0
        
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        
        while queue:
            minimumDepth += 1
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                
                if currentNode.left is None and currentNode.right is None:
                    return minimumDepth
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        
        