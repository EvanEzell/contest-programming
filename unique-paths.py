// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [1 for j in range(n)]
        cur = [0 for j in range(n)]
        
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if i + 1 < m:
                    cur[j] += prev[j]
                if j + 1 < n:
                    cur[j] += cur[j+1]
            prev = cur
            cur = [0 for j in range(n)]
        
        return prev[0]