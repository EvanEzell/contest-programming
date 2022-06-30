// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        total //= 2
        
        prev = [False for target in range(total+1)]
        cur = prev.copy()
        prev[0] = True
        if nums[0] < len(prev):
            prev[nums[0]] = True
        
        for i in range(1,len(nums)):
            for target in range(total+1):
                cur[target] = ((target >= nums[i] and prev[target-nums[i]]) or
                               prev[target])
            if cur[-1]:
                return True
            prev, cur = cur, prev
        
        return False