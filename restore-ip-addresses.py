// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def validLength(n_ints, n_digits):
            return n_digits < n_ints or n_digits > 3 * n_ints
        
        def validNum(num):
            return int(num) >= 0 and int(num) <= 255
        
        result = []
        def helper(prev, s, n_ints):
            
            if validLength(n_ints, len(s)):
                return
            
            if not s:
                result.append(prev)
                return
            
            # if its a zero its the only option to take it by itself (no leading zero)
            if s[0] == "0":
                helper(prev + ["0"], s[1:], n_ints - 1)
                return
            
            numThusFar = ''
            for i in range(min(3,len(s))):
                numThusFar += s[i]
                if validNum(numThusFar):
                    helper(prev + [numThusFar], 
                           s[i+1:], 
                           n_ints - 1)
            
        helper([], s, 4)
        return list(map(lambda s: ".".join(s), result))