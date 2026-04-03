#include <string>
#include <map>
#include <iostream>

struct User { int id; std::string name; };

User mapRow(const std::map<std::string,std::string>& row){
    User u; u.id = std::stoi(row.at("id")); u.name = row.at("name"); return u;
}
int main(){
    std::map<std::string,std::string> r{{"id","1"},{"name","Alice"}};
    auto u = mapRow(r);
    std::cout<<u.id<<" "<<u.name<<"\n";
}
