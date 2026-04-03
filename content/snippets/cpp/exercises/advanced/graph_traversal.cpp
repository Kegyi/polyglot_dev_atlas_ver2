#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<vector<int>> g = {{1,2},{0,3},{0,3},{1,2}}; // simple graph
    // BFS
    vector<int> vis(4); queue<int>q; q.push(0); vis[0]=1;
    cout<<"BFS:";
    while(!q.empty()){int u=q.front();q.pop(); cout<<" "<<u; for(int v:g[u]) if(!vis[v]){vis[v]=1; q.push(v);} }
    cout<<"\n";
    // DFS
    vector<int> seen(4); function<void(int)> dfs=[&](int u){ seen[u]=1; cout<<u<<" "; for(int v:g[u]) if(!seen[v]) dfs(v); };
    cout<<"DFS: "; dfs(0); cout<<"\n"; }
