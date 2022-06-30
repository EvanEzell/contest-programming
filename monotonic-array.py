// https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = decreasing = True
        for i in range(1,len(nums)):
            if increasing and nums[i-1] > nums[i]:
                increasing = False
            if decreasing and nums[i-1] < nums[i]:
                decreasing = False
        
        return increasing or decreasing