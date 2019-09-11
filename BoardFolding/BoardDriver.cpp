#include "BoardFolding2.cpp"

int main (int argc, char **argv)
{
    class BoardFolding TheClass;
    vector<string> compressedPaper;
    const int N = atoi(argv[1]);
    const int M = atoi(argv[2]);

    string row;

    while (cin >> row) 
    {
        compressedPaper.push_back(row);
    }
    
    cout << TheClass.howMany(N, M, compressedPaper) << endl;
}
