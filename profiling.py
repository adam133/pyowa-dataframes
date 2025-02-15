import multiprocessing


def profile_function(func, *args, **kwargs):
    output = func(*args, **kwargs)
    return output


# Run benchmarks
def benchmark(functions: dict[str, callable]):
    print("Benchmarking...")
    for name, func in functions.items():
        process = multiprocessing.Process(target=profile_function, args=(func,))
        process.start()
        process.join()

        print("Finished profiling", name)
