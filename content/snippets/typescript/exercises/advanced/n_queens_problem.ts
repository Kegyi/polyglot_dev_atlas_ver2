const N = 8
const cols = new Array<number>(N).fill(0)
function ok(r:number,c:number){ for(let i=0;i<r;i++) if(cols[i]===c || Math.abs(cols[i]-c)===r-i) return false; return true }
function solve(r=0): boolean{ if(r===N){ console.log(cols); return true } for(let c=0;c<N;c++){ if(ok(r,c)){ cols[r]=c; if(solve(r+1)) return true } } return false }
solve(); export {}
