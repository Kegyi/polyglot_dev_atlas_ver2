#pragma once

#include <array>
#include <condition_variable>
#include <functional>
#include <mutex>
#include <stdexcept>
#include <thread>
#include <cstddef>
#include <utility>

namespace tp {

/**
 * @brief Fixed-size, header-only thread pool.
 *
 * This thread pool uses compile-time fixed sizes for the worker count and
 * task capacity to avoid dynamic heap allocations for thread and task
 * containers. The stored task type is a template parameter to allow
 * avoiding type-erasure overhead (i.e. `std::function`).
 *
 * Template parameters:
 * - ThreadCount: number of worker threads (compile-time constant).
 * - TaskCapacity: maximum number of queued tasks (compile-time constant).
 * - TaskType: callable type stored in the queue (defaults to `void(*)()`).
 *
 * Notes:
 * - All memory for threads and tasks is allocated in fixed-size arrays.
 * - `enqueue()` will throw `std::runtime_error` when the queue is full.
 * - `try_enqueue()` is provided for non-throwing enqueue attempts.
 * - The pool is non-copyable and non-movable.
 *
 * Example: create a pool and enqueue lambdas (see examples for details).
 */
template <std::size_t ThreadCount, std::size_t TaskCapacity, typename TaskType = void(*)()>
class Threadpool {
public:
    /**
     * @brief Construct a thread pool and start worker threads.
     */
    Threadpool() noexcept : stop_(false), task_start_(0), task_end_(0), task_count_(0) {
        for (std::size_t i = 0; i < ThreadCount; ++i) {
            threads_[i] = std::thread([this]() { worker_loop(); });
        }
    }

    // non-copyable, non-movable
    Threadpool(const Threadpool&) = delete;
    Threadpool& operator=(const Threadpool&) = delete;
    Threadpool(Threadpool&&) = delete;
    Threadpool& operator=(Threadpool&&) = delete;

    /**
     * @brief Enqueue a task. Notifies one worker.
     * @throws std::runtime_error if the queue is full.
     */
    template <typename F>
    void enqueue(F&& f) {
        push_task(std::forward<F>(f));
        condition_.notify_one();
    }

    /**
     * @brief Try to enqueue a task without throwing. Returns false if full.
     */
    template <typename F>
    bool try_enqueue(F&& f) noexcept {
        std::unique_lock<std::mutex> lock(queue_mutex_);
        if (task_count_ == TaskCapacity) return false;
        tasks_[task_end_] = std::forward<F>(f);
        task_end_ = (task_end_ + 1) % TaskCapacity;
        ++task_count_;
        lock.unlock();
        condition_.notify_one();
        return true;
    }

    /**
     * @brief Destructor: signal stop and join all threads.
     */
    ~Threadpool() {
        {
            std::unique_lock<std::mutex> lock(queue_mutex_);
            stop_ = true;
        }
        condition_.notify_all();
        for (std::size_t i = 0; i < ThreadCount; ++i) {
            if (threads_[i].joinable()) threads_[i].join();
        }
    }

    /**
     * @brief Wait until all queued and running tasks have completed.
     *
     * This method blocks the caller until both the internal queue is empty
     * and there are no tasks currently being executed by worker threads.
     */
    void wait_for_all() {
        std::unique_lock<std::mutex> lock(queue_mutex_);
        completion_cv_.wait(lock, [this] { return task_count_ == 0 && active_tasks_ == 0; });
    }

private:
    // Main worker loop executed by each thread.
    void worker_loop() {
        for (;;) {
            TaskType task;
            {
                std::unique_lock<std::mutex> lock(queue_mutex_);
                condition_.wait(lock, [this] { return stop_ || task_count_ > 0; });
                if (stop_ && task_count_ == 0) return;
                task = std::move(tasks_[task_start_]);
                task_start_ = (task_start_ + 1) % TaskCapacity;
                --task_count_;
                ++active_tasks_;
            }
            task();
            {
                std::unique_lock<std::mutex> lock(queue_mutex_);
                --active_tasks_;
                if (task_count_ == 0 && active_tasks_ == 0) completion_cv_.notify_all();
            }
        }
    }

    // Internal push that assumes the caller holds no lock.
    template <typename F>
    void push_task(F&& f) {
        std::unique_lock<std::mutex> lock(queue_mutex_);
        if (task_count_ == TaskCapacity) throw std::runtime_error("Task queue is full");
        tasks_[task_end_] = std::forward<F>(f);
        task_end_ = (task_end_ + 1) % TaskCapacity;
        ++task_count_;
    }

    std::array<std::thread, ThreadCount> threads_;
    std::array<TaskType, TaskCapacity> tasks_;
    std::mutex queue_mutex_;
    std::condition_variable condition_;
    std::condition_variable completion_cv_;
    bool stop_;

    // Circular buffer indices and task count
    std::size_t task_start_;
    std::size_t task_end_;
    std::size_t task_count_;
    // Number of tasks currently being executed by workers (not queued)
    std::size_t active_tasks_ = 0;
};

} // namespace tp
