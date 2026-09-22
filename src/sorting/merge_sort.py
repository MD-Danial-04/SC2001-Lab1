def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_count = merge_sort(arr[:mid])
    right, right_count = merge_sort(arr[mid:])

    merged, merge_count = merge(left, right)
    total_count = left_count + right_count + merge_count

    return merged, total_count

def merge(left, right):
    result = []
    i = j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, comparisons
