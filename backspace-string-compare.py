// https://leetcode.com/problems/backspace-string-compare

from itertools import zip_longest

class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def nextChar(S: str):
            skip = 0
            for c in reversed(S):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c   
        
        return all(s == t for s,t in zip_longest(nextChar(S), nextChar(T)))