from src.sorting.insertion_sort import insertion_sort
from src.sorting.merge_sort import merge


def hybrid_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)

    mid = len(arr) // 2

    left, left_count = hybrid_sort(arr[:mid], threshold)
    right, right_count = hybrid_sort(arr[mid:], threshold)

    merged, merge_count =  merge(left, right)
    total = left_count + right_count + merge_count
    return merged, total
