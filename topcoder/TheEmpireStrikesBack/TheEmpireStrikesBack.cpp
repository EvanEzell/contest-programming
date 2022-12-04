#include <iostream>
#include <map>
#include <deque>
#include <limits>

using namespace std;

class TheEmpireStrikesBack
{
    public:
        long long find(long long ax, long long bx, long long cx,
                       long long ay, long long by, long long cy,
                       long long n, long long m);

    private:
        bool validT(unsigned long long t,
                    long long m,
                    deque< pair<unsigned long, unsigned long> > dq);
};

long long 
TheEmpireStrikesBack::find(long long ax, long long bx, long long cx,
                           long long ay, long long by, long long cy,
                           long long n, long long m)
{
    multimap<unsigned long, unsigned long> mm;

    mm.insert(make_pair(ax, ay));
    unsigned long first = ax;
    unsigned long second = ay;
    for (long long i = 1; i < n; i++)
    {
        first = ((first * bx) + cx) % 1000000007;
        second = ((second * by) + cy) % 1000000007;
        mm.insert(make_pair(first,second));
    }

    multimap<unsigned long, unsigned long>::iterator itr, prev;
    for (itr = mm.begin(); itr != mm.end();)
    {
        if (itr != mm.begin() && prev->second <= itr->second)
        {
            mm.erase(prev);
            prev = itr;
            prev--;
            continue;
        }
        prev = itr;
        itr++;
    }

    deque< pair<unsigned long, unsigned long> > dq;
    for (itr = mm.begin(); itr != mm.end(); itr++)
    {
        dq.push_back(make_pair(itr->first, itr->second));
    }

    long long low = 0;
    long long high = numeric_limits<long long>::max();
    long long mid, result;

    while (low <= high)
    {
        mid = (low + high) / 2;

        if (validT(mid,m,dq)) {
            result = mid;
            high = mid-1;
        } else {
            low = mid+1;
        }
    }

    return result;
}

bool
TheEmpireStrikesBack::validT(unsigned long long t,
                             long long m,
                             deque< pair<unsigned long, unsigned long> > dq)
{
    deque< pair<unsigned long, unsigned long> >::iterator itr, last;

    while (true)
    {

        if (dq.size() <= m) return true;
        if (m == 0) return false;
        for (itr = dq.begin(); itr != dq.end(); itr++)
        {
            if (itr->second+t >= dq.begin()->second) last = itr;
        }

        itr = last;
        itr++;

        dq.erase(dq.begin(),itr);

        for (itr = dq.begin(); itr != dq.end(); itr++)
        {
            if (last->first + t >= itr->first) dq.pop_front();
        }

        m--;
    }
}
