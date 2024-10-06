import math


def BinarySearch(arr, n) -> bool:
    low = 0
    high = len(arr)

    while low < high:
        middle = math.floor(low + (high - low)/2)
        value = arr[middle]
        if n == value:
            return True
        elif n > value:
            low = middle + 1
        else:
            high = middle
    return False


array = [3, 4, 5, 7, 8, 9]
num = 2
print(BinarySearch(array, num))
