#include <iostream>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

class BoardFolding
{
    public:
        long long howMany(int N, int M, vector<string> compressedPaper);

    private:
        vector<string> rotate(vector<string> &paper);
        int toNumber(char c);
        vector<string> decompress(int N, 
                                  int M, 
                                  vector<string>& compressedPaper);
        vector<int> startingPlaces(vector<int>& id);
        long long combinations(vector<int> &start_places, 
                               vector<int> &end_places);
        vector<int> mapRows(vector<string>& paper);
};

long long
BoardFolding::howMany(int N, int M, vector<string> compressedPaper)
{
    vector<string> paper = decompress(N, M, compressedPaper);

    vector<int> id; // id of rows currently working on
    vector<int> start_places; // start place of fold
    vector<int> end_places;  // end place of fold

    // store total folds for each axes
    long long row_folds;
    long long col_folds;

    /* compute possible row folds */
    id = mapRows(paper);
    start_places = startingPlaces(id);

    // reverse rows to compute ending places
    reverse(id.begin(), id.end());
    end_places = startingPlaces(id);
    reverse(end_places.begin(), end_places.end());
    reverse(id.begin(), id.end());

    row_folds = combinations(start_places, end_places);

    /* compute possible col folds */
    paper = rotate(paper);

    id = mapRows(paper);
    start_places = startingPlaces(id);

    reverse(id.begin(), id.end());
    end_places = startingPlaces(id);
    reverse(end_places.begin(), end_places.end());

    // count possible column folds
    col_folds = combinations(start_places, end_places);

    return row_folds * col_folds;    
}

vector<int>
BoardFolding::mapRows(vector<string>& paper)
{
    map<string,int> row_map;

    vector<int> id;
    int unique_idx = 0;
    int idx = 0;

    for (vector<string>::const_iterator itr = paper.begin();
         itr != paper.end();
         ++itr)
    {
        if (row_map.find(*itr) == row_map.end()) // new row found
        {
            unique_idx++;
            row_map.insert(pair<string,int>(*itr,unique_idx));
            id.push_back(unique_idx);
        } else { // row already exists 
            id.push_back(row_map[*itr]);
        }
        idx++;  
    }

    return id;
}

vector<string> 
BoardFolding::rotate(vector<string> &paper)
{
    vector<string> rotated_paper;
    string cur_column = "";
    int M = paper[0].length();

    for (int j = 0; j < M; j++)
    {
        for (vector<string>::reverse_iterator itr = paper.rbegin();
             itr != paper.rend();
             ++itr)
        {
            cur_column += (*itr)[j];
        }
        rotated_paper.push_back(cur_column);
        cur_column = "";
    }

    return rotated_paper;
}

long long 
BoardFolding::combinations(vector<int> &start_places, 
                           vector<int> &end_places)
{
    long long count = 0;

    for (int i = 0; i < start_places.size(); i++)
    {
        if (start_places[i])
            count = accumulate(end_places.begin()+i+1,
                               end_places.end(), 
                               count);
    }

    return count;
}

vector<int> 
BoardFolding::startingPlaces(vector<int>& id)
{
    int N = id.size();

    // calculate maximum w for each j and store it
    vector<int> max_w;
    for (int j = 0; j <= N; j++)
    {
        int w = 1;
        for (w = 1; w <= j && w+j <= N; w++)
        {
            if (id[j-w] != id[j+(w-1)])
            {
                max_w.push_back(w-1);
                break;
            }
        }
        if (max_w.size() <= j) max_w.push_back(w-1);
    }

    vector<int> start_places (N+1);
    start_places[0] = 1; // first fold line is always start place

    // compute possible starting places
    for (int i = 0; i < N; i++)
    {
        if (start_places[i] == 0) continue; // i must be a start row

        for (int j = i+1; j < N && j+j-(i+1) < N; j++)
        {
            if (start_places[j]) continue;
            if (max_w[j] >= j-i) start_places[j] = 1;
        }
    }

    return start_places;
}

vector<string> 
BoardFolding::decompress(int N, int M, vector<string>& compressedPaper)
{
    vector<string> paper;
    string curRow = "";
    short int bit;
    ostringstream convert;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            bit = ((toNumber(compressedPaper[i][j / 6])) >> (j % 6)) % 2;
            convert << bit;
            curRow += convert.str();
            convert.str("");
        }
        paper.push_back(curRow);
        curRow.clear();
    }

    return paper;
}

int 
BoardFolding::toNumber(char c)
{
    if (c >= '0' && c <= '9') return c-'0';
    if (c >= 'a' && c <= 'z') return c-'a'+10;
    if (c >= 'A' && c <= 'Z') return c-'A'+36;
    if (c == '#') return c-'#'+62;
    if (c == '@') return c-'@'+63;
    return -1; // invalid input
}
