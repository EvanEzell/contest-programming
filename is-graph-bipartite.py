// https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        green = set()
        red = set()
        colorSets = (green, red)
        
        def dfs(node, color = True):
            
            if node in visited:
                return node in colorSets[color]
            
            visited.add(node)
            colorSets[color].add(node)
            
            for neighbor in graph[node]:
                if not dfs(neighbor, not color):
                    return False
                
            return True
        
        for node in range(len(graph)):
            if not node in visited:
                if not dfs(node):
                    return False
            
        return True