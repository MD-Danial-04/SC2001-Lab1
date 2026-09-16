def merge_sort(A, left, mid, right):  # merge sort from lecture
    comparisons = 0
    i = 0
    m = mid - left
    k = left
    # Copy A[left] to A[right] into an array B 
    B = A[left : right + 1]
    
    # j loops from the start of the right half (m + 1) to the end of B
    for j in range(m + 1, len(B)):
        while i <= m:
            comparisons += 1 
            if B[i] <= B[j]:
                A[k] = B[i]
                i += 1
                k += 1
            else:
                break 
                
        A[k] = B[j]
        k += 1
        
    while i <= m:
        A[k] = B[i]
        i += 1
        k += 1
        
    return comparisons
