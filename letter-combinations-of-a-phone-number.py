// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        
        letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        combos = []
        
        def backtrack(i = 0, combo = ""):
            
            if i == len(digits):
                combos.append(combo)
                return
            
            for letter in letters[int(digits[i])]:
                backtrack(i + 1, combo + letter)

        if not digits:
            return []
        
        backtrack()
        return combos