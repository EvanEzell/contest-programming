// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        required = Counter(t)
        requirements = 0
        window = {key: 0 for key in required.keys()}
        
        minWindow = (None, None)
        minLength = float('inf')
        
        left = 0
        right = 0
        
        while right < len(s):
            char = s[right]
            
            if char in window:
                window[char] += 1
                if window[char] == required[char]:
                    requirements += 1
            
            while left <= right and requirements == len(required):
                # check if we have new minWindow
                if right - left < minLength:
                    minLength = right - left
                    minWindow = (left, right)
                
                char = s[left]
                if char in window:
                    window[char] -= 1
                    if window[char] < required[char]:
                        requirements -= 1
                        
                left += 1

            right += 1
        
        if minLength == float('inf'):
            return ""
        else:
            left, right = minWindow
            return s[left:right+1]