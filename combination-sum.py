// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combos = set()
        
        def backtrack(candidate = [], target = target):
            if target == 0:
                combos.add(tuple(sorted(candidate)))
                return
            if target < 0:
                return
            
            for num in candidates:
                candidate.append(num)
                backtrack(candidate, target - num)
                candidate.pop()
            
            return combos
        
        return backtrack()
        