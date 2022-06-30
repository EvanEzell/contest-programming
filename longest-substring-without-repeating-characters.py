// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = right = 0
        maxThusFar = 0
        
        while right < len(s):
            if s[right] in window:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                left += 1
                
            window.add(s[right])
            right += 1
            maxThusFar = max(maxThusFar, len(window))
            
        return maxThusFar