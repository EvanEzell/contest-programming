// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        minSum, maxSum = float('inf'), float('-inf')
        curMin = curMax = 0
        
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                curMin = min(curMin + nums[i], nums[i])
                minSum = min(minSum, curMin)
            
            curMax = max(curMax + nums[i], nums[i])
            maxSum = max(maxSum, curMax)
        
        return max(maxSum, sum(nums) - minSum)