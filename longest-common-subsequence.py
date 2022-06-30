// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        prev = [0 for j in range(n+1)]
        cur = [0 for j in range(n+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text1[i] == text2[j]:
                    cur[j] = prev[j+1] + 1
                cur[j] = max(cur[j], prev[j], cur[j+1], prev[j+1])
            prev = cur
            cur = [0 for j in range(n+1)]
        
        return prev[0]