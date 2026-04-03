#include <iostream>

class Target { public: virtual void request() = 0; };
class Adaptee { public: void specific() { std::cout<<"Adaptee specific\n"; } };
// C++ class adapter via inheritance isn't common; emulate by inheriting Adaptee and adapting
class ClassAdapter : public Adaptee, public Target { public: void request() override { specific(); } };
int main(){ ClassAdapter a; a.request(); }
