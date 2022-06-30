// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = ((right-left)//2)+left
        
        while not nums[left] <= nums[mid] <= nums[right]:
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
                left = left + 1
            mid =((right-left)//2)+left
        return nums[left]