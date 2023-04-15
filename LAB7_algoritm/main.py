
#CHATGPT
# def counting_sort(arr):
#      min_value = min(arr)
#      max_value = max(arr)
#      counts = [0] * (max_value - min_value + 1)
#      for value in arr:
#          counts[value - min_value] += 1
#      for i in range(1, len(counts)):
#          counts[i] += counts[i - 1]
#      sorted_arr = [0] * len(arr)
#      for value in arr:
#          index = counts[value - min_value] - 1
#          sorted_arr[index] = value
#          counts[value - min_value] -= 1
#      return sorted_arr
# print(counting_sort(arr=[414,21414,41145,-123,21441,-2,0,123]))


#HUMAN
# def counting_sort(arr):
#    min_value = min(arr)
#    max_value = max(arr)
#    support=[0 for i in range(max_value-min_value+1)]
#
#    for i in arr:
#        support[i-min_value]+=1
#    index=0
#    for i in range(len(support)):
#        for el in range(support[i]):
#            arr[index]=i+min_value
#            index+=1
#    return arr
# print(counting_sort(arr=[123,535,-1123,-2,0,123]))


# def counting_sort(arr):
#     max_value = max(arr)
#     count = [0] * (max_value + 1)
#     for num in arr:
#         count[num] += 1
#     for i in range(1, len(count)):
#         count[i] += count[i-1]
#     output = [0] * len(arr)
#     for num in reversed(arr):
#         output[count[num]-1] = num
#         count[num] -= 1
#     return output
#
# arr = [4, 2, 1, 5, 6, 3,]
# sorted_arr = counting_sort(arr)
# print(sorted_arr)
#
# def radix_sort(arr):
#     max_num = max(arr)
#     exp = 1
#     while max_num // exp > 0:
#         counting_sort(arr, exp)
#         exp *= 10
#     return arr
#
# def counting_sort(arr, exp):
#     n = len(arr)
#     output = [0] * n
#     count = [0] * 10
#     for i in range(n):
#         index = arr[i] // exp
#         count[index % 10] += 1
#     for i in range(1, 10):
#         count[i] += count[i-1]
#     i = n - 1
#     while i >= 0:
#         index = arr[i] // exp
#         output[count[index % 10] - 1] = arr[i]
#         count[index % 10] -= 1
#         i -= 1
#     for i in range(n):
#         arr[i] = output[i]
#
# arr = [170, 45, 75, 90, 802, 24, 2, 66]
# sorted_arr = radix_sort(arr)
# print(sorted_arr)


# def counting_sort(arr):
#     count = [0] * (max(arr) + 1)
#     print(count)
#     for i in arr:
#         count[i] += 1
#     for i in range(len(count)):
#         if count[i] > 0:
#             print((str(i) + ' ') * count[i], end='')
# counting_sort(arr = [9,8,7,6,5,4,3,2,1])
# print("\n--------------")


# def countingSort(array):
#     size = len(array)
#     output = [0] * size
#
#     # Initialize count array
#     count = [0] * 10
#     print(count)
#     print("------")
#     # Store the count of each elements in count array
#     for i in range(0, size):
#         count[array[i]] += 1
#     print(count)
#     print("------")
#     # Store the cummulative count
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#     print(count)
#     print("------")
#     # Find the index of each element of the original array in count array
#     # place the elements in output array
#     i = size - 1
#     while i >= 0:
#         output[count[array[i]] - 1] = array[i]
#         count[array[i]] -= 1
#         i -= 1
#     print(count)
#     print("------")
#     print(array)
#     print("------")
#     # Copy the sorted elements into original array
#     for i in range(0, size):
#         array[i] = output[i]
#     print(array)
#     print("------")
#
# data = [4, 2, 2, 8, 3, 3, 1]
# countingSort(data)
# print("Sorted Array in Ascending Order: ")
# print(data)


# def counting_sort(arr):
#     # Знаходимо максимальне та мінімальне значення у списку
#     max_val = max(arr)
#     min_val = min(arr)
#
#     # Ініціалізуємо список лічильників з розміром, що дорівнює різниці між
#     # максимальним та мінімальним значеннями, плюс одиниця для нульового елементу
#     counts = [0] * (max_val - min_val + 1)
#
#     # Рахуємо кількість входжень кожного значення в список
#     for num in arr:
#         counts[num - min_val] += 1
#
#     # Ініціалізуємо змінну для зберігання відсортованого списку
#     sorted_arr = []
#
#     # Проходимо по списку лічильників та додаємо відповідну кількість елементів до відсортованого списку
#     for i in range(len(counts)):
#         sorted_arr += [i + min_val] * counts[i]
#
#     return sorted_arr
# print(counting_sort(arr=[9,8,7,6,5,4,3,2,1]))


def countingSort(array, place=1):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
data = [9,8,7,6,5,4,3,2,1]
countingSort(data)
print(data)

def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
array = [121, 432, 564, 23, 1, 45, 788]
radixSort(array)
print(array)