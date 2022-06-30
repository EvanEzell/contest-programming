// https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        string = " " + s
        pattern = " " + p
        
        match = [[False for i in string] for j in pattern]
        match[0][0] = True
        
        for j in range(2,len(pattern)):
            match[j][0] = pattern[j] == '*' and match[j-2][0]
        
        for j in range(1,len(pattern)):
            for i in range(1,len(string)):
                if pattern[j] == '*':
                    match[j][i] = (match[j-2][i] or 
                                   ((pattern[j-1] == '.' or pattern[j-1] == string[i]) and match[j][i-1]))
                else:
                    match[j][i] = match[j-1][i-1] and (pattern[j] == string[i] or pattern[j] == '.')
        
        return match[-1][-1]