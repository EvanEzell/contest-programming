// https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result | ((n & 1) << (32 - i - 1))
            n = n >> 1
        return result