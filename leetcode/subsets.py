// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = [[]]
        def backtrack():
            if not nums:
                return

            num = nums.pop()
            next_results = []
            for result in results:
                cur = result.copy()
                cur.append(num)
                next_results.append(cur)
            results.extend(next_results)
            backtrack()
            return results
        
        return backtrack()