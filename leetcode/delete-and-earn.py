// https://leetcode.com/problems/delete-and-earn

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        prev2 = 0
        prev1 = 0
        prev_num = 0
        
        for num in sorted(set(nums)):
            if prev_num == num - 1:
                cur = max(prev1, prev2 + (count[num] * num))
            else:
                cur = max(prev1, prev2) + (count[num] * num)

            prev2, prev1 = prev1, cur
            prev_num = num
        
        return cur
            