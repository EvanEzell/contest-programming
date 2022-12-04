// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        while i <= j:
            a = s[i].lower()
            b = s[j].lower()
            
            if not a.isalnum():
                i += 1
                continue
            if not b.isalnum():
                j -= 1
                continue
            
            if a != b:
                return False
            i += 1
            j -= 1
        
        return True