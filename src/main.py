from functools import partial

from src.benchmarking.benchmark import benchmark
from src.benchmarking.plotting import plot_multiple, plot_results
from src.data_generator import sizes
from src.sorting.hybrid_sort import hybrid_sort
from src.sorting.merge_sort import merge_sort


def load_dataset(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]


def run_c_i(threshold=16):
    """Fixed S, vary n: key comparisons vs input size."""
    print(f"\n=== c(i) Hybrid sort with S = {threshold} ===")
    ns, hybrid_comps, merge_comps = [], [], []

    for n in sizes:
        data = load_dataset(f"datasets/data_{n}.txt")
        sort_fn = partial(hybrid_sort, threshold=threshold)
        _, h_c, h_t = benchmark(sort_fn, data.copy())
        _, m_c, m_t = benchmark(merge_sort, data.copy())
        ns.append(n)
        hybrid_comps.append(h_c)
        merge_comps.append(m_c)
        print(
            f"n = {n:10d}  hybrid = {h_c} ({h_t:.4f}s)  "
            f"merge = {m_c} ({m_t:.4f}s)"
        )

    plot_results(
        ns,
        hybrid_comps,
        "n",
        "key comparisons",
        f"Hybrid key comparisons vs n (S={threshold})",
    )
    plot_results(
        ns,
        merge_comps,
        "n",
        "key comparisons",
        "Merge sort key comparisons vs n",
    )


def run_c_ii():
    """Fixed n, vary S: key comparisons vs threshold."""
    n = 1_000_000
    data = load_dataset(f"datasets/data_{n}.txt")
    thresholds = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    _, merge_comparisons, merge_time = benchmark(merge_sort, data.copy())
    print(f"\n=== c(ii) n = {n} ===")
    print(f"Merge sort: {merge_comparisons} comparisons, {merge_time:.4f}s")
    xs, comps, times = [], [], []
    for s in thresholds:
        sort_fn = partial(hybrid_sort, threshold=s)
        _, c, t = benchmark(sort_fn, data.copy())
        xs.append(s)
        comps.append(c)
        times.append(t)
        print(f"S = {s:3d}  comparisons = {c}  time = {t:.4f}s")
    plot_results(xs, comps, "S", "comparisons", f"Hybrid comparisons vs S (n={n})")
    plot_results(xs, times, "S", "CPU time (s)", f"Hybrid time vs S (n={n})")


def run_c_iii():
    """Vary n and S; pick S that minimises CPU time for each n."""
    thresholds = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    # Skip tiny n (time is too noisy) and 5M/10M for a first sweep.
    study_sizes = [10_000, 50_000, 100_000, 500_000, 1_000_000, 2_000_000]
    time_series = []
    best_n, best_s, best_t = [], [], []

    print("\n=== c(iii) Optimal S across input sizes ===")
    for n in study_sizes:
        data = load_dataset(f"datasets/data_{n}.txt")
        times = []
        print(f"\nn = {n}")
        best_threshold, best_time = None, None
        for s in thresholds:
            sort_fn = partial(hybrid_sort, threshold=s)
            _, _, t = benchmark(sort_fn, data.copy())
            times.append(t)
            print(f"  S = {s:3d}  time = {t:.4f}s")
            if best_time is None or t < best_time:
                best_threshold, best_time = s, t
        time_series.append((f"n={n}", thresholds, times))
        best_n.append(n)
        best_s.append(best_threshold)
        best_t.append(best_time)
        print(f"  best S = {best_threshold} ({best_time:.4f}s)")

    print("\nSummary: fastest S per n")
    for n, s, t in zip(best_n, best_s, best_t):
        print(f"  n = {n:10d}  S* = {s:3d}  time = {t:.4f}s")

    plot_multiple(
        time_series,
        "S",
        "CPU time (s)",
        "Hybrid CPU time vs S for different n",
    )
    plot_results(
        best_n,
        best_s,
        "n",
        "optimal S",
        "Optimal S vs n (min CPU time)",
    )


def run_d(threshold=16, n=10_000_000):
    """Compare original merge sort vs hybrid (optimal S) on 10 million integers."""
    print(f"\n=== (d) Merge vs hybrid (S={threshold}), n={n} ===")
    data = load_dataset(f"datasets/data_{n}.txt")

    _, merge_comps, merge_time = benchmark(merge_sort, data.copy())
    hybrid_fn = partial(hybrid_sort, threshold=threshold)
    _, hybrid_comps, hybrid_time = benchmark(hybrid_fn, data.copy())

    print(f"Merge sort:          {merge_comps} comparisons, {merge_time:.4f}s")
    print(f"Hybrid sort (S={threshold}): {hybrid_comps} comparisons, {hybrid_time:.4f}s")
    print(
        f"Comparisons: hybrid is {hybrid_comps / merge_comps:.3f}x merge"
    )
    print(f"CPU time:    hybrid is {hybrid_time / merge_time:.3f}x merge")


def main():
    # generate_all_datasets()  # run once if files are missing
    run_c_i(threshold=16)
    run_c_ii()
    run_c_iii()
    run_d()


if __name__ == "__main__":
    main()
