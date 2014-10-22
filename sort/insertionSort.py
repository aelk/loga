def sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        while (i > 0) and (temp < arr[i-1]):
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = temp
