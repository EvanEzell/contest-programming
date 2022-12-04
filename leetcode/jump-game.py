// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastStep = len(nums) - 1
        lowestReachingStep = len(nums) - 1 # lowest step that can reach last step
        
        for step in range(lastStep,-1,-1):
            if step + nums[step] >= lowestReachingStep:
                lowestReachingStep = step
        
        return lowestReachingStep == 0