# def parent(i):
#     return (i - 1) // 2
#
# def left(i):
#     return 2 * i + 1
#
# def right(i):
#     return 2 * i + 2
#
# def max_heapify(arr, n, i):
#     largest = i
#     l = left(i)
#     r = right(i)
#
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         max_heapify(arr, n, largest)
#
# def build_max_heap(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         max_heapify(arr, n, i)
#
# def heap_sort(arr):
#     n = len(arr)
#     build_max_heap(arr)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         max_heapify(arr, i, 0)
#     return arr
#
# arr = [5, 3, 8, 4, 2]
# sorted_arr = heap_sort(arr)
# print(sorted_arr)


def max_heapify(A, n, i):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def build_max_heap(A):
    n = len(A)
    for i in range(n, -1, -1):
        max_heapify(A, n, i)
    print(A)

def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort(A)
print(A)

