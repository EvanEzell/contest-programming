# AliceGame Problem
Adapted from Topcoder SRM 639 (AliceGame) D1 250 point problem

### Problem Statement
Alice and Kirito just played a game. The game consisted of a finite (possibly empty) sequence of turns. You do not know the exact number of turns. The turns were numbered starting from 1. In each turn, exactly one of our two players won. The winner of turn i scored 2*i-1 points. You are given two scores, x and y. Find out whether it is possible that at the end of the game Alice had exactly x points and Kirito had exactly y points. If it is possible, return the smallest number of turns Alice could have won. If the given final result is not possible, return -1 instead.

### Definition
**Class:** AliceGame  
**Method:** findMinimumValue  
**Parameters:** long long, long long  
**Returns:** long long  
**Method signature:** long long findMinimumValue(long long x, long long y)

### Limits
**Time limit (s):** 2.000  
**Memory limit (MB):** 256

### Constraints
x + y < 2^63

### My solution
My solution is in [AliceGame.cpp](https://github.com/EvanEzell/Topcoder/blob/master/AliceGame/AliceGame.cpp). It runs in O(log(rounds)) time. The linear solution is most trivial. There also is a constant time solution, discovered by one of my classmates, involving some geometric math.
