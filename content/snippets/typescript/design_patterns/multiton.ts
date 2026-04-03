class Multiton {
  private static instances: Record<string, Multiton> = {}
  private constructor(public key: string){}
  static get(key: string){
    return this.instances[key] ??= new Multiton(key)
  }
}
console.log(Multiton.get('a').key, Multiton.get('b').key)
export {}
