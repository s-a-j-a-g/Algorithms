def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]


if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Your input: ", arr)
    selection_sort(arr)
    print("After Sorting: ", arr)
