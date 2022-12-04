// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += n & 1
            n = n >> 1
        return weight