// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        
        def neighbors(cell):
            i, j = cell
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            
            result = []
            for x, y in dirs:
                if ((i+x >= 0 and i+x < len(board)) and 
                    (j+y >= 0 and j+y < len(board[0]))):
                    result.append((i+x,j+y))
            return result
        
        def dfs(cell, word):
            i, j = cell
            if board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True
            
            visited.add(cell)
            
            word = word[1:]
            for neighbor in neighbors(cell):
                if neighbor not in visited and dfs(neighbor, word):
                    return True
            visited.remove(cell)
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = (i,j)
                visited = set()
                if dfs(cell, word):
                    return True
        return False