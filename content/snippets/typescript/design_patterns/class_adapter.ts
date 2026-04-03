class Adaptee{ specific(){ console.log('Adaptee specific') } }
interface Target{ request(): void }
class ClassAdapter extends Adaptee implements Target { request(){ this.specific() } }
new ClassAdapter().request()
export {}
