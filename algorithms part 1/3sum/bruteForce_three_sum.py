import random as r


def count(a): #a is a list
    n = len(a)
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i]+a[j]+a[k] == 0:
                    count += 1
    return count

test_array = [30, -40, -20, -10, 40, 0, 10, 5]
result = count(test_array)
print(result)
