

def swap(arr, i, j):
    
    arr[i], arr[j] = arr[j], arr[i]

def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            swap(A, nextpos, nextpos - 1)
            nextpos -= 1  

    return A

lst = [99,1, 12, 25, 71, 100]
print(insertionSort(lst, len(lst)))
