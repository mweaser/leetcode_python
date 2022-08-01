# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        count = 0
        
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                currentNode = queue.popleft()
                count += 1
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        
        return count
        