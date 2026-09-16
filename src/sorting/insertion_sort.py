def insertion_sort(arr, left, right):
    comparisons = 0 
    for i in range(left + 1, right + 1): 
        key = arr[i]
        j = i - 1 
        while j >= left:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons
