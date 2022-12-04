// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[right]: # in sorted part
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # in unsorted part
                if nums[mid] >= nums[left]:
                    if nums[left] <= target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] <= target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return -1
        
        
        