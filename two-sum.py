// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # only works if there is exactly one solution
        # otherwise num index could get overwritten with new index
        num_map = {num: index for index, num in enumerate(nums)}
        
        for i, addend in enumerate(nums):
            augend = target - addend
            if augend in num_map and num_map[augend] != i:
                return [num_map[augend], i]