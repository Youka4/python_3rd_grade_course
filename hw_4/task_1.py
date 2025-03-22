import time
import threading
import multiprocessing

repeat = 10
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def run_task(n, method):
    start_time = time.time()

    if method == 'sync':
        for _ in range(repeat):
            fib(n)

    elif method == 'threading':
        threads = []
        for _ in range(repeat):
            thread = threading.Thread(target=fib, args=(n,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    elif method == 'multiprocessing':
        processes = []
        for _ in range(repeat):
            process = multiprocessing.Process(target=fib, args=(n,))
            process.start()
            processes.append(process)
        for process in processes:
            process.join()

    end_time = time.time()
    return end_time - start_time


def compare_times(n):
    sync_time = run_task(n, 'sync')

    thread_time = run_task(n, 'threading')

    process_time = run_task(n, 'multiprocessing')

    return sync_time, thread_time, process_time


if __name__ == "__main__":
    n = 35
    sync_time, thread_time, process_time = compare_times(n)


    with open('artifacts/task1.txt', 'w') as f:
        f.write(f"Time taken for synchronous execution: {sync_time}\n")
        f.write(f"Time taken for threading execution: {thread_time}\n")
        f.write(f"Time taken for multiprocessing execution: {process_time}\n")


