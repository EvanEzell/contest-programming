#include <iostream>
#include <cmath>

using namespace std;

class AliceGame
{
    public:
        long long findMinimumValue(long long a, long long b);
};

long long 
AliceGame::findMinimumValue(long long a, long long b)
{
    long long r = sqrt(a+b); // r must be a perfect square

    // test for base cases
    if (r*r != a+b) return -1; 
    else if (a == 2 || b == 2) return -1;
    else if (a == 0 && b == 0) return 0;
    else if (a < 2*r && a % 2 != 0) return 1;
    else if (a <= 2*r && a % 2 == 0) return 2;
    else if (a == 2*r+1) return 3;
    else { // find minimum h using binary search

        long long low = 1;
        long long high = r;
        long long mid, h;

        while (low <= high)
        {
            mid = (low + high) / 2;

            if(2*r*mid - mid*mid > a) {
                high = mid-1;
            } else {
                h = mid;
                low = mid+1;
            }
        }
        
        a -= (2*r*h - h*h);

        return h + findMinimumValue(a, b);
    }
}
