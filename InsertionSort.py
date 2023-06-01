def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Your input: ", arr)
    insertion_sort(arr)
    print("After Sorting: ", arr)
