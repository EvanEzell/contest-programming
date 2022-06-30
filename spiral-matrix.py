// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def spiralOuter(left, right, top, bottom):
            
            result = []

            j = left
            while j < right:
                result.append(matrix[top][j])
                j += 1

            i = top
            while i < bottom:
                result.append(matrix[i][right])
                i += 1

            j = right
            while j > left:
                result.append(matrix[bottom][j])
                j -= 1

            i = bottom
            while i > top:
                result.append(matrix[i][left])
                i -= 1
            
            return result
        
        result = []
        
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
            
        while left < right and top < bottom:
            result.extend(spiralOuter(left, right, top, bottom))
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        for i in range(top, bottom+1):
            for j in range(left, right+1):
                result.append(matrix[i][j])
        
        return result

        
        