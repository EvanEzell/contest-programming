// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        
        nrows, ncols = len(heights), len(heights[0])
        
        def neighbors(cell):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            
            i, j = cell
            result = []
            for x, y in directions:
                if ((i+x >= 0 and i+x < nrows) and
                    (j+y >= 0 and j+y < ncols)):
                    result.append((i+x,j+y))
            return result

        def dfs(cell, visited):
            if cell in visited:
                return
            
            visited.add(cell)
            i, j = cell
            for x, y in neighbors(cell):
                if heights[i][j] <= heights[x][y]:
                    dfs((x,y), visited)
        
        for j in range(ncols):
            dfs((0,j), pacific)
            dfs((nrows-1,j), atlantic)
        for i in range(nrows):
            dfs((i,0), pacific)
            dfs((i,ncols-1), atlantic)
        
        return pacific & atlantic