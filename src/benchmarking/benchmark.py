import time


def benchmark(sorting_function, data):
    # run a sorting algorithm and benchmark both comparisons and CPU time
    start = time.process_time()
    sorted_data, comparisons = sorting_function(data)
    end = time.process_time()
    cpu_time = end - start
    return sorted_data, comparisons, cpu_time
