import math


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[p + i]
    for j in range(0, n2):
        R[j] = arr[q + j + 1]

    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1


def merge_sort(arr, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Your input: ", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("After Sorting: ", arr)
