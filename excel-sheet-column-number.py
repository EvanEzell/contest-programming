// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        return sum([(ord(c) - ord('A') + 1) * (26**pow) for pow, c in enumerate(reversed(columnTitle))])