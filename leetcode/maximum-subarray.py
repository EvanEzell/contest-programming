// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = float('-inf')
        maxThusFar = float('-inf')

        for num in nums:
            cur = max(cur+num,num)
            maxThusFar = max(maxThusFar,cur)
        
        return maxThusFar