// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        canBreak = [False] * (len(s) + 1)
        canBreak[-1] = True
        

        for i in range(len(s)-1, -1, -1):
            curWord = ""
            for j in range(i, len(s)):
                curWord += s[j]
                if curWord in wordDict and canBreak[j+1]:
                    canBreak[i] = True
                    continue
        
        return canBreak[0]