import math


def Balls(arr) -> int:
    jump = math.floor(math.sqrt(len(arr)))
    i = 0
    while arr[i] == 0:
        i += jump
    i -= jump
    j = 0
    while j < jump and i + j < len(arr):

        if arr[i+j] == 0:
            j += 1
        else:
            return i + j
            break
    return i + jump


array = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(Balls(array))
