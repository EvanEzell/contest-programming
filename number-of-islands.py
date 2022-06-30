// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def neighbors(cell):
            i, j = cell
            
            dirs = [(-1,0), # left
                    (1,0),  # right
                    (0,-1), # up
                    (0,1)]  # down
            
            result = []
            for x, y in dirs:
                # in bounds and land
                if ((i+x >= 0 and i+x < len(grid)) and 
                    (j+y >= 0 and j+y < len(grid[0])) and
                    int(grid[i+x][j+y])):
                    result.append((i+x,j+y))
            return result
            
        def dfs(cell):
            
            visited.add(cell)
            
            for neighbor in neighbors(cell):
                if neighbor not in visited:
                    dfs(neighbor)
        
        islands = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = (i,j)
                if cell not in visited and int(grid[i][j]):
                    dfs(cell)
                    islands += 1
        
        return islands