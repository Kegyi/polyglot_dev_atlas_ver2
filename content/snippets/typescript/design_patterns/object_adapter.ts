class Adaptee{ specific(){ console.log('Adaptee specific') } }
interface Target{ request(): void }
class ObjectAdapter implements Target{ constructor(private a=new Adaptee()){} request(){ this.a.specific() } }
new ObjectAdapter().request()
export {}
