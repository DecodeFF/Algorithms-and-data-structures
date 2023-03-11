def merge_sort(arr):
    sorted_arr = []
    i=j=0
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            sorted_arr.append(sorted_left[i])
            i += 1
        else:
            sorted_arr.append(sorted_right[j])
            j += 1

    sorted_arr.extend(sorted_left[i:])
    sorted_arr.extend(sorted_right[j:])

    return sorted_arr

print(merge_sort(arr = [5, 2, 9, 1, 5, 6, 8, 3,-1]))