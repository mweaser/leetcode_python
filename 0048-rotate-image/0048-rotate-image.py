class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        res = []
        
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        
        while left < right:
            curr = []
            for i in range(top, bottom):
                curr.append(matrix[i][left])
            # print("curr:", curr)
            left += 1
            curr.reverse()
            res.append(curr)
            
        for i in range(len(matrix)):
            matrix[i] = res[i]


            
        