import numpy as np

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        final = []
        
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        
        while top < bottom and left < right:
            #top
            for i in range(left, right):
                final.append(matrix[top][i])
            top += 1
            
            #right
            for i in range(top, bottom):
                final.append(matrix[i][right-1])
            right -= 1
            
            if not (top < bottom and left < right):
                break
            
            #bottom
            for i in range(right - 1, left - 1, -1):
                final.append(matrix[bottom - 1][i])
            bottom -= 1
            
            #left
            for i in range(bottom - 1, top - 1, -1):
                final.append(matrix[i][left])
            left += 1
        
        return final