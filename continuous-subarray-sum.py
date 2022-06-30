// https://leetcode.com/problems/continuous-subarray-sum

# Brute force
# check all n^2 sub-arrays
# O(n^3) time, O(1) space

# Use prefix sum array, converts sum into O(1) operation
# O(n^2) time, O(n) space

# [23,2,4,6,7]
# [0,23,25,29,35,42]
#   { 5, 1, 5, 5, 0}
# tot: 23
# what number would make it a multiple of 6
# 1, 7, 13, 19, 25, 31, ...
# how do we get this?
# (23 % 6) = 5
# {5, 1, 5}



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        subtract = {0}
        windowSum = nums[0]
        prefixSum = 0
        for i in range(1,len(nums)):
            windowSum += nums[i]
            # print("window: " + str(nums[:i+1]))
            if i - 2 >= 0:
                prefixSum += nums[i-2]
                subtract.add(prefixSum % k)
            # print("subtract: " + str(subtract))
            if windowSum % k in subtract:
                return True
            # print()
        return False