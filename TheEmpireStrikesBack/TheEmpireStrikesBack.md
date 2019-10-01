# TheEmpireStrikesBack Problem
Topcoder SRM 678 (TheEmpireStrikesBack) D1 500 point problem

### Problem Statement
Darth Vader wants to destroy an entire galaxy that consists of N planets. Quite surprisingly, the entire galaxy lies in a single plane, so we can consider it to be two-dimensional. The planets are numbered 0 through N-1. For each i, planet i is located at the coordinates (P[i].x, P[i].y). All coordinates are nonnegative integers. They are given in a format that is specified below.
Darth Vader has a Death Star. The Death Star is almost complete. The only missing thing is a booster that will increase its range by some amount T. T must be a nonnegative integer.

Once the booster is installed, Darth Vader will be able to fire M missiles from the Death Star. All missiles will be fired at the same time. Each of those M missiles must target one of the N planets. (It is not possible to target coordinates that do not contain a planet.)

Each missile will destroy all planets in some specific rectangular area. More precisely, suppose that one of the missiles targeted a planet located at (X,Y). Consider the rectangle that has sides parallel to coordinate axes, one corner at (0,0), and the opposite corner at (X+T,Y+T). The missile will destroy all planets that lie in this rectangle, including its boundary. Above, T is the contribution of the booster.

You are given the following ints:

AX, BX, CX: these determine the x-coordinates of all planets AY, BY, CY: these determine the y-coordinates of all planets N and M: the number of planets and the number of missiles, as defined above

Use the following pseudocode to generate the coordinates of all planets. Watch out for integer overflow.

P[0].x = AX for i = 1 to N-1: P[i].x = ((P[i-1].x * BX) + CX) mod 1,000,000,007

P[0].y = AY for i = 1 to N-1: P[i].y = ((P[i-1].y * BY) + CY) mod 1,000,000,007

Given this information, your task is to find the weakest booster that still allows Darth Vader to destroy the entire galaxy. Formally, compute and return the smallest nonnegative integer T for which Darth Vader can destroy all N planets.

### Definition
**Class:** TheEmpireStrikesBack
**Method:** find
**Parameters:** int, int, int, int, int, int, int, int
**Returns:** int
**Method signature:** int find(int AX, int BX, int CX, int AY, int BY, int CY, int N, int M)

### Notes
-There may be two or more planets on the same exact position.

#### Constraints
-AX, BX, CX, AY, BY and CY will be between 0 and 10^9 inclusive.
-N will be between 1 and 10^5 inclusive.
-M will be between 1 and N inclusive.

### Examples

0)
2
2
2
2
2
2
2
1

Returns: 0

There are two planets, located at (2,2) and (6,6).
The Death Star has one missile.
If Darth Vader fires it at the planet located at (6,6), the missile will destroy both planets.
This happens regardless of the value of T, so we can choose T = 0.

1)
2
2
2
2
4
1000000000
2
1

Returns: 1

Now we have planets at (2,2) and (6,1).
Again, the Death Star has only one missile.
This time the optimal strategy is to use a booster with T = 1.
Then we can fire the missile at the planet at (6,1), which will destroy all planets in the rectangle between (0,0) and (7,2), inclusive.

2)
1
3
8
10000
10
999910000
3
1

Returns: 30

In this case planets are located at positions (1,10000), (11,9993) and (41,9923).

3)
0
0
0
0
0
0
100000
1000

Returns: 0

All 10^5 planets are in the same position, that is (0,0).

4)
10
20
30
40
50
60
100000
10

Returns: 15720

### My solution
My solution is in [TheEmpireStrikesBack.cpp](). It runs in O(Nlog(N)) time.
