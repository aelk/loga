from bisect import bisect_left

def search(arr, key, low = 0, high = None):
    if high is None:
        high = len(a)
    pos = bisect_left(arr, key, low, high)
    if arr[pos] == key:
    	return pos
    else:
    	return -1
