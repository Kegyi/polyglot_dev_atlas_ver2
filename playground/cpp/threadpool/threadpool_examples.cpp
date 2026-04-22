#include "threadpool.h"
#include <iostream>
#include <functional>
#include <atomic>
#include <thread>
#include <chrono>

using namespace std::literals;

// Example free functions for use with function-pointer task type
void fp_task_0() { std::cout << "fp_task_0 executed\n"; }
void fp_task_1() { std::cout << "fp_task_1 executed\n"; }

int main() {
    std::cout << "Example: function-pointer task type" << std::endl;
    {
        // Thread pool storing plain function pointers (no type-erasure)
        tp::Threadpool<2, 8, void(*)()> pool_fp;
        pool_fp.enqueue(&fp_task_0);
        pool_fp.enqueue(&fp_task_1);
        std::this_thread::sleep_for(200ms);
    }

    std::cout << "Example: std::function task type with captures" << std::endl;
    {
        // Thread pool storing std::function to allow capturing lambdas
        tp::Threadpool<2, 8, std::function<void()>> pool_fn;

        std::atomic<int> counter{0};
        for (int i = 0; i < 6; ++i) {
            pool_fn.enqueue([i, &counter]() {
                counter.fetch_add(1, std::memory_order_relaxed);
                std::cout << "lambda task " << i << " executed\n";
            });
        }

        // Demonstrate try_enqueue fails when full
        bool ok = true;
        for (int i = 0; i < 10; ++i) {
            // try to push many tasks; some will fail if the queue is full
            ok = pool_fn.try_enqueue([i]() { std::cout << "try task " << i << "\n"; });
            if (!ok) {
                std::cout << "try_enqueue failed at iteration " << i << " (queue full)\n";
                break;
            }
        }

        std::this_thread::sleep_for(300ms);
        std::cout << "counter = " << counter.load() << std::endl;
    }

    std::cout << "Examples done." << std::endl;
    return 0;
}
