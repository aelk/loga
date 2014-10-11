def bubbleSort(arr, len):
    changed = True
    while changed:
        changed = False
        for i in range(1, len):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                changed = True
    return arr
    
