// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev2 = prev1 = 0
        
        for num in nums:
            cur = max(num + prev2, prev1)
            prev2, prev1 = prev1, cur
        
        return cur