def insertionSort(arr):
    for i in range(0, len(arr)):
        temp = arr[i]
        while (i > 0) and (temp < arr[i-1]):
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = temp
