// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev2, prev1 = 0, 1
        
        for _ in range(n):
            cur = prev2 + prev1
            prev2, prev1 = prev1, cur
        
        return cur
            