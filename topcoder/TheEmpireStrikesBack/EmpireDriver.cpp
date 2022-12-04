#include "TheEmpireStrikesBack.cpp"
#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

void usage(string msg)
{
    cout << "usage: Empire AX BX CX AY BY CY N M" << endl;
    if (msg.length() != 0) cout << msg << endl;
}

int main (int argc, char** argv)
{
    if (argc != 9) usage("");

    long long ax = atoll(argv[1]);
    long long bx = atoll(argv[2]);
    long long cx = atoll(argv[3]);
    long long ay = atoll(argv[4]);
    long long by = atoll(argv[5]);
    long long cy = atoll(argv[6]);
    long long n = atoll(argv[7]);
    long long m = atoll(argv[8]);

    class TheEmpireStrikesBack TheClass;

    cout << TheClass.find(ax, bx, cx, ay, by, cy, n, m) << endl;

    return 0;
}
