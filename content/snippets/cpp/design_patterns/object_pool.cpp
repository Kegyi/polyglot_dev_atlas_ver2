#include <vector>
#include <memory>
#include <iostream>

class PooledObject {
public:
    int value;
};

class ObjectPool {
    std::vector<std::unique_ptr<PooledObject>> pool;
public:
    PooledObject* acquire() {
        if (!pool.empty()) {
            auto p = pool.back().release(); pool.pop_back();
            return p;
        }
        return new PooledObject();
    }
    void release(PooledObject* obj) {
        pool.emplace_back(obj);
    }
};

int main(){
    ObjectPool p;
    auto *o = p.acquire();
    o->value = 42;
    std::cout<<o->value<<"\n";
    p.release(o);
}
