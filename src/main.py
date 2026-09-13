from src.benchmarking.benchmark import benchmark
from src.benchmarking.plotting import plot_results
from src.data_generator import generate_all_datasets
from src.sorting.hybrid_sort import hybrid_sort
from src.sorting.insertion_sort import insertion_sort
from src.sorting.merge_sort import merge_sort


def main():
    # Generate datasets
    generate_all_datasets()

    # TODO: sorting

    # TODO: benchmarking

    # TODO: plotting

if __name__ == "__main__":
    main()
