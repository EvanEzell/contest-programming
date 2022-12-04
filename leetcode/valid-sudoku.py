// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # validate rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        
        # validate cols
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        # validate boxes
        for row_offset in range(0,7,3):
            for col_offset in range(0,7,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row_offset+i][col_offset+j] != '.':
                            if board[row_offset+i][col_offset+j] in seen:
                                return False
                            else:
                                seen.add(board[row_offset+i][col_offset+j])
        
        return True  