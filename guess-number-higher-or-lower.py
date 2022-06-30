// https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        lower = 1
        upper = n
        
        while True:
            my_guess = ((upper - lower) // 2) + lower
            result = guess(my_guess)
            
            if result == -1:
                upper = my_guess - 1
            elif result == 1:
                lower = my_guess + 1
            else:
                return my_guess
            