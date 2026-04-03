#include <bits/stdc++.h>
using namespace std;int main(){ vector<pair<int,int>> acts={{1,4},{3,5},{0,6},{5,7},{8,9},{5,9}}; sort(acts.begin(), acts.end(), [](auto &a, auto &b){ return a.second < b.second; }); int last= -1; cout<<"Selected:"; for(auto &p:acts) if(p.first>last){ cout<<" ("<<p.first<<","<<p.second<<")"; last=p.second; } cout<<"\n"; }
