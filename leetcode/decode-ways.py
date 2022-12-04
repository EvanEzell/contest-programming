// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def isValid(code):
            if code[0] == '0':
                return False
            
            if len(code) == 2:
                return int(code) >= 0 and int(code) <= 26
            
            return True
        
        post1 = 1
        post2 = 0
        
        for i in range(len(s)-1, -1, -1):
            cur = 0
            if isValid(s[i]):
                cur += post1
            if i+2 <= len(s) and isValid(s[i:i+2]):
                cur += post2
            post2 = post1
            post1 = cur

        return cur
    