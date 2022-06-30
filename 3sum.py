// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        
        nums.sort()
        for i, num in enumerate(nums):
            if i and nums[i-1] == num:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    triplets.append([num, nums[left], nums[right]])
                    prev = nums[left]
                    while left < len(nums) and nums[left] == prev:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return triplets