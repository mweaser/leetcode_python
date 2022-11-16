

import numpy as np
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        directions = [[-1,0],[1,0], [0,-1], [0,1]]
        
        rows = []
        cols = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows:
                    matrix[i][j] = 0
                if j in cols:
                    matrix[i][j] = 0
                
                    
        print(rows)
        print(cols)
        
        print(np.matrix(matrix))
            
                        
                    
                
                
                
                
# #         -1,0 1,0 0,-1 0,1

# matrix[i-1][j] = 0 and (i-1 in range(len(matrix)) and j in range(len(matrix[i])))
                    # matrix[i+1][j] = 0 and (i+1 in range(len(matrix)) and j in range(len(matrix[i])))
                    # matrix[i][j-1] = 0 and (i in range(len(matrix)) and j in range(len(matrix[i])))
                    # matrix[i][j+1] = 0 and (i in range(len(matrix)) and j in range(len(matrix[i])))