// https://leetcode.com/problems/jump-game-ii

from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        jumps = 0
        
        while left < right:
            if nums[left] + left >= right:
                right = left
                left = 0
                jumps += 1
            else:
                left += 1
        
        return jumps