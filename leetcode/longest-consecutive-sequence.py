// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        bag = set(nums)
        maxThusFar = float('-inf') # stores maximum consecutive nums thus far
        
        while bag:
            high = low = bag.pop() # stores high and low of current sequence
            cur = 1 # stores current number of consecutive nums

            # check for new low
            while low - 1 in bag:
                cur += 1
                low -= 1
                bag.remove(low)
            
            # check for new high
            while high + 1 in bag:
                cur += 1
                high += 1
                bag.remove(high)
            
            maxThusFar = max(maxThusFar, cur)
        
        return maxThusFar