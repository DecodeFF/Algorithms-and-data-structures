import statistics
numbers = [31,414,124,-13,41241,22122,-1]
def quick_sort(numbers):
    if len(numbers) >= 1:
        pivot = numbers[0]
        left = []
        right = []
        for i in range(1, len(numbers)):
            if numbers[i] < pivot:
                left.append(numbers[i])
            else:
                right.append(numbers[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return numbers
print(quick_sort(numbers))
print("---------------")
def ordinal_statistics(numbers):
    try:
        sorted_numbers = sorted(numbers)
        lowest = sorted_numbers[0]
        highest = sorted_numbers[-1]
        median=statistics.median(numbers)
        return lowest, highest, median
    except IndexError:
        print("пустий масив")

numbers = [31,414,124,-13,41241,22122,-1]
lowest, highest, median = ordinal_statistics(numbers)
print("найменше число:", lowest)
print("найбільше число:", highest)
print("медіана:", median)


