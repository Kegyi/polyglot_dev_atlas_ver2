#include "threadpool.h"
#include <functional>
#include <iostream>
#include <thread>
#include <chrono>
#include <atomic>
#include <condition_variable>
#include <mutex>
#include "sync_print.h"

int main()
{
    constexpr std::size_t THREADCOUNT = 4;
    constexpr std::size_t TASKCAPACITY = 16;

    // Example with a specific task type
    tp::Threadpool<THREADCOUNT, TASKCAPACITY, std::function<void()>> pool;

    const int task_count = 8;

    std::mutex cout_mtx;

    for (int i = 0; i < task_count; ++i) {
        pool.enqueue([i, &cout_mtx]() {
            LockedOString out(cout_mtx);
            out << "Task " << i << " executed in thread pool.";
        });
    }

    // Use the threadpool's built-in completion notification
    pool.wait_for_all();

    {
        LockedOString out(cout_mtx);
        out << "All tasks completed.";
    }
    return 0;
}