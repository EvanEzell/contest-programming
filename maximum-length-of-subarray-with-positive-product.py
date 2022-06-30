// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product

# dp(nums, i, product, maxLen)
# dp([1,-2,-3,4], 1, 1, 0)
#   dp([-2,-3,4], 2, 1, 1)
#     dp([-3,4], 3, 1, -2)


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        def maxLen(nums, start, end):
            
            negatives = 0
            leftNeg = rightNeg = None
            i = start
            while i < end:
                if nums[i] < 0:
                    if leftNeg is None:
                        leftNeg = i
                    rightNeg = i
                    negatives += 1
                i += 1
            
            if negatives % 2 == 0:
                return end - start
            
            return max(end - leftNeg - 1, rightNeg - start)
        
        result = start = i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
            else:
                result = max(result, maxLen(nums, start, i))
                start = i
                while start < len(nums) and nums[start] == 0:
                    start += 1
                i = start
        
        return max(result, maxLen(nums, start, i))
            
        
                
            
            
            