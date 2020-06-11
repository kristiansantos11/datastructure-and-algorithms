from stopwatch import Stopwatch
import random

def count(a): #a is a list
    n = len(a)
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i]+a[j]+a[k]) == 0:
                    count += 1
    return count

test_array = [random.randint(-50, 50) for x in range(0, 250)]
print(test_array)
stopwatch = Stopwatch()
stopwatch.start()
print("There are " + str(len(test_array)) + " inputs")
result = count(test_array)
stopwatch.stop()
print(result)
print("Program took " + str(stopwatch))
