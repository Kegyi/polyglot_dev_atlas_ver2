const g: number[][] = [[1,2],[0,3],[0,3],[1,2]]
console.log('BFS:');
{
  const q = [0]; const seen = new Set([0]);
  while(q.length){ const u = q.shift()!; process.stdout.write(' '+u); for(const v of g[u]) if(!seen.has(v)){ seen.add(v); q.push(v); } }
  console.log();
}
console.log('DFS:');
{ const seen = new Set<number>(); function dfs(u:number){ seen.add(u); process.stdout.write(' '+u); for(const v of g[u]) if(!seen.has(v)) dfs(v); } dfs(0); console.log(); }
export {}
