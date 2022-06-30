// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count = Counter(t)
        for char in s:
            if char in count and count[char]:
                count[char] -= 1
            else:
                return False
        return True