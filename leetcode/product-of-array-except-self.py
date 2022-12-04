// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]
        
        # prefix pass
        for i in range(len(nums)-1):
            result.append(result[-1] * nums[i])
        
        # postfix pass
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result