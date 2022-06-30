// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        total = numbers[left] + numbers[right]
        
        while total != target:
            if total < target:
                left += 1
            if total > target:
                right -= 1
            total = numbers[left] + numbers[right]
        return [left + 1, right + 1]