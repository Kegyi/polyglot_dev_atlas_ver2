#include <memory>
#include <iostream>

class LazySingleton {
public:
    static LazySingleton& instance(){
        static LazySingleton inst;
        return inst;
    }
    int value = 0;
};
int main(){
    LazySingleton::instance().value = 10;
    std::cout<<LazySingleton::instance().value<<"\n";
}
