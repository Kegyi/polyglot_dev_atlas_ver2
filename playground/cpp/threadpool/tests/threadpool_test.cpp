#include "threadpool.h"
#include <gtest/gtest.h>
#include <atomic>
#include <chrono>
#include <thread>

TEST(ThreadpoolTest, SingleTask) {
    constexpr std::size_t ThreadCount = 2;
    constexpr std::size_t TaskCapacity = 4;

    tp::Threadpool<ThreadCount, TaskCapacity, std::function<void()>> pool;

    bool task_executed = false;
    pool.enqueue([&]() {
        task_executed = true;
    });

    std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Allow time for task execution
    EXPECT_TRUE(task_executed) << "Single task was not executed correctly.";
}

TEST(ThreadpoolTest, MultipleTasks) {
    constexpr std::size_t ThreadCount = 4;
    constexpr std::size_t TaskCapacity = 8;

    tp::Threadpool<ThreadCount, TaskCapacity, std::function<void()>> pool;

    std::atomic<int> counter = 0;
    for (int i = 0; i < 8; ++i) {
        pool.enqueue([&]() {
            counter.fetch_add(1, std::memory_order_relaxed);
        });
    }

    std::this_thread::sleep_for(std::chrono::milliseconds(200)); // Allow time for task execution
    EXPECT_EQ(counter, 8) << "Not all tasks were executed correctly.";
}

TEST(ThreadpoolTest, ThreadpoolShutdown) {
    constexpr std::size_t ThreadCount = 2;
    constexpr std::size_t TaskCapacity = 4;

    {
        tp::Threadpool<ThreadCount, TaskCapacity, std::function<void()>> pool;

        for (int i = 0; i < 4; ++i) {
            pool.enqueue([i]() {
                std::this_thread::sleep_for(std::chrono::milliseconds(50));
            });
        }
    } // Threadpool destructor should wait for all tasks to complete

    SUCCEED() << "Threadpool shutdown gracefully.";
}