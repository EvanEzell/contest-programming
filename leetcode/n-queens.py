// https://leetcode.com/problems/n-queens

class Solution:
    def __init__(self):
        self.solutions = []
        self.current = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def translateBoard():
            
            board = []
            
            for column in self.current:
                row = ""
                for i in range(n):
                    row += "Q" if i == column else "."
                board.append(row)
            return board
        
        def generateCandidates():
            
            def isValid(candidate):
                
                for row in range(len(self.current)):
                    difference = len(self.current) - row
                    if (self.current[row] == candidate - difference or
                        self.current[row] == candidate + difference or
                        self.current[row] == candidate):
                        return False
                return True
                        
            if not self.current:
                return list(range(n))
            
            candidates = []
            for candidate in range(n):
                if isValid(candidate):
                    candidates.append(candidate)
            return candidates
                    
        def backtrack():
            
            # is_a_solution(columns), if it is append it to solutions
            if len(self.current) == n:
                self.solutions.append(translateBoard())
                return
            
            # generate possible candidates
            for candidate in generateCandidates():
                self.current.append(candidate)
                backtrack()
                self.current.pop()
        
        backtrack()
        return self.solutions