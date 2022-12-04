// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        
        def helper(prev, cur, solutions):
            
            if not cur:
                # print("SOLUTION")
                solutions.append(prev.strip())
                return
            
            strThusFar = ''
            for i, letter in enumerate(cur):
                strThusFar += letter
                # print(strThusFar, end='')
                if strThusFar in wordDict:
                    # print(' *** found word')
                    helper(prev + " " + strThusFar, 
                           cur[i+1:], 
                           solutions)
                # print()
            
            return solutions

        return helper("", s, [])