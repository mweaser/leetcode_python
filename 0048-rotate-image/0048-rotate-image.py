class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        res = []
        
        t = 0
        b = len(matrix)
        
        l = 0
        r = len(matrix[0]) -1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                top_left = matrix[top][l + i]
                
                #bottom_left into top_left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                #bottom_right into bottom_left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                #top_right into bottom_right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                #top_left tmp into top_right
                matrix[top + i][r] = top_left
            l += 1
            r -= 1
                        
                  


            
        