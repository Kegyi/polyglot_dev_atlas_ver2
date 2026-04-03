#include <bits/stdc++.h>
using namespace std;
int N=8; vector<int> col;
bool ok(int r,int c){ for(int i=0;i<r;i++) if(col[i]==c||abs(col[i]-c)==r-i) return false; return true; }
void solve(int r){ if(r==N){ for(int i=0;i<N;i++) cout<<col[i]<<" "; cout<<"\n"; exit(0);} for(int c=0;c<N;c++) if(ok(r,c)){ col[r]=c; solve(r+1); }}
int main(){ col.assign(N,0); solve(0); }
