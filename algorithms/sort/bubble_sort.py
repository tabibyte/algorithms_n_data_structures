def Bubble(arr):
    n = len(arr)
    for j in range(n):
        for i in range(n-1-j):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    return arr


array = [1, 5, 3, 2, 4, 7, 6, 8, 3, 0, 4]
print(Bubble(array))

