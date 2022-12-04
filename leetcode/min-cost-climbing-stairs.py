// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev2, prev1 = 0, 0
        
        for c in cost:
            cur = min(prev2, prev1) + c
            prev2, prev1 = prev1, cur
        
        return min(prev2, prev1)