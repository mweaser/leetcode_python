from collections import *

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                currNode = q.popleft()
                if not currNode.left and not currNode.right:
                    return depth
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        return -1