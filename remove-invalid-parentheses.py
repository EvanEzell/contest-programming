// https://leetcode.com/problems/remove-invalid-parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def countInvalid(s):
            
            left = 0
            right = 0
            
            for char in s:
                if char == "(":
                    left += 1
                elif char == ")":
                    if left:
                        left -= 1
                    else:
                        right += 1
                
            return left, right
    
        def recurse(prev, cur, count, left, right, solutions):
            
            if not cur:
                if count == 0:
                    solutions.add(prev + cur)
                return
            
            # removed more than min amount of parens or can't make valid
            if left < 0 or right < 0 or count < 0:
                return
            
            char = cur[0]
            if char == "(":
                recurse(prev, cur[1:], count, left - 1, right, solutions)
                recurse(prev + cur[0], cur[1:], count + 1, left, right, solutions)
            elif char == ")":
                recurse(prev, cur[1:], count, left, right - 1, solutions)
                recurse(prev + cur[0], cur[1:], count - 1, left, right, solutions)
            else: # not a paren
                recurse(prev + cur[0], cur[1:], count, left, right, solutions)

            return solutions
        
        left, right = countInvalid(s)
        return recurse("", s, 0, left, right, set())
            
            
        
                    