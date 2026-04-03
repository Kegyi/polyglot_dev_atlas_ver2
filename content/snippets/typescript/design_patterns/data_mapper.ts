type Row = { [k: string]: string }
class User { constructor(public id: number, public name: string){} }
function mapRow(r: Row){ return new User(Number(r.id), r.name) }
console.log(mapRow({id:'4', name:'Dana'}))
export {}
