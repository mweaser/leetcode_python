import numpy as np

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        final = []
        
        while len(matrix) > 0:
        
            top = matrix.pop(0)
            final.extend(top)
            
            right = []
            for i in range(len(matrix)):
                if len(matrix[i]) == 0:
                    break
                right.append(matrix[i].pop(-1))
            final.extend(right)
            
            if len(matrix) == 0:
                break
                
            bottom = (matrix.pop(len(matrix)-1)) 
            bottom.reverse()
            final.extend(bottom)
            
            left = [] 
            for i in reversed(range(len(matrix))):
                if len(matrix[i]) == 0:
                    break
                left.append(matrix[i].pop(0))
            final.extend(left)
            
        return final
        
      

    