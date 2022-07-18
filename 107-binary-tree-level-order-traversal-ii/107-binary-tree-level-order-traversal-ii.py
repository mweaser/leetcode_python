# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        queue = deque()
        
        if not root:
            return
        
        queue.append(root)
        
        while queue:
            currentLevel = []
            levelSize = len(queue)
            
            for i in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)
                
            result.appendleft(currentLevel)
        return result
        