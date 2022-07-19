# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def sumHelper(self, currentNode, pathSum):
        
        if not currentNode:
            return 0
     
        pathSum = (pathSum * 10) + currentNode.val
        
        if not currentNode.left and not currentNode.right:
            return pathSum
        
        return self.sumHelper(currentNode.left, pathSum) + self.sumHelper(currentNode.right, pathSum)
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
            return self.sumHelper(root, 0)   



            
                