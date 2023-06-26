def max_heapify(A, n, i):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)


def heap_sort(A):
    build_max_heap(A)
    print("After Buiding Max Heap: ", arr)
    n = len(A)

    # After building max heap, the first node (i.e the largest element) is kept at at last and heap is again built and repeated 
    # we start from end of the array since last element is swapped with the first element.
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


if __name__ == "__main__":
    arr = [15, 5, 20, 1, 17, 10, 30]
    print("Original Array: ", arr)
    heap_sort(arr)
    print("After Heap Sort: ", arr)
