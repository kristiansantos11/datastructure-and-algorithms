def bubble_sort(array):     # Code from RealPython.
    n = len(array)          # len() function is expensive in number of operations. Use it once.
    for i in range(n):
        sort_success = True
        for j in range(n - i - 1):  # Quite complicated. It pushes the highest numbers to the rightmost side of array
            if array[j] > array[j + 1]:     # Swap the two values if condition is satisfied.
                array[j], array[j + 1] = array[j + 1], array[j]
                sort_success = False
        if sort_success:
            break
    return array

'''
size = 10
arrayInt = [randint(0, size) for i in range(0, size)]
print(bubble_sort(arrayInt))
'''
'''
# If you have stopwatch.py installed. Use the client below to benchmark this algorithm.
stopwatch = Stopwatch()
n_array = [10, 100, 1000, 2000]
for x in n_array:
    arrayInt = [randint(0, x) for i in range(0, x)]
    stopwatch.start()
    print(bubble_sort(arrayInt))
    stopwatch.stop()
    print(f"Process took: {stopwatch}")
    stopwatch.reset()
'''

