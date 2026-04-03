import heapq

g = {0:[(1,10),(2,3)], 1:[(3,2)], 2:[(1,1),(3,8)], 3:[]}
INF=10**9

def dijkstra(src):
    dist = {v:INF for v in g}
    dist[src]=0; pq=[(0,src)]
    while pq:
        d,u = heapq.heappop(pq)
        if d!=dist[u]: continue
        for v,w in g[u]:
            if dist[v]>d+w:
                dist[v]=d+w; heapq.heappush(pq,(dist[v],v))
    return dist

print(dijkstra(0))
