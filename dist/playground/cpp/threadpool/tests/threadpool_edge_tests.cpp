#include "threadpool.h"
#include <gtest/gtest.h>
#include <atomic>
#include <chrono>
#include <thread>

// Test that enqueue throws when the queue is full (no workers consuming)
TEST(ThreadpoolEdgeTests, EnqueueThrowsWhenFull) {
    constexpr std::size_t ThreadCount = 0; // no workers
    constexpr std::size_t TaskCapacity = 2;

    tp::Threadpool<ThreadCount, TaskCapacity, std::function<void()>> pool;

    pool.enqueue([](){});
    pool.enqueue([](){});
    EXPECT_THROW(pool.enqueue([](){}), std::runtime_error);
}

// Test try_enqueue returns false when queue is full
TEST(ThreadpoolEdgeTests, TryEnqueueReturnsFalseWhenFull) {
    constexpr std::size_t ThreadCount = 0; // no workers
    constexpr std::size_t TaskCapacity = 3;

    tp::Threadpool<ThreadCount, TaskCapacity, std::function<void()>> pool;

    EXPECT_TRUE(pool.try_enqueue([](){}));
    EXPECT_TRUE(pool.try_enqueue([](){}));
    EXPECT_TRUE(pool.try_enqueue([](){}));
    EXPECT_FALSE(pool.try_enqueue([](){}));
}

// Test function-pointer specialization executes tasks (no-arg function pointer)
static std::atomic<int> g_edge_counter{0};
void edge_fp_task_noarg() { g_edge_counter.fetch_add(1, std::memory_order_relaxed); }

TEST(ThreadpoolEdgeTests, FunctionPointerTasks) {
    constexpr std::size_t ThreadCount = 2;
    constexpr std::size_t TaskCapacity = 8;

    g_edge_counter.store(0, std::memory_order_relaxed);
    tp::Threadpool<ThreadCount, TaskCapacity, void(*)()> pool;

    pool.enqueue(&edge_fp_task_noarg);
    pool.enqueue(&edge_fp_task_noarg);

    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    EXPECT_EQ(g_edge_counter.load(), 2);
}
