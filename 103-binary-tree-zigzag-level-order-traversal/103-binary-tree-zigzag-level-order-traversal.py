# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        isOddLevel = True
        
        result = deque()
        
        if not root:
            return
        
        queue = deque()
        queue.append(root)
        
        while queue:
            currentLevel = deque()
            levelSize = len(queue)
            
            for i in range(levelSize):
                currentNode = queue.popleft()
                if isOddLevel:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            isOddLevel = not isOddLevel
            result.append(currentLevel)
        return result
        