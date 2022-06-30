// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            n = len(matrix)
            start = 0
            for i in range(n):
                for j in range(start,n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                start += 1
        
        def reflectVertically(matrix):
        
            for row in range(len(matrix)):
                left = 0
                right = len(matrix) - 1
            
                while left < right:
                    matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                    left += 1
                    right -= 1
        
        transpose(matrix)
        reflectVertically(matrix)