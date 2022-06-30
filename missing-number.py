// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]-1:
                return i
        return len(nums) if nums[0] == 0 else 0