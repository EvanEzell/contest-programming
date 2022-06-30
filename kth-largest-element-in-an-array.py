// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            def run(nums, k, left, right):
        
                start = left
                end = right

                pivot = left
                left += 1

                while left <= right:

                    if nums[left] <= nums[pivot]:
                        left += 1
                    elif nums[right] > nums[pivot]:
                        right -= 1
                    else:
                        nums[left], nums[right] = nums[right], nums[left]

                nums[right], nums[pivot] = nums[pivot], nums[right]
                pivot = right

                target = len(nums) - k

                if pivot == target:
                    return nums[target]
                elif pivot < target:
                    return run(nums, k, pivot + 1, end)
                else: # pivot > target
                    return run(nums, k, start, pivot - 1)

            return run(nums, k, left = 0, right = len(nums) - 1)