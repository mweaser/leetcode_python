import numpy as np

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        final = []
        
        while len(matrix) > 0:
        
            top = matrix.pop(0)
            #print(top)
            
            final.extend(top)
            
            right = []
        
            for i in range(len(matrix)):
                if len(matrix[i]) == 0:
                    break
                right.append(matrix[i].pop(-1))
                
            print("right:",right)
         
            final.extend(right)
            
            if len(matrix) == 0:
                break
                
            bottom = (matrix.pop(len(matrix)-1)) 
            bottom.reverse()
            
            print("bottom:", bottom)
       
            final.extend(bottom)
            
            print("matrix:", matrix)
            
            left = []
            
            for i in reversed(range(len(matrix))):
                if len(matrix[i]) == 0:
                    break
                left.append(matrix[i].pop(0))

            print("left:",left)
  
            final.extend(left)
            
            print("matrix:", matrix)
            
        return final
        
      

    