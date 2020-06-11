from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        if item == pivot:
            same.append(item)
        if item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)
