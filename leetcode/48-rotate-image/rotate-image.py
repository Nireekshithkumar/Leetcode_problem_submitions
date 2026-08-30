class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        res=[[0]*c for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                res[j][c-i-1]=matrix[i][j]
        
        for i in range(r):
            for j in range(c):
                matrix[i][j]=res[i][j]



            
            