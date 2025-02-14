import timeit
import memory_profiler


def benchmark_function(func, *args, **kwargs):
    """Measures execution time and memory usage of a function."""
    mem_before = memory_profiler.memory_usage()[0]

    start_time = timeit.default_timer()
    result = func(*args, **kwargs)  # Run the function
    exec_time = timeit.default_timer() - start_time

    mem_after = memory_profiler.memory_usage()[0]
    mem_usage = mem_after - mem_before

    return exec_time, mem_usage, result


# Run benchmarks
def benchmark(functions: dict[str, callable]):
    print("Benchmarking...")
    for name, func in functions.items():
        exec_time, mem_usage, _ = benchmark_function(func)
        print(_)
        print(f"{name}: Time = {exec_time:.6f}s, Memory = {mem_usage:.2f} MiB")
