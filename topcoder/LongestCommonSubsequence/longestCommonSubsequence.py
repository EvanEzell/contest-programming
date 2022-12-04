class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = ' ' + text1
        text2 = ' ' + text2
        
        if len(text1) < len(text2):
            text2, text1 = text1, text2
        
        prevRow = [0 for c in text2]
        curRow = [0 for c in text2]
        
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                
                curRow[j] = max(int(text1[i] == text2[j]) + prevRow[j-1],
                                max(prevRow[j],curRow[j-1]))
            
            prevRow, curRow = curRow, prevRow
            
        return prevRow[-1]
