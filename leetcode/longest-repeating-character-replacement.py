// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = Counter(s[0])
        left = right = 0
        maxWindow = 1
        maxCount = 1
        
        while right < len(s):
            windowSize = right - left + 1
            
            if windowSize - maxCount <= k:
                maxWindow = max(maxWindow, windowSize)
                right += 1
                if right < len(s):
                    count[s[right]] += 1
                    maxCount = max(maxCount, count[s[right]])
            else:
                count[s[left]] -= 1
                left += 1
                
        return maxWindow