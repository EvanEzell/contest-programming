// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        match = {')': '(',
                 '}': '{',
                 ']': '['}
        
        stack = []
        for char in s:
            if char in match:
                if stack and stack[-1] == match[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack