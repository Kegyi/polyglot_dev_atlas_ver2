const acts: [number,number][] = [[1,4],[3,5],[0,6],[5,7],[8,9],[5,9]]
acts.sort((a,b)=>a[1]-b[1])
const res: [number,number][] = []
let last=-1
for(const [s,e] of acts) if(s>last){ res.push([s,e]); last=e }
console.log('Selected', res)
export {}
