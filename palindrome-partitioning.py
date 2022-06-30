// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def __init__(self):
        self.partitions = []
        self.solution = []
        
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start):
            
            # is a solution?
            if start == len(s):
                # process solution
                self.partitions.append(self.solution.copy())
                return
            
            # generate candidates
            # all possible partitions > k
            for end in range(start, len(s)):
                if palindrome(start, end): # prune partitions that aren't palindromes
                    self.solution.append(s[start:end+1])
                    backtrack(end+1)
                    self.solution.pop()
            
            return self.partitions
        
        backtrack(0)
        return self.partitions
                    
            
            