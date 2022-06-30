// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        editDistance = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        
        prevED = [j for j in range(len(word2)+1)]
        curED = [0 for _ in range(len(word2)+1)]
        
        print(prevED)
    
        for i in range(1,len(word1)+1):
            curED[0] = prevED[0] + 1
            for j in range(1,len(word2)+1):
                curED[j] = min(prevED[j-1] + int(word1[i-1] != word2[j-1]),
                               prevED[j] + 1,
                               curED[j-1] + 1)
            
            prevED = curED
            curED = [0 for _ in range(len(word2)+1)]
        
        return prevED[len(word2)]