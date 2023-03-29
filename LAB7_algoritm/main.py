
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
#def counting_sort(arr):
#    min_value = min(arr)
#    max_value = max(arr)
#    support=[0 for i in range(max_value-min_value+1)]
#    print(support)
#    for i in arr:
#        support[i-min_value]+=1
#    index=0
#    for i in range(len(support)):
#        for el in range(support[i]):
#            arr[index]=i+min_value
#            index+=1
#    return arr
#print(counting_sort(arr=[123,535,-1123,-2,0,123]))


#def countsort(A, k):
    # создает целочисленный список размера `n` для хранения отсортированного списка
#    output = [0] * len(A)
    # создает целочисленный список размером `k + 1`, инициализированный всеми нулями
#    freq = [0] * (k + 1)
#    print(freq)

    # , используя значение каждого элемента в списке ввода в качестве индекса,
    # сохраняет счетчик каждого целого числа в `freq[]`
#    for i in A:
#        freq[i] = freq[i] + 1
#    print(freq)

    # вычисляет начальный индекс для каждого целого числа
#    total = 0
#    for i in range(k + 1):
#        oldCount = freq[i]
#        freq[i] = total
#        total += oldCount

    # копирует в список выходов, сохраняя порядок входов с одинаковыми ключами
#    for i in A:
#        output[freq[i]] = i
#        freq[i] = freq[i] + 1

    # скопировать список вывода обратно в список ввода
#    for i in range(len(A)):
 #       A[i] = output[i]


#if __name__ == '__main__':
 #   A = [4, 2, 10, 10, 1, 4, 2, 1, 10,]

    # диапазон элементов списка
 #   k = 10

 #   countsort(A, k)
 #   print(A)

def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    print(count)
    for i in arr:
        count[i] += 1
    print(count)
    for i in range(len(count)):
        if count[i] > 0:
            print((str(i) + ' ') * count[i], end='')
counting_sort(arr = [9,8,7,6,5,4,3,2,1])