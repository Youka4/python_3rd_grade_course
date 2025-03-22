import math
import concurrent.futures
import time
import os


def worker(f, a, step, start, end):
    local_acc = 0
    for i in range(start, end):
        local_acc += f(a + i * step) * step
    return local_acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter

    chunk_size = n_iter // n_jobs
    futures = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < n_jobs - 1 else n_iter
            futures.append(executor.submit(worker, f, a, step, start, end))

        result = sum(future.result() for future in futures)

    return result


def compare_integrate():
    n_jobs_values = [1, 2, 4, 8, os.cpu_count() * 2]
    results = {}

    for n_jobs in n_jobs_values:
        start_time = time.time()
        result = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time = time.time()
        results[n_jobs] = (end_time - start_time, result)

    return results


if __name__ == "__main__":
    results = compare_integrate()

    with open('artifacts/task2.txt', 'w') as f:
        for n_jobs, time_taken in results.items():
            f.write(f"Time taken with {n_jobs} workers: {time_taken[0]}\n Result: {time_taken[1]}\n")
