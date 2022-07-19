# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSumRecursive(self, currentNode, requiredSum, currentPath, allPaths):
        
        if currentNode is None:
            return
        
        currentPath.append(currentNode.val)
        
        if currentNode.val == requiredSum and currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
            
        else:
            
            self.pathSumRecursive(currentNode.left, requiredSum - currentNode.val, currentPath, allPaths)
            
            self.pathSumRecursive(currentNode.right, requiredSum - currentNode.val, currentPath, allPaths)
            
        currentPath.pop()
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        allPaths = []
        
        if not root:
            return
        
        self.pathSumRecursive(root, targetSum, [], allPaths)
        
        return allPaths
        
    
    
