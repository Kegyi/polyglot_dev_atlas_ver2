#include <bits/stdc++.h>
using namespace std;
int main(){
    int n=5; vector<vector<pair<int,int>>> g(n);
    g[0].push_back({1,10}); g[0].push_back({2,3}); g[2].push_back({1,1}); g[1].push_back({3,2}); g[2].push_back({3,8});
    const long long INF=1e18; vector<long long> d(n,INF); d[0]=0; priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<pair<long long,int>>>pq; pq.push({0,0});
    while(!pq.empty()){ auto [dist,u]=pq.top(); pq.pop(); if(dist!=d[u]) continue; for(auto [v,w]:g[u]) if(d[v]>d[u]+w){ d[v]=d[u]+w; pq.push({d[v],v}); } }
    for(int i=0;i<n;i++) cout<<"dist["<<i<<"]="<<d[i]<<"\n";
}
