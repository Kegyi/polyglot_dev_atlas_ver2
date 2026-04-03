from collections import deque

g = {0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
print('BFS:', end=' ')
q=deque([0]); seen={0}
while q:
    u=q.popleft(); print(u, end=' ')
    for v in g[u]:
        if v not in seen: seen.add(v); q.append(v)
print('\nDFS:', end=' ')
seen=set()
import sys
sys.setrecursionlimit(10000)
def dfs(u):
    seen.add(u); print(u, end=' ')
    for v in g[u]:
        if v not in seen: dfs(v)

dfs(0)
