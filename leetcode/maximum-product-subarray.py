// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        globalMax = float('-inf')
        
        localMax = 1
        localMin = 1
        
        for num in nums:
            curProd = localMax * num
            localMax = max(num, curProd, localMin * num)
            localMin = min(num, curProd, localMin * num)
            
            globalMax = max(globalMax, localMax)
            
        return globalMax