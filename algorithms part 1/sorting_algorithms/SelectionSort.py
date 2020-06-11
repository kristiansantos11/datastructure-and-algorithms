def selection_sort(array):
    n = len(array)
    for x in range(n):
        for i in range(x+1, n):
            if array[x] > array[i]:
                array[x], array[i] = array[i], array[x]
    return array
