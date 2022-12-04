// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.solution = (0, 0)
        self.max_len = 0
        def expand(center, between_chars=True):
            left = center
            right = center + between_chars
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > self.max_len:
                        self.solution = (left, right)
                        self.max_len = right - left + 1
                    left -= 1
                    right += 1
                else:
                    break
        
        for center in range(len(s)):
            expand(center, False)
            expand(center, True)
        
        left, right = self.solution
        return s[left:right+1]