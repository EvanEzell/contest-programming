#include "AliceGame.cpp"

int main (int argc, char **argv)
{
    class AliceGame theClass;
    cout << theClass.findMinimumValue(atoll(argv[1]),atoll(argv[2])) << endl;
}
