#include <iostream>

// Object Adapter: Adapter has-a Adaptee
class Adaptee { public: void specific() { std::cout<<"Adaptee specific\n"; } };
class Target { public: virtual void request() = 0; };
class ObjectAdapter : public Target { Adaptee a; public: void request() override { a.specific(); } };
int main(){ ObjectAdapter a; a.request(); }
