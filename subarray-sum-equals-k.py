// https://leetcode.com/problems/subarray-sum-equals-k

from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sumsThusFar = {0: 1}
        result = 0
        tot = 0
        
        for num in nums:
            tot += num
            result += sumsThusFar.get(tot - k, 0)
            sumsThusFar[tot] = sumsThusFar.get(tot, 0) + 1
        
        return result
            