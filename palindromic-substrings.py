// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        self.count = 0
        def expand(center, between_chars = True):
            left = center
            right = center + between_chars
            
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                    
                self.count += 1
                left -= 1
                right += 1
        
        for center in range(len(s)):
            expand(center, True)
            expand(center, False)
        
        return self.count