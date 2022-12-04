// https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = Counter(s)
        result = []
        
        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char]
        
        for char, num in count.items():
            result.append(char * num)
            
        return ''.join(result)