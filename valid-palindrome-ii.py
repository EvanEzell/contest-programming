// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValid(i = 0, j = len(s) - 1, delete = False):
            
            while i <= j:
                if s[i] != s[j]:
                    if delete:
                        return False
                    else:
                        return isValid(i + 1, j, True) or isValid(i, j - 1, True)
                    
                i += 1
                j -= 1
                
            return True
    
        return isValid()