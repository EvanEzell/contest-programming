// https://leetcode.com/problems/island-perimeter

# compute inner rectangle perimeter

# compute outer L, middle lines perimeter

# compute border perimeter

# O(m * n) time
# O(1) space

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
                
        def dfs(i,j, visited = set()):
            
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            
            perimeter = 0
            for x,y in directions:
                if i+x >= 0 and i+x < len(grid):
                    if j+y >= 0 and j+y < len(grid[0]):
                        if not grid[i+x][j+y]:
                            perimeter += 1
                        else:
                            perimeter += dfs(i+x,j+y,visited)
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
                    