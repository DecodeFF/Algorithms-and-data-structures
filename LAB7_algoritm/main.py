
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


def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    print(count)
    for i in arr:
        count[i] += 1
    for i in range(len(count)):
        if count[i] > 0:
            print((str(i) + ' ') * count[i], end='')
counting_sort(arr = [9,8,7,6,5,4,3,2,1])
print("\n--------------")
def radix_sort(arr):
    RADIX = max(arr)+1
    max_digit = len(str(max(arr)))
    for i in range(max_digit):
        buckets = [[] for _ in range(RADIX)]
        for num in arr:
            digit = (num // RADIX ** i) % RADIX
            buckets[digit].append(num)
        print(buckets)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    print(arr)

sorted_nums = radix_sort(arr=[170, 45, 75, 90, 802, 24, 2, 66])