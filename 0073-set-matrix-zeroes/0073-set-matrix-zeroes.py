

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
                
         
                    
        