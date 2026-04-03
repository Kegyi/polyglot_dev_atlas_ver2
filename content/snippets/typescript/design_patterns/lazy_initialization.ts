class LazySingleton {
  private static _instance: LazySingleton | null = null
  private constructor(public value = 0){}
  static instance(){
    if (!this._instance) this._instance = new LazySingleton()
    return this._instance
  }
}
console.log(LazySingleton.instance().value)
export {}
