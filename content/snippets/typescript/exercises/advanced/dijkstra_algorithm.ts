type Edge = [number,number]
const g: Record<number,Edge[]> = {0:[[1,10],[2,3]],1:[[3,2]],2:[[1,1],[3,8]],3:[]}
const INF = 1e9
function dijkstra(src:number){ const dist = new Map<number,number>(); for(const k in g) dist.set(Number(k), INF); dist.set(src,0);
  const pq: [number,number][] = [[0,src]]
  while(pq.length){ pq.sort((a,b)=>a[0]-b[0]); const [d,u]=pq.shift()!; if(d!==dist.get(u)) continue; for(const [v,w] of g[u]) if((dist.get(v)??INF) > d + w){ dist.set(v,d+w); pq.push([d+w,v]); } }
  return Object.fromEntries(dist)
}
console.log(dijkstra(0))
export {}
