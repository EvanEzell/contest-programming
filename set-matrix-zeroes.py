// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
                    
        for i in zero_row:
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
        for j in zero_col:
            for row in range(len(matrix)):
                matrix[row][j] = 0