// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        cur = nums[0]
        
        for i in range(len(nums)-1):
            cur = max(prev2 + nums[i], prev1)
            prev2, prev1 = prev1, cur
        
        solution1 = cur
        
        prev2 = prev1 = 0
        for i in range(1, len(nums)):
            cur = max(prev2 + nums[i], prev1)
            prev2, prev1 = prev1, cur
        
        return max(cur, solution1)