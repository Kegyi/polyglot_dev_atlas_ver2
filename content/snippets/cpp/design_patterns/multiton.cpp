#include <map>
#include <memory>
#include <string>
#include <iostream>

class Multiton {
    static std::map<std::string, std::shared_ptr<Multiton>> instances;
public:
    std::string name;
    Multiton(std::string n):name(n){}
    static std::shared_ptr<Multiton> get(const std::string &k){
        auto it = instances.find(k);
        if (it!=instances.end()) return it->second;
        auto v = std::make_shared<Multiton>(k);
        instances[k]=v; return v;
    }
};
std::map<std::string, std::shared_ptr<Multiton>> Multiton::instances;
int main(){
    auto a = Multiton::get("a");
    auto b = Multiton::get("b");
    std::cout<<a->name<<" "<<b->name<<"\n";
}
