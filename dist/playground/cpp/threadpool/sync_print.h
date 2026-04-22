#pragma once
#include <sstream>
#include <mutex>
#include <iostream>
#include <utility>

// RAII helper that accumulates into a stringstream and emits under a lock on destruction.
class LockedOString {
public:
    explicit LockedOString(std::mutex &m) : mtx_(m) {}
    ~LockedOString() {
        std::lock_guard<std::mutex> lk(mtx_);
        std::cout << ss_.str() << std::endl;
    }

    template <typename T>
    LockedOString &operator<<(T &&v) {
        ss_ << std::forward<T>(v);
        return *this;
    }

    // Support manipulators like std::endl (applies to internal stream)
    LockedOString &operator<<(std::ostream &(*manip)(std::ostream &)) {
        manip(ss_);
        return *this;
    }

private:
    std::mutex &mtx_;
    std::ostringstream ss_;
};
